# Specialist-lift protocol 2

Compare A (no skill), B (GTTA only), and C (GTTA plus the complete regional reference
package). C includes the root, regional logic, risk archetypes, source guide,
currency watch, and analysis contract. All arms receive the same question, source
access (no tools), output budget, temperature, and model. Prompt length is an
explicit treatment difference; report token usage and truncation, and repeat
runs before generalizing. A equal to B does not invalidate C minus B: regional
coverage may be insensitive to the horizontal method.

The rubric is model-drafted from committed regional references and requires
author review. Coverage scoring is not factual accuracy or practitioner validation.
No outputs or results are included with this change. No maturity claim is advanced.

## Prepare and freeze

Choose the actual generator and a judge from a different vendor family before
preparation. Supply exact identifiers rather than treating example names as runs.

```bash
python evals/specialist-lift/tools/lift_eval.py prepare NEW_RUN_ID \
  --model GENERATOR_ID --model-family openai \
  --judge-model JUDGE_ID --judge-family anthropic \
  --horizontal-skill ../global-think-tank-analyst/SKILL.md \
  --output-budget 4096 --temperature 0 --seed 20260930
```

Commit `manifest.json`, `inputs/`, `prompts/`, and the separate `blinding-key.json`
before generation. The manifest pins complete source files, cases (including
context), rubric items and prompts. Use fresh contexts, the declared settings,
and no browsing in all arms. Save all three outputs per case under
`runs/NEW_RUN_ID/outputs/CASE_ID__condition_A.md` (and B/C). Retain provider logs,
settings actually used, token counts, truncation and retry records. The harness
checks saved bytes, not whether the provider followed those settings.

## Export blind packets

```bash
python evals/specialist-lift/tools/lift_eval.py judge NEW_RUN_ID
```

Commit the output receipts before judging. Send **only `judge/`** to the judge;
keep the manifest, model identities, and blinding key outside its context. Text
style may reveal an arm despite label removal; disclose that limitation. Export
refuses missing/empty outputs and freezes their hashes.

Write `scores.json` with every case, anonymous output and rubric item:

```json
{"cases":{"CASE_ID":{"output_1":{"S1":{"satisfied":true,"rationale":"Criterion matches this mechanism","evidence":"verbatim span from this output"}}}}}
```

This excerpt is a shape example, not a complete accepted score file. Include
`output_1`, `output_2`, `output_3` and every S item. Use `false` for unmet criteria;
use `null` only when the criterion is inapplicable to the question, consistently
across all three outputs. Every item needs a rationale; positive items need a
verbatim span. Numeric totals, including out-of-range scores, are rejected.

```bash
python evals/specialist-lift/tools/lift_eval.py score NEW_RUN_ID
python evals/specialist-lift/tools/validate_lift.py
```

The report calculates item totals, applicable denominators, raw and normalized
C-minus-B differences. Validation recomputes it from scores and output receipts.
Read controls before measured cases and publish null/negative results. A small
null result does not establish equivalence or justify retiring a skill; distinguish
underpowered measurement, loading defects, and substantive redundancy.

## Historical preparations

Protocol-1 preparations are retained unchanged for the audit trail. They cannot
be scored under protocol 2: prepare a new run with complete references and receipts.
No historical holdout or published model output is rewritten.
