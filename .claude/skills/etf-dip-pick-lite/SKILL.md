---
name: etf-dip-pick-lite
description: Cheap single-agent version of etf-dip-pick — same scan, same five lenses (cause, necessity, catalyst, basket, price), same weights/veto/one-buy-per-theme rule, same TP/SL/R-R, dip#, deviations and $100k sizing sections, but ONE agent does everything in one pass with ~12 web searches total (one per theme, not per ETF or per lens) and writes only log/<DATE>-lite.md. No subagents, no output/<DATE>/ dossier or ballots, and only a 2-search spot-check instead of the full verifier. Use when the user says "lite", "quick", "cheap", "one pass", "no subagents", is near a usage limit, or wants a fast read on which sector/thematic ETFs are on sale / beaten down / lagging. For the full panel with audit trail use etf-dip-pick.
---

# etf-dip-pick-lite — one agent, one pass, one memo

Same question as `etf-dip-pick` (is this dip *on sale* or *broken*?), scored by you alone. Read
`../etf-dip-pick/lenses.md` for the five lenses, weights, veto and bucket rule — do not re-derive them.
Budget: **≤12 WebSearch total, no WebFetch** of filings/PDFs. Search snippets only.
The memo carries every section the full memo does (dip#, TP/SL/R-R footnote, deviations, $100k sizing) — those are
computed, not researched, so they cost nothing. What lite gives up is the five independent panelists and the
full verifier.

## 1. Scan
```
cd etf-dipfinder && uv run python scripts/scan.py     # full path if cwd is already inside
```
Read LEADERS first (where did the money go?), then CANDIDATES — every dip in the 15 deepest themes, grouped by
theme. `dip_score` is depth, not quality.

## 2. Research — one search per theme
The scan already groups candidates by `theme` — funds the same headline moves (URA/URNM/NLR; GLD/GDX/GDXJ; XLU alone).
One search per theme: `"<theme> ETF" selloff <Month YYYY> outlook`. Plus one regime search (10y yield, Fed odds).
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
df["dip_rank"] = df.dip_score.rank(method="min").astype(int)   # depth rank = memo's dip# column
df = df.sort_values("wtd", ascending=False)
df["theme_rank"] = 0; ok = ~df.veto
df.loc[ok, "theme_rank"] = df[ok].groupby("theme").cumcount() + 1
qual = ok & (df.cause >= 7) & (df.stabilizing.astype(bool) | (df.cat >= 7))
df["bucket"] = "watch"; df.loc[qual, "bucket"] = "alt"; df.loc[qual & (df.theme_rank == 1), "bucket"] = "buy"
df.loc[df.veto, "bucket"] = "avoid"
print(df.to_string())
```
Then set **my rank**: start from `wtd`, reorder only where a fact justifies it — one sentence per deviation.

## 3b. Spot-check the buy — 2 searches
The one thing that moved the answer last run. For the top buy only, name its two load-bearing facts (the ones that
would flip it if false) and spend up to 2 searches checking each is current, not a stale quote. Prefer the primary
number (term price, budget line, rate-odds print) over a headline about it. If a fact is stale or contradicted,
demote to watch and say so in Deviations. This is not the full verifier — it covers one fund, not the top 3.

## 4. Memo → `log/<DATE>-lite.md`
```
# etf-dip-pick <DATE> — lite (one agent, N searches, buy spot-checked, no panel)

Regime: 2-3 lines.

| my # | ETF | theme | dd_52w | dip# | cause | need | cat | basket | price | wtd | TP | SL | R/R | bucket | why (1 line) |
...all candidates, in MY order...

<4-line TP / SL / R/R / dip# / wtd footnote — same wording as the full memo, see log/2026-09-06.md>

Deviations from the bucket rule (cause ≥ 7 and (stabilizing or cat ≥ 7), first non-vetoed in theme = buy, rest = alt):
one sentence each (or "none"), including any demotion from the spot-check.
Buy: ...   Alt: ...   Watch: ...   Avoid: ...

## With $100k (`consolidate.py lite 100000 <final buys>`)
Risk-parity table: $ per buy, loss at SL, gain at TP, totals. Then the tranche call: buys sharing one macro date →
half now, half after it; independent → all in. One buy → do not risk-parity into it, use the per-position risk
budget (~1% of capital at the stop, `size_1pct` in scan.csv) and leave the rest cash. Stops as orders, TPs as alerts.

Since last memo: what changed vs the previous log/ entry — one or two lines, no searches (read the file).

Caveat: the one macro thing that flips the whole list.
Not done in lite: per-lens independent scoring (one head scored all five — price contamination risk); the verifier
covered the buy only, not the top 3. Run the full /etf-dip-pick before sizing real money if the buys survive a week.
```
TP/SL/R/R/dip# from `data/scan.csv` (`tp_pct` `sl_pct` `rr` `dip_score` rank; blank TP and R/R for avoids). Append a
line to `SESSIONS.md`. Nothing is written to `output/`.
