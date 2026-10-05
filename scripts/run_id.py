"""The id this run writes under. Usage: uv run python scripts/run_id.py [YYYY-MM-DD]   (default: today)

A date's first run is the date itself (2026-10-05): output/2026-10-05/, log/2026-10-05.md (or -lite.md).
A second run on the same date never overwrites the first; it gets the next free id - 2026-10-05-r2, -r3 ...
Use the printed id everywhere the skill says <DATE>: output/<RUN>/, log/<RUN>.md, consolidate.py <RUN>,
check_memo.py <RUN>.

Why: on 2026-10-01 and again on 2026-10-04 a rerun replaced the date's original memo, ballots and scores,
so the two independent opinions on identical prices - the only direct measure of judgment noise - survived
only in git history."""
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def taken(run):
    return ((ROOT / "output" / run).exists() or (ROOT / "log" / f"{run}.md").exists()
            or (ROOT / "log" / f"{run}-lite.md").exists())


def next_run_id(day=None):
    day = str(day or date.today())
    run, n = day, 1
    while taken(run):
        n += 1
        run = f"{day}-r{n}"
    return run


if __name__ == "__main__":
    print(next_run_id(sys.argv[1] if len(sys.argv) > 1 else None))
