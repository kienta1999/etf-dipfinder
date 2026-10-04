# etf-dip-pick dossier — 2026-10-04 (data as of 2026-10-02 Friday close)

## A. Candidates (25 in 15 themes) — CSV rows with column legend

Column legend: `theme` = same-headline group; `asof` = price date; `days` = lookback window; `price` = close;
`dd_52w` = drawdown from 52w high; `dd_pctile` = drawdown percentile vs own 3y history; `dd_z` = z-score of drawdown;
`vs_sma200` / `vs_sma50`; `rs_spy_3m/6m/12m` = return vs SPY; `ret_10d` = last-10-day return; `vol_60d` = 60d vol;
`dollar_vol` = $ daily volume; `tp_pct`/`sl_pct` = +52w-high / −2σ stop sizing from consolidate; `dip_low_pct` =
distance below dip low; `rr` = reward/risk; `size_1pct` = 1%-risk position size fraction; `is_dip` = dip gate;
`stabilizing` = ret_10d ≥ 0; `dip_score` = depth (CSV rank, never the memo's); `price_score` = computed price lens
(depth dd_pctile: ≤.02→5, ≤.05→4, ≤.10→3, ≤.25→2 else 1) + (trend rs_spy_12m: >0→3, >−.15→2, >−.35→1 else 0) + (2 if
stabilizing); `theme_score` = best dip_score in the theme.

| ETF | theme | price | dd_52w | dd_pctile | vs_sma200 | rs_spy_3m | ret_10d | stabilizing | dip_score | price_score | tp_pct | sl_pct | rr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REMX | rare-earth | 63.21 | -42% | 0.007 | -26% | -29% | -8.5% | False | 0.076 | 6 | +73% | -17% | 4.3 |
| TAN | solar | 44.05 | -40% | 0.031 | -20% | -26% | -3.5% | False | 0.089 | 5 | +68% | -15% | 4.4 |
| KWEB | china | 23.86 | -41% | 0.003 | -18% | -9% | -3.9% | False | 0.089 | 5 | +70% | -10% | 6.9 |
| FXI | china | 33.19 | -19% | 0.029 | -8% | -1% | -3.3% | False | 0.285 | 5 | +24% | -7% | 3.2 |
| URNM | nuclear | 47.42 | -44% | 0.022 | -21% | -14% | -5.8% | False | 0.101 | 5 | +77% | -19% | 4.0 |
| NLR | nuclear | 102.74 | -37% | 0.003 | -20% | -15% | -4.6% | False | 0.139 | 5 | +60% | -17% | 3.4 |
| URA | nuclear | 39.79 | -36% | 0.016 | -17% | -12% | -4.5% | False | 0.227 | 6 | +55% | -19% | 2.9 |
| SLV | silver | 54.74 | -48% | 0.040 | -17% | -5% | -8.7% | False | 0.114 | 7 | +93% | -17% | 5.6 |
| SHLD | defense-us | 60.23 | -23% | 0.016 | -11% | -10% | -3.9% | False | 0.152 | 6 | +29% | -9% | 3.3 |
| XAR | defense-us | 233.09 | -21% | 0.004 | -13% | -22% | -2.8% | False | 0.265 | 6 | +27% | -11% | 2.5 |
| ITA | defense-us | 207.79 | -18% | 0.003 | -10% | -20% | -2.8% | False | 0.303 | 6 | +22% | -9% | 2.5 |
| PPA | defense-us | 155.69 | -16% | 0.004 | -9% | -17% | -2.3% | False | 0.323 | 6 | +19% | -8% | 2.3 |
| UFO | space | 43.13 | -36% | 0.019 | -9% | -17% | -0.2% | False | 0.165 | 8 | +57% | -12% | 4.8 |
| ARKX | space | 32.68 | -13% | 0.135 | +1% | -7% | +1.7% | True | 0.792 | 6 | +15% | -11% | 1.4 |
| XLU | utilities | 39.83 | -15% | 0.011 | -9% | -14% | -2.4% | False | 0.197 | 6 | +17% | -6% | 2.9 |
| PBW | clean | 29.52 | -36% | 0.070 | -14% | -23% | -2.8% | False | 0.253 | 4 | +57% | -16% | 3.5 |
| ICLN | clean | 17.19 | -27% | 0.012 | -9% | -17% | -2.1% | False | 0.310 | 7 | +38% | -12% | 3.2 |
| GLD | gold | 380.14 | -23% | 0.044 | -9% | -3% | -5.2% | False | 0.266 | 6 | +30% | -11% | 2.8 |
| IGF | grid/infra | 61.76 | -10% | 0.004 | -5% | -11% | -2.2% | False | 0.299 | 7 | +11% | -4% | 3.0 |
| PAVE | grid/infra | 53.88 | -10% | 0.124 | -1% | -10% | +1.7% | True | 0.709 | 6 | +11% | -7% | 1.5 |
| LIT | lithium | 69.28 | -24% | 0.154 | -7% | -12% | -1.7% | False | 0.343 | 5 | +32% | -11% | 2.9 |
| ARGT | argentina | 84.52 | -18% | 0.055 | -8% | -13% | -8.6% | False | 0.348 | 6 | +21% | -9% | 2.3 |
| ITB | housing | 86.64 | -23% | 0.154 | -10% | -16% | -0.9% | False | 0.366 | 2 | +30% | -12% | 2.5 |
| XHB | housing | 96.70 | -20% | 0.128 | -8% | -15% | +0.9% | True | 0.455 | 5 | +24% | -11% | 2.3 |
| INDA | india | 46.52 | -16% | 0.041 | -7% | -9% | -3.1% | False | 0.374 | 5 | +19% | -5% | 3.5 |

BJK (gaming) delisted — skipped by scan ("No data found, symbol may be delisted").

## B. Leaders — regime read

LEADERS (rs_spy_3m): ETHA +46% (crypto-spot), USO +39% (oil/gas), IBIT +29% (crypto-spot), ARKG +21% (biotech),
SKYY/WCLD +18–20% (software), XOP +18% / XLE +16% (oil/gas/energy). Money sits in crypto-spot, oil/gas, software
and energy. Dip themes cluster as the rate-shock mirror: utilities, housing, clean, solar, gold are the
rate-sensitive side of a Fed-hike regime (Sep 16 hike to 3.75–4.00%, 10y at ~5.2–5.35%, highest since 2007;
soft Aug PCE 3.0% and weak Sep payrolls 29K eased October-hike odds to ~38% by 10/1; oil elevated, WTI ~$93,
Brent ~$98–106 on the Iran/Strait-of-Hormuz standoff). Broadly the same regime as the 10/3 run: a rate-shock
rotation, not a broad selloff.

## C. Quick-pass memo — *UNVERIFIED, challenge it*

- rare-earth (REMX): **rotation** — sector-wide selloff on Trump-Xi Sept summit optimism eroding the scarcity
  premium (MP −15.8%/30d, REMX −17%); fundamentals constructive (MP Gd supply deal, GM magnet qual, Q4
  commercial magnet shipments). Thaw depth vs Nov-10 expiration still unresolved.
- solar (TAN): **break** — residential 25D eliminated, commercial 48E phased out in the tax bill; rates add
  pressure (Barron's 9/28: TAN −10%/month). Policy repeal, not rotation.
- china (KWEB/FXI): **unclear** — broad US-listed China ETF outflows (−$3–3.5B peak-to-trough since May per
  Global Markets Investor); Fifth Plenum 10/26–29 is symmetric timing, not direction.
- nuclear (URNM/NLR/URA): **rotation** — term uranium at record $96.50/lb (Aug) while miners −35%+; oilprice.com
  10/1: AI-power trade divorced from momentum (NLR −35% below high); utilities reluctant to contract at record
  prices; Oklo FERC queue rejection, Holtec IPO pull. Thesis intact, momentum unwind.
- silver (SLV): **rotation** — futures-led selling on the Sep rate hike; dovish Williams/Jefferson comments
  eased Oct-hike odds; China export tightening in January is a demand tailwind; industrial demand fell 3%
  (World Silver Survey 2026).
- defense-us (SHLD/XAR/ITA/PPA): **rotation** — valuation fatigue after the $1.5T budget proposal rally;
  spending intact (RTX $24.4B SM-6); equal-weight XAR cleanest.
- space (UFO/ARKX): **rotation** — SpaceX IPO pulled returns forward (UFO +50% YTD → −40% from high);
  high-capex physics + dilution risk now pricing (barchart via TipRanks). No dated event.
- utilities (XLU): **rotation** — pure rate selloff (−17.7% since Feb record $47.73); 10y 5.23% vs XLU 3.08%
  yield (Jefferies); options flow 10/2 suggests traders see the bond selloff nearing an end (10× XLU options
  volume, $1M bet sector stops falling, CNBC 10/2). Broad fund → core candidate.
- clean (PBW/ICLN): **break-ish** — subsidy cuts real headwind (48E phaseout) + rates; ICLN quality operators
  (Bloom Energy 9.4%, First Solar 7.0%) vs PBW small-cap junk. ICLN the cleaner basket.
- gold (GLD): **rotation** — September decline led by futures/speculative selling, not ETF redemptions
  (tradingnews 10/1: ETF allocators added into the Fed meeting and held); central-bank buying intact (~1,000t/yr,
  China 1,077t Jan–Aug); Morgan Stanley sees $4,000/oz floor. No dated trigger.
- grid/infra (IGF/PAVE): **rotation** — AI data-center buildout capex intact (IEA: grid investment must double
  to >$600B/yr by 2030; Gartner: AI infra +$401B 2026); PAVE stabilizing (+1.7% ret_10d, retaking). No dated catalyst;
  broad funds → core candidates.
- lithium (LIT): **unclear** — supply-driven (China lithium carbonate back to 1-month low on Australian
  supply); Albemarle Q3 11/4 confirmed; LIT basket flawed (Rio Tinto 22.5%, chemicals).
- argentina (ARGT): **unclear** — reform-durability bet on Milei; MELI 21.6% anchor; IMF review risk, peso
  band dynamics; Oct 2026 legislative elections looming. Macro binary, no dated trigger.
- housing (ITB/XHB): **rotation** — pure rate play; 30y ~7%, July new-home sales −10.5% MoM; structural 3–4M
  home shortage intact; DHI Q4 10/29 confirmed; XHB stabilizing. ITB hit 52w low 10/2.
- india (INDA): **rotation** — FII outflows ₹3.05 lakh crore Jan–Sep 2026 (NSDL), AI rotation to Taiwan/Korea,
  weak rupee (₹96/$); no dated trigger.

## D. Confirmed catalysts carried forward — already verified, do NOT rescore as "not found"

| theme | event | date | confirmed by |
|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 and 2026-10-01 |
| macro | FOMC decision (Oct 27-28 meeting, statement on second day) | **2026-10-28** | federalreserve.gov FOMC calendar; re-verified 2026-09-29 and 2026-10-01 |
| macro | FOMC decision (Dec 8-9 meeting, statement on second day) | **2026-12-09** | federalreserve.gov FOMC calendar; re-verified 2026-09-29 and 2026-10-01 |
| ai/robot | NVIDIA GTC 2027, San Jose | **2027-03-14** | nvidia.com GTC FAQ |
| solar | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | **2026-10-14** | Reuters/SRN 2026-09-11; re-verified 2026-09-29 and 2026-10-01 (pv-tech 9/15) |
| solar | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | **2026-11-02** | Sxcoal 2026-09-14; re-verified 2026-09-29 and 2026-10-01 (pv-tech 9/15) |
| housing | D.R. Horton Q4/FY26 results, before market open, 8:30 a.m. ET call | **2026-10-29** | D.R. Horton investor site PR 2026-09-10 (BusinessWire) |
| lithium | Albemarle Q3 2026 results, after NYSE close; call Nov 5, 8:00 a.m. EST | **2026-11-04** | Albemarle PR Newswire 2026-10-01 |

### Disputed — sources contradict; neither date confirmed

| theme | claim | readings | sources |
|---|---|---|---|
| rare-earth | China's suspension of Oct-2025 rare-earth export controls (MOFCOM Announcement No. 70) | (a) expires 2026-11-10 with automatic snapback — MOFCOM No. 70 text (2025-11-07, pre-summit); (b) extended with truce to 2027-01-10 — Bessent post-9/24-summit (stockmoguls 9/22 flags the Nov-10 deadline as the real forcing function, leverage intact either way). No MOFCOM text on either side | (a) MOFCOM No. 70 text; (b) Bessent via post-summit outlets; 9/22 stockmoguls: "China's one-year suspension ... due to expire on November 10, 2026, giving Beijing significant leverage" |
