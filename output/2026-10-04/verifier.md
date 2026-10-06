> Run by: Claude Opus 5.5 (claude-opus-5-5) — annotated 2026-10-06 from the owner's record, not by the run itself.

# Verifier (Phase 3.5) — 2026-10-04

Scope: the three buy/core funds from consolidate.py (**XLU** buy, **NLR** buy, **IGF** core), alternates URA/URNM where facts are shared, the regime premises a memo opens on, the catalyst ballot's "New confirmed dates" list, and the Disputed MOFCOM row. Checked against primary sources (company press releases / IR pages / SEC filings, federalreserve.gov, home.treasury.gov, Freddie Mac, EIA, IEA, RBI, congress.gov, issuer fund pages) with uncapped searches/fetches on 2026-10-04. Where only a secondary source exists the evidence column says so. Searches: 29; fetches: 42 (39 WebFetch + 3 direct downloads).

| # | claim | fund(s) | verdict | evidence (source, date) |
|---|---|---|---|---|
| 1 | Southern Co Q3 2026 earnings by 7:30 a.m. ET **2026-11-05**, call 1 p.m. ET | XLU (IGF) | CONFIRMED | southerncompany.mediaroom.com press release 2026-09-25: "plans to release its earnings for the third quarter of 2026 by 7:30 a.m. ET on Thursday, November 5, 2026" (fetched) |
| 2 | Southern Co is a top-3 XLU weight | XLU | CONFIRMED | SSGA XLU page, holdings as of 2026-10-01: NextEra 12.75%, **Southern 7.69% (#2)**, Duke 7.10% |
| 3 | XLU yield ~3.05%; fee 0.08%; top-10 58.8%, NEE 12.75% | XLU | CONFIRMED | SSGA XLU page 2026-10-01: distribution yield 3.05% (30-day SEC 3.13%), gross ER 0.08%; top-10 sum 58.77% |
| 4 | XLU −6% in September, sharpest selloff since Oct 2023 | XLU | CONFIRMED (secondary only) | 24/7 Wall St 2026-10-02: "dropped 6% in the past month ... its sharpest selloff since October 2023". Its "17% below 52-week high" overstates scan.py's dd_52w of −14.8% at the 10/2 close |
| 5 | 10y above 5.2% vs XLU yield 3.05% | XLU, IGF | CONFIRMED | home.treasury.gov daily par yield curve: 10y 5.24% (10/1), 5.28% (10/2); above 5.2% every session since 9/28 |
| 6 | FERC five-month freeze on PJM capacity buying hits CEG (~7%) and VST (~4%) | XLU, NLR | CONFIRMED (corrected detail) | FERC order 2026-09-29 (eLibrary 20260929-3099; PJM Inside Lines / APPA): accepted PJM's 6,831 MW Reliability Backstop Procurement but **suspended it five months to 2027-02-28**; PJM pulled the 9/30 procurement. It is a backstop procurement, not the base capacity auction. SSGA weights are CEG 6.83%, VST 3.53% |
| 7 | EIA STEO 2026-09-09: record US electricity sales 4,135 BkWh 2026 (4,211 in 2027) | XLU | CONFIRMED | EIA press release press592 2026-09-09: "U.S. electricity sales to total 4,135 billion kilowatthours (BkWh) in 2026 ... rise another 2% to 4,211 BkWh in 2027" |
| 8 | Cameco Q3 results before the open **2026-10-30** (ledger row) | NLR, URA, URNM | CONFIRMED (re-verified) | SEC EDGAR 6-K ex-99.1 (Cameco Q2 release dated 2026-07-31, acc. 0001193125-26-326768): "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026." No contradicting source |
| 9 | Uranium spot ~\$89.6 Sep (\$89.68 Aug); long-term \$96.50 unchanged | NLR, URA, URNM | CONFIRMED | cameco.com/invest/markets/uranium-price: Aug spot \$89.68 / LT \$96.50; Sep spot \$89.63 / LT \$96.50 |
| 10 | Hyperscaler 2026 capex raised to \$720-745B at July earnings | NLR, URA | CONFIRMED (direction company-sourced; aggregate from trackers) | Meta PR 2026-07-29: "\$130-145 billion, narrowed from our prior outlook of \$125-145 billion"; Alphabet Q2 (2026-07-22) raised to \$195-205B from \$180-190B (call/8-K, via Motley Fool/Investing.com); Amazon Q2 (2026-07-30) raised to ~\$220B from \$200B (CNBC). The \$720-745B sum is from TMT Finance / yieldtheory trackers. Microsoft's figure was not checked |
| 11 | NLR holdings: Constellation 8.38% top, top-10 62.4%, 28 names, \$3.66B | NLR | CONFIRMED (aggregator; issuer page unreachable) | stockanalysis NLR holdings 2026-10-02: CEG 8.38%, Cameco 8.12% (#2), PEG 7.78%; top-10 62.36%; 28 names. vaneck.com redirect-looped twice |
| 12 | NLR fee 0.52% | NLR | CONFIRMED | VanEck 497K summary prospectus 2026-05-01 (SEC): management fee 0.50% + other 0.02% = 0.52% total |
| 13 | Catalyst ballot calls Cameco a "mid-weight holding" of NLR (reason for its −1) | NLR | CORRECTED (no score impact) | Cameco is NLR's **#2 holding at 8.12%** (stockanalysis 2026-10-02). If anything this argues against the −1; it does not lower the score |
| 14 | WNA reference case 746 GWe by 2040 (from 372); uranium 68,920 → 150,000+ tU | NLR, URA, URNM | CONFIRMED | world-nuclear.org press statement 2025-09-05 (World Nuclear Fuel Report 2025) |
| 15 | IEA WEI 2026: network spend ~\$550B in 2026, up ~20% | IGF | CONFIRMED | IEA World Energy Investment 2026 PDF (iea.blob.core.windows.net, launched 2026-05-28): "Global spending on networks is expected at around USD 550 billion in 2026, up nearly 20% year-on-year" |
| 16 | IGF holds 116 names | IGF | CORRECTED | iShares IGF page: **75 holdings** as of 2026-10-01 (excl. cash/derivatives). The 116 count is stockanalysis 2026-10-02. The catalyst ballot's "75-name" was right |
| 17 | IGF top-10 38.4%, top name Aena ~5% | IGF | UNVERIFIABLE (on primary) | iShares holdings tab is not machine-readable (CSV/JSON endpoints return HTML). stockanalysis 2026-10-02 shows Aena 4.98%, top-10 38.36%, so the aggregator agrees |
| 18 | IGF fee 0.37% | IGF | CONFIRMED | iShares IGF page: expense ratio 0.37%; net assets \$10.18B (2026-10-02) |
| 19 | IGF ~17% oil & gas midstream | IGF | CORRECTED | iShares sector split: Utilities 40.06%, Transportation 39.63%, **Energy 19.78%**. The seven named midstream names sum to 16.9% on stockanalysis; the issuer puts the off-grid energy sleeve at ~20%. Basket band 10 −1 still holds |
| 20 | IGF yield ~3.09% | IGF | CORRECTED | iShares IGF page: 12m trailing yield **2.96%**, 30-day SEC 2.84% (as of 2026-08-31). No 3.09% figure on the issuer page. The yield gap to the 10y (5.28%) is wider, so the cause reading is unchanged |
| 21 | IGF YTD +1.5% / +1.73% at 9/30 | IGF | CORRECTED (minor) | iShares: NAV total return YTD +1.01% as of 2026-10-01 |
| 22 | Fed hiked 25bp on 2026-09-16 to 3.75–4.00% | all (regime) | CONFIRMED | federalreserve.gov press release monetary20260916a: "raise the target range for the federal funds rate by 1/4 percentage point to 3-3/4 to 4 percent", vote 12-0 |
| 23 | 10y peaked ~5.33% and eased Oct 1–2 (dossier) | all (regime) | CORRECTED | Treasury par curve: closing peak **5.29% on 2026-09-30** (H.15 agrees); eased to 5.24% on 10/1, then **rose to 5.28% on 10/2**. 5.33% was not a closing print (possibly intraday). The dossier is right for 10/1 and wrong for 10/2 |
| 24 | 10y +5bp to 5.281% on 10/2 after weak jobs (cause ballot) | all (regime) | CONFIRMED | CNBC 2026-10-02 (via search; page 403): "rose almost 5 basis points to 5.281%", payrolls +29k, unemployment 4.2%. Treasury par 5.28% on 10/2 agrees. "Highest since 2002" not checked |
| 25 | FOMC decisions 2026-10-28 and 2026-12-09 (ledger rows) | all (regime) | CONFIRMED (re-verified) | federalreserve.gov/monetarypolicy/fomccalendars.htm: October 27-28; December 8-9* (SEP) |
| 26 | 30y mortgage 7.28% (Freddie Mac PMMS 2026-10-01) | housing (regime) | CONFIRMED | freddiemac.com/pmms: "averaged 7.28% as of October 1, 2026, up from last week when it averaged 7.03%" |
| 27 | ~94% December hike odds | all (regime) | CORRECTED | After the 10/2 jobs report CNBC (citing CME FedWatch) put **December hike odds above 75%** and a 77% chance of an October hold. The 94% figure (Yahoo) predates the jobs print or is unsupported. CME page not machine-readable |
| 28 | RTX Q3 2026 results before the open **2026-10-20** | ITA, PPA, XAR, SHLD | CONFIRMED | rtx.com news release 2026-09-29 (PRNewswire): "will issue its third quarter 2026 earnings results on Tuesday, October 20, prior to the stock market opening" |
| 29 | Lockheed Martin Q3 2026 results before the open **2026-10-22**, 8:30 a.m. ET call | ITA, PPA, XAR, SHLD | CONFIRMED (now primary) | news.lockheedmartin.com release, dateline "BETHESDA, Md., Oct. 1, 2026": call "Thursday, Oct. 22, 2026, at 8:30 a.m. ET", results "prior to market opening". Also listed at investors.lockheedmartin.com |
| 30 | Howmet Q3 2026 results ~7:00 a.m. ET **2026-10-29** | ITA, XAR, PAVE | CONFIRMED | howmet.com press release 2026-10-01 (fetched): "Thursday, October 29, 2026 ... available at approximately 7:00 AM ET"; webcast 10:00 a.m. ET |
| 31 | FY27 CR expires **2026-12-11** | defense-us | CONFIRMED | P.L. 119-103 text (congress.gov PLAW-119publ103), Div. A sec. 106(3): funds available until "December 11, 2026". CRS R49353 (2026-09-17) |
| 32 | Surface Transportation Extension Act of 2026 expires **2026-12-11** | PAVE (grid/infra) | CONFIRMED | P.L. 119-103 Div. C: "extension end date means December 11, 2026"; extension period begins 2026-10-01 |
| 33 | "IIJA surface-transportation authorities expired 9/30 with no highway bill" (cause ballot; necessity ballot's PAVE line) | PAVE | REFUTED | P.L. 119-103 Div. C (signed 2026-09-02) extended them from 10/1 through 2026-12-11. No reauthorization has passed, but they did not lapse on 9/30. Affects PAVE (watch) only, not IGF |
| 34 | Vestas Q3 2026 interim report **2026-11-11** | ICLN | CONFIRMED | vestas.com/en/investor/Calendar-Events (fetched 2026-10-04): "Disclosure of Q3 2026 interim report" 11 Nov 2026; quiet period from 2026-10-10 |
| 35 | HDFC Bank board meets **2026-10-17** to approve Q2 FY27 results | INDA | CONFIRMED | HDFC Bank Form 6-K filed 2026-09-22 (SEC acc. 0001193125-26-397434; text read via stocktitan; BSE copy 403): board meeting 2026-10-17 on results for the quarter ended 2026-09-30; trading window closed 9/24–10/19 |
| 36 | RBI MPC decision **2026-10-07** (Oct 5-7 meeting); next Dec 2-4 | INDA | CONFIRMED | rbi.org.in press release 2026-03-23, "Meeting Schedule of the Monetary Policy Committee for 2026-2027": Oct 5-7, Dec 2-4 |
| 37 | APEC Economic Leaders' Meeting, Shenzhen, **2026-11-18/19** | KWEB, FXI | CONFIRMED | Shenzhen Government Online (sz.gov.cn) 2026-09-10: Leaders' Meeting "Nov. 18 to 19", CEO Summit Nov. 17-18 |
| 38 | MOFCOM No. 70 suspension end: 2026-11-10 vs 2027-01-10 | REMX (rare-earth) | UNVERIFIABLE — stays Disputed | MOFCOM site search finds only (a) No. 70 (2025-11-07): suspension "至2026年11月10日" (until 2026-11-10), and (b) MOFCOM Americas-dept readout 2026-05-20, which says measures are suspended "至2026年11月10日" and mentions plans to extend without a date. No MOFCOM text gives 2027-01-10; Bessent's post-summit statement remains the only basis for it |

## Demotions

None. Every load-bearing fact behind the three buckets holds on a primary source:
- **XLU**: its catalyst 7 rests on Southern's date, which is company-confirmed (Southern is #2 at 7.69%). Its cause 7 rests on the 10y/yield gap and the FERC item, both confirmed.
- **NLR**: Cameco 10/30 is re-confirmed on Cameco's own SEC-filed release, and the uranium price page matches exactly.
- **IGF**: core rests on cause 7 and necessity 9. The IEA \$550B/+20% figure is confirmed on IEA's own report.

The corrections (IGF has 75 holdings, ~20% energy, 2.96% yield; the 10y peaked at a 5.29% close and rose on 10/2; December odds are >75%, not 94%) do not move any lens score across a bucket threshold.

Memo fixes to carry:
- Open the regime as: "10y closed at a 5.29% peak on 9/30, dipped to 5.24% on 10/1 and closed 10/2 at 5.28% after a weak jobs report".
- Do not say "eased Oct 1–2".
- Use ">75% December hike odds (CME via CNBC 10/2)".

## GO / NO-GO

- **XLU (buy)**: GO
- **NLR (buy)**: GO
- **IGF (core)**: GO
