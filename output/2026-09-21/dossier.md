# Research Dossier — 2026-09-21 ETF dip scan (rerun)

Market data as-of: **2026-09-18 close** (run executed Monday 2026-09-21 before a completed session).
Repo: `~/workspace/etf-dipfinder`, branch `master`. Rerun after pulling upstream process commits
(`72680ac` price lens computed, `c8f47ee` 3/5/7 anchors, `2350cf3` carry-forward + audit fail on dropped catalysts).
This file is research input for the panel. Nothing here is scored, ranked, or final.

## A. Candidate scan rows (31 candidates, is_candidate=True)

Complete CSV rows from `output/2026-09-21/scan.csv` — full header and all 31 candidate rows, in scan (orchestrator) order. Prices are the **2026-09-18 close**.

```text
,theme,asof,days,price,dd_52w,dd_pctile,dd_z,vs_sma200,vs_sma50,rs_spy_3m,rs_spy_6m,rs_spy_12m,ret_10d,vol_60d,dollar_vol,tp_pct,sl_pct,dip_low_pct,rr,size_1pct,is_dip,stabilizing,dip_score,theme_score,is_candidate
TAN,solar,2026-09-18,753.0000,45.6600,-0.3824,0.0368,-1.0707,-0.1707,-0.0909,-0.2688,-0.3617,-0.1059,-0.0432,0.3571,46120281.6148,0.6191,-0.1546,-0.0228,4.0038,0.0647,True,False,0.0647,0.0647,True
REMX,rare-earth,2026-09-18,753.0000,69.0600,-0.3695,0.0995,-0.9195,-0.1982,-0.0644,-0.2998,-0.3309,-0.0199,-0.0917,0.4018,43953064.9773,0.5860,-0.1740,-0.0647,3.3679,0.0575,True,False,0.0777,0.0777,True
KWEB,china,2026-09-18,753.0000,24.8300,-0.3865,0.0191,-1.5063,-0.1622,-0.0668,-0.0388,-0.3099,-0.5527,-0.0278,0.2566,322144986.4508,0.6301,-0.1111,-0.0483,5.6703,0.0900,True,False,0.0783,0.0783,True
URNM,nuclear,2026-09-18,753.0000,50.3200,-0.4009,0.0586,-0.8999,-0.1712,-0.0557,-0.1470,-0.3372,-0.2417,-0.1203,0.4455,45384025.4144,0.6691,-0.1929,-0.0634,3.4689,0.0518,True,False,0.0841,0.0841,True
NLR,nuclear,2026-09-18,753.0000,107.6900,-0.3448,0.0109,-0.8501,-0.1733,-0.0554,-0.1742,-0.3575,-0.3046,-0.0965,0.4056,44029909.8772,0.5263,-0.1756,-0.0463,2.9965,0.0569,True,False,0.0902,0.0841,True
URA,nuclear,2026-09-18,753.0000,41.6500,-0.3262,0.0300,-0.7441,-0.1371,-0.0347,-0.1508,-0.3006,-0.1917,-0.0886,0.4383,163246791.3387,0.4840,-0.1898,-0.0992,2.5502,0.0527,True,False,0.1939,0.0841,True
SLV,silver,2026-09-18,753.0000,59.9300,-0.4325,0.0749,-1.1592,-0.0892,0.0548,-0.0155,-0.2510,0.4147,-0.0102,0.3731,1005046482.0970,0.7621,-0.1616,-0.1592,4.7172,0.0619,True,False,0.1501,0.1501,True
UFO,space,2026-09-18,753.0000,43.2100,-0.3619,0.0150,-1.1548,-0.0801,-0.0376,-0.1619,-0.2252,0.0774,-0.0074,0.3134,8201511.0496,0.5672,-0.1357,-0.0106,4.1796,0.0737,True,False,0.1826,0.1826,True
ARKX,space,2026-09-18,753.0000,32.1200,-0.1489,0.0886,-0.5256,-0.0042,-0.0025,-0.0932,-0.1395,0.0336,-0.0071,0.2833,12627913.6446,0.1750,-0.1227,-0.0809,1.4263,0.0815,True,False,0.5845,0.1826,True
XLU,utilities,2026-09-18,753.0000,41.1000,-0.1273,0.0014,-0.8736,-0.0706,-0.0621,-0.0985,-0.2685,-0.1695,-0.0449,0.1458,902897404.7859,0.1459,-0.0631,0.0000,2.3118,0.1584,True,False,0.2016,0.2016,True
SHLD,defense-us,2026-09-18,753.0000,62.6800,-0.1940,0.0409,-0.8179,-0.0777,-0.0287,-0.0132,-0.3347,-0.2155,-0.0168,0.2372,58180524.0124,0.2407,-0.1027,-0.0744,2.3435,0.0973,True,False,0.2074,0.2074,True
XAR,defense-us,2026-09-18,753.0000,239.8600,-0.1917,0.0027,-0.7184,-0.1025,-0.0995,-0.1787,-0.2679,-0.0914,-0.0554,0.2668,68996892.6460,0.2371,-0.1155,0.0000,2.0524,0.0866,True,False,0.2393,0.2074,True
ITA,defense-us,2026-09-18,753.0000,213.8400,-0.1545,0.0027,-0.7269,-0.0692,-0.0902,-0.1268,-0.2210,-0.1021,-0.0526,0.2126,172577708.4679,0.1828,-0.0921,0.0000,1.9856,0.1086,True,False,0.3115,0.2074,True
PPA,defense-us,2026-09-18,753.0000,159.7800,-0.1382,0.0068,-0.6845,-0.0654,-0.0723,-0.1104,-0.2378,-0.0975,-0.0350,0.2019,35893723.7045,0.1603,-0.0874,-0.0019,1.8341,0.1144,True,False,0.3176,0.2074,True
PBW,clean,2026-09-18,753.0000,30.6300,-0.3444,0.1649,-0.8498,-0.1168,-0.0652,-0.2809,-0.2063,-0.0248,-0.0289,0.4053,11756273.1927,0.5253,-0.1755,-0.0251,2.9933,0.0570,True,False,0.2143,0.2143,True
ICLN,clean,2026-09-18,753.0000,17.5600,-0.2586,0.0245,-0.8654,-0.0639,-0.0216,-0.1903,-0.2244,0.0070,-0.0040,0.2989,127400536.5864,0.3489,-0.1294,-0.0393,2.6959,0.0773,True,False,0.2603,0.2143,True
QCLN,clean,2026-09-18,753.0000,47.8200,-0.3016,0.0313,-0.7185,-0.0844,-0.0551,-0.2782,-0.1646,0.0152,-0.0267,0.4198,6818404.3646,0.4318,-0.1818,-0.0280,2.3757,0.0550,True,False,0.3309,0.2143,True
ITB,housing,2026-09-18,753.0000,87.4100,-0.2211,0.1717,-0.7875,-0.0995,-0.0793,-0.1344,-0.1893,-0.3687,-0.0584,0.2807,190331356.6290,0.2838,-0.1216,-0.0234,2.3348,0.0823,True,False,0.2725,0.2725,True
XHB,housing,2026-09-18,753.0000,96.3900,-0.2022,0.1104,-0.8094,-0.0943,-0.0844,-0.1532,-0.1827,-0.3181,-0.0575,0.2498,171129986.5750,0.2534,-0.1082,-0.0173,2.3430,0.0924,True,False,0.2792,0.2725,True
INDA,india,2026-09-18,753.0000,48.0200,-0.1315,0.1199,-1.0711,-0.0426,-0.0247,-0.0540,-0.1529,-0.2823,-0.0381,0.1228,249576586.9003,0.1514,-0.0532,-0.0541,2.8482,0.1881,True,False,0.3263,0.3263,True
IGF,grid/infra,2026-09-18,753.0000,63.1700,-0.0766,0.0177,-0.8222,-0.0295,-0.0394,-0.0706,-0.2058,-0.0991,-0.0283,0.0931,47680559.7444,0.0829,-0.0403,-0.0028,2.0562,0.2480,True,False,0.3578,0.3578,True
PAVE,grid/infra,2026-09-18,753.0000,52.9600,-0.1156,0.0886,-0.6007,-0.0201,-0.0568,-0.1166,-0.1022,-0.0161,-0.0316,0.1925,85728632.2802,0.1308,-0.0834,-0.0040,1.5688,0.1200,True,False,0.5721,0.3578,True
GRID,grid/infra,2026-09-18,753.0000,178.2500,-0.1043,0.0695,-0.3942,0.0178,-0.0118,-0.1033,-0.0869,0.0446,0.0040,0.2645,87830021.7237,0.1164,-0.1145,-0.0602,1.0162,0.0873,True,True,0.7726,0.3578,True
LIT,lithium,2026-09-18,753.0000,70.5000,-0.2272,0.2398,-0.8370,-0.0515,-0.0248,-0.1607,-0.1334,0.1793,-0.0532,0.2715,20632846.5185,0.2940,-0.1175,-0.0533,2.5012,0.0851,True,False,0.3776,0.3776,True
BOTZ,ai/robot,2026-09-18,753.0000,35.1100,-0.1562,0.0640,-0.5965,-0.0484,-0.0173,-0.1071,-0.1563,-0.1448,-0.0195,0.2619,22480161.3695,0.1851,-0.1134,-0.0407,1.6325,0.0882,True,False,0.4282,0.4282,True
ARKQ,ai/robot,2026-09-18,753.0000,122.2000,-0.1503,0.1104,-0.4767,-0.0152,0.0043,-0.1049,-0.1363,0.0068,-0.0050,0.3154,10760452.4478,0.1769,-0.1366,-0.1034,1.2956,0.0732,True,False,0.5774,0.4282,True
ROBO,ai/robot,2026-09-18,753.0000,78.5000,-0.1311,0.0640,-0.4734,0.0092,-0.0242,-0.1098,-0.0525,0.0404,-0.0159,0.2769,14038705.3541,0.1508,-0.1199,-0.0349,1.2581,0.0834,True,False,0.7407,0.4282,True
AIPO,ai/robot,2026-09-18,290.0000,28.5100,-0.1800,0.0554,-0.4398,0.0213,-0.0244,-0.1840,-0.0618,0.1559,0.0014,0.4094,33133026.4051,0.2196,-0.1773,-0.0775,1.2386,0.0564,True,True,0.7730,0.4282,True
QTUM,ai/robot,2026-09-18,753.0000,147.7900,-0.1228,0.0858,-0.3561,0.1159,0.0027,-0.1412,0.1699,0.2986,0.0114,0.3448,37374613.4006,0.1400,-0.1493,-0.1052,0.9376,0.0670,True,True,0.8898,0.4282,True
BAI,ai/robot,2026-09-18,478.0000,45.1400,-0.1676,0.1743,-0.3182,0.1134,0.0238,-0.1741,0.1270,0.1718,0.0379,0.5269,100657912.6045,0.2014,-0.2281,-0.1693,0.8827,0.0438,True,True,0.9023,0.4282,True
XLY,discretionary,2026-09-18,753.0000,111.0300,-0.1048,0.1240,-0.5226,-0.0476,-0.0376,-0.0730,-0.1473,-0.2448,-0.0466,0.2005,665909038.9421,0.1170,-0.0868,-0.0503,1.3482,0.1152,True,False,0.4863,0.4863,True
```

Only four candidates are marked `stabilizing=True`: GRID, AIPO, QTUM, BAI. Full scan CSV at `output/2026-09-21/scan.csv`.

## B. Leaders (momentum, not in dip set)

ETHA, ARKG, WCLD, USO, BUG, IBIT, XOP, HACK. Rotation read: money fled rate-sensitive and
risk-duration themes (utilities, solar, clean, discretionary, housing) after the September FOMC move and
into energy/crypto spot/cyber momentum. Not scored by the dip panel; listed for context.

## C. Theme quick-pass — UNVERIFIED, challenge it (one search per theme, 2026-09-21)

- **solar (TAN, −38%, −4.3% 10d):** concentrated sector selling after the September Fed move; higher
  rates directly pressure financed residential solar; TAN crossed below its 200-day average around
  2026-09-18. Reads rate-driven, not company-specific. *Provisional: rotation.*
- **rare-earth (REMX, −37%, −9.2% 10d):** recent correction/oversold behavior while Western
  supply-chain investment remains intact; execution and valuation risks remain. No clean selloff
  explanation found — panel should not assume one. *Provisional: unclear.*
- **china tech (KWEB, −39%, −2.8% 10d):** acute selloff tied to Alibaba's 2026-08-24 ~$10.2B share
  placement and persistent China-tech outflows/downtrend. *Provisional: unclear leaning break*
  (outflows may be flow-driven, placement overhang is event-specific).
- **nuclear (URNM −40%, NLR −34%, URA −33%; 10d −9 to −12%):** September selling linked to
  AI-growth fears and high Treasury yields; reported long-term uranium pricing remained ~$97/lb.
  Cameco Q3 date carried forward (see D). *Provisional: rotation.*
- **silver (SLV, −43%, −1.0% 10d):** pressure from higher real yields / Fed expectations plus
  profit-taking after a strong run; some sources still describe a physical-market deficit. Strong
  12m relative strength (+0.41 vs SPY). *Provisional: rotation.*
- **space (UFO −36%, ARKX −15%):** search results repeated an unsupported claim about a SpaceX
  IPO/ticker SPCX — **do not use or repeat that claim**. Starship Flight 14 timing/status and
  UFO exposure require fresh independent verification (see carried-forward date in D). *Provisional: unclear.*
- **utilities (XLU, −12.7%, −4.5% 10d):** rising Treasury yields hurt bond-proxy utilities; the
  10-year traded near 5.01% and XLU was the worst-performing sector for the week ending
  2026-09-18. Textbook rate-victim dip. *Provisional: rotation.*
- **defense (SHLD, XAR, ITA, PPA, −14 to −19%, 10d −1.7 to −5.5%):** price pullback despite
  ongoing spending/backlogs; distinguish ordinary digestion from genuine program or budget
  damage. *Provisional: unclear leaning rotation.*
- **clean energy (PBW −34%, ICLN −26%, QCLN −30%):** ICLN remained deeply below its May 2026
  high; rates, policy, and margin pressure are material. *Provisional: unclear.*
- **housing (ITB −22%, XHB −20%, 10d −5.8%):** high mortgage rates, expensive homes, and builder
  incentives suppressing demand despite the structural housing shortage. *Provisional: rotation*
  (rate-driven, thesis of shortage intact).
- **india (INDA, −13.2%, −3.8% 10d):** weak/downtrend setup with fund-flow pressure; current
  evidence not strong enough for a confident rotation classification. *Provisional: unclear.*
- **grid/infra (GRID −10.4%, PAVE −11.6%, IGF −7.7%):** PAVE down ~5.5% over one month as of
  2026-09-18 with positive one-month/YTD flows reported; valuation and hyperscaler-capex
  sensitivity are the main risks. *Provisional: unclear leaning rotation.*
- **lithium (LIT, −22.7%, −5.3% 10d):** StockInvest.us rates LIT a Sell candidate (technical score
  −1.90 on −10..+10; sell signal since Sep 10, −2.73% since then); LIT crossed below its 50-day
  ($72.75) and trades below its 200-day ($76.96); structural lithium-oversupply / EV-demand
  concerns persist while short interest fell 45.5% in August. *Provisional: unclear leaning break*
  (commodity glut is a thesis question, not just flows).
- **ai/robotics (BOTZ −15.6%, ARKQ −15.0%, ROBO −13.1%, QTUM −12.3%, BAI −16.8%, AIPO −18%):**
  BOTZ down >8% over five years per Sep 2026 coverage, weighed by heavy industrial-automation
  exposure and concentration risk (Tesla/Baidu cited); BOTZ below its 50-day ($35.71) and
  200-day ($36.70); humanoid-robot ETF boom coverage names BOTZ, CHAT, AIPO as ones to watch.
  Broader AI-capex sentiment is the swing factor. *Provisional: unclear.*
- **discretionary (XLY, −10.5%, −4.7% 10d):** XLY down 6 straight weeks; hot August CPI
  (+0.3% vs +0.2% consensus) kept rate pressure on; XLY among the sectors in a 5-6 week
  downtrend per the Sep 18 weekly recap, with 10y yields near 4.97-5.01%. *Provisional: rotation*
  (market's pressure valve for rate anxiety).

## D. Confirmed catalysts carried forward — already verified, do NOT rescore as 'not found'

| theme | event | date | confirmed by |
|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | Cameco press release, 2026-07-31 (BusinessWire) |
| space | Starship Flight 14 — first orbital attempt, 26 Starlink V3, first revenue flight | **2026-09-28** | SpaceX via TechCrunch / USA Today, 2026-09-17 slip notice |
| macro | FOMC decision | **2026-10-28** | federalreserve.gov FOMC calendar |
| macro | FOMC decision | **2026-12-09** | federalreserve.gov FOMC calendar |

A panelist that cannot re-find one of these writes "carried forward, not re-searched" and keeps
the band the date earns. It does not score the theme down for having no dated trigger.

## Data gaps

- BJK/PHOX had no data in the scan window; several illiquid funds dropped by the scan.
- REMX: no clean current selloff explanation found.
- SpaceX IPO/SPCX claims in search results are unsupported — excluded from evidence.
- Regime claims above and in B are carried from the prior run's quick pass; the verifier re-checks them.
