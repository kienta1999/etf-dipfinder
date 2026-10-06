> Run by: Muse AI (underlying model not recorded) — annotated 2026-10-06 from the owner's record, not by the run itself.

# Dossier — 2026-09-29 (scan asof 2026-09-28 close)

**DO NOT trust this dossier blindly. It is an unverified quick-pass memo — panelists must challenge every claim.**

## Scan state

- Candidates: **25** across **15 themes**.
- vs prior run (frozen 2026-09-25 scan): **GRID entered**, **SHLD exited**.
- All 105 universe rows changed; close date is now 2026-09-28.
- `data/scan.csv` is source of truth. BJK download 404'd and was skipped (as in prior runs); scan still exited 0.

## Candidate rows (exact, from data/scan.csv)

Columns: `ticker | theme | price | dd_52w | vs_sma200 | vs_sma50 | rs_spy_3m | ret_10d | vol_60d | dollar_vol_M | stabilizing | price_score`

| ticker | theme | price | dd_52w | vs_sma200 | vs_sma50 | rs_spy_3m | ret_10d | vol_60d | dollar_vol_M | stabilizing | price_score |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TAN | solar | 43.00 | −41.84% | −21.78% | −12.35% | −0.289 | −6.97% | 0.362 | 35.8 | false | 6 |
| REMX | rare-earth | 64.47 | −41.14% | −25.06% | −11.46% | −0.289 | −6.47% | 0.407 | 37.3 | false | 5 |
| KWEB | china | 24.66 | −39.07% | −15.91% | −6.56% | −0.021 | −0.28% | 0.247 | 334.5 | false | 5 |
| URNM | nuclear | 47.92 | −42.95% | −20.83% | −10.03% | −0.134 | −5.35% | 0.464 | 32.1 | false | 4 |
| NLR | nuclear | 103.97 | −36.75% | −19.75% | −8.70% | −0.147 | −5.02% | 0.417 | 38.5 | false | 5 |
| URA | nuclear | 40.13 | −35.08% | −16.68% | −7.28% | −0.122 | −4.88% | 0.455 | 130.6 | false | 6 |
| XLU | utilities | 39.25 | −16.05% | −10.45% | −8.44% | −0.177 | −5.46% | 0.137 | 984.9 | false | 6 |
| ICLN | clean | 16.81 | −29.03% | −10.49% | −5.42% | −0.190 | −4.27% | 0.287 | 125.7 | false | 7 |
| PBW | clean | 28.97 | −37.43% | −15.64% | −9.54% | −0.269 | −3.84% | 0.397 | 10.4 | false | 4 |
| QCLN | clean | 47.75 | −30.26% | −8.74% | −4.51% | −0.225 | +0.42% | 0.392 | 5.2 | true | 8 |
| GLD | gold | 377.91 | −23.79% | −9.24% | −4.48% | −0.011 | −3.80% | 0.250 | 3853.0 | false | 6 |
| UFO | space | 42.91 | −36.64% | −9.16% | −4.03% | −0.163 | −0.12% | 0.276 | 8.4 | false | 8 |
| ARKX | space | 32.07 | −15.02% | −0.99% | −0.92% | −0.068 | +1.33% | 0.273 | 12.0 | true | 7 |
| XAR | defense-us | 234.19 | −21.03% | −12.41% | −11.04% | −0.190 | −3.51% | 0.264 | 75.8 | false | 7 |
| ITA | defense-us | 209.26 | −17.26% | −9.04% | −10.00% | −0.160 | −3.35% | 0.210 | 180.0 | false | 7 |
| PPA | defense-us | 156.24 | −15.47% | −8.48% | −8.28% | −0.130 | −2.45% | 0.195 | 40.0 | false | 7 |
| LIT | lithium | 68.28 | −25.15% | −8.39% | −5.43% | −0.153 | −2.42% | 0.262 | 14.7 | false | 5 |
| IGF | grid/infra | 62.02 | −9.34% | −4.82% | −4.93% | −0.115 | −2.16% | 0.082 | 56.4 | false | 7 |
| PAVE | grid/infra | 53.08 | −11.36% | −2.07% | −4.79% | −0.130 | +0.11% | 0.177 | 86.2 | true | 7 |
| GRID | grid/infra | 177.53 | −10.61% | +1.09% | −1.29% | −0.091 | +2.83% | 0.252 | 89.4 | true | 8 |
| INDA | india | 47.09 | −14.83% | −5.79% | −4.14% | −0.078 | −2.77% | 0.129 | 247.3 | false | 4 |
| IHI | health-other | 51.96 | −19.01% | −4.78% | −2.35% | −0.009 | +0.35% | 0.238 | 123.4 | true | 6 |
| ITB | housing | 88.75 | −20.91% | −8.23% | −5.57% | −0.175 | −0.61% | 0.290 | 198.4 | false | 3 |
| XHB | housing | 97.30 | −19.02% | −7.85% | −5.93% | −0.188 | −0.43% | 0.258 | 189.9 | false | 3 |
| ARGT | argentina | 86.48 | −15.69% | −6.41% | −7.52% | −0.091 | −9.40% | 0.223 | 13.2 | false | 6 |

Full rows with all computed columns (dd_pctile, dd_z, rs_spy_6m, rs_spy_12m, tp_pct, sl_pct, dip_low_pct, rr, size_1pct, dip_score, theme_score): `data/scan.csv`.

## Leaders (2026-09-28 close scan, rs_spy_3m)

1. ETHA crypto-spot, +0.610
2. USO oil/gas, +0.365
3. IBIT crypto-spot, +0.345
4. WCLD software, +0.230
5. ARKG biotech, +0.224
6. BUG cyber, +0.191
7. SKYY software, +0.187
8. IGV software, +0.137

## Regime (as of 2026-09-29 morning PT)

- **10y Treasury:** closed 5.241% on 2026-09-28 — 19-year closing high (intraday 5.272%).
  Sources: WSJ live coverage 9/28/2026; Morningstar/Dow Jones data talk.
- **Fed:** funds target 3.75–4.00% after the 9/16 hike; ~70.3% odds of an October hike (CME FedWatch, per 9/28 reporting).
- **Brent:** settled $105.28 on 9/28; ~$105.9–106.8 early 9/29 amid Hormuz disruption + US–Iran talks. WTI ~$96.33 (per 9/28 reporting).
- **Gold spot:** ~$4,146–4,156/oz on 9/28, seven-week low (−3.3%); GLD $380.99 in 9/28 reporting.
- Macro frame: bond selloff deepening (30y >5.3%), rate-hike expectations dominating gold/geopolitics; oil up on Hormuz/Iran, which is being read as an inflation shock pushing yields higher, not a safe-haven bid.

## Carry-forward catalysts (scripts/carry_forward.py, 2026-09-29)

### Confirmed
| theme | catalyst | date |
|---|---|---|
| nuclear | Cameco Q3 results before market open | 2026-10-30 |
| macro | FOMC decision | 2026-10-28 |
| macro | FOMC decision | 2026-12-09 |
| ai/robot | NVIDIA GTC 2027 | 2027-03-14 |
| solar | USITC final injury vote on Solar IV AD/CVD | 2026-10-14 |
| solar | Commerce final Solar IV AD/CVD orders | 2026-11-02 |

### Disputed — rare-earth
| claim | source status |
|---|---|
| China's rare-earth-controls suspension expires 2026-11-10 | one reading of carried ledger |
| Pause extended to 2027-01-10 | another reading of carried ledger |

No primary MOFCOM text settling the conflict was found in the ledger. **A catalyst score ≥7 must NOT rest on this disputed date without primary-source resolution.**

## Theme quick-pass (UNVERIFIED — challenge it)

### 1. solar — TAN
Selling tied strongly to higher project-financing costs; TAN fell sharply while demand remains. Solar IV AD/CVD confirmed catalysts: USITC final injury vote 10/14, Commerce final orders 11/2.
Source: summamoney.com 9/28 report on solar stocks sliding on high borrowing costs (First Solar −8%, SolarEdge −5%, Enphase −4%).

### 2. rare-earth — REMX
Strategic need intact (China dominates processing/magnets); November deadline disputed — one reading says China's export-control suspension expires 2026-11-10, another says extended to 2027-01-10. No primary MOFCOM text. Catalyst ≥7 cannot rest on the date.
Source: rareearthexchanges.com (controls-expiry explainer); disputed ledger entries.

### 3. china — KWEB
Mixed: broad China-ETF outflows + sanctions risk — more than a clean technical rotation; evidence does not clearly support "panic oversold" alone.
Source: adalytica.com (FXI/KWEB sanctions risk).

### 4. nuclear — URNM, NLR, URA
Uranium spot ~$89.70/lb and term ~$96.50/lb while uranium equities sold off — commodity/equity divergence; fuel thesis intact. Reactor/developer names carry execution risk. Cameco Q3 results before market open 10/30 is the live catalyst.
Source: discoveryalert.com (Sept 2026 nuclear-equities analysis).

### 5. utilities — XLU
Dividend yield ~3.08% vs 10y ~5.23–5.24%: selling is heavily rate/bond-proxy driven. Data-center power demand structurally supportive. XLU at 17-month low per reporting.
Source: MarketWatch live coverage 9/28 (utilities sink to 17-month low).

### 6. clean — ICLN, PBW, QCLN
Rate sensitivity is the main shared mechanism, but policy/subsidy risk and constituent quality are real (PBW is small-cap concentrated and more volatile). QCLN flagged stabilizing=true by scan.

### 7. gold — GLD
GLD down ~3.2% to ~$380.99 on 9/28 with spot at seven-week low ~$4,146–4,156; drivers are 10y at 5.22% (highest since 2007), 70.3% October-hike odds, stronger dollar, higher oil. State Street gold strategist: may test $4,000 within a week on rate fears but $5,000 still possible within six months; central banks bought a record 289t in Q2 (+62% y/y).
Sources: tradingnews.com, stocktwits/Reuters, investinglive.com (State Street/Kitco).

### 8. space — UFO, ARKX
SpaceX Starship Flight 14 on 9/28 successfully reached orbit and deployed 26 Starlink V3 satellites (engine issues shortened the mission; first orbital flight). Event catalyst realized; whether it sustains multiple expansion in UFO/ARKX is the open question.
Sources: space.com live updates; nss.org (first orbital flight of Starship).

### 9. defense-us — XAR, ITA, PPA
Evidence points to high yields + investor fatigue/profit-taking and valuation compression rather than demand collapse; order/spending thesis remains. No demand-destruction headline found.

### 10. lithium — LIT
Chinese inventories and mine restarts created genuine oversupply risk; lithium carbonate fell below CNY135,000/tonne (8-month low). This is a fundamental-demand question, not pure rate noise.
Source: tradingview.com news (te_news:584982).

### 11. grid/infra — IGF, PAVE, GRID
GRID entered the candidate set this run (price 177.53, dd −10.61%, stabilizing=true). Underlying AI/power demand and equipment backlogs intact; GRID holds Eaton, Schneider, ABB, Quanta, Johnson Controls; investors reportedly added $283M into the falling fund as Dell's $95B AI backlog named power.
Source: tradingnews.com (GRID ETF flow story).

### 12. india — INDA
FPIs dumped ₹23,676 crore of Indian equities in September through 9/19 — reversing July+August inflows — on crude surge + bond-yield fears (US 10y near 5%). Primary market holding up; Elara notes India-focused outflows moderated vs Taiwan/Korea but absolute trend still weak.
Sources: nationpress.com; ianslive.in / indusbusinessjournal.com (Elara Capital).

### 13. health-other — IHI
IHI (med devices: Abbott ~18%, ISRG, Medtronic) is down ~12.5% YTD / ~−17% per one source, flagged stabilizing=true by scan. Biotech is rallying (XBI +29%, ARKG +84% YTD) on M&A/innovation, but med-tech is weighed down by TMO/DHR-style health-tech weakness; short interest ~12% of float. Contrast with biotech strength suggests sub-sector rotation rather than healthcare collapse.
Sources: tickeron.com, talkmarkets.com (9/28), Zacks, MarketBeat short interest.

### 14. housing — ITB, XHB
New-home sales plunged 10.5% m/m in July (607k, weakest since Nov 2022 excl. Jan); 30y mortgage near 7%; the 9/16 Fed hike kept yield pressure on. Structural shortage (3–4M homes) intact but builders' margin/incentive economics are deteriorating; 10y >4.75% keeps the housing short on per one desk.
Sources: tradingview.com (Benzinga), thecheapinvestor.com (9/5).

### 15. argentina — ARGT
No fresh election catalyst (midterms were Oct 2025, already priced). Current pressure: reserves slipping (gross ~$48.2B after a ~$800M IMF payment 9/25), peso at new nominal highs (~1,521 mayorista), country risk >600 bps, Treasury burning ~$1.5B over six sessions defending the peso (reported ~$700M left in dollar coffers per Bloomberg Law); 2027 election already looking contested with Milei approval ~34%. ARGT up only ~5% YTD 2026 vs 12% S&P.
Sources: particle.news, Bloomberg Law, economicaffairs.co.uk.

## Notes for panelists

- GRID is new; SHLD is gone (was a candidate in the prior run).
- Stabilizing=true this run: QCLN, ARKX, PAVE, GRID, IHI.
- Theme sibling deviations (nuclear has 3, clean has 3, defense has 3, grid/infra has 3, space has 2, housing has 2) must be explained in ballots, not silently split.
- Buy gate (README §2): cause ≥ 7 and (stabilizing or catalyst ≥ 7) and not thin and theme_rank == 1.
