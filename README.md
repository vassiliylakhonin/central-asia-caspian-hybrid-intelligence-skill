# Central Asia + Caspian Hybrid Intelligence Skill

**Risk reasoning for AI agents working on Central Asia and the Caspian.**

Use this skill when an agent must explain how sanctions, banking, ownership, logistics, energy, or corridor risk moves through the region. The output starts with the driver, traces the transmission channel and exposure, labels uncertainty, and ends with role-specific actions and triggers.

It is for bank and fintech risk teams, logistics and energy operators, regional analysts, and AI builders.

[Try one prompt](#try-it) · [Open the skill file](SKILL.md) · [See worked examples](#flagship-examples)


<p align="left">
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill"><img src="https://img.shields.io/github/stars/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub stars"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/network/members"><img src="https://img.shields.io/github/forks/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub forks"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/blob/main/LICENSE"><img src="https://img.shields.io/github/license/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/validate.yml?branch=main&style=for-the-badge" alt="Validate"></a>
</p>

## Problem it handles

General-purpose agents often return a regional summary when the user needs a risk mechanism. This skill makes the agent name what changed, how the effect travels through payments, ownership, counterparties, or routes, who is exposed, and what evidence still needs checking.

## Who it is for

- compliance and risk leadership at banks, fintechs and payment providers with SME, correspondent or routing exposure to Kazakhstan, Uzbekistan, Azerbaijan, Turkmenistan, Kyrgyzstan or Tajikistan
- sanctions desks tracking transshipment, beneficial-ownership opacity and re-export risk across the region
- logistics, energy and trading firms operating Caspian, trans-Caspian or Middle Corridor routes
- analysts and researchers covering the region for institutional clients
- AI builders embedding regional risk reasoning into agents or assistants

## What you get

- mechanism-first reasoning: primary driver → transmission channel → exposure
- explicit uncertainty labels: `Verified` / `Plausible` / `Judgment` / `Unknown`
- role-based actions and trigger points — not "monitor closely"
- no fabricated citations, sanctions designations, or dates

**Where this sits in the Agenda Intelligence stack**

Reasoning skills (markdown-first reasoning contracts for agents):
- [Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst) — horizontal: policy, sanctions, regulatory, geopolitical, trade memos
- **→ Central Asia + Caspian Hybrid Intelligence Skill (this repo)** — vertical: sanctions, AML, banking, corridor risk in Central Asia / Caspian
- [Gulf + Middle East Hybrid Intelligence Skill](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill) — vertical: Iran sanctions, GCC banking, sovereign wealth, maritime chokepoint risk

Evidence-packet checker:
- [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) — checks claim/source references, declared quotes, lexical support, and unmatched numbers before human review

The skills define how agents *reason*. Agenda Intelligence MD reports whether the supplied claim/source packet is complete enough for review. It does not establish factual truth.

Primary handoff: [`docs/evidence-packet-handoff.md`](docs/evidence-packet-handoff.md) with runnable synthetic [`examples/evidence-packet-handoff.json`](examples/evidence-packet-handoff.json).

## Try it

Paste this into an AI agent using the Codex, Claude or OpenClaw skill file:

```text
Use the Central Asia + Caspian Hybrid Intelligence Skill.

Question: A European fintech is onboarding SME exporters in Kazakhstan and Uzbekistan that trade through Caspian-connected routes. What sanctions, AML, payment-rail and routing risks matter over the next 6-12 months?
Audience: fintech risk and compliance leadership.
Time horizon: 6-12 months.
Evidence mode: reasoning-only unless live source tools are available.
Mode: risk / compliance.

```

Expected shape of a good answer:
- starts with `Primary driver is: ...`;
- explains how the risk transmits through payment rails, counterparties, ownership, routing or corridors;
- labels uncertainty using `Verified` / `Plausible` / `Judgment` / `Unknown` where useful;
- gives role-based actions and trigger points, not vague "monitor closely" advice;

The public browser demos that used this regional frame are no longer published; [`examples/`](examples/) shows the output format.

## What it does

This skill helps agents produce mechanism-first, evidence-aware, decision-useful regional risk analysis. It:

- frames regional questions as concrete risk or strategy problems
- explains mechanisms before implications
- separates `Verified` / `Plausible` / `Judgment` / `Unknown`
- maps risk transmission channels across banking, payments, routing, ownership and corridors
- supports sanctions, AML, banking, corridor, energy, logistics and political-economy analysis
- identifies leverage shifts and actor incentives
- produces trigger points and watch-next indicators
- supports role-based implications for banks, fintechs, investors, logistics operators, energy teams and analysts
- runs a cold-start interview ([`docs/cold-start-interview.md`](docs/cold-start-interview.md)) to capture role, geography, decision context, risk appetite and source access into a populated practice profile ([`templates/practice-profile.md`](templates/practice-profile.md)) before substantive memos
- carries an active currency watch ([`docs/currency-watch.md`](docs/currency-watch.md)) listing fast-moving regional topics that source-backed memos should re-verify against current primary sources, with a 90-day staleness rule

## What it is not

- not sanctions screening
- not AML transaction monitoring
- not factuality verification by itself
- not a live source retriever
- not a risk database
- not an agent framework
- not a CLI, MCP server, or validation platform
- not a replacement for human analyst or counsel review

## Relationship to Agenda Intelligence MD and Global Think Tank Analyst

This skill is one of four repos in a wider portfolio. Each has a distinct role; do not blur them.

This repo is the **Central Asia / Caspian vertical specialist**. Use it standalone or inside the older `analyze` compatibility workflow. The current primary composition is: horizontal method → regional specialist → claim/source packet → Agenda Intelligence MD linter → human review.

> **Project maturity.** This repo uses a two-bar Definition of Done (Bar 1 — early but credible; Bar 2 — agent-validated specialist resource). Current honest status, per criterion, lives in [STATUS.md](STATUS.md). Criteria are defined in [docs/definition-of-done.md](docs/definition-of-done.md).

- **Central Asia + Caspian Hybrid Intelligence Skill** *(this repo)* — specialist regional/corridor-risk reasoning, domain-specific risk-transmission logic, sanctions / AML / banking / logistics / energy / corridor analysis patterns.
- **Gulf + Middle East Hybrid Intelligence Skill** — sibling vertical specialist; reference it when a flow crosses both regions (Iran-Caspian routes, Russia-Iran-China junction, Iraq-Kurdistan corridors, Central Asian energy routed through Gulf hubs). See [gulf-middle-east-hybrid-intelligence-skill](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill).
- **Global Think Tank Analyst** — broader strategic-risk memo workflow, general policy-risk analysis, scenario and red-team memo modes: https://github.com/vassiliylakhonin/global-think-tank-analyst
- **Agenda Intelligence MD** — primary evidence-packet linter; older validation, scoring, CLI / MCP / HTTP / A2A surfaces remain compatible: https://github.com/vassiliylakhonin/agenda-intelligence-md

> Use this repo for specialist Central Asia + Caspian reasoning. Use Global Think Tank Analyst for broader strategic-risk memo workflows. Use Agenda Intelligence MD to lint the claim/source packet; treat its result as packet completeness, not factual truth.

This repo does **not** itself perform Agenda Intelligence MD validation, schema enforcement on outputs, or live source retrieval.

For the full portfolio architecture, see [PORTFOLIO.md in Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst/blob/main/PORTFOLIO.md). [docs/companion-patterns.md](docs/companion-patterns.md) describes structural patterns for using this skill alongside Agenda Intelligence MD and Global Think Tank Analyst; for current interfaces, schemas and tooling, consult those repos directly.

## Quick usage

Use the root contract in every environment. Load the matching runtime overlay after it only when the platform-specific behavior applies.

| Environment | File | Notes |
|---|---|---|
| All runtimes | `SKILL.md` | Required baseline contract |
| Codex | `runtimes/codex/SKILL.md` | Optional agent-loop and file-output rules |
| Claude | `runtimes/claude/SKILL.md` | Optional retrieval and document-use rules |
| OpenClaw | `runtimes/openclaw/SKILL.md` | Optional direct GitHub installation guidance |
| ChatGPT / other LLMs | `SKILL.md` | No overlay required |

Install the packaged skill in Claude Code through the existing Agenda Intelligence marketplace:

```text
/plugin marketplace add vassiliylakhonin/agenda-intelligence-md
/plugin install central-asia-caspian@agenda-intelligence
```

Install in OpenClaw directly from GitHub:

```bash
openclaw skills install git:https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill.git --as central-asia-caspian
```

Validation:

```bash
python3 scripts/validate.py
```

The validator checks the Claude composition adapter and its load order, plugin-manifest consistency, the complete root contract, allowlisted runtime overlays, evidence-mode counts, evidence-packet structure, local links, and safety gates. It rejects overlays that duplicate common contract sections. It does **not** validate factuality of any output produced by the skill.

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

## Flagship examples

For a guided route through the examples, start with [examples/README.md](examples/README.md).

- [examples/fintech-sanctions-routing.md](examples/fintech-sanctions-routing.md) — fintech sanctions and routing exposure across Kazakhstan, Uzbekistan and Caspian-connected trade routes.
- [examples/bank-correspondent-counterparty-exposure.md](examples/bank-correspondent-counterparty-exposure.md) — regional bank correspondent and counterparty exposure under tier-1 EDD pressure.
- [examples/caspian-corridor-chokepoint.md](examples/caspian-corridor-chokepoint.md) — Middle Corridor / Caspian logistics chokepoint risk for shippers, operators and energy buyers.
- [examples/energy-infrastructure-corridor-risk.md](examples/energy-infrastructure-corridor-risk.md) — Caspian and Central Asia energy / infrastructure corridor risk for buyers, producers and investors.
- [examples/beneficial-ownership-opacity.md](examples/beneficial-ownership-opacity.md) — BO opacity and adjacency risk for EDD analysts onboarding cross-border trading groups.
- [examples/trade-finance-dual-use-routing.md](examples/trade-finance-dual-use-routing.md) — trade finance and dual-use goods routing risk for SME-focused trade-finance providers.
- [examples/illustrative-source-packet-fintech.md](examples/illustrative-source-packet-fintech.md) — worked example of `illustrative source packet` mode, demonstrating how a memo grounds claims in a labeled (constructed) packet.
- [examples/live-source-backed-circumvention-and-corridor.md](examples/live-source-backed-circumvention-and-corridor.md) — `live-source-backed` memo on Russia-circumvention exposure (KZ / KG) and Middle Corridor capacity, grounded in publicly retrievable OFAC/BIS, Treasury, World Bank, EBRD, EAG and reputable secondary reporting.
- [examples/live-source-backed-bank-correspondent.md](examples/live-source-backed-bank-correspondent.md) — `live-source-backed` memo on Kazakhstani correspondent and counterparty exposure under EO 14114, UK CHPL guidance and EU enforcement on Central Asian banks.
- [examples/live-source-backed-bo-opacity.md](examples/live-source-backed-bo-opacity.md) — `live-source-backed` memo on beneficial ownership opacity in cross-border KZ/UZ/KG structures under FATF R24/R25 and the EU 2024 AML package.
- [examples/live-source-backed-energy-corridor.md](examples/live-source-backed-energy-corridor.md) — `live-source-backed` memo on Caspian and Central Asia energy corridor risk grounded in EIA primary, World Bank and EBRD/EC primary reports.
- [examples/user-provided-sources-middle-corridor.md](examples/user-provided-sources-middle-corridor.md) — `user-provided sources` memo for an EU shipper, scoped strictly to a four-item public packet on Middle Corridor capacity.
- [examples/live-source-backed-vasp-travel-rule.md](examples/live-source-backed-vasp-travel-rule.md) — `live-source-backed` memo on VASP / Travel Rule enforcement gap in Kazakhstan and Uzbekistan for European fintech compliance leadership assessing EU TFR 2023/1113 alignment and de-risking exposure.
- [examples/live-source-backed-customs-statistics-anomaly.md](examples/live-source-backed-customs-statistics-anomaly.md) — `live-source-backed` memo on customs / mirror-statistic anomaly as a sanctions-circumvention indicator for a European trade finance bank reviewing KZ counterparty exposure; grounded in UN Comtrade, KSE/CREA, OFAC/BIS, World Bank and Kazstat primary sources.
- [examples/user-provided-sources-russia-iran-china-junction.md](examples/user-provided-sources-russia-iran-china-junction.md) — `user-provided sources` skeleton-packet memo on the Russia–Iran–China commercial junction for a European trade-finance bank's sanctions, compliance and risk leadership; structural framing of junction-pattern tiering vs named-entity screening, composed with the Gulf + Middle East skill, with canonical Axis A / Axis B tags throughout. The user supplies the binding evidence by retrieving from OFAC, EU, UK OFSI, BIS, FATF, EAG and MENAFATF mandate pages.
- [examples/source-conflict-kz-ru-circumvention-volume-estimates.md](examples/source-conflict-kz-ru-circumvention-volume-estimates.md) — `illustrative source packet` demonstrator of the source-conflict-surfacing rule applied to KZ→RU CHPL-circumvention volume estimates across EU Commission, KSE Institute, Bruegel and industry advisories, with explicit source-independence assessment and regret-asymmetry calibration for EDD threshold decisions.


## Skill files

- `skills/central-asia-caspian/SKILL.md` — Claude Code plugin discovery and composition adapter; attaches the root contract, then the Claude overlay.
- `SKILL.md` — complete runtime-neutral analytical contract and the only copy of common behavior.
- `runtimes/claude/SKILL.md` — additive Claude retrieval and document-use rules.
- `runtimes/codex/SKILL.md` — additive Codex agent-loop, file-output, and validation-chaining rules.
- `runtimes/openclaw/SKILL.md` — additive OpenClaw direct GitHub installation guidance.
- `docs/cold-start-interview.md` — preflight procedure that captures role, geography, decision context, risk appetite, and source access before substantive memo work. STOP rule blocks generic memos when the practice profile is missing or contains `[PLACEHOLDER]` markers.
- `templates/practice-profile.md` — populated profile read by every memo in the session as the default `Decision / Audience / Geography / Time horizon` block.
- `docs/currency-watch.md` — active list of fast-moving regional topics (OFAC Russia/Iran, EU sanctions packages, FATF/EAG status, Middle Corridor, CPC/BTC, etc.) that source-backed memos should re-verify against current primary sources. 90-day staleness rule.
- `scripts/validate.py` — single dependency-free interface for all repository and packaging checks.


## Repository layout

```text
.
├── README.md            # Public positioning (this file)
├── AGENTS.md            # Canonical project contract (identity, scope, evidence rules)
├── CLAUDE.md            # Claude Code working rules (inherits AGENTS.md)
├── SKILL.md             # Complete runtime-neutral skill contract
├── STATUS.md            # Honest Bar 1 / Bar 2 status against the Definition of Done
├── CONTEXT.md           # Working context for cross-session continuity
├── CONTRIBUTING.md      # Local validator workflow and CI invariants
├── llms.txt             # Orientation for LLMs and agent indexers
├── runtimes/            # Runtime overlay skill files per platform (claude/, codex/, openclaw/)
├── skills/              # Claude Code plugin composition adapter
├── examples/            # Flagship memo examples (state evidence mode)
├── evals/               # Review checklist, failure modes, starter rubric, agent-eval cases
├── docs/                # Source guide, currency watch, cold-start interview, regional logic, risk archetypes
├── templates/           # Practice-profile template populated by the cold-start interview
├── scripts/             # Repository and packaging checks
└── .github/             # CI workflows
```

## Contributing

New contributors: [`CONTRIBUTING.md`](CONTRIBUTING.md) opens with a "First 15 minutes" onboarding path — read the three load-bearing files (`README.md`, `AGENTS.md`, `STATUS.md`), run `python3 scripts/validate.py` locally, and walk one concrete `live-source-backed` flagship example end-to-end. CI runs the same command on every push.

Cross-repo terminology — evidence modes, Verified/Plausible/Judgment/Unknown labels, Axis A/B provenance tags (incl. table-cell discipline), three-value response logic, and the deliberate maturity-framework asymmetry across the four-repo stack (this repo and the Gulf+ME sibling use Bar 1/2; `global-think-tank-analyst` uses `VALIDATION_PLAN.md`; `agenda-intelligence-md` uses `ROADMAP.md` version targets) — is consolidated in the portfolio glossary at [`agenda-intelligence-md/docs/glossary.md`](https://github.com/vassiliylakhonin/agenda-intelligence-md/blob/main/docs/glossary.md).

## Source guide

Latest source-maintenance pass: [`docs/source-refresh-2026-07-11.md`](docs/source-refresh-2026-07-11.md).

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

## Risk archetypes

[docs/risk-archetypes.md](docs/risk-archetypes.md) catalogues recurring archetypes for the region. For each: mechanism → typical indicators → evidence needed → common false positives → watch-next triggers → role-based enforcement actions. Current archetypes:

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

## Review checklist

[evals/checklist.md](evals/checklist.md) — review checklist (not a benchmark) covering scope, reasoning quality, evidence discipline, tone/safety and decision usefulness.

[evals/starter-rubric.md](evals/starter-rubric.md) — starter rubric for scoring memos against the analytical contract. Honest label: starter rubric, not a validated benchmark.

[evals/scoring-example.md](evals/scoring-example.md) — worked scoring examples applying the rubric to a `reasoning-only` memo and to the `live-source-backed` memo. The rubric includes evidence-mode-specific dimensions for each of the four canonical modes.


### Evidence mode vocabulary

Every example and every memo produced with this skill should state one of four canonical evidence modes:

- **`live-source-backed`** — facts retrieved from current authoritative sources at the time of writing.
- **`user-provided sources`** — facts grounded in a source packet supplied by the user.
- **`illustrative source packet`** — facts grounded in a constructed, illustrative source packet for demonstration purposes.
- **`reasoning-only`** — no sources retrieved; structural reasoning only. No factual claims about specific entities, designations or enforcement actions.


## Roadmap

Indicative direction, not a commitment:

- continued refinement of `docs/risk-archetypes.md` indicator catalogues as the field evolves — crypto/VASP archetype (#13) added 2026-05-12
- additional worked memos in each evidence mode as new use cases arise
- pairing of `live-source-backed` memos with primary-list URLs (OFAC SDN, BIS Entity List, EU consolidated, FATF/EAG MER PDFs) once retrieved at point of use

This roadmap is additive. It will not turn this repo into a CLI, MCP server, screening engine or validation platform.

