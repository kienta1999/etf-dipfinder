# etf-dipfinder

Scan ~115 liquid sector / thematic ETFs for dips.

```
uv sync
uv run python scripts/scan.py        # → data/scan.csv + top dips / leaders
uv run python scripts/test_scan.py   # self-check on synthetic prices
/dipfind                              # Claude: ranks + explains why each is down
```

`is_dip = (price < SMA200 OR dd_52w ≤ −10%) AND rs_spy_3m < 0`
— trend broken *or* sharp pullback, **and** lagging SPY (so a broad selloff
doesn't flag everything). Knobs at the top of `scripts/scan.py`.
