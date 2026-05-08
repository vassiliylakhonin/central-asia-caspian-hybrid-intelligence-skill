# Central Asia + Caspian Hybrid Intelligence Skill

<p align="left">
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/stargazers"><img src="https://img.shields.io/github/stars/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub stars"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/network/members"><img src="https://img.shields.io/github/forks/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub forks"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/blob/main/LICENSE"><img src="https://img.shields.io/github/license/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/validate.yml?branch=main&style=for-the-badge" alt="Validate"></a>
</p>

## 1. Positioning

**Central Asia & Caspian specialist skill for AI agents working on sanctions, AML, corridors, banking, logistics, energy and geopolitical risk.**

## 2. Problem

Generic LLMs produce broad regional commentary on Central Asia and the Caspian: high-level country narration, vague "monitor sanctions" advice, no transmission mechanism, no actor incentives, no trigger points, no evidence boundaries.

That output is not decision-useful for analysts, banks, fintechs, investors, logistics operators or energy teams who actually have exposure to the region. They need mechanism-first reasoning, explicit evidence mode, and role-based implications — not regional essays.

## 3. What it does

This skill helps agents produce mechanism-first, evidence-aware, decision-useful regional risk analysis. It:

- frames regional questions as concrete risk or strategy problems
- explains mechanisms before implications
- separates `Verified` / `Plausible` / `Judgment` / `Unknown`
- maps risk transmission channels across banking, payments, routing, ownership and corridors
- supports sanctions, AML, banking, corridor, energy, logistics and political-economy analysis
- identifies leverage shifts and actor incentives
- produces trigger points and watch-next indicators
- supports role-based implications for banks, fintechs, investors, logistics operators, energy teams and analysts

## 4. What it is not

- not legal advice
- not compliance advice
- not sanctions screening
- not AML transaction monitoring
- not factuality verification by itself
- not a live source retriever
- not a risk database
- not an agent framework
- not a CLI, MCP server, or validation platform
- not a replacement for human analyst or counsel review

## 5. Relationship to Agenda Intelligence MD and Global Think Tank Analyst

This skill is one of three repos in a wider portfolio. Each has a distinct role; do not blur them.

- **Central Asia + Caspian Hybrid Intelligence Skill** *(this repo)* — specialist regional/corridor-risk reasoning, domain-specific risk-transmission logic, sanctions / AML / banking / logistics / energy / corridor analysis patterns.
- **Global Think Tank Analyst** — broader strategic-risk memo workflow, general policy-risk analysis, scenario and red-team memo modes.
- **Agenda Intelligence MD** — schemas, validation, evidence audit, scoring, CLI / MCP / CI tooling where implemented.

> Use this repo for specialist Central Asia + Caspian reasoning. Use Global Think Tank Analyst for broader strategic-risk memo workflows. Use Agenda Intelligence MD to validate, score or audit outputs where that functionality is implemented.

This repo does **not** itself perform Agenda Intelligence MD validation, schema enforcement on outputs, or live source retrieval.

[docs/companion-patterns.md](docs/companion-patterns.md) describes structural patterns for using this skill alongside Agenda Intelligence MD (validation / evidence audit / scoring) and Global Think Tank Analyst (broader strategic-risk memo workflow). The patterns are illustrative; for current interfaces, schemas and tooling, consult those repos directly.

## 6. Quick usage

Use the skill variant matching your environment as the operating instruction in your agent setup:

| Environment | File | Notes |
|---|---|---|
| Codex | `skills/codex/SKILL.md` | See also `AGENTS.md` |
| Claude | `skills/claude/SKILL.md` | YAML frontmatter |
| OpenClaw | `skills/openclaw/SKILL.md` | |
| ChatGPT / other LLMs | any of the above | Paste or attach as system / project instruction |

Validation:

```bash
python3 scripts/validate_skills.py
```

The validator checks structure, required phrases, forbidden determinative claims and code-fence balance. It does **not** validate factuality of any output produced by the skill.

## 7. Before / after

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

## 8. Flagship examples

- [examples/fintech-sanctions-routing.md](examples/fintech-sanctions-routing.md) — fintech sanctions and routing exposure across Kazakhstan, Uzbekistan and Caspian-connected trade routes.
- [examples/bank-correspondent-counterparty-exposure.md](examples/bank-correspondent-counterparty-exposure.md) — regional bank correspondent and counterparty exposure under tier-1 EDD pressure.
- [examples/caspian-corridor-chokepoint.md](examples/caspian-corridor-chokepoint.md) — Middle Corridor / Caspian logistics chokepoint risk for shippers, operators and energy buyers.
- [examples/energy-infrastructure-corridor-risk.md](examples/energy-infrastructure-corridor-risk.md) — Caspian and Central Asia energy / infrastructure corridor risk for buyers, producers and investors.
- [examples/beneficial-ownership-opacity.md](examples/beneficial-ownership-opacity.md) — BO opacity and adjacency risk for EDD analysts onboarding cross-border trading groups.
- [examples/trade-finance-dual-use-routing.md](examples/trade-finance-dual-use-routing.md) — trade finance and dual-use goods routing risk for SME-focused trade-finance providers.
- [examples/illustrative-source-packet-fintech.md](examples/illustrative-source-packet-fintech.md) — worked example of `illustrative source packet` mode, demonstrating how a memo grounds claims in a labeled (constructed) packet.
- [examples/live-source-backed-circumvention-and-corridor.md](examples/live-source-backed-circumvention-and-corridor.md) — `live-source-backed` memo on Russia-circumvention exposure (KZ / KG) and Middle Corridor capacity, grounded in publicly retrievable OFAC/BIS, World Bank, EBRD, EAG and reputable secondary reporting.
- [examples/user-provided-sources-middle-corridor.md](examples/user-provided-sources-middle-corridor.md) — `user-provided sources` memo for an EU shipper, scoped strictly to a four-item public packet on Middle Corridor capacity.

Every example states its **evidence mode** and ends with a limitation note. The set covers all four canonical evidence modes: six examples use `reasoning-only`, one uses `illustrative source packet`, one is `live-source-backed`, and one is `user-provided sources`.

## 9. Skill files

- `skills/codex/SKILL.md` — Codex variant with expanded trigger description.
- `skills/claude/SKILL.md` — Claude variant with valid YAML frontmatter.
- `skills/openclaw/SKILL.md` — canonical OpenClaw skill.
- `scripts/validate_skills.py` — dependency-free validator for skill metadata, required sections, source-handling discipline, safety disclaimers, unsafe determinative language and fenced-code balance.

All variants share the same analytical contract: mechanism-first reasoning, evidence labels, role-based implications, trigger points, confidence footer, and explicit limitation notes.

## 10. Source guide

A source-backed workflow uses external retrieval, user-provided source packets, or companion tooling. The skill itself does not retrieve sources.

[docs/source-guide.md](docs/source-guide.md) lists recommended source classes:

- official sanctions lists (OFAC, EU, UK OFSI, UN, national regimes)
- national regulators and central banks
- customs / statistics / trade agencies
- company registries, BO registers, court records
- FATF / Egmont / FIU public materials
- IFIs (IMF, World Bank, EBRD, ADB, AIIB)
- government releases
- ports, rail, corridor and logistics operators
- energy and infrastructure operators
- credible regional and international media as Tier 2

Listing a source class is not an endorsement and does not guarantee accuracy or timeliness for any specific question.

## 11. Risk archetypes

[docs/risk-archetypes.md](docs/risk-archetypes.md) catalogues recurring archetypes for the region. For each: mechanism → typical indicators → evidence needed → common false positives → watch-next triggers → role-based mitigation questions. Current archetypes:

1. Re-export / transshipment exposure
2. Dual-use goods routing
3. Correspondent banking de-risking
4. Beneficial ownership opacity
5. Sanctioned-party adjacency
6. Energy / logistics chokepoint risk
7. Customs / statistics anomaly
8. State-capacity enforcement gap
9. China / Russia / EU leverage competition
10. Caspian corridor disruption
11. Regulatory arbitrage
12. Payment-rail exposure

Use them as patterns to structure reasoning, not as factual claims about any specific entity, route or jurisdiction.

[docs/regional-logic.md](docs/regional-logic.md) explains when to include which geography. Core rule: do not expand geography for decoration; expand only when it changes the mechanism, risk exposure, leverage or decision.

## 12. Review checklist

[evals/checklist.md](evals/checklist.md) — review checklist (not a benchmark) covering scope, reasoning quality, evidence discipline, tone/safety and decision usefulness.

[evals/starter-rubric.md](evals/starter-rubric.md) — starter rubric for scoring memos against the analytical contract. Honest label: starter rubric, not a validated benchmark.

[evals/scoring-example.md](evals/scoring-example.md) — worked scoring examples applying the rubric to a `reasoning-only` memo and to the `live-source-backed` memo. The rubric includes evidence-mode-specific dimensions for each of the four canonical modes.

[evals/failure-modes.md](evals/failure-modes.md) — common failure modes (generic essay, alarmism without channel, fake sanctions certainty, fake citations, over-expanded geography, missing limitation note, etc.).

### Evidence mode vocabulary

Every example and every memo produced with this skill should state one of four canonical evidence modes:

- **`live-source-backed`** — facts retrieved from current authoritative sources at the time of writing.
- **`user-provided sources`** — facts grounded in a source packet supplied by the user.
- **`illustrative source packet`** — facts grounded in a constructed, illustrative source packet for demonstration purposes.
- **`reasoning-only`** — no sources retrieved; structural reasoning only. No factual claims about specific entities, designations or enforcement actions.

## 13. Limitations

- This skill helps **structure analysis**; it does not verify facts on its own.
- It does not perform sanctions screening, AML transaction monitoring, or live source retrieval.
- It does not provide legal, regulatory, sanctions, AML, tax, audit or investment advice.
- It does not guarantee correctness, completeness or timeliness of any output.
- It is not production-grade risk control infrastructure.
- Outputs require source-backed verification and qualified professional review before any operational, compliance or commercial use.
- No production-usage, adoption or benchmark numbers are claimed.
- See [STATUS.md](STATUS.md) for an honest status against the Definition of Done in `AGENTS.md`. The repo currently clears the "early but credible" bar; it does **not** clear the "externally validated specialist resource" bar.

## 14. Roadmap

Indicative direction, not a commitment:

- continued refinement of `docs/risk-archetypes.md` indicator catalogues as the field evolves
- additional worked memos in each evidence mode as new use cases arise
- pairing of `live-source-backed` memos with primary-list URLs (OFAC SDN, BIS Entity List, EU consolidated, FATF/EAG MER PDFs) once retrieved at point of use, layered on top of the current secondary-reporting links

This roadmap is additive. It will not turn this repo into a CLI, MCP server, screening engine or validation platform.

## Disclaimer

This repository provides analytical guidance only and does not constitute legal, regulatory, sanctions, AML, tax, audit or investment advice. Outputs require source-backed verification before any operational, compliance or commercial use.
