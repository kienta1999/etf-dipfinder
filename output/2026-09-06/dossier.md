# Dossier — ETF dip candidates, scan date 2026-09-05

## A. Scan numbers (deterministic; dip_score 0 = most beaten up on depth + rel weakness + trend)
dd_52w = % off 52w high; dd_z = dd / 60d annualised vol; dd_pctile = share of this ETF's own 3y drawdown history
that is shallower than today (0.02 = worst 2% of its own history); vs_sma200/50 = % vs moving avg; rs_spy_Nm = return
minus SPY over N months; ret_10d = 10-day return; stabilizing = ret_10d > 0; days < 250 = young ETF, stats since inception.

```
            theme    days  dd_52w   dd_z  dd_pctile  vs_sma200  vs_sma50  rs_spy_3m  rs_spy_6m  rs_spy_12m  ret_10d  vol_60d  stabilizing  dip_score
KWEB      country 754.000  -0.356 -1.397      0.026     -0.135    -0.025     -0.059     -0.275      -0.471   -0.023    0.255        False      0.057
SLV   gold/silver 754.000  -0.433 -1.024      0.064     -0.084     0.068     -0.075     -0.364       0.420   -0.046    0.423        False      0.057
TAN         clean 754.000  -0.350 -0.915      0.083     -0.128    -0.077     -0.297     -0.250      -0.056   -0.026    0.383        False      0.106
REMX       metals 754.000  -0.309 -0.689      0.231     -0.121    -0.008     -0.193     -0.334       0.097   -0.063    0.449        False      0.130
SHLD      defense 747.000  -0.190 -0.695      0.040     -0.073    -0.022     -0.045     -0.334      -0.177   -0.061    0.274        False      0.154
NLR       nuclear 754.000  -0.270 -0.683      0.073     -0.082     0.050     -0.065     -0.270      -0.160    0.000    0.395         True      0.187
URNM      nuclear 754.000  -0.321 -0.701      0.177     -0.059     0.072     -0.015     -0.259      -0.045   -0.019    0.457        False      0.187
UFO         space 754.000  -0.355 -0.892      0.014     -0.060    -0.049     -0.247     -0.169       0.122   -0.048    0.398        False      0.236
GLD   gold/silver 754.000  -0.180 -0.698      0.078     -0.021     0.046     -0.020     -0.292       0.045   -0.039    0.258        False      0.260
PBW         clean 754.000  -0.320 -0.729      0.332     -0.082    -0.061     -0.263     -0.114       0.096   -0.045    0.438        False      0.293
ICLN        clean 754.000  -0.250 -0.769      0.048     -0.049    -0.029     -0.211     -0.129       0.053    0.010    0.325         True      0.301
XAR       defense 754.000  -0.148 -0.487      0.009     -0.050    -0.073     -0.119     -0.245      -0.021   -0.073    0.303        False      0.317
ITB       housing 754.000  -0.193 -0.591      0.274     -0.045    -0.041     -0.034     -0.194      -0.372   -0.037    0.327        False      0.350
XLU        sector 754.000  -0.085 -0.594      0.040     -0.027    -0.031     -0.069     -0.217      -0.142    0.007    0.144         True      0.358
URA       nuclear 754.000  -0.255 -0.569      0.136     -0.044     0.070     -0.030     -0.207      -0.005   -0.000    0.448        False      0.358
```

## B. Leaders (where money went)
```
            theme  rs_spy_3m  rs_spy_6m  dd_52w
ETHA       crypto      0.513      0.089  -0.482
ARKG      biotech      0.364      0.525  -0.058
IBIT       crypto      0.278      0.020  -0.365
GDXJ  gold/silver      0.236     -0.204  -0.174
XBI       biotech      0.227      0.171  -0.034
WCLD     software      0.218      0.217  -0.056
GDX   gold/silver      0.212     -0.172  -0.143
IBB       biotech      0.211      0.114  -0.023
```

## C. First-pass memo from a prior single-agent run (same scan date). Starting point only — its buckets and
"why" lines came from ONE web search per ETF and are NOT verified. Challenge them.

# dipfind 2026-09-05

Regime: This is a **rate-hike scare**, not a growth scare. The 10y hit 4.82% (highest since Nov 2023),
Warsh says the Fed has "work to do" on inflation, and FedWatch puts ~66% odds on a September *hike* —
so every long-duration and rate-sensitive theme is in the dip list at once (gold, silver, utilities,
homebuilders, clean energy, nuclear, space). Layered on top: the AI-physical trade is unwinding, which
is why uranium/space/utilities/defense all sit together.

Money went to biotech (ARKG +36%, XBI +23%, IBB +21% vs SPY 3m — the cleanest leadership, small
drawdowns, real rotation out of AI), crypto (BTC ~$81k, +25% off mid-Aug on SEC Reg Crypto Assets —
but ETHA/IBIT still carry −48%/−37% drawdowns, so that's a bounce off a crash, not leadership), and
gold *miners* (GDX/GDXJ +21/+24% while GLD/SLV are in the dip list). That miner-vs-metal divergence is
the single most useful tell on the board: it says precious-metals weakness is rates and dollar, not a
broken gold thesis.

| # | ETF | theme | dd_52w | vs_sma200 | rs_spy_3m | stab | bucket | why (1 line) |
|---|-----|-------|--------|-----------|-----------|------|--------|--------------|
| 1 | KWEB | china | -36% | -13% | -6% | no | unclear | Alibaba HK$80bn placement + 4 straight EPS misses + AI capex crushing EBITDA — more than flows, but no policy break |
| 2 | SLV | silver | -43% | -8% | -8% | no | rotation | Halved from the Jan $121 blowoff; rate-hike bets + strong dollar, industrial/monetary thesis untouched |
| 3 | TAN | solar | -35% | -13% | -30% | no | **break** | OBBBA phases out 45Y/48E for construction after Jul 4 2026, 25D expired, FEOC cuts off Chinese supply — policy, not flows |
| 4 | REMX | metals | -31% | -12% | -19% | no | unclear | Half the fund is really lithium (oversupplied); the rare-earth half is fine on defense demand — two theses in one ticker |
| 5 | SHLD | defense | -19% | -7% | -5% | no | rotation | Rotation *within* defense: European primes cooling after a violent repricing while XAR's US mid-caps took the FY27 munitions/space budget |
| 6 | NLR | nuclear | -27% | -8% | -7% | **yes** | rotation | Uranium equities −30% off highs while AI datacenter load, SMR announcements and term uranium prices all still point up |
| 7 | URNM | nuclear | -32% | -6% | -2% | no | rotation | Same trade, more concentrated (Cameco 21% + SPUT 14% + NexGen 13%); rs_3m already back to flat |
| 8 | UFO | space | -36% | -6% | -25% | no | **break** | SpaceX listed Jun 12 and took the scarcity premium with it, then converts/ATMs/insider sales flooded supply — that multiple doesn't come back |
| 9 | GLD | gold | -18% | -2% | -2% | no | rotation | Bond selloff and hike odds; miners leading the metal is the classic bottoming shape |
| 10 | PBW | clean | -32% | -8% | -26% | no | **break** | Same OBBBA repeal as TAN, worse quality holdings |
| 11 | ICLN | clean | -25% | -5% | -21% | **yes** | rotation | Global/utility-scale mix, far less exposed to the US residential credit repeal than TAN/PBW — caught in the same tape |
| 12 | XAR | defense | -15% | -5% | -12% | no | rotation | Up ~20% YTD and resting; the FY27 request put $53bn into munitions and $60bn into space |
| 13 | ITB | housing | -19% | -5% | -3% | no | rotation | Pure mortgage-rate math; order books growing, margins defended with incentives |
| 14 | XLU | utilities | -9% | -3% | -7% | **yes** | rotation | Yields, plus the AI-power premium deflating; the "safe" sector is now a risk canary |

Note on confidence: KWEB (dd_pctile 0.026), UFO (0.014), XAR (0.010), SHLD (0.040), XLU (0.039) and
ICLN (0.048) are all in the worst decile of their *own* 3-year drawdown history — real events, not
noise. PBW (0.332) and ITB (0.273) are only having an ordinary bad patch by their own standards.

Buy candidates (rotation + stabilizing): **NLR**, **ICLN**, **XLU**. Thin list, and all three are
rate-sensitive — see the caveat below.

Watch (rotation, still falling): URNM/URA, GLD, SLV, SHLD, XAR, ITB. The uranium pair is the best
setup on the board — deepest thesis/price gap — but it hasn't turned yet.

Avoid (break): **TAN**, **PBW** (policy repeal needs a policy reversal), **UFO** (permanent re-rating).

Unclear, needs a second look: KWEB (is the AI-capex margin hit temporary like the US hyperscalers, or
structural?), REMX (lithium vs rare earths pull opposite directions).

Caveat: in a *hiking* regime, a rate-driven "rotation" dip can keep going for a long time. Everything
in the buy/watch lists here is levered to the same 10y yield. If the September meeting hikes, this
whole list gets cheaper before it gets better.

