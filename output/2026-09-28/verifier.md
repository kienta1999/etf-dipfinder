# Verifier — 2026-09-28 (full panel; scan asof 2026-09-25 close)

All checks re-done from primary or first-party sources on 2026-09-28, uncapped searches. Prices are
the 2026-09-25 close; quotes below are from sources dated 9/24–9/28 as noted. Dossier §D carried-forward
rows were re-checked only for contradictions, per the carry-forward rule.

## Per-candidate verification (claim / verdict / evidence)

### NLR (nuclear; buy via catalyst 10)
| claim | source + date | verdict |
|---|---|---|
| Cameco Q3 2026 results before market open Friday, October 30, 2026 | Cameco's own Q2 press release 2026-07-31 (BusinessWire): "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026." Quoted verbatim by Morningstar, GuruFocus, Post-Gazette (financialcontent) 9/28 | **CONFIRMED** (carried-forward ledger row; no later Cameco PR contradicts it) |
| No contradiction from company calendars | No later Cameco release or investor-calendar entry moves the date; the 9/26 verifier's "unverifiable on cameco.com" was overruled by the carry-forward rule (a live row is overturned only by a cited contradiction — none exists) | stands |

Catalyst 10 stands. No demotion. Already in `log/catalysts.md` — no duplicate row appended.

### REMX (rare-earth; rule-bucketed buy → VERIFIER-DEMOTED to watch)
| claim | source + date | verdict |
|---|---|---|
| Ballot claim: MOFCOM No. 70's text settles the dispute — suspension expires 2026-11-10, snapback one-sided | The No. 70 text does state the original suspension window to 2026-11-10 (corroborated by Sphera and SilmarilMedia) — BUT the text is dated 2025-11-07, i.e. pre-summit; it cannot settle whether an extension was agreed. The ballot's cited link was the macmap.org PDF (a USADMIN measure document), not the ministry's publication | claim's factual quote stands; **the settlement inference COLLAPSES** |
| Ballot claim: the 2026-09-24 Trump–Xi summit was "silent on rare earths" (cited Sphera ~9/15, SilmarilMedia 9/23) | Both cited sources were written BEFORE the 9/24 summit — stale. Post-summit: The Global Market Brief 9/26 — "Bessent confirmed the two sides agreed to extend their temporary trade truce — which had lowered US tariffs and suspended Beijing's controls on rare earth and critical mineral exports — by two months, pushing the expiration from mid-November to Jan. 10, 2027." Corroborated by chomcho (post-summit) and tamaranews 9/26. FXStreet/InvestedAlpha report no *new* firm rare-earth commitments — consistent with a continuation of the pause, not a new deal | **CONTRADICTED** by post-summit sources |
| No MOFCOM announcement settles the extension either way | No MOFCOM text seen by either side (unchanged) | stands |

**DEMOTION: REMX catalyst 9 → 6.** The ledger's ## Disputed rule governs: no 7+ on a disputed date
without a primary source that settles it. No such source exists — the dispute is live (and now leans
toward the 2027-01-10 extension). At catalyst 6 with stabilizing=False, the buy gate fails
(cause ≥ 7 AND (stabilizing OR catalyst ≥ 7) AND not thin AND theme_rank == 1): **REMX buy → watch**.
This matches the 9/25 precedent (verifier-demoted REMX to catalyst 6 / watch). Applied via the ballot
edit + `scripts/consolidate.py` (scores.csv regenerated, never hand-edited). The disputed ledger row was
refreshed with the post-summit evidence and stays in ## Disputed.

### ARKX (space; buy via stabilizing + catalyst 8)
| claim | source + date | verdict |
|---|---|---|
| NVIDIA GTC 2027 at San Jose McEnery Convention Center, starting 2027-03-14 | nvidia.com GTC FAQ (crawled 9/28): "NVIDIA GTC will take place from March 14–18, 2027... at the San Jose McEnery Convention Center and venues throughout San Jose, CA" (150 W. San Carlos St.) | **CONFIRMED** (carried-forward ledger row) |
| Exact start date | NVIDIA's LinkedIn GTC showcase post says "March 15–18, 2027" — one-day discrepancy vs the official FAQ (14–18). The FAQ is the authoritative event page; the mid-March McEnery event itself is undisputed | minor flag, not a retraction; row stands at 2027-03-14 per the FAQ |

Catalyst 8 stands. No demotion. Already in `log/catalysts.md` — no duplicate row appended.

### TAN (solar; buy via catalyst 8)
| claim | source + date | verdict |
|---|---|---|
| Commerce finalized AD/CVD duties 2026-09-11 on solar imports from India/Indonesia/Laos | Reuters/SRN 9/11/2026: final affirmative AD determinations — India 123.04%, Indonesia 94.36%, Laos 65.43%; CVD — India 126.09%, Indonesia 73.2–173.7%, Laos 82.03–153.67% (combined India rate 249.13%). Corroborated by pv-tech, SMM, Sxcoal 9/14 | **CONFIRMED** |
| USITC final injury vote 2026-10-14 | SMM: "The U.S. International Trade Commission is scheduled to make its final injury determination on October 14"; Sxcoal: "scheduled to vote on October 14" | **CONFIRMED** — new row appended to `log/catalysts.md` |
| Commerce final duty orders 2026-11-02 | Sxcoal 9/14: "Commerce will issue final duty orders on November 2" (if USITC affirmative) | **CONFIRMED** — new row appended to `log/catalysts.md` |

Catalyst 8 stands. No demotion. Two new dated-event rows appended to the ledger (USITC 10-14, Commerce 11-02).

### IHI (health-other; buy via stabilizing=True)
| claim | source + date | verdict |
|---|---|---|
| Recent price action stabilized — bounce started | Scan (9/25 close): ret_10d +1.57%, stabilizing=True. Quote sources: Finimize $51.60 close 9/25 ("- $3.25 / -5.92% this month"); Intelligent Investor $51.60, +0.51% on 9/26; INDmoney $51.42 as of 9/29 00:30 IST — holding ~$51.4–51.6, off the dip low | **CONFIRMED** |
| No other load-bearing fact was assigned to IHI this run | catalyst ballot row 24 = 4 ("no confirmed date found") — nothing to check | n/a |

Buy stands on the stabilizing leg. No demotion.

### XLU (core; utilities)
| claim | source + date | verdict |
|---|---|---|
| 10y touched 5.225–5.23% intraday 9/25–9/28 (19-yr high) | Motley Fool 9/28: "reached 5.23% on Friday, Sept. 25, its highest level since 2007"; HDFCSky: intraday peak 5.225%; dailyforex 9/28: "touched 5.2297% on Friday"; tradingeconomics 9/25: spiked ~23bps to ~5.20% | **CONFIRMED** |
| 30y > 5.3% | naturalresourcestocks 9/25: 30y 5.44% | **CONFIRMED** |
| Utility earnings power unchanged (pure duration repricing) | No adverse utility earnings news in September: PSEG stable (9/2–9/3, mid-single-digit EPS growth guided); Fortis FY2026 estimates lifted by Scotiabank 9/10; FirstEnergy Q2 stable margins, moderate-buy consensus 9/14; ONE Gas stable with guidance intact (9/3). Regulated-dividend basket: the dip is rate math, not earnings damage | **CONFIRMED** |

Core stands. No demotion.

### IGF (core; grid/infra)
| claim | source + date | verdict |
|---|---|---|
| Gartner: +49% AI-server spend 2026 | PEX Network citing Gartner: "Building AI foundations alone will drive a 49 percent increase in spending on AI-optimized servers for 2026." (Gartner's 9/16 quarterly update separately: total AI spend +49.5% to $2.67T, infrastructure +51.2% — the 49% server figure matches the ballot's claim) | **CONFIRMED** |
| NEE 9.5GW gas for datacenters | NextEra Energy Q1 2026 8-K (stocktitan): "the U.S. Department of Commerce selected NextEra Energy Resources to build 9.5 GW of new gas-fired generation to serve large load in Texas and Pennsylvania" — part of Japan's $550B US investment commitment; projects serve data centers and advanced manufacturing | **CONFIRMED** |
| Dip is duration rotation, not capex reversal | AI capex figures above (rising, not cut); the fund's −9% drawdown coincides with the 10y spike — mechanism consistent | stands |

Core stands. No demotion.

## Regime premises
| claim | source + date | verdict |
|---|---|---|
| Sep 16 FOMC: unanimous +25bp hike to 3.75–4.00% | MBA Newslink 9/17 (quoting the FOMC statement, 12–0 vote): "raise the target range for the federal funds rate by 1/4 percentage point to 3-3/4 to 4%"; Motley Fool 9/19; summa money 9/28 (16/18 dots anticipate more hikes this year) — first hike since July 2023 | **CONFIRMED** |
| ~70% October-hike odds | dailyforex 9/28: CME FedWatch "approximate 70% probability of another Fed rate hike at its late October meeting, up from about 56% early last week"; thoughtcatalog 9/25: "roughly 70%" | **CONFIRMED** |
| 10y level | see XLU section — 5.23% 9/25, near-19-yr highs through 9/28 | **CONFIRMED** |
| Oil price (dated 9/28) | Dow Jones via TradingView 9/28: Brent $108.57 (+4%), WTI $96.27 (+4.1%) — Trump rejected Iran's Hormuz-reopening proposal over the weekend; hdfcsky: Brent $106.2, WTI $93.4; blinknews 9/28: Brent $107.75, WTI $94.55 | **CONFIRMED** (Brent ~$106–108, WTI ~$93–96 on 9/28; Iran/Hormuz risk premium) |

## check_memo.py check 5c
The 9/28 catalyst ballot did NOT call any live ledger row "unverified" — Cameco (NLR/URA/URNM), GTC
(ARKX), and FOMC (XLU/IGF/etc.) were all carried forward at their bands, per the rule. **No 5c failure.**
One rule violation found and corrected: the ballot scored REMX 9 on a disputed date, claiming the
MOFCOM text "settles" the dispute — but the dispute table requires a primary source (the issuing
ministry / agency / company) that settles it, and no such source exists (the cited text predates the
9/24 summit; the cited link was a USADMIN measure PDF, not MOFCOM's publication). This is the basis
for the demotion below.

## Ledger changes (`log/catalysts.md`)
- APPENDED: solar | Solar IV | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | 2026-10-14 | Reuters/SRN 2026-09-11; SMM; Sxcoal | 2026-09-28
- APPENDED: solar | Solar IV | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | 2026-11-02 | Sxcoal 2026-09-14; Reuters 2026-09-11 | 2026-09-28
- UPDATED (stays in ## Disputed): rare-earth No. 70 suspension-expiry row — added the post-summit
  Bessent confirmation of the pause extension to 2027-01-10 (The Global Market Brief 9/26; chomcho;
  tamaranews 9/26) and the "no new firm commitments" counter-readings (FXStreet, InvestedAlpha). No
  MOFCOM text seen on either side. No retractions.

## Demotions
- **REMX — catalyst 9 → 6; bucket buy → watch.** What collapsed: the ballot's load-bearing claim
  that the MOFCOM No. 70 text settles the rare-earth dispute in favor of a 2026-11-10 snapback.
  The text predates the 9/24 summit and cannot settle the extension question; post-summit sources
  (Bessent via The Global Market Brief 9/26, chomcho, tamaranews) report the rare-earth export-control
  pause was extended with the truce to 2027-01-10. With no settling primary source on either reading,
  the ledger's dispute rule caps catalyst at 6. Does it change the buy/core case: **yes — REMX drops
  out of buy into watch** (gate fails: not stabilizing, catalyst 6 < 7; rare-earth is a narrow theme,
  not core-eligible). Applied by editing the catalyst ballot row + notes and re-running
  `scripts/consolidate.py` (scores.csv regenerated, never hand-edited). Final: REMX wtd 6.60, rank 16.
- **No other demotions.** NLR (buy), ARKX (buy), TAN (buy), IHI (buy), XLU (core), IGF (core) all
  confirmed from primary/first-party sources.

Post-demotion final buckets: **buy: NLR, ARKX, TAN, IHI; core: XLU, IGF; watch: REMX** (plus the rest).
