"""Live confirmed catalysts, for the dossier and the audit.

    uv run python scripts/carry_forward.py [YYYY-MM-DD]   # default: today

Panelists start cold every run, so a dated fact the verifier already confirmed has to be
rediscovered — and on 2026-09-21 the catalyst lens failed to, writing "no dated trigger found"
for nuclear five weeks before a confirmed Cameco print. log/catalysts.md is the ledger; this
prints the rows that have not expired, as the block that goes into the dossier."""
import re, sys
from datetime import date
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "log" / "catalysts.md"
COLS = ["theme", "match", "event", "date", "confirmed_by", "verified_on"]


def load():
    rows = []
    for ln in LEDGER.read_text().splitlines():
        c = [x.strip() for x in ln.strip().strip("|").split("|")] if ln.strip().startswith("|") else []
        if len(c) == len(COLS) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", c[3]):
            rows.append(dict(zip(COLS, c)))
    return rows


def unexpired(asof=None):
    """Rows whose event has not happened yet as of `asof`, retractions dropped."""
    asof = str(asof or date.today())
    return [r for r in load() if r["date"] >= asof and "RETRACTED" not in r["match"].upper()]


def block(asof=None):
    live = unexpired(asof)
    if not live:
        return "## D. Confirmed catalysts carried forward\n\nNone live.\n"
    out = ["## D. Confirmed catalysts carried forward — already verified, do NOT rescore as 'not found'",
           "", "| theme | event | date | confirmed by |", "|---|---|---|---|"]
    out += [f"| {r['theme']} | {r['event']} | **{r['date']}** | {r['confirmed_by']} |" for r in live]
    out += ["", "A panelist that cannot re-find one of these writes \"carried forward, not re-searched\" and keeps",
            "the band the date earns. It does not score the theme down for having no dated trigger."]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    print(block(sys.argv[1] if len(sys.argv) > 1 else None))
