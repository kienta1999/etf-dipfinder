# Dossier — ETF dip candidates, scan date 2026-09-18 (market data as of 2026-09-17 close)

## A. Scan numbers (deterministic; dip_score 0 = most beaten up on depth + rel weakness + trend)
dd_52w = % off 52w high; dd_z = dd / 60d annualised vol; dd_pctile = share of this ETF's own 3y drawdown history
that is shallower than today (0.02 = worst 2% of its own history); vs_sma200/50 = % vs moving avg; rs_spy_Nm = return
minus SPY over N months; ret_10d = 10-day return; stabilizing = ret_10d > 0; tp_pct/sl_pct/rr = take-profit/stop/reward:risk
from 52w-high targets and dip lows; size_1pct = $ size of a 1% portfolio-risk position.

```
       ETF      theme       days      price     dd_52w  dd_pctile       dd_z  vs_sma200   vs_sma50  rs_spy_3m  rs_spy_6m rs_spy_12m    ret_10d    vol_60d stabilizing     tp_pct     sl_pct         rr dip_low_pct  size_1pct  dip_score
      KWEB      china   753.0000    24.4000    -0.3971     0.0082    -1.5597    -0.1782    -0.0841    -0.0705    -0.3306    -0.5434    -0.0506     0.2546      False     0.6588    -0.1103     5.9748    -0.0316     0.0907     0.0532
       FXI      china   753.0000    34.1900    -0.1660     0.0872    -0.9327    -0.0583    -0.0267    -0.0158    -0.2075    -0.3200    -0.0380     0.1780      False     0.1990    -0.0771     2.5825    -0.0760     0.1298     0.2459
      REMX rare-earth   753.0000    69.1000    -0.3691     0.1076    -0.9180    -0.1979    -0.0666    -0.3124    -0.3618    -0.0070    -0.0942     0.4021      False     0.5851    -0.1741     3.3603    -0.0653     0.0574     0.0591
       TAN      solar   753.0000    46.3600    -0.3729     0.0436    -1.0463    -0.1581    -0.0803    -0.2387    -0.3397    -0.0818    -0.0193     0.3564      False     0.5947    -0.1543     3.8534    -0.0375     0.0648     0.0727
      URNM    nuclear   753.0000    51.3100    -0.3891     0.0817    -0.8711    -0.1550    -0.0378    -0.1329    -0.3388    -0.2046    -0.0662     0.4467      False     0.6369    -0.1934     3.2931    -0.0815     0.0517     0.1056
       NLR    nuclear   753.0000   110.5700    -0.3273     0.0218    -0.8079    -0.1517    -0.0311    -0.1448    -0.3446    -0.2762    -0.0552     0.4052      False     0.4866    -0.1754     2.7734    -0.0712     0.0570     0.1251
       URA    nuclear   753.0000    42.6800    -0.3095     0.0436    -0.7078    -0.1158    -0.0112    -0.1257    -0.2893    -0.1602    -0.0370     0.4373      False     0.4482    -0.1893     2.3673    -0.1209     0.0528     0.2241
       SLV     silver   753.0000    58.9700    -0.4416     0.0627    -1.1005    -0.1033     0.0400    -0.0589    -0.3007     0.3595    -0.0017     0.4012      False     0.7907    -0.1737     4.5512    -0.1455     0.0576     0.1196
       UFO      space   753.0000    43.6600    -0.3553     0.0204    -1.1094    -0.0695    -0.0294    -0.1757    -0.1983     0.1062     0.0121     0.3202       True     0.5511    -0.1387     3.9741    -0.0208     0.0721     0.2064
      ARKX      space   753.0000    32.3000    -0.1441     0.0981    -0.5044     0.0022     0.0030    -0.0959    -0.1258     0.0388     0.0141     0.2857       True     0.1684    -0.1237     1.3612    -0.0861     0.0808     0.6493
       PBW      clean   753.0000    30.7600    -0.3416     0.1798    -0.8356    -0.1130    -0.0642    -0.2580    -0.1928     0.0095    -0.0213     0.4088      False     0.5188    -0.1770     2.9311    -0.0293     0.0565     0.2187
      ICLN      clean   753.0000    17.7300    -0.2515     0.0436    -0.8415    -0.0545    -0.0140    -0.1661    -0.1913     0.0350     0.0207     0.2988       True     0.3360    -0.1294     2.5963    -0.0485     0.0773     0.2988
      QCLN      clean   753.0000    48.1000    -0.2975     0.0341    -0.7083    -0.0787    -0.0528    -0.2437    -0.1435     0.0468    -0.0082     0.4200      False     0.4235    -0.1819     2.3286    -0.0337     0.0550     0.3708
      SHLD defense-us   753.0000    62.9900    -0.1900     0.0504    -0.7780    -0.0730    -0.0236    -0.0418    -0.3283    -0.2191    -0.0019     0.2443      False     0.2346    -0.1058     2.2184    -0.0790     0.0945     0.2247
       XAR defense-us   753.0000   241.3200    -0.1867     0.0041    -0.6987    -0.0967    -0.0963    -0.1867    -0.2682    -0.0897    -0.0355     0.2672      False     0.2296    -0.1157     1.9842     0.0000     0.0864     0.2573
       ITA defense-us   753.0000   213.8800    -0.1544     0.0027    -0.7260    -0.0687    -0.0920    -0.1499    -0.2332    -0.1062    -0.0414     0.2126      False     0.1826    -0.0921     1.9827     0.0000     0.1086     0.2978
       PPA defense-us   753.0000   160.0400    -0.1368     0.0082    -0.6772    -0.0635    -0.0724    -0.1307    -0.2415    -0.0999    -0.0216     0.2019      False     0.1584    -0.0874     1.8118    -0.0036     0.1144     0.3370
       XLU  utilities   753.0000    41.6900    -0.1148     0.0041    -0.7892    -0.0575    -0.0503    -0.0882    -0.2550    -0.1497    -0.0230     0.1455      False     0.1297    -0.0630     2.0590    -0.0089     0.1587     0.2848
       GLD       gold   753.0000   398.3600    -0.1967     0.0668    -0.7960    -0.0428     0.0149    -0.0067    -0.2634     0.0048    -0.0110     0.2471      False     0.2449    -0.1070     2.2884    -0.0838     0.0935     0.3183
       XHB    housing   753.0000    97.0700    -0.1966     0.1213    -0.7090    -0.0884    -0.0799    -0.1261    -0.1800    -0.3179    -0.0405     0.2772      False     0.2447    -0.1200     2.0380    -0.0242     0.0833     0.3243
       ITB    housing   753.0000    88.5500    -0.2109     0.2098    -0.6826    -0.0884    -0.0690    -0.0996    -0.1801    -0.3639    -0.0379     0.3090      False     0.2673    -0.1338     1.9979    -0.0359     0.0747     0.3371
      INDA      india   753.0000    48.0100    -0.1317     0.1172    -1.0520    -0.0434    -0.0253    -0.0533    -0.1530    -0.2770    -0.0392     0.1252      False     0.1516    -0.0542     2.7978    -0.0539     0.1845     0.3328
       LIT    lithium   753.0000    70.9000    -0.2228     0.2629    -0.8198    -0.0456    -0.0199    -0.1747    -0.1338     0.2088    -0.0452     0.2718      False     0.2867    -0.1177     2.4361    -0.0587     0.0850     0.3919
       IGF grid/infra   753.0000    63.6000    -0.0703     0.0218    -0.7578    -0.0227    -0.0339    -0.0679    -0.1901    -0.0886    -0.0182     0.0927      False     0.0756    -0.0402     1.8823    -0.0096     0.2490     0.4112
      PAVE grid/infra   753.0000    52.9100    -0.1165     0.0858    -0.6005    -0.0205    -0.0588    -0.1177    -0.1056    -0.0202    -0.0252     0.1940      False     0.1318    -0.0840     1.5695    -0.0030     0.1191     0.5767
      GRID grid/infra   753.0000   176.8400    -0.1113     0.0450    -0.4219     0.0106    -0.0202    -0.1025    -0.0928     0.0307     0.0075     0.2639       True     0.1253    -0.1143     1.0963    -0.0527     0.0875     0.7349
      BOTZ   ai/robot   753.0000    35.1150    -0.1561     0.0640    -0.5960    -0.0483    -0.0180    -0.0972    -0.1510    -0.1443    -0.0021     0.2619      False     0.1849    -0.1134     1.6310    -0.0409     0.0882     0.4633
      ARKQ   ai/robot   753.0000   122.5200    -0.1481     0.1199    -0.4669    -0.0120     0.0066    -0.0997    -0.1291     0.0135     0.0190     0.3172       True     0.1738    -0.1374     1.2656    -0.1058     0.0728     0.6221
      AIPO   ai/robot   289.0000    28.2000    -0.1890     0.0370    -0.4625     0.0112    -0.0369    -0.1700    -0.0618     0.1443     0.0115     0.4085       True     0.2330    -0.1769     1.3170    -0.0674     0.0565     0.7353
      ROBO   ai/robot   753.0000    78.6300    -0.1296     0.0681    -0.4679     0.0116    -0.0236    -0.0949    -0.0477     0.0372    -0.0029     0.2770      False     0.1489    -0.1200     1.2415    -0.0365     0.0834     0.7356
       BAI   ai/robot   477.0000    44.2700    -0.1837     0.1550    -0.3497     0.0934     0.0027    -0.1530     0.1342     0.1378     0.0317     0.5251       True     0.2250    -0.2274     0.9894    -0.1529     0.0440     0.8939
      QTUM   ai/robot   753.0000   146.7500    -0.1290     0.0736    -0.3723     0.1097    -0.0054    -0.1270     0.1698     0.3029     0.0140     0.3464       True     0.1481    -0.1500     0.9871    -0.0989     0.0667     0.9073
```

## B. Leaders (where money went) — rs_spy_3m leaders
```
         ETF        theme    rs_spy_3m    rs_spy_6m   rs_spy_12m       dd_52w    dd_pctile
        ARKG      biotech        0.441        0.799        0.775        0.000        1.000
        ETHA  crypto-spot        0.381       -0.040       -0.625       -0.484        0.362
        WCLD     software        0.354        0.283       -0.021       -0.048        0.805
         USO      oil/gas        0.328        0.117        0.884       -0.041        0.881
         BUG        cyber        0.315        0.570        0.159        0.000        1.000
        HACK        cyber        0.231        0.383        0.236       -0.012        0.745
        SKYY     software        0.214        0.292        0.052       -0.027        0.657
         XOP      oil/gas        0.211       -0.038        0.309       -0.036        0.857
        CIBR        cyber        0.176        0.410        0.186       -0.005        0.815
         IBB      biotech        0.162        0.105        0.304       -0.045        0.458
```
## C. First-pass memo — one search per theme, provisional buckets, UNVERIFIED. Challenge it.

# etf-dip-pick quick pass 2026-09-18

Regime: The hawkish-Fed repricing is still the tape. The Sept 16–17 FOMC decision kept guidance
for at least one more 2026 hike; the 10y sits near 5% (19-year highs in the long bond), the dollar is
strong, and Brent is ~$108 on Hormuz/Yanbu supply disruption — punishing every rate-sensitive and
commodity theme at once (silver −44%, nuclear −31–39%, solar −37%, utilities, housing, clean).
Money rotates into biotech (ARKG +44% vs SPY 3m, sitting at its 52w high — the cleanest leadership
on the board), crypto-spot (ETHA +38% but still −48% off its high), software (WCLD +35%), cyber,
and oil/gas. One new wrinkle today: gold and silver are bouncing (MCX metals up ~1%, spot silver
recovering as the dollar and yields eased post-decision) — the question is whether the rate
repricing is peaking. This is a growth-rotation tape, not a broad crash: the SPY gate kept the
dip list honest, and the dips are the mirror of the leaders.

Provisional buckets — rotation (thesis intact, sellers are macro tourists) / break (thesis changed)
/ unclear (needs the panel):

| # | ETF | theme | dd_52w | vs_sma200 | rs_spy_3m | stab | bucket | why (1 line) |
|---|-----|-------|--------|-----------|-----------|------|--------|--------------|
| 1 | KWEB | china | -40% | -18% | -7% | no | unclear | Consumption/property bust killing internet ad revenues (Morningstar 9/11); Star-50 tech is up 30% while KWEB down 30% — internet-specific weakness, profits OK but confidence gone; flows deeply negative ($819M 3m outflow) |
| 2 | FXI | china | -17% | -6% | -2% | no | unclear | Same tape, shallower; large-cap SOE tilt cushions the internet hit |
| 3 | REMX | rare-earth | -37% | -20% | -31% | no | unclear | No thesis-break found; globally diversified (~30% China, 24% Australia, 18% US); low short interest, institutional buyers outnumber sellers 96:27 — a commodities-rotation casualty so far |
| 4 | TAN | solar | -37% | -16% | -24% | no | **break** | Accelerated US clean-energy tax-credit phaseouts plus acute rate sensitivity — policy and rates both against it |
| 5 | URNM | nuclear | -39% | -16% | -13% | no | rotation | Uranium equities −35–39% off highs while long-term uranium price is $97/lb and still rising m/m (Sept 16) — miner/fund disconnect, not a uranium break; AI-power-demand story intact |
| 6 | NLR | nuclear | -33% | -15% | -14% | no | rotation | Same disconnect, broader basket (miners + reactors + utilities), dividend 2.7% — best structure of the three |
| 7 | URA | nuclear | -31% | -12% | -13% | no | rotation | Same trade, most liquid ($5.8B), 22% Cameco + 14% Oklo concentration; +3.2% on Sept 17 — first of the three showing life |
| 8 | SLV | silver | -44% | -10% | -6% | no | rotation | Post-decision bounce underway (+1.2% today as dollar/yields ease); gold-silver ratio >63:1 says silver is the laggard of the pair — deepest dip, highest bounce potential, structurally oversold vs gold |
| 9 | UFO | space | -36% | -7% | -18% | **yes** | unclear | Post-SpaceX-IPO valuation reset: worst month in 6 years in June, lockups expiring in tranches Aug–Dec; now stabilizing; Starship Flight 14 target Sept 22 could re-rate sentiment |
| 10 | ARKX | space | -14% | +0% | -10% | **yes** | unclear | Same theme reset, shallower, above its 200d; SpaceX 7.2% weight + Rocket Lab 6.8% — the cleaner vehicle if the reset was overdone |
| 11 | PBW | clean | -34% | -11% | -26% | no | **break** | Same subsidy phaseouts as TAN; junky basket (47% micro-cap, beta 1.8) — worst structure in the clean group |
| 12 | ICLN | clean | -25% | -5% | -17% | **yes** | **break** | Stabilizing but thesis is the subsidy regime; lowest fee (0.39%) of the three yet still policy-broken |
| 13 | QCLN | clean | -30% | -8% | -24% | no | **break** | Same subsidy overhang, most expensive of the clean three (0.59%) |
| 14 | SHLD | defense-us | -19% | -7% | -4% | no | rotation | No thesis change: Pentagon missile-stockpile push (Zacks, Aug 12), Zacks Buy ranks on ITA/PPA; sector de-rating is flow rotation into software/biotech |
| 15 | XAR | defense-us | -19% | -10% | -19% | no | rotation | Same; equal-weight small/mid defense — the deeper of the drawdowns, same catalyst |
| 16 | ITA | defense-us | -15% | -7% | -15% | no | rotation | Concentrated primes (GE 21%, RTX 17%); cheapest fee (0.38%); rotation not demand loss |
| 17 | PPA | defense-us | -14% | -6% | -13% | no | rotation | Broader 62-holding basket; same flows, mildest drawdown in the group |
| 18 | XLU | utilities | -11% | -6% | -9% | no | rotation | Classic bond-proxy repricing: yields at 19-year highs kill dividends' appeal; flashing oversold (Seeking Alpha, Sept 6); AI data-center power demand is the structural offset |
| 19 | GLD | gold | -20% | -4% | -1% | no | rotation | Bouncing with silver post-decision; central-bank buying + Treasury buybacks support; UBS $6,200 Mar–Sep 2026 target (+27%) — rate-driven correction in a structurally supported asset |
| 20 | XHB | housing | -20% | -9% | -13% | no | unclear | Mortgage-rate vise (Zacks Sell rank); equal-weight incl. building products — rate-driven, but builder confidence is genuinely falling |
| 21 | ITB | housing | -21% | -9% | -10% | no | unclear | Cap-weighted pure builders; same rate headwind, deeper drawdown history is worse (dd_pctile 0.21) |
| 22 | INDA | india | -13% | -4% | -5% | no | rotation | External, not domestic: Brent $108 + Fed-hike fears hammer EM; Nifty at 5-month low on oil, domestic growth data still robust — textbook macro-tourist selloff |
| 23 | LIT | lithium | -22% | -5% | -17% | no | unclear | Lithium carbonate $22.30/kg (+59% vs 2024 avg); JPM upgraded Lithium Americas Sept 9 on deficits "through end of decade" — yet stocks can't rally: expectation-sensitivity (Albemarle −3.5% Sept 17) says demand-doubt isn't gone |
| 24 | IGF | grid/infra | -7% | -2% | -7% | no | rotation | Shallowest dip on the board (dd_pctile 0.02 = actually extreme for it); global infra compounding at 9.5% YTD; pure rotation |
| 25 | PAVE | grid/infra | -12% | -2% | -12% | no | rotation | US infra capex story intact; −12% is noise against the AI-grid capex wave |
| 26 | GRID | grid/infra | -11% | +1% | -10% | **yes** | rotation | Already above its 200d and green on the 10d; record inflows, Zacks Buy; the electricity-demand theme the user already likes — dip is the tape, not the thesis |
| 27 | BOTZ | ai/robot | -16% | -5% | -10% | no | rotation | Caught in the Sept 15 AI-selloff washout (SOXX −5.1% on coordinated-slowdown calls); industrial-automation basket, not the speculative quantum cohort |
| 28 | ARKQ | ai/robot | -15% | -1% | -10% | **yes** | rotation | Active ARK basket, stabilizing; Tesla/Robotics/energy-storage mix |
| 29 | AIPO | ai/robot | -19% | +1% | -17% | **yes** | rotation | Only 289 days of history — above its 200d-equivalent and bouncing; young-fund noise |
| 30 | ROBO | ai/robot | -13% | +1% | -9% | no | rotation | Shallow, above 200d; theme rotation, not thesis damage |
| 31 | BAI | ai/robot | -18% | +9% | -15% | **yes** | unclear | +13% vs SPY over 6m and well above its 200d — barely a dip; strong momentum may mean it's the wrong vehicle for a dip-buy |
| 32 | QTUM | ai/robot | -13% | +11% | -13% | **yes** | unclear | Same: +17% 6m vs SPY, above 200d — quantum names are −54–73% off highs individually (IonQ, D-Wave), so the ETF's mildness is diversification, not safety |

Rotation clusters: (a) hawkish-Fed rate repricing → utilities, housing, silver, gold, nuclear miners, defense;
(b) post-SpaceX-IPO reset → space; (c) subsidy repeal → solar/clean (the only true breaks);
(d) oil + EM risk-off → india; (e) AI-rotation into software → ai/robot hardware, china internet.
Lone-wolf watch: KWEB/FXI's China-internet-specific weakness has a property/demand component the
rest of the board doesn't share — the panel should test whether that's demand-collapse (break)
or confidence (rotation).
