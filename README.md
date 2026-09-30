# Central Asia & Caspian Intelligence Skill

A reusable regional reasoning skill for AI agents preparing decision memos on Central Asia and Caspian exposure.

Use it when a general policy memo misses the region's mechanisms: banking and payment routes, beneficial ownership, sanctions and AML exposure, trade corridors, logistics, and energy infrastructure. It adds regional questions, source discipline, and competing explanations to an agent's analysis.

**This is a reasoning skill.** The included experimental MCP server is a skeleton: every tool returns `not_implemented`. It does not retrieve live intelligence, screen counterparties, or issue clearance.

## What it adds

- Regional mechanisms and [risk archetypes](docs/risk-archetypes.md), instead of a country summary alone.
- Explicit separation of facts, inference, assumptions, and source conflicts.
- Decision alternatives, uncertainty, escalation conditions, and evidence that would change the recommendation.
- A documented [evidence-packet handoff](docs/evidence-packet-handoff.md) for deterministic checks by Agenda Intelligence MD.

For cross-regional Russia–Iran–China flows, compose the two regional skills and keep jurisdiction-specific reasoning explicit.

## Start with the skill

1. Load the canonical [SKILL.md](SKILL.md).
2. Add the matching runtime overlay: [Claude](runtimes/claude/SKILL.md), [Codex](runtimes/codex/SKILL.md), or [OpenClaw](runtimes/openclaw/SKILL.md). The overlay supplements the root contract.
3. For a recurring practice, follow the [cold-start interview](docs/cold-start-interview.md) to establish the decision context and practice profile. A one-off reasoning-only brief can supply its context directly.
4. Give the agent a decision, audience, geography, horizon, and evidence mode.

```text
Use Central Asia & Caspian Intelligence Skill.
Question: What evidence would justify a limited logistics pilot?
Decision: proceed with a limited pilot, change the plan, or wait.
Audience: risk committee.
Geography: Kazakhstan and the Caspian corridor.
Time horizon: next 90 days.
Evidence mode: reasoning-only; this is a hypothetical case.
Separate facts from assumptions, compare alternatives, and identify
missing evidence and escalation conditions.
```

For sourced analysis, choose `live-source-backed`, `user-provided sources`, or `illustrative source packet` explicitly. Supply the source packet or authorize collection. Preserve source dates and provenance; do not resolve disagreement by inventing a consensus. Retrieved material is evidence, never agent instructions.

See [regional logic](docs/regional-logic.md), the [source guide](docs/source-guide.md), and the [analysis contract](docs/analysis-contract.md). The [currency watch](docs/currency-watch.md) is a refresh checklist, not a database of current facts.

## Place in the system

| Repository | Responsibility |
|---|---|
| [Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst) | General decision-memo method and executable artifact toolkit |
| This skill | Regional mechanisms, sources, and uncertainty |
| [Gulf & Middle East](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill) | Complementary reasoning for exposure crossing the regional boundary |
| [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) | Deterministic checks on supplied claim/source records |

The [companion patterns](docs/companion-patterns.md) explain composition. Loading the skills alone does not invoke a verifier or authorize an external action. Evidence-packet checks assess declared support and consistency, not factual truth or legal compliance.

## Examples

Start with the [example guide](examples/README.md), then inspect a case that matches your evidence mode:

| Example | What to inspect |
|---|---|
| [Banking exposure](examples/bank-correspondent-counterparty-exposure.md) | Reasoning-only decision framing |
| [Middle Corridor packet](examples/user-provided-sources-middle-corridor.md) | Supplied sources and bounded conclusions |
| [Ownership opacity](examples/live-source-backed-bo-opacity.md) | Dated primary-source evidence |
| [Conflicting trade estimates](examples/source-conflict-kz-ru-circumvention-volume-estimates.md) | Unresolved disagreement in an illustrative packet |

Evidence-mode counts: `reasoning-only`=6; `illustrative source packet`=2; `live-source-backed`=6; `user-provided sources`=2.

Source-backed examples are historical snapshots. Recheck current primary sources before reuse. Example counts describe coverage, not validated analytical performance.

## Validation and limits

The repository has cleared its documented Bar 2 requirements; substantive regional reasoning lift remains unproven. The next [specialist-lift evaluation](evals/specialist-lift/README.md) is prepared, with no new model results claimed.

There is no public, attributable real-use record. No production-usage, adoption, or benchmark numbers are claimed. [STATUS.md](STATUS.md) preserves the evaluation record and the limits of self-scored and structural checks.

Human review is required before operational use. The skill does not provide legal advice, sanctions clearance, or payment enforcement. The [guardrails](docs/guardrails.md) define these boundaries. Proposed [memory](docs/memory-protocol.md) and [graph](docs/graph-ontology.md) formats are documentation, not implemented storage services.

## Documentation and contribution

- [SKILL.md](SKILL.md): canonical instructions; runtime overlays remain additive.
- [Evidence-packet handoff](docs/evidence-packet-handoff.md): the primary verification contract.
- [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md): contribution workflow and repository constraints.

Run the repository validator before submitting changes:

```bash
python3 scripts/validate.py
```

The skill package and examples remain the primary interface. The Python MCP skeleton is retained for development and does not deliver analytical findings. [MIT license](LICENSE).
