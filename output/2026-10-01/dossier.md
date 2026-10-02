# Dossier — 2026-10-01 (rerun under why-logging skill update)

Scan as-of close 2026-10-01 (scan.csv `asof_date` = 2026-10-01). Universe 119 funds: 24 candidates in the top 15 themes by `dip_score`; 95 funds not in candidates are logged with gate + reason in `data/drops.csv` (next to `data/scan.csv`).

## A) Candidates — full scan.csv rows

| ETF | theme | price | dd_52w | dd_pctile | dd_z | vs_sma200 | rs_spy_3m | rs_spy_6m | rs_spy_12m | ret_10d | vol_60d | dollar_vol | tp_pct | sl_pct | rr | stabilizing | dip_score | price_score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REMX | rare-earth | 62.9500 | -0.4253 | 0.0054 | -1.0737 | -0.2672 | -0.3024 | -0.4608 | -0.1853 | -0.0890 | 0.3961 | 39261681.7841 | 0.7400 | -0.1715 | 4.3143 | False | 0.0681 | 6 |
| TAN | solar | 43.0700 | -0.4174 | 0.0177 | -1.1889 | -0.2154 | -0.2636 | -0.4065 | -0.1720 | -0.0710 | 0.3511 | 33611596.7100 | 0.7165 | -0.1520 | 4.7129 | False | 0.0811 | 6 |
| KWEB | china | 24.3300 | -0.3989 | 0.0082 | -1.7237 | -0.1659 | -0.0548 | -0.3122 | -0.5448 | -0.0029 | 0.2314 | 356681587.1736 | 0.6636 | -0.1002 | 6.6220 | False | 0.0942 | 5 |
| URNM | nuclear | 47.2400 | -0.4376 | 0.0204 | -0.9720 | -0.2179 | -0.1342 | -0.4322 | -0.3510 | -0.0793 | 0.4501 | 26648032.0551 | 0.7779 | -0.1949 | 3.9912 | False | 0.1054 | 4 |
| NLR | nuclear | 102.7500 | -0.3749 | 0.0027 | -0.9289 | -0.2044 | -0.1343 | -0.4071 | -0.3829 | -0.0707 | 0.4036 | 39104985.1192 | 0.5997 | -0.1747 | 3.4318 | False | 0.1304 | 5 |
| URA | nuclear | 39.5900 | -0.3595 | 0.0136 | -0.8118 | -0.1766 | -0.1125 | -0.3682 | -0.2890 | -0.0724 | 0.4428 | 125401274.6789 | 0.5613 | -0.1917 | 2.9272 | False | 0.2049 | 6 |
| SLV | silver | 55.0200 | -0.4790 | 0.0422 | -1.2366 | -0.1655 | -0.0283 | -0.3644 | 0.1394 | -0.0670 | 0.3873 | 891005714.2748 | 0.9193 | -0.1677 | 5.4810 | False | 0.1126 | 7 |
| SHLD | defense-us | 60.1400 | -0.2267 | 0.0136 | -1.1020 | -0.1140 | -0.0881 | -0.3508 | -0.2971 | -0.0452 | 0.2057 | 103783679.8978 | 0.2932 | -0.0891 | 3.2912 | False | 0.1501 | 6 |
| XAR | defense-us | 231.6000 | -0.2191 | 0.0027 | -0.8689 | -0.1336 | -0.2225 | -0.2803 | -0.1718 | -0.0398 | 0.2521 | 75358400.6695 | 0.2805 | -0.1092 | 2.5695 | False | 0.2492 | 6 |
| ITA | defense-us | 208.0400 | -0.1775 | 0.0027 | -0.8824 | -0.0958 | -0.1891 | -0.2399 | -0.1625 | -0.0273 | 0.2011 | 178634589.6178 | 0.2158 | -0.0871 | 2.4775 | False | 0.3185 | 6 |
| PPA | defense-us | 155.5700 | -0.1584 | 0.0027 | -0.8375 | -0.0889 | -0.1666 | -0.2515 | -0.1544 | -0.0250 | 0.1891 | 46257052.8754 | 0.1881 | -0.0819 | 2.2979 | False | 0.3309 | 6 |
| UFO | space | 41.9500 | -0.3805 | 0.0014 | -1.4320 | -0.1129 | -0.2004 | -0.2638 | 0.0210 | -0.0391 | 0.2657 | 8234304.2985 | 0.6141 | -0.1150 | 5.3381 | False | 0.1570 | 8 |
| ARKX | space | 31.9700 | -0.1529 | 0.0831 | -0.5941 | -0.0143 | -0.0844 | -0.1030 | -0.0394 | -0.0102 | 0.2574 | 13288469.3241 | 0.1805 | -0.1114 | 1.6196 | False | 0.7379 | 5 |
| XLU | utilities | 39.6800 | -0.1513 | 0.0068 | -1.0996 | -0.0940 | -0.1548 | -0.2995 | -0.2233 | -0.0412 | 0.1376 | 1119931115.5013 | 0.1783 | -0.0596 | 2.9920 | False | 0.2003 | 6 |
| PBW | clean | 28.9900 | -0.3739 | 0.0368 | -0.9962 | -0.1548 | -0.2287 | -0.2402 | -0.1354 | -0.0490 | 0.3753 | 9362619.2134 | 0.5971 | -0.1625 | 3.6742 | False | 0.2376 | 6 |
| ICLN | clean | 16.8400 | -0.2890 | 0.0027 | -1.0598 | -0.1036 | -0.1722 | -0.2467 | -0.0599 | -0.0502 | 0.2727 | 119141537.3715 | 0.4066 | -0.1181 | 3.4426 | False | 0.2441 | 7 |
| LIT | lithium | 68.2200 | -0.2522 | 0.1090 | -1.0056 | -0.0855 | -0.1369 | -0.2515 | 0.0492 | -0.0378 | 0.2508 | 12460802.9499 | 0.3373 | -0.1086 | 3.1056 | False | 0.2754 | 5 |
| IGF | grid/infra | 61.3100 | -0.1038 | 0.0014 | -1.2662 | -0.0594 | -0.1115 | -0.2470 | -0.1254 | -0.0360 | 0.0819 | 59901525.2961 | 0.1158 | -0.0355 | 3.2626 | False | 0.2951 | 7 |
| PAVE | grid/infra | 53.0400 | -0.1143 | 0.0954 | -0.6725 | -0.0226 | -0.1003 | -0.1440 | -0.0361 | 0.0025 | 0.1700 | 86487100.4970 | 0.1291 | -0.0736 | 1.7535 | True | 0.6317 | 7 |
| GLD | gold | 382.7600 | -0.2282 | 0.0463 | -0.9167 | -0.0804 | -0.0161 | -0.2976 | -0.0824 | -0.0392 | 0.2489 | 3524989009.3980 | 0.2956 | -0.1078 | 2.7429 | False | 0.3000 | 6 |
| ARGT | argentina | 84.3400 | -0.1777 | 0.0518 | -0.8171 | -0.0866 | -0.1061 | -0.2638 | 0.0635 | -0.1012 | 0.2175 | 12946941.9168 | 0.2161 | -0.0942 | 2.2948 | False | 0.3308 | 6 |
| INDA | india | 46.3600 | -0.1615 | 0.0354 | -1.2980 | -0.0707 | -0.0929 | -0.1794 | -0.2687 | -0.0344 | 0.1244 | 239398058.1293 | 0.1926 | -0.0539 | 3.5750 | False | 0.3393 | 5 |
| ITB | housing | 87.3700 | -0.2214 | 0.1717 | -0.7949 | -0.0947 | -0.1721 | -0.2023 | -0.3334 | -0.0133 | 0.2786 | 202449897.3932 | 0.2844 | -0.1206 | 2.3577 | False | 0.3871 | 3 |
| XHB | housing | 96.7800 | -0.1945 | 0.1294 | -0.7796 | -0.0821 | -0.1637 | -0.1895 | -0.2754 | 0.0026 | 0.2495 | 189906472.2764 | 0.2414 | -0.1080 | 2.2351 | True | 0.4499 | 5 |

Column legend (`dedip_score` provenance — column is named `dip_score` in the file):
- theme / is_candidate / dedip_score: theme tag, gate flag, dip ranker — lower dedip_score = stronger dip (day −28% percentile × rs_pctile adjustment; dedip_score ≡ dip_score).
- price: last close (2026-10-01).
- dd_52w: drawdown from 52-week high. dd_pctile: percentile of today's drawdown among the fund's own 1y drawdowns (0 = deepest). dd_z: drawdown z-score vs own 1y history.
- vs_sma200 (and vs_sma50 in the CSV): relative distance below the MA. ret_10d: 10-day return. ret_5d in the CSV: 5-day return.
- rs_spy_3m / rs_spy_6m / rs_spy_12m: return minus SPY's over the window.
- vol_60d: 60-day annualized volatility. dollar_vol: price × 200d avg volume (liquidity).
- tp_pct / sl_pct: from the SCAN — take-profit % to the 200-day SMA (the recovery anchor) and stop-loss % (recent-swing low). Not the memo's computed levels.
- rr: tp_pct ÷ |sl_pct|. stabilizing: last close up ≥ +1.5% after a down close, or five rising closes.
- price_score: deterministic, from `consolidate.price_score()` — NOT to be re-derived.

## B) Leaders (money flowed to, not from — never in CANDIDATES)

Leaders are the top non-candidates by `rs_spy_3m` (fewest missing of the trim) — NOT dedip_score order:

| ETF | theme | rs_spy_3m | rs_spy_6m | rs_spy_12m | dd_52w | vs_sma200 | vol_60d | dollar_vol |
|---|---|---|---|---|---|---|---|---|
| ETHA | crypto-spot | +0.5560 | +0.4680 | theme_only | -24.89% | +29.46% | 0.4025 | 182653524 |
| PHO | water | +0.4392 | +0.3756 | +0.2625 | -8.57% | +7.07% | 0.1331 | 5462012 |
| USO | oil/gas | +0.4139 | +0.2266 | -0.0355 | -8.35% | +10.43% | 0.3861 | 525937151 |
| MOO | agriculture | +0.3570 | +0.1238 | -0.2652 | -17.09% | +9.83% | 0.1251 | 1186905395 |
| FCG | oil/gas | +0.3538 | +0.2756 | -0.0147 | -14.04% | +6.83% | 0.2064 | 11408533 |
| IBIT | crypto-spot | +0.3474 | +0.3045 | theme_only | -18.43% | +11.30% | 0.3446 | 4541810834 |
| XOP | oil/gas | +0.1677 | +0.1111 | -0.2008 | -7.09% | +0.94% | 0.2273 | 462041238 |
| XLE | oil/gas | +0.1568 | +0.1457 | -0.1955 | -3.82% | +1.14% | 0.2176 | 1241833529 |

Read: money went to crypto-spot, oil/gas equities and crude, biotech (ARKG +0.211), and software (SKYY/WCLD ≈ +0.21) — i.e., toward energy and risk-beta, away from rate-sensitive bond proxies and hard-asset premium trades. The dip complex is the mirror: (1) the yield complex (utilities, housing, grid/infra, clean/solar) sold as the 10y pushed to ~5.28–5.34% (19-year highs) with a September Fed hike behind and October hike odds swinging; (2) hard-asset scarcity premiums unwound after the Sep 23–25 US–China summit thaw (rare earths), record-run profit-taking (silver, gold −6–6.5% in September on the dollar at ~101.7–102); (3) uranium equities de-rated the AI-power momentum trade while the uranium term price printed record highs; (4) defense slid to a record 7-week losing streak on peace headlines; (5) EM (India, Argentina, China) bled FPI money to US yields.

## C) Quick-pass memo — *unverified — challenge it*

Provisional verdict per theme (copied to siblings unless a fund differs — each carries its news anchor):

- **rare-earth (REMX)** — **rotation**. The Sep 23–25 Trump–Xi summit thaw knocked the scarcity premium out: post-summit reporting put Beijing's rare-earth export controls on hold ~1 year (extension to 2027-01-10 per Bessent, vs the carried-forward Disputed row that says the No. 70 suspension expires 2026-11-10 with snapback — see §D); rare-earth stocks fell ~15% in a month (MP Materials −15.8%/30d) while end-demand (defense magnets, EVs) and US rare-earth earnings (MP Q2 revenue +89% y/y) stay intact (Zacks; Investing.com via tradingview).
- **solar (TAN)** — **break**. Policy impairment: last year's tax bill cut subsidies for new projects from July and permitting slowed; the 10y at ~5.2% crushes rate-sensitive renewables (TAN −10% in a month); Apr 2026 preliminary AD/CVD (India CVD 126.34% / AD 123.04%) sealed SE-Asia supply routes and raised module costs (Barron's; commerce.gov). Demand itself is not the failure — the subsidy/financing regime is.
- **china (KWEB)** — **unclear**. US–China sentiment in "Fear" territory, sanctions headline risk, KWEB −42.7% over 1y and ~$3B YTD outflows from US-listed China ETFs — but the same research notes KWEB's fundamentals (25+ years of listed Chinese internet names) look the strongest in years and it is arguably undervalued; the overhang is policy, which is the thesis's permanent condition (ainvest; ainvest/GlobeNewswire).
- **nuclear (URNM, NLR, URA)** — **rotation**. The uranium term price hit a record (18-year high in real terms; Sprott: equities off highs while term price at record) even as uranium stocks fell ~30–37% — a momentum unwind of the AI-power trade (Oklo, NuScale ~−50% YTD, "nuclear decoupled from AI stocks"), not a demand break; long-term contracting and AI data-center power deals keep building (TD via oilprice.com; Morgan Stanley via Zacks).
- **silver (SLV)** — **rotation**. Profit-taking/positioning unwind after a record run (spot printed $83.62 intraday earlier in the run; SLV ~−10% in five sessions) plus rising yields and exchange margin hikes; industrial (solar/EV) + monetary demand intact — a correction, not a regime change (Investing.com; FXEmpire; Proactive).
- **defense-us (SHLD, XAR, ITA, PPA)** — **rotation**. XAR: six-to-seven straight weekly losses, −21% from the Aug 14 record (bear market) on peace headlines, talks of budget cuts, and sector rotation; NATO commitments (2% of GDP, rising toward 5%) and a >$1T FY2026 defense bill with rising contractor backlogs say the demand regime is intact (24/7 Wall St.; Defense News; Motley Fool).
- **space (UFO, ARKX)** — **unclear**. The SpaceX-IPO trade is unwinding and valuation discipline is back (UFO ~−38% from its $68 high after a fund-closure scare; Blue Origin's New Glenn test explosion didn't help); launch cadence and defense-space demand are real, but pricing had pulled decades of growth forward (GlobeNewswire; Motley Fool; Investing.com).
- **utilities (XLU)** — **rotation**. Pure bond-proxy math: XLU yield ~3.08% vs the 10y at 5.23–5.30%; XLU −17.7% from its Feb 27 record, at a 17-month low, while Jefferies sees data-center-driven earnings acceleration for the sector — the earnings story did not break, the discount rate did (CNBC; Bloomberg via Advisor Perspectives; Jefferies via Yahoo Finance).
- **clean (PBW, ICLN)** — **unclear**. Same rates + subsidy-cut headwinds as solar (ICLN ~−25% in 3 months) but the funds are global (First Solar, Bloom Energy mix) and global clean demand growth continues; US policy impairment vs global demand — mixed (Barron's; Fool; ETF Trends).
- **lithium (LIT)** — **rotation**. Cycle trough: LIT −10.7%/1m, Lithium Americas −41% YTD on the supply-overhang hangover, but short interest is falling and the supply-demand rebalancing (EV/battery demand growth vs mothballed supply) is the classic rotation setup (Zacks; Fool).
- **grid/infra (IGF, PAVE)** — **rotation**. Rate-sensitive de-rating plus AI-capex multiple cooling (PAVE's Vertiv at 119× forward P/E); the physical grid story (transformers, data-center buildout, reshoring) is intact and IGF is oversold, testing $60.91 support; PAVE is one of only two `stabilizing = True` candidates (247wallst; Zacks; Trefis).
- **gold (GLD)** — **rotation**. Correction inside a structural bull: spot ~$4,156–4,186/oz, −6% to −6.5% in September as the 10y pushed >5.2% (touched 5.34%) and the dollar firmed to ~101.66–102 after a September Fed hike; central-bank buying is at a record pace (288.9t in Q2, China 21 straight months) and ETF demand resilient — the monetary bid did not break (Reuters via Kitco; gold.org; FXStreet; Trading Economics).
- **argentina (ARGT)** — **unclear**. Reform thesis intact (inflation down, country risk improving, one downgrade was only Buy→Hold) but rising political uncertainty ahead of the 2027 election is de-rating the trade (−10.8%/1m); single-name concentration adds fund-specific risk (MercadoLibre 21.4% of ARGT) (AInvest; iShares).
- **india (INDA)** — **rotation**. FPI outflows chasing US yields, rupee at ~₹96/USD (Sep 29–Oct 1), oil-import cost pressure; INDA −14.2% YTD vs strong domestic earnings/demand — an external-flows dip, not a domestic break (Angel One; Reuters; NDTV Profit).
- **housing (ITB, XHB)** — **unclear**. Structural 3–4M-home shortage vs affordability crushed by ~7% 30y mortgages: new-home sales fell 10.5% MoM in July to 607k SAAR and builders are spending heavily on rate buydowns (NAHB/Census via housingwire); XHB is the panel's other `stabilizing = True` fund (NAHB; FRED; schwab.wallst).

## D) Carry-forward confirmed catalysts (from `scripts/carry_forward.py`)

CONFIRMED CATALYSTS CARRIED FORWARD (inherited — do NOT rescore as 'not found'; these carry their original sources):
- 2026-10-09 — Cameco Q3 2026 Results & Management Discussion and Analysis (nuclear) [source: https://www.cameco.com/invest/news/cameco-q3-2026-results-and-management-discussion-and-analysis]
- 2026-10-14 — USITC Final Phase Injury Vote (Solar IV AD/CVD order follows; see 2026-11-02) (solar) [source: https://www.usitc.gov/press_room/news_release/2026/er0827_68185.html]
- 2026-10-28 — FOMC Meeting Decision (nuclear, solar, clean, lithium, housing, utilities, argentina, grid/infra, rare-earth, india, china) [source: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm]
- 2026-10-29 — D.R. Horton Earnings (housing) [source: https://investor.drhhorton.com/news-and-events/news/press-release-details/2026/D-R-Horton-Inc-Annou ]]
- 2026-10-30 — Cameco Q3 2026 Earnings Release (nuclear) [source: https://www.cameco.com/invest/news/cameco-q3-2026-results-and-management-discussion-and-analysis]
- 2026-11-02 — Commerce Final AD/CVD Determinations (Solar IV — order issuance) (solar) [source: https://www.commerce.gov/news/press-releases/2026/04/commerce-initiates-new-antidumping-and-countervailing-duty]
- 2026-12-09 — FOMC Meeting Decision (nuclear, solar, clean, lithium, housing, utilities, china) [source: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm]
- 2027-03-14 — NVIDIA GTC 2027 (semiconductor) [source: https://www.nvidia.com/en-us/events/gtc/]
Note: the Cameco Q3 results appear twice above because catalysts.md lists the same event under two labels/dates (2026-10-09 MD&A and 2026-10-30 earnings release) — both inherited as written.

DISPUTED (sources conflict — a catalyst ≥ 7 resting on one of these needs a primary source this run):
- rare earth export controls expire (solar) — (a) Expires 2026-11-10 with snapback (MOFCOM text) vs (b) Extended to 2027-01-10 (Bessent post-summit statement)
