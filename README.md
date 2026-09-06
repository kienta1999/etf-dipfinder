# etf-dipfinder

Scan ~115 liquid sector / thematic ETFs for dips, then decide which dips are worth buying.

```
uv sync
uv run python scripts/scan.py                 # → data/scan.csv + DIPS / LEADERS
uv run python scripts/test_scan.py            # self-check
/etf-dip-pick                                      # Claude: quick memo, or full 5-lens Opus panel
uv run python scripts/consolidate.py <DATE>   # merge panel ballots → output/<DATE>/scores.csv
```

## 1. The scan (deterministic)

`is_dip = (price < SMA200  OR  dd_52w ≤ −10%)  AND  rs_spy_3m < 0`

- Two shapes of "down": trend broken (slow dip) or ≥10% off the high while still above trend (fast dip after a run).
- The AND gate — lagging SPY over 3 months — stops a broad selloff from flagging the whole universe. In a real crash the
  trade is SPY, not sector picking.
- Everything is computed; only dips are ranked. Leaders are kept because they tell you *where the money went*.

Columns worth knowing: `dd_z` (drawdown ÷ vol — XBI at −15% is noise, XLP at −10% is news), `dd_pctile` (how deep vs
this ETF's own 3y history; < 0.10 = real event), `stabilizing` (10-day return > 0), `dip_score` (depth rank, 0 = most
beaten up). `dip_score` is depth, **not** quality. Knobs at the top of `scripts/scan.py`.

Universe: SPDR sectors, semis (SMH/SOXX/DRAM), AI/robot, software, cyber, banks, crypto, biotech, oil/gas, nuclear, metals,
gold/silver, clean, grid, defense, space, housing, consumer, REIT, country. < $5M/day dollar volume is dropped.

## 2. The panel (judgment)

An ETF 25% off its high is either **on sale** (money rotated, thesis intact) or **broken** (thesis changed). The numbers
look identical. Five Opus subagents each score every candidate 1-10 on ONE criterion, so the loudest fact (the price drop)
can't contaminate the others:

| lens | w | question |
|---|---|---|
| cause | .30 | flows/rates/rotation, or did the thesis change? (≤3 = veto) |
| necessity | .20 | does the world need this in 5-10y; can AI/tech/policy route around it? |
| catalyst | .20 | dated trigger in 3-12 months that reverses the flow? |
| basket | .15 | is the fund a clean way to own the theme — holdings, concentration, fee, structure? |
| price | .15 | unusually cheap vs own history, trend intact, bounce started? |

Agents run **sequentially** and each writes `output/<DATE>/score_<lens>.md` before the next starts, so a budget cutoff
resumes from the first missing ballot. `consolidate.py` is deterministic: weighted score, `theme_rank` (order inside a
theme by weighted score, non-vetoed only), and `bucket`:

| bucket | rule |
|---|---|
| avoid | cause ≤ 3 (veto) |
| buy | cause ≥ 7 and (stabilizing or catalyst ≥ 7) and `theme_rank == 1` |
| alt | same but `theme_rank > 1` — URA/URNM/NLR are one position, not three |
| watch | everything else |

The orchestrator then sets **my rank** and may override a bucket; every deviation from `scores.csv` gets one sentence
in `log/<DATE>.md`. First `consolidate.py` run freezes `data/scan.csv` into `output/<DATE>/scan.csv` so a later
re-scan never changes a dated result.

Borrowed from `conviction-pick-sp500/stock-pick-dip`: dossier → independent lenses → consolidate → dated log. Dropped:
company-level lenses (moat, balance sheet) — an ETF is a basket.

## 3. Layout

```
scripts/scan.py, consolidate.py, test_scan.py
data/scan.csv                 latest scan, gitignored (has an asof column = last close used)
output/<DATE>/scan.csv        frozen scan the panel scored against (committed)
output/<DATE>/dossier.md      what the panel saw (committed)
output/<DATE>/score_*.md      ballots (committed)   scores.csv (committed)
log/<DATE>.md                 the memo — audit trail, never delete
.claude/skills/etf-dip-pick/       SKILL.md + lenses.md
```

## 4. Latest run — 2026-09-06

Buy (one per theme): **NLR, GLD, XLU**; URA/URNM are nuclear alternates. Watch: SLV XAR SHLD ITB ICLN. Avoid: TAN UFO PBW. Full table in `log/2026-09-06.md`.
Headline: uranium term price at an 18-year high while uranium equities fell 14-17% — the commodity says the seller is a
position, not a thesis. All three buys lean on the Sep 16 FOMC not hiking.

## 5. TODO (next session)

- ~~TP / SL columns~~ done. ~~Adversarial review fixes~~ done (bucket column, frozen scan, parse asserts, NaN guards).
- Run the verifier (Phase 3.5) on NLR / GLD / XLU top claims.
- Re-scan after FOMC Sep 16 2026.
