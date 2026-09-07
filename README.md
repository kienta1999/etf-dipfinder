# etf-dipfinder

Scan ~115 liquid sector / thematic ETFs for dips, then decide which dips are worth buying.

```
uv sync
uv run python scripts/scan.py                 # → data/scan.csv + CANDIDATES (dips in top 15 themes) / LEADERS
uv run python scripts/test_scan.py            # self-check
/etf-dip-pick                                      # Claude: full 5-lens Opus panel → log/<DATE>.md
/etf-dip-pick-lite                                 # Claude: one agent, ~12 searches, same memo sections → log/<DATE>-lite.md
uv run python scripts/consolidate.py <DATE> [100000 NLR,GLD,XLU]   # ballots → scores.csv; optional $ split of buys
```

## 1. The scan (deterministic)

`is_dip = (price < SMA200  OR  dd_52w ≤ −10%)  AND  rs_spy_3m < 0`

- Two shapes of "down": trend broken (slow dip) or ≥10% off the high while still above trend (fast dip after a run).
- The AND gate — lagging SPY over 3 months — stops a broad selloff from flagging the whole universe. In a real crash the
  trade is SPY, not sector picking.
- Everything is computed; only dips are ranked. Leaders are kept because they tell you *where the money went*.
- **Candidates are picked by theme, not by depth.** A theme = funds the same headline moves (URA/URNM/NLR;
  GLD/GDX/GDXJ; XLU is its own theme, so is XLY). Themes rank by their deepest dip; the top `TOP_THEMES` (15) themes
  contribute every one of their dips as candidates. Research is once per theme, so 15 themes cost the same as 15 funds
  and cover more ground; siblings still get their own row, score and `theme_rank`.

Columns worth knowing: `dd_z` (drawdown ÷ vol — XBI at −15% is noise, XLP at −10% is news), `dd_pctile` (how deep vs
this ETF's own 3y history; < 0.10 = real event), `stabilizing` (10-day return > 0), `dip_score` (depth rank, 0 = most
beaten up). `dip_score` is depth, **not** quality. Knobs at the top of `scripts/scan.py`.

Universe (~50 themes): each SPDR sector, semis (SMH/SOXX/DRAM), AI/robot, software, cyber, banks, crypto spot vs equity,
biotech, oil/gas, nuclear, base metals / rare earth / lithium, gold, silver, solar / clean / hydrogen / wind, grid, defense
US vs EU, space, housing, consumer, REIT, one theme per country. < $5M/day dollar volume is dropped.

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
.claude/skills/etf-dip-pick-lite/  SKILL.md (one agent, reads ../etf-dip-pick/lenses.md, same memo sections as full, writes log/<DATE>-lite.md only)
log/<DATE>-lite.md            lite memo
```

## 4. Latest run — 2026-09-06

Buy (one per theme): **NLR, GLD, XLU**; URA/URNM are nuclear alternates. Watch: SLV XAR SHLD ITB ICLN. Avoid: TAN UFO PBW. Full table and the $100k split (risk parity, half now / half after FOMC) in `log/2026-09-06.md`.
Headline: uranium term price at an 18-year high while uranium equities fell 14-17% — the commodity says the seller is a
position, not a thesis. All three buys lean on the Sep 16 FOMC not hiking.
Lite rerun on the theme-first cut (30 funds / 15 themes): same answer, NLR the only buy; ai/robot, lithium, XLY, XLC added
nothing buyable. `log/2026-09-06-lite.md`.

## 5. TODO (next session)

- ~~TP / SL columns~~ done. ~~Adversarial review fixes~~ done (bucket column, frozen scan, parse asserts, NaN guards).
- Verifier (Phase 3.5) is now mandatory in panel mode; out of budget → run `/etf-dip-pick-lite` instead.
- Re-scan after FOMC Sep 16 2026.
- Shallow dips score too high: ROBO / XLC / XLY / PPA (-6 to -11%, R/R < 1.3) ranked mid-table on the lite rerun. Either
  a depth gate in the price lens (dd_52w > -12% or R/R < 1.2 → price ≤ 4) or a `min_rr` cut in `scan.py`.
- Build `-lite` versions of stock-pick-dip / momentum / earnings (memo in conviction-pick-sp500/TODO.md).
