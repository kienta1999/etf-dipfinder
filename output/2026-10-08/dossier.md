> Run by: Muse Spark (unknown) — full panel

# etf-dip-pick 2026-10-08 — dossier (Phase 1: quick pass)

Scan data as of 2026-10-07 (close). 25 CANDIDATES across 15 themes.

## A. Candidate rows (from data/scan.csv, is_candidate=True)

Column legend: `theme` = theme group; `asof` = price date; `days` = bars of history; `price` = close;
`dd_52w` = drawdown from 52-week high; `dd_pctile` = depth percentile vs own history (lower = deeper);
`dd_z` = drawdown z-score; `vs_sma200`, `vs_sma50` = distance to moving averages;
`rs_spy_3m/6m/12m` = excess return vs SPY over 3/6/12 months; `ret_10d` = trailing 10-day return;
`vol_60d` = 60-day annualized vol; `dollar_vol` = avg dollar volume; `tp_pct`/`sl_pct` = target/stop
pct from consolidate; `dip_low_pct` = how far the dip low is below current; `rr` = reward/risk;
`size_1pct` = position size for 1% portfolio risk; `is_dip` = passed the dip gate; `stabilizing` =
bounce signal; `dip_score` = depth (NOT quality); `price_score` = computed lens score;
`theme_score` = best dip_score in theme; `is_candidate` = True.

```
,theme,asof,days,price,dd_52w,dd_pctile,dd_z,vs_sma200,vs_sma50,rs_spy_3m,rs_spy_6m,rs_spy_12m,ret_10d,vol_60d,dollar_vol,tp_pct,sl_pct,dip_low_pct,rr,size_1pct,is_dip,stabilizing,dip_score,price_score,theme_score,is_candidate
REMX,rare-earth,2026-10-07,752.0000,61.8800,-0.4350,0.0041,-1.1377,-0.2785,-0.1407,-0.2633,-0.4944,-0.3189,-0.1001,0.3824,43388641.6026,0.7700,-0.1656,0.0000,4.6506,0.0604,True,False,0.0537,6,0.0537,True
TAN,solar,2026-10-07,752.0000,43.5300,-0.4112,0.0232,-1.2046,-0.2060,-0.0909,-0.2443,-0.3709,-0.2283,-0.0337,0.3413,33432766.3732,0.6984,-0.1478,-0.0122,4.7248,0.0677,True,False,0.0777,5,0.0777,True
SLV,silver,2026-10-07,752.0000,53.8200,-0.4903,0.0314,-1.2859,-0.1827,-0.0702,-0.0424,-0.3579,0.0518,-0.0746,0.3813,886640867.0167,0.9621,-0.1651,-0.0637,5.8269,0.0606,True,False,0.0958,7,0.0958,True
KWEB,china,2026-10-07,752.0000,24.3300,-0.3896,0.0286,-1.6043,-0.1603,-0.0659,-0.1177,-0.3195,-0.5676,-0.0209,0.2429,371161568.1570,0.6384,-0.1052,-0.0288,6.0701,0.0951,True,False,0.1019,4,0.1019,True
FXI,china,2026-10-07,752.0000,33.4200,-0.1743,0.0628,-0.9956,-0.0718,-0.0464,-0.0362,-0.2292,-0.3476,-0.0274,0.1751,585417607.6966,0.2111,-0.0758,-0.0548,2.7846,0.1319,True,False,0.3238,4,0.1019,True
URNM,nuclear,2026-10-07,752.0000,47.8700,-0.4301,0.0300,-0.9541,-0.2064,-0.0972,-0.1196,-0.4161,-0.3560,-0.0543,0.4508,28719591.0446,0.7545,-0.1952,-0.0155,3.8658,0.0512,True,False,0.1133,4,0.1133,True
NLR,nuclear,2026-10-07,752.0000,105.2700,-0.3596,0.0150,-0.8692,-0.1828,-0.0708,-0.1055,-0.3897,-0.4281,-0.0282,0.4137,43607929.0255,0.5614,-0.1791,-0.0244,3.1342,0.0558,True,False,0.1731,5,0.1133,True
URA,nuclear,2026-10-07,752.0000,39.9300,-0.3540,0.0205,-0.7986,-0.1690,-0.0778,-0.0936,-0.3787,-0.3528,-0.0491,0.4433,133091563.7671,0.5480,-0.1919,-0.0604,2.8549,0.0521,True,False,0.2090,4,0.1133,True
SHLD,defense-us,2026-10-07,752.0000,58.7400,-0.2447,0.0068,-1.1898,-0.1338,-0.0884,-0.0808,-0.3694,-0.3376,-0.0571,0.2057,107722977.4133,0.3240,-0.0891,-0.0124,3.6380,0.1123,True,False,0.1320,6,0.1320,True
XAR,defense-us,2026-10-07,752.0000,226.6400,-0.2358,0.0014,-0.9276,-0.1521,-0.1224,-0.2086,-0.3207,-0.2507,-0.0532,0.2542,80169479.2566,0.3086,-0.1101,0.0000,2.8033,0.0909,True,False,0.2034,6,0.1320,True
ITA,defense-us,2026-10-07,752.0000,203.6000,-0.1950,0.0014,-0.9569,-0.1150,-0.1087,-0.1858,-0.2770,-0.2094,-0.0482,0.2038,187124254.5695,0.2423,-0.0882,0.0000,2.7454,0.1133,True,False,0.2395,6,0.1320,True
PPA,defense-us,2026-10-07,752.0000,152.8500,-0.1731,0.0014,-0.9048,-0.1051,-0.0897,-0.1600,-0.2852,-0.2010,-0.0417,0.1913,47929640.4303,0.2093,-0.0828,0.0000,2.5268,0.1207,True,False,0.2694,6,0.1320,True
UFO,space,2026-10-07,752.0000,43.0400,-0.3644,0.0177,-1.3255,-0.0926,-0.0354,-0.1284,-0.3101,-0.0682,-0.0052,0.2749,10075800.1994,0.5733,-0.1190,-0.0253,4.8159,0.0840,True,False,0.1804,7,0.1804,True
ARKX,space,2026-10-07,752.0000,32.6200,-0.1357,0.1310,-0.5248,0.0026,0.0004,-0.0271,-0.1265,-0.1325,-0.0015,0.2585,15960456.3778,0.1570,-0.1119,-0.0950,1.4021,0.0893,True,False,0.7848,4,0.1804,True
PBW,clean,2026-10-07,752.0000,28.9200,-0.3754,0.0314,-1.0153,-0.1565,-0.0839,-0.2186,-0.2530,-0.2683,-0.0509,0.3697,9565314.0911,0.6010,-0.1601,0.0000,3.7539,0.0625,True,False,0.1854,5,0.1854,True
ICLN,clean,2026-10-07,752.0000,17.3100,-0.2692,0.0205,-1.0134,-0.0797,-0.0193,-0.1410,-0.2184,-0.0820,-0.0063,0.2656,105544536.5109,0.3684,-0.1150,-0.0289,3.2025,0.0869,True,False,0.3294,6,0.1854,True
GLD,gold,2026-10-07,752.0000,375.8800,-0.2420,0.0327,-0.9930,-0.0962,-0.0526,-0.0426,-0.2905,-0.1382,-0.0433,0.2437,3266088038.1935,0.3193,-0.1055,-0.0291,3.0254,0.0948,True,False,0.2279,6,0.2279,True
INDA,india,2026-10-07,752.0000,46.1100,-0.1660,0.0205,-1.3362,-0.0732,-0.0561,-0.0959,-0.2197,-0.2958,-0.0404,0.1243,235738986.4706,0.1991,-0.0538,-0.0150,3.7001,0.1858,True,False,0.2939,5,0.2939,True
ITB,housing,2026-10-07,752.0000,84.7000,-0.2452,0.1228,-0.8679,-0.1199,-0.0865,-0.1549,-0.2403,-0.3673,-0.0461,0.2826,216288723.8882,0.3249,-0.1224,0.0000,2.6555,0.0817,True,False,0.3168,2,0.3168,True
XHB,housing,2026-10-07,752.0000,94.8900,-0.2102,0.0900,-0.8412,-0.0984,-0.0694,-0.1498,-0.2222,-0.2955,-0.0227,0.2499,193590811.4299,0.2662,-0.1082,-0.0073,2.4597,0.0924,True,False,0.3826,4,0.3168,True
LIT,lithium,2026-10-07,752.0000,69.5100,-0.2381,0.1678,-0.9573,-0.0699,-0.0393,-0.0820,-0.2455,0.0049,-0.0010,0.2487,9504076.6294,0.3124,-0.1077,-0.0399,2.9016,0.0929,True,False,0.3180,5,0.3180,True
EUAD,defense-eu,2026-10-07,491.0000,40.1500,-0.1684,0.0424,-0.8888,-0.0751,-0.0953,-0.0967,-0.2529,-0.3026,-0.0652,0.1895,6309299.7227,0.2025,-0.0820,-0.0625,2.4684,0.1219,True,False,0.3355,5,0.3355,True
IGF,grid/infra,2026-10-07,752.0000,62.1100,-0.0921,0.0095,-0.9885,-0.0477,-0.0374,-0.1060,-0.2394,-0.1313,-0.0042,0.0931,63474570.9138,0.1014,-0.0403,-0.0129,2.5142,0.2480,True,False,0.3602,7,0.3602,True
PAVE,grid/infra,2026-10-07,752.0000,53.2900,-0.1101,0.1064,-0.6140,-0.0201,-0.0359,-0.0920,-0.1649,-0.0494,-0.0019,0.1794,77062721.7060,0.1238,-0.0777,-0.0148,1.5935,0.1288,True,False,0.6592,4,0.3602,True
XLU,utilities,2026-10-07,752.0000,41.1500,-0.1199,0.0205,-0.7935,-0.0599,-0.0236,-0.1180,-0.2638,-0.2268,0.0352,0.1511,1355881045.0208,0.1362,-0.0654,-0.0462,2.0820,0.1529,True,True,0.3896,7,0.3896,True
```
## B. Leaders — where did the money go?

From the scan's LEADERS block: the 3-month relative-to-SPY leaders were **crypto (ETHA/IBIT),
oil (USO/XOP), software (WCLD/SKYX), Brazil (EWZ), cyber (BUG)**. Reading the leadership:
money is crowding into (a) inflation/refuge hedges (crypto spot, oil/energy, gold held
structurally bid), (b) AI-exposed cash-flow tech (software, cyber), and (c) a Brazil
idiosyncratic/em bounce. The mirror image: almost every dip theme is either rate-sensitive
(utilities, housing, solar/clean — Fed hiked to 3.75–4% mid-September, 10y >5.3%),
war-premium-deflating (defense-us/eu — Middle East peace agreement signed in Egypt ~Oct 6–7),
or geopolitics-cooling (rare-earth, china — Trump-Xi Sept meeting; KL arrangement extended to
2027-01-10). The cluster reads as one macro rotation — higher-for-longer rates + cooling
conflict risk — not 15 independent problems.

## C. Quick-pass memo (UNVERIFIED — panelists, challenge every line)

One web search per theme; provisional buckets below are the orchestrator's first pass only.

1. **rare-earth → rotation.** REMX fell ~28% in 3m; sector-wide, not company-specific:
   MP Materials −15.8% in 30 days "largely sector-driven rather than company-specific"
   (tickeron, Oct 2026), fundamentals intact (Q2 revenue +89% YoY, GM magnet shipments
   targeted Q4). Driver: renewed US–China diplomatic signals (Trump-Xi Sept meeting) and
   the KL arrangement's extension to 2027-01-10 undercut the scarcity premium.
   Single fund; no sibling nuance.
2. **solar → rotation.** TAN −41% off high. Headwinds are rates (10y ~5.3% crushes solar
   financing economics) plus broad growth selloffs — not demand: EIA expects solar to be
   51% of new US power capacity in 2026. Dated protectionist tailwinds are live: USITC
   final injury vote Oct 14 and Commerce AD/CVD duty orders Nov 2 (Solar IV), plus Section
   232 polysilicon duties/minimum import prices from Dec 4. Watch: Deutsch-Bank-type
   sentiment says "recovery may stumble while borrowing costs stay elevated."
3. **silver → rotation.** SLV −49% off high; silver peaked at $121/oz Jan 2026. Cause is
   macro, not metal: Kevin Warsh Fed-chair pick (Jan 30) repriced rate-cut hopes, CME margin
   hikes forced liquidations, and the Sept Fed hike + 5.3% 10y + strong dollar keep the
   carry cost high. Structural story intact: 5th consecutive annual supply deficit
   (2025: 40.3M oz; Metals Focus expects another deficit ~46.3M oz in 2026).
4. **china → rotation.** KWEB/FXI drifted on a liquidity gap, not a policy event: Hong Kong
   fell 2.6% last week while mainland was closed for Golden Week; Stock Connect reopens
   Oct 8. The KL arrangement extension (tariff suspension to 2027-01-10) and APEC Shenzhen
   Nov 18–19 are constructive; Trump-Xi September summit kept tone calm. FXI is the
   less-volatile SOE/banks version of the same theme — bucket copied.
5. **nuclear → rotation.** Uranium at a 19-year high (~$96/lb) yet miners fell: utilities
   are reluctant to sign term contracts at record prices and are drawing down inventories,
   so producers' realized prices lag (Cameco ~$65/lb in H1 vs spot) — investors marked
   shares down on earnings, not on demand. Structurally the market tightens (Kazatomprom's
   sulphuric-acid dependence; fuel is a small share of reactor opex, so utilities must
   return to market). URNM/NLR/URA get the same bucket; URNM is deepest (−43%), no
   fund-specific break found.
6. **defense-us → rotation.** Sector −18% from mid-Aug highs; Reuters (Oct 5) calls it
   sentiment, not fundamentals: Middle East peace agreement, stalled FY27 budget/CR to
   Dec 11, and pre-election wait-and-see. Structural thesis intact: $1T+ US defense
   budgets, record backlogs, NATO 5%-by-2035 commitments; munitions inventories must be
   rebuilt. SHLD/XAR/ITA/PPA all copied — SHLD is defense-tech, otherwise the same
   political-noise selloff.
7. **space → UNVERIFIED-leaning unclear.** UFO −36% off its $68 52w high. The write-up
   (barchart, ~Aug 2026) argues the market "priced in decades of science-fiction
   perfection" and is repricing on capex, dilution risk, and late-cycle valuation
   discipline — not because satellites stopped launching. That is rotation-shaped, but the
   "trillion-dollar space economy" multiple may be permanently repriced, which is
   break-adjacent. UFO vs ARKX: UFO is the deeper, purer space exposure; ARKX is a
   mild dip (−13.6%) and barely qualifies. Panelists should challenge: is the 2026
   repricing a flow move or a permanent multiple reset?
8. **clean → rotation.** PBW/ICLN hit by the same rate shock plus US-specific policy
   drag: IRA rollbacks and US withdrawal from the UNFCCC. Global demand is accelerating
   elsewhere (India cut GST on renewables to 5%; EIA 51%-of-new-capacity solar).
   Provisional rotation — but panelists: weigh whether US policy repeal is a partial
   break for the US-heavy sleeves of these funds (PBW is small-cap heavy, concentrated).
9. **gold → rotation.** GLD −24% off high; ~20% below Jan peak, but holding above $4,000
   with no new lows since July despite 10y at 24-year highs — profit-taking on rates,
   not demand destruction. Structural buyers (central banks) intact; December Fed
   pricing (87% hike odds) is the cap, midterms historically the turn. Single fund.
10. **india → rotation.** Nifty −13% YTD; the triple hit is all macro: oil >$100
    (Iran war, India's 90%-import dependence), RBI hiked repo to 5.5% (inflation 4.82%),
    and $27.8B YTD FII outflows while domestic institutions buy the dip. Structural
    India growth story untouched; HDFC Bank results Oct 17 is the near dated trigger.
    Single fund.
11. **housing → rotation.** ITB −24.5% / XHB −21% off highs on 30y mortgage 7.28% and
    10y >5.1% — pure affordability squeeze, builders flagging caution (KB Home, Lennar).
    Counter-signal: Berkshire Hathaway is doubling down (Lennar stake, Taylor Morrison
    deal) and the structural US housing shortage persists. Copied to both funds.
    D.R. Horton Q4 results Oct 29 gives the theme a dated catalyst.
12. **lithium → UNVERIFIED-leaning unclear.** Guangzhou carbonate futures fell 22.5% in
    September to 122,800 yuan/t, 39% below the May high — on a Chinese price-agency
    methodology change that doubled reported stockpiles plus rising Australian supply,
    while CATL's Jianxiawo mine went back on care-and-maintenance. That's a genuine
    supply-side surplus, not just flows — but EV/ESS demand growth is intact and the
    lithium cycle has always been surplus-then-squeeze. Not a demand collapse, not
    clearly a permanent re-rating. Panelists should challenge hard either way;
    Albemarle reports Nov 4. Single fund.
13. **defense-eu → rotation.** EUAD −16.8% off high. Same peace-headline pressure as
    defense-us (Middle East peace agreement signed in Egypt); EU names were also
    digesting 2025's parabolic run (Rheinmetall +152%). Rearmament commitments intact
    (NATO 3.5%-by-2035 roadmap, SIPRI: European military spend +14% in 2025). Single fund.
14. **grid/infra → rotation.** No theme-specific bad news found; shallow dips
    (IGF −9.2%, PAVE −11%). Rate/macro drift plus AI-infra multiple compression on
    PAVE's high-flyer exposures (Vertiv etc.). Long-term thesis intact: IEA sees annual
    grid investment rising ~50% by 2030; the Surface Transportation Extension Act cliff
    (Dec 11) is two-way policy risk, not a break. Copied to both funds.
15. **utilities → rotation.** XLU −12% off high is the cleanest rate-shock read in the
    scan: Fed hiked to 3.75–4% mid-September, 10y >5.3% vs XLU's ~3% dividend yield —
    discount-rate repricing, not an earnings impairment. Regulated cash flows intact;
    Morningstar sees 6–8% sector earnings growth and calls the group fairly valued after
    the pullback. Broad fund → core-bucket eligible. Single fund, stabilizing=True.

Summary: 13 rotation, 2 unclear (space, lithium), 0 break. The common thread is a
September rate shock plus October geopolitical cooling — the same macro weather, 15
different umbrellas.
## D. Confirmed catalysts carried forward — already verified, do NOT rescore as "not found"

*(verbatim output of `uv run python scripts/carry_forward.py`, run 2026-10-08; floor marks added per the script's "floor" column)*

| theme | event | date | floor | confirmed by |
|---|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | **catalyst >= 7 FLOOR** | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 and 2026-10-01 (BusinessWire 20260730139928: "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026"); re-verified 2026-10-04 on SEC EDGAR 6-K ex-99.1 (Cameco Q2 release 2026-07-31, acc. 0001193125-26-326768), same sentence |
| macro | FOMC decision (Oct 27-28 meeting, statement on second day) | **2026-10-28** |  | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: October 27-28) |
| macro | FOMC decision (Dec 8-9 meeting, statement on second day) | **2026-12-09** |  | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: December 8-9, SEP meeting) |
| ai/robot | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | **2027-03-14** |  | nvidia.com GTC FAQ |
| solar | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | **2026-10-14** | **catalyst >= 7 FLOOR** | Reuters/SRN 2026-09-11; SMM; Sxcoal; re-verified 2026-09-29 (solarpowerworld 9/20, Sxcoal 9/14, pv-magazine) and 2026-10-01 (pv-tech.org 9/15: "Commission is scheduled to make its final determination on 14 October 2026") |
| solar | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | **2026-11-02** |  | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 (Sxcoal, pv-magazine, taiyangnews) and 2026-10-01 (pv-tech.org 9/15: "final AD/CVD duty orders, currently scheduled for 2 November 2026") |
| housing | D.R. Horton Q4/FY26 results, before market open, 8:30 a.m. ET call | **2026-10-29** | **catalyst >= 7 FLOOR** | D.R. Horton investor site press release, 2026-09-10 (BusinessWire): "will release financial results for its fourth quarter and fiscal year ended September 30, 2026 on Thursday, October 29, 2026 before the market opens" |
| lithium | Albemarle Q3 2026 results, after NYSE close; earnings call Nov 5, 8:00 a.m. EST | **2026-11-04** | **catalyst >= 7 FLOOR** | Albemarle PR Newswire, 2026-10-01: "will release its third quarter 2026 earnings after the NYSE closes on Wednesday, November 4, 2026" |
| utilities | Southern Company Q3 2026 earnings released by 7:30 a.m. ET; analyst call 1 p.m. ET | **2026-11-05** | **catalyst >= 7 FLOOR** | southerncompany.mediaroom.com press release 2026-09-25 (fetched): "plans to release its earnings for the third quarter of 2026 by 7:30 a.m. ET on Thursday, November 5, 2026"; Southern is XLU's #2 holding at 7.69% (SSGA, 2026-10-01) |
| defense-us | RTX Q3 2026 results before market open; 8:30 a.m. ET call | **2026-10-20** | **catalyst >= 7 FLOOR** | rtx.com news release 2026-09-29 (PRNewswire, fetched): "will issue its third quarter 2026 earnings results on Tuesday, October 20, prior to the stock market opening" |
| defense-us | Lockheed Martin Q3 2026 results before market open; 8:30 a.m. ET webcast | **2026-10-22** |  | news.lockheedmartin.com release dated 2026-10-01 (fetched; also at investors.lockheedmartin.com): call "Thursday, Oct. 22, 2026, at 8:30 a.m. ET", results published prior to market opening |
| defense-us | Howmet Aerospace Q3 2026 results ~7:00 a.m. ET, webcast 10:00 a.m. ET (also a PAVE holding) | **2026-10-29** |  | howmet.com press release 2026-10-01 (fetched): "Thursday, October 29, 2026. The press release and presentation materials will be available at approximately 7:00 AM ET" |
| defense-us | FY27 continuing resolution (Division A of P.L. 119-103) expires: appropriations cliff, outcome cuts both ways | **2026-12-11** |  | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. A sec. 106(3): funds available until "December 11, 2026"; CRS R49353 (2026-09-17) |
| grid/infra | Surface Transportation Extension Act of 2026 (Division C of P.L. 119-103) ends: IIJA highway/transit authorities lapse unless reauthorized or re-extended | **2026-12-11** |  | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. C: "extension end date means December 11, 2026", extension period from 2026-10-01 |
| clean | Vestas Q3 2026 interim report (quiet period from 2026-10-10) | **2026-11-11** |  | vestas.com/en/investor/Calendar-Events (fetched 2026-10-04): "Disclosure of Q3 2026 interim report", 11 November 2026 |
| india | HDFC Bank board meeting to approve results for the quarter ended 2026-09-30 (Q2 FY27) | **2026-10-17** | **catalyst >= 7 FLOOR** | HDFC Bank Form 6-K filed 2026-09-22 (SEC acc. 0001193125-26-397434, text read via stocktitan): board meets 2026-10-17 to approve unaudited standalone and consolidated results; trading window closed 9/24-10/19 |
| china | APEC Economic Leaders' Meeting, Shenzhen, Nov 18-19 (CEO Summit Nov 17-18) | **2026-11-18** |  | Shenzhen Government Online (sz.gov.cn) 2026-09-10 (fetched): Economic Leaders' Meeting "Nov. 18 to 19"; Xi announced Shenzhen host 2025-11 (cppcc.gov.cn) |
| rare-earth | DFARS 252.225-7052: from 2027-01-01 US defense contractors may not deliver NdFeB/SmCo magnets (or tantalum/tungsten) mined, refined, separated, melted or produced in China, Russia, Iran or North Korea; full supply chain for magnets | **2027-01-01** |  | acquisition.gov DFARS 252.225-7052 (clause MAY 2024), paras (b)(1)(ii), (b)(2), (b)(3): "Effective January 1, 2027, the Contractor shall not deliver..." (fetched 2026-10-05) |
| rare-earth | China's suspension of its Oct-2025 export controls (rare-earth items, equipment and technology; MOFCOM/GACC No. 70) rides the Kuala Lumpur joint arrangement, now extended from 2026-11-10 to 2027-01-10; expiry vs further extension cuts both ways | **2027-01-10** |  | MOFCOM 美大司负责人解读第八轮中美经贸磋商成果, PubDate 2026-09-28 (mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_cd060e0649964da8ae13216c3bb1a645.html, fetched 2026-10-05), item 8: "中美双方同意在将吉隆坡经贸磋商联合安排延期至2027年1月10日的基础上，继续积极探讨这一事项"; the KL arrangement is what suspended these controls "至2026年11月10日" (MOFCOM/GACC No. 70); formal notice amending No. 70 not yet on the mofcom 2026 announcement list (checked 2026-10-05). Resolves the former Disputed row (moved to Resolved) |
| china | US-China Kuala Lumpur joint arrangement (US 24% reciprocal-tariff suspension, China's countermeasures and export-control suspensions) extended to 2027-01-10; renewal vs snapback cuts both ways | **2027-01-10** |  | MOFCOM 美大司负责人解读第八轮中美经贸磋商成果, PubDate 2026-09-28 (mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_cd060e0649964da8ae13216c3bb1a645.html, fetched 2026-10-05), item 8: "中美双方同意在将吉隆坡经贸磋商联合安排延期至2027年1月10日的基础上，继续积极探讨这一事项"; the KL arrangement is what suspended these controls "至2026年11月10日" (MOFCOM/GACC No. 70); formal notice amending No. 70 not yet on the mofcom 2026 announcement list (checked 2026-10-05) |
| lithium | China's suspended Oct-2025 export controls on lithium batteries and artificial-graphite anode items (No. 58, suspended by No. 70) now run with the KL arrangement to 2027-01-10; two-way | **2027-01-10** |  | MOFCOM 美大司负责人解读第八轮中美经贸磋商成果, PubDate 2026-09-28 (mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_cd060e0649964da8ae13216c3bb1a645.html, fetched 2026-10-05), item 8: "中美双方同意在将吉隆坡经贸磋商联合安排延期至2027年1月10日的基础上，继续积极探讨这一事项"; the KL arrangement is what suspended these controls "至2026年11月10日" (MOFCOM/GACC No. 70); formal notice amending No. 70 not yet on the mofcom 2026 announcement list (checked 2026-10-05) |
| solar | Section 232 proclamation "Adjusting Imports of Polysilicon and Its Derivatives": 15% duty on derivatives plus minimum import prices ($0.22/W cells, $0.38/W modules) from 12:01 a.m. ET | **2026-12-04** |  | whitehouse.gov presidential action signed 2026-08-06 (whitehouse.gov/presidential-actions/2026/08/adjusting-imports-of-polysilicon-and-its-derivatives-into-the-united-states/, fetched 2026-10-05): "12:01 a.m. eastern time on December 4, 2026" |
| clean | Section 232 polysilicon tariff (15%) and module/cell minimum import prices take effect (helps US module makers, e.g. First Solar sleeve; hurts importers) | **2026-12-04** |  | whitehouse.gov presidential action signed 2026-08-06 (fetched 2026-10-05) |
| utilities | PJM 2029/2030 Base Residual Auction results posted (bidding window 2026-12-09 to 12-15) | **2026-12-22** |  | pjm.com RPM auction schedule (pjm.com/-/media/markets-ops/rpm/rpm-auction-info/rpm-auction-schedule.ashx, xlsx, fetched 2026-10-05): 2029/2030 BRA "Auction results posted" 2026-12-22 |
| india | RBI MPC policy decision (Dec 2-4 meeting, decision on the last day) | **2026-12-04** |  | rbi.org.in press release 2026-03-23, prid=62422 (fetched 2026-10-05): "December 2, 3 and 4, 2026" |
| argentina | Semiannual interest/amortisation date on Argentina's 2020 restructured USD/EUR Globales (2029/30/35/38/41/46); 2027-01-09 is a Saturday, so cash moves the next business day | **2027-01-09** |  | Republic of Argentina prospectus supplement, SEC 424B5 acc. 0001193125-20-221606 (fetched 2026-10-05): "pay interest ... semi-annually in arrears on January 9 and July 9 of each year" |
| macro | BLS CPI release (September 2026 data), 8:30 a.m. ET | **2026-10-14** |  | bls.gov/schedule/news_release/cpi.htm (fetched 2026-10-05): Oct. 14, 2026 08:30 AM |
| macro | BLS CPI release (October 2026 data), 8:30 a.m. ET | **2026-11-10** |  | bls.gov/schedule/news_release/cpi.htm (fetched 2026-10-05): Nov. 10, 2026 08:30 AM |

**Catalyst floors this run (issuer/agency-confirmed, theme-specific, ≤30 days from 2026-10-08):**
nuclear (Cameco Q3, 2026-10-30) · solar (USITC Solar IV vote, 2026-10-14) · housing (D.R. Horton Q4, 2026-10-29) · lithium (Albemarle Q3, 2026-11-04) · utilities (Southern Co Q3, 2026-11-05) · defense-us (RTX Q3, 2026-10-20) · india (HDFC Bank results, 2026-10-17).
Every fund in these themes scores catalyst **>= 7** — judgment may lift to 8-10, never below; only 'CONTRADICTED: <source>' overrides (check_memo.py fails a lower score).
Themes without a floor: rare-earth (no dated event within 30d), china (APEC 11-18 is outside 30d), space (none), clean (Vestas 11-11 is 34 days out — outside), gold (none), defense-eu (none), grid/infra (STEA cliff 12-11 is 64 days out, two-way).

A panelist that cannot re-find one of these writes "carried forward, not re-searched" and keeps the band the date earns. It does not score the theme down for having no dated trigger, and never calls it "unverified": only a cited source that CONTRADICTS the date overturns it (write "CONTRADICTED: <source>"; the verifier then marks the ledger row RETRACTED). check_memo.py fails a ballot that doubts a live row without one.
