# etf-dip-pick — the five scoring lenses

Each lens is one subagent. It scores EVERY candidate 1-10 on its criterion only, ranks them, and
writes `output/<DATE>/score_<lens>.md`. Weights are applied by the orchestrator at consolidation.

| lens | weight | question | 10 looks like | 1 looks like |
|---|---|---|---|---|
| **cause** | 0.30 | Is the drop about *flows/rates/rotation* or did the *thesis* change? | pure rotation, thesis untouched, sellers are macro tourists | policy repeal / demand collapse / permanent re-rating; cheap keeps getting cheaper |
| **necessity** | 0.20 | How much does the world *need* this theme in 5-10y, and can anything (AI, substitute tech, policy) route around it? | civilisation-critical, no substitute, demand structurally rising | fashion trade, easily substituted, or dependent on a subsidy that's gone |
| **catalyst** | 0.20 | Is there a *dated, concrete* trigger in 3-12 months that reverses the flow? | named event, near, high-probability, market not yet positioned for it | "eventually mean-reverts" with nothing on the calendar |
| **basket** | 0.15 | Is the ETF itself a clean way to own the theme? Holdings quality, concentration, hidden exposures, structure, expense ratio, liquidity | diversified, profitable holdings, theme-pure, cheap, liquid | one stock = 25%, half the fund is a different theme, junky/unprofitable constituents, structural decay (futures roll, single-stock convert overhang) |
| **price** | 0.15 | Is this *unusually* cheap for this ETF, and is the long-term trend intact? Use dd_pctile, dd_z, rs_spy_12m, stabilizing, plus valuation vs own history (P/E, P/B, or commodity vs cost curve) | worst-decile drawdown vs own history, valuation at multi-year low, 12m trend still positive, bounce started | ordinary bad patch (dd_pctile > 0.25), valuation not cheap, 12m trend broken, still falling |

## Consolidation (orchestrator)
- `score = Σ weight × lens_score`.
- **Veto:** cause ≤ 3 → bucket = *avoid* regardless of score.
- **My rank** is the orchestrator's final order after reading all five ballots. It may deviate from the
  weighted score — every deviation gets one written sentence. It always deviates from `dip_score`
  (that is depth, not quality) — the memo shows both so the reader can see the gap.
- Buy = top of my rank AND cause ≥ 7 AND (stabilizing OR catalyst ≥ 7). Watch = rotation but still
  falling / catalyst far. Avoid = veto.

## Ballot format (every lens)
```
# <lens> — <DATE>
| rank | ETF | score | one-line reason (this lens only) | key source |
...all candidates...
Top-3 notes: 2 sentences each on the single most load-bearing fact, with source + date.
Disagreements with the dossier's first-pass memo: bullet list (or "none").
```
