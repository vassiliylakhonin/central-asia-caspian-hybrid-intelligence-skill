# Skill Improvement Evals

This folder is a lightweight SkillOpt-style loop for improving the runtime skill variants in this repo without adding prompt-optimization infrastructure.

It is separate from the existing eval layers:

- `evals/agent-eval/` records with/without structural deltas for Agenda Intelligence routing.
- `evals/adversarial/` contains domain traps for response-mode behavior.
- `evals/starter-rubric.md` scores finished memos.
- `evals/skill-improvement/` scores proposed edits to `skills/{codex,claude,openclaw}/SKILL.md` before accepting them.

This is not a factual benchmark, model-quality comparison, practitioner review, or Bar 2 evidence. It is a change-control surface for the skill instructions.

## Files

- `cases/central-asia-caspian.jsonl` - validation cases for the runtime skill variants.
- `rubric.md` - manual scoring rubric for skill responses.
- `runs/central-asia-caspian-baseline.md` - baseline against the current skill contract.
- `tools/validate_cases.py` - local JSONL case validator.

## Workflow

1. Add or update cases before changing skill instructions.
2. Score the current skill against `val` cases.
3. Make the smallest useful edit across the relevant skill variants.
4. Re-score the same `val` cases.
5. Accept the edit only if the validation score improves and no boundary regresses.

## Acceptance Rule

Accept a skill edit only when all are true:

- Average `val` score improves by at least `0.5` on the 10-point rubric, or a critical boundary failure is fixed.
- No `val` case drops by more than `1.0`.
- The edit preserves the repo boundary: no screening claim, no legal/compliance/investment advice, no factual verification claim, no live retrieval claim unless retrieval actually happened.
- The edit stays short enough that the runtime variants remain usable.

## Validate Cases

```bash
python3 evals/skill-improvement/tools/validate_cases.py \
  evals/skill-improvement/cases/central-asia-caspian.jsonl
```
