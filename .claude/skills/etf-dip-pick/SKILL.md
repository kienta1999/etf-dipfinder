---
name: etf-dip-pick
description: Find and rank sector / thematic ETFs that are in a dip — below their 200-day SMA or ≥10% off the 52-week high AND lagging SPY over 3 months — then decide which dips are worth buying. Runs the deterministic scan (scripts/scan.py), builds a dossier, fans out to five SEQUENTIAL Opus scoring panelists (cause, necessity, catalyst, basket, price), consolidates a weighted score plus the orchestrator's own rank, and writes a dated memo to log/. Use this whenever the user asks what ETFs or sectors are "on sale", "beaten down", "lagging", "oversold", "which sectors are dipping", "buy the dip" for ETFs/sectors/themes (semis, nuclear, defense, biotech, clean energy, crypto, gold miners, China, etc.), wants to know where money is rotating, or wants a quick single-agent pass ("quick etf-dip-pick") — even if they don't say "ETF" or "/etf-dip-pick". For single-stock dips use conviction-pick-sp500's /stock-pick-dip instead.
---

# etf-dip-pick — rank ETF dips, separate dips from falling knives

An ETF 25% off its high is either **on sale** (money rotated elsewhere, thesis intact) or
**broken** (the thesis changed). The scan can't tell; the panel can. Two modes:

- **quick** — orchestrator alone, one search per ETF, memo with buckets. ~5 min, cheap.
- **panel** (default when the user says "rank", "review", "which to buy") — quick pass becomes
  the dossier, then five Opus panelists score one criterion each, orchestrator consolidates.

The user is on a Pro plan. **Every panelist runs sequentially and writes its ballot to disk before
the next starts**, so a budget cutoff leaves finished work on disk and the run resumes from the
first missing `score_<lens>.md`. Never run panelists in parallel.

**No search cap here — full is the reliable mode, `/etf-dip-pick-lite` is the cheap one.** A panelist searches
until its facts are pinned and stops: it re-checks nothing it has already confirmed, and never searches to score
a fund whose theme is already covered by a sibling. Stop rule per lens — every score rests on a number or a dated
event the panelist can name, or the ballot says "unverified" and the score caps at 5.

## Phase 0 — scan

```
cd etf-dipfinder && uv run python scripts/scan.py     # full path if cwd is already inside
```

Prints CANDIDATES — every dip in the `TOP_THEMES` (15) themes whose best dip is deepest, grouped by theme — and
LEADERS, writes `data/scan.csv`. A theme = funds the same headline moves (URA/URNM/NLR; GLD/GDX/GDXJ); XLU and XLY
are separate themes. `dip_score` is *depth*, not quality — it's the CSV's rank, never the memo's.

## Phase 1 — quick pass → dossier

Read LEADERS first: *where did the money go?* Dips cluster as the mirror of the leaders; one
cluster = one rotation, not N separate problems. A lone dip while siblings hold is idiosyncratic.

Candidates = the CANDIDATES block. One web search per **theme**, not per fund — `"<theme> ETF" selloff <Month YYYY>` —
and a provisional bucket per theme, copied to siblings unless the search gives a fund-specific reason (one sentence): **rotation** (thesis intact) / **break** (policy repeal, demand collapse,
obsolescence, top-holding blowup, permanent re-rating) / **unclear**.

Write `output/<DATE>/dossier.md`: (A) the candidates' full CSV rows with column legend, (B) leaders,
(C) the quick-pass memo, marked *unverified — challenge it*. In quick mode, stop here and write the
memo (format below) to `log/<DATE>.md`.

## Phase 2 — panel, sequential

Read `lenses.md` (same folder). For each lens in order **cause → necessity → catalyst → basket →
price**, skip if `output/<DATE>/score_<lens>.md` exists, else spawn ONE subagent
(`subagent_type: "claude"`, `model: "opus"`) with: working dir, "read dossier.md and your row in
lenses.md", score ALL candidates 1-10 on that lens only, search as far as the stop rule needs (no cap;
WebFetch a primary source when a snippet is the only evidence for a buy-grade score), write the ballot file in the
lenses.md format, return it. Wait for it before starting the next. Cause, necessity and catalyst are **theme**
questions: research once per theme, copy the score to siblings, one sentence where a sibling differs. Basket and
price are per fund; price needs no search (CSV columns).

Why one criterion per agent: a single agent asked for "overall" quietly lets the loudest fact
(usually the price drop) contaminate every other judgment. Splitting forces the necessity scorer to
say "the world needs uranium" without knowing whether it's cheap.

## Phase 3 — consolidate

`score = 0.30·cause + 0.20·necessity + 0.20·catalyst + 0.15·basket + 0.15·price`.
**Veto:** cause ≤ 3 → *avoid* regardless. Then set **my rank**: start from the weighted score, read
all five ballots, and reorder where the ballots' facts justify it — one sentence per deviation.
`consolidate.py` writes the `bucket` column (buy / alt / watch / avoid — rule in README §2): overlapping funds
(URA/URNM/NLR, GLD/GDX/GDXJ, ICLN/QCLN/PBW…) are one position, so only `theme_rank == 1` can be buy; the rest are *alt*.
Start the memo from `scores.csv` buckets; any override (e.g. a rule-buy you judge watch) is a deviation — one sentence.
Never hand-edit `scores.csv`; my rank lives in the memo only.

Phase 3.5 — verifier, not optional in panel mode: one Opus verifier re-checks the top-3's load-bearing facts
from primary sources, uncapped searches, and may demote. This is the phase that caught a stale quote holding up
two rule-buys on 2026-09-06; skipping it makes the run a lite run with extra steps. Genuinely out of budget →
run `/etf-dip-pick-lite` instead rather than a panel with no verifier.

## Phase 4 — memo → `log/<DATE>.md`

```
# etf-dip-pick <DATE> — panel   (or: quick)

Regime: 2-3 lines.

| my # | ETF | theme | dd_52w | dip_score# | cause | need | cat | basket | price | wtd | TP | SL | R/R | bucket | why (1 line) |
...all candidates, in MY order...

Deviations from weighted score: one sentence each.
Buy: ...   Watch: ...   Avoid: ...

## With $100k (`consolidate.py <DATE> 100000 <final buys>`)
Risk-parity table: $ per buy, loss at SL, gain at TP, totals. Then tranche call: if the buys share one macro
catalyst (same FOMC / same policy date) → half now, half after it; if independent → all in. Stops as orders,
TPs as alerts. Max loss = all stops hit (gaps lose more); max gain = all funds back to 52w high (no timeline).

Caveat: the one macro thing that flips the whole list.
Panel: lenses run / skipped, searches used, verifier findings (or why lite would have been the honest call).
```

TP / SL / R/R come from scores.csv (`tp_pct` `sl_pct` `rr`; blank TP and R/R for avoids). The $100k section comes
from `consolidate.py <DATE> 100000 <ticker,ticker,...>` — pass the memo's final buys if it overrode a rule-buy. Add the 4-line
footnote explaining the rules (see log/2026-09-06.md). Keep "why" to one line. No other targets or sizing. Append to `SESSIONS.md` per the session-log
hook. Overwrite `data/` freely; never delete `log/` or `output/*/dossier.md` — they're the audit trail.
