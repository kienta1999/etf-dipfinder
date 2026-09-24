# Dossier — 2026-09-23 (scan asof 2026-09-22 close)

Prices below are the **2026-09-22 close**; the panel ran 2026-09-23. Yesterday's (2026-09-22 run) buys were NLR, UFO, ICLN; avoid was ITB, XHB (cause veto). All 24 candidates present again; no new themes entered the candidate set.

## (A) Candidates — full CSV rows

Column legend: `theme` = panel theme; `price` = close; `dd_52w` = drawdown vs 52-week high; `dd_pctile` = current drawdown percentile vs own history (lower = deeper); `dd_z` = drawdown z-score vs own history; `vs_sma200` = vs 200-day SMA; `rs_spy_3m/6m/12m` = relative strength vs SPY over 3/6/12 months; `ret_10d` = 10-day return; `stabilizing` = bounce flag; `dip_score` = dip DEPTH (never the memo's rank); `tp_pct`/`sl_pct` = target/stop %; `rr` = reward/risk; `size_1pct` = 1%-risk position fraction.

```
  ticker   theme    price dd_52w dd_pctile   dd_z vs_sma200 rs_spy_3m rs_spy_6m rs_spy_12m ret_10d stabilizing dip_score tp_pct  sl_pct   rr     size_1pct
  TAN      solar    46.71 -0.368 0.0547    -1.019 -0.1516  -0.2773   -0.3517   -0.0927    -0.0277 False       0.0491  0.5827 -0.1564 3.7249 0.0639
  KWEB     china    25.18 -0.378 0.0246    -1.504 -0.1489  -0.0365   -0.3067   -0.5472    -0.0334 False       0.0637  0.6074 -0.1088 5.5818 0.0919
  REMX     rare-earth 70.27 -0.358 0.0930 -0.888 -0.1841  -0.3194   -0.3103   -0.0162    -0.0712 False       0.0770  0.5587 -0.1747 3.1978 0.0572
  URNM     nuclear  52.00 -0.381 0.0930   -0.848 -0.1433  -0.1161   -0.3041   -0.2278    -0.0888 False       0.1265  0.6152 -0.1945 3.1622 0.0514
  NLR      nuclear 110.73 -0.326 0.0246   -0.798 -0.1494  -0.1526   -0.3324   -0.3131    -0.0769 False       0.1327  0.4844 -0.1770 2.7369 0.0565
  SLV      silver   59.63 -0.435 0.0739   -1.167 -0.0943  -0.0295   -0.2294    0.3858    -0.0032 False       0.1486  0.7709 -0.1615 4.7733 0.0619
  XLU      utilities 40.66 -0.130 0.0014  -0.901 -0.0736  -0.1258   -0.2690   -0.1863    -0.0492 False       0.1764  0.1499 -0.0627 2.3913 0.1595
  URA      nuclear  42.98 -0.305 0.0506   -0.689 -0.1096  -0.1233   -0.2732   -0.1989    -0.0669 False       0.2101  0.4381 -0.1914 2.2896 0.0523
  UFO      space    44.17 -0.348 0.0369   -1.106 -0.0608  -0.1339   -0.2237    0.1029     0.0108 True        0.2123  0.5332 -0.1362 3.9152 0.0734
  PBW      clean    30.96 -0.331 0.1573   -0.812 -0.0992  -0.2838   -0.1795   -0.0506    -0.0173 False       0.2676  0.4955 -0.1766 2.8055 0.0566
  XAR      defense-us 243.55 -0.179 0.0123 -0.664 -0.0885 -0.1647   -0.2568   -0.1074    -0.0365 False       0.2735  0.2177 -0.1166 1.8674 0.0858
  GLD      gold     398.38 -0.197 0.0684  -0.824 -0.0430  -0.0058   -0.2350    0.0032    -0.0206 False       0.2822  0.2448 -0.1034 2.3685 0.0968
  ITB      housing  88.20 -0.214 0.1997   -0.762 -0.0907  -0.1279   -0.1894   -0.3761    -0.0529 False       0.2884  0.2723 -0.1216 2.2402 0.0823
  ICLN     clean    17.80 -0.249 0.0588   -0.828 -0.0514  -0.2188   -0.2104    0.0121     0.0017 True        0.2895  0.3307 -0.1300 2.5432 0.0769
  XHB      housing  96.96 -0.193 0.1313   -0.775 -0.0834  -0.1482   -0.1813   -0.3263    -0.0557 False       0.3027  0.2391 -0.1078 2.2175 0.0927
  ITA      defense-us 216.14 -0.145 0.0123 -0.681 -0.0595 -0.1229   -0.2257   -0.1163    -0.0409 False       0.3234  0.1702 -0.0925 1.8396 0.1081
  PPA      defense-us 161.17 -0.128 0.0164 -0.630 -0.0548 -0.1054   -0.2423   -0.1113    -0.0213 False       0.3301  0.1469 -0.0880 1.6681 0.1136
  INDA     india    48.50 -0.123 0.1614   -0.987 -0.0325  -0.0701   -0.1577   -0.2814    -0.0283 False       0.3539  0.1400 -0.0539 2.5990 0.1856
  IGF      grid/infra 63.33 -0.074 0.0096 -0.823 -0.0272 -0.0876   -0.2152   -0.1038    -0.0269 False       0.3670  0.0802 -0.0390 2.0531 0.2561
  LIT      lithium  70.83 -0.224 0.2189   -0.823 -0.0476  -0.1802   -0.1366    0.1743    -0.0452 False       0.3955  0.2880 -0.1176 2.4484 0.0850
  QCLN     clean    48.91 -0.286 0.0479   -0.675 -0.0639  -0.2922   -0.1301    0.0035    -0.0105 False       0.4368  0.3999 -0.1831 2.1836 0.0546
  VNM      vietnam  17.41 -0.121 0.2476   -0.519 -0.0435  -0.1082   -0.1390   -0.2037    -0.0413 False       0.4996  0.1373 -0.1008 1.3618 0.0992
  PAVE     grid/infra 53.08 -0.114 0.0944 -0.620 -0.0184  -0.1441   -0.1139   -0.0439    -0.0377 False       0.5923  0.1282 -0.0794 1.6156 0.1260
  ARKX     space    32.90 -0.128 0.1450   -0.447  0.0190  -0.0555   -0.1075    0.0186     0.0211 True        0.7256  0.1471 -0.1243 1.1836 0.0805
```

## (B) Leaders — where the money is (rs_spy_3m)

crypto-spot (ETHA/IBIT) +0.55/+0.30, software (WCLD) +0.38, biotech (ARKG) +0.38, cyber (BUG/HACK) +0.34/+0.26, oil/gas (USO) +0.27. Same rotation map as yesterday: momentum sits in crypto spot, software, biotech, cyber; dip themes are the mirror — rate-duration victims and post-hike rotation fodder. Sept 16 FOMC: +25bp to 3.75–4.00%, unanimous 12-0, first hike since July 2023; SEP median 4.1% end-2026; Oct 27–28 and Dec 8–9 meetings hike-priced. 10y touched 5.041% Sep 15 (highest since July 2007). Brent pulled back toward ~$97 after the Sept 10–11 Saudi pipeline shock (per whalesbook 9/7–9/11 coverage; yesterday's memo had $108.75 on 9/15 — verify regime premise in verifier phase).

## (C) Quick-pass memo — *unverified, challenge it*

One search per theme (9/23). Provisional buckets:

- solar (TAN) — **rotation**: Fed +25bp 9/16, first hike in 3 yrs; ENPH −5% on 9/19 as selling resumed; TAN crossed below 200d MA (ABMN 9/19, $45.66 vs $55.92). Rates-driven, thesis intact.
- china (KWEB) — **break**: sanctions-risk selloff 9/20 (adalytica, US-China sentiment "Fear" at 30); Alibaba's $10.2B Aug-24 placement still weighing; persistent outflows ($3.46B 6-month). Policy overhang, not a sale.
- rare-earth (REMX) — **rotation**: MP Materials −30 days ~−20%, RSI 24.6 oversold; China's escalating export controls vs Western processing buildout; dated triggers (China export-control snapback 11/10, DFARS magnet ban 1/1/27 per yesterday's panel).
- nuclear (URNM/NLR/URA) — **rotation**: uranium spot $89.70/lb on 9/18, +4.3% YTD, term ~$96.50 — commodity firm while equities −35%+ off peaks (discoveryalert 9/21); seller is AI-data-center sentiment + Saudi discovery fears. Cameco Q3 10/30.
- silver (SLV) — **rotation**: Fed-day reversal 9/16, 10y ~5% crushing non-yielding assets; SLV −44% off high is rate damage.
- utilities (XLU) — **rotation**: worst S&P sector last week −3.04% (smtraderca 9/20); rising yields dim dividend appeal (SA 9/6). Pure rate victim.
- space (UFO/ARKX) — **rotation**: SpaceX post-IPO fade (28% below $200 listing high) dragging the theme; Starship Flight 14 NET 9/28 (spaceq.ca) — a dated test-flight trigger, with sell-the-news risk.
- clean (PBW/ICLN/QCLN) — **rotation**: rate victims like solar; ICLN stabilizing (10d +0.17%), UFO/ARKX/ICLN the only three stabilizing candidates.
- defense-us (XAR/ITA/PPA) — **rotation**: peace-selloff + profit-taking (fool.com.au 8/8: Betashares ARMR −20% since Jan); backlogs intact; war-premium repricing.
- gold (GLD) — **rotation**: 9/16 Fed-day −2–3% wobble on hike bets, but gold rebounded to ~$4,286 (xe.today 9/17); GLD even resumed net purchases (+4.6t over 9/15–16). Geopolitical bid survives the hike.
- housing (ITB/XHB) — **break**: Lennar Q3 profit halved 9/16 (Reuters); NAHB sentiment 32 — 1-year low; 30y mortgage ~6.76–7%; 38% of builders cut prices in Sept. Demand destruction, not rotation.
- india (INDA) — **unclear**: record FPI outflows (~$17.6B YTD per NSDL), Trump tariffs on >half of India's $87B exports + H-1B fee hikes; Nifty up only 2–4% YTD vs 20%+ Asia. Tariff digestion, fragile flows.
- grid/infra (IGF/PAVE) — **rotation**: GRID −7.7% 3m after a +27% 12m run (tradingnews 9/2) — a theme that ran hard then stalled; AI datacenter capex story intact; yesterday's panel noted no dated catalyst.
- lithium (LIT) — **break**: CATL's Jianxiawo mine cleared its safety permit (adds ~3% global supply) after lithium carbonate fell ~30% from May highs; GFEX at 5-month lows (oilprice). Oversupply is the thesis.
- vietnam (VNM) — **rotation**: FTSE upgrade to Secondary Emerging effective 9/21/26 with 10% first-tranche weight; ~$171M est. passive inflows (ACBS 4/8); flows, not thesis damage.

New vs yesterday's scan: same 24 candidates, same candidate set; no theme entered or exited. Only stabilizing candidates: UFO, ICLN, ARKX. Thinnest R/R: ARKX 1.18 (< 1.3 → −1 wtd, never buy). VNM at 1.36 clears the 1.3 thin line — no thin penalty.
