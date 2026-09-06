---
name: dipfind
description: Find and rank sector / thematic ETFs that are in a dip — below their 200-day SMA or ≥10% off the 52-week high AND lagging SPY over 3 months — then decide which dips are worth buying. Runs the deterministic scan (scripts/scan.py), builds a dossier, fans out to five SEQUENTIAL Opus scoring panelists (cause, necessity, catalyst, basket, price), consolidates a weighted score plus the orchestrator's own rank, and writes a dated memo to log/. Use this whenever the user asks what ETFs or sectors are "on sale", "beaten down", "lagging", "oversold", "which sectors are dipping", "buy the dip" for ETFs/sectors/themes (semis, nuclear, defense, biotech, clean energy, crypto, gold miners, China, etc.), wants to know where money is rotating, or wants a quick single-agent pass ("quick dipfind") — even if they don't say "ETF" or "/dipfind". For single-stock dips use conviction-pick-sp500's /stock-pick-dip instead.
---

# dipfind — rank ETF dips, separate dips from falling knives

An ETF 25% off its high is either **on sale** (money rotated elsewhere, thesis intact) or
**broken** (the thesis changed). The scan can't tell; the panel can. Two modes:

- **quick** — orchestrator alone, one search per ETF, memo with buckets. ~5 min, cheap.
- **panel** (default when the user says "rank", "review", "which to buy") — quick pass becomes
  the dossier, then five Opus panelists score one criterion each, orchestrator consolidates.

The user is on a Pro plan. **Every panelist runs sequentially and writes its ballot to disk before
the next starts**, so a budget cutoff leaves finished work on disk and the run resumes from the
first missing `score_<lens>.md`. Never run panelists in parallel. Cap each at ~10 web searches.

## Phase 0 — scan

```
cd etf-dipfinder && uv run python scripts/scan.py     # full path if cwd is already inside
```

Prints DIPS (sorted by `dip_score`, 0 = most beaten up) and LEADERS, writes `data/scan.csv`.
`dip_score` is *depth*, not quality — it's the CSV's rank, never the memo's.

## Phase 1 — quick pass → dossier

Read LEADERS first: *where did the money go?* Dips cluster as the mirror of the leaders; one
cluster = one rotation, not N separate problems. A lone dip while siblings hold is idiosyncratic.

For the top ~12-15 dips, one web search each — `"<TICKER> ETF" <theme> selloff <Month YYYY>` —
and a provisional bucket: **rotation** (thesis intact) / **break** (policy repeal, demand collapse,
obsolescence, top-holding blowup, permanent re-rating) / **unclear**.

Write `output/<DATE>/dossier.md`: (A) the candidates' full CSV rows with column legend, (B) leaders,
(C) the quick-pass memo, marked *unverified — challenge it*. In quick mode, stop here and write the
memo (format below) to `log/<DATE>.md`.

## Phase 2 — panel, sequential

Read `lenses.md` (same folder). For each lens in order **cause → necessity → catalyst → basket →
price**, skip if `output/<DATE>/score_<lens>.md` exists, else spawn ONE subagent
(`subagent_type: "claude"`, `model: "opus"`) with: working dir, "read dossier.md and your row in
lenses.md", score ALL candidates 1-10 on that lens only, ≤10 searches, write the ballot file in the
lenses.md format, return it. Wait for it before starting the next.

Why one criterion per agent: a single agent asked for "overall" quietly lets the loudest fact
(usually the price drop) contaminate every other judgment. Splitting forces the necessity scorer to
say "the world needs uranium" without knowing whether it's cheap.

## Phase 3 — consolidate

`score = 0.30·cause + 0.20·necessity + 0.20·catalyst + 0.15·basket + 0.15·price`.
**Veto:** cause ≤ 3 → *avoid* regardless. Then set **my rank**: start from the weighted score, read
all five ballots, and reorder where the ballots' facts justify it — one sentence per deviation.
Bucket: **buy** = cause ≥ 7 and (stabilizing or catalyst ≥ 7) and `theme_rank == 1` — overlapping funds
(URA/URNM/NLR, GDX/GDXJ, TAN/ICLN/PBW…) are one position; the rest of the theme are *alternates*, not extra buys; **watch** = rotation but still
falling / catalyst far; **avoid** = veto. Save `output/<DATE>/scores.csv` (lens scores, weighted,
my_rank, dip_score).

Optional Phase 3.5 (skip on tight budget, say so in the memo): one Opus verifier re-checks the
top-3's load-bearing facts from primary sources.

## Phase 4 — memo → `log/<DATE>.md`

```
# dipfind <DATE> — panel   (or: quick)

Regime: 2-3 lines.

| my # | ETF | theme | dd_52w | dip_score# | cause | need | cat | basket | price | wtd | bucket | why (1 line) |
...all candidates, in MY order...

Deviations from weighted score: one sentence each.
Buy: ...   Watch: ...   Avoid: ...
Caveat: the one macro thing that flips the whole list.
Panel: lenses run / skipped, searches used, verifier yes/no.
```

Keep "why" to one line. No price targets, no sizing. Append to `SESSIONS.md` per the session-log
hook. Overwrite `data/` freely; never delete `log/` or `output/*/dossier.md` — they're the audit trail.
