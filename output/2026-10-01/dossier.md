# dossier — 2026-10-01 (asof 2026-09-30 close)

## A. Candidates — full CSV rows

Column legend: Ticker, theme, asof, days, price, dd_52w (drawdown from 52w high),
dd_pctile (drawdown vs own 3y history; <0.10 = real event), dd_z (drawdown / vol),
vs_sma200, vs_sma50, rs_spy_3m, rs_spy_6m, rs_spy_12m (relative to SPY),
ret_10d, vol_60d, dollar_vol ($/day), tp_pct, sl_pct, dip_low_pct, rr (TP/SL reward-risk),
size_1pct, is_dip, stabilizing (ret_10d > 0), dip_score (depth rank, 0 = deepest),
price_score (computed), theme_score, is_candidate.

| Ticker | theme | price | dd_52w | dd_pctile | dd_z | vs_sma200 | rs_spy_3m | rs_spy_12m | ret_10d | rr | stabilizing | price_score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REMX | rare-earth | 64.26 | -0.413 | 0.007 | -1.04 | -0.25 | -0.29 | -0.16 | -0.050 | 4.11 | False | 6 |
| SLV | silver | 54.51 | -0.484 | 0.038 | -1.23 | -0.17 | -0.01 | +0.12 | -0.045 | 5.52 | False | 7 |
| TAN | solar | 43.97 | -0.405 | 0.027 | -1.16 | -0.20 | -0.26 | -0.16 | -0.015 | 4.50 | False | 5 |
| KWEB | china | 24.51 | -0.394 | 0.016 | -1.62 | -0.16 | -0.05 | -0.54 | +0.011 | 6.19 | True | 7 |
| URNM | nuclear | 47.46 | -0.435 | 0.021 | -0.96 | -0.21 | -0.12 | -0.35 | -0.055 | 3.94 | False | 5 |
| NLR | nuclear | 103.46 | -0.371 | 0.003 | -0.92 | -0.20 | -0.12 | -0.39 | -0.036 | 3.37 | False | 5 |
| URA | nuclear | 39.85 | -0.355 | 0.015 | -0.80 | -0.17 | -0.10 | -0.30 | -0.037 | 2.88 | False | 6 |
| SHLD | defense-us | 60.08 | -0.228 | 0.012 | -1.09 | -0.12 | -0.04 | -0.28 | -0.041 | 3.26 | False | 6 |
| XAR | defense-us | 231.25 | -0.220 | 0.001 | -0.87 | -0.14 | -0.21 | -0.16 | -0.045 | 2.56 | False | 6 |
| ITA | defense-us | 207.18 | -0.181 | 0.001 | -0.88 | -0.10 | -0.17 | -0.15 | -0.038 | 2.49 | False | 6 |
| PPA | defense-us | 154.62 | -0.164 | 0.001 | -0.86 | -0.09 | -0.15 | -0.14 | -0.032 | 2.36 | False | 7 |
| XLU | utilities | 39.44 | -0.156 | 0.004 | -1.14 | -0.10 | -0.14 | -0.23 | -0.038 | 3.13 | False | 6 |
| UFO | space | 42.32 | -0.375 | 0.001 | -1.40 | -0.10 | -0.18 | +0.03 | -0.015 | 5.19 | False | 8 |
| ARKX | space | 31.90 | -0.155 | 0.078 | -0.60 | -0.02 | -0.08 | -0.03 | +0.010 | 1.64 | True | 7 |
| PBW | clean | 29.07 | -0.372 | 0.041 | -0.99 | -0.15 | -0.26 | -0.14 | -0.019 | 3.65 | False | 6 |
| ICLN | clean | 17.00 | -0.282 | 0.007 | -1.03 | -0.10 | -0.18 | -0.05 | -0.019 | 3.32 | False | 7 |
| LIT | lithium | 68.42 | -0.250 | 0.117 | -0.98 | -0.08 | -0.15 | +0.06 | -0.021 | 3.02 | False | 5 |
| IGF | grid/infra | 61.56 | -0.100 | 0.001 | -1.22 | -0.06 | -0.09 | -0.12 | -0.023 | 3.14 | False | 7 |
| PAVE | grid/infra | 52.50 | -0.123 | 0.072 | -0.73 | -0.03 | -0.12 | -0.04 | -0.005 | 1.92 | False | 5 |
| GRID | grid/infra | 177.11 | -0.108 | 0.045 | -0.44 | +0.01 | -0.08 | +0.03 | +0.018 | 1.15 | True | 9 |
| INDA | india | 46.68 | -0.156 | 0.042 | -1.23 | -0.06 | -0.08 | -0.27 | -0.016 | 3.36 | False | 5 |
| ARGT | argentina | 86.18 | -0.160 | 0.066 | -0.75 | -0.07 | -0.08 | +0.04 | -0.077 | 2.06 | False | 6 |
| ITB | housing | 87.02 | -0.225 | 0.164 | -0.78 | -0.10 | -0.17 | -0.34 | -0.013 | 2.31 | False | 3 |
| XHB | housing | 96.03 | -0.201 | 0.113 | -0.78 | -0.09 | -0.17 | -0.28 | -0.002 | 2.27 | False | 3 |
| IHI | health-other | 51.15 | -0.203 | 0.075 | -0.85 | -0.06 | -0.00 | -0.30 | -0.015 | 2.46 | False | 4 |

## B. Leaders (rs_spy_3m) — regime

| ETF | theme | rs_spy_3m | rs_spy_6m | dd_52w |
|---|---|---|---|---|
| ETHA | crypto-spot | +0.625 | +0.092 | -0.438 |
| USO | oil/gas | +0.385 | -0.034 | -0.100 |
| IBIT | crypto-spot | +0.367 | +0.054 | -0.336 |
| ARKG | biotech | +0.247 | +0.874 | 0.000 |
| WCLD | software | +0.198 | +0.308 | -0.059 |
| SKYY | software | +0.178 | +0.321 | -0.029 |
| BUG | cyber | +0.154 | +0.661 | -0.020 |
| XLE | energy | +0.146 | -0.161 | -0.062 |

**Regime read (9/30 close):** risk-on tech/beta (crypto, software, cyber, biotech) + energy lead; the money sits in
yields' beneficiaries and duration-immune themes. The mirror image is everything duration-sensitive: 10y Treasury at
~5.2-5.28% (19-year high), Fed hiked mid-September (~9/16-9/17) and left the door open to more (70% October-hike
pricing per CME FedWatch). Bond-proxy selloff is the dominant rotation engine; XLU (-17.7% from $47.73 Feb high),
housing, solar, clean all cluster around it.

## C. Quick-pass memo (UNVERIFIED — challenge it; one search per theme, 2026-10-01)

- **rare-earth (REMX): UNCLEAR.** REMX crashed ~40% from >$110 on "war apathy" — the speculative Iran-war trade
  unwound even as bombs keep falling (barchart/butterfieldgrain, ~113 days old piece but the pattern matches).
  The thesis is geopolitical speculation, not fundamentals; the rare-earth export-control pause date is Disputed
  in the ledger. No confirmed thesis break, but the thesis itself is sentiment → unclear.
- **silver (SLV): ROTATION.** Broad precious-metals selloff Monday 9/28: 10y back above 5.2%, 30y above 5.3%, 70%
  October-hike pricing; spot gold −3% to $4,156 (7-week low), silver −5% to ~$61 (stocktwits 9/28). Physical shortage
  narrative intact: silver +150% YTD, chronic deficit, inventories near decade lows, China exports tightening in
  January (Benzinga via webull.my). Sellers are rate tourists → rotation.
- **solar (TAN): UNCLEAR leaning break.** Rate pressure (Barron's: 10y up a full point in 7 months) plus real policy
  damage: last year's tax bill cut tax subsidies for new projects, Trump admin slowed renewables permitting
  (barrons.com 9/27). TAN −10% in a month, −23% in six months. Demand lever is financing → headwind is structural,
  not just cyclical.
- **china (KWEB): UNCLEAR leaning break.** US-listed China ETFs saw ~$3.5B cumulative outflows since May, near
  12-month lows (globalmarketsinvestor 9/14); KWEB −28% YTD, −42% 1y, rejected off 50-EMA (fxempire). Regulatory
  overhang persists; the trade is value-not-catalyst → unclear.
- **nuclear (URNM/NLR/URA): ROTATION.** Policy-trade whipsaw: nuclear stocks rallied mid-week 9/16-9/17 on a House
  vote on data-center power costs, gave it back Friday (foreignpolicyjournal 9/22). URA −12% in a week mid-September
  (ortex.news). Uranium term price at 18-year high per prior runs — commodity says the seller is positioning, not
  the thesis. Cameco Q3 10/30 carried forward.
- **defense-us (SHLD/XAR/ITA/PPA): UNCLEAR.** XAR's longest weekly losing streak ever — six straight weeks, −19%
  since Aug-14 record, bear market while SPY −1.4% (TradingView/Benzinga 9/29). Driver: "peace headlines, budget
  talks" — peace-talk thesis risk is real if Iran war de-escalates, but the war is ongoing; Trump's proposed $1.5T
  2027 military budget is a positive. Genuine thesis question, no resolution → unclear.
- **utilities (XLU): ROTATION.** Pure rates story: 10y 5.284% vs XLU dividend 3.08% (Jefferies via marketwatch 9/29);
  sector at 17-month low, most oversold in 3 years (seekingalpha 9/25). Data-center power-demand thesis intact
  (marketwise: AI power boom, strong fundamental drivers). Sellers are yield tourists → rotation; core candidate.
- **space (UFO/ARKX): ROTATION.** Post-SpaceX-IPO hype unwind: UFO −40% from $68 peak on "cold physics of high
  capex, dilution risk, late-cycle valuation discipline" (barchart via cloudfront, 72 days old). No business-model
  change — valuation tourists → rotation. ARKX dip shallower (−15%), stabilized.
- **clean (PBW/ICLN): UNCLEAR leaning break.** Trump admin hostile to renewables (Fool 9/23: "policies have not
  been favorable"), subsidy cuts, rate pressure. PBW −37% from high, ICLN −28%. Some AI-green-energy demand
  offset (tech buildouts prefer green) → unclear.
- **lithium (LIT): UNCLEAR.** Spot oversupply narrative, EV adoption/policy reversals (ainvest); LIT concentrated —
  Rio Tinto now 22.87% of the fund (indmoney 10/1). 52w high $91.98 → $68.42; demand question is fundamental, not
  just flows → unclear.
- **grid/infra (IGF/PAVE/GRID): ROTATION.** Shallow rate-driven dip; AI data-center capex thesis intact — GRID is
  "the cleanest capex story of the decade" (tradingnews 9/1), PAVE was a 9/30 buy, IGF global infra diversified
  ($10.6B, 0.37%). Thesis untouched → rotation; core candidates.
- **india (INDA): UNCLEAR leaning rotation.** FII shorts at 6-month high (267k index-future shorts), Nifty −6.7%
  in September series on global bond rout (Reuters 9/30); domestic institutions cushioned. Flows, not fundamentals
  → unclear leaning rotation.
- **argentina (ARGT): UNCLEAR.** MELI 21.4% concentration; September −8.54%, peso/macro risk live, IMF targets and
  politics the swing factor (ainvest). Country-risk thesis question with no new facts → unclear.
- **housing (ITB/XHB): UNCLEAR leaning break.** 30y mortgage ~7%, new home sales −10.5% MoM July to 6-month low,
  purchase apps −5% YoY (TradingView/Kobeissi 8/26); 30y govt bond 5.6% highest since 2002 (seekingalpha 9/29).
  Rates are temporary but demand is impaired while they hold → unclear.
- **health-other (IHI): UNCLEAR leaning rotation.** Med-devices in healthcare rotation; short interest 12.1% of
  float (marketbeat); top-10 74.7% (Zacks 9/2). No thesis news, no catalyst → unclear.

## D. Confirmed catalysts carried forward — already verified, do NOT rescore as "not found"

| theme | event | date | confirmed by |
|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 |
| macro | FOMC decision | **2026-10-28** | federalreserve.gov FOMC calendar; re-verified 2026-09-29 |
| macro | FOMC decision | **2026-12-09** | federalreserve.gov FOMC calendar; re-verified 2026-09-29 |
| ai/robot | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | **2027-03-14** | nvidia.com GTC FAQ |
| solar | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | **2026-10-14** | Reuters/SRN 2026-09-11; SMM; Sxcoal; re-verified 2026-09-29 (solarpowerworld 9/20, Sxcoal 9/14, pv-magazine) |
| solar | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | **2026-11-02** | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 (Sxcoal, pv-magazine, taiyangnews) |

A panelist that cannot re-find one of these writes "carried forward, not re-searched" and keeps the band the date
earns. It does not score the theme down for having no dated trigger, and never calls it "unverified": only a cited
source that CONTRADICTS the date overturns it (write "CONTRADICTED: <source>"; the verifier then marks the ledger
row RETRACTED). check_memo.py fails a ballot that doubts a live row without one.

### Disputed — sources contradict each other; neither date is confirmed

| theme | claim | readings | sources |
|---|---|---|---|
| rare-earth | China's suspension of its Oct-2025 rare-earth export controls (MOFCOM Announcement No. 70) | (a) expires 2026-11-10 with automatic snapback — MOFCOM No. 70 text (2025-11-07, pre-summit), per Sphera and pre-summit SilmarilMedia; (b) the rare-earth export-control pause was extended with the truce to 2027-01-10 — Bessent confirmed post-9/24-summit (The Global Market Brief 9/26; chomcho; tamaranews 9/26). Some outlets (FXStreet, InvestedAlpha) report no *new* firm rare-earth commitments. No MOFCOM text seen on either side | (a) MOFCOM No. 70 text; (b) Bessent via The Global Market Brief 9/26, chomcho, tamaranews 9/26; post-summit: Bessent Fox News 9/24 announced the Nov-10 → 2027-01-10 extension (WSJ headline via killbait; tokenpost; roic; pressinsider — which notes Beijing did not separately announce the date); silmarilmedia 9/29: "a 61-day reprieve with no binding commitments on rare earth supply volumes, no resolution of the April 2025 licensing architecture"; neuralwired 9/26: extension "preserves China's suspension of rare earth export controls". Still no MOFCOM text on either side — stays Disputed |

A catalyst score of 7+ that rests on a disputed date must cite a primary source (the issuing ministry / agency /
company) that settles it; otherwise score only what holds under both readings.
