# Analysis Contract (Structured Output)

All decisions rendered by this skill MUST conform to the JSON schema defined in `schemas/compliance-decision.schema.json`.

Markdown essays are deprecated. The agent must return a parseable JSON block containing:
- The definitive `decision` (APPROVE, BLOCK, ESCALATE).
- A `confidence_score` between 0 and 1.
- The `autonomous_enforcement_action` code.
- A concise `rationale`.
