> Run by: Claude Opus 5.5 (claude-opus-5-5) — annotated 2026-10-06 from the owner's record, not by the run itself.

# Dossier — 2026-10-04 (panel; clean rerun, scan as of Friday 2026-10-02 close)

Clean rerun: every prior 2026-10-04 artifact (output/2026-10-04/, log/2026-10-04.md, the two catalyst-ledger
rows verified on 2026-10-04) was deleted before this run at the user's request — nothing below is inherited
from the earlier 10-04 run. Fresh scan.py, fresh quick-pass searches.

## A. Candidates (25 dips in top 15 themes; scan.py 2026-10-04, asof 2026-10-02 close)

Legend: dd_52w = drawdown from 52w high; dd_pctile = how deep vs own 3y history (<0.10 = real event);
dd_z = drawdown / vol (vol-normalised depth); vs_sma200 = price vs 200-day SMA; rs_spy_3m/6m/12m = return
relative to SPY; ret_10d = 10-day return; stabilizing = ret_10d > 0; dip_score = depth rank (0 = deepest,
NOT quality); price_score = consolidate.price_score() (depth + trend + 2 if stabilizing) — the price lens,
computed, never voted; tp_pct = back to 52w high; sl_pct = stop; rr = reward/risk (thin if < 1.3).

| ETF | theme | dd_52w | dd_pctile | dd_z | vs_sma200 | rs_spy_3m | rs_spy_6m | rs_spy_12m | ret_10d | stabilizing | dip_score | price_score | tp_pct | sl_pct | rr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REMX | rare-earth | -0.423 | 0.007 | -1.07 | -0.264 | -0.286 | -0.469 | -0.217 | -0.085 | False | 0.076 | 6 | 0.733 | -0.172 | 4.27 |
| TAN | solar | -0.404 | 0.031 | -1.14 | -0.197 | -0.261 | -0.376 | -0.187 | -0.035 | False | 0.088 | 5 | 0.678 | -0.153 | 4.44 |
| KWEB | china | -0.410 | 0.003 | -1.75 | -0.181 | -0.095 | -0.330 | -0.567 | -0.039 | False | 0.089 | 5 | 0.696 | -0.101 | 6.87 |
| FXI | china | -0.190 | 0.029 | -1.12 | -0.080 | -0.005 | -0.239 | -0.347 | -0.033 | False | 0.285 | 5 | 0.235 | -0.074 | 3.19 |
| URNM | nuclear | -0.435 | 0.022 | -0.97 | -0.214 | -0.142 | -0.432 | -0.342 | -0.058 | False | 0.101 | 5 | 0.771 | -0.194 | 3.97 |
| NLR | nuclear | -0.375 | 0.003 | -0.93 | -0.204 | -0.145 | -0.411 | -0.398 | -0.046 | False | 0.139 | 5 | 0.600 | -0.174 | 3.45 |
| URA | nuclear | -0.356 | 0.016 | -0.81 | -0.172 | -0.120 | -0.366 | -0.300 | -0.045 | False | 0.227 | 6 | 0.553 | -0.191 | 2.89 |
| SLV | silver | -0.482 | 0.040 | -1.25 | -0.170 | -0.051 | -0.347 | 0.112 | -0.087 | False | 0.114 | 7 | 0.929 | -0.166 | 5.58 |
| SHLD | defense-us | -0.226 | 0.016 | -1.12 | -0.113 | -0.098 | -0.362 | -0.300 | -0.039 | False | 0.152 | 6 | 0.291 | -0.087 | 3.33 |
| XAR | defense-us | -0.214 | 0.004 | -0.85 | -0.128 | -0.222 | -0.281 | -0.177 | -0.028 | False | 0.265 | 6 | 0.272 | -0.109 | 2.49 |
| ITA | defense-us | -0.178 | 0.003 | -0.89 | -0.097 | -0.197 | -0.241 | -0.168 | -0.028 | False | 0.303 | 6 | 0.217 | -0.087 | 2.49 |
| PPA | defense-us | -0.158 | 0.004 | -0.83 | -0.088 | -0.171 | -0.259 | -0.160 | -0.023 | False | 0.323 | 6 | 0.187 | -0.082 | 2.29 |
| UFO | space | -0.363 | 0.019 | -1.33 | -0.088 | -0.170 | -0.301 | 0.031 | -0.002 | False | 0.165 | 8 | 0.570 | -0.118 | 4.83 |
| ARKX | space | -0.134 | 0.135 | -0.51 | 0.007 | -0.068 | -0.102 | -0.033 | 0.017 | True | 0.791 | 6 | 0.155 | -0.113 | 1.37 |
| XLU | utilities | -0.148 | 0.011 | -1.07 | -0.090 | -0.141 | -0.308 | -0.233 | -0.024 | False | 0.197 | 6 | 0.174 | -0.060 | 2.91 |
| PBW | clean | -0.362 | 0.070 | -0.96 | -0.139 | -0.233 | -0.236 | -0.178 | -0.028 | False | 0.253 | 4 | 0.568 | -0.163 | 3.49 |
| ICLN | clean | -0.274 | 0.012 | -1.00 | -0.085 | -0.173 | -0.225 | -0.070 | -0.021 | False | 0.310 | 7 | 0.378 | -0.119 | 3.18 |
| GLD | gold | -0.233 | 0.044 | -0.94 | -0.086 | -0.032 | -0.294 | -0.096 | -0.052 | False | 0.266 | 6 | 0.304 | -0.108 | 2.83 |
| IGF | grid/infra | -0.097 | 0.004 | -1.16 | -0.053 | -0.106 | -0.254 | -0.126 | -0.022 | False | 0.299 | 7 | 0.108 | -0.036 | 2.97 |
| PAVE | grid/infra | -0.100 | 0.124 | -0.58 | -0.008 | -0.095 | -0.127 | -0.022 | 0.017 | True | 0.709 | 6 | 0.112 | -0.075 | 1.49 |
| LIT | lithium | -0.241 | 0.154 | -0.95 | -0.072 | -0.117 | -0.241 | 0.048 | -0.017 | False | 0.343 | 5 | 0.317 | -0.109 | 2.90 |
| ARGT | argentina | -0.176 | 0.054 | -0.81 | -0.085 | -0.128 | -0.276 | 0.102 | -0.086 | False | 0.348 | 6 | 0.213 | -0.094 | 2.27 |
| ITB | housing | -0.228 | 0.154 | -0.82 | -0.102 | -0.165 | -0.210 | -0.352 | -0.009 | False | 0.366 | 2 | 0.295 | -0.120 | 2.45 |
| XHB | housing | -0.195 | 0.128 | -0.79 | -0.082 | -0.153 | -0.188 | -0.287 | 0.009 | True | 0.455 | 5 | 0.242 | -0.107 | 2.27 |
| INDA | india | -0.159 | 0.041 | -1.28 | -0.067 | -0.094 | -0.182 | -0.276 | -0.031 | False | 0.374 | 5 | 0.189 | -0.053 | 3.52 |

Themes ranked by depth: rare-earth, solar, china, nuclear, silver, defense-us, space, utilities, clean,
gold, grid/infra, lithium, argentina, housing, india. Sibling groups: KWEB/FXI; URNM/NLR/URA;
SHLD/XAR/ITA/PPA; UFO/ARKX; PBW/ICLN; IGF/PAVE; ITB/XHB. Thin (R/R < 1.3): none (ARKX 1.37 and PAVE 1.49
are closest). Stabilizing: ARKX, PAVE, XHB only.

## B. Leaders (rs_spy_3m) — where the money went

| ETF | theme | rs_spy_3m | rs_spy_6m | dd_52w |
|---|---|---|---|---|
| ETHA | crypto-spot | 0.457 | 0.107 | -0.438 |
| USO | oil/gas | 0.385 | -0.111 | -0.090 |
| IBIT | crypto-spot | 0.294 | 0.078 | -0.330 |
| ARKG | biotech | 0.212 | 0.794 | -0.004 |
| SKYY | software | 0.195 | 0.324 | -0.005 |
| WCLD | software | 0.182 | 0.305 | -0.044 |
| XOP | oil/gas | 0.179 | -0.130 | -0.070 |
| XLE | energy | 0.162 | -0.105 | -0.042 |

Money went to oil/energy (USO/XOP/XLE), crypto (rebounding from deep drawdowns — ETHA still −44% off high),
biotech and software. The dips are the mirror: long-duration and rate-sensitive themes (utilities, housing,
solar/clean, grid), no-yield metals (gold, silver) and 2025-26 momentum trades (nuclear, defense, space,
rare-earth). That is one rotation — a rates shock — not 15 separate problems.

## C. Quick-pass memo (UNVERIFIED — challenge it; one search per theme, 2026-10-04)

Regime as read from today's searches: Fed hiked 25bp on 2026-09-16 to 3.75–4.00% (discoveryalert, kitco);
10y Treasury peaked ~5.33% (multi-decade high) and eased from it Oct 1–2 (CNBC 10/1 "Treasury yields fall from
multiyear highs"; TLT best day in a month on 10/2); one source cites ~94% December hike odds (Yahoo, silver
piece) — not confirmed against CME. Gold −6% in September, worst month since June.

- **rare-earth (REMX) — rotation.** YTD −14.4% at 10/2 (VanEck). Trump–Xi thaw (September meeting) eroded the
  scarcity premium on Western producers; no company-specific news from top holdings (tickeron; rareearthexchanges
  on Benzinga). The ledger's MOFCOM No. 70 expiry is still Disputed (2026-11-10 vs 2027-01-10) — see §D.
- **solar (TAN) — break-leaning.** −27% since late June, rates (Seeking Alpha downgrade to hold); 52w range
  42.46–75.60. Policy backdrop (2025 tax bill cut residential 25D / phases 48E) is the thesis question for
  cause. §D dates: USITC final vote 10/14, Commerce final AD/CVD orders 11/02.
- **china (KWEB, FXI) — unclear.** KWEB YTD NAV −28% at 10/2 (KraneShares); overcapacity, weak domestic
  consumption (pluang). No fund-specific break; FXI is the broad large-cap sibling, much shallower (−19%).
- **nuclear (URNM, NLR, URA) — rotation.** NLR ~35% off 1/28 peak; selling clustered after Q1 hyperscaler calls
  as the market moved from celebrating AI capex to questioning it (VanEck "The Nuclear Reset"); NLR −12% in a
  month (MarketBeat). Thesis question = AI-power demand; §D: Cameco Q3 10/30.
- **silver (SLV) — rotation, high beta.** Silver ~$60.4/oz 10/2, −9.9% 1m, still +26% y/y (tradingeconomics);
  SLV ~50% below 52w high $109.83 (Yahoo) — the yield high crushed both monetary and industrial cases.
- **defense-us (SHLD, XAR, ITA, PPA) — rotation (sentiment).** XAR/ITA six straight weekly losses, XAR longest
  losing streak in its history, ~21% off peak = bear market; 42 of 50 XAR names fell in September; biggest losers
  defense-tech (Axon −25%, Red Cat −24%) (Benzinga/TradingView). RSI ITA 22, XAR 18 (Investing.com). No budget
  cut cited — positioning/valuation unwind.
- **space (UFO, ARKX) — rotation-leaning, valuation.** SpaceX-fueled rally losing momentum, UFO −9% in recent
  trading, 3m −17% (MarketBeat, stockanalysis). ARKX shallower (−13%), above its SMA200, stabilizing.
- **utilities (XLU) — rotation.** −6% in September, steepest monthly drop since 2023, ~17% off 52w high; 10y >5.2%
  vs XLU yield ~3.05% (24/7 Wall St 10/2; Seeking Alpha "oversold"); CNBC 10/2 "poised for a bounce". AI-power
  demand backdrop intact.
- **clean (PBW, ICLN) — break-leaning.** ICLN YTD +3.2% at 10/2 after being +27% mid-year (iShares); same policy
  question as solar; PBW small/micro-cap, 0.6% fee.
- **gold (GLD) — rotation.** Gold $4,140 10/2, −7.5% 1m, +6.5% y/y (tradingeconomics); worst month since June on
  the hike and 5.3% 10y (discoveryalert); Goldman keeps bullish view on CB buying (TheStreet); Garner tactical
  buy but bearish at $4,500 (Kitco 10/1).
- **grid/infra (IGF, PAVE) — rotation.** No selloff story found; IGF YTD +1.5% (9/30), PAVE YTD +22% — the dip is
  the rate-driven de-rating of yield infrastructure (IGF holds utilities/pipelines/toll roads). PAVE stabilizing.
- **lithium (LIT) — unclear.** LIT +1.55% to $69.28 on 10/2; Sept 10 slide on "well-supplied physical market"
  (Rio Times); China lithium futures shut for National Day through 10/8. §D: Albemarle Q3 11/04.
- **argentina (ARGT) — unclear.** Search returned the 2025 swap/midterm episode, not a 2026 one — no current
  catalyst found; MELI ~21% of fund (prior runs). Treat as unexplained.
- **housing (ITB, XHB) — rates headwind.** Search returned mostly stale (2025) articles; XHB YTD −5.1% at 10/2
  (stockanalysis). 30y mortgage ~7% per prior runs — panel must re-establish. §D: D.R. Horton Q4/FY26 10/29.
  XHB stabilizing.
- **india (INDA) — unclear/flows.** Nifty/Sensex headed for 8th straight weekly loss, longest in 25 years;
  foreigners sold \$27.8B YTD; tariffs, weak rupee, high US yields, elevated crude (Rallies, whalesbook,
  multibagg). INDA −10% YTD.

Lone/idiosyncratic: rare-earth (trade diplomacy), space (SpaceX valuation reset), defense (positioning).
The rest are one cluster around the Sep-16 hike and the 5%+ 10y.

## D. Confirmed catalysts carried forward — already verified, do NOT rescore as 'not found'

| theme | event | date | confirmed by |
|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 and 2026-10-01 (BusinessWire 20260730139928: "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026") |
| macro | FOMC decision (Oct 27-28 meeting, statement on second day) | **2026-10-28** | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01 |
| macro | FOMC decision (Dec 8-9 meeting, statement on second day) | **2026-12-09** | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01 |
| ai/robot | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | **2027-03-14** | nvidia.com GTC FAQ |
| solar | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | **2026-10-14** | Reuters/SRN 2026-09-11; SMM; Sxcoal; re-verified 2026-09-29 (solarpowerworld 9/20, Sxcoal 9/14, pv-magazine) and 2026-10-01 (pv-tech.org 9/15: "Commission is scheduled to make its final determination on 14 October 2026") |
| solar | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | **2026-11-02** | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 (Sxcoal, pv-magazine, taiyangnews) and 2026-10-01 (pv-tech.org 9/15: "final AD/CVD duty orders, currently scheduled for 2 November 2026") |
| housing | D.R. Horton Q4/FY26 results, before market open, 8:30 a.m. ET call | **2026-10-29** | D.R. Horton investor site press release, 2026-09-10 (BusinessWire): "will release financial results for its fourth quarter and fiscal year ended September 30, 2026 on Thursday, October 29, 2026 before the market opens" |
| lithium | Albemarle Q3 2026 results, after NYSE close; earnings call Nov 5, 8:00 a.m. EST | **2026-11-04** | Albemarle PR Newswire, 2026-10-01: "will release its third quarter 2026 earnings after the NYSE closes on Wednesday, November 4, 2026" |

A panelist that cannot re-find one of these writes "carried forward, not re-searched" and keeps
the band the date earns. It does not score the theme down for having no dated trigger, and never
calls it "unverified": only a cited source that CONTRADICTS the date overturns it (write
"CONTRADICTED: <source>"; the verifier then marks the ledger row RETRACTED). check_memo.py fails
a ballot that doubts a live row without one.

### Disputed — sources contradict each other; neither date is confirmed

| theme | claim | readings | sources |
|---|---|---|---|
| rare-earth | China's suspension of its Oct-2025 rare-earth export controls (MOFCOM Announcement No. 70) | (a) expires 2026-11-10 with automatic snapback — MOFCOM No. 70 text (2025-11-07, pre-summit), per Sphera and pre-summit SilmarilMedia; (b) the rare-earth export-control pause was extended with the truce to 2027-01-10 — Bessent confirmed post-9/24-summit (The Global Market Brief 9/26; chomcho; tamaranews 9/26). Some outlets (FXStreet, InvestedAlpha) report no *new* firm rare-earth commitments. No MOFCOM text seen on either side | (a) MOFCOM No. 70 text; (b) Bessent via The Global Market Brief 9/26, chomcho, tamaranews 9/26; post-summit: Bessent Fox News 9/24 announced the Nov-10 → 2027-01-10 extension (WSJ headline via killbait; tokenpost; roic; pressinsider — which notes Beijing did not separately announce the date); silmarilmedia 9/29: "a 61-day reprieve with no binding commitments on rare earth supply volumes, no resolution of the April 2025 licensing architecture"; neuralwired 9/26: extension "preserves China's suspension of rare earth export controls". Still no MOFCOM text on either side — stays Disputed |

A catalyst score of 7+ that rests on a disputed date must cite a primary source (the issuing
ministry / agency / company) that settles it; otherwise score only what holds under both readings.

