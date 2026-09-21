"""Audit one dated run: uv run python scripts/check_memo.py 2026-09-18

Every check here is a failure a panel actually shipped. ERRORs mean the memo's verdict is not
the rule's verdict and must not be traded; WARNings mean the memo is readable but incomplete.
Exit code 1 on any ERROR.

Run it on the date you just produced. Run it on an older date and it tells you that memo no
longer matches the current rule - which is the point: that is how the stale 2026-09-17 buy list
(GRID, filed before the thin rule landed) was caught."""
import re, shutil, subprocess, sys, io, contextlib
from pathlib import Path
import pandas as pd

import consolidate
import carry_forward
ROOT = Path(__file__).resolve().parent.parent
LENSES = ["cause", "necessity", "catalyst", "basket", "price"]   # price is computed, not balloted
BALLOTS = ["cause", "necessity", "catalyst", "basket"]
errors, warns = [], []


def memo_table(date):
    """(header line, {ticker: bucket}) for the memo's main ranking table."""
    for p in (ROOT / "log" / f"{date}.md", ROOT / "log" / f"{date}-lite.md"):
        if p.exists():
            break
    else:
        errors.append(f"no memo at log/{date}.md")
        return None, {}
    head, rows = None, {}
    for ln in p.read_text().splitlines():
        if head is None and re.match(r"^\|\s*(my )?#\s*\|\s*ETF\s*\|", ln):
            head = ln
        m = re.match(r"^\|\s*\d+\s*\|\s*([A-Z]+)\s*\|.*\|\s*\**([A-Za-z() ]+?)\**\s*\|\s*$", ln)
        if m:
            rows[m.group(1)] = m.group(2).strip().lower().split()[0]
    return head, rows


def main(date):
    out = ROOT / "output" / date
    if not out.exists():
        print(f"ERROR: no output/{date}"); return 1

    # 1. scores.csv must be consolidate.py's own output, not hand-written.
    committed = pd.read_csv(out / "scores.csv", index_col=0)
    for col in ["bucket", "veto", "thin", "theme_rank", "wtd"]:
        if col not in committed.columns:
            errors.append(f"scores.csv has no '{col}' column - it was not written by consolidate.py")

    # 2. Ballots must parse, and re-running the rule must reproduce scores.csv exactly.
    tmp = ROOT / "output" / f".check-{date}"
    shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir(parents=True)
    try:
        shutil.copy(out / "scan.csv", tmp / "scan.csv")
        found = [l for l in BALLOTS if (out / f"score_{l}.md").exists()]
        for l in found:
            shutil.copy(out / f"score_{l}.md", tmp / f"score_{l}.md")
        for l in set(BALLOTS) - set(found):
            errors.append(f"missing ballot score_{l}.md")
        if found:
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    consolidate.main(tmp.name)
                fresh = pd.read_csv(tmp / "scores.csv", index_col=0)
                if fresh.empty:
                    errors.append("ballots do not parse - consolidate.py reads zero rows from them")
                elif not fresh.round(4).equals(committed.round(4)):
                    errors.append("consolidate.py does NOT reproduce the committed scores.csv")
            except AssertionError as e:
                errors.append(f"consolidate.py rejected the ballots: {str(e).splitlines()[0]}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # 3. Every bucket printed in the memo must equal the bucket the rule computed.
    head, memo = memo_table(date)
    if memo and "bucket" in committed.columns:
        missing = set(committed.index) - set(memo)
        if missing:
            warns.append(f"{len(missing)} funds scored but absent from the memo table: {sorted(missing)}")
        bad = [f"{t}: memo={memo[t]} rule={committed.bucket[t]}"
               for t in memo if t in committed.index and memo[t] != committed.bucket[t]]
        if bad:
            errors.append("memo buckets contradict scores.csv -> " + "; ".join(bad))

    # 4. Header must be the template's, spelled out, with the per-row reasoning kept.
    if head:
        for l in LENSES:
            if not re.search(rf"\|\s*{l}\s*\|", head):
                errors.append(f"memo header is missing the spelled-out '{l}' column")
        for col, why in [("why", "per-row reasoning is the only rationale in the memo"),
                         ("dip#", "depth rank, recoverable from scores.csv dip_rank")]:
            if col not in head:
                warns.append(f"memo header dropped '{col}' ({why})")

    # 5. Every fund the rule buys must appear in the verifier's report (Phase 3.5).
    if "bucket" in committed.columns:
        vf = next((out / n for n in ("verifier.md", "verify.md") if (out / n).exists()), None)
        buys = list(committed.index[committed.bucket == "buy"])
        if vf is None:
            errors.append(f"no verifier report in output/{date} - Phase 3.5 is not optional")
        else:
            txt = vf.read_text()
            unchecked = [t for t in buys if not re.search(rf"\b{t}\b", txt)]
            if unchecked:
                errors.append(f"buys absent from {vf.name}, so nothing verified their case: {unchecked}")

    # 5b. A catalyst the verifier already confirmed must not quietly vanish from the next ballot.
    cat_ballot = out / "score_catalyst.md"
    if cat_ballot.exists() and "theme" in committed.columns:
        txt, themes = cat_ballot.read_text(), set(committed.theme.dropna())
        for r in carry_forward.unexpired(date):
            if r["theme"] in themes and not re.search(re.escape(r["match"]), txt, re.I):
                errors.append(f"confirmed catalyst dropped: {r['match']} ({r['event']}, {r['date']}) is live for "
                              f"theme '{r['theme']}' and verified on {r['verified_on']}, but score_catalyst.md "
                              f"never mentions it")

    # 6. Lens scores that move hard with no new prices behind them.
    prev = [d.name for d in sorted((ROOT / "output").iterdir())
            if d.is_dir() and d.name[0].isdigit() and d.name < date and (d / "scores.csv").exists()]
    if prev:
        pdate = prev[-1]
        pscan, pscores = ROOT / "output" / pdate / "scan.csv", ROOT / "output" / pdate / "scores.csv"
        same_scan = pscan.exists() and pscan.read_bytes() == (out / "scan.csv").read_bytes()
        if same_scan:
            warns.append(f"scan.csv is byte-identical to {pdate} - no new market data, so every score change "
                         f"is re-scoring, not the market")
        old = pd.read_csv(pscores, index_col=0)
        moved = []
        for lens in LENSES:
            if lens in old.columns and lens in committed.columns:
                both = old.index.intersection(committed.index)
                d = (committed.loc[both, lens] - old.loc[both, lens])
                moved += [f"{t} {lens} {int(old.loc[t, lens])}->{int(committed.loc[t, lens])}"
                          for t in both if abs(d[t]) >= 3]
        if moved:
            (warns if not same_scan else warns).append(
                f"lens scores moved 3+ points vs {pdate}"
                + (" on identical prices" if same_scan else "") + f": {sorted(moved)}"
                + " - the memo should say why, or the judgment layer is just noisy")

    # 7. A run nobody committed is a run nobody else can see. check_memo reads the filesystem,
    #    so everything above passes locally whether or not the work was ever pushed - which is
    #    exactly how conviction-pick-sp500 published three runs of picks off an uncommitted
    #    screen and lost their inputs for good.
    dirty = subprocess.run(["git", "status", "--porcelain", "output/", "log/"], cwd=ROOT,
                           capture_output=True, text=True).stdout.strip()
    if dirty:
        errors.append("uncommitted files under output/ or log/ - the run is not finished until "
                      "this is empty:\n" + "\n".join("    " + ln for ln in dirty.splitlines()))

    for e in errors: print(f"ERROR   {e}")
    for w in warns: print(f"WARN    {w}")
    print(f"\n{date}: {len(errors)} error(s), {len(warns)} warning(s)")
    if errors:
        dates = sorted(d.name for d in (ROOT / "output").iterdir() if d.is_dir() and d.name[0].isdigit())
        if dates and date != dates[-1]:
            print(f"note: {date} is not the newest run ({dates[-1]}). Errors on an older date usually\n"
                  f"      mean the rule changed after it was filed, not that the run was wrong at the time.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
