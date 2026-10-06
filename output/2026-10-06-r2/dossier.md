> Run by: Muse Spark (muse-spark) — full panel

# ETF Dip Panel Dossier — RUN_DATE 2026-10-06 (run id `2026-10-06-r2`)

## A. Candidates — full scan rows (asof 2026-10-05)

### Column legend (scan.csv, one row per fund)
- `theme`: this run's theme label
- `asof`: price date (2026-10-05)
- `days`: lookback window used by the scan
- `price`: closing price at asof
- `dd_52w`: drawdown fraction from 52-week high (negative)
- `dd_pctile`: percentile of current drawdown vs 3-year drawdown history (low = deep for this fund)
- `dd_z`: z-score of current drawdown vs 3-year mean/std
- `vs_sma200`: distance from 200-day SMA (fraction)
- `vs_sma50`: distance from 50-day SMA (fraction)
- `rs_spy_3m` / `rs_spy_6m` / `rs_spy_12m`: relative strength vs SPY over 3/6/12 months
- `ret_10d`: 10-day return
- `vol_60d`: 60-day realized volatility (daily, as fraction)
- `dollar_vol`: 60-day average daily dollar volume
- `tp_pct`: take-profit fraction above current price used by size logic
- `sl_pct`: stop-loss fraction below current price
- `dip_low_pct`: fraction below current price at which the dip entry triggers
- `rr`: reward/risk ratio (thin if < 1.3)
- `size_1pct`: risk-parity size factor
- `is_dip`: True (in a dip by the scan's gate)
- `stabilizing`: True if scan flags the dip as stabilizing (not still accelerating down)
- `dip_score`: scan dip-strength score
- `price_score`: 1–7 deterministic technical score from scan.py
- `theme_score`: theme leader's dip_score (ties candidates to their theme)
- `is_candidate`: True for the 24 scored candidates; False = in dip but not a candidate

### Candidate rows (verbatim from data/scan.csv)

| # | row |
|---|-----|
| 1 | REMX,rare-earth,2026-10-05,751.0000,63.5400,-0.4199,0.0082,-1.0591,-0.2598,-0.1199,-0.2550,-0.4634,-0.2374,-0.0958,0.3964,40671043.9181,0.7238,-0.1717,-0.0093,4.2163,0.0583,True,False,0.0696,6,0.0696,True |
| 2 | TAN,solar,2026-10-05,751.0000,43.6700,-0.4093,0.0246,-1.1586,-0.2040,-0.0928,-0.2421,-0.3755,-0.2247,-0.0651,0.3533,33201517.9777,0.6929,-0.1530,-0.0153,4.5296,0.0654,True,False,0.0838,5,0.0838,True |
| 3 | URNM,nuclear,2026-10-05,751.0000,47.9200,-0.4295,0.0328,-0.9606,-0.2059,-0.0963,-0.0931,-0.4202,-0.3583,-0.0785,0.4471,26012480.4038,0.7527,-0.1936,-0.0165,3.8883,0.0517,True,False,0.1114,4,0.1114,True |
| 4 | NLR,nuclear,2026-10-05,751.0000,103.7300,-0.3689,0.0068,-0.9193,-0.1956,-0.0846,-0.1024,-0.4043,-0.4210,-0.0632,0.4013,40085445.2897,0.5846,-0.1738,-0.0099,3.3641,0.0575,True,False,0.1464,5,0.1114,True |
| 5 | URA,nuclear,2026-10-05,751.0000,40.1900,-0.3498,0.0232,-0.7932,-0.1637,-0.0708,-0.0762,-0.3551,-0.3315,-0.0649,0.4410,122934304.2042,0.5379,-0.1909,-0.0664,2.8173,0.0524,True,False,0.2438,5,0.1114,True |
| 6 | KWEB,china,2026-10-05,751.0000,24.5600,-0.3922,0.0232,-1.6169,-0.1551,-0.0610,-0.0761,-0.3091,-0.5635,-0.0246,0.2426,379901067.8385,0.6453,-0.1050,-0.0379,6.1434,0.0952,True,False,0.1121,4,0.1121,True |
| 7 | SLV,silver,2026-10-05,751.0000,55.1300,-0.4779,0.0451,-1.2431,-0.1634,-0.0461,-0.0265,-0.3477,0.1260,-0.0755,0.3845,889318006.4473,0.9155,-0.1665,-0.0860,5.4989,0.0601,True,False,0.1189,7,0.1189,True |
| 8 | SHLD,defense-us,2026-10-05,751.0000,60.4100,-0.2232,0.0232,-1.1054,-0.1096,-0.0651,-0.0918,-0.3714,-0.3113,-0.0438,0.2019,104922375.3879,0.2874,-0.0874,-0.0397,3.2866,0.1144,True,False,0.1613,5,0.1613,True |
| 9 | XAR,defense-us,2026-10-05,751.0000,231.2800,-0.2202,0.0027,-0.8714,-0.1348,-0.1102,-0.2104,-0.3039,-0.1973,-0.0504,0.2526,76295370.8897,0.2823,-0.1094,-0.0001,2.5805,0.0914,True,False,0.2652,6,0.1613,True |
| 10 | ITA,defense-us,2026-10-05,751.0000,206.9800,-0.1817,0.0014,-0.9033,-0.1003,-0.0999,-0.1934,-0.2610,-0.1793,-0.0424,0.2011,185005733.9785,0.2220,-0.0871,0.0000,2.5492,0.1148,True,False,0.3004,6,0.1613,True |
| 11 | PPA,defense-us,2026-10-05,751.0000,155.4600,-0.1589,0.0027,-0.8405,-0.0897,-0.0791,-0.1663,-0.2728,-0.1706,-0.0354,0.1891,46760024.4597,0.1890,-0.0819,-0.0054,2.3079,0.1221,True,False,0.3354,6,0.1613,True |
| 12 | UFO,space,2026-10-05,751.0000,43.5600,-0.3567,0.0301,-1.3064,-0.0801,-0.0239,-0.1404,-0.2994,-0.0069,-0.0137,0.2730,8431172.1468,0.5545,-0.1182,-0.0370,4.6900,0.0846,True,False,0.2179,6,0.2179,True |
| 13 | ARKX,space,2026-10-05,751.0000,32.9100,-0.1280,0.1571,-0.4902,0.0132,0.0121,-0.0293,-0.1107,-0.0645,0.0003,0.2611,14713202.2474,0.1468,-0.1131,-0.1030,1.2981,0.0884,True,True,0.8466,6,0.2179,True |
| 14 | XLU,utilities,2026-10-05,751.0000,39.9700,-0.1451,0.0123,-1.0560,-0.0870,-0.0552,-0.1578,-0.3042,-0.2348,-0.0170,0.1374,1234122815.0538,0.1697,-0.0595,-0.0180,2.8526,0.1681,True,False,0.2385,6,0.2385,True |
| 15 | PBW,clean,2026-10-05,751.0000,29.3200,-0.3667,0.0587,-0.9769,-0.1450,-0.0737,-0.2007,-0.2467,-0.1950,-0.0530,0.3754,10051963.3604,0.5791,-0.1626,-0.0119,3.5628,0.0615,True,False,0.2442,4,0.2442,True |
| 16 | ICLN,clean,2026-10-05,751.0000,17.2900,-0.2700,0.0178,-0.9820,-0.0801,-0.0206,-0.1444,-0.2128,-0.0708,-0.0287,0.2750,118514246.0929,0.3699,-0.1191,-0.0278,3.1069,0.0840,True,False,0.3431,7,0.2442,True |
| 17 | GLD,gold,2026-10-05,751.0000,379.5500,-0.2346,0.0437,-0.9443,-0.0878,-0.0426,-0.0334,-0.2943,-0.1005,-0.0473,0.2485,3331369191.9345,0.3065,-0.1076,-0.0384,2.8493,0.0929,True,False,0.2800,6,0.2800,True |
| 18 | IGF,grid/infra,2026-10-05,751.0000,62.0100,-0.0935,0.0068,-1.1114,-0.0489,-0.0415,-0.1157,-0.2523,-0.1268,-0.0208,0.0841,62212403.9221,0.1032,-0.0364,-0.0113,2.8313,0.2744,True,False,0.3160,7,0.3160,True |
| 19 | PAVE,grid/infra,2026-10-05,751.0000,54.1100,-0.0964,0.1366,-0.5586,-0.0038,-0.0234,-0.0801,-0.1279,-0.0301,0.0194,0.1726,76934398.4258,0.1067,-0.0748,-0.0298,1.4278,0.1338,True,True,0.7558,6,0.3160,True |
| 20 | ITB,housing,2026-10-05,751.0000,85.5800,-0.2374,0.1393,-0.8543,-0.1119,-0.0820,-0.1747,-0.2359,-0.3690,-0.0297,0.2779,210578860.9886,0.3113,-0.1203,-0.0025,2.5870,0.0831,True,False,0.3279,2,0.3279,True |
| 21 | XHB,housing,2026-10-05,751.0000,85.5800,-0.1985,0.1175,-0.8061,-0.0858,-0.0602,-0.1537,-0.2041,-0.2975,-0.0068,0.2462,189996410.6395,0.2476,-0.1066,-0.0218,2.3227,0.0938,True,False,0.4400,3,0.3279,True |
| 22 | INDA,india,2026-10-05,751.0000,46.5700,-0.1577,0.0423,-1.2839,-0.0652,-0.0488,-0.0948,-0.1962,-0.2799,-0.0398,0.1228,241918445.6608,0.1872,-0.0532,-0.0247,3.5203,0.1880,True,False,0.3434,5,0.3434,True |
| 23 | LIT,lithium,2026-10-05,751.0000,70.1300,-0.2313,0.1885,-0.9135,-0.0608,-0.0294,-0.0886,-0.2186,0.0384,-0.0099,0.2532,9623054.3167,0.3008,-0.1096,-0.0483,2.7442,0.0912,True,False,0.3921,5,0.3921,True |
| 24 | IHI,health-other,2026-10-05,751.0000,51.5900,-0.1959,0.0888,-0.8128,-0.0499,-0.0328,-0.0499,-0.2106,-0.3056,-0.0069,0.2410,139983864.6246,0.2436,-0.1044,-0.0811,2.3344,0.0958,True,False,0.4617,4,0.4617,True |

## B. Theme leaders (theme_rank candidate)

| # | ticker | theme | why leads |
|---|--------|-------|-----------|
| 1 | REMX | rare-earth | sole candidate |
| 2 | TAN | solar | sole candidate |
| 3 | URNM | nuclear | strongest dip_score (0.1114) among URNM/NLR/URA |
| 6 | KWEB | china | sole candidate |
| 7 | SLV | silver | sole candidate |
| 8 | SHLD | defense-us | strongest dip_score (0.1613) among SHLD/XAR/ITA/PPA |
| 12 | UFO | space | sole space candidate (ARKX is a candidate but not theme leader) |
| 14 | XLU | utilities | sole candidate |
| 15 | PBW | clean | strongest dip_score (0.2442) among PBW/ICLN |
| 17 | GLD | gold | sole candidate |
| 18 | IGF | grid/infra | strongest dip_score (0.3160) among IGF/PAVE |
| 20 | ITB | housing | strongest dip_score (0.3279) among ITB/XHB |
| 22 | INDA | india | sole candidate |
| 23 | LIT | lithium | sole candidate |
| 24 | IHI | health-other | sole candidate |

Stabilizing flags: only ARKX and PAVE are marked stabilizing=True.

## C. Quick-pass memo (2026-10-06, web search; all themes, one search per theme)

*These are quick-pass provisional buckets — unverified — challenge them with your own research. Panelists: score from THIS dossier + your own web research only; open nothing from other runs.*

1. **rare-earth (REMX) — provisional: rotation.** Sector-wide selloff on US–China thaw hopes after the Trump–Xi September meeting; MP Materials −15.8% in 30 days on sentiment, not operations; Nov 10 2026 export-control suspension expiry is the forcing function. Source: adalytica 2026-10-05.
2. **solar (TAN) — provisional: unclear.** Fed hiked Sept 16 (first in 3+ yrs, 3.75–4.00%); residential solar crushed (Enphase, Sunrun); utility-scale (First Solar) contracted and less affected — rate headwind is real fundamentals, but segment split matters.
3. **nuclear (URNM, NLR, URA) — provisional: rotation.** Uranium at $96/lb (19-yr high) but equities down (NLR ~−35% off high) — AI-demand skepticism, Oklo FERC rejection, Holtec IPO pulled; Cameco Q3 due 2026-10-30 is a live catalyst.
4. **china (KWEB) — provisional: unclear.** KWEB −28% YTD; sanctions risk, US–China sentiment in "Fear"; Stock Connect reopens Oct 8; policy overhang dominates fundamentals.
5. **silver (SLV) — provisional: rotation.** Parabolic +150% YTD then sharp selloff on China physical squeeze; volatile, squeeze-driven — bull story intact per sources.
6. **defense-us (SHLD, XAR, ITA, PPA) — provisional: rotation.** ITA −18.2% from Aug 14 high, near bear market; 7 straight weekly declines (worst since 2006); 9-wk RSI 30.2 (oversold); budget uncertainty despite live conflicts — spending intact; RTX Q3 (Oct 20), Lockheed (Oct 22), Howmet (Oct 29) all imminent.
7. **space (UFO, ARKX) — provisional: unclear.** UFO −40% from $68 high; SpaceX IPO valuation cut to $1.8T; Blue Origin New Glenn explosion — valuation reset, not obviously sentiment-only.
8. **utilities (XLU) — provisional: rotation.** XLU −13% in a quarter; 10y >5% since Sept 15; dividend stocks hurt by rate competition — pure rate-driven, earnings story intact.
9. **clean (PBW, ICLN) — provisional: rotation.** ICLN crushed by higher rates — rate-driven; Vestas Q3 2026-11-11 for PBW sleeve.
10. **gold (GLD) — provisional: rotation.** Gold fell 4% to lowest since early August as 10y hit 5.3% and 30y 5.4%; record $2.91B GLD liquidation on panic; central-bank buying intact, oversold/under-owned per Seeking Alpha — yield-driven, not demand break.
11. **grid/infra (IGF, PAVE) — provisional: rotation.** No selloff-specific news found; PAVE −9.6% drawdown, stabilizing flag; valuation questions on Vertiv-type AI exposures; infrastructure spending story intact.
12. **housing (ITB, XHB) — provisional: rotation.** Homebuilders down on mortgage rates (30y at 4-yr high); XHB ~−21% from high; structural shortage persists; D.R. Horton Q4/FY26 results Oct 29 live catalyst.
13. **india (INDA) — provisional: unclear.** India ETFs fall as US–China thaw erodes the "China alternative" premium — INDA below 50d/200d, testing $46 support; macro/geopolitical, not earnings-driven.
14. **lithium (LIT) — provisional: unclear.** Spot lithium carbonate in China slipped back toward one-month lows on rising Australian supply (surplus persists); ALB below 50d and 200d, RSI ~35, distribution-heavy selling; Albemarle Q3 2026-11-04 is a live catalyst. Commodity fundamentals impaired, not just sentiment — panelists judge break vs rotation.
15. **health-other (IHI) — provisional: unclear.** Med-device selloff (−12.5% YTD); defensive healthcare exposure; AbbVie/Intuitive/Medtronic Q3 earnings window Oct 21–29 pending; unclear whether healthcare de-rating is overdone.


## D. Confirmed catalysts carried forward — already verified, do NOT rescore as 'not found'

| theme | event | date | floor | confirmed by |
|---|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | **catalyst >= 7** | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 and 2026-10-01 (BusinessWire 20260730139928: "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026"); re-verified 2026-10-04 on SEC EDGAR 6-K ex-99.1 (Cameco Q2 release 2026-07-31, acc. 0001193125-26-326768), same sentence |
| macro | FOMC decision (Oct 27-28 meeting, statement on second day) | **2026-10-28** |  | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: October 27-28) |
| macro | FOMC decision (Dec 8-9 meeting, statement on second day) | **2026-12-09** |  | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: December 8-9, SEP meeting) |
| ai/robot | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | **2027-03-14** |  | nvidia.com GTC FAQ |
| solar | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | **2026-10-14** | **catalyst >= 7** | Reuters/SRN 2026-09-11; SMM; Sxcoal; re-verified 2026-09-29 (solarpowerworld 9/20, Sxcoal 9/14, pv-magazine) and 2026-10-01 (pv-tech.org 9/15: "Commission is scheduled to make its final determination on 14 October 2026") |
| solar | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | **2026-11-02** |  | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 (Sxcoal, pv-magazine, taiyangnews) and 2026-10-01 (pv-tech.org 9/15: "final AD/CVD duty orders, currently scheduled for 2 November 2026") |
| housing | D.R. Horton Q4/FY26 results, before market open, 8:30 a.m. ET call | **2026-10-29** | **catalyst >= 7** | D.R. Horton investor site press release, 2026-09-10 (BusinessWire): "will release financial results for its fourth quarter and fiscal year ended September 30, 2026 on Thursday, October 29, 2026 before the market opens" |
| lithium | Albemarle Q3 2026 results, after NYSE close; earnings call Nov 5, 8:00 a.m. EST | **2026-11-04** | **catalyst >= 7** | Albemarle PR Newswire, 2026-10-01: "will release its third quarter 2026 earnings after the NYSE closes on Wednesday, November 4, 2026" |
| utilities | Southern Company Q3 2026 earnings released by 7:30 a.m. ET; analyst call 1 p.m. ET | **2026-11-05** | **catalyst >= 7** | southerncompany.mediaroom.com press release 2026-09-25 (fetched): "plans to release its earnings for the third quarter of 2026 by 7:30 a.m. ET on Thursday, November 5, 2026"; Southern is XLU's #2 holding at 7.69% (SSGA, 2026-10-01) |
| defense-us | RTX Q3 2026 results before market open; 8:30 a.m. ET call | **2026-10-20** | **catalyst >= 7** | rtx.com news release 2026-09-29 (PRNewswire, fetched): "will issue its third quarter 2026 earnings results on Tuesday, October 20, prior to the stock market opening" |
| defense-us | Lockheed Martin Q3 2026 results before market open; 8:30 a.m. ET webcast | **2026-10-22** |  | news.lockheedmartin.com release dated 2026-10-01 (fetched; also at investors.lockheedmartin.com): call "Thursday, Oct. 22, 2026, at 8:30 a.m. ET", results published prior to market opening |
| defense-us | Howmet Aerospace Q3 2026 results ~7:00 a.m. ET, webcast 10:00 a.m. ET (also a PAVE holding) | **2026-10-29** |  | howmet.com press release 2026-10-01 (fetched): "Thursday, October 29, 2026. The press release and presentation materials will be available at approximately 7:00 AM ET" |
| defense-us | FY27 continuing resolution (Division A of P.L. 119-103) expires: appropriations cliff, outcome cuts both ways | **2026-12-11** |  | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. A sec. 106(3): funds available until "December 11, 2026"; CRS R49353 (2026-09-17) |
| grid/infra | Surface Transportation Extension Act of 2026 (Division C of P.L. 119-103) ends: IIJA highway/transit authorities lapse unless reauthorized or re-extended | **2026-12-11** |  | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. C: "extension end date means December 11, 2026", extension period from 2026-10-01 |
| clean | Vestas Q3 2026 interim report (quiet period from 2026-10-10) | **2026-11-11** |  | vestas.com/en/investor/Calendar-Events (fetched 2026-10-04): "Disclosure of Q3 2026 interim report", 11 November 2026 |
| india | HDFC Bank board meeting to approve results for the quarter ended 2026-09-30 (Q2 FY27) | **2026-10-17** | **catalyst >= 7** | HDFC Bank Form 6-K filed 2026-09-22 (SEC acc. 0001193125-26-397434, text read via stocktitan): board meets 2026-10-17 to approve unaudited standalone and consolidated results; trading window closed 9/24-10/19 |
| india | RBI MPC policy decision (Oct 5-7 meeting, decision on the last day); next meeting Dec 2-4 | **2026-10-07** |  | rbi.org.in press release 2026-03-23 "Meeting Schedule of the Monetary Policy Committee for 2026-2027" (prid=62422, fetched): October 5-7, 2026 |
| china | APEC Economic Leaders' Meeting, Shenzhen, Nov 18-19 (CEO Summit Nov 17-18) | **2026-11-18** |  | Shenzhen Government Online (sz.gov.cn) 2026-09-10 (fetched): Economic Leaders' Meeting "Nov. 18 to 19"; Xi announced Shenzhen host 2025-11 (cppcc.gov.cn) |
| rare-earth | DFARS 252.225-7052: from 2027-01-01 US defense contractors may not deliver NdFeB/SmCo magnets (or tantalum/tungsten) mined, refined, separated, melted or produced in China, Russia, Iran or North Korea; full supply chain for magnets | **2027-01-01** |  | acquisition.gov DFARS 252.225-7052 (clause MAY 2024), paras (b)(1)(ii), (b)(2), (b)(3): "Effective January 1, 2027, the Contractor shall not deliver..." (fetched 2026-10-05) |
| rare-earth | China's suspension of its Oct-2025 export controls (rare-earth items, equipment and technology; MOFCOM/GACC No. 70) rides the Kuala Lumpur joint arrangement, now extended from 2026-11-10 to 2027-01-10; expiry vs further extension cuts both ways | **2027-01-10** |  | MOFCOM 美大司负责人解读第八轮中美经贸磋商成果, PubDate 2026-09-28 (mofcom.gov.cn, fetched 2026-10-05), item 8: "中美双方同意在将吉隆坡经贸磋商联合安排延期至2027年1月10日的基础上，继续积极探讨这一事项"; the KL arrangement is what suspended these controls "至2026年11月10日" (MOFCOM/GACC No. 70); formal notice amending No. 70 not yet on the mofcom 2026 announcement list (checked 2026-10-05) |
| china | US-China Kuala Lumpur joint arrangement (US 24% reciprocal-tariff suspension, China's countermeasures and export-control suspensions) extended to 2027-01-10; renewal vs snapback cuts both ways | **2027-01-10** |  | MOFCOM 美大司负责人解读第八轮中美经贸磋商成果, PubDate 2026-09-28 (mofcom.gov.cn, fetched 2026-10-05), item 8 |
| lithium | China's suspended Oct-2025 export controls on lithium batteries and artificial-graphite anode items (No. 58, suspended by No. 70) now run with the KL arrangement to 2027-01-10; two-way | **2027-01-10** |  | MOFCOM 美大司负责人解读第八轮中美经贸磋商成果, PubDate 2026-09-28 (mofcom.gov.cn, fetched 2026-10-05), item 8 |
| solar | Section 232 proclamation "Adjusting Imports of Polysilicon and Its Derivatives": 15% duty on derivatives plus minimum import prices ($0.22/W cells, $0.38/W modules) from 12:01 a.m. ET | **2026-12-04** |  | whitehouse.gov presidential action signed 2026-08-06 (fetched 2026-10-05): "12:01 a.m. eastern time on December 4, 2026" |
| clean | Section 232 polysilicon tariff (15%) and module/cell minimum import prices take effect (helps US module makers, e.g. First Solar sleeve; hurts importers) | **2026-12-04** |  | whitehouse.gov presidential action signed 2026-08-06 (fetched 2026-10-05) |
| utilities | PJM 2029/2030 Base Residual Auction results posted (bidding window 2026-12-09 to 12-15) | **2026-12-22** |  | pjm.com RPM auction schedule (xlsx, fetched 2026-10-05): 2029/2030 BRA "Auction results posted" 2026-12-22 |
| india | RBI MPC policy decision (Dec 2-4 meeting, decision on the last day) | **2026-12-04** |  | rbi.org.in press release 2026-03-23, prid=62422 (fetched 2026-10-05): "December 2, 3 and 4, 2026" |
| argentina | Semiannual interest/amortisation date on Argentina's 2020 restructured USD/EUR Globales (2029/30/35/38/41/46); 2027-01-09 is a Saturday, so cash moves the next business day | **2027-01-09** |  | Republic of Argentina prospectus supplement, SEC 424B5 acc. 0001193125-20-221606 (fetched 2026-10-05): "pay interest ... semi-annually in arrears on January 9 and July 9 of each year" |
| macro | BLS CPI release (September 2026 data), 8:30 a.m. ET | **2026-10-14** |  | bls.gov/schedule/news_release/cpi.htm (fetched 2026-10-05): Oct. 14, 2026 08:30 AM |
| macro | BLS CPI release (October 2026 data), 8:30 a.m. ET | **2026-11-10** |  | bls.gov/schedule/news_release/cpi.htm (fetched 2026-10-05): Nov. 10, 2026 08:30 AM |

**Catalyst floor:** every fund in a theme marked above scores catalyst >= 7 this run (issuer-confirmed, theme-specific, within 30 days). Judgment may lift it to 8-10, never below; only 'CONTRADICTED: <source>' overrides. check_memo.py fails a lower score.

A panelist that cannot re-find one of these writes "carried forward, not re-searched" and keeps
the band the date earns. It does not score the theme down for having no dated trigger, and never
calls it "unverified": only a cited source that CONTRADICTS the date overturns it (write
"CONTRADICTED: <source>"; the verifier then marks the ledger row RETRACTED). check_memo.py fails
a ballot that doubts a live row without one.
