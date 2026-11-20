> Run by: Opus 5.5 (claude-opus-5-5) — full panel

# verifier — 2026-11-20-r2

Scope: all seven rule-`buy` funds (no `core` this run): SOXX, GRID, BAI, EWY, VNM, URA, REMX, plus the four regime premises the memo opens on. Buy rule: cause ≥ 7 AND (stabilizing OR catalyst ≥ 7) AND R/R ≥ 1.3. For SOXX, GRID, BAI and EWY (stabilizing = True) the catalyst score is not load-bearing for the bucket, so cause is the fact that matters. For VNM, URA and REMX (not stabilizing) catalyst ≥ 7 is load-bearing. All web checks were run 2026-11-20.

| fund/premise | claim | verdict (CONFIRMED / CONTRADICTED / UNVERIFIED) | evidence (source + date) |
|---|---|---|---|
| regime (1) | Dec 8-9 FOMC, decision Dec 9, SEP meeting | CONFIRMED | federalreserve.gov/monetarypolicy/fomccalendars.htm (fetched 2026-11-20): "December 8-9*", * = Summary of Economic Projections |
| regime (1) | 25bp **hike** priced ~90-96% for Dec 9 | CONFIRMED | CME FedWatch via 24/7 Wall St. 2026-11-18 (~95% Nov 17 close, ~96% Nov 18); Investing.com/longbridge snapshots 92.7% 25bp / 7.2% 50bp; post-Waller reading 90% 25bp / 10% 50bp. The remainder is a 50bp hike, with 0% on hold or cut. Pricing depends on the snapshot. Fool's "100%" is the any-hike total |
| regime (1) | 10y UST > 5% | CONFIRMED | 24/7 Wall St. 2026-11-18: closes of 5.10% (Nov 12), 5.15% (Nov 13), 5.12% (Nov 16), 5.10% (Nov 17). The ledger's 10Y-Nov19 row (Treasury par curve) has 5.04% on Nov 19 |
| regime (2) | Democrats won both chambers on Nov 3, 2026 | CONFIRMED | Al Jazeera 2026-11-04 ("Democrats win control of House and Senate"); Variety; Yahoo final results (Senate 56-44 after Peltola's Alaska win, Jeffries in line for Speaker). These contradict technews.tw's "GOP held both" claim, which the cause ballot already set aside |
| regime (3) | Nov 5 crash: S&P ~-4.4%, SOX ~-12% | CONFIRMED | leprivatebanker / bbntimes / stocktitan, 2026-11-05: S&P 500 -4.36% to 7,353.73 (worst since Apr 2025), Nasdaq -5.52% to 24,315.00, PHLX SOX -12.25% to 9,011.14; Fox Business: "SOX plunged more than 12%". Bloomberg's -1.7% S&P figure (advisorperspectives, 403) was an intraday snapshot. Dossier section C's "SOX ~-10%" is stale; the cause ballot's -12.25% is correct |
| regime (4) | Jensen Huang resigned as NVIDIA CEO on Nov 12; Kress interim CEO | CONFIRMED | nvidianews.nvidia.com "NVIDIA Announces CEO Transition" (2026-11-12); the board accepted the resignation on Nov 11 per the 8-K. The spy-relationship reason comes from press reports only; NVIDIA gave no reason |
| regime (4) / SOXX, BAI cause | NVIDIA Q3 FY27 (Nov 17): Data Center $107.6B (+110%), Q4 guide $130B | CONFIRMED | investor.nvidia.com Q3 FY27 release (fetched): revenue $115.8B (+103% y/y), Data Center $107.6B (+110% y/y), Q4 outlook "$130.0 billion, plus or minus 3%", no China DC compute assumed, Kress interim CEO |
| SOXX | cause 8: de-rating against rising demand (SOX -12.25% Nov 5, Huang exit, NVDA print) | CONFIRMED | same three sources as above |
| SOXX, BAI | catalyst 7: NVIDIA GTC 2027, San Jose, mid-March (start day disputed) | UNVERIFIED (start day); CONFIRMED (event, venue, month) | nvidia.com/gtc/faq (fetched): FAQ body says "March 14–18, 2027" twice, but the same page's banner says "GTC 2027 March 15–18"; nvidia.com/gtc (fetched): "March 15–18" in all three places. nvidia.com still contradicts itself, so the dispute cannot be settled. The score holds under both readings (both fall 3-12 months out), and the catalyst is not load-bearing for either buy (both stabilizing) |
| SOXX | basket 8: AMD ~10.8% top, top-10 62.4% | UNVERIFIED | iShares holdings CSV returned an HTML shell (no data). This would not flip the bucket: basket is not a rule input |
| BAI | basket 8: 75 names, top-10 45.9%, ~5% cash | CONFIRMED | stockanalysis.com/etf/bai/holdings (holdings 2026-11-18): 75 holdings, top-10 45.87%, BLK Treasury cash fund 5.17% |
| BAI | cause 7: AI de-rating against accelerating demand | CONFIRMED | NVIDIA Q3 FY27 release (above) |
| GRID | cause 7: Eaton Q3 sales +28%, electrical backlog +46%, guidance raised | CONFIRMED | SEC 8-K ex-99 (etn09302026exhibit99.htm, fetched): "record $8.9 billion, up 28%"; "total backlog growth of 46% in Electrical"; "Raises Organic Growth Guidance" to 13-15% |
| GRID | cause headwind bounded: Hinojosa takes office 2027-01-19; pledge covers new approvals only | CONFIRMED | Texas Tribune 2026-11-04, ABC13, DCD, KSAT: takes office Jan 19, 2027; "a moratorium — a ban — on all data center approvals until laws can be passed" (Oct 22 video); applies to "any new permits" |
| GRID | catalyst floor 7: Surface Transportation Extension ends 2026-12-11 | CONFIRMED | congress.gov PLAW-119publ103 (fetched), Div. C sec. 3002(2): "The term 'extension end date' means December 11, 2026." Div. A sec. 106(3) CR also runs to "December 11, 2026" |
| EWY | cause 7: foreign AI-fear exodus, KOSPI 4,968, 1.44tn won sold Nov 17 | CONFIRMED | Korea Herald / Money Today / Korea Times 2026-11-17: close 4,968.48 (-2.59%), first close below 5,000 since Feb 2 (4,949.67); foreigners net sold 1.44-1.45tn won |
| EWY | catalyst floor 7: Korea 2027 budget, 820.9tn won, statutory deadline 2026-12-02 | CONFIRMED | Newsis 2026-11-01, Hankyung, korea.kr: total spending 820.9tn won (+12.8%), "법정 처리 기한은 오는 12월 2일"; the Speaker pledged passage within the deadline; budget committee plenary planned Nov 30. It is still a proposal, not yet law |
| EWY | basket flip-risk: Samsung + SK hynix ≈ 43% | CONFIRMED | stockanalysis.com/etf/ewy/holdings (holdings 2026-11-18): Samsung 22.58% + SK hynix 20.65% = 43.23%; top-10 58.62%. iShares page (fetched): ER 0.59%, 75 positions as of Nov 19. Basket 3 stands |
| VNM | catalyst 8: FTSE GEIS Vietnam tranche 2 effective 2027-03-22 | CONFIRMED | LSEG "Reclassification of Vietnam … FAQ, v1.3, August 2026" (PDF fetched and text-extracted): Tranche Two review "March 2027", "Implementation Effective Date … 22 March", tranching factor 30% (then 65% on 21 June and 100% on 20 September); "FTSE Russell will evaluate the ability of index trackers to replicate … prior to proceeding" |
| VNM | cause 9: foreign selling is mechanical Frontier→EM rotation | CONFIRMED (mechanism and direction); UNVERIFIED (exact figures) | LSEG FAQ v1.3: "The deletion of Vietnam from the FTSE Frontier Index Series will be implemented in a single tranche … September 2026", while EM inclusion is tranched, which creates the mechanical gap. Net selling persists: japan-sec.vn 2026-11-12 (VND -857.25bn, VN-Index 1,734.75); SSI monthly outlook (third straight month of net selling). The ballot's "37 of 45 sessions, VND -33.4tn since 9/21" could not be re-fetched (stockbiz.vn/en/markets/flows returns 404) and is not contradicted |
| VNM | basket 4: top-10 53.1%, Vingroup complex ~16% | CONFIRMED | stockanalysis.com/etf/vnm/holdings (2026-11-18): VIC 8.48% + VHM 7.27% (+ Vinpearl 3.24%), top-10 53.14% |
| URA | cause 8: physical uranium firm while equities slide (futures > $91/lb Nov 10, highest since Feb; Kazatomprom prices +17%) | CONFIRMED | tradingeconomics.com/commodity/uranium (fetched 2026-11-20): Nov 10 "above $91/lb, the highest level since February"; $90.10 on Nov 19 (+18.2% y/y); Kazatomprom Q3 turnover +25%, average prices +17% |
| URA | catalyst date: Cameco Q4/FY2026 results 2027-02-12 | CONFIRMED | SEC 6-K acc. 0001193125-26-439858 ex-99.1 (Cameco Q3 release, 2026-10-30, fetched): "before markets open on February 12, 2027" |
| URA | catalyst +1 (6 → 7): Cameco says Key Lake is "back on schedule in Q4" | **UNVERIFIED** (not contradicted) | Phrase not found in the 6-K ex-99.1 release, the ex-99.2 MD&A (first 100k chars) or the Fool Q3 call transcript (2026-10-30). The release says "commissioning of the new infrastructure is underway" and "greater certainty in the timing of uranium production and deliveries"; the MD&A lists delay of the Key Lake plan as a material risk and assumes the work "proceed[s]" as scheduled. The cause ballot's "the mill has restarted" is likewise not stated in any of the three. This is the most fragile buy on the board: if the +1 falls, URA scores catalyst 6, is not stabilizing, and drops to watch |
| URA | basket flip-risk: CCJ 21.8%, top-10 62.5% | CONFIRMED (immaterial drift) | Global X full-holdings CSV as of 11/19/2026: CCO CN 21.58%, top-10 61.91%, 61 lines. Still > 20% single name; basket 4 stands |
| REMX | catalyst 8: DFARS 252.225-7052 magnet delivery ban effective 2027-01-01 | CONFIRMED | acquisition.gov DFARS 252.225-7052 (MAY 2024), fetched: "(b)(1)(ii) Effective January 1, 2027, the Contractor shall not deliver under this contract any covered material", with the full NdFeB supply chain from Jan 1, 2027; covered countries are North Korea, China, Russia and Iran |
| REMX | catalyst context: KL truce / MOFCOM No. 58 to 2027-01-10 (two-way) | CONFIRMED (carried) | Live ledger rows (MOFCOM 2026-09-28; MOFCOM/GACC 2026 No. 58). Not re-fetched this run; nothing contradicts them |
| REMX | cause 7: Canaccord "equity disconnect"; ex-China NdPr +23% YTD, above $110/kg floor | CONFIRMED (with caveat) | oilprice.com 2026-10-21 (fetched): "ex-China NdPr pricing up 23% YTD", "now sits above the US$110/kg floor", Chinese pricing has "begun to normalise around the US$110/kg floor". Caveat: Benchmark Minerals priced ex-China NdPr oxide below the floor earlier ($95/kg CIF on Aug 21; $106.5/kg for September in its Sep 25 Q3 review, updated Oct 9). That is earlier in time, not a contradiction of the Oct 21 level, but the "above floor" claim is fragile. The cause ballot already withheld the +1 |
| REMX | basket flip-risk: ~1/3 lithium (ALB 9.1%, SQM 8.9%, PLS 5.5%) | CONFIRMED | stockanalysis.com/etf/remx/holdings (2026-11-18): ALB 9.05%, SQM 8.88%, PLS 5.51%, Ganfeng 3.24%, Liontown 2.78% = 29.46% in the top 20, with more lithium names at ranks 21-24 (about one third in total). Basket 4 stands |

## Demotions

None. No load-bearing fact for any of the seven buys is contradicted by a primary source.

- **URA: flagged, not demoted.** The +1 that lifts catalyst from band 6 to 7 rests on a Cameco quote ("Key Lake back on schedule in Q4") that I could not find in Cameco's own release, MD&A or call transcript. Nothing contradicts it either, so under the rules it stands. URA is not stabilizing, so this one point is the difference between `buy` and `watch`. The orchestrator should size URA at the low end and treat it as the first buy to drop if the point is challenged.
- **REMX: stands.** DFARS Jan 1, 2027 is confirmed on acquisition.gov. Benchmark's below-floor NdPr prints (Aug and Sep) temper the cause but do not contradict Canaccord's Oct 21 reading.
- **SOXX / BAI: stand.** GTC's start day is still disputed on nvidia.com itself, but both buys qualify on cause ≥ 7 plus stabilizing, so the dispute does not matter for the bucket.
- **Memo correction (not a demotion):** dossier section C's "SOX ~-10%" on Nov 5 should read -12.25% (S&P -4.36%).

## Ledger changes (log/catalysts.md)

Re-verified in place, by appending "; re-verified 2026-11-20 (2026-11-20-r2 verifier: <source>)" to the confirmed-by cell (13 rows):
- macro | FOMC | 2026-12-09: fomccalendars.htm "December 8-9*"; FedWatch ~90-96% 25bp hike; 10y > 5%
- ai/robot | GTC | 2027-03-14: nvidia.com is still split (FAQ body Mar 14–18; banner and /gtc Mar 15–18); start day stays Disputed
- defense-us | 12-11 | 2026-12-11: P.L. 119-103 Div. A sec. 106(3)
- grid/infra | Surface | 2026-12-11: P.L. 119-103 Div. C sec. 3002(2)
- rare-earth | DFARS | 2027-01-01: acquisition.gov clause (b)(1)(ii)
- vietnam | FTSE | 2027-03-22: LSEG FAQ v1.3 PDF, text-extracted
- nuclear | Cameco-FY | 2027-02-12: SEC 6-K ex-99.1. The row's older "back on schedule in Q4" wording was noted as not found in the primary documents. It was not retracted, because it is not contradicted
- grid/infra | Hinojosa | 2027-01-19: Texas Tribune / ABC13 / DCD
- korea | budget | 2026-12-02: Newsis / Hankyung / korea.kr
- history rows, re-confirmed: us-midterms | Dem-sweep; macro | rout (Nov 5); ai-semis | NVDA-CEO (Nov 12); semis | NVDA-Q3FY27 (Nov 17)

New rows appended to the confirmed table (2):
- `korea | KOSPI-Nov17 | ... 4,968.48 ... foreigners net sold ~1.44tn won (history row, no floor) | 2026-11-17 | Korea Herald / Korea Times / Money Today | 2026-11-20`
- `nuclear | uranium-Nov10 | US uranium futures above $91/lb Nov 10, highest since Feb; $90.10 Nov 19 ... (history row, no floor) | 2026-11-10 | tradingeconomics.com/commodity/uranium | 2026-11-20`

Disputed table: the GTC 2027 start-day row got a "Re-checked 2026-11-20" note. It stays Disputed.

RETRACTED: none.
