---
name: etf-dip-pick
description: Find and rank sector / thematic ETFs that are in a dip — below their 200-day SMA or ≥10% off the 52-week high AND lagging SPY over 3 months — then decide which dips are worth buying. Runs the deterministic scan (scripts/scan.py), builds a dossier, fans out to four SEQUENTIAL Opus scoring panelists (cause, necessity, catalyst, basket; price is computed), consolidates a weighted score plus the orchestrator's own rank, and writes a dated memo to log/. Use this whenever the user asks what ETFs or sectors are "on sale", "beaten down", "lagging", "oversold", "which sectors are dipping", "buy the dip" for ETFs/sectors/themes (semis, nuclear, defense, biotech, clean energy, crypto, gold miners, China, etc.), wants to know where money is rotating, or wants a quick single-agent pass ("quick etf-dip-pick") — even if they don't say "ETF" or "/etf-dip-pick". For single-stock dips use conviction-pick-sp500's /stock-pick-dip instead.
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
Every ballot row names the band from `lenses.md` it scored into; the anchors bind, and a score 2+ points
off its band is a deviation that needs its own sentence.

## Independence — every run scores from today's evidence only

A run's judgment must be its own, or the consensus counts one opinion several times: the 2026-09-24, 09-27 and
09-28 lite memos carried their predecessor's cause/necessity/catalyst/basket scores over unchanged (100% of rows),
while genuinely independent runs on byte-identical prices never matched more than 29%.

- **Until `consolidate.py` has written this run's `scores.csv`, open nothing from another run:** no other
  `log/20*.md`, no other `output/<id>/` (ballots, scores, dossier, verifier), no `SESSIONS.md`. Panelists get this run's
  dossier and the web, nothing else, and their prompt says so.
- **Facts are shared, opinions are not.** The one past input allowed is dossier section D
  (`carry_forward.py`): issuer-confirmed dated events, no scores. Re-searching a confirmed date from scratch only adds noise.
- **Comparisons come after scoring.** check_memo's day-over-day table (check 6) is an audit of the finished run.
- **Run id, not date.** `RUN=$(uv run python scripts/run_id.py)` — the date for a date's first run, `<date>-r2`, `-r3`…
  for any later one. Everything below that says `<DATE>` means `<RUN>`: `output/<RUN>/`, `log/<RUN>.md`,
  `consolidate.py <RUN>`, `check_memo.py <RUN>`. A rerun never edits or deletes an earlier run's files (the 2026-10-01
  and 2026-10-04 reruns did, and the first opinion survived only in git history); `log/catalysts.md` is the only shared file a run may change.

`check_memo.py` enforces all four: it fails a run whose judged scores match an earlier memo on ≥80% of ≥8 shared funds,
a catalyst below the computed floor (lenses.md), and any change to another run's files.

## Phase 0 — scan

```
cd etf-dipfinder && uv run python scripts/scan.py     # full path if cwd is already inside
```

Prints CANDIDATES — every dip in the `TOP_THEMES` (15) themes whose best dip is deepest, grouped by theme — and
LEADERS, writes `data/scan.csv`. A theme = funds the same headline moves (URA/URNM/NLR; GLD/GDX/GDXJ); XLU and XLY
are separate themes. `dip_score` is *depth*, not quality — it's the CSV's rank, never the memo's.
It also writes `data/drops.csv` — every fund that missed CANDIDATES with the gate and the failing values. When the
user holds or asks about a fund that is not a candidate (or not a buy), run `uv run python scripts/why.py <TICKER>`
and quote it — never guess. `consolidate.py` freezes drops.csv with scan.csv and writes `output/<DATE>/buckets_why.csv`
(the rule leg behind each bucket); both are committed with the run.

## Phase 1 — quick pass → dossier

Read LEADERS first: *where did the money go?* Dips cluster as the mirror of the leaders; one
cluster = one rotation, not N separate problems. A lone dip while siblings hold is idiosyncratic.

Candidates = the CANDIDATES block. One web search per **theme**, not per fund — `"<theme> ETF" selloff <Month YYYY>` —
and a provisional bucket per theme, copied to siblings unless the search gives a fund-specific reason (one sentence): **rotation** (thesis intact) / **break** (policy repeal, demand collapse,
obsolescence, top-holding blowup, permanent re-rating) / **unclear**.

Write `output/<DATE>/dossier.md`: (A) the candidates' full CSV rows with column legend, (B) leaders,
(C) the quick-pass memo, marked *unverified — challenge it*, (D) the output of
`uv run python scripts/carry_forward.py` — catalysts a previous verifier already confirmed and that have
not expired, with the **catalyst floor** column (lenses.md) marked. Panelists start cold, so without (D) a confirmed date has to be rediscovered every run. In quick mode, stop here and write the
memo (format below) to `log/<DATE>.md`.

## Phase 2 — panel, sequential

Read `lenses.md` (same folder). Four lenses are researched; **price is computed by `consolidate.price_score()`
from the scan, so never spawn a price panelist and never write `score_price.md`.** For each lens in order
**cause → necessity → catalyst → basket**, skip if `output/<DATE>/score_<lens>.md` exists, else spawn ONE subagent
(`subagent_type: "claude"`, `model: "opus"`) with: working dir, "read dossier.md and your row in
lenses.md; do not open any other run's files (other log/ memos, other output/ folders, SESSIONS.md) — score from
this dossier and the web only", score ALL candidates 1-10 on that lens only, search as far as the stop rule needs (no cap;
WebFetch a primary source when a snippet is the only evidence for a buy-grade score), write the ballot file in the
lenses.md format, return it. Wait for it before starting the next. Cause, necessity and catalyst are **theme**
questions: research once per theme, copy the score to siblings, one sentence where a sibling differs. Basket is per fund.

Why one criterion per agent: a single agent asked for "overall" quietly lets the loudest fact
(usually the price drop) contaminate every other judgment. Splitting forces the necessity scorer to
say "the world needs uranium" without knowing whether it's cheap.

## Phase 3 — consolidate

`score = 0.30·cause + 0.20·necessity + 0.20·catalyst + 0.15·basket + 0.15·price`, −1 if thin (R/R < 1.3).
**Veto:** cause ≤ 3 → *avoid* regardless. Then set **my rank**: start from the weighted score, read
all five ballots, and reorder where the ballots' facts justify it — one sentence per deviation.
`consolidate.py` writes the `bucket` column (buy / core / alt / watch / avoid — rule in README §2; *core* is a broad
fund bought on cause + necessity without a dated catalyst, held long term with no stop): overlapping funds
(URA/URNM/NLR, GLD/GDX/GDXJ, ICLN/QCLN/PBW…) are one position, so only `theme_rank == 1` can be buy; the rest are *alt*.
Start the memo from `scores.csv` buckets; any override (e.g. a rule-buy you judge watch) is a deviation — one sentence.
Never hand-edit `scores.csv`; my rank lives in the memo only.

Phase 3.5 — verifier, not optional in panel mode: one Opus verifier re-checks, from primary sources with
uncapped searches, the load-bearing facts behind **every fund the rule buckets `buy` or `core`** (not the top 3 by
weighted score — on 2026-09-18 UFO was a buy ranked 10th and went unverified, so the one position whose
whole case was a dated event had that date checked by nobody), plus the regime premises the memo opens on.
Every dated event it CONFIRMS gets a row appended to `log/catalysts.md` (theme, match keyword, event,
date, source, verified-on) so the next run inherits it. A live row is overturned only by a cited source that
CONTRADICTS it — then mark it `RETRACTED` with that source; "could not re-find it" leaves the row standing, and
`check_memo.py` fails a catalyst ballot that calls a live row "unverified". Dates that sources contradict each other
on go in the ledger's `## Disputed` table, not the confirmed one. It writes `output/<DATE>/verifier.md` as a claim / verdict / evidence table — confirmations listed the same
way as demotions, so a clean pass leaves as much evidence as a failing one — and may demote. This is the phase that caught a stale quote holding up
two rule-buys on 2026-09-06; skipping it makes the run a lite run with extra steps. Genuinely out of budget →
run `/etf-dip-pick-lite` instead rather than a panel with no verifier.

Phase 3.6 — audit, before the memo is final: `uv run python scripts/check_memo.py <DATE>`.
It fails the run if `scores.csv` was not written by `consolidate.py`, if the ballots do not parse,
if re-running the rule does not reproduce `scores.csv`, if any bucket printed in the memo
contradicts the one the rule computed, if the judged scores copy an earlier run, if a catalyst sits below the computed
floor, or if the run changed another run's files. It also fails when anything under `output/` or `log/` is uncommitted, because a run nobody committed
is a run nobody else can see: every other check here reads the filesystem and passes locally either way.
Fix what it reports, commit what it lists, and re-run until it exits 0 — the run is not finished, and the
memo is not published, while it is non-zero.

## Phase 4 — memo → `log/<DATE>.md`

```
# etf-dip-pick <DATE> — panel   (or: quick)

Regime: 2-3 lines.

| my # | ETF | theme | dd_52w | dip# | cause | necessity | catalyst | basket | price | wtd | TP | SL | R/R | bucket | why (1 line) |
...all candidates, in MY order...

Deviations from weighted score: one sentence each.
Buy: ...   Core: ...   Watch: ...   Avoid: ...

## With $100k (`consolidate.py <DATE> 100000 <final buys>`)
Risk-parity table: $ per buy, loss at SL, gain at TP, totals. Then tranche call: if the buys share one macro
catalyst (same FOMC / same policy date) → half now, half after it; if independent → all in. Stops as orders,
TPs as alerts. Max loss = all stops hit (gaps lose more); max gain = all funds back to 52w high (no timeline).
Core funds are listed separately under the table, not in the risk-parity split: long-term holds, no stop,
rebalance at ±25% of target weight, exit only if a later run vetoes the cause.

Caveat: the one macro thing that flips the whole list.
Panel: lenses run / skipped, searches used, verifier findings (or why lite would have been the honest call).
```

Copy the header row above verbatim: spell the five lenses out in full, keep every column, and do not
rename, abbreviate, reorder or drop one. A reader who has never seen the skill must be able to read the
table without a legend, and `why (1 line)` is the only place each row's reasoning survives.

TP / SL / R/R come from scores.csv (`tp_pct` `sl_pct` `rr`; blank TP and R/R for avoids). The $100k section comes
from `consolidate.py <DATE> 100000 <ticker,ticker,...>` — pass the memo's final buys if it overrode a rule-buy. Add the 4-line
footnote explaining the rules (see log/2026-09-06.md). Keep "why" to one line. No other targets or sizing. Append to `SESSIONS.md` per the session-log
hook. Overwrite `data/` freely; never delete `log/` or `output/*/dossier.md` — they're the audit trail.
