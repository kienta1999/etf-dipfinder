# Dossier — 2026-10-03 (panel; as of Friday 2026-10-02 close)

## A. Candidates (25 dips in top 15 themes; scan.py 2026-10-03)

Legend: dd_52w = drawdown from 52w high; dd_pctile = how deep vs own 3y history (<0.10 = real event);
dd_z = drawdown / vol (vol-normalised depth); vs_sma200 = price vs 200-day SMA; rs_spy_3m/6m = relative to SPY;
ret_10d = 10-day return; stabilizing = ret_10d > 0; dip_score = depth rank (0 = deepest, NOT quality);
price_score = computed by consolidate.price_score() (depth + trend + 2 if stabilizing); rr = reward/risk.

| ETF | theme | dd_52w | dd_pctile | dd_z | vs_sma200 | rs_spy_3m | rs_spy_6m | ret_10d | stabilizing | dip_score | price_score | rr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REMX | rare-earth | -0.423 | 0.007 | -1.07 | -0.264 | -0.286 | -0.469 | -0.085 | False | 0.076 | 6 | 4.27 |
| TAN | solar | -0.404 | 0.031 | -1.14 | -0.197 | -0.261 | -0.376 | -0.035 | False | 0.089 | 5 | 4.44 |
| KWEB | china | -0.411 | 0.003 | -1.75 | -0.181 | -0.095 | -0.330 | -0.039 | False | 0.089 | 5 | 6.87 |
| FXI | china | -0.190 | 0.029 | -1.12 | -0.080 | -0.005 | -0.239 | -0.033 | False | 0.285 | 5 | 3.19 |
| URNM | nuclear | -0.435 | 0.022 | -0.97 | -0.215 | -0.142 | -0.432 | -0.058 | False | 0.101 | 5 | 3.97 |
| NLR | nuclear | -0.375 | 0.003 | -0.93 | -0.204 | -0.145 | -0.411 | -0.046 | False | 0.139 | 5 | 3.45 |
| URA | nuclear | -0.356 | 0.016 | -0.81 | -0.172 | -0.120 | -0.366 | -0.045 | False | 0.227 | 6 | 2.89 |
| SLV | silver | -0.482 | 0.040 | -1.25 | -0.170 | -0.051 | -0.347 | -0.087 | False | 0.114 | 7 | 5.58 |
| SHLD | defense-us | -0.226 | 0.016 | -1.12 | -0.113 | -0.098 | -0.363 | -0.039 | False | 0.152 | 6 | 3.33 |
| XAR | defense-us | -0.214 | 0.004 | -0.85 | -0.128 | -0.222 | -0.281 | -0.028 | False | 0.265 | 6 | 2.49 |
| ITA | defense-us | -0.179 | 0.003 | -0.89 | -0.097 | -0.197 | -0.241 | -0.028 | False | 0.303 | 6 | 2.49 |
| PPA | defense-us | -0.158 | 0.004 | -0.83 | -0.088 | -0.171 | -0.259 | -0.023 | False | 0.323 | 6 | 2.29 |
| UFO | space | -0.363 | 0.019 | -1.33 | -0.089 | -0.170 | -0.301 | -0.002 | False | 0.165 | 8 | 4.83 |
| ARKX | space | -0.134 | 0.135 | -0.51 | 0.007 | -0.068 | -0.102 | 0.017 | True | 0.792 | 6 | 1.37 |
| XLU | utilities | -0.148 | 0.011 | -1.07 | -0.090 | -0.141 | -0.308 | -0.024 | False | 0.197 | 6 | 2.91 |
| PBW | clean | -0.362 | 0.070 | -0.96 | -0.139 | -0.233 | -0.236 | -0.028 | False | 0.253 | 4 | 3.49 |
| ICLN | clean | -0.274 | 0.012 | -1.00 | -0.085 | -0.173 | -0.225 | -0.021 | False | 0.310 | 7 | 3.18 |
| GLD | gold | -0.233 | 0.044 | -0.94 | -0.087 | -0.032 | -0.294 | -0.052 | False | 0.266 | 6 | 2.83 |
| IGF | grid/infra | -0.097 | 0.004 | -1.16 | -0.053 | -0.106 | -0.254 | -0.022 | False | 0.299 | 7 | 2.97 |
| PAVE | grid/infra | -0.100 | 0.124 | -0.58 | -0.008 | -0.095 | -0.127 | 0.017 | True | 0.709 | 6 | 1.49 |
| LIT | lithium | -0.241 | 0.154 | -0.95 | -0.072 | -0.117 | -0.241 | -0.017 | False | 0.343 | 5 | 2.90 |
| ARGT | argentina | -0.176 | 0.055 | -0.81 | -0.085 | -0.128 | -0.276 | -0.086 | False | 0.348 | 6 | 2.27 |
| ITB | housing | -0.228 | 0.154 | -0.82 | -0.102 | -0.165 | -0.210 | -0.009 | False | 0.366 | 2 | 2.45 |
| XHB | housing | -0.195 | 0.128 | -0.79 | -0.082 | -0.153 | -0.188 | 0.009 | True | 0.455 | 5 | 2.27 |
| INDA | india | -0.159 | 0.041 | -1.28 | -0.067 | -0.094 | -0.182 | -0.031 | False | 0.374 | 5 | 3.52 |

Themes ranked by depth: rare-earth, solar, china, nuclear, silver, defense-us, space, utilities,
clean, gold, grid/infra, lithium, argentina, housing, india. Sibling groups: KWEB/FXI; URNM/NLR/URA;
SHLD/XAR/ITA/PPA; UFO/ARKX; PBW/ICLN; IGF/PAVE; ITB/XHB.

## B. Leaders (rs_spy_3m) — regime

Crypto-spot (ETHA +0.457, IBIT +0.294), oil/gas (USO +0.385, XOP +0.179), biotech (ARKG +0.212),
software (SKYY +0.195, WCLD +0.182), energy (XLE +0.162). The money is in energy, crypto, and software.
Rate shock: Fed HIKE Sep 16 (+25bp to 3.75-4.00%), 10y Treasury ~5.2-5.3%, CME ~70% odds of another
October hike (Sep 28); soft Aug PCE (3.0% y/y, Sep 30) and weak Sep payrolls (29K, Oct 2) eased odds after.
Macro regime: hawkish Fed repricing, rising oil (WTI ~$96 on Iran/Strait of Hormuz rejection of reopening),
strong dollar. Rate-sensitive sectors (utilities, housing, solar, clean) are the mirror.

## C. Quick-pass memo (UNVERIFIED — challenge it; one search per theme, Oct 3)

- **rare-earth (REMX) — rotation.** Sept Trump-Xi meeting thaw removed the scarcity premium on Western
  producers; REMX -17% in a month while SPY flat (tickeron.com, 1d ago). MP's operating news constructive
  (Gd oxide deal, GM magnet qualification, Q4 commercial magnet shipments). Disputed: MOFCOM Nov-10
  export-control expiry vs truce extension to 2027-01-10.
- **solar (TAN) — break-leaning, rates headwind.** Fed Sep 16 hike + another-hike signal bends residential
  solar directly (most rooftop systems financed; SunPower installs down; barron's 10y at 5.2%, 5d ago).
  2025 tax bill cut subsidies; Trump admin slowed permitting. Carried forward: USITC final injury vote
  2026-10-14, Commerce final AD/CVD orders 2026-11-02.
- **china (KWEB, FXI) — unclear/sentiment.** -$3B YTD outflows from US-listed China ETFs, -$3.5B since May
  (Global Markets Investor, Sep 14); broad de-risking, not fund-specific. FXI (broad large-cap) vs KWEB
  (internet: Tencent/Alibaba/PDD).
- **nuclear (URNM, NLR, URA) — rotation.** Uranium term price at 18-year high while mining equities -30%+
  from highs (ainvest.com; oilprice.com Oct 1: NLR -17% YTD, ~39% off 52w high) — momentum/policy-trade
  unwind, not thesis. Westinghouse $80B US partnership (Oct 2025) and spring-2026 AI-power run pulled returns
  forward; SMR hype broke (Holtec IPO pulled, Oklo PJM queue loss, NuScale ATM dilution). Carried forward:
  Cameco Q3 before open 2026-10-30.
- **silver (SLV) — rotation.** Rate-driven: silver -$60 test, -8% in 30d, 6th straight supply deficit
  (ad-hoc-news.de, 2d ago); no-yield asset punished by 5.2% 10y and Oct-hike odds; soft Aug PCE eased.
- **defense-us (SHLD, XAR, ITA, PPA) — rotation.** Investor fatigue + high valuations (LMT ~27x, ~25% pricier
  than a year ago; barron's; UBS trading desk note Sep 18 via zerohedge): spending intact — RTX $24.4B
  Navy SM-6 contract Oct 1 (everhint.com). Sentiment, not operating conditions.
- **space (UFO, ARKX) — break-leaning.** SpaceX IPO happened (SPCX in portfolio); valuations pulled forward
  (BI: stretched; tipranks); Blue Origin New Glenn test explosion; UFO -40% from $68 high. ARKX still above
  its 200-day (stabilizing). Late-cycle valuation discipline vs thesis.
- **utilities (XLU) — rotation.** Pure rate play: 17.7% off Feb 27 record $47.73, XLU div 3.08% vs 10y 5.23%
  (marketwatch, 4d ago); AI data-center demand structural; SocGen says cheap after de-rating; options flow
  (74K calls vs 4.5K puts Oct 1) suggests a floor forming.
- **clean (PBW, ICLN) — break-leaning.** Rates + subsidy removal (2025 tax bill) + slowed permitting;
  PBW small/micro-cap heavy (~80% small/micro, junky); ICLN has quality operators (Bloom Energy, China
  Yangtze Power, First Solar).
- **gold (GLD) — rotation.** Spot $4,156, 7w low on 5.2% 10y + Oct-hike odds + oil spike (Reuters/UBS via
  stocktwits, Sep 28); selloff futures/spot-led, ETF holders held (tradingnews.com); record Q2 central bank
  buying (289t); weak Sep payrolls (29K, Oct 2) gave partial bounce.
- **grid/infra (IGF, PAVE) — rotation.** Multiple compression on AI-infra names priced to perfection
  (Vertiv etc.); thesis intact — GRID $284M inflows into a falling fund over 5 days (tradingnews.com);
  Amazon $8B Nvidia chip offload / Anthropic-Broadcom $42B lease financing (Oct 1) raises AI-capex questions
  but also confirms the buildout scale. PAVE stabilizing.
- **lithium (LIT) — break-leaning.** Lithium carbonate sank to 5-month low on mine restarts / 2027 glut
  fears (mining.com, Aug); demand actually running hot (China battery output +55% y/y May); Rio Tinto now
  22.5% of LIT (fund composition changed).
- **argentina (ARGT) — unclear.** No current catalyst found; Milei reform story, MELI 21.6% of fund;
  fragile externals (soy, reserves), IMF $20B support.
- **housing (ITB, XHB) — rates headwind.** 30y mortgage ~7%, July new-home sales -10.5% MoM (lowest since
  Nov 2022 ex-Jan); builders leaning on buydowns; structural shortage 3-4M homes. Carried forward: D.R.
  Horton Q4/FY26 before open 2026-10-29. XHB stabilizing.
- **india (INDA) — unclear.** Persistent outflows (recurring ~$200M weekly patterns on nasdaq.com flow
  watches, though dated); $46.52, strong downtrend, no current trigger found.

The cluster is one macro event: the Fed's hawkish repricing (Sep 16 hike + Oct-hike odds) punishing
rate-sensitive and speculative themes. Lone idiosyncratic dips: space (IPO dynamics), lithium (supply
restarts), rare-earth (trade-diplomacy).

## D. Confirmed catalysts carried forward

| theme | event | date | confirmed by |
|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 and 2026-10-01 |
| macro | FOMC decision (Oct 27-28 meeting, statement on second day) | **2026-10-28** | federalreserve.gov FOMC calendar; re-verified 2026-09-29 and 2026-10-01 |
| macro | FOMC decision (Dec 8-9 meeting, statement on second day) | **2026-12-09** | federalreserve.gov FOMC calendar; re-verified 2026-09-29 and 2026-10-01 |
| solar | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | **2026-10-14** | Reuters/SRN 2026-09-11; re-verified 2026-09-29 and 2026-10-01 (pv-tech.org 9/15) |
| solar | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | **2026-11-02** | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 and 2026-10-01 (pv-tech.org 9/15) |
| housing | D.R. Horton Q4/FY26 results, before market open, 8:30 a.m. ET call | **2026-10-29** | D.R. Horton investor site press release, 2026-09-10 (BusinessWire) |

Disputed (neither date confirmed — score only what holds under both readings): rare-earth China's
suspension of Oct-2025 export controls (MOFCOM No. 70) — expires 2026-11-10 with snapback vs extended to
2027-01-10 with the truce (Bessent post-9/24-summit; no MOFCOM text on either side).
