"""Merge panel ballots → output/<DATE>/scores.csv. Usage: uv run python scripts/consolidate.py 2026-09-06

First run freezes data/scan.csv into output/<DATE>/scan.csv so later rescans never change this date's scores."""
import re, shutil, sys
from pathlib import Path
import pandas as pd

W = {"cause": .30, "necessity": .20, "catalyst": .20, "basket": .15, "price": .15}
VETO = 3  # cause <= VETO → avoid

def parse(p, candidates):
    rows = re.findall(r"^\|\s*\d+\s*\|\s*([A-Z]+)\s*\|\s*(\d+)\s*\|", p.read_text(), re.M)
    d = {t: int(s) for t, s in rows}
    assert set(d) >= candidates, f"{p.name}: ballot rows not parsed for {sorted(candidates - set(d))}"
    return d

def bucket(df):
    """buy = cause ≥ 7 and (stabilizing or catalyst ≥ 7) and first eligible in theme; alt = same but not first;
    avoid = veto; else watch. theme_rank counts non-vetoed rows only (0 = vetoed)."""
    df = df.copy()
    ok = ~df.veto
    df["theme_rank"] = 0
    df.loc[ok, "theme_rank"] = df[ok].groupby("theme").cumcount() + 1
    qual = ok & (df.cause >= 7) & (df.stabilizing.astype(bool) | (df.catalyst >= 7))
    df["bucket"] = "watch"
    df.loc[qual, "bucket"] = "alt"
    df.loc[qual & (df.theme_rank == 1), "bucket"] = "buy"
    df.loc[df.veto, "bucket"] = "avoid"
    return df

def main(date):
    out = Path(__file__).resolve().parent.parent / "output" / date
    snap = out / "scan.csv"
    if not snap.exists():
        shutil.copy(out.parent.parent / "data" / "scan.csv", snap)
        print(f"froze data/scan.csv → {snap}")
    scan = pd.read_csv(snap, index_col=0)
    ballots = {l: out / f"score_{l}.md" for l in W if (out / f"score_{l}.md").exists()}
    cands = set(re.findall(r"^\|\s*\d+\s*\|\s*([A-Z]+)\s*\|", next(iter(ballots.values())).read_text(), re.M))
    df = pd.DataFrame({l: parse(p, cands) for l, p in ballots.items()})
    assert not df.isna().any().any(), f"missing scores:\n{df[df.isna().any(axis=1)]}"
    have = list(ballots)
    wsum = sum(W[l] for l in have)
    df["wtd"] = sum(df[l] * W[l] for l in have) / wsum
    df["veto"] = df.get("cause", pd.Series(10, index=df.index)) <= VETO
    df["dip_score"] = scan.dip_score.reindex(df.index)
    df["dip_rank"] = df.dip_score.rank(method="min").astype("Int64")
    df["stabilizing"] = scan.stabilizing.reindex(df.index)
    df["theme"] = scan.theme.reindex(df.index)
    for c in ["tp_pct", "sl_pct", "dip_low_pct", "rr", "size_1pct"]:
        if c in scan: df[c] = scan[c].reindex(df.index)
    df = df.sort_values("wtd", ascending=False)
    df.insert(0, "wtd_rank", range(1, len(df) + 1))
    df = bucket(df)
    df.to_csv(out / "scores.csv", float_format="%.2f")
    print(f"lenses: {have} (weights renormalised to {wsum:.2f})")
    print(df.to_string(float_format="{:.2f}".format))

if __name__ == "__main__":
    main(sys.argv[1])
