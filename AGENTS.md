# AGENTS.md

Permanent repository instructions for AI agents working on this codebase.

## Purpose of this repo

This repo is a **vertical domain skill** for Central Asia and the Caspian region — sanctions, AML, banking, corridors, logistics, energy and geopolitical risk. It is not infrastructure, not an agent framework, not an MCP server, not a sanctions screening engine, and not a factuality verifier.

## Hard rules

- **Preserve evidence limitations.** Every example, doc and skill variant must keep an explicit notion of evidence mode and uncertainty labels (`Verified` / `Plausible` / `Judgment` / `Unknown`).
- **Examples must state evidence mode.** If an example is reasoning-only with no retrieved sources, label it: *"Evidence mode: illustrative / reasoning-only. This example does not verify live sanctions or legal status."*
- **No fake citations.** Do not fabricate URLs, list IDs, case numbers, statute citations, or enforcement records.
- **No legal, compliance, sanctions, AML, tax, audit or investment advice.** Use cautious language: *may consider*, *subject to review*, *depends on enforcement or regulation*. Never *guaranteed*, *no risk*, *fully compliant*.
- **Do not claim live sanctions screening or live source retrieval.** This repo does neither.
- **Do not invent metrics, benchmarks, adoption numbers or production-usage claims.**
- **Mechanism before implication.** Always explain how a risk transmits before asserting what it means.
- **Tight regional scope.** Central Asia is the core frame. Caspian is included only when material. Russia / China / EU / UK / US / Middle East / South Caucasus are included only when they change the mechanism, exposure, leverage or decision. See `docs/regional-logic.md`.
- **No scope creep.** Do not turn this repo into a generic agent framework, MCP server, CLI product, factuality verifier, compliance tool or screening engine.

## Portfolio boundaries

- This repo = Central Asia + Caspian specialist regional/corridor risk reasoning.
- **Global Think Tank Analyst** = broader strategic-risk memo workflow.
- **Agenda Intelligence MD** = schemas / validation / evidence audit / eval / CLI / MCP / CI.

Reference Agenda Intelligence MD for validation/eval workflows; do not duplicate them here.

## When editing skill files

`skills/openclaw/SKILL.md`, `skills/codex/SKILL.md`, `skills/claude/SKILL.md` must remain consistent on:

- positioning (specialist regional skill)
- evidence mode and uncertainty labels
- no legal/compliance/investment advice
- mechanism-first reasoning
- Central Asia / Caspian scope
- role-based implications
- trigger points
- confidence and unknowns

Preserve platform-specific formatting (e.g. Claude's YAML frontmatter). Do not bloat the files.

## Validation

If you change skill files, run:

```bash
python3 scripts/validate_skills.py
```

The validator checks structure, required phrases, forbidden determinative claims and code-fence balance. It does not validate factuality of skill outputs.

## Style

- Default to no comments in code; prefer concise prose in docs.
- Do not add benchmark tables, adoption metrics or release-count badges that are not real.
- Do not introduce heavy dependencies for tooling.
