"""Why did a fund not become a buy? Usage: uv run python scripts/why.py GRID [XHB ...] [--date 2026-10-01]

Reads drops.csv (scan gates: no data / illiquid / not a dip / theme outside top N) and, for a panel run,
buckets_why.csv (panel rule: thin / cause / catalyst / one buy per theme). Without --date it reads the live
data/drops.csv from the last scan.py, and falls back to the newest output/<DATE>/ only when no scan has run yet.
With --date it reads output/<DATE>/drops.csv + buckets_why.csv.

Why live first: a run in progress must not read another run's output/ folder (independence rule). On 2026-10-21
two lite runs called why.py and it opened the full panel's output/2026-10-21/, because the newest output/ won."""
import argparse, signal
from pathlib import Path
import pandas as pd

from scan import THEME

ROOT = Path(__file__).resolve().parent.parent


def run_dir(date):
    if date:
        return ROOT / "output" / date
    runs = sorted(d for d in (ROOT / "output").iterdir() if d.is_dir() and d.name[0].isdigit() and (d / "drops.csv").exists())
    return runs[-1] if runs else None


def main():
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--date", help="run id, e.g. 2026-10-21 (default: live data/drops.csv)")
    a = ap.parse_args()
    live = ROOT / "data" / "drops.csv"
    d = run_dir(a.date) if a.date or not live.exists() else None
    if a.date and not (d / "drops.csv").exists():
        raise SystemExit(f"no output/{a.date}/drops.csv — check the run id (ls output/)")
    drops_p = d / "drops.csv" if d and (d / "drops.csv").exists() else live
    if not drops_p.exists():
        raise SystemExit("no drops.csv yet — run scripts/scan.py")
    drops = pd.read_csv(drops_p, index_col=0)
    why_p = drops_p.parent / "buckets_why.csv"
    why = pd.read_csv(why_p, index_col=0) if why_p.exists() and drops_p.parent != ROOT / "data" else None
    print(f"{drops_p.relative_to(ROOT)}" + (f" + {why_p.relative_to(ROOT)}" if why is not None else ""))
    for t in (x.upper() for x in a.tickers):
        if t in drops.index:
            r = drops.loc[t]
            print(f"  {t:<5} {r.stage}: {r.reason}")
        elif why is not None and t in why.index:
            print(f"  {t:<5} candidate → {why.loc[t, 'why']}")
        elif t in THEME:
            print(f"  {t:<5} candidate — passed every scan gate (its bucket: buckets_why.csv for a panel run, "
                  f"the memo's table for lite)")
        else:
            print(f"  {t:<5} not in the scan universe (scan.py UNIVERSE)")


if __name__ == "__main__":
    main()
