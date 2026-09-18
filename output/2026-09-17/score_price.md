# price — 2026-09-17

Scored only from the scan snapshot (`data/scan.csv`, asof 2026-09-17): dd_52w, dd_pctile, dd_z, vs_sma200, rs_spy_12m, ret_10d, stabilizing.

| rank | ETF | score | one-line reason (this lens only) | key source |
|---|---|---|---|---|
| 1 | SLV | 8 | Deepest dip on the board (dd -44.16%, worst ~6.3% of own history) with the most positive 12m trend (rs_spy_12m +0.36); not stabilizing yet (ret_10d -0.17%) | scan.csv 2026-09-17 |
| 2 | UFO | 8 | Worst 2.0% of own 3y drawdown history, 12m +0.11 intact, and the only space fund already stabilizing (ret_10d +1.21%) | scan.csv 2026-09-17 |
| 3 | ICLN | 8 | Worst 4.4% of own history, 12m +0.035, stabilizing=True with ret_10d +2.07% — a bounce has actually started | scan.csv 2026-09-17 |
| 4 | KWEB | 7 | Worst 0.8% of own history (dd -39.7%); capped because the 12m trend is broken (rs_spy_12m -0.54) and it's still falling (ret_10d -5.06%) | scan.csv 2026-09-17 |
| 5 | URNM | 7 | Worst 8.2% of history, dd -38.9%, 12m -0.20; still falling (ret_10d -6.62%) keeps it out of 8 | scan.csv 2026-09-17 |
| 6 | TAN | 7 | Worst 4.4% of history, dd -37.3%, 12m only mildly negative (-0.08); still falling (ret_10d -1.93%) | scan.csv 2026-09-17 |
| 7 | NLR | 7 | Worst 2.2% of history, dd -32.7%; capped on a broken 12m (-0.28) and a still-falling tape (ret_10d -5.52%) | scan.csv 2026-09-17 |
| 8 | URA | 7 | Worst 4.4% of history, dd -31.0%, 12m -0.16, ret_10d -3.70% — deep but not turning | scan.csv 2026-09-17 |
| 9 | QCLN | 7 | Worst 3.4% of history, dd -29.8%, 12m +0.05; not stabilizing (ret_10d -0.82%) | scan.csv 2026-09-17 |
| 10 | GLD | 7 | Worst 6.7% of history, dd -19.7%, 12m flat (+0.005); ret_10d -1.10%, no stabilization | scan.csv 2026-09-17 |
| 11 | AIPO | 7 | Worst 3.7% of history, dd -18.9%, above its 200d (+1.1%), stabilizing (ret_10d +1.15%), 12m +0.14 — young fund (289d), stats lightly held | scan.csv 2026-09-17 |
| 12 | XAR | 7 | Worst 0.4% of own history — historically extreme — but shallow (dd -18.7%), 12m -0.09, still falling (ret_10d -3.55%) | scan.csv 2026-09-17 |
| 13 | ITA | 7 | Worst 0.3% of own history, dd -15.4%; capped on 12m -0.11 and ret_10d -4.14% | scan.csv 2026-09-17 |
| 14 | PPA | 7 | Worst 0.8% of own history, dd -13.7%, 12m -0.10, ret_10d -2.16% — shallow but historically unusual | scan.csv 2026-09-17 |
| 15 | REMX | 6 | Deep (dd -36.9%) but only pctile 0.108 — not worst-decile by its own standards; 12m flat (-0.007), ret_10d -9.42% still falling hard | scan.csv 2026-09-17 |
| 16 | FXI | 6 | Worst 8.7% of history, dd -16.6%; 12m -0.32 broken, ret_10d -3.80% | scan.csv 2026-09-17 |
| 17 | SHLD | 6 | Worst 5.0% of history, dd -19.0%; 12m -0.22 broken, ret_10d -0.19% | scan.csv 2026-09-17 |
| 18 | ARKX | 6 | Ordinary patch by own history (pctile 0.098), but above its 200d, stabilizing, 12m +0.04 — trend intact | scan.csv 2026-09-17 |
| 19 | GRID | 6 | Shallow (dd -11.1%) but worst 4.5% of its own history; above 200d (+1.1%), stabilizing (ret_10d +0.75%), 12m +0.03 | scan.csv 2026-09-17 |
| 20 | ROBO | 6 | Worst 6.8% of history, above 200d (+1.2%), 12m +0.04 — but not stabilizing (ret_10d -0.29%) | scan.csv 2026-09-17 |
| 21 | QTUM | 6 | Worst 7.4% of history, above 200d by +11%, 12m +0.30, stabilizing — this "dip" is 3m-relative weakness only | scan.csv 2026-09-17 |
| 22 | XLU | 6 | Worst 0.4% of own history (historically extreme) but shallow (dd -11.5%), 12m -0.15 broken, still falling (ret_10d -2.30%) | scan.csv 2026-09-17 |
| 23 | LIT | 5 | Ordinary bad patch (pctile 0.263), dd -22.3%, ret_10d -4.52% falling; 12m +0.21 keeps it out of 4 | scan.csv 2026-09-17 |
| 24 | PBW | 5 | Deep (dd -34.2%) but ordinary by its own history (pctile 0.18); 12m flat (+0.01) | scan.csv 2026-09-17 |
| 25 | BOTZ | 5 | Worst 6.4% of history, dd -15.6%, 12m -0.14 broken, ret_10d -0.21% flat | scan.csv 2026-09-17 |
| 26 | PAVE | 5 | Shallow (dd -11.7%), worst 8.6% of history, 12m flat (-0.02), ret_10d -2.52% | scan.csv 2026-09-17 |
| 27 | IGF | 5 | Shallowest dip on the board (dd -7.0%); worst 2.2% of its history, but there is barely a dip to buy | scan.csv 2026-09-17 |
| 28 | ARKQ | 5 | Ordinary patch (pctile 0.12); above 200d, stabilizing (ret_10d +1.90%), 12m flat (+0.01) | scan.csv 2026-09-17 |
| 29 | BAI | 5 | Ordinary by own history (pctile 0.155); above 200d by +9.3%, stabilizing (ret_10d +3.17%), 12m +0.14 — 3m-relative weakness only | scan.csv 2026-09-17 |
| 30 | XHB | 4 | Ordinary bad patch (pctile 0.121), 12m -0.32 broken, still falling (ret_10d -4.05%) — nothing unusually cheap | scan.csv 2026-09-17 |
| 31 | ITB | 4 | Ordinary bad patch (pctile 0.210), 12m -0.36 broken, ret_10d -3.79% falling | scan.csv 2026-09-17 |
| 32 | INDA | 4 | Ordinary bad patch (pctile 0.117), 12m -0.28 broken, sharp recent leg (dd_z -1.05, ret_10d -3.92%) | scan.csv 2026-09-17 |

## Top-3 notes

**1. SLV (8) — the deepest dip with the healthiest 12m trend.** −44.16% off the 52-week high in the worst ~6% of its own 3-year drawdown history, while rs_spy_12m is +0.36 — the most positive 12-month relative trend on the entire board. The load-bearing caveat is tape, not history: ret_10d is −0.17% and stabilizing=False, so the price lens says "unusually cheap, trend intact, not turning yet" — an 8, not a 10. Source: scan.csv, 2026-09-17.

**2. UFO (8) — historically extreme and already stabilizing.** Worst 2.0% of its own drawdown history with the 12-month trend still positive (+0.11 rs_spy_12m), and it is the only space fund with stabilizing=True (ret_10d +1.21%). Depth plus a turn is the exact combination the lens pays for. Source: scan.csv, 2026-09-17.

**3. ICLN (8) — the bounce has started.** Worst 4.4% of its own history, 12m +0.035, and stabilizing=True on a +2.07% 10-day return — the only clean-energy fund where the tape has already turned. Source: scan.csv, 2026-09-17.

## Disagreements with the dossier's first-pass memo

1. **BAI stabilizing — confirmed and scored.** The memo's row 31 said stabilizing "no"; the scan says True (ret_10d +3.17%), corrected on 2026-09-18. The price lens still caps BAI at 5: dd_pctile 0.155 is an ordinary bad patch by its own standards — the "dip" is 3m-relative weakness, not unusual cheapness.
2. **SLV's −44% — depth is not the risk, the tape is.** The memo frames SLV's depth as the highest risk on the board; the price lens agrees the risk is real but locates it precisely: the 12m trend (+0.36 rs_spy_12m) is the healthiest on the board, and the dip is the deepest — the problem is only that stabilizing=False. Depth + intact trend is exactly what this lens buys.
3. **QTUM — same correction as BAI.** Above its 200d by +11% with 12m +0.30: the price lens scores it 6, agreeing with the memo that the cause lens has to justify inclusion — there is no unusual cheapness here.
4. **IGF "correction after strong gains" — agreed, and that's why it's a 5.** The memo's framing is right, but −7.0% is the shallowest dip on the board; there is barely a dip to buy, so the price lens caps it at 5 despite the worst-2.2%-of-history percentile.
5. **XHB / ITB / INDA / LIT ordinary patches — price lens concurs with the dossier's confidence note.** Scores of 4–5: no unusual cheapness (percentiles 0.117–0.263) and, except LIT's +0.21, broken 12m trends. Nothing here earns a price premium.
