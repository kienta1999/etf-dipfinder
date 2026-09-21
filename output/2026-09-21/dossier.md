# Research Dossier — 2026-09-21 ETF dip scan

Market data as-of: 2026-09-18 (latest scan run). Repo: `~/workspace/etf-dipfinder`.
This file is research input for the panel. Nothing here is scored, ranked, or final.

## Candidate scan rows (31 candidates, is_candidate=True)

Legend: `ticker` · `theme` · `asof` · `days` (history window) · `price` (USD close) · `dd_52w` (drawdown from 52w high) · `dd_pctile` (drawdown depth percentile) · `dd_z` (drawdown z-score) · `vs_sma200` / `vs_sma50` (fraction above/below moving avg) · `rs_spy_3m`/`rs_spy_6m`/`rs_spy_12m` (relative strength vs SPY) · `ret_10d` (10-day return) · `vol_60d` (60d annualized vol) · `dollar_vol` (avg daily $ volume) · `tp_pct` (take-profit target %) · `sl_pct` (stop-loss %) · `dip_low_pct` (dip low distance) · `rr` (reward/risk ratio) · `size_1pct` (position size for 1% risk) · `is_dip` · `stabilizing` (10d return ≥ 0 with recent bounce) · `dip_score` / `theme_score` (scan's own ranking inputs).

| ticker | theme | price | dd_52w | vs_sma200 | vs_sma50 | rs_spy_3m | rs_spy_12m | ret_10d | rr | stabilizing | dip_score | theme_score |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---:|---:|
| TAN | solar | 45.66 | -0.382 | -0.171 | -0.091 | -0.269 | -0.106 | -0.043 | 4.00 | False | 0.065 | 0.065 |
| REMX | rare-earth | 69.06 | -0.370 | -0.198 | -0.064 | -0.300 | -0.020 | -0.092 | 3.37 | False | 0.078 | 0.078 |
| KWEB | china | 24.83 | -0.387 | -0.162 | -0.067 | -0.039 | -0.553 | -0.028 | 5.67 | False | 0.078 | 0.078 |
| URNM | nuclear | 50.32 | -0.401 | -0.171 | -0.056 | -0.147 | -0.242 | -0.120 | 3.47 | False | 0.084 | 0.084 |
| NLR | nuclear | 107.69 | -0.345 | -0.173 | -0.055 | -0.174 | -0.305 | -0.097 | 3.00 | False | 0.090 | 0.084 |
| URA | nuclear | 41.65 | -0.326 | -0.137 | -0.035 | -0.151 | -0.192 | -0.089 | 2.55 | False | 0.194 | 0.084 |
| SLV | silver | 59.93 | -0.433 | -0.089 | 0.055 | -0.016 | 0.415 | -0.010 | 4.72 | False | 0.150 | 0.150 |
| UFO | space | 43.21 | -0.362 | -0.080 | -0.038 | -0.162 | 0.077 | -0.007 | 4.18 | False | 0.183 | 0.183 |
| ARKX | space | 32.12 | -0.149 | -0.004 | -0.003 | -0.093 | 0.034 | -0.007 | 1.43 | False | 0.585 | 0.183 |
| XLU | utilities | 41.10 | -0.127 | -0.071 | -0.062 | -0.099 | -0.170 | -0.045 | 2.31 | False | 0.202 | 0.202 |
| SHLD | defense-us | 62.68 | -0.194 | -0.078 | -0.029 | -0.013 | -0.216 | -0.017 | 2.34 | False | 0.207 | 0.207 |
| XAR | defense-us | 239.86 | -0.192 | -0.103 | -0.100 | -0.179 | -0.091 | -0.055 | 2.05 | False | 0.239 | 0.207 |
| ITA | defense-us | 213.84 | -0.155 | -0.069 | -0.090 | -0.127 | -0.102 | -0.053 | 1.99 | False | 0.312 | 0.207 |
| PPA | defense-us | 159.78 | -0.138 | -0.065 | -0.072 | -0.110 | -0.098 | -0.035 | 1.83 | False | 0.318 | 0.207 |
| PBW | clean | 30.63 | -0.344 | -0.117 | -0.065 | -0.281 | -0.025 | -0.029 | 2.99 | False | 0.214 | 0.214 |
| ICLN | clean | 17.56 | -0.259 | -0.064 | -0.022 | -0.190 | 0.007 | -0.004 | 2.70 | False | 0.260 | 0.214 |
| QCLN | clean | 47.82 | -0.302 | -0.084 | -0.055 | -0.278 | 0.015 | -0.027 | 2.38 | False | 0.331 | 0.214 |
| ITB | housing | 87.41 | -0.221 | -0.100 | -0.079 | -0.134 | -0.369 | -0.058 | 2.33 | False | 0.273 | 0.273 |
| XHB | housing | 96.39 | -0.202 | -0.094 | -0.084 | -0.153 | -0.318 | -0.058 | 2.34 | False | 0.279 | 0.273 |
| INDA | india | 48.02 | -0.132 | -0.043 | -0.025 | -0.054 | -0.282 | -0.038 | 2.85 | False | 0.326 | 0.326 |
| IGF | grid/infra | 63.17 | -0.077 | -0.030 | -0.039 | -0.071 | -0.099 | -0.028 | 2.06 | False | 0.358 | 0.358 |
| PAVE | grid/infra | 52.96 | -0.116 | -0.020 | -0.057 | -0.117 | -0.016 | -0.032 | 1.57 | False | 0.572 | 0.358 |
| GRID | grid/infra | 178.25 | -0.104 | 0.018 | -0.012 | -0.103 | 0.045 | 0.004 | 1.02 | **True** | 0.773 | 0.358 |
| LIT | lithium | 70.50 | -0.227 | -0.052 | -0.025 | -0.161 | 0.179 | -0.053 | 2.50 | False | 0.378 | 0.378 |
| BOTZ | ai/robot | 35.11 | -0.156 | -0.048 | -0.017 | -0.107 | -0.145 | -0.020 | 1.63 | False | 0.428 | 0.428 |
| ARKQ | ai/robot | 122.20 | -0.150 | -0.015 | 0.004 | -0.105 | 0.007 | -0.005 | 1.30 | False | 0.577 | 0.428 |
| ROBO | ai/robot | 78.50 | -0.131 | 0.009 | -0.024 | -0.110 | 0.040 | -0.016 | 1.26 | False | 0.741 | 0.428 |
| AIPO | ai/robot | 28.51 | -0.180 | 0.021 | -0.024 | -0.184 | 0.156 | 0.001 | 1.24 | **True** | 0.773 | 0.428 |
| QTUM | ai/robot | 147.79 | -0.123 | 0.116 | 0.003 | -0.141 | 0.299 | 0.011 | 0.94 | **True** | 0.890 | 0.428 |
| BAI | ai/robot | 45.14 | -0.168 | 0.113 | 0.024 | -0.174 | 0.172 | 0.038 | 0.88 | **True** | 0.902 | 0.428 |
| XLY | discretionary | 111.03 | -0.105 | -0.048 | -0.038 | -0.073 | -0.245 | -0.047 | 1.35 | False | 0.486 | 0.486 |

Only four candidates are marked `stabilizing=True`: GRID, AIPO, QTUM, BAI. Full scan CSV at `output/2026-09-21/scan.csv`.

## Leaders (momentum, not in dip set)

Scan leaders per lenses: ETHA, ARKG, WCLD, USO, BUG, IBIT, XOP, HACK. Not scored by the dip panel; listed for context.

## Regime quick-pass (preliminary — verifier scope will confirm)

Marked PRELIMINARY; each claim to be independently rechecked by the verifier.

- FOMC September 16, 2026: +25bp rate hike, the first Fed hike since 2023 (eOption mid-morning look, Sep 17). US equities rebounded Sep 17 (XLK, XLY, XLB led) as tech/semis/data-center names bounced post-hike; VIX fell ~10%.
- 10-year Treasury: above 5% on Sep 15 (10y touched 5.014% per Morningstar/Dow Jones wire, Sep 15; near highest since 2007). 20-year auction Sep 15 cleared at 5.42% — highest since 1986, soft-ish demand. Treasury is upsizing long-bond buybacks (≥$4B/op from Sep 9) to cool the long end.
- Oil: Brent topped ~$108/bbl in mid-September on Houthi strikes against Saudi Arabia and Iranian attacks on Gulf shipping (eOption, Sep 15); prices dipped slightly after the FOMC hike. Rough current level ~$102–104.
- September inflation backdrop: August CPI held at 3.4%; markets had priced ~92% odds of the hike the week before.

## Theme quick-pass (UNVERIFIED — one search per theme; panel lenses form their own views)

- **solar (TAN, −38% off 52w high, −4.3% 10d):** September Fed hike and rising borrowing costs pressuring residential solar; TAN trading below its 200-day average. Dip cause reads rate-driven, not company-specific.
- **rare earths (REMX, −37%, −9.2% 10d):** VanEck frames Western capex to cut China reliance as the thesis; no strong current selloff explanation found — broad risk-off and China sentiment likely contributors.
- **china tech (KWEB, −39%, −2.8% 10d):** August 24 Alibaba ~$10.2B placement plus weak-demand concerns fed the selloff; KWEB below key moving averages.
- **nuclear/uranium (URNM −40%, NLR −34%, URA −33%; 10d −9 to −12%):** Spot uranium ~$90.10/lb, long-term $97/lb (mid-September sources); miner weakness looks like broad risk-off plus AI-regulation/slowdown fears, not a change in the structural scarcity story.
- **silver (SLV, −43%, −1.0% 10d):** Silver ~$66.54 (Sep 18); recent movement primarily real-yield driven; oil retreating toward ~$102 supports margin compression. Notable 12m relative strength (+0.41 vs SPY) — deeper drawdown may reflect profit-taking rather than thesis damage.
- **space (UFO −36%, ARKX −15%):** Starship Flight 14 moved from Sep 22 to NET Sep 28, pending regulatory approval; first orbital/operational deployment of 26 Starlink V3 satellites planned. No thesis break — schedule slip only.
- **utilities (XLU, −12.7%, −4.5% 10d, −3.04% for the week):** higher yields and the 25bp Fed hike are the clear pressure; textbook rate-victim dip.
- **defense (SHLD, XAR, ITA, PPA, −14 to −19%, 10d −1.7 to −5.5%):** September weakness attributed to high yields and investor fatigue rather than operating deterioration; mid-September coverage cited strong backlogs/revenue visibility.
- **clean energy (PBW −34%, ICLN −26%, QCLN −30%):** ICLN rallied 40%+ over the past year and is now pulling back; rate/policy sensitive. Prior memo's blanket "subsidy repeal" thesis found NO primary supporting evidence in current research — treat as unverified.
- **housing (ITB −22%, XHB −20%, 10d −5.8%):** NAHB builder confidence fell to 32 (1-year low); 30-year mortgage 6.76% (highest in over a year), 10-year ~5.04% (Sep 16). ~38% of builders cut prices in September. Structural shortage (~5M units) thesis intact but demand frozen by rates.
- **india (INDA, −13.2%, −3.8% 10d):** search inconclusive; late-summer foreign inflows (August at 2-year high, ~₹29.6k crore) improved after heavy spring outflows (~$20B). Recovery story but flow-fragile.
- **grid/infra (GRID −10.4%, PAVE −11.6%, IGF −7.7%):** GRID off its $199.99 May high on AI-capex repricing questions, still +19% over 12m; investors accumulated on weakness — $7.52B of 12m net flows, $283.7M in one 5-day window while price fell (tradingnews). Underlying story: transformers/switchgear/transmission into an AI data-center buildout; repricing not a demand break.
- **lithium (LIT, −22.7%, −5.3% 10d):** fell 8 of the last 10 sessions, below 50-day ($72.75) and 200-day ($76.96) MAs, ~$70.24 close Sep 18; technicals flashing oversold (Mitrade indicators); LAC −34% YTD. Commodity-glut/rate driven.
- **ai/robotics (BOTZ −15.6%, ARKQ −15.0%, ROBO −13.1%, QTUM −12.3%, BAI −16.8%, AIPO −18%):** Sep 14 selloff triggered by Anthropic CEO Dario Amodei's Sep 12 essay "We Must Pace the Frontier" (endorsed by Altman and Musk on X) calling for slower model-capability gains; NO company has announced capex cuts — the scare is sentiment/regulatory, not demand. Chip/infrastructure sold off globally (NVDA −3.9%, VRT −8.6% premarket). Cyber (BUG, HACK, CIBR) rallied on the same news.
- **discretionary (XLY, −10.5%, −4.7% 10d):** −7.0% YTD vs SPY +12.5% — market's pressure valve for rate anxiety; $528.3M weekly outflows (Zacks, Sep 15). Fourth straight red week; both 50D and 200D MAs lost.

## Data gaps

- BJK/PHOX had no data in the scan window; several illiquid funds dropped by the scan.
- REMX: no clean current selloff explanation — panel should not assume one.
- Clean energy "subsidy repeal" thesis: no primary evidence found.
- India: foreign-flow data incomplete.
