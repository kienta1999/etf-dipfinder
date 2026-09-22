# Research Dossier — 2026-09-22 ETF dip scan (panel)

Market data as-of: **2026-09-21 close** (24 candidates, 15 themes). New completed market
session vs output/2026-09-21/scan.csv (asof 2026-09-18), so a full panel runs, not lite.
Repo: `~/workspace/etf-dipfinder`, branch `master`. Skill followed exactly: four judgment
panelists (cause, necessity, catalyst, basket) sequential; price is deterministic via
consolidate.py (no score_price.md). NOTE: SKILL.md prose still describes a fifth price
*subagent* panelist — stale relative to consolidate.py's BALLOT_LENSES; reported, not fixed.
This file is research input for the panel. Nothing here is scored, ranked, or final.

## A. Candidate scan rows (24 candidates, is_candidate=True)

Complete CSV rows from `output/2026-09-22/scan.csv` — full header and all 24 candidate
rows, in dip-depth (scan) order. Prices are the **2026-09-21 close**.

Column legend: ticker | theme | asof (last close used) | days (3y lookback) | price | dd_52w
(drawdown vs 52-week high) | dd_pctile (drawdown depth vs own 3y history; <0.10 = real event) |
dd_z (drawdown / 60d vol) | vs_sma200 / vs_sma50 | rs_spy_3m/6m/12m (excess return vs SPY) |
ret_10d | vol_60d | dollar_vol ($/day avg) | tp_pct / sl_pct (take-profit / stop-loss from scan
mechanics) | dip_low_pct (how far below the dip low) | rr (TP/SL reward-risk) | size_1pct (risk-parity
position size for 1% portfolio risk) | is_dip (scan gate) | stabilizing (10-day return > 0) |
dip_score (depth rank, 0 = most beaten up — depth, not quality) | price_score (deterministic
price-lens input) | theme_score | is_candidate.

```text
ticker,theme,asof,days,price,dd_52w,dd_pctile,dd_z,vs_sma200,vs_sma50,rs_spy_3m,rs_spy_6m,rs_spy_12m,ret_10d,vol_60d,dollar_vol,tp_pct,sl_pct,dip_low_pct,rr,size_1pct,is_dip,stabilizing,dip_score,price_score,theme_score,is_candidate
TAN,solar,2026-09-21,751.0000,46.7100,-0.3682,0.0546,-1.0191,-0.1516,-0.0669,-0.2773,-0.3517,-0.0927,-0.0277,0.3613,35777532.9544,0.5827,-0.1564,-0.0447,3.7249,0.0639,True,False,0.0491,5,0.0491,True
KWEB,china,2026-09-21,751.0000,25.1800,-0.3779,0.0246,-1.5037,-0.1489,-0.0528,-0.0365,-0.3067,-0.5472,-0.0334,0.2513,318252240.1862,0.6074,-0.1088,-0.0616,5.5818,0.0919,True,False,0.0637,4,0.0637,True
REMX,rare-earth,2026-09-21,751.0000,70.2700,-0.3584,0.0984,-0.8884,-0.1841,-0.0455,-0.3194,-0.3103,-0.0162,-0.0712,0.4035,39767469.3060,0.5587,-0.1747,-0.0808,3.1978,0.0572,True,False,0.0770,5,0.0770,True
URNM,nuclear,2026-09-21,751.0000,52.0000,-0.3809,0.0929,-0.8477,-0.1433,-0.0237,-0.1161,-0.3041,-0.2278,-0.0888,0.4493,43683550.9852,0.6152,-0.1945,-0.0937,3.1622,0.0514,True,False,0.1265,4,0.1265,True
NLR,nuclear,2026-09-21,751.0000,110.7300,-0.3263,0.0246,-0.7984,-0.1494,-0.0281,-0.1526,-0.3324,-0.3131,-0.0769,0.4088,43430010.6797,0.4844,-0.1770,-0.0725,2.7369,0.0565,True,False,0.1327,5,0.1265,True
SLV,silver,2026-09-21,751.0000,59.6300,-0.4353,0.0738,-1.1671,-0.0943,0.0475,-0.0295,-0.2294,0.3858,-0.0032,0.3730,965332853.1730,0.7709,-0.1615,-0.1550,4.7733,0.0619,True,False,0.1486,6,0.1486,True
XLU,utilities,2026-09-21,751.0000,40.6600,-0.1303,0.0014,-0.9005,-0.0736,-0.0634,-0.1258,-0.2690,-0.1863,-0.0492,0.1447,891950870.9871,0.1499,-0.0627,0.0000,2.3913,0.1595,True,False,0.1764,6,0.1764,True
URA,nuclear,2026-09-21,751.0000,42.9800,-0.3046,0.0505,-0.6894,-0.1096,-0.0039,-0.1233,-0.2732,-0.1989,-0.0669,0.4419,161719660.8665,0.4381,-0.1914,-0.1270,2.2896,0.0523,True,False,0.2101,4,0.1265,True
UFO,space,2026-09-21,751.0000,44.1700,-0.3478,0.0369,-1.1058,-0.0608,-0.0150,-0.1339,-0.2237,0.1029,0.0108,0.3145,8328358.0437,0.5332,-0.1362,-0.0321,3.9152,0.0734,True,True,0.2123,9,0.2123,True
PBW,clean,2026-09-21,751.0000,30.9600,-0.3313,0.1571,-0.8123,-0.0992,-0.0443,-0.2838,-0.1795,-0.0506,-0.0173,0.4079,10819771.9465,0.4955,-0.1766,-0.0442,2.8055,0.0566,True,False,0.2676,4,0.2676,True
XAR,defense-us,2026-09-21,751.0000,243.5500,-0.1788,0.0123,-0.6640,-0.0885,-0.0832,-0.1647,-0.2568,-0.1074,-0.0365,0.2692,70193987.2659,0.2177,-0.1166,-0.0157,1.8674,0.0858,True,False,0.2735,7,0.2735,True
GLD,gold,2026-09-21,751.0000,398.3800,-0.1967,0.0683,-0.8239,-0.0430,0.0127,-0.0058,-0.2350,0.0032,-0.0206,0.2387,4549554318.1810,0.2448,-0.1034,-0.0839,2.3685,0.0968,True,False,0.2822,6,0.2822,True
ITB,housing,2026-09-21,751.0000,88.2000,-0.2140,0.1995,-0.7624,-0.0907,-0.0692,-0.1279,-0.1894,-0.3761,-0.0529,0.2807,180476627.2087,0.2723,-0.1216,-0.0321,2.2402,0.0823,True,False,0.2884,2,0.2884,True
ICLN,clean,2026-09-21,751.0000,17.8000,-0.2485,0.0587,-0.8276,-0.0514,-0.0066,-0.2188,-0.2104,0.0121,0.0017,0.3003,125762267.0099,0.3307,-0.1300,-0.0522,2.5432,0.0769,True,True,0.2895,8,0.2676,True
XHB,housing,2026-09-21,751.0000,96.9600,-0.1930,0.1311,-0.7749,-0.0834,-0.0718,-0.1482,-0.1813,-0.3263,-0.0557,0.2491,172923192.0030,0.2391,-0.1078,-0.0285,2.2175,0.0927,True,False,0.3027,3,0.2884,True
ITA,defense-us,2026-09-21,751.0000,216.1400,-0.1454,0.0123,-0.6807,-0.0595,-0.0786,-0.1229,-0.2257,-0.1163,-0.0409,0.2137,173239356.0751,0.1702,-0.0925,-0.0106,1.8396,0.1081,True,False,0.3234,7,0.2735,True
PPA,defense-us,2026-09-21,751.0000,161.1700,-0.1281,0.0164,-0.6298,-0.0548,-0.0600,-0.1054,-0.2423,-0.1113,-0.0213,0.2033,33581917.0562,0.1469,-0.0880,-0.0135,1.6681,0.1136,True,False,0.3301,7,0.2735,True
INDA,india,2026-09-21,751.0000,48.5000,-0.1228,0.1612,-0.9872,-0.0325,-0.0146,-0.0701,-0.1577,-0.2814,-0.0283,0.1244,252595163.1605,0.1400,-0.0539,-0.0635,2.5990,0.1856,True,False,0.3539,3,0.3539,True
IGF,grid/infra,2026-09-21,751.0000,63.3300,-0.0742,0.0096,-0.8230,-0.0272,-0.0359,-0.0876,-0.2152,-0.1038,-0.0269,0.0902,49237391.3453,0.0802,-0.0390,-0.0054,2.0531,0.2561,True,False,0.3670,7,0.3670,True
LIT,lithium,2026-09-21,751.0000,70.8300,-0.2236,0.2186,-0.8231,-0.0476,-0.0198,-0.1802,-0.1366,0.1743,-0.0452,0.2716,20117784.0709,0.2880,-0.1176,-0.0577,2.4484,0.0850,True,False,0.3955,5,0.3955,True
QCLN,clean,2026-09-21,751.0000,48.9100,-0.2857,0.0478,-0.6754,-0.0639,-0.0310,-0.2922,-0.1301,0.0035,-0.0105,0.4230,6518005.2747,0.3999,-0.1831,-0.0497,2.1836,0.0546,True,False,0.4368,7,0.2676,True
VNM,vietnam,2026-09-21,751.0000,17.4100,-0.1207,0.2514,-0.5185,-0.0435,-0.0026,-0.1082,-0.1390,-0.2037,-0.0413,0.2328,11418040.8051,0.1373,-0.1008,-0.0615,1.3618,0.0992,True,False,0.4996,2,0.4996,True
PAVE,grid/infra,2026-09-21,751.0000,53.0800,-0.1136,0.0943,-0.6201,-0.0184,-0.0534,-0.1441,-0.1139,-0.0439,-0.0377,0.1833,83896394.4263,0.1282,-0.0794,-0.0062,1.6156,0.1260,True,False,0.5923,5,0.3670,True
ARKX,space,2026-09-21,751.0000,32.9000,-0.1282,0.1448,-0.4468,0.0190,0.0212,-0.0555,-0.1075,0.0186,0.0211,0.2870,13043864.1831,0.1471,-0.1243,-0.1027,1.1836,0.0805,True,True,0.7256,7,0.2123,True
```

Only three candidates are marked `stabilizing=True`: **UFO** (space), **ICLN** (clean), **ARKX** (space).

## B. Leaders (momentum, not in dip set)

Top 8 by rs_spy_3m, from the same scan (the LEADERS block):

ETHA (crypto-spot, +0.55 3m), WCLD (software, +0.38), ARKG (biotech, +0.38), BUG (cyber, +0.34),
IBIT (crypto-spot, +0.30), USO (oil/gas, +0.27), SKYY (software, +0.26), HACK (cyber, +0.26).

Rotation read: money sits in crypto spot, software, biotech, cyber momentum and energy, while
rate-sensitive and risk-duration themes (solar, clean, utilities, housing, nuclear, China) lag.
Not scored by the dip panel; listed for context.

## C. Theme quick-pass — UNVERIFIED, challenge it (one search per theme, 2026-09-22)

Regime: Sep 16 FOMC hiked +25bp to 3.75–4.00% (first hike since 2023); 16 of 18 policymakers
see ≥1 more hike this year. 10y hit 5.041% on Sep 15 (highest since July 2007). Brent
breached $108/bbl after Saudi East-West pipeline shutdown; US-Israel war with Iran inflames
inflation. OilPrice.com (crawled 9/21) reports uranium futures rose to $73.50/lb this week
while uranium equities fell — and flags possible Ukraine ceasefire / thaw in US-Russia
relations as a new pressure, plus Kazatomprom ramping output to 4,000 t/yr. SpaceX's
Starship Flight 14 is scheduled TODAY (9/22, ~8am EDT window, pending regulatory approval),
first orbital attempt with 26 Starlink V3 satellites; SpaceX is now a listed company (SPCX).

- **solar (TAN, −37%, −2.8% 10d):** Fed hiked mid-September; residential solar is financed,
  so rate path hits demand directly. First Solar withdrew its ITC patent case (9/20, company
  calls it procedural, stock fell 5%). Sector selling concentrated, not broad-market.
  *Provisional: rotation.*
- **china (KWEB, −38%, −3.3% 10d):** in a bear market; Alibaba's 8/24 $10.2B placement
  overhang plus persistent outflows (1m −$2.09B AUM). Fresh sanctions-risk headlines
  (Adalytica, 9/20) keep policy overhang alive. *Provisional: unclear leaning break.*
- **rare-earth (REMX, −36%, −7.1% 10d):** mixed: China Rare Earth Group in talks to acquire
  Shenghe (MP's indirect 3% holder, reported 9/19 — strategic interest vs geopolitical
  scrutiny), China possibly delaying export controls, Lynas double-bottoming with
  record FY26 results but profit miss. *Provisional: unclear.*
- **nuclear (URNM −38%, NLR −33%, URA −30%; 10d −7 to −9%):** NEW since yesterday: oilprice.com
  reports uranium equities tumbling despite strong prices, citing Ukraine-ceasefire talk
  (reduces Russia-sanctions bid) and Kazatomprom output ramp. Long-term price still ~$97/lb.
  Cameco Q3 (10/30) carried forward. The ban-thesis weakening is the thing to score.
  *Provisional: rotation, weaker than yesterday — challenge it.*
- **silver (SLV, −44%, −0.3% 10d):** Fed-day reversal: silver's $65.47 rally vanished after
  the FOMC mapped another hike; real yields + dollar both against it. 12m relative strength
  still strong (+0.39). *Provisional: rotation.*
- **utilities (XLU, −13%, −4.9% 10d):** textbook rate victim — Dow Jones 9/18 & 9/21 roundups:
  utilities down as 10y/30y test multiyear/19-year highs; XLU down ~5% YTD. Deep in the
  defensive rotation, not an idiosyncratic dip. *Provisional: rotation.*
- **space (UFO −35% stabilizing, ARKX −13% stabilizing):** Flight 14 is TODAY (9/22) —
  catalyst is concurrent, not future; a test flight can also be a sell-the-news event.
  Yesterday's memo cited SpaceX as a top-5 UFO holding post-IPO (~5%) — verify against
  current holdings. The unsupported "SpaceX IPO/ticker SPCX" claims from earlier searches
  are now confirmed real (SPCX listed, ~$2T market cap). *Provisional: unclear —
  catalyst status changed since yesterday.*
- **clean (PBW −33%, ICLN −25% stabilizing, QCLN −29%):** rate victims like solar; ICLN/QCLN
  +8% YTD — the selloff is a giveback of the summer rally. Individual winners (Bloom Energy
  +223% YTD) show stock dispersion, but ETFs lag. *Provisional: rotation.*
- **defense-us (XAR −18%, ITA −15%, PPA −13%):** digestion after a run: Guggenheim launched
  bullish coverage of 22 defense names (9/15); $1.5T 2027 budget proposal supports backlogs.
  AI-safety selloff hit AI-linked names mid-month. *Provisional: rotation.*
- **gold (GLD, −20%, −2.1% 10d):** $4,401/oz on 9/21, ~22% off January record; sold on the
  hawkish FOMC and hot August PPI (5.4% y/y) via real yields. Central bank buying and ETF
  inflows still a backstop — "pullback, not a new regime" (briefs.co 9/19). *Provisional:
  rotation.*
- **housing (ITB −21%, XHB −19%):** demand shock: NAHB index 32 (1-yr low, 9/16), 30y mortgage
  6.76–7% (1-yr high), Lennar Q3 earnings −40%, 38% of builders cutting prices. Existing-home
  sales at a 14-month low. This is demand destruction, not multiple compression.
  *Provisional: break — challenge it.*
- **india (INDA, −12%, −2.8% 10d):** FII flows returned in August (two-year high) after the
  spring $20B outflow; recovery depends on inflows holding. US tariffs hit SE Asia hard in
  early September. Cause score 5 yesterday — structural. *Provisional: unclear.*
- **grid/infra (IGF −7%, PAVE −11%):** shallow dip on strong fundamentals; GRID ETF saw
  $284M of 5-day inflows into a falling fund (accumulation, ~Aug 31 article). IGF short
  interest doubled in August (bet against the pause). *Provisional: rotation.*
- **lithium (LIT, −22%, −4.5% 10d):** oversupply is the thesis: Albemarle fell 3.5% on 9/17,
  weak lithium prices, CEO change, CATL mine resumption overhang. Cause 4 yesterday.
  *Provisional: break.*
- **vietnam (VNM, −12%, −4.1% 10d):** FTSE upgrade to secondary emerging-market status
  took effect 9/21 — catalyst is past; tariff shock earlier in September still digested.
  *Provisional: unclear.*
