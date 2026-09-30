# ETF dip panel — dossier for RUN_DATE 2026-09-30

Scan asof: 2026-09-29 close (3 years of daily bars, days=751). 26 candidates in 15 themes.
BJK (steel/coal) dropped — delisted. GLD theme exited (GDX is now a LEADER, not a dip).
ARGT (argentina) newly entered. GRID and SHLD remain candidates.

---

## A. Candidate scan rows (full `data/scan.csv` rows, 26 candidates)

```csv
ticker,theme,asof,days,price,dd_52w,dd_pctile,dd_z,vs_sma200,vs_sma50,rs_spy_3m,rs_spy_6m,rs_spy_12m,ret_10d,vol_60d,dollar_vol,tp_pct,sl_pct,dip_low_pct,rr,size_1pct,is_dip,stabilizing,dip_score,price_score,theme_score,is_candidate
REMX,rare-earth,2026-09-29,751.0,64.79,-0.4085,0.0205,-1.0039,-0.2465,-0.109,-0.2938,-0.4574,-0.1653,-0.0514,0.4069,38206633.3698,0.6905,-0.1762,-0.0049,3.9194,0.0568,True,False,0.062,5,0.062,True
TAN,solar,2026-09-29,751.0,43.43,-0.4126,0.0178,-1.1473,-0.2096,-0.1114,-0.2916,-0.3942,-0.1669,-0.0368,0.3596,33872713.578,0.7023,-0.1557,-0.0099,4.5102,0.0642,True,False,0.0623,6,0.0623,True
KWEB,china,2026-09-29,751.0,24.37,-0.3979,0.0082,-1.6406,-0.1675,-0.0744,-0.03,-0.3381,-0.5376,-0.0045,0.2425,337832571.6291,0.6608,-0.105,-0.0304,6.2925,0.0952,True,False,0.0816,5,0.0816,True
NLR,nuclear,2026-09-29,751.0,104.14,-0.3664,0.0041,-0.8822,-0.1954,-0.0854,-0.128,-0.3963,-0.3837,-0.0386,0.4154,38756687.6593,0.5784,-0.1799,-0.0138,3.2156,0.0556,True,False,0.118,5,0.118,True
URNM,nuclear,2026-09-29,751.0,48.25,-0.4255,0.0342,-0.9191,-0.2024,-0.0941,-0.1084,-0.3897,-0.3425,-0.0427,0.463,32100824.8953,0.7407,-0.2005,-0.0232,3.6946,0.0499,True,False,0.1181,5,0.118,True
URA,nuclear,2026-09-29,751.0,40.04,-0.3522,0.0164,-0.7767,-0.1682,-0.0755,-0.1096,-0.3313,-0.3006,-0.0414,0.4534,131180202.0924,0.5437,-0.1963,-0.0629,2.7691,0.0509,True,False,0.1804,6,0.118,True
XLU,utilities,2026-09-29,751.0,39.71,-0.1507,0.0055,-1.0877,-0.0938,-0.0715,-0.1436,-0.3387,-0.2262,-0.0319,0.1385,1016267275.2714,0.1774,-0.06,-0.0116,2.9576,0.1667,True,False,0.144,6,0.144,True
SHLD,defense-us,2026-09-29,751.0,60.45,-0.2227,0.0191,-1.0572,-0.11,-0.0662,-0.0135,-0.3275,-0.275,-0.0339,0.2107,101469340.317,0.2865,-0.0912,-0.0403,3.1409,0.1096,True,False,0.1501,6,0.1501,True
XAR,defense-us,2026-09-29,751.0,233.16,-0.2138,0.0014,-0.8131,-0.128,-0.1126,-0.2038,-0.2521,-0.1532,-0.0341,0.263,76358341.1137,0.272,-0.1139,0.0,2.3884,0.0878,True,False,0.2184,6,0.1501,True
ITA,defense-us,2026-09-29,751.0,209.3,-0.1725,0.0027,-0.828,-0.0903,-0.0983,-0.1615,-0.2206,-0.1471,-0.022,0.2083,181916328.9207,0.2084,-0.0902,-0.0002,2.3108,0.1109,True,False,0.2751,7,0.1501,True
PPA,defense-us,2026-09-29,751.0,155.94,-0.1564,0.0014,-0.8045,-0.0867,-0.0833,-0.1405,-0.2377,-0.1408,-0.0192,0.1943,46600099.8602,0.1853,-0.0842,0.0,2.2023,0.1188,True,False,0.2874,7,0.1501,True
UFO,space,2026-09-29,751.0,42.42,-0.3735,0.0014,-1.353,-0.1023,-0.0509,-0.1886,-0.2159,0.0469,-0.0109,0.2761,8191114.7717,0.5963,-0.1195,0.0,4.9877,0.0836,True,False,0.1884,8,0.1884,True
ARKX,space,2026-09-29,751.0,31.92,-0.1542,0.0792,-0.5658,-0.015,-0.0147,-0.0904,-0.075,-0.0214,0.013,0.2726,12454113.1619,0.1823,-0.118,-0.0752,1.5448,0.0847,True,True,0.7066,7,0.1884,True
PBW,clean,2026-09-29,751.0,29.12,-0.3711,0.0437,-0.9449,-0.1517,-0.0885,-0.2726,-0.2329,-0.1469,-0.0257,0.3927,9726533.1185,0.59,-0.17,-0.0052,3.4697,0.0588,True,False,0.2126,6,0.2126,True
ICLN,clean,2026-09-29,751.0,17.01,-0.2819,0.0068,-0.9926,-0.0944,-0.0417,-0.1957,-0.2413,-0.0371,-0.0247,0.284,127906811.0861,0.3925,-0.123,-0.0118,3.1921,0.0813,True,False,0.2128,7,0.2126,True
QCLN,clean,2026-09-29,751.0,48.59,-0.2903,0.041,-0.752,-0.0716,-0.0273,-0.2335,-0.1017,-0.0084,0.0297,0.3861,5133817.4543,0.4091,-0.1672,-0.0434,2.4472,0.0598,True,True,0.4695,8,0.2126,True
IGF,grid/infra,2026-09-29,751.0,61.86,-0.0957,0.0014,-1.17,-0.0508,-0.0503,-0.0971,-0.2716,-0.1224,-0.02,0.0818,53048648.7283,0.1058,-0.0354,0.0,2.988,0.2823,True,False,0.2385,7,0.2385,True
PAVE,grid/infra,2026-09-29,751.0,52.91,-0.1165,0.0874,-0.6665,-0.0243,-0.05,-0.1279,-0.1378,-0.0335,0.0013,0.1747,90585554.0172,0.1318,-0.0757,-0.003,1.7423,0.1322,True,True,0.5504,7,0.2385,True
GRID,grid/infra,2026-09-29,751.0,178.27,-0.1024,0.0628,-0.4107,0.0144,-0.009,-0.0944,-0.0773,0.0387,0.0339,0.2493,90616405.2909,0.1141,-0.1079,-0.0621,1.0568,0.0926,True,True,0.806,8,0.2385,True
LIT,lithium,2026-09-29,751.0,68.54,-0.2487,0.1243,-0.9489,-0.0807,-0.0511,-0.1503,-0.266,0.0754,-0.0211,0.2621,14446813.5669,0.331,-0.1135,-0.0263,2.9168,0.0881,True,False,0.2441,5,0.2441,True
INDA,india,2026-09-29,751.0,46.94,-0.151,0.0574,-1.1797,-0.0603,-0.0438,-0.0755,-0.1819,-0.2688,-0.0137,0.128,244183425.1792,0.1779,-0.0554,-0.0324,3.209,0.1804,True,False,0.3078,4,0.3078,True
ARGT,argentina,2026-09-29,751.0,86.11,-0.1605,0.0642,-0.747,-0.0679,-0.0778,-0.0827,-0.2453,0.0271,-0.0888,0.2148,13322271.5515,0.1911,-0.093,-0.0105,2.0548,0.1075,True,False,0.3372,6,0.3372,True
ITB,housing,2026-09-29,751.0,88.38,-0.2124,0.2104,-0.7351,-0.0855,-0.0584,-0.1728,-0.2018,-0.3293,-0.0083,0.289,205013586.2121,0.2697,-0.1251,-0.0341,2.1555,0.0799,True,False,0.381,3,0.381,True
XHB,housing,2026-09-29,751.0,96.97,-0.1929,0.1339,-0.7498,-0.0812,-0.061,-0.1821,-0.1935,-0.2784,-0.0025,0.2573,189284927.4622,0.239,-0.1114,-0.0286,2.1455,0.0898,True,False,0.3813,3,0.381,True
XME,base-metals,2026-09-29,751.0,103.9,-0.2167,0.0451,-0.5844,-0.0871,-0.0708,-0.0536,-0.2097,-0.0366,-0.05,0.3709,172351074.2518,0.2767,-0.1606,-0.0615,1.723,0.0623,True,False,0.4113,6,0.4113,True
XLY,discretionary,2026-09-29,751.0,109.15,-0.118,0.0847,-0.6054,-0.0596,-0.0456,-0.0932,-0.178,-0.249,-0.0134,0.1949,717517708.7352,0.1338,-0.0844,-0.036,1.5852,0.1185,True,False,0.4932,4,0.4932,True
```

### Column legend
| column | meaning |
|---|---|
| ticker | fund ticker (index of data/scan.csv) |
| theme | thematic/sector label |
| asof | scan close date |
| days | trading bars in lookback (751 = 3 years) |
| price | close price at scan asof |
| dd_52w | drawdown from 52-week high (negative = off high) |
| dd_pctile | percentile of drawdown across the fund universe (low = deep relative dip) |
| dd_z | z-score of drawdown |
| vs_sma200 / vs_sma50 | distance vs 200-day / 50-day SMA |
| rs_spy_3m / 6m / 12m | total-return ratio vs SPY over trailing 3 / 6 / 12 months (negative = lagging) |
| ret_10d | 10-day trailing return |
| vol_60d | 60-day annualized volatility |
| dollar_vol | 60-day average dollar volume |
| tp_pct / sl_pct | take-profit / stop-loss fractions vs current price (computed from dip structure) |
| dip_low_pct | dip-low fraction vs current price |
| rr | reward/risk ratio (tp_pct/sl_pct) |
| size_1pct | 1% risk position size (fraction of portfolio) |
| is_dip | dip-flag predicate (below 200-SMA or >=10% off 52w high AND lagging SPY 3m) |
| stabilizing | True when the dip shows stabilization (per scan rule) |
| dip_score / theme_score | deterministic dip/theme scores; candidates share the theme's top theme_score |
| price_score | mechanical price-structure score 1-8 (1=deep falling, 8=strong base) |
| is_candidate | in this run's scored candidate set (top themes' leaders) |

---

## B. Per-theme leaders (by theme_score)

Only the 15 candidate themes are scored by the panel; non-candidate themes (gold, semis, korea, staples, etc.) are not in the scored set.

| theme | leader(s) scored by the panel |
|---|---|
| rare-earth | REMX |
| solar | TAN |
| china | KWEB |
| nuclear | NLR / URNM / URA (three funds, one theme) |
| utilities | XLU |
| defense-us | SHLD / XAR / ITA / PPA (four funds, one theme) |
| space | UFO / ARKX (two funds, one theme) |
| clean | PBW / ICLN / QCLN (three funds, one theme) |
| grid/infra | IGF / PAVE / GRID (three funds, one theme) |
| lithium | LIT |
| india | INDA |
| argentina | ARGT |
| housing | ITB / XHB (two funds, one theme) |
| base-metals | XME |
| discretionary | XLY |

Notable vs 2026-09-29: GLD theme exited (GDX is now a LEADER, not a dip); ARGT (argentina) entered;
GRID and SHLD still in; BJK dropped (delisted).

---

## C. Quick-pass memo (ORCHESTRATOR — *unverified, challenge it*)

One web search per theme, 2026-09-30. Provisional buckets — the panel must verify or overturn them.

- **rare-earth (REMX): rotation** — summit hopes deflating the scarcity premium; the 11/10 deadline
  is the forcing function. The expiry dispute (11/10 snapback vs extension to 2027-01-10) is
  unresolved — see Disputed table below.
- **solar (TAN): rotation with rate headwind** — Fed hiked this week (first in 3 years), TAN at new
  52-week low $43.00; Solar IV duties on the calendar (10/14 USITC final injury vote, 11/2 Commerce
  final duty orders).
- **china (KWEB): break** — sanctions risk, US-China sentiment "Fear", ~$3B YTD outflows.
- **nuclear (NLR/URNM/URA): rotation** — uranium spot $89.70 (+4.3% YTD), term $96.50; selloff from
  AI-growth anxiety / policy trade while the commodity itself is rising.
- **utilities (XLU): rotation** — 10y at 5.28% (19-yr high), XLU at 17-mo low; rate-driven derating,
  data-center power thesis intact.
- **defense-us (SHLD/XAR/ITA/PPA): rotation** — record 6-7-week losing streak, bear market
  (-21% from Aug 14 high), war-premium deflation on peace headlines.
- **space (UFO/ARKX): rotation** — SpaceX IPO trade unwinding, valuation reset; Starship Flight 14
  success 9/28.
- **clean (PBW/ICLN/QCLN): break-ish / unclear** — rate headwind + 2025 tax-bill subsidy impairment.
- **grid/infra (IGF/PAVE/GRID): rotation** — data-center power demand strong (Westwood PWRX launched
  9/17 on TXSE).
- **lithium (LIT): rotation** — carbonate down, but CATL Jianxiawo mine lost its license; Benchmark
  flipped 2027 to deficit.
- **india (INDA): rotation** — spring FPI outflows, Aug inflows 2-yr high; crude+yield fears.
- **argentina (ARGT): unclear** — Milei economy concerns, -7.8% 30d.
- **housing (ITB/XHB): rotation** — mortgages ~7%, 30y govt 5.6%, new-home sales -10.5% MoM in July.
- **base-metals (XME): rotation** — copper tariff premium unwound 9/10 after White House tariff
  delay; physical tight.
- **discretionary (XLY): unclear / rotation** — 7-week losing streak, rates squeezing consumers;
  AMZN+TSLA ~40% of the fund.

---

## D. Confirmed catalysts carried forward — already verified, do NOT rescore as "not found"

| theme | event | date | confirmed by |
|---|---|---|---|
| nuclear | Cameco Q3 results, before market open | **2026-10-30** | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 |
| macro | FOMC decision | **2026-10-28** | federalreserve.gov FOMC calendar; re-verified 2026-09-29 |
| macro | FOMC decision | **2026-12-09** | federalreserve.gov FOMC calendar; re-verified 2026-09-29 |
| ai/robot | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | **2027-03-14** | nvidia.com GTC FAQ |
| solar | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | **2026-10-14** | Reuters/SRN 2026-09-11; SMM; Sxcoal; re-verified 2026-09-29 (solarpowerworld 9/20, Sxcoal 9/14, pv-magazine) |
| solar | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | **2026-11-02** | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 (Sxcoal, pv-magazine, taiyangnews) |

A panelist that cannot re-find one of these writes "carried forward, not re-searched" and keeps
the band the date earns. It does not score the theme down for having no dated trigger, and never
calls it "unverified": only a cited source that CONTRADICTS the date overturns it (write
"CONTRADICTED: <source>"; the verifier then marks the ledger row RETRACTED). check_memo.py fails
a ballot that doubts a live row without one.

### Disputed — sources contradict each other; neither date is confirmed

| theme | claim | readings | sources |
|---|---|---|---|
| rare-earth | China's suspension of its Oct-2025 rare-earth export controls (MOFCOM Announcement No. 70) | (a) expires 2026-11-10 with automatic snapback — MOFCOM No. 70 text (2025-11-07, pre-summit), per Sphera and pre-summit SilmarilMedia; (b) the rare-earth export-control pause was extended with the truce to 2027-01-10 — Bessent confirmed post-9/24-summit (The Global Market Brief 9/26; chomcho; tamaranews 9/26). Some outlets (FXStreet, InvestedAlpha) report no *new* firm rare-earth commitments. No MOFCOM text seen on either side | (a) MOFCOM No. 70 text; (b) Bessent via The Global Market Brief 9/26, chomcho, tamaranews 9/26 |

A catalyst score of 7+ that rests on a disputed date must cite a primary source (the issuing
ministry / agency / company) that settles it; otherwise score only what holds under both readings.
