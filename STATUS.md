# STATUS.md

Honest status against the Definition of Done in [`AGENTS.md`](AGENTS.md). Update this file truthfully whenever a criterion is met or no longer met. Do not advance status without verifiable evidence.

**Last updated:** 2026-05-14 (Wave 4: B2.4 closed; platform differentiation implemented).

## Bar 1 — Early but credible

| Criterion | Status | Notes |
|---|---|---|
| B1.1 README follows the 14-section structure | ✅ met | See `README.md`. |
| B1.2 All four evidence modes demonstrated | ✅ met | `reasoning-only`, `illustrative source packet`, `live-source-backed`, `user-provided sources` each have at least one example. |
| B1.3 All preferred examples exist or are deferred with reason | ✅ met | All six AGENTS.md preferred examples exist. |
| B1.4 `evals/` has checklist + starter rubric + failure-modes with honest labels | ✅ met | No benchmark claim made. |
| B1.5 Validation passes on every commit to `main` | ✅ met | `python3 scripts/validate_skills.py` runs in CI and pre-commit. |
| B1.6 Honesty constraints observed everywhere | ✅ met | No fabricated citations, no legal/compliance/investment advice posture, no production-grade or screening claims. |

**Bar 1 — cleared.**

## Bar 2 — Externally validated specialist resource

| Criterion | Status | What is missing |
|---|---|---|
| B2.1 Source-anchored majority (≥50% of flagship examples) | ⚠ partial | Currently 5 of 12 flagship examples are source-anchored (4 `live-source-backed`, 1 `user-provided sources`) — 42%. Need at least 6 of 12 (50%) to clear. Three more `live-source-backed` examples added in Wave 3 closed half the gap. |
| B2.2 At least one external reviewer of an example and a rubric application, with findings incorporated or addressed | ❌ not met | All current scorecards are reviewer judgments by the author. No external reviewer recorded. |
| B2.3 At least three validated cases by domain practitioners, stored under `validated-cases/` | ❌ not met | Directory does not exist. No practitioner-attributed reviews. |
| B2.4 Platform differentiation or consolidation across `skills/{codex,claude,openclaw}` | ✅ met | Differentiation chosen. Claude variant adds `Claude Tool-Use Awareness` (retrieval → evidence mode shifting, prompt injection protection). Codex variant adds `Codex Agentic-Loop Awareness` (multi-step workflow, file output labeling, validation chaining). OpenClaw is the explicit canonical baseline with a section documenting the design choice. |
| B2.5 Honest real-use evidence or explicit "no real-use evidence" disclosure | ⚠ partial | AGENTS.md and README acknowledge no production usage; no positive real-use record exists yet. The honest disclosure is in place; the positive evidence is not. |
| B2.6 Source freshness discipline | ✅ met | Retrieval dates stated on `live-source-backed` examples; documented re-verification horizons per claim type in [docs/source-guide.md](docs/source-guide.md), including stale-source handling rules. Same-day re-verification required for sanctions / AML / export-controls operational decisions regardless of horizon. |
| B2.7 Independent rubric application by someone other than the author | ❌ not met | No external scorecard has been added. |

**Bar 2 — not cleared.**

## Open path to Bar 2

What would need to happen, in honest order:

1. Decide on platform differentiation vs consolidation for `skills/` variants (closes B2.4).
2. Add ≥3 source-anchored memos to push the ratio over half (closes B2.1).
3. Recruit at least one external reviewer for one memo and one rubric application; record their attribution (closes B2.2 and B2.7).
4. Run the skill against ≥3 real practitioner workflows; store outcomes in `validated-cases/` with practitioner attribution where consented (closes B2.3).
5. If real use happens, record it publicly with permission (closes B2.5 positively); if not, leave the negative disclosure as it stands.

None of these steps should be faked. Bar 2 is the hard bar. Most repos in this space conflate Bar 1 with Bar 2 and lose credibility on contact with practitioners.

## What this status is not

- Not a roadmap commitment with dates.
- Not an admission of failure — Bar 1 is a genuine accomplishment for an early-stage specialist skill.
- Not a marketing document. If a future contributor finds it inconvenient, that is the point.
