# Confirmed dated catalysts — carried between runs

The verifier appends a row here every time it CONFIRMS a dated event on a primary source. Panelists
read the live rows (via `scripts/carry_forward.py`, pasted into the dossier as section D) so a fact
that has already been nailed down is never rediscovered from scratch — or lost.

Why this file exists: on 2026-09-21 the catalyst ballot wrote "No single dated trigger found" for
NLR and URNM, five weeks before a Cameco Q3 date its own verifier had confirmed twice on Cameco's
press release. Nuclear fell from rank 1-2 to rank 14-15 on a 2% price move. A run starting cold
cannot keep a fact it found last week.

A row stays live until `date` passes. Expired rows stay in the file as history; `carry_forward.py`
drops them. Retracted rows get `RETRACTED` in the `match` column and are ignored — and a row is retracted only
on a cited source that CONTRADICTS it. "Could not find it" is not a contradiction: on 2026-09-26 the catalyst
ballot and verifier called the Cameco row below "unverifiable" and capped nuclear at 5, although two earlier
verifiers had quoted the date from Cameco's own Q2 release. `check_memo.py` now fails that.

| theme | match | event | date | confirmed by | verified on |
|---|---|---|---|---|---|
| housing | DHI | D.R. Horton authorized a new $5.00B share repurchase program, no expiration; FY26 repurchases expected ≥$3.25B ($2.2B YTD through Q3) | 2026-09-15 | StockTitan via ad-hoc-news (board authorization 2026-09-15) | 2026-10-02 |
|---|---|---|---|---|---|
| nuclear | Cameco | Cameco Q3 results, before market open | 2026-10-30 | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 and 2026-10-01 (BusinessWire 20260730139928: "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026"); re-verified 2026-10-04 on SEC EDGAR 6-K ex-99.1 (Cameco Q2 release 2026-07-31, acc. 0001193125-26-326768), same sentence | 2026-10-01 |
| space | Starship | Starship Flight 14 — first orbital attempt, 26 Starlink V3, first revenue flight | 2026-09-28 | SpaceX via TechCrunch / USA Today, 2026-09-17 slip notice | 2026-09-21 |
| macro | FOMC | FOMC decision (Oct 27-28 meeting, statement on second day) | 2026-10-28 | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: October 27-28) | 2026-10-01 |
| macro | FOMC | FOMC decision (Dec 8-9 meeting, statement on second day) | 2026-12-09 | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01; re-verified 2026-10-04 (fomccalendars.htm: December 8-9, SEP meeting) | 2026-10-01 |
| ai/robot | GTC | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | 2027-03-14 | nvidia.com GTC FAQ | 2026-09-21 |
| solar | Solar IV | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | 2026-10-14 | Reuters/SRN 2026-09-11; SMM; Sxcoal; re-verified 2026-09-29 (solarpowerworld 9/20, Sxcoal 9/14, pv-magazine) and 2026-10-01 (pv-tech.org 9/15: "Commission is scheduled to make its final determination on 14 October 2026") | 2026-10-01 |
| solar | Solar IV | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | 2026-11-02 | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 (Sxcoal, pv-magazine, taiyangnews) and 2026-10-01 (pv-tech.org 9/15: "final AD/CVD duty orders, currently scheduled for 2 November 2026") | 2026-10-01 |
| housing | DHI | D.R. Horton Q4/FY26 results, before market open, 8:30 a.m. ET call | 2026-10-29 | D.R. Horton investor site press release, 2026-09-10 (BusinessWire): "will release financial results for its fourth quarter and fiscal year ended September 30, 2026 on Thursday, October 29, 2026 before the market opens" | 2026-10-01 |
| lithium | ALB | Albemarle Q3 2026 results, after NYSE close; earnings call Nov 5, 8:00 a.m. EST | 2026-11-04 | Albemarle PR Newswire, 2026-10-01: "will release its third quarter 2026 earnings after the NYSE closes on Wednesday, November 4, 2026" | 2026-10-03 |
| utilities | Southern | Southern Company Q3 2026 earnings released by 7:30 a.m. ET; analyst call 1 p.m. ET | 2026-11-05 | southerncompany.mediaroom.com press release 2026-09-25 (fetched): "plans to release its earnings for the third quarter of 2026 by 7:30 a.m. ET on Thursday, November 5, 2026"; Southern is XLU's #2 holding at 7.69% (SSGA, 2026-10-01) | 2026-10-04 |
| defense-us | RTX | RTX Q3 2026 results before market open; 8:30 a.m. ET call | 2026-10-20 | rtx.com news release 2026-09-29 (PRNewswire, fetched): "will issue its third quarter 2026 earnings results on Tuesday, October 20, prior to the stock market opening" | 2026-10-04 |
| defense-us | LMT | Lockheed Martin Q3 2026 results before market open; 8:30 a.m. ET webcast | 2026-10-22 | news.lockheedmartin.com release dated 2026-10-01 (fetched; also at investors.lockheedmartin.com): call "Thursday, Oct. 22, 2026, at 8:30 a.m. ET", results published prior to market opening | 2026-10-04 |
| defense-us | Howmet | Howmet Aerospace Q3 2026 results ~7:00 a.m. ET, webcast 10:00 a.m. ET (also a PAVE holding) | 2026-10-29 | howmet.com press release 2026-10-01 (fetched): "Thursday, October 29, 2026. The press release and presentation materials will be available at approximately 7:00 AM ET" | 2026-10-04 |
| defense-us | 12-11 | FY27 continuing resolution (Division A of P.L. 119-103) expires: appropriations cliff, outcome cuts both ways | 2026-12-11 | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. A sec. 106(3): funds available until "December 11, 2026"; CRS R49353 (2026-09-17) | 2026-10-04 |
| grid/infra | Surface | Surface Transportation Extension Act of 2026 (Division C of P.L. 119-103) ends: IIJA highway/transit authorities lapse unless reauthorized or re-extended | 2026-12-11 | P.L. 119-103 enrolled text (congress.gov PLAW-119publ103), Div. C: "extension end date means December 11, 2026", extension period from 2026-10-01 | 2026-10-04 |
| clean | Vestas | Vestas Q3 2026 interim report (quiet period from 2026-10-10) | 2026-11-11 | vestas.com/en/investor/Calendar-Events (fetched 2026-10-04): "Disclosure of Q3 2026 interim report", 11 November 2026 | 2026-10-04 |
| india | HDFC | HDFC Bank board meeting to approve results for the quarter ended 2026-09-30 (Q2 FY27) | 2026-10-17 | HDFC Bank Form 6-K filed 2026-09-22 (SEC acc. 0001193125-26-397434, text read via stocktitan): board meets 2026-10-17 to approve unaudited standalone and consolidated results; trading window closed 9/24-10/19 | 2026-10-04 |
| india | RBI | RBI MPC policy decision (Oct 5-7 meeting, decision on the last day); next meeting Dec 2-4 | 2026-10-07 | rbi.org.in press release 2026-03-23 "Meeting Schedule of the Monetary Policy Committee for 2026-2027" (prid=62422, fetched): October 5-7, 2026 | 2026-10-04 |
| china | APEC | APEC Economic Leaders' Meeting, Shenzhen, Nov 18-19 (CEO Summit Nov 17-18) | 2026-11-18 | Shenzhen Government Online (sz.gov.cn) 2026-09-10 (fetched): Economic Leaders' Meeting "Nov. 18 to 19"; Xi announced Shenzhen host 2025-11 (cppcc.gov.cn) | 2026-10-04 |

## Disputed

Dates that sources contradict each other on. Not confirmed, so `carry_forward.py` prints them apart from the
live rows and no panelist may score a catalyst of 7+ on either reading without a primary source that settles it.
Move a row up into the table above (or delete it) once one does.

| theme | claim | readings | sources | noted on |
|---|---|---|---|---|
| rare-earth | China's suspension of its Oct-2025 rare-earth export controls (MOFCOM Announcement No. 70) | (a) expires 2026-11-10 with automatic snapback — MOFCOM No. 70 text (2025-11-07, pre-summit), per Sphera and pre-summit SilmarilMedia; (b) the rare-earth export-control pause was extended with the truce to 2027-01-10 — Bessent confirmed post-9/24-summit (The Global Market Brief 9/26; chomcho; tamaranews 9/26). Some outlets (FXStreet, InvestedAlpha) report no *new* firm rare-earth commitments. No MOFCOM text seen on either side | (a) MOFCOM No. 70 text; (b) Bessent via The Global Market Brief 9/26, chomcho, tamaranews 9/26; post-summit: Bessent Fox News 9/24 announced the Nov-10 → 2027-01-10 extension (WSJ headline via killbait; tokenpost; roic; pressinsider — which notes Beijing did not separately announce the date); silmarilmedia 9/29: "a 61-day reprieve with no binding commitments on rare earth supply volumes, no resolution of the April 2025 licensing architecture"; neuralwired 9/26: extension "preserves China's suspension of rare earth export controls". Still no MOFCOM text on either side — stays Disputed. 2026-10-04 verifier: a mofcom.gov.cn search finds only No. 70 itself (suspension "至2026年11月10日") and the MOFCOM Americas-dept readout of 2026-05-20 (measures suspended to 2026-11-10, extension planned but undated). No MOFCOM text for 2027-01-10 — still Disputed | 2026-09-28; sources updated 2026-09-30, 2026-10-04 |
