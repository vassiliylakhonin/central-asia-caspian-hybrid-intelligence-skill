# STATUS.md

Honest status against the Definition of Done in [`AGENTS.md`](AGENTS.md). Update this file truthfully whenever a criterion is met or no longer met. Do not advance status without verifiable evidence.

**Last updated:** 2026-05-20 (Bar 2 agent-validation path completed: three agent-eval delta cases are recorded, including one `mixed` evidence-mode mapping case through Agenda Intelligence `analyze`.)

## Bar 1 — Early but credible

| Criterion | Status | Notes |
|---|---|---|
| B1.1 README follows the 15-section structure | ✅ met | See `README.md`. |
| B1.2 All four evidence modes demonstrated | ✅ met | `reasoning-only`, `illustrative source packet`, `live-source-backed`, `user-provided sources` each have at least one example. |
| B1.3 All preferred examples exist or are deferred with reason | ✅ met | All six AGENTS.md preferred examples exist. |
| B1.4 `evals/` has checklist + starter rubric + failure-modes with honest labels | ✅ met | No benchmark claim made. |
| B1.5 Validation passes on every commit to `main` | ✅ met | `python3 scripts/validate_skills.py` runs in CI and pre-commit. |
| B1.6 Honesty constraints observed everywhere | ✅ met | No fabricated citations, no legal/compliance/investment advice posture, no production-grade or screening claims. |

**Bar 1 — cleared.**

## Bar 2 — Agent-validated specialist resource

| Criterion | Status | What is missing |
|---|---|---|
| B2.1 Source-anchored majority (≥50% of flagship examples) | ✅ met (at threshold, no margin) | 8 of 16 flagship examples are source-anchored (6 `live-source-backed`, 2 `user-provided sources`) — 50%. Wave 8 added an `illustrative source packet` source-conflict-surfacing demonstrator (KZ→RU CHPL-circumvention volume estimates), which is not source-anchored; the ratio dropped from 53% to exactly the 50% threshold. To restore margin, the next added example should be `live-source-backed` or `user-provided sources`. |
| B2.2 Agent-eval delta documented (≥3 cases) | ✅ met | Three completed cases exist: `2026-05-20-correspondent-exposure.md`, `2026-05-20-customs-mirror-statistics-anomaly.md`, and `2026-05-20-caspian-corridor-chokepoint.md`. |
| B2.3 Evidence-mode mapping exercised through `analyze` | ✅ met | `2026-05-20-customs-mirror-statistics-anomaly.md` maps upstream `live-source-backed` specialist material to Agenda Intelligence `analyze` as `mixed`, not `live_source_backed`. |
| B2.4 Platform differentiation or consolidation across `skills/{codex,claude,openclaw}` | ✅ met | Differentiation chosen. Claude variant adds `Claude Tool-Use Awareness` (retrieval → evidence mode shifting, prompt injection protection). Codex variant adds `Codex Agentic-Loop Awareness` (multi-step workflow, file output labeling, validation chaining). OpenClaw is the explicit canonical baseline with a section documenting the design choice. All three gained Profile Assumptions and Optional User Calibration. |
| B2.5 Honest real-use evidence or explicit "no real-use evidence" disclosure | ✅ met via negative disclosure | README states no production-usage, adoption or benchmark numbers are claimed; this STATUS file states no positive real-use record exists yet. |
| B2.6 Source freshness discipline | ✅ met | Retrieval dates stated on `live-source-backed` examples; documented re-verification horizons per claim type in [docs/source-guide.md](docs/source-guide.md), including stale-source handling rules. Same-day re-verification required for sanctions / AML / export-controls operational decisions regardless of horizon. |
| B2.7 Agent-eval honesty discipline | ✅ met | All three completed agent-evals state structural-only limitations and avoid factual-verification, model-quality, aggregate-benchmark and practitioner-validation claims. |
| B2.8 Practitioner review (optional, audience-gated) | optional / not required for Bar 2 | No `validated-cases/` directory yet. Add only if the downstream audience includes practitioner buying-side trust, not as the hard agent-integration gate. |

**Bar 2 — cleared for agent integration.**

## Open path to Bar 2

What would need to happen, in honest order:

1. ~~Decide on platform differentiation vs consolidation for `skills/` variants (closes B2.4).~~ Done — Wave 4.
2. ~~Add more source-anchored memos to push the ratio over half (closes B2.1).~~ Done — Wave 6 raised ratio to 54% (7 of 13); B2.1 met.
3. ~~Add two more agent-eval delta cases under `evals/agent-eval/` using the Agenda Intelligence methodology (closes B2.2).~~ Done — `customs-mirror-statistics-anomaly` and `caspian-corridor-chokepoint`.
4. ~~Make the customs / mirror-statistics agent-eval source-backed through the product shell, mapping specialist source-backed material to `user_provided` or `mixed` (closes B2.3).~~ Done — mapped to `mixed`.
5. ~~Keep each agent-eval explicitly structural-only: no factual verification, no model-quality comparison, no aggregate benchmark claim (closes B2.7 as the set grows).~~ Done for the three current cases.
6. If real agent-integrator use happens, record it publicly with permission (strengthens B2.5 positively); if not, leave the negative disclosure as it stands.
7. If the audience expands to practitioner buying-side trust, add practitioner reviews under `validated-cases/`; do not treat them as required for agent-first Bar 2.

None of these steps should be faked. Bar 2 is now cleared as a hard agent-integration bar, not as practitioner validation. Most repos in this space conflate a polished prompt with evidence that it improves agent output structure.

## What this status is not

- Not a roadmap commitment with dates.
- Not an admission of failure — Bar 1 is a genuine accomplishment for an early-stage specialist skill.
- Not a marketing document. If a future contributor finds it inconvenient, that is the point.
