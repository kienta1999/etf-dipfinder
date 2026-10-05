# ETF dip-pick dossier — 2026-10-05 (asof 2026-10-02, Friday close; ALWAYS-FULL run)

## A. Candidates — full CSV rows
Column legend: ticker, theme, asof, days(lookback), price, dd_52w (drawdown vs 52w high), dd_pctile (drawdown percentile vs own 3y history), dd_z, vs_sma200, vs_sma50, rs_spy_3m/6m/12m (relative strength vs SPY), ret_10d, vol_60d, dollar_vol ($), tp_pct (take-profit %), sl_pct (stop-loss %), dip_low_pct, rr (reward/risk), size_1pct, is_dip, stabilizing, dip_score (depth), price_score (computed 1-10), theme_score, is_candidate.

|  | theme | asof | days | price | dd_52w | dd_pctile | dd_z | vs_sma200 | vs_sma50 | rs_spy_3m | rs_spy_6m | rs_spy_12m | ret_10d | vol_60d | dollar_vol | tp_pct | sl_pct | dip_low_pct | rr | size_1pct | is_dip | stabilizing | dip_score | price_score | theme_score | is_candidate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REMX | rare-earth | 2026-10-02 | 753.0000 | 63.2100 | -0.4229 | 0.0068 | -1.0678 | -0.2639 | -0.1254 | -0.2863 | -0.4685 | -0.2169 | -0.0847 | 0.3960 | 40259228.8711 | 0.7328 | -0.1715 | -0.0041 | 4.2732 | 0.0583 | True | False | 0.0756 | 6 | 0.0756 | True |
| TAN | solar | 2026-10-02 | 753.0000 | 44.0500 | -0.4042 | 0.0313 | -1.1443 | -0.1973 | -0.0878 | -0.2614 | -0.3764 | -0.1867 | -0.0353 | 0.3532 | 33263639.3685 | 0.6783 | -0.1529 | -0.0238 | 4.4351 | 0.0654 | True | False | 0.0885 | 5 | 0.0885 | True |
| KWEB | china | 2026-10-02 | 753.0000 | 23.8600 | -0.4105 | 0.0027 | -1.7528 | -0.1806 | -0.0890 | -0.0946 | -0.3301 | -0.5673 | -0.0391 | 0.2342 | 368479190.6368 | 0.6963 | -0.1014 | -0.0096 | 6.8667 | 0.0986 | True | False | 0.0887 | 5 | 0.0887 | True |
| FXI | china | 2026-10-02 | 753.0000 | 33.1900 | -0.1904 | 0.0286 | -1.1192 | -0.0798 | -0.0553 | -0.0054 | -0.2391 | -0.3469 | -0.0329 | 0.1701 | 628697198.8709 | 0.2351 | -0.0737 | -0.0482 | 3.1924 | 0.1358 | True | False | 0.2854 | 5 | 0.0887 | True |
| URNM | nuclear | 2026-10-02 | 753.0000 | 47.4200 | -0.4354 | 0.0218 | -0.9704 | -0.2145 | -0.1062 | -0.1416 | -0.4316 | -0.3419 | -0.0576 | 0.4487 | 25705307.6966 | 0.7712 | -0.1943 | -0.0061 | 3.9692 | 0.0515 | True | False | 0.1009 | 5 | 0.1009 | True |
| NLR | nuclear | 2026-10-02 | 753.0000 | 102.7400 | -0.3749 | 0.0027 | -0.9335 | -0.2038 | -0.0940 | -0.1452 | -0.4109 | -0.3980 | -0.0460 | 0.4017 | 39866963.0409 | 0.5999 | -0.1739 | -0.0004 | 3.4490 | 0.0575 | True | False | 0.1387 | 5 | 0.1009 | True |
| URA | nuclear | 2026-10-02 | 753.0000 | 39.7900 | -0.3563 | 0.0163 | -0.8068 | -0.1722 | -0.0799 | -0.1202 | -0.3658 | -0.3000 | -0.0447 | 0.4415 | 123574970.6233 | 0.5534 | -0.1912 | -0.0570 | 2.8945 | 0.0523 | True | False | 0.2271 | 6 | 0.1009 | True |
| SLV | silver | 2026-10-02 | 753.0000 | 54.7400 | -0.4816 | 0.0395 | -1.2532 | -0.1695 | -0.0520 | -0.0514 | -0.3474 | 0.1119 | -0.0866 | 0.3843 | 897374624.2760 | 0.9291 | -0.1664 | -0.0795 | 5.5830 | 0.0601 | True | False | 0.1141 | 7 | 0.1141 | True |
| SHLD | defense-us | 2026-10-02 | 753.0000 | 60.2300 | -0.2255 | 0.0163 | -1.1165 | -0.1125 | -0.0686 | -0.0981 | -0.3625 | -0.3002 | -0.0391 | 0.2020 | 104678680.1771 | 0.2912 | -0.0875 | -0.0368 | 3.3293 | 0.1143 | True | False | 0.1522 | 6 | 0.1522 | True |
| XAR | defense-us | 2026-10-02 | 753.0000 | 233.0900 | -0.2140 | 0.0041 | -0.8469 | -0.1280 | -0.1058 | -0.2220 | -0.2809 | -0.1766 | -0.0277 | 0.2528 | 75119990.0866 | 0.2723 | -0.1094 | -0.0079 | 2.4884 | 0.0914 | True | False | 0.2652 | 6 | 0.1522 | True |
| ITA | defense-us | 2026-10-02 | 753.0000 | 207.7900 | -0.1785 | 0.0027 | -0.8875 | -0.0968 | -0.0990 | -0.1974 | -0.2414 | -0.1683 | -0.0283 | 0.2011 | 183450344.9230 | 0.2172 | -0.0871 | -0.0029 | 2.4948 | 0.1148 | True | False | 0.3033 | 6 | 0.1522 | True |
| PPA | defense-us | 2026-10-02 | 753.0000 | 155.6900 | -0.1577 | 0.0041 | -0.8338 | -0.0883 | -0.0798 | -0.1710 | -0.2585 | -0.1600 | -0.0227 | 0.1891 | 46530875.4243 | 0.1872 | -0.0819 | -0.0069 | 2.2861 | 0.1221 | True | False | 0.3226 | 6 | 0.1522 | True |
| UFO | space | 2026-10-02 | 753.0000 | 43.1300 | -0.3631 | 0.0191 | -1.3316 | -0.0885 | -0.0333 | -0.1696 | -0.3011 | 0.0313 | -0.0018 | 0.2726 | 8165913.2075 | 0.5700 | -0.1181 | -0.0274 | 4.8282 | 0.0847 | True | False | 0.1652 | 8 | 0.1652 | True |
| ARKX | space | 2026-10-02 | 753.0000 | 32.6800 | -0.1341 | 0.1349 | -0.5130 | 0.0069 | 0.0066 | -0.0678 | -0.1016 | -0.0326 | 0.0174 | 0.2614 | 13867208.4210 | 0.1548 | -0.1132 | -0.0967 | 1.3681 | 0.0884 | True | True | 0.7915 | 6 | 0.1652 | True |
| XLU | utilities | 2026-10-02 | 753.0000 | 39.8300 | -0.1481 | 0.0109 | -1.0733 | -0.0904 | -0.0612 | -0.1413 | -0.3081 | -0.2333 | -0.0238 | 0.1380 | 1197847882.8165 | 0.1738 | -0.0597 | -0.0146 | 2.9097 | 0.1674 | True | False | 0.1965 | 6 | 0.1965 | True |
| PBW | clean | 2026-10-02 | 753.0000 | 29.5200 | -0.3624 | 0.0695 | -0.9642 | -0.1392 | -0.0686 | -0.2331 | -0.2362 | -0.1780 | -0.0275 | 0.3759 | 9750001.5312 | 0.5684 | -0.1628 | -0.0186 | 3.4923 | 0.0614 | True | False | 0.2525 | 4 | 0.2525 | True |
| ICLN | clean | 2026-10-02 | 753.0000 | 17.1900 | -0.2743 | 0.0123 | -0.9988 | -0.0851 | -0.0268 | -0.1726 | -0.2246 | -0.0700 | -0.0211 | 0.2746 | 117689298.5018 | 0.3779 | -0.1189 | -0.0221 | 3.1784 | 0.0841 | True | False | 0.3102 | 7 | 0.2525 | True |
| GLD | gold | 2026-10-02 | 753.0000 | 380.1400 | -0.2334 | 0.0436 | -0.9393 | -0.0865 | -0.0408 | -0.0322 | -0.2942 | -0.0961 | -0.0524 | 0.2485 | 3447219397.0624 | 0.3045 | -0.1076 | -0.0399 | 2.8297 | 0.0929 | True | False | 0.2661 | 6 | 0.2661 | True |
| IGF | grid/infra | 2026-10-02 | 753.0000 | 61.7600 | -0.0972 | 0.0041 | -1.1600 | -0.0526 | -0.0469 | -0.1056 | -0.2541 | -0.1258 | -0.0223 | 0.0838 | 60955618.5234 | 0.1076 | -0.0363 | -0.0073 | 2.9672 | 0.2757 | True | False | 0.2989 | 7 | 0.2989 | True |
| PAVE | grid/infra | 2026-10-02 | 753.0000 | 53.8800 | -0.1003 | 0.1240 | -0.5806 | -0.0076 | -0.0288 | -0.0953 | -0.1273 | -0.0225 | 0.0174 | 0.1727 | 76164496.0209 | 0.1115 | -0.0748 | -0.0256 | 1.4904 | 0.1337 | True | True | 0.7094 | 6 | 0.2989 | True |
| LIT | lithium | 2026-10-02 | 753.0000 | 69.2800 | -0.2406 | 0.1540 | -0.9542 | -0.0717 | -0.0406 | -0.1174 | -0.2414 | 0.0481 | -0.0173 | 0.2521 | 9568370.7831 | 0.3168 | -0.1092 | -0.0367 | 2.9018 | 0.0916 | True | False | 0.3425 | 5 | 0.3425 | True |
| ARGT | argentina | 2026-10-02 | 753.0000 | 84.5200 | -0.1760 | 0.0545 | -0.8086 | -0.0845 | -0.0890 | -0.1277 | -0.2760 | 0.1015 | -0.0856 | 0.2176 | 12033697.6639 | 0.2135 | -0.0942 | -0.0021 | 2.2661 | 0.1061 | True | False | 0.3481 | 6 | 0.3481 | True |
| ITB | housing | 2026-10-02 | 753.0000 | 86.6400 | -0.2279 | 0.1540 | -0.8202 | -0.1016 | -0.0727 | -0.1646 | -0.2098 | -0.3516 | -0.0088 | 0.2779 | 203927166.6414 | 0.2952 | -0.1203 | -0.0147 | 2.4533 | 0.0831 | True | False | 0.3661 | 2 | 0.3661 | True |
| XHB | housing | 2026-10-02 | 753.0000 | 96.7000 | -0.1952 | 0.1281 | -0.7894 | -0.0824 | -0.0585 | -0.1532 | -0.1880 | -0.2868 | 0.0088 | 0.2472 | 190145010.9600 | 0.2425 | -0.1070 | -0.0259 | 2.2651 | 0.0934 | True | True | 0.4551 | 5 | 0.3661 | True |
| INDA | india | 2026-10-02 | 753.0000 | 46.5200 | -0.1586 | 0.0409 | -1.2841 | -0.0668 | -0.0504 | -0.0943 | -0.1823 | -0.2758 | -0.0312 | 0.1235 | 242233358.8932 | 0.1885 | -0.0535 | -0.0236 | 3.5246 | 0.1870 | True | False | 0.3742 | 5 | 0.3742 | True |

## B. Leaders (rs_spy_3m) — regime read

| theme | rs_spy_3m | rs_spy_6m | dd_52w |
|---|---|---|---|
| crypto-spot (ETHA) | 0.457 | 0.107 | -0.438 |
| oil/gas (USO) | 0.385 | -0.111 | -0.090 |
| crypto-spot (IBIT) | 0.294 | 0.078 | -0.330 |
| biotech (ARKG) | 0.212 | 0.794 | -0.004 |
| software (SKYY) | 0.195 | 0.324 | -0.005 |
| software (WCLD) | 0.182 | 0.305 | -0.044 |
| oil/gas (XOP) | 0.179 | -0.130 | -0.070 |
| energy (XLE) | 0.162 | -0.105 | -0.042 |
# dossier.md section C + D — quick-pass memo (UNVERIFIED — challenge it)

## C. Quick-pass memo (per-theme, one search each, 2026-10-05) — *unverified — challenge it*

- **rare-earth (REMX)**: **rotation** — sector selloff after Sep 24 Trump-Xi summit raised hopes of a thaw; MP Materials -15.8% in 30 days despite constructive company news (Gd oxide supply deal, GM magnet deliveries, Q4 commercial magnet shipments). China rare-earth export-control suspension (MOFCOM No. 70) expires 2026-11-10 — the real forcing function (stockmoguls 9/22; tickeron).
- **solar (TAN)**: **break-ish → unclear leaning break** — rates + policy double hit: 10y at ~5.2%, Fed's Sep 16 hike (first in 3+ years), Trump's big tax bill cut project subsidies, permitting slowed. TAN -10% in a month/-23% in 6m. Carried-forward Solar IV final determinations 10/14 and 11/2 are the dated catalysts (barrons; ainvest 9/18).
- **china (KWEB, FXI)**: **rotation** — HK reopened after holiday Oct 2 with -3% (biggest drop since March); new stimulus underwhelmed (only backstops the 4.5-5% growth target), 10y at 5.25-5.34% tightening conditions through the HKD peg, mainland closed until Oct 8. Financials/tech led down (XTB; Reuters 10/5).
- **nuclear (URNM, NLR, URA)**: **rotation** — uranium at $96/lb (19y high) but stocks -35%+ off highs: utilities won't sign at these prices, Oklo lost its PJM interconnection fight (FERC), Holtec pulled its ~$10B IPO, SMR debutantes (X-Energy -37% from IPO) showed valuation fatigue. Cameco Q3 on 10/30 carried forward (oilprice; pluang 10/3).
- **silver (SLV)**: **rotation** — bond-yield selloff (10y at 5.34%, highest since 2002) crushed non-yielding metals; silver -10% in 5 days to ~$60, down ~25% from Jan record $5,608 spot gold context; SLV 48% off its high. Underlying: record central-bank gold buying, China silver-export tightening in January (Reuters 9/28; ad-hoc-news 10/3).
- **defense-us (SHLD, XAR, ITA, PPA)**: **rotation** — sector fell out of favor: elevated bond yields, LMT F/A-XX fighter loss to Boeing ($20B Navy contract), Trump jawboning about buybacks/dividends (then $1.5T budget talk). RTX/LMT Q3 on 10/20 and 10/22 carried forward; backlog thesis intact (zerohedge 9/18; WSJ 9/30).
- **space (UFO, ARKX)**: **rotation** — post-SpaceX-IPO hangover: UFO -40% from its $68 52w high after the $1.8T IPO pulled attention to SPCX; Blue Origin New Glenn explosion; space names mostly unprofitable, high-beta. ARKX (stabilizing, +1.7% ret_10d) held better (tipranks 6/2026; ainvest 9/18).
- **utilities (XLU)**: **rotation** — classic rate trade: XLU -8.3% in 11 sessions, -6% in September, 10y >5.2% makes the 3.04% dividend yield uncompetitive; but Oct 2 saw TLT's best intraday rally in a month and XLU put-selling bets on bottoming (CNBC 10/2; spotgamma 10/4).
- **clean (PBW, ICLN)**: **rotation** — same rate hit as solar/utilities, plus margin squeeze; ICLN only -27% off high vs PBW -36%. Vestas Q3 on 11/11 carried forward (oilprice; ainvest).
- **gold (GLD)**: **rotation** — 10y at 5.34% + firm dollar + Iran ceasefire rejection → gold ended week at $4,144 (-3.4% w/w, -25% from Jan $5,608 record); Sep payrolls only 29k cooled Oct-hike odds to ~14%, support at $4,000. Record Q2 central-bank buying (288.9t) the counterweight (Reuters 9/28; tradingnews 10/1).
- **grid/infra (IGF, PAVE)**: **rotation** — IGF -9.7% off high mostly rate-driven; PAVE stabilizing (+1.7% ret_10d). Surface Transportation Extension Act lapse date 12/11 carried forward (search; multibagg 10/1).
- **lithium (LIT)**: **unclear leaning break** — China lithium carbonate -22.5% in September to 122,800 yuan/t after a pricing-method change doubled reported stockpiles to 175,000t; Macquarie cut targets across the sector; Albemarle Q3 on 11/4 carried forward (geomechanics 10/5; thebull 10/3).
- **argentina (ARGT)**: **rotation** — broad EM/risk-off: FII-style outflows on Milei reform uncertainty, US support still the backstop. Dated catalyst: none confirmed; **unclear** (reuters 2025-10; cnn 2025-10).
- **housing (ITB, XHB)**: **rotation** — 30y mortgage 7.28% (Oct 1, biggest weekly jump in 4 years), ITB -9.9% in a month; but Berkshire bought $53.9M more Lennar in late Sept (now 11%) and owns Taylor Morrison. D.R. Horton Q4 10/29 carried forward (tradersunion 10/1; fool 10/4).
- **india (INDA)**: **rotation** — Nifty 8 straight weekly losses (longest in 25y); record FII outflows ($27.8B YTD), USD 10y >5.3%, rupee weakness; HDFC Bank board 10/17 and RBI MPC decision 10/7 carried forward (thehindubusinessline 10/1; dsij).

Regime read: leaders are ETHA/crypto, USO/oil-gas, ARKG biotech, SKYY/WCLD software — money is in crypto, energy, software; dips cluster in rate-sensitive (utilities, housing, solar, clean, grid) + geopolitical rotation (nuclear, rare-earth, defense, china, india). The unifying macro variable is the 10y at ~5.3% and Fed Oct-28 hike odds.

## D. Confirmed catalysts carried forward — already verified, do NOT rescore as 'not found'

(paste of scripts/carry_forward.py output below)
## D. Confirmed catalysts carried forward — already verified, do NOT rescore as 'not found'

| theme | event | date | confirmed by |
|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 and 2026-10-01 (BusinessWire 20260730139928: "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026"); re-verified 2026-10-04 on SEC EDGAR 6-K ex-99.1 (Cameco Q2 release 2026-07-31, acc. 0001193125-26-326768), same sentence |
| macro | FOMC decision (Oct 27-28 meeting, statement on second day) | **2026-10-28** | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: October 27-28) |
| macro | FOMC decision (Dec 8-9 meeting, statement on second day) | **2026-12-09** | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: December 8-9, SEP meeting) |
| ai/robot | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | **2027-03-14** | nvidia.com GTC FAQ |
| solar | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | **2026-10-14** | Reuters/SRN 2026-09-11; SMM; Sxcoal; re-verified 2026-09-29 (solarpowerworld 9/20, Sxcoal 9/14, pv-magazine) and 2026-10-01 (pv-tech.org 9/15: "Commission is scheduled to make its final determination on 14 October 2026") |
| solar | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | **2026-11-02** | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 (Sxcoal, pv-magazine, taiyangnews) and 2026-10-01 (pv-tech.org 9/15: "final AD/CVD duty orders, currently scheduled for 2 November 2026") |
| housing | D.R. Horton Q4/FY26 results, before market open, 8:30 a.m. ET call | **2026-10-29** | D.R. Horton investor site press release, 2026-09-10 (BusinessWire): "will release financial results for its fourth quarter and fiscal year ended September 30, 2026 on Thursday, October 29, 2026 before the market opens" |
| lithium | Albemarle Q3 2026 results, after NYSE close; earnings call Nov 5, 8:00 a.m. EST | **2026-11-04** | Albemarle PR Newswire, 2026-10-01: "will release its third quarter 2026 earnings after the NYSE closes on Wednesday, November 4, 2026" |
| utilities | Southern Company Q3 2026 earnings released by 7:30 a.m. ET; analyst call 1 p.m. ET | **2026-11-05** | southerncompany.mediaroom.com press release 2026-09-25 (fetched): "plans to release its earnings for the third quarter of 2026 by 7:30 a.m. ET on Thursday, November 5, 2026"; Southern is XLU's #2 holding at 7.69% (SSGA, 2026-10-01) |
| defense-us | RTX Q3 2026 results before market open; 8:30 a.m. ET call | **2026-10-20** | rtx.com news release 2026-09-29 (PRNewswire, fetched): "will issue its third quarter 2026 earnings results on Tuesday, October 20, prior to the stock market opening" |
| defense-us | Lockheed Martin Q3 2026 results before market open; 8:30 a.m. ET webcast | **2026-10-22** | news.lockheedmartin.com release dated 2026-10-01 (fetched; also at investors.lockheedmartin.com): call "Thursday, Oct. 22, 2026, at 8:30 a.m. ET", results published prior to market opening |
| defense-us | Howmet Aerospace Q3 2026 results ~7:00 a.m. ET, webcast 10:00 a.m. ET (also a PAVE holding) | **2026-10-29** | howmet.com press release 2026-10-01 (fetched): "Thursday, October 29, 2026. The press release and presentation materials will be available at approximately 7:00 AM ET" |
| defense-us | FY27 continuing resolution (Division A of P.L. 119-103) expires: appropriations cliff, outcome cuts both ways | **2026-12-11** | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. A sec. 106(3): funds available until "December 11, 2026"; CRS R49353 (2026-09-17) |
| grid/infra | Surface Transportation Extension Act of 2026 (Division C of P.L. 119-103) ends: IIJA highway/transit authorities lapse unless reauthorized or re-extended | **2026-12-11** | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. C: "extension end date means December 11, 2026", extension period from 2026-10-01 |
| clean | Vestas Q3 2026 interim report (quiet period from 2026-10-10) | **2026-11-11** | vestas.com/en/investor/Calendar-Events (fetched 2026-10-04): "Disclosure of Q3 2026 interim report", 11 November 2026 |
| india | HDFC Bank board meeting to approve results for the quarter ended 2026-09-30 (Q2 FY27) | **2026-10-17** | HDFC Bank Form 6-K filed 2026-09-22 (SEC acc. 0001193125-26-397434, text read via stocktitan): board meets 2026-10-17 to approve unaudited standalone and consolidated results; trading window closed 9/24-10/19 |
| india | RBI MPC policy decision (Oct 5-7 meeting, decision on the last day); next meeting Dec 2-4 | **2026-10-07** | rbi.org.in press release 2026-03-23 "Meeting Schedule of the Monetary Policy Committee for 2026-2027" (prid=62422, fetched): October 5-7, 2026 |
| china | APEC Economic Leaders' Meeting, Shenzhen, Nov 18-19 (CEO Summit Nov 17-18) | **2026-11-18** | Shenzhen Government Online (sz.gov.cn) 2026-09-10 (fetched): Economic Leaders' Meeting "Nov. 18 to 19"; Xi announced Shenzhen host 2025-11 (cppcc.gov.cn) |

A panelist that cannot re-find one of these writes "carried forward, not re-searched" and keeps
the band the date earns. It does not score the theme down for having no dated trigger, and never
calls it "unverified": only a cited source that CONTRADICTS the date overturns it (write
"CONTRADICTED: <source>"; the verifier then marks the ledger row RETRACTED). check_memo.py fails
a ballot that doubts a live row without one.

### Disputed — sources contradict each other; neither date is confirmed

| theme | claim | readings | sources |
|---|---|---|---|
| rare-earth | China's suspension of its Oct-2025 rare-earth export controls (MOFCOM Announcement No. 70) | (a) expires 2026-11-10 with automatic snapback — MOFCOM No. 70 text (2025-11-07, pre-summit), per Sphera and pre-summit SilmarilMedia; (b) the rare-earth export-control pause was extended with the truce to 2027-01-10 — Bessent confirmed post-9/24-summit (The Global Market Brief 9/26; chomcho; tamaranews 9/26). Some outlets (FXStreet, InvestedAlpha) report no *new* firm rare-earth commitments. No MOFCOM text seen on either side | (a) MOFCOM No. 70 text; (b) Bessent via The Global Market Brief 9/26, chomcho, tamaranews 9/26; post-summit: Bessent Fox News 9/24 announced the Nov-10 → 2027-01-10 extension (WSJ headline via killbait; tokenpost; roic; pressinsider — which notes Beijing did not separately announce the date); silmarilmedia 9/29: "a 61-day reprieve with no binding commitments on rare earth supply volumes, no resolution of the April 2025 licensing architecture"; neuralwired 9/26: extension "preserves China's suspension of rare earth export controls". Still no MOFCOM text on either side — stays Disputed. 2026-10-04 verifier: a mofcom.gov.cn search finds only No. 70 itself (suspension "至2026年11月10日") and the MOFCOM Americas-dept readout of 2026-05-20 (measures suspended to 2026-11-10, extension planned but undated). No MOFCOM text for 2027-01-10 — still Disputed |

A catalyst score of 7+ that rests on a disputed date must cite a primary source (the issuing
ministry / agency / company) that settles it; otherwise score only what holds under both readings.

