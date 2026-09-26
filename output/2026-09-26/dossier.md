# Dossier — 2026-09-26 (scan asof 2026-09-25 close)

Prices below are the **2026-09-25 close**; the panel runs 2026-09-26. **25 candidates, 15 themes** (same count as 9/25).
New candidates vs output/2026-09-25/: **ARGT** (argentina, re-entry), **GLD** (gold, re-entry), **SHLD** (defense-us theme now 4-deep).
Exited: **GRID, PICK** (both had been thin-barred), **XLY** (discretionary), **XME** (base-metals). SHLD is Global X Defense Tech
($8.6B AUM since 2023 launch, +49% 1y — the "track two" defense-tech layer per stockmoguls).

## (A) Candidates — full CSV rows

Column legend: `theme` = panel theme; `price` = close; `dd_52w` = drawdown vs 52-week high; `dd_pctile` = current drawdown percentile vs own history (lower = deeper); `dd_z` = drawdown z-score vs own history; `vs_sma200` = vs 200-day SMA; `rs_spy_3m/6m/12m` = relative strength vs SPY over 3/6/12 months; `ret_10d` = 10-day return; `stabilizing` = bounce flag; `dip_score` = dip DEPTH (never the memo's rank); `tp_pct`/`sl_pct` = target/stop %; `rr` = reward/risk; `size_1pct` = 1%-risk position fraction.

| ticker | theme | price | dd_52w | dd_pctile | dd_z | vs_sma200 | rs_spy_3m | rs_spy_6m | rs_spy_12m | ret_10d | stabilizing | dip_score | tp_pct | sl_pct | rr | size_1pct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TAN | solar | 44.06 | -0.404 | 0.0259 | -1.1138 | -0.1989 | -0.2857 | -0.404 | -0.163 | -0.0655 | False | 0.0445 | 0.6779 | -0.1571 | 4.3159 | 0.0637 |
| REMX | rare-earth | 66.66 | -0.3914 | 0.0531 | -0.9711 | -0.2255 | -0.2904 | -0.4138 | -0.1369 | -0.0553 | False | 0.0568 | 0.6431 | -0.1745 | 3.6849 | 0.0573 |
| KWEB | china | 24.58 | -0.3927 | 0.015 | -1.5917 | -0.1633 | -0.034 | -0.3302 | -0.5519 | -0.0008 | False | 0.0768 | 0.6466 | -0.1068 | 6.0527 | 0.0936 |
| URNM | nuclear | 49.13 | -0.415 | 0.045 | -0.8992 | -0.1889 | -0.1346 | -0.3724 | -0.3162 | -0.062 | False | 0.1141 | 0.7095 | -0.1999 | 3.55 | 0.05 |
| NLR | nuclear | 105.78 | -0.3565 | 0.0068 | -0.8585 | -0.1844 | -0.1512 | -0.3911 | -0.3808 | -0.0657 | False | 0.1329 | 0.5539 | -0.1798 | 3.0807 | 0.0556 |
| XLU | utilities | 39.51 | -0.1549 | 0.0027 | -1.0679 | -0.0988 | -0.1993 | -0.3182 | -0.2371 | -0.0611 | False | 0.1404 | 0.1833 | -0.0628 | 2.9184 | 0.1592 |
| UFO | space | 43.55 | -0.3569 | 0.0218 | -1.2949 | -0.0774 | -0.1167 | -0.2499 | 0.0535 | 0.0062 | **True** | 0.1536 | 0.555 | -0.1194 | 4.65 | 0.0838 |
| SHLD | defense-us | 61.46 | -0.2097 | 0.0259 | -0.9063 | -0.0956 | -0.0048 | -0.3406 | -0.2671 | -0.0047 | False | 0.159 | 0.2654 | -0.1002 | 2.6485 | 0.0998 |
| URA | nuclear | 40.91 | -0.3381 | 0.0245 | -0.7463 | -0.1511 | -0.1222 | -0.3258 | -0.2972 | -0.0602 | False | 0.1903 | 0.5109 | -0.1962 | 2.6041 | 0.051 |
| ICLN | clean | 17.23 | -0.2726 | 0.0082 | -0.948 | -0.0825 | -0.1771 | -0.2436 | -0.0294 | -0.0385 | False | 0.217 | 0.3747 | -0.1245 | 3.0097 | 0.0803 |
| XAR | defense-us | 239.46 | -0.1926 | 0.0054 | -0.7347 | -0.1044 | -0.1866 | -0.2694 | -0.1202 | -0.0259 | False | 0.2222 | 0.2385 | -0.1135 | 2.1015 | 0.0881 |
| PBW | clean | 30.02 | -0.3516 | 0.0981 | -0.8815 | -0.1261 | -0.2387 | -0.2312 | -0.1247 | -0.026 | False | 0.2229 | 0.5423 | -0.1727 | 3.1397 | 0.0579 |
| LIT | lithium | 69.02 | -0.2434 | 0.1567 | -0.9238 | -0.0737 | -0.1478 | -0.2166 | 0.0812 | -0.0346 | False | 0.2681 | 0.3218 | -0.1141 | 2.8198 | 0.0876 |
| IGF | grid/infra | 62.38 | -0.0881 | 0.0041 | -0.9881 | -0.0425 | -0.1355 | -0.2488 | -0.1222 | -0.0261 | False | 0.2749 | 0.0966 | -0.0386 | 2.5024 | 0.259 |
| IHI | health-other | 51.6 | -0.1957 | 0.0845 | -0.7846 | -0.0552 | -0.048 | -0.2484 | -0.3145 | 0.0157 | **True** | 0.3059 | 0.2434 | -0.108 | 2.2528 | 0.0926 |
| GLD | gold | 393.41 | -0.2067 | 0.0599 | -0.8639 | -0.0553 | -0.0078 | -0.2198 | -0.0335 | -0.0134 | False | 0.3189 | 0.2605 | -0.1036 | 2.5149 | 0.0965 |
| ITA | defense-us | 213.81 | -0.1547 | 0.0041 | -0.7346 | -0.0705 | -0.1567 | -0.2286 | -0.1269 | -0.0226 | False | 0.3246 | 0.183 | -0.0912 | 2.0068 | 0.1097 |
| INDA | india | 47.86 | -0.1344 | 0.1076 | -1.068 | -0.0431 | -0.095 | -0.175 | -0.2719 | -0.0146 | False | 0.3457 | 0.1552 | -0.0545 | 2.8493 | 0.1835 |
| PPA | defense-us | 159.32 | -0.1381 | 0.0095 | -0.6994 | -0.0666 | -0.1292 | -0.2472 | -0.1211 | -0.0124 | False | 0.3434 | 0.1602 | -0.0855 | 1.8738 | 0.117 |
| QCLN | clean | 49.31 | -0.2798 | 0.0599 | -0.7014 | -0.0574 | -0.2017 | -0.1273 | -0.0031 | -0.0036 | False | 0.4909 | 0.3886 | -0.1728 | 2.2492 | 0.0579 |
| PAVE | grid/infra | 53.47 | -0.1071 | 0.1063 | -0.6048 | -0.0131 | -0.1504 | -0.1337 | -0.0229 | -0.0113 | False | 0.6121 | 0.12 | -0.0767 | 1.5642 | 0.1304 |
| ITB | housing | 89.43 | -0.2031 | 0.2507 | -0.6985 | -0.0757 | -0.201 | -0.2017 | -0.3331 | 0.0072 | **True** | 0.3625 | 0.2548 | -0.1259 | 2.0243 | 0.0794 |
| XHB | housing | 98.32 | -0.1817 | 0.1689 | -0.7058 | -0.0691 | -0.2058 | -0.1921 | -0.2802 | 0.0042 | **True** | 0.3693 | 0.222 | -0.1115 | 1.9918 | 0.0897 |
| ARKX | space | 32.695 | -0.1337 | 0.1294 | -0.4948 | 0.0099 | -0.0368 | -0.1072 | 0.0001 | 0.0269 | **True** | 0.7392 | 0.1543 | -0.117 | 1.3191 | 0.0855 |
| ARGT | argentina | 88.6 | -0.1362 | 0.1185 | -0.6254 | -0.0413 | -0.0868 | -0.1897 | 0.0021 | -0.0713 | False | 0.4712 | 0.1577 | -0.0943 | 1.6719 | 0.106 |

**Thin flags (R/R < 1.3 → −1 wtd, never buy): ARKX 1.3191 only.** GRID, PICK, XLY, XME exited — the thin-barred names
are gone from the set, leaving ARKX as the sole thin fund. Only stabilizing flags: UFO, ARKX (space), IHI (health-other),
ITB, XHB (housing) — housing REGAINED both stabilizing flags after 10d turned positive.

## (B) Leaders — where the money is (rs_spy_3m)

crypto-spot ETHA +0.65 / IBIT +0.34, oil/gas USO +0.35 (Hormuz risk, Brent elevated ~$103–110), software WCLD +0.25 /
SKYY +0.21 / IGV +0.14, biotech ARKG +0.23 (+0.81 on 6m), cyber BUG +0.20. Gold miners GDX +0.15 / GDXJ +0.15 reappear
as leaders while GLD itself re-enters the dip set — miners leading the metal is unusual and worth the panel's attention.
Momentum still in crypto, software, cyber, biotech; rotation map unchanged: duration victims + China + housing on the
dip side.
Regime: Sep 16 FOMC +25bp to 3.75–4.00% (unanimous, first hike since 2023); 16 of 18 FOMC members expect ≥1 more rise
this year; Oct 27–28 second hike ~70% priced. 10y touched 5.135% 9/23, above 5.20% during the week (highest since
June 2007). Brent ~$103.67 (9/24), HinduBusinessLine notes a $109.97/barrel print; Hormuz closed. Trump-Xi summit held
9/24 in Washington — produced only a **two-month truce extension through Jan 10** (below Wall St hopes of 3–6 months;
freedombunker 9/24, businesstoday 9/25); China's suspension of expanded rare-earth export controls expires Nov 10, 2026.

## (C) Quick-pass memo — *unverified, challenge it*

One search per theme (9/26). Provisional buckets:

- solar (TAN) — **rotation**: borrowing-cost wrecking ball again — FSLR −8% to $177.45 on 9/24 (summamoney); Roth 9/25 calls the polysilicon-crackdown (20+ importer licenses revoked) a "very attractive entry point" tailwind for FSLR. Residential solar is financed, not bought — rate path decides demand. Thesis intact.
- rare-earth (REMX) — **rotation**: summit 9/24 produced only a short truce on minerals (2 months on trade; stockmoguls 9/25: "no extension gets signed" still not priced); China suspension expiry 11/10 the forcing function; licensing as leverage. Greer remarks reintroduced no-extension risk. Intact.
- china (KWEB) — **break**: sanctions-risk selloff (adalytica 9/20, US-China sentiment "Fear" at 30); −27.8% YTD, −40.9% 1y; HK fell 1% 9/25 on yields + summit digestion (businesstoday 9/25); two-month truce extension too short to re-rate. Policy overhang, not a sale.
- nuclear (URNM/NLR/URA) — **rotation**: uranium spot $89.70/lb on 9/18, +4.3% YTD, term ~$96.50 — commodity firm while equities −35%+ off peaks (discoveryalert 9/21); sellers are AI-data-center sentiment + Saudi discovery fears. NEW: House passed Ratepayer Protection Act (data centers pay for their power — bullish for SMRs), but Holtec cancelled its IPO ("perfect storm") — sentiment remains fragile. Cameco Q3 10/30.
- utilities (XLU) — **rotation**: −1.92% on 9/23 (worst sector) and −0.98% on 9/24 (aitrading67) as 10y broke 2007 highs; 3.06% yield, 0.08% expense, moderate-buy aggregate. Pure rate victim.
- clean (ICLN/PBW/QCLN) — **rotation**: rate victims; ICLN +1.53% 9/25 to $17.23 but still no stabilizing flag; ETFdb put ICLN on its 9/22 "sell on the pop" list (etfdb.com 9/23). PBW/QCLN small-cap clean. No dated catalyst.
- space (UFO/ARKX) — **rotation**: Flight 14 NET 9/28, first orbital attempt, deploy 26 Starlink V3 satellites, pending FAA (teslanorth 9/23). Sell-the-news risk post-launch. UFO stabilizing (10d +0.6%); ARKX thin 1.3191, barred.
- defense-us (SHLD/XAR/ITA/PPA) — **rotation**: SHLD new — Global X Defense Tech, $8.6B AUM since 2023, +49% 1y, the "track two" drones/counter-drone/AI-targeting layer (stockmoguls); budgets signed ($1T+ 2026, $1.5T 2027 proposal) but war-premium leg deflating; Bernstein caution on buying the selloff (9/23). No dated catalyst; no stabilizing flags.
- lithium (LIT) — **break**: oversupply resurgent — GFEX LC2609 at 141,320 CNY/t (9/9) vs MMLC 145,750 yuan/t; CATL's Jianxiawo mine back on care and maintenance (loses license); SMM stockpile revision +175kt; Australian restarts; China EV sales −15% H1 2026 (Reuters via minelistings). Benchmark flipped 2027 to deficit (Seeking Alpha 9/22) — dissent exists.
- housing (ITB/XHB) — **break**, but BOTH regained stabilizing flags: 30y mortgage at 7.12% (MBA, week ending 9/19; refi apps lowest since Feb 2025); KB Home cut margin guidance 9/23 (Q3 revenue −20%, orders −12%); Lennar cut delivery target; NAHB 32. Demand destruction by rates — the bounce needs the 10y to turn, which it hasn't.
- grid/infra (IGF/PAVE) — **rotation**: GRID exited (recovered); PAVE now the deeper dip but IGF is theme leader. AI datacenter capex story intact (Gartner: +49% AI-server spending 2026; NEE building 9.5GW gas for data centers). No dated catalyst.
- health-other (IHI) — **unclear**: REGAINED stabilizing flag; but 35k puts bought 9/24 (+324% vs avg, zolmax 9/24); 10.3% short interest (marketbeat 8/31); concentrated (ABT 18.25%, ISRG 14.28%, MDT 12.12%), 30.8x PE — expensive defensives in a rate shock. Bounce vs put panic — judge it.
- india (INDA) — **unclear**: FPI outflows ₹23,676 cr Sept (to 9/19); 2026 YTD outflow ₹2.45 lakh cr vs ₹1.66 lakh cr all of 2025 (multibagg); rupee at record low (~95.9–96/USD); drivers are dollar/crude/US yields, not India-specific — rupee breach of 96. Flows, not thesis; tariff digestion unresolved.
- gold (GLD) — **rotation** (re-entry): −20.7% from 52w high after the 2nd-biggest gold-ETF inflow month ever (Aug $18B, WGC); then 5 weeks of falling on 10y >5.20% (bullionvault 9/25; GLD small weekly outflow); gold fix ~$4,268 (5th straight weekly decline). Thesis (diversification, inflation hedge) intact; rate headwind is the seller.
- argentina (ARGT) — **unclear** (re-entry): macro thesis intact (falling inflation, reforms, US support deal) but 2027 election is a toss-up — Milei approval ~34%, 60% of Argentines want change (economicaffairs, ~9/8); Seeking Alpha downgraded ARGT to Hold (~9/2); Milei "very calm" on re-election in NY 9/24 (Bloomberg). Political risk, not economics.

The gate (cause ≥ 7 AND (stabilizing OR catalyst ≥ 7) AND not thin AND theme_rank == 1) needs catalyst≥7 on
stabilizing themes — IHI and housing have the flags but need a catalyst, which the searches did not produce.
Space (UFO) has the flag plus a dated catalyst (Flight 14, 9/28) but faces sell-the-news; ARKX is barred by thin.
