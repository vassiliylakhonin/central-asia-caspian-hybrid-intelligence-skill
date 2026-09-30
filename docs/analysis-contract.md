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

## Human-readable claim contract

Every claim-bearing sentence and table cell carries one Axis A provenance tag:
`[primary]`, `[secondary]`, `[user-provided]`, `[inference]`, or `[analyst-judgment]`.
Use `[verify]` and `[stale-risk: YYYY-MM]` as optional action flags, not provenance.
A tag is supported only when the named source supports the specific claim.

Keep facts, assessments, assumptions, scenarios, and unknowns distinct. Account
for each material supplied claim as used, flagged-but-not-used, conflict-surfaced,
or out-of-scope. Surface source disagreements and assess source independence.

Answer with calibrated confidence when evidence suffices. Flag-but-don't-use an
unverified premise when independent analysis remains useful. Stop only the
dependent conclusion when entity identifiers, current designation status,
ownership/control, or transaction facts needed for that conclusion are missing.
Name the missing evidence; do not issue clearance or imply absence from a list
settles transaction permission.

Use four memo evidence modes: `live-source-backed`, `user-provided sources`,
`illustrative source packet`, and `reasoning-only`. `mixed` is a legacy transport
value only. When composed with GTTA, use its selected memo mode and confidence
labels (`Low` / `Moderate` / `High`); regional instructions add mechanisms and
evidence requirements rather than replacing the horizontal output contract.
