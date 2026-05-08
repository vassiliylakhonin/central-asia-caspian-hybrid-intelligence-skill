# AGENTS.md

## Project identity

Central Asia + Caspian Hybrid Intelligence Skill is a vertical specialist skill for AI agents working on Central Asia, the Caspian region, sanctions, AML, banking, logistics, corridors, energy, infrastructure and geopolitical risk.

Use this positioning:

> Central Asia & Caspian specialist skill for AI agents working on sanctions, AML, corridors, banking, logistics, energy and geopolitical risk.

This repo is a domain skill, not an infrastructure product.

## Relationship to the broader stack

Agenda Intelligence MD:
- validation
- schemas
- evidence audit
- scoring
- CLI / MCP / CI tooling where implemented

Global Think Tank Analyst:
- broad strategic-risk memo workflows
- general policy-risk analysis
- scenario and red-team memo modes

Central Asia + Caspian Hybrid Intelligence Skill:
- specialist regional/corridor-risk reasoning
- domain-specific risk transmission logic
- sanctions / AML / banking / logistics / energy / corridor analysis patterns

Do not duplicate Agenda Intelligence MD inside this repo.
Do not turn this repo into a CLI, MCP server, screening engine, or validation platform unless explicitly requested.

## Scope

Core scope:
- Central Asia
- Caspian region when material
- sanctions and AML exposure
- routing and transshipment risk
- correspondent banking and payment rails
- beneficial ownership opacity
- logistics chokepoints
- energy and infrastructure corridors
- Russia / China / EU / Middle East connectivity when material
- state capacity and political economy
- strategic competition and leverage

Expand geography only when it changes the mechanism, risk exposure, leverage, or decision. Do not expand geography for decoration.

## Evidence rules

Every example must state its evidence mode:
- live-source-backed
- user-provided sources
- illustrative source packet
- reasoning-only

Do not fabricate:
- citations
- sanctions designations
- legal conclusions
- compliance conclusions
- company facts
- ownership structures
- enforcement actions
- dates
- statistics
- prices
- regulatory changes

If facts are not verified, say so.

Use labels where helpful:
- Verified
- Plausible
- Judgment
- Unknown

## Safety and limitation rules

This repo must not claim to provide:
- legal advice
- compliance advice
- sanctions screening
- AML transaction monitoring
- investment advice
- factual verification by itself
- live source retrieval by itself
- guaranteed correctness
- production-grade risk controls

Avoid exaggerated claims:
- revolutionary
- best-in-class
- fully autonomous
- guarantees compliance
- solves hallucinations
- detects sanctions evasion

Use careful language:
- helps structure analysis
- supports analyst-style reasoning
- requires source-backed verification for factual claims
- does not replace professional review

## Analytical style

Prefer mechanism-first reasoning.

Good output should include:
- bottom line
- scope and evidence mode
- primary driver
- risk transmission mechanism
- exposure map
- actor incentives and leverage
- role-based implications
- trigger points
- unknowns
- confidence
- what would change the judgment
- limitation note

Avoid:
- generic geopolitical essays
- alarmism without transmission channel
- fake precision
- overconfident forecasting
- unsupported legal/compliance conclusions
- vague “monitor closely” recommendations

## README priorities

README should make value clear in 30 seconds.

Recommended structure:
1. One-line positioning
2. Problem
3. What it does
4. What it is not
5. Relationship to Agenda Intelligence MD and Global Think Tank Analyst
6. Quick usage
7. Before / after
8. Flagship example
9. Skill files
10. Source guide
11. Risk archetypes
12. Review checklist
13. Limitations
14. Roadmap

## Examples

Examples should be concrete and role-relevant.

Preferred examples:
- fintech sanctions/routing exposure
- bank correspondent/counterparty exposure
- Caspian corridor logistics chokepoint
- energy/infrastructure corridor risk
- beneficial ownership opacity
- trade finance or dual-use goods routing

Every example must include evidence mode and limitation note.

## Evaluation docs

Use honest labels:
- review checklist
- starter rubric
- failure modes

Do not call it a benchmark unless benchmark cases and results actually exist.

## Validation

If validation scripts exist, run them before finalizing changes.

Prefer additive improvements.
Do not introduce heavy dependencies unless necessary.

## Definition of done

A senior AI or agent engineering reviewer should understand that this repo is not a generic regional prompt. It should read as an early but credible vertical specialist skill for Central Asia + Caspian strategic-risk agents, with evidence discipline, mechanism-first reasoning, examples, source guidance and clear limitations.
