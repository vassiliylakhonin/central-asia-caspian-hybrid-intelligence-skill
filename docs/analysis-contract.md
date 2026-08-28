# Analysis Contract (Structured Output)

Machine-readable workflows may use `schemas/compliance-decision.schema.json` to
return a **review recommendation**. The object must contain:

- `recommendation`: `CONTINUE_REVIEW`, `REQUEST_EVIDENCE`,
  `ESCALATE_TO_HUMAN`, or `STOP_PENDING_REVIEW`;
- `evidence_sufficiency_score`: a 0–1 score about supplied evidence only;
- `suggested_reviewer_action`: a non-enforcing next step;
- `rationale` and `human_review_required: true`.

The schema cannot express legal clearance, sanctions status, transaction approval,
or authority to act. Human-readable analysis remains allowed when it follows the
provenance, uncertainty, and input-claim-accounting rules in this repository.
