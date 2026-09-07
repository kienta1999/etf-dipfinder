---
name: etf-dip-pick-lite
description: Cheap single-agent version of etf-dip-pick — same scan, same five lenses (cause, necessity, catalyst, basket, price), same weights/veto/one-buy-per-theme rule, but ONE agent does everything in one pass with ~10 web searches total (one per theme, not per ETF or per lens) and writes only log/<DATE>-lite.md. No subagents, no output/<DATE>/ dossier or ballots, no verifier. Use when the user says "lite", "quick", "cheap", "one pass", "no subagents", is near a usage limit, or wants a fast read on which sector/thematic ETFs are on sale / beaten down / lagging. For the full panel with audit trail use etf-dip-pick.
---

# etf-dip-pick-lite — one agent, one pass, one memo

Same question as `etf-dip-pick` (is this dip *on sale* or *broken*?), scored by you alone. Read
`../etf-dip-pick/lenses.md` for the five lenses, weights, veto and bucket rule — do not re-derive them.
Budget: **≤10 WebSearch total, no WebFetch** of filings/PDFs. Search snippets only.

## 1. Scan
```
cd etf-dipfinder && uv run python scripts/scan.py     # full path if cwd is already inside
```
Read LEADERS first (where did the money go?), then the top ~12-15 DIPS. `dip_score` is depth, not quality.

## 2. Research — one search per theme
Group the candidates by `theme` (URA/URNM/NLR are one theme, TAN/ICLN/PBW one, GLD/SLV one…). One search
per theme: `"<theme> ETF" selloff <Month YYYY> outlook`. Plus one regime search (10y yield, Fed odds).
Siblings in a theme share cause / necessity / catalyst scores unless the snippet gives a fund-specific reason
(e.g. US-residential-solar policy hits TAN but not ICLN) — then write that one sentence.
Basket and price need no search: basket from what you know of the fund's top holdings / concentration;
price from the CSV columns (`dd_pctile`, `dd_z`, `rs_spy_12m`, `stabilizing`).

## 3. Score and consolidate — in python, not in your head
Score every candidate 1-10 on each lens, then run this in the scratchpad (reads TP/SL from `data/scan.csv`):
```python
import pandas as pd
S = {"NLR": (8,9,8,7,8), ...}   # cause, necessity, catalyst, basket, price
W = (.30,.20,.20,.15,.15)
scan = pd.read_csv("data/scan.csv", index_col=0)
df = pd.DataFrame(S, index=["cause","need","cat","basket","price"]).T
df["wtd"] = (df * W).sum(axis=1).round(2)
df["veto"] = df.cause <= 3
for c in ["theme","dd_52w","dip_score","stabilizing","tp_pct","sl_pct","rr"]: df[c] = scan[c].reindex(df.index)
df = df.sort_values("wtd", ascending=False)
df["theme_rank"] = 0; ok = ~df.veto
df.loc[ok, "theme_rank"] = df[ok].groupby("theme").cumcount() + 1
qual = ok & (df.cause >= 7) & (df.stabilizing.astype(bool) | (df.cat >= 7))
df["bucket"] = "watch"; df.loc[qual, "bucket"] = "alt"; df.loc[qual & (df.theme_rank == 1), "bucket"] = "buy"
df.loc[df.veto, "bucket"] = "avoid"
print(df.to_string())
```
Then set **my rank**: start from `wtd`, reorder only where a fact justifies it — one sentence per deviation.

## 4. Memo → `log/<DATE>-lite.md`
```
# etf-dip-pick <DATE> — lite (one agent, N searches, no verifier)

Regime: 2-3 lines.

| my # | ETF | theme | dd_52w | cause | need | cat | basket | price | wtd | TP | SL | R/R | bucket | why (1 line) |
...all candidates, in MY order...

Deviations from weighted score: one sentence each (or "none").
Buy: ...   Alt: ...   Watch: ...   Avoid: ...

Caveat: the one macro thing that flips the whole list.
Not done in lite: per-lens independent scoring (one head scored all five — price contamination risk), verifier
of load-bearing facts. Run the full /etf-dip-pick before sizing real money if the buys survive a week.
```
TP/SL/R/R from `data/scan.csv` (`tp_pct` `sl_pct` `rr`; blank for avoids). No sizing section. Append a line to
`SESSIONS.md`. Nothing is written to `output/`.
