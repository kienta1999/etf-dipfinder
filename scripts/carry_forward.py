"""Live confirmed catalysts, for the dossier and the audit.

    uv run python scripts/carry_forward.py [YYYY-MM-DD]   # default: today

Panelists start cold every run, so a dated fact the verifier already confirmed has to be
rediscovered — and on 2026-09-21 the catalyst lens failed to, writing "no dated trigger found"
for nuclear five weeks before a confirmed Cameco print. log/catalysts.md is the ledger; this
prints the rows that have not expired, as the block that goes into the dossier."""
import re, sys
from datetime import date, timedelta
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "log" / "catalysts.md"
COLS = ["theme", "match", "event", "date", "confirmed_by", "verified_on"]

# Computed catalyst floor (lenses.md): a THEME-SPECIFIC event confirmed in the ledger and dated within
# FLOOR_DAYS of the run sets catalyst >= FLOOR for every fund in that theme. The panel's "is it one-sided /
# priced?" judgment may lift it to 8-10 but never below. Rate decisions and data prints are symmetric
# timing, not direction, so they never set a floor. Why: on identical prices NLR's catalyst went 7 -> 6
# between two runs (2026-10-04/05) with Cameco's Oct 30 date unchanged, and that one point flipped buy -> watch.
FLOOR, FLOOR_DAYS = 7, 30
SYMMETRIC = re.compile(r"FOMC|\bMPC\b|monetary policy|policy decision|rate decision|\bCPI\b|payroll|jobs report", re.I)


def load():
    rows = []
    for ln in LEDGER.read_text().splitlines():
        c = [x.strip() for x in ln.strip().strip("|").split("|")] if ln.strip().startswith("|") else []
        if len(c) == len(COLS) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", c[3]):
            rows.append(dict(zip(COLS, c)))
    return rows


def unexpired(asof=None):
    """Rows whose event has not happened yet as of `asof`, retractions dropped. A rerun id such as
    2026-10-05-r2 is read as its date."""
    asof = str(asof or date.today())[:10]
    # Known by then: a row the verifier only added later cannot bind a run that predates it (auditing an old
    # date against today's ledger otherwise fails it for facts nobody had yet).
    return [r for r in load() if r["date"] >= asof and r["verified_on"][:10] <= asof
            and "RETRACTED" not in r["match"].upper()]


def floors(run_date=None):
    """{theme: ledger row} for themes whose catalyst score may not fall below FLOOR on run_date."""
    d0 = date.fromisoformat(str(run_date or date.today())[:10])
    out = {}
    for r in unexpired(d0.isoformat()):
        if r["theme"] == "macro" or SYMMETRIC.search(r["event"]):
            continue
        if date.fromisoformat(r["date"]) <= d0 + timedelta(days=FLOOR_DAYS):
            if r["theme"] not in out or r["date"] < out[r["theme"]]["date"]:
                out[r["theme"]] = r
    return out


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
    fl = floors(asof)
    out = ["## D. Confirmed catalysts carried forward — already verified, do NOT rescore as 'not found'",
           "", "| theme | event | date | floor | confirmed by |", "|---|---|---|---|---|"]
    out += [f"| {r['theme']} | {r['event']} | **{r['date']}** | "
            f"{f'**catalyst >= {FLOOR}**' if fl.get(r['theme']) == r else ''} | {r['confirmed_by']} |" for r in live]
    if fl:
        out += ["", f"**Catalyst floor:** every fund in a theme marked above scores catalyst >= {FLOOR} this run "
                f"(issuer-confirmed, theme-specific, within {FLOOR_DAYS} days). Judgment may lift it to 8-10, never "
                "below; only 'CONTRADICTED: <source>' overrides. check_memo.py fails a lower score."]
    out += ["", "A panelist that cannot re-find one of these writes \"carried forward, not re-searched\" and keeps",
            "the band the date earns. It does not score the theme down for having no dated trigger, and never",
            "calls it \"unverified\": only a cited source that CONTRADICTS the date overturns it (write",
            "\"CONTRADICTED: <source>\"; the verifier then marks the ledger row RETRACTED). check_memo.py fails",
            "a ballot that doubts a live row without one."]
    return "\n".join(out + tail) + "\n"


if __name__ == "__main__":
    print(block(sys.argv[1] if len(sys.argv) > 1 else None))
