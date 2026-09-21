# etf-dip-pick — the five scoring lenses

Four lenses are subagents: each scores EVERY candidate 1-10 on its criterion only, ranks them, and
writes `output/<DATE>/score_<lens>.md`. **price is not a subagent** - it is `consolidate.price_score()`,
computed from `dd_pctile`, `rs_spy_12m` and `stabilizing` and written into `scan.csv` as `price_score`. Weights are applied by the orchestrator at consolidation.

| lens | weight | question | 10 looks like | 1 looks like |
|---|---|---|---|---|
| **cause** | 0.30 | Is the drop about *flows/rates/rotation* or did the *thesis* change? | pure rotation, thesis untouched, sellers are macro tourists | policy repeal / demand collapse / permanent re-rating; cheap keeps getting cheaper |
| **necessity** | 0.20 | How much does the world *need* this theme in 5-10y, and can anything (AI, substitute tech, policy) route around it? | civilisation-critical, no substitute, demand structurally rising | fashion trade, easily substituted, or dependent on a subsidy that's gone |
| **catalyst** | 0.20 | Is there a *dated, concrete* trigger in 3-12 months that reverses the flow? | named event, near, high-probability, market not yet positioned for it | "eventually mean-reverts" with nothing on the calendar |
| **basket** | 0.15 | Is the ETF itself a clean way to own the theme? Holdings quality, concentration, hidden exposures, structure, expense ratio, liquidity | diversified, profitable holdings, theme-pure, cheap, liquid | one stock = 25%, half the fund is a different theme, junky/unprofitable constituents, structural decay (futures roll, single-stock convert overhang) |
| **price** | 0.15 | *Computed, not voted.* Is this unusually cheap for **this** ETF, and is the long-term trend intact? `depth(dd_pctile: <=.02 -> 5, <=.05 -> 4, <=.10 -> 3, <=.25 -> 2, else 1) + trend(rs_spy_12m: >0 -> 3, >-.15 -> 2, >-.35 -> 1, else 0) + 2 if stabilizing` | worst-decile drawdown vs own history, 12m trend still positive, bounce started | ordinary bad patch (dd_pctile > 0.25), 12m trend broken, still falling |

## Anchors — score the band first, then move at most 1 point for a named reason

A rubric with only 10 and 1 defined leaves 2-9 to taste, and taste resamples: across
2026-09-17/18/21, on price moves under 3%, catalyst went 7 -> 4 -> 9 for six different funds and
21 scores reversed direction by 3+ points. Pick the band a fund falls in, say which band in the
ballot's reason column, and only then adjust by one point with a stated fact. A score two or more
points from where its band puts it is a deviation and needs its own sentence.

**cause** — 10 pure rotation, thesis untouched · **7** mean-reversion inside an intact trend, or a
real but temporary headwind (rates, input costs) with demand unchanged · **5** sentiment or fear,
no thesis change *established* and no evidence it is only flows · **3** a fundamental impairment
that may be permanent (this is the veto line) · 1 policy repeal, demand collapse, permanent re-rating.

**necessity** — 10 civilisation-critical, no substitute, demand structurally rising · **7**
structurally growing but substitutable, or with a visible competing technology · **5** real demand,
cyclical, no structural growth claim · **3** discretionary, or demand rests on conditions that may
not hold · 1 fashion trade, easily substituted, or subsidy-dependent with the subsidy gone.

**catalyst** — the band is set by *who confirmed the date* and *whether the outcome is one-sided*,
never by how exciting the theme is:
- **10** date confirmed by the company or agency itself, inside 90 days, outcome materially
  one-sided for the theme, market not yet positioned
- **8** confirmed date 3-12 months out; or a confirmed near date that is material but partly priced
- **6** scheduled event whose outcome cuts both ways (an FOMC meeting, a CPI print). Symmetric
  events are *timing*, not direction, and cannot score 7+ on the calendar alone
- **4** expected on cadence but no date confirmed (a quarterly print not yet scheduled, a bill with
  no floor date)
- **2** nothing on the calendar; "eventually mean-reverts"

**basket** — 10 diversified, profitable, theme-pure, cheap, liquid · **7** theme-pure and liquid
with one visible flaw (top-ten above ~50%, or fee above ~0.60%) · **5** two such flaws, or ~a third
of the fund is a different theme · **3** a single name above ~20%, or half the fund off-theme ·
1 one stock at 25%, junky constituents, structural decay (futures roll, convert overhang).

**price** is not scored by a panelist at all — see the table above; it is `price_score()`.

## Consolidation (orchestrator)
- `score = Σ weight × lens_score`.
- **Veto:** cause ≤ 3 → bucket = *avoid* regardless of score.
- **My rank** is the orchestrator's final order after reading all five ballots. It may deviate from the
  weighted score — every deviation gets one written sentence. It always deviates from `dip_score`
  (that is depth, not quality) — the memo shows both so the reader can see the gap.
- Bucket is computed by `consolidate.py`: buy = cause ≥ 7 AND (stabilizing OR catalyst ≥ 7) AND not thin AND first
  non-vetoed in its theme; alt = same but not first; avoid = veto; else watch. Thin = R/R < 1.3:
  wtd −1 and never buy — vol-normalised depth, so a −10% XLU dip can be deeper than a −20% NLR dip; thin names stay in the table but sink. Overrides go in the memo as deviations.

## Ballot format (every lens)
```
# <lens> — <DATE>
| rank | ETF | score | one-line reason (this lens only) | key source |
...all candidates...
Top-3 notes: 2 sentences each on the single most load-bearing fact, with source + date.
Disagreements with the dossier's first-pass memo: bullet list (or "none").
```
