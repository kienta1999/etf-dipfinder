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
| nuclear | Cameco | Cameco Q3 results, before market open | 2026-10-30 | Cameco press release, 2026-07-31 (BusinessWire); re-verified 2026-09-29 and 2026-10-01 (BusinessWire 20260730139928: "We plan to announce our 2026 third quarter results before markets open on Friday, October 30, 2026") | 2026-10-01 |
| space | Starship | Starship Flight 14 — first orbital attempt, 26 Starlink V3, first revenue flight | 2026-09-28 | SpaceX via TechCrunch / USA Today, 2026-09-17 slip notice | 2026-09-21 |
| macro | FOMC | FOMC decision (Oct 27-28 meeting, statement on second day) | 2026-10-28 | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01 | 2026-10-01 |
| macro | FOMC | FOMC decision (Dec 8-9 meeting, statement on second day) | 2026-12-09 | federalreserve.gov FOMC calendar (monetary20240809a + fomccalendars.htm); re-verified 2026-09-29 and 2026-10-01 | 2026-10-01 |
| ai/robot | GTC | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | 2027-03-14 | nvidia.com GTC FAQ | 2026-09-21 |
| solar | Solar IV | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | 2026-10-14 | Reuters/SRN 2026-09-11; SMM; Sxcoal; re-verified 2026-09-29 (solarpowerworld 9/20, Sxcoal 9/14, pv-magazine) and 2026-10-01 (pv-tech.org 9/15: "Commission is scheduled to make its final determination on 14 October 2026") | 2026-10-01 |
| solar | Solar IV | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | 2026-11-02 | Sxcoal 2026-09-14; Reuters 2026-09-11; re-verified 2026-09-29 (Sxcoal, pv-magazine, taiyangnews) and 2026-10-01 (pv-tech.org 9/15: "final AD/CVD duty orders, currently scheduled for 2 November 2026") | 2026-10-01 |
| housing | DHI | D.R. Horton Q4/FY26 results, before market open, 8:30 a.m. ET call | 2026-10-29 | D.R. Horton investor site press release, 2026-09-10 (BusinessWire): "will release financial results for its fourth quarter and fiscal year ended September 30, 2026 on Thursday, October 29, 2026 before the market opens" | 2026-10-01 |
| lithium | ALB | Albemarle Q3 2026 results, after NYSE close; earnings call Nov 5, 8:00 a.m. EST | 2026-11-04 | Albemarle PR Newswire, 2026-10-01: "will release its third quarter 2026 earnings after the NYSE closes on Wednesday, November 4, 2026" | 2026-10-03 |
| defense-us | RTX | RTX Q3 2026 results, before market open; call 8:30 a.m. ET | 2026-10-20 | RTX PR Newswire, 2026-09-29: "will issue its third quarter 2026 earnings results on Tuesday, October 20, prior to the stock market opening" (re-verified on prnewswire.com 2026-10-04; raised FY26 guidance: adj sales $95-96B from $92.5-93.5B, adj EPS $7.10-7.25 from $6.70-6.90; record $289B backlog) | 2026-10-04 |
| gold | Diwali | Diwali 2026 — Lakshmi Puja main festival day; Dhanteras (gold/silver-buying day) Nov 6; seasonal India gold stocking window Nov 6-10 | 2026-11-08 | Wikipedia (Diwali 2026: Lakshmi Puja Nov 8, Dhanteras Nov 6); vedictemple.in 2026 guide (recurring annual seasonal, secondary/soft) | 2026-10-04 |

## Disputed

Dates that sources contradict each other on. Not confirmed, so `carry_forward.py` prints them apart from the
live rows and no panelist may score a catalyst of 7+ on either reading without a primary source that settles it.
Move a row up into the table above (or delete it) once one does.

| theme | claim | readings | sources | noted on |
|---|---|---|---|---|
| rare-earth | China's suspension of its Oct-2025 rare-earth export controls (MOFCOM Announcement No. 70) | (a) expires 2026-11-10 with automatic snapback — MOFCOM No. 70 text (2025-11-07, pre-summit), per Sphera and pre-summit SilmarilMedia; (b) the rare-earth export-control pause was extended with the truce to 2027-01-10 — Bessent confirmed post-9/24-summit (The Global Market Brief 9/26; chomcho; tamaranews 9/26). Some outlets (FXStreet, InvestedAlpha) report no *new* firm rare-earth commitments. No MOFCOM text seen on either side | (a) MOFCOM No. 70 text; (b) Bessent via The Global Market Brief 9/26, chomcho, tamaranews 9/26; post-summit: Bessent Fox News 9/24 announced the Nov-10 → 2027-01-10 extension (WSJ headline via killbait; tokenpost; roic; pressinsider — which notes Beijing did not separately announce the date); silmarilmedia 9/29: "a 61-day reprieve with no binding commitments on rare earth supply volumes, no resolution of the April 2025 licensing architecture"; neuralwired 9/26: extension "preserves China's suspension of rare earth export controls". Still no MOFCOM text on either side — stays Disputed | 2026-09-28; sources updated 2026-09-30 |
