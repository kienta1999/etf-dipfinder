# Dossier — ETF dip candidates, scan date 2026-09-17

## A. Scan numbers (deterministic; dip_score 0 = most beaten up on depth + rel weakness + trend)
dd_52w = % off 52w high; dd_z = dd / 60d annualised vol; dd_pctile = share of this ETF's own 3y drawdown history
that is shallower than today (0.02 = worst 2% of its own history); vs_sma200/50 = % vs moving avg; rs_spy_Nm = return
minus SPY over N months; ret_10d = 10-day return; stabilizing = ret_10d > 0; days < 250 = young ETF, stats since inception.

```
             theme    days  dd_52w   dd_z  dd_pctile  vs_sma200  vs_sma50  rs_spy_3m  rs_spy_6m  rs_spy_12m  ret_10d  vol_60d  stabilizing  dip_score
KWEB       china   753.000  -0.397 -1.560      0.008     -0.178    -0.084     -0.071     -0.331      -0.543   -0.051    0.255        False      0.053
FXI        china   753.000  -0.166 -0.933      0.087     -0.058    -0.027     -0.016     -0.208      -0.320   -0.038    0.178        False      0.246
REMX  rare-earth   753.000  -0.369 -0.918      0.108     -0.198    -0.067     -0.312     -0.362      -0.007   -0.094    0.402        False      0.059
TAN        solar   753.000  -0.373 -1.046      0.044     -0.158    -0.080     -0.239     -0.340      -0.082   -0.019    0.356        False      0.073
URNM     nuclear   753.000  -0.389 -0.871      0.082     -0.155    -0.038     -0.133     -0.339      -0.205   -0.066    0.447        False      0.106
NLR      nuclear   753.000  -0.327 -0.808      0.022     -0.152    -0.031     -0.145     -0.345      -0.276   -0.055    0.405        False      0.125
URA      nuclear   753.000  -0.310 -0.708      0.044     -0.116    -0.011     -0.126     -0.289      -0.160   -0.037    0.437        False      0.224
SLV       silver   753.000  -0.442 -1.101      0.063     -0.103     0.040     -0.059     -0.301       0.360   -0.002    0.401        False      0.120
UFO        space   753.000  -0.355 -1.109      0.020     -0.070    -0.029     -0.176     -0.198       0.106    0.012    0.320         True      0.206
ARKX       space   753.000  -0.144 -0.504      0.098     0.002     0.003     -0.096     -0.126       0.039    0.014    0.286         True      0.649
PBW        clean   753.000  -0.342 -0.836      0.180     -0.113    -0.064     -0.258     -0.193       0.010   -0.021    0.409        False      0.219
ICLN       clean   753.000  -0.252 -0.842      0.044     -0.055    -0.014     -0.166     -0.191       0.035    0.021    0.299         True      0.299
QCLN       clean   753.000  -0.298 -0.708      0.034     -0.079    -0.053     -0.244     -0.144       0.047   -0.008    0.420        False      0.371
SHLD  defense-us   753.000  -0.190 -0.778      0.050     -0.073    -0.024     -0.042     -0.328      -0.219   -0.002    0.244        False      0.225
XAR   defense-us   753.000  -0.187 -0.699      0.004     -0.097    -0.096     -0.187     -0.268      -0.090   -0.036    0.267        False      0.257
ITA   defense-us   753.000  -0.154 -0.726      0.003     -0.069    -0.092     -0.150     -0.233      -0.106   -0.041    0.213        False      0.298
PPA   defense-us   753.000  -0.137 -0.677      0.008     -0.064    -0.072     -0.131     -0.242      -0.100   -0.022    0.202        False      0.337
XLU    utilities   753.000  -0.115 -0.789      0.004     -0.058    -0.050     -0.088     -0.255      -0.150   -0.023    0.146        False      0.285
GLD         gold   753.000  -0.197 -0.796      0.067     -0.043     0.015     -0.007     -0.263       0.005   -0.011    0.247        False      0.318
XHB      housing   753.000  -0.197 -0.709      0.121     -0.088    -0.080     -0.126     -0.180      -0.318   -0.041    0.277        False      0.324
ITB      housing   753.000  -0.211 -0.683      0.210     -0.088    -0.069     -0.100     -0.180      -0.364   -0.038    0.309        False      0.337
INDA       india   753.000  -0.132 -1.052      0.117     -0.043    -0.025     -0.053     -0.153      -0.277   -0.039    0.125        False      0.333
LIT      lithium   753.000  -0.223 -0.820      0.263     -0.046    -0.020     -0.175     -0.134       0.209   -0.045    0.272        False      0.392
IGF   grid/infra   753.000  -0.070 -0.758      0.022     -0.023    -0.034     -0.068     -0.190      -0.089   -0.018    0.093        False      0.411
PAVE  grid/infra   753.000  -0.117 -0.601      0.086     -0.021    -0.059     -0.118     -0.106      -0.020   -0.025    0.194        False      0.577
GRID  grid/infra   753.000  -0.111 -0.422      0.045     0.011    -0.020     -0.103     -0.093       0.031    0.008    0.264         True      0.735
BOTZ    ai/robot   753.000  -0.156 -0.596      0.064     -0.048    -0.018     -0.097     -0.151      -0.144   -0.002    0.262        False      0.463
ARKQ    ai/robot   753.000  -0.148 -0.467      0.120     -0.012     0.007     -0.100     -0.129       0.014    0.019    0.317         True      0.622
AIPO    ai/robot   289.000  -0.189 -0.463      0.037     0.011    -0.037     -0.170     -0.062       0.144    0.012    0.409         True      0.735
ROBO    ai/robot   753.000  -0.130 -0.467      0.068     0.012    -0.024     -0.095     -0.048       0.037    -0.003    0.277        False      0.736
BAI     ai/robot   477.000  -0.184 -0.350      0.155     0.093     0.003     -0.153     0.134       0.138    0.032    0.525        False      0.894
QTUM    ai/robot   753.000  -0.129 -0.372      0.074     0.110    -0.005     -0.127     0.170       0.303    0.014    0.346         True      0.907
```

## B. Leaders (where money went)
```
             theme  rs_spy_3m  rs_spy_6m  rs_spy_12m  dd_52w  dd_pctile
ARKG     biotech      0.441      0.799      0.775    0.000     1.000
ETHA  crypto-spot      0.381     -0.040     -0.625   -0.484     0.362
WCLD    software      0.354      0.283     -0.021   -0.048     0.805
USO      oil/gas      0.328      0.117      0.884   -0.041     0.882
BUG        cyber      0.315      0.570      0.159    0.000     1.000
HACK       cyber      0.231      0.383      0.237   -0.012     0.745
SKYY    software      0.214      0.292      0.052   -0.027     0.657
XOP      oil/gas      0.211     -0.038      0.309   -0.036     0.857
```

## C. First-pass memo — one search per theme, provisional buckets, UNVERIFIED. Challenge it.

# dipfind 2026-09-17

Regime: The hawkish-Fed repricing keeps running — higher real yields and a stronger dollar are
pressuring every rate-sensitive and commodity theme at once (silver −44%, nuclear, solar, clean,
utilities, housing), while money rotates into biotech (ARKG +44% vs SPY 3m, at its 52w high — the
cleanest leadership on the board), a crypto-spot bounce (ETHA +38% but still −48% off its high),
software (WCLD +35%), cyber, and oil/gas. This is a growth-rotation tape, not a broad crash: the SPY
gate kept the dip list honest, and the dips are the mirror of the leaders.

| # | ETF | theme | dd_52w | vs_sma200 | rs_spy_3m | stab | bucket | why (1 line) |
|---|-----|-------|--------|-----------|-----------|------|--------|--------------|
| 1 | KWEB | china | -40% | -18% | -7% | no | unclear | Alibaba's Aug 24 share placement added supply; weak domestic demand/property is hitting internet ad/consumption — profits strong, investor confidence weak |
| 2 | FXI | china | -17% | -6% | -2% | no | unclear | Same tape as KWEB, shallower; large-cap SOE tilt cushions the internet-specific hit |
| 3 | REMX | rare-earth | -37% | -20% | -31% | no | unclear | Very large correction with no clear thesis-break found; holdings globally diversified (~30% China exposure per 2026-08-31) |
| 4 | TAN | solar | -37% | -16% | -24% | no | **break** | Rate sensitivity plus accelerated US clean-energy tax-credit phaseouts — direct policy headwind, not flows |
| 5 | URNM | nuclear | -39% | -16% | -13% | no | rotation | Uranium equities −35-39% off highs while uranium ~$97/lb — a miner/fundamental disconnect, not a uranium break |
| 6 | NLR | nuclear | -33% | -15% | -14% | no | rotation | Same disconnect, broader basket; hasn't turned yet |
| 7 | URA | nuclear | -31% | -12% | -13% | no | rotation | Same trade, most liquid of the three; hasn't turned yet |
| 8 | SLV | silver | -44% | -10% | -6% | no | rotation | Hawkish repricing + higher yields + stronger dollar + crowded positioning/leverage and margin changes; structural supply-deficit thesis intact — deepest dip, highest risk |
| 9 | UFO | space | -36% | -7% | -18% | **yes** | unclear | Post-SpaceX-IPO valuation reset, lockup expirations, dilution risk, long-duration capital needs; commercial/NASA/national-security demand remains |
| 10 | ARKX | space | -14% | +0% | -10% | **yes** | unclear | Same theme reset, shallower, still above its 200d; the cleaner space vehicle if the reset is overdone |
| 11 | PBW | clean | -34% | -11% | -26% | no | **break** | Same accelerated subsidy/tax-credit phaseouts as TAN; worse-quality holdings |
| 12 | ICLN | clean | -25% | -5% | -17% | **yes** | unclear | Global/utility-scale mix, less exposed to the US credit repeal than TAN/PBW, but the policy tape is the same — stabilizing is the only green shoot |
| 13 | QCLN | clean | -30% | -8% | -24% | no | **break** | Same policy headwind as TAN/PBW, no offsetting green shoot |
| 14 | SHLD | defense-us | -19% | -7% | -4% | no | rotation | No thesis break found; global defense spending and geopolitical demand strong — resting after earlier gains |
| 15 | XAR | defense-us | -19% | -10% | -19% | no | rotation | Same, deepest of the four and in the worst 1% of its own 3y history — real event, same intact demand |
| 16 | ITA | defense-us | -15% | -7% | -15% | no | rotation | Same tape; worst 0.3% of its own history |
| 17 | PPA | defense-us | -14% | -6% | -13% | no | rotation | Same tape; worst 0.8% of its own history |
| 18 | XLU | utilities | -11% | -6% | -9% | no | rotation | Rising Treasury yields cut dividend appeal and raised financing costs; recovery needs yield stabilization |
| 19 | GLD | gold | -20% | -4% | -1% | no | rotation | Hawkish expectations + higher real yields + stronger USD; central-bank buying and fiscal/debt concerns still support the long case |
| 20 | XHB | housing | -20% | -9% | -13% | no | unclear | Mortgage rates, affordability, muted demand — rate math, not clearly a permanent break |
| 21 | ITB | housing | -21% | -9% | -10% | no | unclear | Same rate math; homebuilder order books were the offset in prior runs — needs a verifier look |
| 22 | INDA | india | -13% | -4% | -5% | no | rotation | Higher oil, Fed caution, high global rates, foreign institutional outflows — no permanent fundamental break established |
| 23 | LIT | lithium | -22% | -5% | -17% | no | unclear | Tariff uncertainty, inflation/rate concerns, possibly slowing manufacturing demand; recovery evidence mixed |
| 24 | IGF | grid/infra | -7% | -2% | -7% | no | rotation | Shallowest dip on the board; correction after strong gains, electrification/data-center/grid-upgrade thesis intact |
| 25 | PAVE | grid/infra | -12% | -2% | -12% | no | rotation | Same rotation, deeper than IGF |
| 26 | GRID | grid/infra | -11% | +1% | -10% | **yes** | rotation | Same rotation, above its 200d and stabilizing, with reported inflows — the green shoot of the theme |
| 27 | BOTZ | ai/robot | -16% | -5% | -10% | no | unclear | AI-slowdown fears plus a reported $187M one-day outflow; basket-concentration concerns on top |
| 28 | ARKQ | ai/robot | -15% | -1% | -10% | **yes** | unclear | Same sentiment hit, stabilizing, broader ARK active basket |
| 29 | AIPO | ai/robot | -19% | +1% | -17% | **yes** | unclear | Young ETF (289d), IPO-flavored AI basket, stabilizing above its 200d |
| 30 | ROBO | ai/robot | -13% | +1% | -9% | no | unclear | Shallowest of the theme, above its 200d, diversified robotics basket |
| 31 | BAI | ai/robot | -18% | +9% | -15% | **yes** | unclear | Above its 200d (+9%), rs_spy_6m/12m still positive, stabilizing per scan — lagging only on the 3m window |
| 32 | QTUM | ai/robot | -13% | +11% | -13% | **yes** | unclear | Above its 200d (+11%), rs_spy_12m +30%; this "dip" is mostly 3m relative weakness — needs the cause lens to justify inclusion |

Note on confidence: KWEB (dd_pctile 0.008), XAR (0.004), ITA (0.003), PPA (0.008) and XLU (0.004)
are all in the worst 1% of their *own* 3-year drawdown history — real events, not noise. UFO (0.020),
NLR (0.022), IGF (0.022), AIPO (0.037), TAN (0.044), URA (0.044), ICLN (0.044), GRID (0.045),
SHLD (0.050), SLV (0.063), BOTZ (0.064), GLD (0.067), ROBO (0.068), QTUM (0.074), URNM (0.082),
FXI (0.087), PAVE (0.086), ARKX (0.098) are in the worst decile. LIT (0.263), ITB (0.210),
BAI (0.155), XHB (0.121) and INDA (0.117) are only having an ordinary bad patch by their own
standards. BAI (477d) and AIPO (289d) are young; treat their percentiles and SMA stats lightly.

Buy candidates (rotation + stabilizing): **GRID** — the only rotation-bucket theme with a
stabilizing, above-200d fund and reported inflows. Thin, single-name list.

Watch (rotation, still falling): URNM/NLR/URA, SLV, GLD, SHLD/XAR/ITA/PPA, XLU, INDA, IGF/PAVE.
Nuclear is the deepest thesis/price gap on the board but hasn't turned; SLV is the deepest dip
but the highest risk (leverage/margin unwind can overshoot).

Avoid (break): **TAN**, **PBW**, **QCLN** (policy repeal needs a policy reversal).

Unclear, needs the panel: China (supply + demand, profits vs confidence), REMX (no break found but
−37% needs a cause), space (valuation reset vs demand), ICLN (policy tape vs global mix), housing
(rate math vs permanence), LIT (tariffs vs demand), all of ai/robot (sentiment vs concentration).

Caveat: this is a *hiking/strong-dollar* regime tape. A rate-driven "rotation" dip can keep falling
for a long time — every rotation name here is levered to the same 10y yield and the dollar. If
yields keep rising, this whole list gets cheaper before it gets better. And the one fresh crack in
the tape is ai/robot: the BOTZ outflow + AI-slowdown chatter is the first sentiment break in the
theme that powered 2025 — watch whether it spreads to software (WCLD is currently a *leader*).
