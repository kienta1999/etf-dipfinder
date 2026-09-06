# Sessions

## 2026-09-05 — project created: scanner + /dipfind skill
**Resume:** `claude --resume 37e23d4f-34ee-41a9-8273-a0b1ff1bc431` (from `investment_strategy/`)
**Did:**
- Chose name `etf-dipfinder`; curated ~115 liquid sector/thematic ETFs (SPDR sectors, semis, AI/robot, nuclear, defense, metals, clean, crypto, country) incl. 2026 launches DRAM, AIPO, AIHY, BAI, PHOX.
- `scripts/scan.py`: yfinance 3y download → dd_52w, dd_z (dd/vol), dd_pctile (vs own history), vs_sma200/50, rs_spy_3m/6m/12m, ret_10d, dollar_vol. Drops <$5M/day.
- Decided `is_dip = (price<SMA200 OR dd_52w≤−10%) AND rs_spy_3m<0`. Everything is computed, only dips ranked; leaders kept as regime info.
- `scripts/test_scan.py` synthetic self-check (passes). `.claude/skills/dipfind/SKILL.md`: run scan → web-check why each top dip is down → bucket rotation/break/unclear → memo to `log/`.
- First live scan: 41/106 dips. Cluster: nuclear/defense/space/rare-earth/clean unwinding; leaders crypto + biotech. BJK delisted, PHOX no data, 11 illiquid dropped.
- Local git repo initialised, no remote.

**Continue:**
- `cd etf-dipfinder && uv run python scripts/scan.py` then `/dipfind` (not yet run once).
- Open: add `strict` column (all three conditions)? Add remote + push? Tune knobs (`DD_MIN`, `MIN_DOLLAR_VOL`) at top of scan.py.

## 2026-09-06 — panel mode: 5 Opus lenses, consolidate, my-rank memo
**Resume:** `claude --resume 37e23d4f-34ee-41a9-8273-a0b1ff1bc431` (from `investment_strategy/`)
**Did:**
- Reviewed the 09-05 single-agent memo: KWEB #1 was depth not quality; XLU on its buy list only via "stabilizing" flag. Memo now carries MY rank, CSV keeps dip_score.
- Designed 5 lenses (cause .30 / necessity .20 / catalyst .20 / basket .15 / price .15) in `.claude/skills/dipfind/lenses.md`; SKILL.md rewritten to quick vs panel mode, sequential Opus agents, ≤10 searches each.
- Ran the panel on 15 candidates (~340k subagent tokens). `scripts/consolidate.py` merges ballots → `output/2026-09-06/scores.csv`. Memo: `log/2026-09-06.md`. Buy NLR URA GLD XLU.
- README rewritten as a short report. Verifier (Phase 3.5) skipped — user near Pro limit.
**Continue:**
- Optional: run the verifier on NLR/URA/GLD top claims (one Opus agent). Re-scan after FOMC Sep 16.
- Open: should `buy` require stabilizing? Add strict column? Push to a remote (none yet).
