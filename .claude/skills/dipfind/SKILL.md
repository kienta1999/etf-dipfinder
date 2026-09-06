---
name: dipfind
description: Find and rank sector / thematic ETFs that are in a dip — below their 200-day SMA or ≥10% off the 52-week high AND lagging SPY over 3 months — then work out WHY each is down and sort them into rotation dips (buy candidates), fundamental breaks (avoid), or unclear. Runs the deterministic scan in etf-dipfinder/scripts/scan.py, web-checks the top dips, and writes a dated memo to log/. Use this whenever the user asks what ETFs or sectors are "on sale", "beaten down", "lagging", "oversold", "which sectors are dipping", "buy the dip" for ETFs/sectors/themes (semis, nuclear, defense, biotech, clean energy, crypto, gold miners, China, etc.), or wants to know where money is rotating — even if they don't say "ETF" or "/dipfind". For single-stock dips use conviction-pick-sp500's /stock-pick-dip instead.
---

# dipfind — rank ETF dips, separate dips from falling knives

The script does the arithmetic; this skill exists for the one thing arithmetic
can't do. An ETF that is 25% off its high is either **on sale** (money rotated
into a hotter theme, the theme's thesis is intact, it will mean-revert) or
**broken** (the thesis itself changed — regulation, demand collapse, a key
holding blew up — and cheap keeps getting cheaper). The numbers look identical.
Only reading the news tells them apart, and that's the whole job.

## 1. Run the scan

```
cd etf-dipfinder && uv run python scripts/scan.py
```

(Use the full path if unsure of cwd — the shell may already be inside
`etf-dipfinder/`, in which case `cd etf-dipfinder` fails.)

It prints two blocks and writes `data/scan.csv`:

- **DIPS** — ETFs with `is_dip = (price < SMA200 OR dd_52w ≤ −10%) AND rs_spy_3m < 0`,
  sorted by `dip_score` (0 = most beaten up on depth + relative weakness + trend).
- **LEADERS** — top 8 by `rs_spy_3m`. Not candidates; they're context.

If the script errors on a delisted ticker, that's already handled (it prints
`skip X` and continues). Only investigate if the CSV is missing or nearly empty.

## 2. Read the regime first

Look at LEADERS before any dip. The question is: *where did the money go?*

Dips usually come in clusters that mirror the leaders. If crypto and biotech
lead while nuclear, defense, space and rare earths all sit in the dip list
together, that's one rotation, not five separate problems — the AI-physical
trade unwinding into risk-on. A cluster like that is much more likely to be
"rotation" than a lone ETF falling while its siblings hold up (which smells
idiosyncratic and deserves a harder look).

Write two lines on this. It frames every bucket decision below.

## 3. Check the top ~10 dips

For each, one web search — `"<TICKER> ETF" <theme> selloff <Month YYYY>` — and
read enough to answer: *did the thesis change, or just the flows?*

| bucket | means | typical evidence |
|---|---|---|
| **rotation** | thesis intact, money left for something hotter | "profit-taking after big run", rate moves, risk-on/off, sector rotation, macro fear, one bad print at a top holding |
| **break** | thesis impaired | policy reversal (subsidy repeal, export ban), demand collapse, tech obsolescence, fraud/blowup at a top-3 holding, the theme's core commodity structurally oversupplied |
| **unclear** | one search didn't settle it | say so; don't guess |

Then cross-check the row's numbers — they modulate confidence, not the bucket:

- `dd_pctile < 0.10` — this drawdown is in the worst decile of *this ETF's own
  3-year history*. Real event, not normal noise. (XBI at −15% is a Tuesday;
  XLP at −10% is news.) `dd_z` says the same thing in vol units.
- `stabilizing` (10-day return > 0) — the bounce has started. Without it,
  even a rotation dip is still a knife; note it as *watch*, not *buy*.
- `days < 250` — young ETF (DRAM, AIPO…). Its SMA200 / 52w numbers are
  since-inception and mean less. Say so.
- `rs_spy_12m` strongly positive while `rs_spy_3m` negative — a leader that's
  resting, the most common good dip shape.

## 4. Write the memo and log it

Append to `log/YYYY-MM-DD.md` (create if missing). Logging is what makes the
skill improvable — in three months you can check which buckets were right.

```
# dipfind YYYY-MM-DD

Regime: <2 lines>

| # | ETF | theme | dd_52w | vs_sma200 | rs_spy_3m | stab | bucket | why (1 line) |
|---|-----|-------|--------|-----------|-----------|------|--------|--------------|
| 1 | KWEB | china | -36% | -13% | -6% | no | rotation | Tariff headline + Mag7 rotation; earnings at top holdings fine |
| 2 | TAN  | clean | -35% | -13% | -30% | no | break | IRA credits repealed in July bill; thesis needs policy reversal |
...

Buy candidates (rotation + stabilizing): ...
Watch (rotation, still falling): ...
Avoid (break): ...
```

Keep the "why" to one line — the point is the bucket, not a research report.
No price targets, no position sizes; that's the user's call.
