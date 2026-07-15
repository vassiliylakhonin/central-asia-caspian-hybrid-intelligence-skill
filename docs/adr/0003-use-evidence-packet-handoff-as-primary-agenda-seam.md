# Use the evidence-packet handoff as the primary Agenda seam

Status: accepted — 2026-07-15

## Context

The specialist produces regional reasoning and may still participate in the older Agenda Intelligence `analyze` workflow. Agenda Intelligence MD v1.3.0 now leads with a smaller `claims[] + sources[]` evidence-packet contract. Evidence-mode mapping remains relevant for compatibility agent-evals but is not part of the new packet schema.

## Decision

The primary composition seam is an evidence-packet handoff containing externally checkable factual and quantitative claims plus caller-supplied source text. Regional assessments, scenarios, assumptions, and analyst judgments remain in the specialist memo. The older `analyze`, memo-schema, scoring, and MCP workflows remain compatibility paths.

## Consequences

- Regional mechanism logic stays in this authoring source.
- Agenda Intelligence can lint packet completeness without claiming sanctions, ownership, corridor, or factual verification.
- ADR 0001 still governs evidence-mode mapping when the compatibility `analyze` workflow is used.
- The handoff shape is documented and guarded in CI without vendoring Agenda Intelligence's schema.
