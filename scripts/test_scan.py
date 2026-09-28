"""Self-check: synthetic prices → is_dip / metrics behave as documented."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
import pandas as pd
from scan import DD_MIN, flag_dips, metrics

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
print("ok")
