# Sessions

## 2026-09-05 — project created: scanner + /dipfind skill
**Resume:** `claude --resume 37e23d4f-34ee-41a9-8273-a0b1ff1bc431` (from `investment_strategy/`)
**Did:**
- Chose name `etf-dipfinder`; curated ~115 liquid sector/thematic ETFs (SPDR sectors, semis, AI/robot, nuclear, defense, metals, clean, crypto, country) incl. 2026 launches DRAM, AIPO, AIHY, BAI, PHOX.
- `scripts/scan.py`: yfinance 3y download → dd_52w, dd_z (dd/vol), dd_pctile (vs own history), vs_sma200/50, rs_spy_3m/6m/12m, ret_10d, dollar_vol. Drops <$5M/day.
- Decided `is_dip = (price<SMA200 OR dd_52w≤−10%) AND rs_spy_3m<0`. Everything is computed, only dips ranked; leaders kept as regime info.
- `scripts/test_scan.py` synthetic self-check (passes). `.claude/skills/etf-dip-pick/SKILL.md`: run scan → web-check why each top dip is down → bucket rotation/break/unclear → memo to `log/`.
- First live scan: 41/106 dips. Cluster: nuclear/defense/space/rare-earth/clean unwinding; leaders crypto + biotech. BJK delisted, PHOX no data, 11 illiquid dropped.
- Local git repo initialised, no remote.

**Continue:**
- `cd etf-dipfinder && uv run python scripts/scan.py` then `/dipfind` (not yet run once).
- Open: add `strict` column (all three conditions)? Add remote + push? Tune knobs (`DD_MIN`, `MIN_DOLLAR_VOL`) at top of scan.py.

## 2026-09-06 — panel mode: 5 Opus lenses, consolidate, my-rank memo
**Resume:** `claude --resume 37e23d4f-34ee-41a9-8273-a0b1ff1bc431` (from `investment_strategy/`)
**Did:**
- Reviewed the 09-05 single-agent memo: KWEB #1 was depth not quality; XLU on its buy list only via "stabilizing" flag. Memo now carries MY rank, CSV keeps dip_score.
- Designed 5 lenses (cause .30 / necessity .20 / catalyst .20 / basket .15 / price .15) in `.claude/skills/etf-dip-pick/lenses.md`; SKILL.md rewritten to quick vs panel mode, sequential Opus agents, ≤10 searches each.
- Ran the panel on 15 candidates (~340k subagent tokens). `scripts/consolidate.py` merges ballots → `output/2026-09-06/scores.csv`. Memo: `log/2026-09-06.md`. Buy NLR URA GLD XLU.
- README rewritten as a short report. Verifier (Phase 3.5) skipped — user near Pro limit.
**Continue:**
- Optional: run the verifier on NLR/URA/GLD top claims (one Opus agent). Re-scan after FOMC Sep 16.
- Open: should `buy` require stabilizing? Add strict column? Push to a remote (none yet).
- Added one-buy-per-theme rule (`theme_rank`), memo updated: buy NLR GLD XLU; URA/URNM alternates. Repo public at https://github.com/kienta1999/etf-dipfinder.
- TODO for next session in README §5: TP/SL columns (TP = 52w high, SL = vol-scaled), verifier, post-FOMC rescan.

## 2026-09-06 (b) — /etf-dip-pick-lite: one-agent version
**Did:**
- New skill `.claude/skills/etf-dip-pick-lite/SKILL.md`: same scan + lenses.md + weights/veto/theme rule, but one agent,
  one search per theme (~10 total), scores consolidated with an inline pandas snippet, memo only to `log/<DATE>-lite.md`.
  Nothing written to `output/`, no verifier.
- Ran it: `log/2026-09-06-lite.md`. Buy NLR; GLD/XLU watch until FOMC Sep 16 — same answer as the full panel at ~1/6 the tokens.
**Continue:** post-FOMC rescan (Sep 16/17) — lite first; run the full panel only if the buy list changes.
- Theme-first candidates: `scan.py` themes re-cut to "same headline moves both" (gold ≠ silver, each SPDR sector its own
  theme, one theme per country, solar ≠ clean, crypto spot ≠ equity, defense US ≠ EU). `TOP_THEMES = 15`; CANDIDATES =
  every dip in the 15 deepest themes (today 30 funds / 15 themes vs 15 funds / 9 themes). Both skills research once per theme.
- Re-ran lite on the theme-first cut (30 funds / 15 themes, 4 new searches): buy list unchanged — NLR buy, GLD/XLU watch
  until FOMC. New themes (ai/robot, lithium, XLY, XLC) are rests in uptrends or wobbles, not dips. `log/2026-09-06-lite.md`.
- 2026-09-15 lite (12 searches): regime flipped — 10y 5%, hike 92% priced. NLR still the only buy (-34%, term U3O8 $96.50
  record; cause cut to 7 on AI-capex doubt), URNM/URA alt, GLD/XLU watch until the Sep 16 statement. TAN/UFO/PBW avoid →
  watch. $5,740 NLR (size_1pct), half now / half post-FOMC. `log/2026-09-15-lite.md`.

## 2026-09-17 — full panel on 32 candidates / 15 themes (user: "tiếp luôn… commit lên đc k push thẳng master okay")
**Did:**
- Ran the full panel (user authorized direct push to master): scan froze `data/scan.csv` → `output/2026-09-17/scan.csv`;
  five sequential lens ballots all written for exactly 32 tickers (`dossier.md`, `score_cause.md`, `score_necessity.md`,
  `score_catalyst.md`, `score_basket.md`, `score_price.md`); `scripts/consolidate.py 2026-09-17` → `scores.csv`.
- Fixes along the way: dossier BAI row now says `stabilizing=yes` (matches scan.csv); XHB basket link corrected (was PBW's).
- Verifier (Phase 3.5) re-checked XLU/NLR/URNM load-bearing facts on primary sources — all confirmed, no demotions
  (XLU 0.08%/$21.5B/100% utilities on ssga.com; NLR 0.52%/26 holdings/Cameco Oct 30 on vaneck.com/BusinessWire; URNM
  0.75%/≥80% mandate/top-three 47.2% on sprottetfs.com; FOMC Oct 27–28 + Dec 8–9 on federalreserve.gov). Regime
  cross-check: Sep 16 FOMC **hiked** 25bp to 3.75–4.00% (first since 2023), 10y hit 5.008% Sep 14–15.
- Memo `log/2026-09-17.md`: buy XLU NLR GRID REMX UFO; alts URNM URA IGF PAVE ARKX; watch 18; avoid ICLN TAN QCLN PBW
  (cause veto). $100k risk parity: XLU $36.7k / NLR $13.2k / GRID $20.2k / REMX $13.3k / UFO $16.7k; max loss −$11.5k,
  max gain +$30.7k. Tranche: XLU/NLR/GRID half now + half post Oct 27–30 cluster; REMX half now + half post Sep 24
  summit; UFO full now. Caveat: Warsh hikes again Oct 28 → whole rate-sensitive list re-prices lower.
- Committed dated artifacts + log + this entry; pushed straight to master per user instruction.
**Continue:** post-event rescan (after Sep 24 summit and/or Oct 27–30 cluster) — lite first, full panel only if the buy
  list changes. Open: GitHub deploy-key auth (new key generated, public key given to user for the repo's deploy-keys
  page with write access; existing personal key is registered elsewhere and GitHub rejects duplicates).
