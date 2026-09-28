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
| nuclear | Cameco | Cameco Q3 results, before market open | 2026-10-30 | Cameco press release, 2026-07-31 (BusinessWire) | 2026-09-18 |
| space | Starship | Starship Flight 14 — first orbital attempt, 26 Starlink V3, first revenue flight | 2026-09-28 | SpaceX via TechCrunch / USA Today, 2026-09-17 slip notice | 2026-09-21 |
| macro | FOMC | FOMC decision | 2026-10-28 | federalreserve.gov FOMC calendar | 2026-09-18 |
| macro | FOMC | FOMC decision | 2026-12-09 | federalreserve.gov FOMC calendar | 2026-09-18 |
| ai/robot | GTC | NVIDIA GTC 2027, San Jose McEnery Convention Center — flagship AI/robotics launch showcase | 2027-03-14 | nvidia.com GTC FAQ | 2026-09-21 |
| solar | Solar IV | USITC final injury vote on Solar IV AD/CVD (India/Indonesia/Laos) | 2026-10-14 | Reuters/SRN 2026-09-11; SMM; Sxcoal | 2026-09-28 |
| solar | Solar IV | Commerce final AD/CVD duty orders (India/Indonesia/Laos), Solar IV | 2026-11-02 | Sxcoal 2026-09-14; Reuters 2026-09-11 | 2026-09-28 |

## Disputed

Dates that sources contradict each other on. Not confirmed, so `carry_forward.py` prints them apart from the
live rows and no panelist may score a catalyst of 7+ on either reading without a primary source that settles it.
Move a row up into the table above (or delete it) once one does.

| theme | claim | readings | sources | noted on |
|---|---|---|---|---|
| rare-earth | China's suspension of its Oct-2025 rare-earth export controls (MOFCOM Announcement No. 70) | (a) expires 2026-11-10 with automatic snapback — MOFCOM No. 70 text (2025-11-07, pre-summit), per Sphera and pre-summit SilmarilMedia; (b) the rare-earth export-control pause was extended with the truce to 2027-01-10 — Bessent confirmed post-9/24-summit (The Global Market Brief 9/26; chomcho; tamaranews 9/26). Some outlets (FXStreet, InvestedAlpha) report no *new* firm rare-earth commitments. No MOFCOM text seen on either side | (a) MOFCOM No. 70 text; (b) Bessent via The Global Market Brief 9/26, chomcho, tamaranews 9/26 | 2026-09-28 |
