# Verifier — 2026-09-29

Independent re-check of the load-bearing claims behind every rule **buy** (URA, TAN, IHI) and **core**
(IGF, XLU) row plus the regime premises. Gate arithmetic was re-run from `output/2026-09-29/scores.csv`
directly: URA/TAN/IHI satisfy the buy gate (cause ≥ 7, (stabilizing or catalyst ≥ 7), not thin,
theme_rank == 1) and IGF/XLU satisfy the core rule (broad theme, not a buy, cause ≥ 7, necessity ≥ 8,
not thin, theme_rank == 1) exactly as printed. No rule reproduction failure.

## Verdicts

### §1 — Rule buy rows (gate components from scores.csv)

| claim | verdict | evidence |
|---|---|---|
| URA: cause 7, catalyst 8, theme nuclear, theme_rank 1, not thin | CONFIRMED | scores.csv: cause=7, catalyst=8, thin=False, theme_rank=1 (rr 2.74 > 1.3), wtd_rank 5 |
| TAN: cause 7, catalyst 8, theme solar, theme_rank 1, not thin | CONFIRMED | scores.csv: cause=7, catalyst=8, thin=False, theme_rank=1 (rr 4.58), wtd_rank 8 |
| IHI: cause 7, stabilizing=true, theme health-other, theme_rank 1, not thin | CONFIRMED | scores.csv: cause=7, stabilizing=True, thin=False, theme_rank=1 (rr 2.28); data/scan.csv: ret_10d +0.35% > 0 → stabilizing |

### §2 — Rule core rows (core = cause ≥ 7, necessity ≥ 8, not thin, theme_rank 1, broad theme, not buy)

| claim | verdict | evidence |
|---|---|---|
| IGF: cause ≥ 7, necessity ≥ 8, not thin, grid/infra (broad), theme_rank 1 | CONFIRMED | scores.csv: cause=7, necessity=10, thin=False (rr 2.90), theme_rank=1; grid/infra ∈ BROAD_THEMES (README §2); rule-buy=False |
| XLU: cause ≥ 7, necessity ≥ 8, not thin, utilities (broad), theme_rank 1 | CONFIRMED | scores.csv: cause=7, necessity=10, thin=False (rr 3.24), theme_rank=1; utilities ∈ BROAD_THEMES; rule-buy=False |

### §3 — Dated catalysts behind the buy/catalyst scores

| claim | verdict | evidence |
|---|---|---|
| Cameco Q3 results before market open 2026-10-30 (backs nuclear catalyst 8) | CONFIRMED — primary source | Cameco's own 7/31/2026 Q2 press release via BusinessWire: "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026." (TipRanks corroborates the Oct 30 date as confirmed.) Ledger row re-verified, verified_on bumped to 2026-09-29. |
| Uranium commodity backdrop (spot ~$89.7, term ~$96.5 record) behind URA cause 7 | CONFIRMED | discoveryalert.com Sept 2026: spot $89.50–89.75 mid-Sept; long-term indicator $96–97/lb, record term premium; equities derated while commodity held — the divergence claim stands. |
| USITC final injury vote on Solar IV AD/CVD 2026-10-14 (backs TAN catalyst 8) | CONFIRMED — strong secondaries | solarpowerworldonline.com 9/20/2026: "The ITC is scheduled to vote on the matter on Oct. 14, 2026"; Sxcoal 9/14: "scheduled to vote on October 14"; pv-magazine (all editions): "injury vote, scheduled for October 14, 2026". Ledger row re-verified, verified_on → 2026-09-29. |
| Commerce final Solar IV AD/CVD orders 2026-11-02 (backs TAN catalyst 8) | CONFIRMED — strong secondaries | Sxcoal 9/14: "If affirmative, Commerce will issue final duty orders on November 2"; pv-magazine: "Commerce will issue official duty orders on November 2, 2026, imposing the finalized cash deposit rates"; taiyangnews.info same. Conditional on affirmative ITC vote. Ledger row re-verified, verified_on → 2026-09-29. |
| Solar cause-7 backdrop (rate-driven leg down 9/24–25, TAN −4% vs SPY −0.54%) | CONFIRMED | summamoney.com 9/24: "TAN down 4% to $43.23 while SPY down 0.54%"; tradingview/SeekingAlpha: FSLR −10.3% to new 52w low; stocktwits: FSLR down 12% on week; mechanism documented as borrowing-cost-driven project financing pressure. |

Note: the ITC vote outcome is binary (affirmative → 11/2 orders; negative → proceedings terminate). The dates are confirmed; "one-sided positive" is the catalyst lens's judgment call, not a verified claim. TAN catalyst 8 rests on real dated events either way.

### §4 — Regime premises

| claim | verdict | evidence |
|---|---|---|
| FOMC decision 2026-10-28 | CONFIRMED — primary source | federalreserve.gov meeting calendar: two-day FOMC meeting Oct 27-28; statement 2pm ET Oct 28. Dec meeting Dec 8-9 confirmed likewise. Ledger rows re-verified, verified_on → 2026-09-29. |
| 10y Treasury closed ~5.24% on 2026-09-28, a 19-year closing high | CONFIRMED | WSJ live coverage 9/28: "settled at 5.241%, a fresh 19-year high… seventh time this month"; Morningstar/Dow Jones Data Talk: 5.241% close, 19-yr high, intraday 5.272%. 30y 5.561% = 24-year high. |
| Brent settled ~$105.28 on 2026-09-28 | CONFIRMED | WSJ 9/28: Brent "closed at $105.28 a barrel, up 0.9%"; Morningstar/Dow Jones Data Talk: front-month ICE Brent "gained 96 cents… to $105.28"; Barron's same. |
| Oil context on 9/29 (US-Iran/Hormuz driving the inflation-yield chain) | CONFIRMED | NY Post 9/28: Brent spiked to $107.02 intraday before settling $105.28 after Trump rejected Iran peace proposal; 9/29 reporting: Brent ~$106.86 trading up, WTI ~$93.86 — the Hormuz/US-Iran mechanism behind the rate narrative is live. |
| Rate-hike odds backdrop (~70% October hike) | CONFIRMED | Multiple 9/28 outlets (BigGo citing CME FedWatch): ~70% probability of a second consecutive hike at the October FOMC, up from 57.6% a week ago and 17.7% a month ago. |

### §5 — Fund-level facts behind basket scores

| claim | verdict | evidence |
|---|---|---|
| URA: 0.69% fee, top-ten ~61%, Cameco ~22%, AUM ~$5.8–6.5B | CONFIRMED | ainvest.com: 0.69% expense ratio, Cameco 22.23%, top-ten 60.96%, $5.86B AUM (as of 9/18); indmoney.com: 0.69%, Cameco 21.81%, $5.74B AUM (9/29); thetanerd: ~$6.5B AUM, 0.69% fee. |
| TAN: 0.70% fee, top-ten ~57.7% (Nextpower ~10.5%), ~$900M AUM, small/micro tilt | CONFIRMED | indmoney.com 9/29: 0.7%, $901.50M AUM, Nextpower 10.40%, small 42.41% + micro 17.55%; ainvest.com 9/18: 0.70%, $938.44M, top-ten 57.99%, Nextpower 8.84%; marketchameleon: top-ten 58.2%, Nextpower 10.56%. |
| IHI: ~0.37% fee, Abbott ~18%, ISRG ~14%, Medtronic ~12%, top-ten ~75% | CONFIRMED with one variance noted | indmoney.com 9/29: 0.37%, AUM $3.51B, Abbott 18.11%, ISRG 14.62%, Medtronic 11.73%; marketbeat.com: Abbott 18.19%, ISRG 13.81%; marketchameleon: top-ten 74.7%. Variance: marketbeat (12 days old) shows Medtronic at 4.96% rather than ~12% — provider/date variance on the exact MDT weight, but the "three-name concentration" structure (top-3 ~40–44%) is confirmed by all sources. |
| IGF: ~$10.3B AUM, ~0.37% fee, ~99 names, 5% single-name cap, top-10 ~38.5%, ~40% transport | CONFIRMED with minor variances noted | financecharts.com: $10.334B AUM; stockanalysis.com: $10.17B, 94 holdings, top-10 39.06%; mutualfunds.com: $10.5B, top-10 38.5%; seekingalpha: index "No single stock can exceed 5%", ~40% transportation / ~40% utilities / ~20% energy cluster targets. Expense ratio reads 0.37% (indmoney) vs 0.39% (marketchameleon, seekingalpha) vs 0.41% (financecharts); holdings read 94–96 vs ballot's 99. All within rounding/staleness — the basket profile holds. |
| XLU: 0.08% fee, ~$21B AUM, 31 names, NEE ~12.7%, 100% utilities | CONFIRMED | ssga.com (9/25/2026 factsheet): 0.08% gross expense ratio, NEXTERA 12.75%, 100% utilities allocation, 31-fund structure; marketbeat: $20.95B AUM; zacks: 0.08% fee, NEE ~13.1%, ~34 holdings, top-10 ~58.14%. |

### §6 — Core claims

| claim | verdict | evidence |
|---|---|---|
| XLU dividend yield ~3.08% vs 10y ~5.24% (bond-proxy selloff) | CONFIRMED | zacks: $1.21 (3.07%) dividend yield; marketbeat: 3.06%; stocknear: 2.981%; 10y 5.241% (9/28, §4). The ~3% yield vs ~5.24% risk-free spread is real; "sold as a bond proxy" mechanism is consistent with the reported utilities 17-month low. |
| Utilities/data-center demand thesis for XLU/IGF/PAVE/GRID (AI power demand + equipment backlogs) | CONFIRMED | IEA *Energy and AI* report (April 2026): global data-center electricity 415 TWh (2024) → 945 TWh by 2030, slightly more than Japan's total; US data centers to account for ~half of US electricity demand growth through 2030 (based.info, nsenergybusiness.com, datacenterdynamics.com). |
| Grid capex/backlog thesis (grid is the roads of the energy economy) | CONFIRMED | IEA *Electricity Grids and Secure Energy Transitions*: annual grid investment must double to >$600B/yr by 2030; 80M km of lines added/rebuilt by 2040; 1,500 GW of renewables waiting in connection queues (oilprice.com, electricityforum.com, reneweconomy.com.au). |
| GRID $283M inflows / Dell's $95B AI backlog (dossier supporting detail) | NOT RE-VERIFIED | Not load-bearing for any buy/core row (GRID is watch/thin). Flagged as uncarried supporting color; not contradicting anything found today. |

## Final verdicts

- **Buy rows: GO.** URA (cause 7 + catalyst 8 w/ Cameco 10/30 confirmed primary + theme_rank 1 + not thin), TAN (cause 7 + catalyst 8 w/ 10/14 and 11/2 confirmed + theme_rank 1 + not thin), IHI (cause 7 + stabilizing=true verified in scan + theme_rank 1 + not thin). No contradicted claim; all load-bearing dates and basket facts confirmed.
- **Core rows: GO.** IGF (cause 7, necessity 10, not thin, grid/infra theme_rank 1 — IEA demand/capex thesis confirmed), XLU (cause 7, necessity 10, not thin, utilities theme_rank 1 — ~3% yield vs 5.24% 10y confirmed).

Nothing in this pass contradicts any claim behind the buy or core decisions. Minor data-provider variances
(IGF fee 0.37–0.41%, IGF holdings 94–99, XLU yield 2.98–3.07%, IHI Medtronic weight 5–12% across providers)
do not touch any score rationale. Ledger updated: re-confirmed rows (Cameco 10/30, FOMC 10/28, FOMC 12/9,
USITC 10/14, Commerce 11/2) re-verified 2026-09-29.
