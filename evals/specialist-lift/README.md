# Specialist-lift suite (Bar 3)

Measures the claim this repository is named for: that the Central Asia + Caspian
vertical changes the **substance** of an answer beyond the horizontal method
(`global-think-tank-analyst`) on its own.

Bar 2 measured structure. A structural rubric shows a large delta for any
well-formed skill file, and every Bar 2 writeup says so. This suite is the part
that was never run.

**Status: not attempted.** The harness is here; the rubric is not written. See
[`../../STATUS.md`](../../STATUS.md).

## What this is not

Not factual accuracy. Not compliance, sanctions, AML or screening validation.
Not practitioner validation. Not a labelled dataset, and never a benchmark. It
measures substantive coverage against a rubric the author wrote, on a small
number of cases.

## The protocol

Three conditions per case, identical but for which method files precede the
question:

| | loaded |
|---|---|
| **A** | nothing |
| **B** | horizontal method only |
| **C** | horizontal method + this vertical |

**B is the comparison.** A exists only to show the rubric can discriminate at
all — if A scores near B, the rubric is measuring something every model already
does, and it needs rewriting before any conclusion is drawn from C.

## Running it

```bash
# 1. Write the rubric. This is the step that decides whether the measurement
#    means anything, and the only one that cannot be automated: it takes the
#    regional knowledge this repo claims to encode.
$EDITOR evals/specialist-lift/rubric.md

# 2. Define cases: at least 5, spanning at least 3 archetypes from
#    docs/risk-archetypes.md, including at least one negative control.
$EDITOR evals/specialist-lift/cases/

# 3. Emit prompt bundles and pin what is being measured.
python3 evals/specialist-lift/tools/lift_eval.py prepare 2026-09-01 \
  --model <generating-model-id> \
  --judge-model <different-vendor-family-id> \
  --horizontal-skill ../global-think-tank-analyst/SKILL.md

# 4. Run every prompt through the model. Save outputs as
#    runs/<run-id>/outputs/<case_id>__condition_<A|B|C>.md

# 5. Score blind. Present outputs to the judge in the randomised order recorded
#    in manifest.json, with condition labels stripped. Write runs/<run-id>/
#    scores.json as {"cases": {"<case-id>": {"A": n, "B": n, "C": n}}}.

# 6. Produce the report.
python3 evals/specialist-lift/tools/lift_eval.py score 2026-09-01
```

## What the harness refuses to do

Two anti-criteria are enforced mechanically rather than trusted, because both
describe things an author does to themselves under mild pressure:

- **The rubric is hashed at `prepare` time.** `score` refuses to run if it
  changed since. Editing the rubric after reading outputs is the easiest way to
  manufacture lift.
- **Every prepared case must be scored.** `score` refuses and names any case
  that is missing. Publishing only the cases that came out well is the other
  easy way, and it is the one a reader cannot detect from the outside.

`tools/validate_lift.py` additionally rejects a judge from the same vendor
family as the generating model, a suite with no negative control, an archetype
that is not in `docs/risk-archetypes.md`, and a report that omits a prepared
case or carries no scope statement. `tests/test_lift_harness.py` proves each
refusal actually fires.

## Reading the result

A **null result clears Bar 3.** If the vertical demonstrably adds nothing, the
honest outcome is to fold this repo's regional content into the horizontal
method and retire it as a separate skill. That is a successful outcome.

A vertical that cannot demonstrate lift is not a failed repo. An unmeasured one
is.
