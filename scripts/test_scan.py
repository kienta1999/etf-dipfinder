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
f = df.loc["fast"]
assert abs(f.tp_pct - (300 / 260 - 1)) < 1e-9                # TP = back to the 52w high
assert f.sl_pct < 0 and abs(f.rr - f.tp_pct / -f.sl_pct) < 1e-9
assert abs(f.dip_low_pct) < 1e-9                             # fast is sitting on its dip low
assert abs(f.size_1pct * -f.sl_pct - 0.01) < 1e-9

# consolidate: parse + bucket
import tempfile
from consolidate import parse, bucket
tmp = Path(tempfile.mkdtemp()) / "b.md"
tmp.write_text("| 1 | NLR | 8 |\n| 2 | **URA** | 7 |\n| 3 | GLD | 7.5 |\n")
try:
    parse(tmp, {"NLR", "URA", "GLD"}); raise SystemExit("parse should reject dropped rows")
except AssertionError:
    pass
assert parse(tmp, {"NLR"}) == {"NLR": 8}
sc = pd.DataFrame({"cause": [8, 8, 3, 7], "catalyst": [7, 7, 9, 5], "stabilizing": [False, False, True, False],
                   "veto": [False, False, True, False], "theme": ["nuc", "nuc", "clean", "clean"]}, index=list("ABCD"))
b = bucket(sc)
assert list(b.theme_rank) == [1, 2, 0, 1] and list(b.bucket) == ["buy", "alt", "avoid", "watch"]
from consolidate import deploy
d = deploy(pd.DataFrame({"bucket": ["buy", "buy", "watch"], "sl_pct": [-0.1, -0.2, -0.1], "tp_pct": [0.3, 0.3, 0.3]}, index=list("XYZ")), 30000)
assert list(d.index) == ["X", "Y"] and list(d.usd) == [20000, 10000]        # each loses the same $ at its stop
assert d.loss_at_sl.sum() == -4000 and d.gain_at_tp.sum() == 9000
print("ok")
