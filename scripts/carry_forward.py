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


def disputed():
    """Rows under '## Disputed': dates sources contradict each other on. Neither reading is confirmed."""
    rows, on = [], False
    for ln in LEDGER.read_text().splitlines():
        if ln.startswith("## "):
            on = ln.strip().lower().startswith("## disputed")
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")] if on and ln.strip().startswith("|") else []
        if len(c) == 5 and not set(c[0]) <= set("-: ") and c[0] != "theme":
            rows.append(dict(zip(["theme", "claim", "readings", "sources", "noted_on"], c)))
    return rows


def block(asof=None):
    live, dis = unexpired(asof), disputed()
    tail = []
    if dis:
        tail = ["", "### Disputed — sources contradict each other; neither date is confirmed", "",
                "| theme | claim | readings | sources |", "|---|---|---|---|"]
        tail += [f"| {r['theme']} | {r['claim']} | {r['readings']} | {r['sources']} |" for r in dis]
        tail += ["", "A catalyst score of 7+ that rests on a disputed date must cite a primary source (the issuing",
                 "ministry / agency / company) that settles it; otherwise score only what holds under both readings."]
    if not live:
        return "\n".join(["## D. Confirmed catalysts carried forward", "", "None live."] + tail) + "\n"
    out = ["## D. Confirmed catalysts carried forward — already verified, do NOT rescore as 'not found'",
           "", "| theme | event | date | confirmed by |", "|---|---|---|---|"]
    out += [f"| {r['theme']} | {r['event']} | **{r['date']}** | {r['confirmed_by']} |" for r in live]
    out += ["", "A panelist that cannot re-find one of these writes \"carried forward, not re-searched\" and keeps",
            "the band the date earns. It does not score the theme down for having no dated trigger, and never",
            "calls it \"unverified\": only a cited source that CONTRADICTS the date overturns it (write",
            "\"CONTRADICTED: <source>\"; the verifier then marks the ledger row RETRACTED). check_memo.py fails",
            "a ballot that doubts a live row without one."]
    return "\n".join(out + tail) + "\n"


if __name__ == "__main__":
    print(block(sys.argv[1] if len(sys.argv) > 1 else None))
