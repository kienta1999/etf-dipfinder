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

## Disputed

Dates that sources contradict each other on. Not confirmed, so `carry_forward.py` prints them apart from the
live rows and no panelist may score a catalyst of 7+ on either reading without a primary source that settles it.
Move a row up into the table above (or delete it) once one does.

| theme | claim | readings | sources | noted on |
|---|---|---|---|---|
| rare-earth | China's suspension of its Oct-2025 rare-earth export controls (MOFCOM Announcement No. 70) | (a) expires 2026-11-10 with automatic snapback — the 2026-09-24 Trump–Xi summit extended the *tariff* truce to 2027-01-10 but said nothing on rare earths; (b) the rare-earth suspension itself was extended to 2027-01-10 | (a) 2026-09-26 and 2026-09-27 verifiers (Sphera, SilmarilMedia; China's statement silent on rare earths); (b) 2026-09-25 verifier (Bessent 9/23, CNBC, WSJ), Rinnovabili. No MOFCOM text seen by either side | 2026-09-28 |
