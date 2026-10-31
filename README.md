# Central Asia & Caspian Intelligence Skill

A reusable regional reasoning skill for AI agents preparing decision memos on Central Asia and Caspian exposure.

Use it when a general policy memo misses the region's mechanisms: banking and payment routes, beneficial ownership, sanctions and AML exposure, trade corridors, logistics, and energy infrastructure risk.

This is a reasoning skill and decision framework, not a live intelligence feed. The included experimental MCP server is a skeleton: every tool returns `not_implemented`. It does not retrieve live intelligence, screen counterparties, or issue clearances.

## Why this project exists

Regional exposure questions are often reduced to generic geopolitical summaries. This skill gives an agent a more structured way to reason about Central Asia and the Caspian corridor:

- mechanism-first analysis, not just country summaries
- explicit separation of facts, inference, assumptions, and source conflicts
- decision alternatives, escalation conditions, and evidence that would change the recommendation
- a clear handoff for deterministic evidence checks

It is designed to improve the quality of strategic reasoning, not to replace human judgment or legal review.

## What this project includes

- a reusable reasoning contract in [SKILL.md](SKILL.md)
- runtime overlays for [Claude](runtimes/claude/SKILL.md), [Codex](runtimes/codex/SKILL.md), and [OpenClaw](runtimes/openclaw/SKILL.md)
- worked examples in [examples/README.md](examples/README.md)
- an evidence handoff to [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md)
- regional guardrails and explicit uncertainty handling

## Choose a starting point

| Your task | Worked example | Evidence to inspect |
| --- | --- | --- |
| Banking or counterparty exposure | [Open example](examples/bank-correspondent-counterparty-exposure.md) | Reasoning-only decision framing |
| A Middle Corridor source pack | [Open example](examples/user-provided-sources-middle-corridor.md) | Claims tied to supplied sources |
| Beneficial-ownership uncertainty | [Open example](examples/live-source-backed-bo-opacity.md) | A dated source-backed example |

## Start with the skill

1. Load the canonical [SKILL.md](SKILL.md).
2. Add the matching runtime overlay: [Claude](runtimes/claude/SKILL.md), [Codex](runtimes/codex/SKILL.md), or [OpenClaw](runtimes/openclaw/SKILL.md).
3. For a recurring practice, follow the [cold-start interview](docs/cold-start-interview.md) to establish decision context and practice profile.
4. Give the agent a concrete decision brief.

Example prompt:

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

For sourced analysis, choose `live-source-backed`, `user-provided sources`, or `illustrative source packet` explicitly. Supply the source packet or authorize collection. Preserve source dates and disclose unresolved source conflicts.

See [regional logic](docs/regional-logic.md), the [source guide](docs/source-guide.md), and the [analysis contract](docs/analysis-contract.md). The [currency watch](docs/currency-watch.md) is a supporting regional lens for financial exposure analysis.

## Place in the system

| Repository | Responsibility |
| --- | --- |
| [Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst) | General decision-memo method and executable artifact toolkit |
| This skill | Regional mechanisms, sources, and uncertainty |
| [Gulf & Middle East](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill) | Complementary reasoning for exposure crossing the regional boundary |
| [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) | Deterministic checks on supplied claim/source records |

The [companion patterns](docs/companion-patterns.md) explain composition. Loading the skills alone does not invoke a verifier or authorize an external action. Evidence-packet checks assess declared support and consistency; they do not validate real-world facts on their own.

## Examples

For maritime fleet and port/rail questions, the [Caspian capacity reference](docs/maritime-capacity-reasoning.md) distinguishes payload, cycle time, interface constraints, and demand constraints. It adds reasoning guidance, not a live data service.

Start with the [example guide](examples/README.md), then inspect a case that matches your evidence mode:

| Example | What to inspect |
| --- | --- |
| [Banking exposure](examples/bank-correspondent-counterparty-exposure.md) | Reasoning-only decision framing |
| [Middle Corridor packet](examples/user-provided-sources-middle-corridor.md) | Supplied sources and bounded conclusions |
| [Ownership opacity](examples/live-source-backed-bo-opacity.md) | Dated primary-source evidence |
| [Conflicting trade estimates](examples/source-conflict-kz-ru-circumvention-volume-estimates.md) | Unresolved disagreement in an illustrative packet |

Evidence-mode counts: `reasoning-only`=6; `illustrative source packet`=2; `live-source-backed`=6; `user-provided sources`=2.

Source-backed examples are historical snapshots. Recheck current primary sources before reuse. Example counts describe coverage, not validated analytical performance.

## What this is not

This project does not:

- provide live regional intelligence feeds
- screen counterparties or sanctions exposure automatically
- certify legal, regulatory, or sanctions compliance
- authorize external action or payment decisions
- substitute for a human reviewer in operational decisions

The skill is a structured reasoning and evidence-handling layer. The actual decision remains with a human or an authorized process.

## Validation and limits

The repository has cleared its documented Bar 2 requirements; substantive regional reasoning lift remains unproven. The next [specialist-lift evaluation](evals/specialist-lift/README.md) tracks the relevant quality frontier.

There is no public, attributable real-use record. No production-usage, adoption, or benchmark numbers are claimed. [STATUS.md](STATUS.md) preserves the evaluation record and the limits of self-scoring and self-checking.

Human review is required before operational use. The skill does not provide legal advice, sanctions clearance, or payment enforcement. The [guardrails](docs/guardrails.md) define these boundaries.

## Documentation and contribution

- [SKILL.md](SKILL.md): canonical instructions; runtime overlays remain additive
- [Evidence-packet handoff](docs/evidence-packet-handoff.md): the primary verification contract
- [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md): contribution workflow and repository constraints

Run the repository validator before submitting changes:

```bash
python3 scripts/validate.py
```

The skill package and examples remain the primary interface. The Python MCP skeleton is retained for development and does not deliver analytical findings.

## License

[MIT license](LICENSE).
