# Central Asia + Caspian Hybrid Intelligence Skill

<p align="left">
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/stargazers"><img src="https://img.shields.io/github/stars/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub stars"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/network/members"><img src="https://img.shields.io/github/forks/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub forks"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/blob/main/LICENSE"><img src="https://img.shields.io/github/license/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/validate.yml?branch=main&style=for-the-badge" alt="Validate"></a>
</p>

**Central Asia & Caspian specialist skill for AI agents working on sanctions, AML, corridors, banking, logistics, energy and geopolitical risk.**

Generic LLMs often produce broad regional commentary on Central Asia and the Caspian. This skill helps agents produce **mechanism-first, evidence-aware, decision-useful** risk analysis for the region. It emphasizes transmission channels, routing exposure, actor incentives, uncertainty, trigger points and role-based implications instead of general geopolitical narration.

## What it does

- frames regional questions as concrete risk or strategy problems
- explains mechanisms before implications
- separates `Verified` / `Plausible` / `Judgment` / `Unknown`
- maps risk transmission channels across banking, payments, routing, ownership and corridors
- supports sanctions, AML, banking, corridor, energy, logistics and political-economy analysis
- identifies leverage shifts and actor incentives
- produces trigger points and watch-next indicators
- supports role-based implications for banks, fintechs, investors, logistics operators, energy teams and analysts

## What it is not

- not legal advice
- not compliance advice
- not sanctions screening
- not AML transaction monitoring
- not factuality verification by itself
- not a live source retriever
- not a risk database
- not an agent framework
- not a replacement for human analyst or counsel review

## Relationship to the Agenda Intelligence stack

This skill is one piece of a wider portfolio. Each repo has a distinct role; do not blur them.

- **Central Asia + Caspian Hybrid Intelligence Skill** (this repo) — specialist regional/corridor-risk reasoning, domain-specific memo structure, risk-transmission logic, sanctions/AML/corridor analysis patterns.
- **Global Think Tank Analyst** — broader strategic-risk memo workflow, general policy-risk analysis, scenario and red-team memo modes.
- **Agenda Intelligence MD** — schemas, validation, evidence audit, scoring, and CLI/MCP/CI tooling where implemented.

> Use this repo for specialist Central Asia + Caspian reasoning. Use Global Think Tank Analyst for broader strategic-risk memo workflows. Use Agenda Intelligence MD to validate, score or audit outputs where that functionality is implemented.

This repo does **not** itself perform Agenda Intelligence MD validation, schema enforcement on outputs, or live source retrieval.

## Integration / status

| Environment | Status | Notes |
|---|---|---|
| Codex | Supported | Uses `skills/codex/SKILL.md` and `AGENTS.md` |
| Claude | Supported | Uses `skills/claude/SKILL.md` (YAML frontmatter) |
| OpenClaw / ClawHub | Supported if current packaging exists | `skills/openclaw/SKILL.md` |
| ChatGPT / other LLMs | Compatible by context | Paste or attach the relevant `SKILL.md` |
| Agenda Intelligence MD | Companion validation layer | Use for schemas / evidence audit / eval / CLI / MCP if needed |
| MCP server | Not implemented here | Use companion tooling if available |
| Sanctions screening | Not implemented | This is not a screening engine |
| Live retrieval | Not implemented | Requires external sources, tools, or user-provided source packets |

## Before / after

**Before — generic LLM answer:**
- broad regional commentary
- vague "monitor sanctions"
- no transmission mechanism
- no actor incentives
- no trigger points
- no evidence boundaries

**After — skill-style answer:**
- primary driver
- mechanism (how the risk transmits)
- exposure map (where it concentrates)
- actor incentives and leverage
- uncertainty labels (`Verified` / `Plausible` / `Judgment` / `Unknown`)
- trigger points and watch-next indicators
- role-based implications (bank, fintech, investor, operator)
- evidence mode stated explicitly

A worked memo is in [examples/fintech-sanctions-routing.md](examples/fintech-sanctions-routing.md).

## Quick start

### Codex / Claude / ChatGPT

Use the corresponding `SKILL.md` file as the operating instruction in your agent setup:

- `skills/codex/SKILL.md`
- `skills/claude/SKILL.md`
- `skills/openclaw/SKILL.md`

### Validation

```bash
python3 scripts/validate_skills.py
```

The validator checks frontmatter, required analytical sections, source-handling discipline, safety disclaimers, unsafe determinative language and fenced-code balance across the skill variants. It does **not** validate factuality of any output produced by the skill.

## What's inside

- `skills/` — skill variants for Codex, Claude and OpenClaw
- `examples/fintech-sanctions-routing.md` — flagship worked memo
- `docs/source-guide.md` — recommended source classes for source-backed workflows
- `docs/risk-archetypes.md` — Central Asia / Caspian risk archetypes
- `docs/regional-logic.md` — when to include which geography
- `evals/checklist.md` — review checklist for outputs
- `evals/failure-modes.md` — common failure modes
- `AGENTS.md` — permanent repo instructions for agents
- `scripts/validate_skills.py` — dependency-free skill metadata validation

## Honesty notes

- This skill helps **structure analysis**; it does not verify facts on its own.
- Any factual claim about a person, entity, sanctions status, license, or enforcement action requires source-backed verification through external retrieval, user-provided sources, or companion tooling.
- This repo does not provide legal, regulatory, sanctions, AML, tax, audit or investment advice. It does not replace professional review.
- No production-usage, adoption or benchmark numbers are claimed.

## Disclaimer

This repository provides analytical guidance only and does not constitute legal, regulatory, sanctions, AML, tax, audit or investment advice. Outputs require source-backed verification before any operational, compliance or commercial use.
