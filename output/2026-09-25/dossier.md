# Dossier — 2026-09-25 (scan asof 2026-09-24 close)

Prices below are the **2026-09-24 close**; the panel runs 2026-09-25. **26 candidates, 15 themes** (up from 24/13).
New candidates vs output/2026-09-24/: **GRID** (grid/infra, theme now 3-deep), **IHI** (new theme health-other),
**XLY** (new theme discretionary), **XME+PICK** (new theme base-metals). Exited: **SLV** (silver), **GLD** (gold),
**VNM** (vietnam) — all three dropped out of the candidate set (theme-level criteria, not a per-fund recovery).

## (A) Candidates — full CSV rows

Column legend: `theme` = panel theme; `price` = close; `dd_52w` = drawdown vs 52-week high; `dd_pctile` = current drawdown percentile vs own history (lower = deeper); `dd_z` = drawdown z-score vs own history; `vs_sma200` = vs 200-day SMA; `rs_spy_3m/6m/12m` = relative strength vs SPY over 3/6/12 months; `ret_10d` = 10-day return; `stabilizing` = bounce flag; `dip_score` = dip DEPTH (never the memo's rank); `tp_pct`/`sl_pct` = target/stop %; `rr` = reward/risk; `size_1pct` = 1%-risk position fraction.

| ticker | theme | price | dd_52w | dd_pctile | dd_z | vs_sma200 | rs_spy_3m | rs_spy_6m | rs_spy_12m | ret_10d | stabilizing | dip_score | tp_pct | sl_pct | rr | size_1pct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TAN | solar | 43.47 | -0.4120 | 0.0177 | -1.11 | -0.2099 | -0.3015 | -0.3962 | -0.1725 | -0.0894 | False | 0.0381 | 0.7007 | -0.1602 | 4.3731 | 0.0624 |
| REMX | rare-earth | 66.93 | -0.3889 | 0.0573 | -0.96 | -0.2226 | -0.3107 | -0.3895 | -0.0597 | -0.1233 | False | 0.0633 | 0.6365 | -0.1750 | 3.6363 | 0.0571 |
| KWEB | china | 24.69 | -0.3900 | 0.0164 | -1.56 | -0.1625 | -0.0328 | -0.3074 | -0.5308 | -0.0036 | False | 0.0768 | 0.6393 | -0.1084 | 5.8970 | 0.0922 |
| URNM | nuclear | 49.13 | -0.4150 | 0.0437 | -0.91 | -0.1897 | -0.1439 | -0.3752 | -0.3162 | -0.1378 | False | 0.1078 | 0.7095 | -0.1976 | 3.5905 | 0.0506 |
| NLR | nuclear | 106.22 | -0.3538 | 0.0082 | -0.86 | -0.1824 | -0.1596 | -0.3780 | -0.3854 | -0.1361 | False | 0.1203 | 0.5474 | -0.1785 | 3.0673 | 0.0560 |
| XLU | utilities | 39.36 | -0.1581 | 0.0014 | -1.05 | -0.1026 | -0.1782 | -0.2955 | -0.2126 | -0.0766 | False | 0.1340 | 0.1879 | -0.0650 | 2.8902 | 0.1538 |
| ICLN | clean | 16.97 | -0.2836 | 0.0041 | -0.96 | -0.0959 | -0.2203 | -0.2512 | -0.0465 | -0.0577 | False | 0.1595 | 0.3958 | -0.1272 | 3.1104 | 0.0786 |
| PBW | clean | 29.93 | -0.3536 | 0.0955 | -0.88 | -0.1290 | -0.2495 | -0.2380 | -0.1172 | -0.0397 | False | 0.1782 | 0.5469 | -0.1739 | 3.1448 | 0.0575 |
| UFO | space | 43.42 | -0.3588 | 0.0191 | -1.27 | -0.0785 | -0.1135 | -0.2292 | 0.0563 | 0.0084 | **True** | 0.1792 | 0.5596 | -0.1226 | 4.5633 | 0.0815 |
| URA | nuclear | 40.86 | -0.3389 | 0.0218 | -0.76 | -0.1527 | -0.1352 | -0.3326 | -0.3135 | -0.1280 | False | 0.1774 | 0.5127 | -0.1936 | 2.6479 | 0.0516 |
| XAR | defense-us | 239.46 | -0.1926 | 0.0041 | -0.71 | -0.1041 | -0.1694 | -0.2647 | -0.1101 | -0.0288 | False | 0.2284 | 0.2385 | -0.1167 | 2.0439 | 0.0857 |
| LIT | lithium | 68.82 | -0.2456 | 0.1446 | -0.94 | -0.0755 | -0.1730 | -0.2034 | 0.1423 | -0.0671 | False | 0.2553 | 0.3256 | -0.1136 | 2.8672 | 0.0881 |
| ITB | housing | 88.31 | -0.2131 | 0.2060 | -0.76 | -0.0882 | -0.1869 | -0.2024 | -0.3236 | -0.0139 | False | 0.2801 | 0.2707 | -0.1215 | 2.2286 | 0.0823 |
| XHB | housing | 96.80 | -0.1943 | 0.1282 | -0.78 | -0.0841 | -0.1971 | -0.2019 | -0.2815 | -0.0190 | False | 0.2804 | 0.2412 | -0.1079 | 2.2352 | 0.0927 |
| IGF | grid/infra | 62.22 | -0.0904 | 0.0014 | -0.96 | -0.0445 | -0.1147 | -0.2295 | -0.1074 | -0.0394 | False | 0.2811 | 0.0994 | -0.0410 | 2.4280 | 0.2442 |
| IHI | health-other | 51.34 | -0.1998 | 0.0819 | -0.78 | -0.0618 | -0.0126 | -0.2286 | -0.3103 | -0.0012 | False | 0.2869 | 0.2497 | -0.1103 | 2.2641 | 0.0907 |
| ITA | defense-us | 212.76 | -0.1588 | 0.0014 | -0.74 | -0.0746 | -0.1470 | -0.2231 | -0.1188 | -0.0294 | False | 0.3119 | 0.1888 | -0.0923 | 2.0449 | 0.1083 |
| INDA | india | 47.56 | -0.1398 | 0.0887 | -1.11 | -0.0502 | -0.0906 | -0.1553 | -0.2739 | -0.0228 | False | 0.3136 | 0.1625 | -0.0547 | 2.9715 | 0.1828 |
| PPA | defense-us | 159.09 | -0.1393 | 0.0068 | -0.69 | -0.0675 | -0.1160 | -0.2343 | -0.1106 | -0.0107 | False | 0.3179 | 0.1619 | -0.0880 | 1.8390 | 0.1136 |
| QCLN | clean | 48.24 | -0.2955 | 0.0314 | -0.73 | -0.0772 | -0.2518 | -0.1690 | -0.0287 | -0.0225 | False | 0.3374 | 0.4194 | -0.1760 | 2.3828 | 0.0568 |
| XLY | discretionary | 110.32 | -0.1085 | 0.1091 | -0.56 | -0.0507 | -0.0881 | -0.1704 | -0.2367 | -0.0169 | False | 0.4387 | 0.1217 | -0.0843 | 1.4443 | 0.1186 |
| XME | base-metals | 107.96 | -0.1861 | 0.0955 | -0.51 | -0.0501 | -0.0413 | -0.1684 | 0.0281 | -0.0936 | False | 0.4895 | 0.2287 | -0.1571 | 1.4554 | 0.0636 |
| PAVE | grid/infra | 53.07 | -0.1138 | 0.0941 | -0.63 | -0.0194 | -0.1387 | -0.1375 | -0.0256 | -0.0207 | False | 0.5356 | 0.1284 | -0.0782 | 1.6422 | 0.1279 |
| GRID | grid/infra | 178.26 | -0.1024 | 0.0600 | -0.40 | 0.0174 | -0.0958 | -0.0954 | 0.0283 | -0.0084 | False | 0.7767 | 0.1141 | -0.1113 | **1.0259** | 0.0899 |
| ARKX | space | 32.77 | -0.1317 | 0.1351 | -0.48 | 0.0136 | -0.0306 | -0.0968 | 0.0079 | 0.0292 | **True** | 0.7135 | 0.1517 | -0.1199 | **1.2645** | 0.0834 |
| PICK | base-metals | 60.80 | -0.1105 | 0.3397 | -0.40 | 0.0236 | -0.0060 | -0.0464 | 0.2859 | -0.0839 | False | 0.7962 | 0.1243 | -0.1190 | **1.0444** | 0.0840 |

**Thin flags (R/R < 1.3 → −1 wtd, never buy): GRID 1.026, PICK 1.044, ARKX 1.265.**
Only stabilizing candidates: UFO, ARKX (ICLN lost its flag — 10d −5.8%, fell −2.6% 9/24).
VNM (R/R 1.36) cleared thin on 9/24 but the whole theme exited the candidate set today.

## (B) Leaders — where the money is (rs_spy_3m)

crypto-spot ETHA +0.68 / IBIT +0.38, software WCLD +0.35, oil/gas USO +0.35 (Hormuz risk), cyber BUG +0.32 / HACK +0.22,
software IGV +0.22, biotech ARKG +0.34. Momentum still in crypto spot, software, cyber, biotech; gold/silver (GLD
+0.17, SLV +0.05 on 3m; +0.12/+0.06 12m via rebases) recovered enough to leave the dip set. Same rotation map: duration
victims + China + housing on the dip side, risk-on momentum in crypto/AI-adjacent.
Regime: Sept 16 FOMC +25bp to 3.75–4.00% (unanimous, first hike since July 2023); 10y touched 5.135% 9/23 (highest
since 2007), 5y hit 5% on 9/23 — XLU fell −1.92% that day; Oct 27–28 hike ~70% priced. Brent ~$103.67 (9/24), Hormuz
closed. Xi-Trump summit held 9/24 with rare earths on the agenda (outcome pending at panel time).

## (C) Quick-pass memo — *unverified, challenge it*

One search per theme (9/25). Provisional buckets:

- solar (TAN) — **rotation**: borrowing-cost wrecking ball, fresh round 9/24 — First Solar −8% to $177.45, SolarEdge −5% to $31.76, Enphase −3% to $32.04 (summamoney 9/24); residential solar is financed, not bought — rate path decides demand. Thesis intact.
- rare-earth (REMX) — **rotation**: Xi-Trump summit held 9/24, rare earths on agenda (outcome unknown); China suspension expiry 11/10 still the forcing function. MP fell ~5% on summit optimism — summit-hopes erode the scarcity premium (stockmoguls 9/22); Greer remarks reintroduced no-extension risk. Licensing as leverage, intact.
- china (KWEB) — **break**: sanctions-risk selloff 9/20 (adalytica, US-China sentiment "Fear" at 30); −27.5% YTD, −40.6% 1y; outflows $3.46B 6m; trading below 200d ($29.64). Policy overhang, not a sale.
- nuclear (URNM/NLR/URA) — **rotation**: uranium spot $89.70/lb on 9/18, +4.3% YTD, term ~$96.50 — commodity firm while equities −35%+ off peaks (discoveryalert 9/21); sellers are AI-data-center sentiment + Saudi discovery fears. Cameco Q3 10/30.
- utilities (XLU) — **rotation**: worst-session day 9/23 — XLU −1.92% as 5y touched 5% (first since 2007) and 10y ~5.14% (aitrading67 9/24); Zacks 9/2 note: 2.99% yield, oversold per SA 9/6. Pure rate victim.
- clean (PBW/ICLN/QCLN) — **rotation**: rate victims like solar; ICLN LOST its stabilizing flag (10d −5.8%, −2.6% on 9/24 to $16.97; Zacks Hold 3); PBW/QCLN small-cap clean. No dated catalyst.
- space (UFO/ARKX) — **rotation**: Flight 14 NET 9/28 confirmed again — stack assembled on pad 9/23, full-stack testing underway, pending FAA (starlust 9/24; SpaceX X 9/17, 9/23). Sell-the-news risk post-launch. UFO stabilizing (10d +0.8%); ARKX thin 1.265.
- defense-us (XAR/ITA/PPA) — **rotation**: Bernstein caution on buying the defense selloff (9/23, everhint); budgets signed ($1T+ 2026, $1.5T 2027 proposal) but war-premium leg deflating; stockmoguls 9/24 notes production-capacity/execution risk, Boeing drag on ITA.
- lithium (LIT) — **break**: oversupply resurgent — GFEX fell to 136,800 yuan/t 9/23 (5-month low, −30% from May highs), Core Lithium −8% 9/24 (stockpick.market); CATL Jianxiawo got safety permit then permit hurdles extended 1yr+; SMM stockpile revision +175kt; Australian restarts (Bald Hill, Finniss). Oversupply is the thesis again.
- housing (ITB/XHB) — **break**: Sept 2026 Fed hike "fresh shockwaves" (yehey 9/24): mortgage demand −19% yoy, pending sales +0.3% Aug, builder sentiment negative; structural shortage 3–4M homes doesn't pay when 30y tracks 10y higher. Demand destruction, not rotation.
- grid/infra (IGF/PAVE/GRID) — **rotation**: theme ran hard then stalled — GRID −7.72% 3m after +27.17% 12m (tradingnews 9/2), record inflows ($283.7M 5d) into a falling fund; AI datacenter capex story intact (GE Vernova $2.4B data center orders Q1, Quanta $48B backlog); Zacks Buy on GRID (rank 2, 9/24). No dated catalyst.
- health-other (IHI) — **unclear**: med devices −20% YTD, 10.3% short interest (marketbeat), unusual put buying 9/24 (35k puts, +324% vs avg, zolmax); concentrated (ABT 18.4%, top 10 ~75%), 30–34x PE, 0.45% yield — expensive defensives in a rate shock. No thesis damage, no dated catalyst either.
- india (INDA) — **unclear**: FPI outflows ₹20,974–23,676 cr in Sept so far (angelone 9/20; multibagg 9/19), 2026 YTD outflow ₹2.45 lakh cr vs ₹1.66 lakh cr all of 2025; drivers are dollar/crude/US yields, not India-specific — rupee at record low (~95.9/USD). Flows, not thesis; tariff digestion (US tariffs on >half of $87B exports) unresolved.
- discretionary (XLY) — **rotation**: duration/demand victim — Airbnb/Booking −7.5% 9/23 as 10y broke 2007 highs (everhint 9/23); baystreet: consumers spend more on gas, less on discretionary; buy XLY? "Be wary" (margin pressure). No theme-specific trigger.
- base-metals (XME/PICK) — **unclear**: industrial cyclicals; XME (US-focused, 52w high 135.68, now 107.96) vs PICK (global majors BHP/Rio, +41% 1y). Copper-miner short interest surging (COPA +389% Sept, ABMN 9/25). Growth-fear victim more than broken thesis.

Watch thin: GRID (1.026), PICK (1.044), ARKX (1.265) are barred from buys; ARKX carries the only other stabilizing flag.
VNM/GSLV/GLD exited — VNM's FTSE-flow buy reason from 9/24 no longer in scope. The gate (cause ≥ 7 AND (stabilizing OR
catalyst ≥ 7) AND not thin AND theme_rank == 1) will likely cut the theme leaders at catalyst/necessity this round —
ICLN losing stabilization removes yesterday's stabilizing-leg path.
