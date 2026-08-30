# Run 2026-08-30 — prepared, not executed

Prompt bundles and the manifest are committed. **No outputs were generated and
nothing has been scored.**

| | |
|---|---|
| generating model | `claude-sonnet-5` (intended) |
| judge model | `gpt-5` (intended, different vendor family per B3.4) |
| cases | 6 (5 measured, 1 negative control) |
| archetypes covered | 5 |
| rubric SHA-256 | `6cb77dd8f7233c14…` |

## Why it stops here

The environment that prepared this run has no API access to a generating model,
and the only model present is the one that drafted the rubric and cases. Using
it as its own judge would violate B3.4 directly — a blind judge from a different
vendor family is the criterion, and self-judging is the specific bias it exists
to exclude.

Preparing without executing is deliberate rather than incomplete: it pins the
rubric and both skill files by hash at a known point, so whoever runs the
prompts cannot change the instrument afterwards without `score` refusing.

## To execute

```bash
# 1. Generate. 18 prompts, one output each, same model and same settings
#    across all three conditions.
for f in evals/specialist-lift/runs/2026-08-30/prompts/*.txt; do
  # send "$f" to claude-sonnet-5, save to
  # evals/specialist-lift/runs/2026-08-30/outputs/$(basename "$f" .txt).md
done

# 2. Score blind. For each case, present the three outputs to gpt-5 in the
#    order recorded under blinding_key in manifest.json, with condition labels
#    stripped, together with rubric.md. Ask for the satisfied item ids and the
#    applicable denominator per output.

# 3. Write scores.json:
#    {"cases": {"<case-id>": {"A": n, "B": n, "C": n}}}
#    Every prepared case must appear. `score` refuses otherwise.

python3 evals/specialist-lift/tools/lift_eval.py score 2026-08-30
```

## Reading the result

Check the negative control first. `negative-control-monitoring-cadence` is
model-risk governance with regional set dressing; C should not score above B. If
it does, the rubric is rewarding regional vocabulary rather than regional
mechanism, and the lift measured on the other five cases cannot be trusted —
fix the rubric, re-register it, and re-run everything.

Then check A against B. If A scores near B, the rubric is measuring something
every model already does and the C-over-B comparison means little.

Only then read C over B. A null result clears Bar 3 and means folding this
repo's regional content into the horizontal method.
