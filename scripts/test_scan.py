"""Self-check: synthetic prices → is_dip / metrics behave as documented."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
import pandas as pd
from scan import DD_MIN, drop_reasons, flag_dips, metrics

idx = pd.bdate_range("2023-01-01", periods=400)
spy = pd.Series(np.linspace(100, 150, 400), idx)          # steady up
vol = pd.Series(1e6, idx)

def series(path):
    return pd.Series(path, idx)

# fast dip: ran to 200 then dropped 15%, still above SMA200
fast = series(np.r_[np.linspace(100, 300, 380), np.linspace(300, 260, 20)])
# slow dip: sagged from 100 to 60 over the whole window
slow = series(np.linspace(100, 60, 400))
# leader: up faster than SPY
lead = series(np.linspace(100, 300, 400))
# fell with the market only: flat vs SPY (identical path), so rs_spy_3m == 0
same = spy.copy()

df = pd.DataFrame({k: metrics(v, vol, spy) for k, v in
                   dict(fast=fast, slow=slow, lead=lead, same=same).items()}).T
df.insert(0, "theme", ["a", "b", "a", "b"])
df = flag_dips(df)

assert df.loc["fast", "dd_52w"] <= DD_MIN and df.loc["fast", "vs_sma200"] > 0
assert df.loc["fast", "is_dip"]
assert df.loc["slow", "vs_sma200"] < 0 and df.loc["slow", "is_dip"]
assert not df.loc["lead", "is_dip"] and df.loc["lead", "rs_spy_3m"] > 0
assert not df.loc["same", "is_dip"]                       # not worse than SPY → not a dip
assert not df.loc["fast", "stabilizing"]                  # still falling
assert df.loc["slow", "dip_score"] >= 0 and np.isnan(df.loc["lead", "dip_score"])
assert 0 <= df.loc["slow", "dd_pctile"] <= 0.05           # at its own worst → low pctile
assert df.index[0] in ("fast", "slow")                    # dips sort first
assert df.loc["fast", "is_candidate"] and df.loc["slow", "is_candidate"] and not df.loc["lead", "is_candidate"]
assert df.loc["fast", "theme_score"] == df.loc["fast", "dip_score"]   # only dip in its theme
# drop log: every non-candidate gets exactly one row naming the leg it failed; candidates get none
dr = drop_reasons(df)
assert set(dr.index) == set(df.index[~df.is_candidate]) == {"lead", "same"}
assert dr.loc["lead", "stage"] == "2 not a dip" and "not lagging SPY" in dr.loc["lead", "reason"]
assert "not deep" not in dr.loc["lead", "reason"] or df.loc["lead", "vs_sma200"] >= 0
assert "not lagging SPY" in dr.loc["same", "reason"]
f = df.loc["fast"]
assert abs(f.tp_pct - (300 / 260 - 1)) < 1e-9                # TP = back to the 52w high
assert f.sl_pct < 0 and abs(f.rr - f.tp_pct / -f.sl_pct) < 1e-9
assert abs(f.dip_low_pct) < 1e-9                             # fast is sitting on its dip low
assert abs(f.size_1pct * -f.sl_pct - 0.01) < 1e-9

# consolidate: parse + bucket
import tempfile
from consolidate import parse, bucket, price_score
tmp = Path(tempfile.mkdtemp()) / "b.md"
tmp.write_text("| 1 | NLR | 8 |\n| 2 | **URA** | 7 |\n| 3 | GLD | 7.5 |\n")
try:
    parse(tmp, {"NLR", "URA", "GLD"}); raise SystemExit("parse should reject dropped rows")
except AssertionError:
    pass
assert parse(tmp, {"NLR"}) == {"NLR": 8}
# E is thin (rr < THIN_RR): wtd 7.5 - 1 = 6.5, so it sorts below B and can never be a buy.
sc = pd.DataFrame({"cause": [8, 8, 3, 7, 8], "catalyst": [7, 7, 9, 5, 7],
                   "stabilizing": [False, False, True, False, False],
                   "veto": [False, False, True, False, False],
                   "theme": ["nuc", "nuc", "clean", "clean", "nuc"],
                   "wtd": [8.0, 7.0, 6.0, 5.0, 7.5],
                   "rr": [2.0, 2.0, 2.0, 2.0, 1.0]}, index=list("ABCDE"))
b = bucket(sc)
assert list(b.index) == list("ABECD")                      # sorted by wtd after the thin penalty
assert list(b.thin) == [False, False, True, False, False]
assert list(b.wtd) == [8.0, 7.0, 6.5, 6.0, 5.0]            # thin costs exactly 1 point
assert list(b.wtd_rank) == [1, 2, 3, 4, 5]
assert list(b.theme_rank) == [1, 2, 3, 0, 1]
assert list(b.bucket) == ["buy", "alt", "watch", "avoid", "watch"]   # E qualifies on every leg but thin
from consolidate import bucket_reasons
why = bucket_reasons(b)
assert why["A"].startswith("buy:") and "behind A" in why["B"]          # alt names the theme leader that blocks it
assert why["E"] == "watch: thin: R/R 1.00 < 1.3"                       # the one failing leg, nothing else
assert why["C"].startswith("cause veto") and "cause 7" not in why["D"] and "catalyst 5" in why["D"]
# core: broad funds need cause + necessity, not a catalyst. Replays 2026-09-26 (XLU/IGF/PAVE/GLD) plus edge cases.
sc = pd.DataFrame({"cause":      [10, 8, 8, 8, 8, 6, 8, 8],
                   "necessity":  [10, 10, 10, 6, 9, 10, 7, 9],
                   "catalyst":   [6, 6, 6, 7, 3, 6, 3, 6],
                   "stabilizing": [False] * 8,
                   "veto":       [False] * 8,
                   "theme": ["utilities", "grid/infra", "grid/infra", "gold", "space", "staples", "banks", "materials"],
                   "wtd":        [8.45, 7.85, 7.25, 7.10, 7.0, 6.9, 6.8, 6.7],
                   "rr":         [2.9, 2.5, 1.6, 2.5, 3.0, 2.0, 2.0, 1.1],
                   "sl_pct": [-0.06, -0.04, -0.08, -0.10, -0.12, -0.05, -0.08, -0.09],
                   "tp_pct": [0.18, 0.10, 0.12, 0.26, 0.56, 0.10, 0.16, 0.10]}, index=["XLU", "IGF", "PAVE", "GLD", "UFO", "XLP", "KBE", "XLB"])
b = bucket(sc)
assert b.bucket["XLU"] == "core" and b.bucket["IGF"] == "core"  # the two broad funds the catalyst gate kept on watch
assert b.bucket["PAVE"] == "alt"                                # qualifies, but IGF leads grid/infra
assert b.bucket["GLD"] == "buy"                                 # catalyst 7: the buy path wins over core
assert b.bucket["UFO"] == "watch"                               # narrow theme: necessity 9 alone never makes core
assert b.bucket["XLP"] == "watch"                               # cause 6 < 7: necessity cannot carry a weak cause
assert b.bucket["KBE"] == "watch"                               # necessity 7 < CORE_NECESSITY
assert b.bucket["XLB"] == "watch"                               # thin (R/R < 1.3) is never core
why = bucket_reasons(b)
assert why["XLU"].startswith("core:") and "behind IGF" in why["PAVE"]
assert "necessity 7 < 8" in why["KBE"] and "thin" in why["XLB"] and "cause 6 < 7" in why["XLP"]
sc.loc["XLU", ["cause", "veto"]] = [3, True]
assert bucket(sc).bucket["XLU"] == "avoid"                      # the cause veto still overrides everything
from consolidate import deploy as _deploy
assert list(_deploy(b, 10000).index) == ["GLD"]                 # core stays out of the risk-parity split
# price lens is arithmetic now: same inputs must always give the same score
assert price_score(.01, .10, True) == 10      # worst 1%, 12m intact, bouncing
assert price_score(.30, -.50, False) == 1     # ordinary patch, trend broken, still falling
assert price_score(.015, .08, False) == 8     # deep + trend, no bounce yet
assert price_score(.015, .08, True) == 10     # the bounce is worth exactly 2
assert all(1 <= price_score(a, b, c) <= 10    # never leaves the 1-10 scale
           for a in (0, .02, .05, .10, .25, 1) for b in (-1, -.35, -.15, 0, 1) for c in (True, False))

from consolidate import deploy
d = deploy(pd.DataFrame({"bucket": ["buy", "buy", "watch"], "sl_pct": [-0.1, -0.2, -0.1], "tp_pct": [0.3, 0.3, 0.3]}, index=list("XYZ")), 30000)
assert list(d.index) == ["X", "Y"] and list(d.usd) == [20000, 10000]        # each loses the same $ at its stop
assert d.loss_at_sl.sum() == -4000 and d.gain_at_tp.sum() == 9000
# memo rendering: the three ways 2026-09-28's memo broke on GitHub
from check_memo import render_problems
good = "| a | b |\n|---|---|\n| 1 | $5 |\n\ntext\n"
assert render_problems(good) == []
assert "delimiter" in render_problems("| a | b |\n|---|---|---|\n| 1 | 2 |\n")[0][1]      # 2 vs 3 columns
assert render_problems("| a |\n|---|\n| 1 |\nMax loss\n")[0][0] == 4                     # text folded into table
assert render_problems("spend $1.5T request, RTX $289B backlog\n") == []               # closer before a digit
assert render_problems("costs $5 and $10\n") == []
assert "math" in render_problems("the $x$ term\n")[0][1]
assert render_problems("the \\$x\\$ term and `$a$`\n") == []                          # escaped / in code
# independence: memo parsing, copy detection, catalyst floor, run ids, file ownership
import check_memo as cm, carry_forward as cf, run_id
memo = ("| my # | ETF | theme | cause | need | cat | basket | why (1 line) |\n|---|---|---|---|---|---|---|---|\n"
        + "".join(f"| {i} | T{chr(65+i)} | x | 7 | 8 | {6+i%2} | 5 | r{i} |\n" for i in range(10)))
rows = cm.memo_rows(memo)
assert len(rows) == 10 and rows["TA"] == {"cause": "7", "necessity": "8", "catalyst": "6", "basket": "5", "why": "r0"}
cm.errors.clear(); cm.other_runs = lambda run: {"prev": rows}
cm.copy_check("2026-10-06", rows)                                  # identical judged scores -> copied
assert cm.errors and "not an independent run" in cm.errors[0]
cm.errors.clear()
tweak = {t: dict(r, cause=str(int(r["cause"]) + (i % 4 > 0))) for i, (t, r) in enumerate(rows.items())}
cm.copy_check("2026-10-06", tweak)                                 # 3 of 10 the same (30%) -> independent
assert not cm.errors
cm.warns.clear()
close = {t: dict(r, basket=str(int(r["basket"]) + (i < 2))) for i, (t, r) in enumerate(rows.items())}
cm.copy_check("2026-10-06", close)                                 # 8 of 10 (80%) -> warning, not a failure
assert not cm.errors and cm.warns and "unusually close" in cm.warns[0]
cf.load = lambda: [dict(theme="nuclear", match="Cameco", event="Cameco Q3 results", date="2026-10-30",
                        confirmed_by="x", verified_on="2026-10-01"),
                   dict(theme="india", match="RBI", event="RBI MPC policy decision", date="2026-10-07",
                        confirmed_by="x", verified_on="2026-10-01"),
                   dict(theme="solar", match="Solar IV", event="USITC vote", date="2026-12-14",
                        confirmed_by="x", verified_on="2026-10-01"),
                   dict(theme="housing", match="DHI", event="DHI results", date="2026-10-29",
                        confirmed_by="x", verified_on="2026-10-20")]
fl = cf.floors("2026-10-05")
assert set(fl) == {"nuclear"}       # MPC is symmetric; Solar IV is 70 days out; DHI was not known on 10-05
assert set(cf.floors("2026-10-05-r2")) == {"nuclear"}             # a rerun id reads as its date
cm.errors.clear(); cm.floor_check("2026-10-05", {"NLR": ("nuclear", "6", "two-way print"), "URA": ("nuclear", "7", "")})
assert len(cm.errors) == 1 and "NLR catalyst 6" in cm.errors[0]
cm.errors.clear(); cm.floor_check("2026-10-05", {"NLR": ("nuclear", "5", "CONTRADICTED: cameco.com moved it")})
assert not cm.errors
assert cm.run_of("output/2026-10-05/scores.csv") == "2026-10-05" and cm.run_of("log/2026-10-05-r2-lite.md") == "2026-10-05-r2"
assert cm.run_of("log/catalysts.md") is None
import tempfile
from pathlib import Path as _P
_d = _P(tempfile.mkdtemp()); (_d / "a.md").write_text("# memo\n"); (_d / "b.md").write_text("> Run by: X (x) — lite\n\n# memo\n")
cm.errors.clear(); cm.provenance_check("2026-10-06", [_d / "a.md", _d / "b.md"])
assert len(cm.errors) == 1 and "a.md" in cm.errors[0] and "b.md" not in cm.errors[0]
cm.errors.clear(); cm.provenance_check("2026-10-05", [_d / "a.md"])          # older runs were annotated by hand
assert not cm.errors
run_id.ROOT = _P(tempfile.mkdtemp()); (run_id.ROOT / "log").mkdir(); (run_id.ROOT / "output").mkdir()
assert run_id.next_run_id("2026-10-06") == "2026-10-06"
(run_id.ROOT / "log" / "2026-10-06-lite.md").write_text("x")
assert run_id.next_run_id("2026-10-06") == "2026-10-06-r2"
(run_id.ROOT / "output" / "2026-10-06-r2").mkdir()
assert run_id.next_run_id("2026-10-06") == "2026-10-06-r3"
print("ok")
