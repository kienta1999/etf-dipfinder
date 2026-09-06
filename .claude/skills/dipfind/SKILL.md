---
name: dipfind
description: Rank dipped ETFs from the deterministic scan (below SMA200 or ≥10% off 52w high, AND lagging SPY over 3m). Runs scripts/scan.py, then web-checks WHY each top dip is down and buckets it as rotation dip (buy candidate) / fundamental break (avoid) / unclear. Use when the user asks "what ETFs are on sale", "find ETF dips", "rank the dips", or invokes /dipfind.
---

# dipfind — rank ETF dips, separate dips from falling knives

The script does the numbers. You do the one thing it can't: read the world
and decide whether each dip is **rotation** (money left for a hotter theme,
business intact) or **break** (the theme's thesis is impaired).

## Steps

1. Run: `uv run python scripts/scan.py` (from `etf-dipfinder/`). It prints the
   top 15 dips and the 8 leaders, and writes `data/scan.csv`.
2. Note the **regime** from the leaders block: what is money rotating *into*?
   A dip in a theme that's the mirror image of the leaders (e.g. clean energy
   down while oil leads) is a rotation dip by construction.
3. For each of the top ~10 dips, ONE web search: `"<TICKER> ETF" <theme> selloff <Month YYYY>`.
   Bucket it:
   - **rotation** — macro/rate/sentiment/sector rotation, theme thesis intact
   - **break** — thesis impaired (regulation, demand collapse, tech obsolescence, key holding blew up)
   - **unclear** — couldn't tell in one search; say so
4. Cross-check the numbers per ETF:
   - `dd_pctile` < 0.10 → unusually deep *for this ETF* (real event, not normal noise)
   - `dd_z` — depth in vol units; XBI at −15% is noise, XLP at −10% is not
   - `stabilizing` (10d return > 0) → bounce started; otherwise still a knife
   - `days` < 250 → young ETF, SMA200/52w stats are since-inception, weight less
5. Write the memo below and append it to `log/YYYY-MM-DD.md` so hit-rate can be
   checked later.

## Memo format

```
Regime: <2 lines — what's leading, what's lagging>

| # | ETF | theme | dd_52w | vs_sma200 | rs_spy_3m | stab | bucket | why (1 line) |
...

Buy candidates (rotation + stabilizing): ...
Watch (rotation, still falling): ...
Avoid (break): ...
```

Keep it short. No price targets, no position sizing — that's the user's call.
