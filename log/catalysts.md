# Confirmed dated catalysts — carried between runs

The verifier appends a row here every time it CONFIRMS a dated event on a primary source. Panelists
read the live rows (via `scripts/carry_forward.py`, pasted into the dossier as section D) so a fact
that has already been nailed down is never rediscovered from scratch — or lost.

Why this file exists: on 2026-09-21 the catalyst ballot wrote "No single dated trigger found" for
NLR and URNM, five weeks before a Cameco Q3 date its own verifier had confirmed twice on Cameco's
press release. Nuclear fell from rank 1-2 to rank 14-15 on a 2% price move. A run starting cold
cannot keep a fact it found last week.

A row stays live until `date` passes. Expired rows stay in the file as history; `carry_forward.py`
drops them. Retracted rows get `RETRACTED` in the `match` column and are ignored.

| theme | match | event | date | confirmed by | verified on |
|---|---|---|---|---|---|
| nuclear | Cameco | Cameco Q3 results, before market open | 2026-10-30 | Cameco press release, 2026-07-31 (BusinessWire) | 2026-09-18 |
| space | Starship | Starship Flight 14 — first orbital attempt, 26 Starlink V3, first revenue flight | 2026-09-28 | SpaceX via TechCrunch / USA Today, 2026-09-17 slip notice | 2026-09-21 |
| macro | FOMC | FOMC decision | 2026-10-28 | federalreserve.gov FOMC calendar | 2026-09-18 |
| macro | FOMC | FOMC decision | 2026-12-09 | federalreserve.gov FOMC calendar | 2026-09-18 |
