> Run by: Opus 5.5 (claude-opus-5-5) — full panel

# Dossier — etf-dip-pick 2026-10-21-r5

Scan as of 2026-10-21 close. 106 funds scanned (BJK no data; 12 illiquid dropped), 60 dips, 41 candidates in the top 20 themes.
Panelists: score from THIS dossier and the web only. Do not open any other run's files (other `log/` memos, other `output/` folders, SESSIONS.md).

## A. Candidates — full scan rows

Column legend: `price` last close · `dd_52w` drawdown from 52-week high · `dd_pctile` how deep today's drawdown is vs this ETF's own 3y history (<0.10 = rare) ·
`dd_z` drawdown ÷ vol · `vs_sma200` / `vs_sma50` distance from the moving average · `rs_spy_3m/6m/12m` return minus SPY's over the window ·
`ret_10d` 10-day return · `vol_60d` annualised 60-day vol · `dollar_vol` avg daily $ volume · `tp_pct` take-profit = back to the 52w high ·
`sl_pct` stop · `dip_low_pct` distance from the dip low · `rr` = TP ÷ (1.5 monthly σ); < 1.3 = thin · `size_1pct` position size risking 1% ·
`stabilizing` = ret_10d > 0 · `dip_score` depth rank (0 = most beaten up; depth, NOT quality) · `price_score` the computed price lens (1-10) ·
`theme_score` the theme's best dip_score (themes ranked by it).

```csv
,theme,price,dd_52w,dd_pctile,dd_z,vs_sma200,vs_sma50,rs_spy_3m,rs_spy_6m,rs_spy_12m,ret_10d,vol_60d,dollar_vol,tp_pct,sl_pct,dip_low_pct,rr,size_1pct,stabilizing,dip_score,price_score,theme_score
REMX,rare-earth,53.370,-0.513,0.003,-1.416,-0.371,-0.227,-0.282,-0.578,-0.414,-0.138,0.362,50235885.544,1.052,-0.157,-0.000,6.713,0.064,False,0.028,5,0.028
URNM,nuclear,43.730,-0.479,0.011,-1.065,-0.267,-0.151,-0.193,-0.480,-0.401,-0.086,0.450,33691475.075,0.921,-0.195,-0.030,4.725,0.051,False,0.089,5,0.089
NLR,nuclear,94.310,-0.426,0.004,-1.045,-0.259,-0.144,-0.203,-0.456,-0.525,-0.104,0.408,44922427.573,0.743,-0.177,-0.012,4.206,0.057,False,0.117,5,0.089
URA,nuclear,35.550,-0.425,0.007,-0.970,-0.254,-0.158,-0.186,-0.477,-0.467,-0.110,0.438,146269503.344,0.739,-0.190,-0.010,3.894,0.053,False,0.139,5,0.089
SLV,silver,52.260,-0.505,0.021,-1.313,-0.198,-0.089,-0.046,-0.350,-0.069,-0.029,0.385,857265579.291,1.021,-0.167,-0.039,6.126,0.060,False,0.106,6,0.106
PBW,clean,25.570,-0.448,0.005,-1.216,-0.249,-0.155,-0.273,-0.402,-0.398,-0.116,0.368,11159375.917,0.811,-0.160,-0.022,5.083,0.063,False,0.112,5,0.112
ICLN,clean,16.500,-0.303,0.005,-1.244,-0.123,-0.052,-0.152,-0.259,-0.160,-0.047,0.244,94703807.638,0.435,-0.106,-0.015,4.125,0.095,False,0.207,6,0.112
QCLN,clean,45.400,-0.337,0.014,-0.967,-0.135,-0.070,-0.170,-0.284,-0.184,-0.082,0.348,5416925.157,0.508,-0.151,-0.042,3.368,0.066,False,0.246,6,0.112
TAN,solar,42.560,-0.424,0.015,-1.281,-0.218,-0.079,-0.245,-0.346,-0.263,-0.022,0.331,39806516.344,0.737,-0.143,-0.029,5.139,0.070,False,0.117,6,0.117
KWEB,china,23.740,-0.391,0.027,-1.726,-0.166,-0.059,-0.146,-0.280,-0.540,-0.024,0.227,424183377.619,0.642,-0.098,-0.005,6.543,0.102,False,0.134,4,0.134
FXI,china,32.940,-0.186,0.033,-1.112,-0.079,-0.047,-0.094,-0.195,-0.336,-0.014,0.168,628475926.607,0.229,-0.072,-0.041,3.155,0.138,False,0.325,5,0.134
UFO,space,40.640,-0.400,0.008,-1.454,-0.144,-0.066,-0.120,-0.343,-0.113,-0.056,0.275,12920401.554,0.666,-0.119,-0.034,5.595,0.084,False,0.140,7,0.140
ARKX,space,30.550,-0.191,0.027,-0.733,-0.063,-0.054,-0.062,-0.188,-0.170,-0.064,0.260,17558264.357,0.235,-0.113,-0.034,2.091,0.089,False,0.458,5,0.140
LIT,lithium,63.200,-0.307,0.012,-1.309,-0.155,-0.114,-0.134,-0.344,-0.060,-0.091,0.235,11218015.740,0.444,-0.102,0.000,4.362,0.098,False,0.146,7,0.146
XAR,defense-us,222.640,-0.249,0.004,-1.027,-0.163,-0.101,-0.227,-0.248,-0.240,-0.018,0.243,93413963.953,0.332,-0.105,-0.010,3.159,0.095,False,0.229,6,0.229
SHLD,defense-us,61.600,-0.208,0.051,-1.047,-0.088,-0.026,-0.068,-0.213,-0.240,0.049,0.199,68187354.482,0.263,-0.086,-0.058,3.052,0.116,True,0.296,6,0.229
ITA,defense-us,205.790,-0.186,0.007,-0.993,-0.103,-0.066,-0.185,-0.152,-0.180,0.011,0.188,175375779.410,0.229,-0.081,-0.011,2.819,0.123,True,0.374,8,0.229
PPA,defense-us,155.820,-0.157,0.018,-0.858,-0.087,-0.044,-0.153,-0.170,-0.155,0.019,0.183,51781416.954,0.186,-0.079,-0.019,2.352,0.126,True,0.408,8,0.229
WGMI,crypto-equity,32.430,-0.550,0.030,-0.647,-0.334,-0.265,-0.493,-0.445,-0.622,-0.245,0.850,29182832.635,1.223,-0.368,-0.035,3.324,0.027,False,0.239,4,0.239
BKCH,crypto-equity,58.430,-0.466,0.094,-0.648,-0.181,-0.149,-0.233,-0.332,-0.630,-0.127,0.719,5528561.115,0.872,-0.311,-0.113,2.804,0.032,False,0.306,3,0.239
BLOK,crypto-equity,56.430,-0.219,0.117,-0.552,-0.057,-0.083,-0.140,-0.172,-0.369,-0.065,0.397,16883536.984,0.280,-0.172,-0.162,1.631,0.058,False,0.620,2,0.239
GLD,gold,378.950,-0.236,0.048,-0.993,-0.086,-0.043,-0.030,-0.222,-0.224,0.008,0.237,2912590573.435,0.309,-0.103,-0.037,3.002,0.097,True,0.319,7,0.319
ITB,housing,86.570,-0.229,0.166,-0.806,-0.095,-0.042,-0.127,-0.216,-0.319,0.022,0.283,274281418.182,0.296,-0.123,-0.037,2.413,0.082,True,0.335,5,0.335
XHB,housing,95.600,-0.204,0.115,-0.803,-0.088,-0.039,-0.149,-0.208,-0.273,0.007,0.255,193890390.264,0.257,-0.110,-0.029,2.330,0.091,True,0.363,5,0.335
XME,base-metals,101.290,-0.236,0.019,-0.664,-0.109,-0.088,-0.068,-0.260,-0.217,-0.034,0.356,158468052.978,0.310,-0.154,-0.037,2.007,0.065,False,0.351,6,0.351
PICK,base-metals,57.480,-0.159,0.187,-0.614,-0.048,-0.075,-0.059,-0.177,0.107,-0.037,0.259,37374437.883,0.189,-0.112,-0.029,1.685,0.089,False,0.587,5,0.351
COPX,base-metals,78.020,-0.191,0.236,-0.501,-0.065,-0.106,-0.054,-0.170,0.122,-0.067,0.382,173558329.673,0.236,-0.165,0.000,1.429,0.060,False,0.619,5,0.351
BOTZ,ai/robot,33.590,-0.193,0.026,-0.860,-0.086,-0.052,-0.071,-0.193,-0.253,-0.058,0.224,20471568.521,0.239,-0.097,-0.017,2.461,0.103,False,0.380,5,0.380
AIPO,ai/robot,26.020,-0.252,0.014,-0.663,-0.087,-0.087,-0.196,-0.230,-0.099,-0.114,0.380,42627928.240,0.336,-0.164,-0.022,2.046,0.061,False,0.402,7,0.380
ARKQ,ai/robot,115.850,-0.195,0.049,-0.665,-0.071,-0.054,-0.059,-0.208,-0.188,-0.073,0.292,13554924.472,0.241,-0.127,-0.054,1.906,0.079,False,0.453,5,0.380
ROBO,ai/robot,77.550,-0.142,0.051,-0.586,-0.018,-0.034,-0.060,-0.117,-0.031,-0.052,0.241,8813657.232,0.165,-0.104,-0.029,1.578,0.096,False,0.710,5,0.380
BAI,ai/robot,42.890,-0.209,0.091,-0.491,0.021,-0.054,-0.100,-0.061,0.080,-0.130,0.426,162673925.043,0.264,-0.185,-0.126,1.432,0.054,False,0.927,6,0.380
QTUM,ai/robot,141.790,-0.156,0.040,-0.496,0.039,-0.048,-0.059,0.001,0.127,-0.082,0.314,50472118.493,0.185,-0.136,-0.070,1.356,0.073,False,0.939,7,0.380
DTCR,reit,25.610,-0.208,0.007,-0.803,-0.064,-0.077,-0.144,-0.178,-0.001,-0.075,0.259,22631983.411,0.263,-0.112,0.000,2.341,0.089,False,0.447,7,0.447
VNQ,reit,91.490,-0.086,0.100,-0.701,-0.017,-0.021,-0.115,-0.108,-0.133,0.032,0.122,435802210.017,0.094,-0.053,-0.031,1.771,0.189,True,0.643,7,0.447
VNM,vietnam,16.980,-0.142,0.179,-0.667,-0.058,-0.020,-0.031,-0.217,-0.229,0.006,0.213,6328665.039,0.166,-0.092,-0.038,1.796,0.108,True,0.459,5,0.459
INDA,india,47.270,-0.145,0.087,-1.102,-0.043,-0.020,-0.058,-0.147,-0.300,0.025,0.132,261684667.334,0.170,-0.057,-0.039,2.977,0.175,True,0.465,6,0.465
EUAD,defense-eu,40.670,-0.158,0.077,-0.853,-0.061,-0.059,-0.088,-0.096,-0.245,0.013,0.185,9870758.354,0.187,-0.080,-0.074,2.338,0.125,True,0.542,6,0.542
JETS,transport,26.410,-0.212,0.051,-0.794,-0.071,-0.071,-0.149,-0.072,-0.119,-0.045,0.268,106507691.468,0.270,-0.116,-0.031,2.328,0.086,False,0.575,5,0.575
IYT,transport,79.955,-0.110,0.121,-0.725,-0.016,-0.028,-0.141,-0.092,-0.043,0.013,0.151,74278558.144,0.123,-0.066,-0.018,1.881,0.153,True,0.660,6,0.575
XLU,utilities,42.000,-0.102,0.040,-0.671,-0.040,0.006,-0.134,-0.144,-0.220,0.021,0.151,1481103647.681,0.113,-0.066,-0.066,1.725,0.152,True,0.587,7,0.587
```

No candidate is thin (lowest R/R: QTUM 1.36, COPX 1.43, BAI 1.43).

## B. Leaders (rs_spy_3m) — where the money went

```csv
,theme,rs_spy_3m,rs_spy_6m,rs_spy_12m,dd_52w
WCLD,software,0.371,0.494,0.113,0.000
ETHA,crypto-spot,0.283,-0.055,-0.540,-0.408
IBIT,crypto-spot,0.255,-0.024,-0.404,-0.267
SKYY,software,0.235,0.272,0.075,-0.047
ARKG,biotech,0.234,0.522,0.320,-0.122
BUG,cyber,0.210,0.620,0.180,-0.063
IGV,software,0.200,0.134,-0.208,-0.070
HACK,cyber,0.127,0.416,0.246,-0.065
CIBR,cyber,0.126,0.405,0.191,-0.062
EWZ,brazil,0.125,-0.035,0.306,-0.024
ARKF,fin-other,0.123,-0.026,-0.334,-0.203
ARKW,internet/ark,0.111,0.047,-0.226,-0.096
```

Other dips outside the top 20 themes: ARGT PAVE GRID IGF XLI XLC XLRE KBE KBWB IWM EWY OIH PSI XSD DRAM SOXX SMH IAI EEM.

## C. Quick-pass memo — *unverified, challenge it*

One search per theme (21 searches incl. regime). Search coverage of October 2026 was thin for most themes; where no dated
October story was found the provisional bucket rests on the scan shape plus the newest dated item found.

**Regime.** S&P 500 near all-time highs (7,712.57 on 2026-10-20, CNBC; record highs reported 2026-10-07, Al Jazeera). Leadership
is software (WCLD/IGV/SKYY at fresh 2026 highs "as AI disruption worries fade", Reuters via investing.com), cyber, spot crypto
(IBIT/ETHA rs_3m +0.26/+0.28 though still 27-41% off their highs) and biotech (ARKG). Last week saw a rout in AI-infrastructure names on
"anxieties around companies borrowing too much money for their AI build-outs" (CNBC 2026-10-20), partly reversed this week.
The dips are the mirror: hard assets and real-economy cyclicals — rare earths, uranium, silver, gold, base metals, clean/solar,
lithium, defense, homebuilders, transports, utilities, India. Common macro thread in the snippets: firmer dollar, higher US
yields, oil elevated on US-Iran / Strait of Hormuz tensions (one source dates an oil drop on 10-20). Gold -8.5% in September
(WGC: rising yields, stronger dollar) while physically backed gold ETFs still took in $10bn that month. Reading: one rotation
out of the 2025-H1 2026 "real assets / scarcity" trade into software + crypto, not 20 separate problems.

| theme | funds | provisional | one-line basis (newest dated evidence found) |
|---|---|---|---|
| rare-earth | REMX | unclear | NAV 87.01 (Jul 2) → 67.24 (Sep 24) → 53.37 today; top holdings SQM/ALB/MP (lithium-heavy). China export-control suspension extended to 2027-01-10 (section D) removes a scarcity premium; no October story found |
| nuclear | URNM NLR URA | rotation | URA new 52w closing low Oct 16; Jul note: term uranium ~$95/lb up ~7% while spot weak; equities -40%+ from Jan peak — sentiment/flows, not demand |
| silver | SLV | unclear | spot ~$121 peak late Jan → ~$61 Oct 1; parabolic unwind; firm dollar cited. Bubble deflation vs rotation not separable from snippets |
| clean | PBW ICLN QCLN | unclear | ICLN outflows −$108M (Aug), top holding Bloom Energy; no October story. Rides AI-power names + policy |
| solar | TAN | unclear | no October story; policy-driven sector (AD/CVD final orders Nov 2, Sec 232 Dec 4 — section D) |
| china | KWEB FXI | unclear | KWEB $23.86 Oct 2, near 3y low; −22.8% YTD by July with outflows; no October cause found |
| space | UFO ARKX | unclear | SpaceX trading back toward its $135 IPO floor, lockup expiries ahead; funds hold many unprofitable names |
| lithium | LIT | unclear | Aug: GFEX lithium carbonate ~CNY149k/t drifting lower; ALB price targets cut; no October story |
| defense-us | XAR SHLD ITA PPA | unclear | Benzinga: XAR/ITA/PPA six straight weekly losses since Aug 14, −17%/−16%, "not part of a broad market selloff" — sector-specific cause not named in snippet |
| crypto-equity | WGMI BKCH BLOK | unclear | spot crypto leads while miners lag (WGMI rs_3m −0.49); Oct 19 note: WGMI mandate broadened to AI infrastructure, cut to Hold; AI-infra borrowing rout last week |
| gold | GLD | rotation | −8.5% in Sept on yields/dollar (WGC), >20% below Jan 28 peak by early Oct, yet $10bn ETF inflows in Sept |
| housing | ITB XHB | rotation | rate-sensitive; no October story; mortgage ~6.0% low earlier in 2026 (date unclear) |
| base-metals | XME PICK COPX | unclear | no October story found |
| ai/robot | BOTZ AIPO ARKQ ROBO BAI QTUM | rotation | AI-infra debt-anxiety rout last week, rebound this week (CNBC 10-20); BOTZ beta 1.79 |
| reit | DTCR VNQ | unclear (DTCR) / rotation (VNQ) | DTCR: AI data-center capex/borrowing fears (Aug: IREN impairment hit peers); VNQ: rates |
| vietnam | VNM | rotation | FTSE upgrade to secondary EM effective 2026-09-21, inclusion phased 10% → 30% Mar 2027 (SSI est. $1.4bn passive) — sell-the-news |
| india | INDA | rotation | FPI outflows ₹52,100 cr in October to 10-18, ₹3.12 lakh cr YTD; drivers crude, dollar, US yields, capital pulled to North Asia AI; FPIs net buyers 10-16 |
| defense-eu | EUAD | unclear | no October story; peace-talk headlines were the 2025 driver |
| transport | JETS IYT | rotation | fuel shock sensitivity (oil, Hormuz); UNP (IYT #1) and AAL report Oct 22 |
| utilities | XLU | rotation | defensive money left for software/crypto; Southern Co. Q3 Nov 5 (section D) |

## D. Confirmed catalysts carried forward — already verified, do NOT rescore as 'not found'

| theme | event | date | floor | confirmed by |
|---|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | **catalyst >= 7** | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 and 2026-10-01 (BusinessWire 20260730139928: "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026"); re-verified 2026-10-04 on SEC EDGAR 6-K ex-99.1 (Cameco Q2 release 2026-07-31, acc. 0001193125-26-326768), same sentence; re-verified 2026-10-21 (same 6-K ex-99.1 fetched: "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026") |
| macro | FOMC decision (Oct 27-28 meeting, statement on second day) | **2026-10-28** |  | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: October 27-28); re-verified 2026-10-21 (fomccalendars.htm: October 27-28) |
| macro | FOMC decision (Dec 8-9 meeting, statement on second day) | **2026-12-09** |  | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: December 8-9, SEP meeting); re-verified 2026-10-21 (fomccalendars.htm: December 8-9*, SEP meeting) |
| ai/robot | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | **2027-03-14** |  | nvidia.com GTC FAQ |
| solar | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | **2026-11-02** | **catalyst >= 7** | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 (Sxcoal, pv-magazine, taiyangnews) and 2026-10-01 (pv-tech.org 9/15: "final AD/CVD duty orders, currently scheduled for 2 November 2026") |
| housing | D.R. Horton Q4/FY26 results, before market open, 8:30 a.m. ET call | **2026-10-29** | **catalyst >= 7** | D.R. Horton investor site press release, 2026-09-10 (BusinessWire): "will release financial results for its fourth quarter and fiscal year ended September 30, 2026 on Thursday, October 29, 2026 before the market opens"; re-verified 2026-10-21 on investor.drhorton.com fiscal-2026 release-dates notice dated 10/16/25 (fetched): "Fourth quarter and fiscal year: Thursday, October 29, 2026", before the market opens |
| lithium | Albemarle Q3 2026 results, after NYSE close; earnings call Nov 5, 8:00 a.m. EST | **2026-11-04** | **catalyst >= 7** | Albemarle PR Newswire, 2026-10-01: "will release its third quarter 2026 earnings after the NYSE closes on Wednesday, November 4, 2026" |
| utilities | Southern Company Q3 2026 earnings released by 7:30 a.m. ET; analyst call 1 p.m. ET | **2026-11-05** | **catalyst >= 7** | southerncompany.mediaroom.com press release 2026-09-25 (fetched): "plans to release its earnings for the third quarter of 2026 by 7:30 a.m. ET on Thursday, November 5, 2026"; Southern is XLU's #2 holding at 7.69% (SSGA, 2026-10-01) |
| defense-us | Lockheed Martin Q3 2026 results before market open; 8:30 a.m. ET webcast | **2026-10-22** | **catalyst >= 7** | news.lockheedmartin.com release dated 2026-10-01 (fetched; also at investors.lockheedmartin.com): call "Thursday, Oct. 22, 2026, at 8:30 a.m. ET", results published prior to market opening |
| defense-us | Howmet Aerospace Q3 2026 results ~7:00 a.m. ET, webcast 10:00 a.m. ET (also a PAVE holding) | **2026-10-29** |  | howmet.com press release 2026-10-01 (fetched): "Thursday, October 29, 2026. The press release and presentation materials will be available at approximately 7:00 AM ET" |
| defense-us | FY27 continuing resolution (Division A of P.L. 119-103) expires: appropriations cliff, outcome cuts both ways | **2026-12-11** |  | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. A sec. 106(3): funds available until "December 11, 2026"; CRS R49353 (2026-09-17) |
| grid/infra | Surface Transportation Extension Act of 2026 (Division C of P.L. 119-103) ends: IIJA highway/transit authorities lapse unless reauthorized or re-extended | **2026-12-11** |  | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. C: "extension end date means December 11, 2026", extension period from 2026-10-01 |
| clean | Vestas Q3 2026 interim report (quiet period from 2026-10-10) | **2026-11-11** | **catalyst >= 7** | vestas.com/en/investor/Calendar-Events (fetched 2026-10-04): "Disclosure of Q3 2026 interim report", 11 November 2026 |
| china | APEC Economic Leaders' Meeting, Shenzhen, Nov 18-19 (CEO Summit Nov 17-18) | **2026-11-18** | **catalyst >= 7** | Shenzhen Government Online (sz.gov.cn) 2026-09-10 (fetched): Economic Leaders' Meeting "Nov. 18 to 19"; Xi announced Shenzhen host 2025-11 (cppcc.gov.cn) |
| rare-earth | DFARS 252.225-7052: from 2027-01-01 US defense contractors may not deliver NdFeB/SmCo magnets (or tantalum/tungsten) mined, refined, separated, melted or produced in China, Russia, Iran or North Korea; full supply chain for magnets | **2027-01-01** |  | acquisition.gov DFARS 252.225-7052 (clause MAY 2024), paras (b)(1)(ii), (b)(2), (b)(3): "Effective January 1, 2027, the Contractor shall not deliver..." (fetched 2026-10-05) |
| rare-earth | China's suspension of its Oct-2025 export controls (rare-earth items, equipment and technology; MOFCOM/GACC No. 70) rides the Kuala Lumpur joint arrangement, now extended from 2026-11-10 to 2027-01-10; expiry vs further extension cuts both ways | **2027-01-10** |  | MOFCOM 美大司负责人解读第八轮中美经贸磋商成果, PubDate 2026-09-28 (mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_cd060e0649964da8ae13216c3bb1a645.html, fetched 2026-10-05), item 8: "中美双方同意在将吉隆坡经贸磋商联合安排延期至2027年1月10日的基础上，继续积极探讨这一事项"; the KL arrangement is what suspended these controls "至2026年11月10日" (MOFCOM/GACC No. 70); formal notice amending No. 70 not yet on the mofcom 2026 announcement list (checked 2026-10-05). Resolves the former Disputed row (moved to Resolved) |
| china | US-China Kuala Lumpur joint arrangement (US 24% reciprocal-tariff suspension, China's countermeasures and export-control suspensions) extended to 2027-01-10; renewal vs snapback cuts both ways | **2027-01-10** |  | MOFCOM 美大司负责人解读第八轮中美经贸磋商成果, PubDate 2026-09-28 (mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_cd060e0649964da8ae13216c3bb1a645.html, fetched 2026-10-05), item 8: "中美双方同意在将吉隆坡经贸磋商联合安排延期至2027年1月10日的基础上，继续积极探讨这一事项"; the KL arrangement is what suspended these controls "至2026年11月10日" (MOFCOM/GACC No. 70); formal notice amending No. 70 not yet on the mofcom 2026 announcement list (checked 2026-10-05) |
| lithium | China's suspended Oct-2025 export controls on lithium batteries and artificial-graphite anode items (No. 58, suspended by No. 70) now run with the KL arrangement to 2027-01-10; two-way | **2027-01-10** |  | MOFCOM 美大司负责人解读第八轮中美经贸磋商成果, PubDate 2026-09-28 (mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_cd060e0649964da8ae13216c3bb1a645.html, fetched 2026-10-05), item 8: "中美双方同意在将吉隆坡经贸磋商联合安排延期至2027年1月10日的基础上，继续积极探讨这一事项"; the KL arrangement is what suspended these controls "至2026年11月10日" (MOFCOM/GACC No. 70); formal notice amending No. 70 not yet on the mofcom 2026 announcement list (checked 2026-10-05) |
| solar | Section 232 proclamation "Adjusting Imports of Polysilicon and Its Derivatives": 15% duty on derivatives plus minimum import prices ($0.22/W cells, $0.38/W modules) from 12:01 a.m. ET | **2026-12-04** |  | whitehouse.gov presidential action signed 2026-08-06 (whitehouse.gov/presidential-actions/2026/08/adjusting-imports-of-polysilicon-and-its-derivatives-into-the-united-states/, fetched 2026-10-05): "12:01 a.m. eastern time on December 4, 2026" |
| clean | Section 232 polysilicon tariff (15%) and module/cell minimum import prices take effect (helps US module makers, e.g. First Solar sleeve; hurts importers) | **2026-12-04** |  | whitehouse.gov presidential action signed 2026-08-06 (fetched 2026-10-05) |
| utilities | PJM 2029/2030 Base Residual Auction results posted (bidding window 2026-12-09 to 12-15) | **2026-12-22** |  | pjm.com RPM auction schedule (pjm.com/-/media/markets-ops/rpm/rpm-auction-info/rpm-auction-schedule.ashx, xlsx, fetched 2026-10-05): 2029/2030 BRA "Auction results posted" 2026-12-22 |
| india | RBI MPC policy decision (Dec 2-4 meeting, decision on the last day) | **2026-12-04** |  | rbi.org.in press release 2026-03-23, prid=62422 (fetched 2026-10-05): "December 2, 3 and 4, 2026"; re-verified 2026-10-21 (prid=62422 fetched, Press Release 2025-2026/2306: December 2-4, 2026) |
| argentina | Semiannual interest/amortisation date on Argentina's 2020 restructured USD/EUR Globales (2029/30/35/38/41/46); 2027-01-09 is a Saturday, so cash moves the next business day | **2027-01-09** |  | Republic of Argentina prospectus supplement, SEC 424B5 acc. 0001193125-20-221606 (fetched 2026-10-05): "pay interest ... semi-annually in arrears on January 9 and July 9 of each year" |
| macro | BLS CPI release (October 2026 data), 8:30 a.m. ET | **2026-11-10** |  | bls.gov/schedule/news_release/cpi.htm (fetched 2026-10-05): Nov. 10, 2026 08:30 AM |
| health-other | Abbott Q3 2026 results before market open; earnings call webcast 8:00 a.m. CT (9:00 a.m. ET) | **2026-10-21** | **catalyst >= 7** | Abbott PR 2026-09-30 (PRNewswire, republished morningstar.com): "will announce its third-quarter 2026 financial results on Wednesday, Oct. 21, before the market opens"; Abbott is IHI's ~17.8% top holding |
| base-metals | Freeport-McMoRan Q3 2026 results, before market open; conference call 10:00 a.m. ET | **2026-10-27** | **catalyst >= 7** | Freeport-McMoRan Q3 operational update, 2026-10-02 (via ad-hoc-news 2026-10-13 and SMM 2026-10-05): Q3 results scheduled before the open on October 27, 2026, call at 10:00 a.m. ET; re-verified 2026-10-21 on primary FCX IR: investors.fcx.com "Freeport Provides Third-Quarter 2026 Operational Update" (2026-10-02, fetched): "plans to release its third-quarter 2026 earnings results before the market opens on Tuesday, October 27, 2026", call 10:00 a.m. ET; fcx.com event "FCX 3Q 2026 Conference Call — 10/27/26, 10:00 AM ET" (Trendlyne's third-party 10-23 listing is a stale estimate, not a contradiction) |
| transport | UPS Q3 2026 results, before market open; earnings call 8:30 a.m. ET | **2026-10-27** |  | UPS announcement via BusinessWire, 2026-10-13, summarised in Oct 14-15 reports: Q3 results on Oct 27, 2026 before market open, call 8:30 a.m. ET; UPS is a major IYT holding |
| transport | Union Pacific Q3 2026 financial and operating results, 7:45 a.m. ET; conference call 8:45 a.m. ET — Union Pacific is IYT's #1 holding at ~17.5% | **2026-10-22** | **catalyst >= 7** | Union Pacific press release, 2026-09-24 (via BusinessWire): Q3 results on October 22, 2026 at 7:45 a.m. ET, call at 8:45 a.m. ET; re-verified 2026-10-21 (BusinessWire 20260924433924: "will release third quarter 2026 financial and operating results on Thursday, Oct. 22, 2026, at 7:45 a.m. ET", call/webcast 8:45 a.m.) |
| reit | Digital Realty Q3 2026 results after the market close; conference call 5:00 p.m. ET — DLR is DTCR's #2 holding at 13.04% (Global X, 2026-10-20) | **2026-10-29** | **catalyst >= 7** | Digital Realty press release, Austin TX, 2026-10-01 (GlobeNewswire, via finviz news/398000, fetched 2026-10-21): "will release financial results for the third quarter of 2026 after the market closes on Thursday, October 29, 2026"; call "at 5:00 p.m. ET / 4:00 p.m. CT on Thursday, October 29, 2026" |
| transport | American Airlines Group Q3 2026 results conference call, live webcast 7:30 a.m. CT — AAL is JETS's #3 holding at 10.60% (SA 2026-10-16) | **2026-10-22** |  | AAL news release 2026-10-01 (AAL IR PDF on s202.q4cdn.com, fetched 2026-10-21): "will webcast a live audio feed of its third-quarter 2026 financial results conference call Oct. 22 at 7:30 a.m. CT" |

**Catalyst floor:** every fund in a theme marked above scores catalyst >= 7 this run (issuer-confirmed, theme-specific, within 30 days). Judgment may lift it to 8-10, never below; only 'CONTRADICTED: <source>' overrides. check_memo.py fails a lower score.

A panelist that cannot re-find one of these writes "carried forward, not re-searched" and keeps
the band the date earns. It does not score the theme down for having no dated trigger, and never
calls it "unverified": only a cited source that CONTRADICTS the date overturns it (write
"CONTRADICTED: <source>"; the verifier then marks the ledger row RETRACTED). check_memo.py fails
a ballot that doubts a live row without one.

### Disputed — sources contradict each other; neither date is confirmed

| theme | claim | readings | sources |
|---|---|---|---|
| ai/robot | NVIDIA GTC 2027 start date, San Jose McEnery Convention Center | (a) March 14–18, 2027 — NVIDIA's own GTC FAQ; (b) March 15–18, 2027 — NVIDIA's GTC call-for-submissions page and main GTC pages. The live confirmed-table row keeps the FAQ's 2027-03-14 start; the event, venue and month are not in dispute, only the start day | (a) nvidia.com/gtc/faq (fetched 2026-10-17); (b) nvidia.com/gtc/call-for-submissions and nvidia.com/gtc (fetched 2026-10-17). Re-checked 2026-10-21: still split on nvidia.com itself — FAQ "NVIDIA GTC will take place from March 14–18, 2027" (venue San Jose McEnery Convention Center), while the FAQ banner and nvidia.com/gtc read "March 15–18"; neither page names a separate training day. Some third-party listings read the 14th as a pre-conference training day (unconfirmed). Stays Disputed |

A catalyst score of 7+ that rests on a disputed date must cite a primary source (the issuing
ministry / agency / company) that settles it; otherwise score only what holds under both readings.

