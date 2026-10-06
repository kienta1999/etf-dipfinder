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
DOUBT = re.compile(r"unverif|unconfirm|not confirmed|not found|no (verified )?dated|no date|could ?n[o']t (find|verify)",
                   re.I)


def render_problems(text):
    """[(line_no, problem)] for markdown GitHub will not render as written."""
    out, L = [], text.splitlines()
    in_table = False
    for i, ln in enumerate(L):
        row = ln.strip().startswith("|")
        nxt = L[i + 1].strip() if i + 1 < len(L) else ""
        if row and not in_table and nxt.startswith("|"):
            if not (re.fullmatch(r"\|[\s:|-]*\|?", nxt) and "-" in nxt):
                out.append((i + 1, "table header has no |---| delimiter row, so GitHub renders the whole "
                                   "table as one paragraph"))
            else:
                h, d = ln.strip().strip("|").count("|"), nxt.strip("|").count("|")
                if h != d:
                    out.append((i + 1, f"header has {h+1} columns but the delimiter has {d+1} - GitHub does "
                                       f"not render a table whose delimiter row does not match its header"))
        if in_table and not row and ln.strip():
            out.append((i + 1, "text directly under a table (no blank line) - GitHub folds it into the table "
                               "as a row"))
        in_table = row
        # $...$ is inline math on GitHub when the opener is followed by a non-space and the closer is
        # preceded by one and not followed by a digit - so "$18,700 | -$3,400" is safe, "$1.5T ... RTX$" is not.
        bare = re.sub(r"`[^`]*`", "", ln)
        if re.search(r"(?<!\\)\$(?=\S)[^$]*?(?<=\S)(?<!\\)\$(?!\d)", bare):
            out.append((i + 1, "unescaped $...$ pair - GitHub renders the text between them as a math "
                               "formula; write \\$"))
    return out


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


JUDGED = ["cause", "necessity", "catalyst", "basket"]   # the researched lenses; price is computed
COPY_SHARE, COPY_WARN, COPY_MIN = 0.95, 0.60, 8
# Share of >=8 shared funds whose four judged scores are ALL exactly equal to an earlier memo's. Measured
# 2026-09-19..10-05: copies (09-24, 09-27, 09-28 lite) matched 100%; independent runs on byte-identical prices
# matched 4-29% exactly (Claude 10-04 vs 10-05: 4% exact, 52% within +-1, 84% same bucket). Consistency is
# welcome - it shows up as same bucket and +-1 scores, not as every score copied - so only a near-total match
# fails; 60-95% is a warning to look at, room for a tighter rubric to raise honest agreement.


def memo_rows(text):
    """{ticker: {'cause':..,'necessity':..,'catalyst':..,'basket':..,'why':..}} from a memo's ranking table.
    Tolerates the abbreviated headers older lite memos used (need, cat)."""
    alias = {"need": "necessity", "cat": "catalyst"}
    rows, hdr = {}, None
    for ln in text.splitlines():
        c = [x.strip().strip("*").strip() for x in ln.strip().strip("|").split("|")]
        if hdr is None and len(c) > 5 and c[1] == "ETF":
            hdr = [alias.get(h.lower(), h.lower()) for h in c]
            continue
        if hdr and len(c) == len(hdr) and re.fullmatch(r"\d+", c[0]) and re.fullmatch(r"[A-Z]+", c[1]):
            d = dict(zip(hdr, c))
            rows[c[1]] = {k: d.get(k) for k in JUDGED} | {"why": next((v for k, v in d.items() if k.startswith("why")), "")}
    return rows


def _run_date(run):
    return run[:10]


def other_runs(run):
    """{run id: judged rows} for every other memo dated on or before this run's date."""
    out = {}
    for p in sorted((ROOT / "log").glob("20*.md")):
        rid = p.stem[:-5] if p.stem.endswith("-lite") else p.stem
        if rid != run and _run_date(rid) <= _run_date(run):
            rows = memo_rows(p.read_text())
            if rows:
                out[p.stem] = rows
    return out


def copy_check(run, today):
    """Independence: today's judged scores must not be a copy of an earlier run's."""
    for name, rows in other_runs(run).items():
        both = set(rows) & set(today)
        if len(both) < COPY_MIN:
            continue
        same = sum(all(str(today[t][k]) == str(rows[t][k]) for k in JUDGED) for t in both)
        share = same / len(both)
        if COPY_WARN <= share < COPY_SHARE:
            warns.append(f"{same}/{len(both)} funds carry exactly the same four judged scores as log/{name}.md - "
                         f"unusually close for independent runs (history: <=29%); fine if each score's reason is "
                         f"today's evidence")
        if share >= COPY_SHARE:
            errors.append(f"not an independent run: {same}/{len(both)} funds carry exactly the same cause/"
                          f"necessity/catalyst/basket scores as log/{name}.md - score from today's dossier only, "
                          f"never from an earlier memo, ballot or scores.csv")


def floor_check(run, scores):
    """scores: {ticker: (theme, catalyst score, reason text)}. Catalyst may not sit below the computed floor."""
    fl = carry_forward.floors(_run_date(run))
    for t, (theme, s, note) in scores.items():
        r = fl.get(theme)
        if r and s is not None and int(float(s)) < carry_forward.FLOOR and "CONTRADICTED" not in (note or ""):
            errors.append(f"{t} catalyst {int(float(s))} is below the floor {carry_forward.FLOOR}: theme '{theme}' has "
                          f"{r['match']} ({r['event']}) confirmed for {r['date']}, within {carry_forward.FLOOR_DAYS} days "
                          f"(log/catalysts.md) - score >= {carry_forward.FLOOR} or cite 'CONTRADICTED: <source>'")


def run_of(path):
    """Run id a log/ or output/ path belongs to, or None (shared files such as log/catalysts.md)."""
    parts = Path(path).parts
    if len(parts) >= 2 and parts[0] == "output" and parts[1][:1].isdigit():
        return parts[1]
    if len(parts) == 2 and parts[0] == "log" and parts[1][:1].isdigit():
        stem = Path(parts[1]).stem
        return stem[:-5] if stem.endswith("-lite") else stem
    return None


def overwrite_check(run):
    """A run writes only its own files (plus the shared ledger). Modifying or deleting another run's memo,
    ballots or scores - as the 2026-10-01 and 2026-10-04 reruns did - erases an independent opinion."""
    up = subprocess.run(["git", "merge-base", "HEAD", "@{upstream}"], cwd=ROOT, capture_output=True, text=True)
    if up.returncode != 0:
        return
    diff = subprocess.run(["git", "diff", "--name-status", up.stdout.strip(), "--", "log", "output"], cwd=ROOT,
                          capture_output=True, text=True).stdout
    bad = []
    for ln in diff.splitlines():
        st, *paths = ln.split("\t")
        if st[0] in "MDR":
            for path in paths[:1]:
                owner = run_of(path)
                if owner and owner != run:
                    bad.append(f"{st} {path}")
    if bad:
        errors.append("this run modified or deleted another run's files - a rerun writes under its own id "
                      "(scripts/run_id.py), never over an earlier run:\n" + "\n".join("    " + b for b in bad))


def lite_main(run, memo):
    """Lite runs write only log/<RUN>-lite.md: audit what exists - independence, floor, rendering, overwrites."""
    rows = memo_rows(memo.read_text())
    if not rows:
        errors.append(f"{memo.name}: no ranking table parsed")
    copy_check(run, rows)
    import pandas as _pd
    scan = ROOT / "data" / "scan.csv"
    theme = _pd.read_csv(scan, index_col=0).theme.to_dict() if scan.exists() else {}
    from scan import THEME
    floor_check(run, {t: (theme.get(t, THEME.get(t)), r["catalyst"], r["why"]) for t, r in rows.items()
                      if r["catalyst"] and r["catalyst"].isdigit()})
    errors.extend(f"{memo.name} line {n}: {msg}" for n, msg in render_problems(memo.read_text()))
    overwrite_check(run)
    dirty = subprocess.run(["git", "status", "--porcelain", "log/", "SESSIONS.md"], cwd=ROOT,
                           capture_output=True, text=True).stdout.strip()
    if dirty:
        errors.append("uncommitted files - commit the memo and SESSIONS.md:\n"
                      + "\n".join("    " + ln for ln in dirty.splitlines()))
    for e in errors: print(f"ERROR   {e}")
    for w in warns: print(f"WARN    {w}")
    print(f"\n{run} (lite): {len(errors)} error(s), {len(warns)} warning(s)")
    return 1 if errors else 0


def main(date):
    out = ROOT / "output" / date
    if not out.exists():
        lite = ROOT / "log" / f"{date}-lite.md"
        if lite.exists():
            return lite_main(date, lite)
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

    # 2b. Independence: the judged scores must be this run's own, not an earlier run's carried over.
    if set(JUDGED) <= set(committed.columns):
        copy_check(date, {t: {k: int(committed.loc[t, k]) for k in JUDGED} for t in committed.index})

    # 2c. Computed catalyst floor (lenses.md / carry_forward.floors).
    cat_p = out / "score_catalyst.md"
    if cat_p.exists() and "theme" in committed.columns:
        notes = {t: (s, n) for t, s, n in re.findall(r"^\|\s*\d+\s*\|\s*\**([A-Z]+)\**\s*\|\s*(\d+)\s*\|(.*)$",
                                                     cat_p.read_text(), re.M)}
        floor_check(date, {t: (committed.theme[t], notes.get(t, (committed.catalyst[t], ""))[0],
                               notes.get(t, ("", ""))[1]) for t in committed.index})

    # 2d. Reruns never overwrite: only this run's own files (and the shared ledger) may change.
    overwrite_check(date)

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
        for cols, why in [(("why",), "per-row reasoning is the only rationale in the memo"),
                          (("dip#", "dip_score#"), "depth rank, recoverable from scores.csv dip_rank")]:
            col = cols[0]
            if not any(c in head for c in cols):
                warns.append(f"memo header dropped '{col}' ({why})")

    # 5. Every fund the rule buys (buy or core) must appear in the verifier's report (Phase 3.5).
    if "bucket" in committed.columns:
        vf = next((out / n for n in ("verifier.md", "verify.md") if (out / n).exists()), None)
        buys = list(committed.index[committed.bucket.isin(["buy", "core"])])
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

    # 5c. ...nor be scored down as "unverified". A confirmed row is overturned only by a cited source that
    #     CONTRADICTS it (then the verifier marks the row RETRACTED). "Could not find it" is not evidence:
    #     on 2026-09-26 the ballot and verifier called Cameco's Oct 30 date "unverifiable" - a date two
    #     earlier verifiers had quoted from Cameco's own release - and capped nuclear at catalyst 5.
    if cat_ballot.exists() and "theme" in committed.columns:
        live = {r["theme"]: r for r in carry_forward.unexpired(date)}
        for t, s, note in re.findall(r"^\|\s*\d+\s*\|\s*\**([A-Z]+)\**\s*\|\s*(\d+)\s*\|(.*)$",
                                     cat_ballot.read_text(), re.M):
            r = live.get(committed.theme.get(t))
            if r and DOUBT.search(note) and "CONTRADICTED" not in note:
                errors.append(f"{t} catalyst {s}: ballot doubts a confirmed catalyst ({r['match']} {r['date']}, "
                              f"log/catalysts.md, verified {r['verified_on']}) without citing a contradicting "
                              f"source - write 'CONTRADICTED: <source>' or score the date it has")

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

    # 6b. The memo is the deliverable; one GitHub cannot render is not published, however correct its
    #     numbers. 2026-09-28 shipped all three failures below at once.
    for mp in (ROOT / "log" / f"{date}.md", ROOT / "log" / f"{date}-lite.md"):
        if mp.exists():
            errors.extend(f"{mp.name} line {n}: {msg}" for n, msg in render_problems(mp.read_text()))

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
