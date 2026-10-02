"""Merge panel ballots → output/<DATE>/scores.csv. Usage: uv run python scripts/consolidate.py 2026-09-06 [CAPITAL] [NLR,GLD,XLU]

Lite (no ballots, sizes straight off data/scan.csv): uv run python scripts/consolidate.py lite 100000 NLR

First run freezes data/scan.csv into output/<DATE>/scan.csv so later rescans never change this date's scores
(and data/drops.csv alongside it). Also writes output/<DATE>/buckets_why.csv: the rule leg behind every bucket."""
import re, shutil, sys
from pathlib import Path
import pandas as pd

W = {"cause": .30, "necessity": .20, "catalyst": .20, "basket": .15, "price": .15}
BALLOT_LENSES = ["cause", "necessity", "catalyst", "basket"]  # price is computed, not voted on


def price_score(dd_pctile, rs_spy_12m, stabilizing):
    """The price lens as lenses.md defines it, in arithmetic instead of a subagent's judgment.

    'Unusually cheap for THIS ETF' (depth vs its own history, not absolute drawdown - dip_score and
    rr already carry absolute depth), '12m trend intact', 'bounce started'. Scored by an LLM this
    swung 7 points across three runs on unchanged inputs (QTUM 6 -> 1 -> 8); here it cannot move
    unless the scan moves."""
    s = 5 if dd_pctile <= .02 else 4 if dd_pctile <= .05 else 3 if dd_pctile <= .10 else 2 if dd_pctile <= .25 else 1
    s += 3 if rs_spy_12m > 0 else 2 if rs_spy_12m > -.15 else 1 if rs_spy_12m > -.35 else 0
    s += 2 if stabilizing else 0
    return min(max(s, 1), 10)
VETO = 3  # cause <= VETO → avoid
THIN_RR = 1.3  # R/R = TP / 1.5 monthly sigma, i.e. dip depth in vol units; below this = thin: wtd −1 and never buy (still listed)
# Broad sector / infrastructure / gold funds: a temporary cause on something the world needs usually recovers; a dated
# catalyst only says *when*. They get their own path (bucket "core") that drops the catalyst/stabilizing leg and is held
# long term (rebalance bands, no stop). Narrow themes (space, nuclear, rare earths, solar, china…) keep the buy rule.
BROAD_THEMES = {"utilities", "grid/infra", "gold", "staples", "industrials", "materials", "realestate", "banks"}
CORE_NECESSITY = 8  # necessity >= this (with cause >= 7) makes a broad fund core

def parse(p, candidates):
    rows = re.findall(r"^\|\s*\d+\s*\|\s*([A-Z]+)\s*\|\s*(\d+)\s*\|", p.read_text(), re.M)
    d = {t: int(s) for t, s in rows}
    assert set(d) >= candidates, f"{p.name}: ballot rows not parsed for {sorted(candidates - set(d))}"
    return d

def bucket(df):
    """buy = cause ≥ 7 and (stabilizing or catalyst ≥ 7) and not thin and first eligible in theme; alt = same but not
    first; core = a BROAD_THEMES fund that is not a buy but has cause ≥ 7 and necessity ≥ CORE_NECESSITY, not thin, first
    in theme (no catalyst needed; a later-ranked sibling that qualifies the same way is alt); avoid = veto; else watch.
    thin (R/R < THIN_RR) costs 1 point of wtd and can't be a buy or core.
    theme_rank counts non-vetoed rows only (0 = vetoed). Sorts by wtd and (re)writes wtd_rank."""
    df = df.copy()
    df["thin"] = df.rr < THIN_RR
    df["wtd"] = df.wtd - df.thin
    df = df.sort_values("wtd", ascending=False)
    df["wtd_rank"] = range(1, len(df) + 1)
    ok = ~df.veto
    df["theme_rank"] = 0
    df.loc[ok, "theme_rank"] = df[ok].groupby("theme").cumcount() + 1
    qual = ok & ~df.thin & (df.cause >= 7) & (df.stabilizing.astype(bool) | (df.catalyst >= 7))
    necessity = df["necessity"] if "necessity" in df else pd.Series(0, index=df.index)
    core = ok & ~df.thin & df.theme.isin(BROAD_THEMES) & (df.cause >= 7) & (necessity >= CORE_NECESSITY)
    df["bucket"] = "watch"
    df.loc[qual | core, "bucket"] = "alt"
    df.loc[core & (df.theme_rank == 1), "bucket"] = "core"
    df.loc[qual & (df.theme_rank == 1), "bucket"] = "buy"     # the dated-catalyst path wins when both apply
    df.loc[df.veto, "bucket"] = "avoid"
    return df

def bucket_reasons(df):
    """Why each fund of a bucket() frame landed in its bucket — the failing (or deciding) legs, in words.
    Reads only columns bucket() already used; never feeds back into scores."""
    leader = df[df.theme_rank == 1].reset_index().groupby("theme")[df.index.name or "index"].first()
    necessity = df["necessity"] if "necessity" in df else pd.Series(0, index=df.index)
    out = {}
    for t, r in df.iterrows():
        if r.bucket == "avoid":
            out[t] = f"cause veto: cause {r.cause:g} <= {VETO}"
            continue
        if r.bucket == "buy":
            leg = "stabilizing" if bool(r.stabilizing) else f"catalyst {r.catalyst:g} >= 7"
            out[t] = f"buy: cause {r.cause:g} >= 7, {leg}, R/R {r.rr:.2f} >= {THIN_RR}, #1 in theme"
            continue
        if r.bucket == "core":
            out[t] = (f"core: broad theme, cause {r.cause:g} >= 7, necessity {necessity[t]:g} >= {CORE_NECESSITY}, "
                      f"R/R {r.rr:.2f} >= {THIN_RR}, #1 in theme")
            continue
        if r.bucket == "alt":
            out[t] = f"qualifies, but theme #{int(r.theme_rank)} behind {leader.get(r.theme, '?')} (one buy per theme)"
            continue
        legs = []
        if r.thin:
            legs.append(f"thin: R/R {r.rr:.2f} < {THIN_RR}")
        if r.cause < 7:
            legs.append(f"cause {r.cause:g} < 7")
        if not bool(r.stabilizing) and r.catalyst < 7:
            legs.append(f"no catalyst >= 7 (catalyst {r.catalyst:g}) and not stabilizing")
        if r.theme in BROAD_THEMES and necessity[t] < CORE_NECESSITY:
            legs.append(f"core path: necessity {necessity[t]:g} < {CORE_NECESSITY}")
        out[t] = "watch: " + "; ".join(legs) if legs else "watch"
    return pd.Series(out, name="why").reindex(df.index)

def deploy(df, capital, only=None):
    """Risk-parity split of `capital` across bucket == buy, or across `only` (the memo's final buys if it overrode
    the rule). Each position loses the same $ at its stop. Returns per-ETF $, loss at SL, gain at TP."""
    b = df[df.bucket == "buy"] if only is None else df.loc[only]
    w = (1 / -b.sl_pct); w = w / w.sum()
    out = pd.DataFrame({"usd": (capital * w).round(-2), "sl_pct": b.sl_pct, "tp_pct": b.tp_pct})
    out["loss_at_sl"] = (out.usd * out.sl_pct).round(-2)
    out["gain_at_tp"] = (out.usd * out.tp_pct).round(-2)
    return out

def main(date, capital=None, only=None):
    out = Path(__file__).resolve().parent.parent / "output" / date
    snap = out / "scan.csv"
    if not snap.exists():
        shutil.copy(out.parent.parent / "data" / "scan.csv", snap)
        print(f"froze data/scan.csv → {snap}")
        drops = out.parent.parent / "data" / "drops.csv"   # frozen with the scan it describes, never later
        if drops.exists():
            shutil.copy(drops, out / "drops.csv")
    scan = pd.read_csv(snap, index_col=0)
    ballots = {l: out / f"score_{l}.md" for l in BALLOT_LENSES if (out / f"score_{l}.md").exists()}
    cands = set(re.findall(r"^\|\s*\d+\s*\|\s*([A-Z]+)\s*\|", next(iter(ballots.values())).read_text(), re.M))
    df = pd.DataFrame({l: parse(p, cands) for l, p in ballots.items()})
    if "price_score" in scan:                      # scans written since the price lens became code
        df["price"] = scan.price_score.reindex(df.index)
    else:                                          # older frozen scans: recompute from their columns
        df["price"] = [price_score(scan.dd_pctile[t], scan.rs_spy_12m[t], bool(scan.stabilizing[t]))
                       for t in df.index]
    assert not df.isna().any().any(), f"missing scores:\n{df[df.isna().any(axis=1)]}"
    have = list(ballots) + ["price"]
    wsum = sum(W[l] for l in have)
    df["wtd"] = sum(df[l] * W[l] for l in have) / wsum
    df["veto"] = df.get("cause", pd.Series(10, index=df.index)) <= VETO
    df["dip_score"] = scan.dip_score.reindex(df.index)
    df["dip_rank"] = df.dip_score.rank(method="min").astype("Int64")
    df["stabilizing"] = scan.stabilizing.reindex(df.index)
    df["theme"] = scan.theme.reindex(df.index)
    for c in ["dd_52w", "tp_pct", "sl_pct", "dip_low_pct", "rr", "size_1pct"]:
        if c in scan: df[c] = scan[c].reindex(df.index)
    df.insert(0, "wtd_rank", 0)
    df = bucket(df)
    df.to_csv(out / "scores.csv", float_format="%.2f")
    pd.concat([df[["theme", "bucket"]], bucket_reasons(df)], axis=1).to_csv(out / "buckets_why.csv")
    print(f"lenses: {have} (weights renormalised to {wsum:.2f})")
    print(df.to_string(float_format="{:.2f}".format))
    core = list(df.index[df.bucket == "core"])
    if core:
        print(f"\ncore (broad funds, long-term holds — outside the risk-parity split, no stop; rebalance at ±25% of "
              f"target weight, exit only on a cause veto): {', '.join(core)}")
    if capital:
        d = deploy(df, capital, only)
        print(f"\ndeploy ${capital:,.0f} across buys (risk parity):")
        print(d.to_string(float_format="{:,.2f}".format))
        print(f"max loss {d.loss_at_sl.sum():,.0f}  max gain {d.gain_at_tp.sum():,.0f}")

if __name__ == "__main__":
    if sys.argv[1] == "lite":  # sizing without ballots: consolidate.py lite 100000 NLR,GLD
        scan = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "scan.csv", index_col=0)
        d = deploy(scan, float(sys.argv[2]), sys.argv[3].split(","))
        print(d.to_string(float_format="{:,.2f}".format))
        print(f"max loss {d.loss_at_sl.sum():,.0f}  max gain {d.gain_at_tp.sum():,.0f}")
        sys.exit()
    main(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else None, sys.argv[3].split(",") if len(sys.argv) > 3 else None)
