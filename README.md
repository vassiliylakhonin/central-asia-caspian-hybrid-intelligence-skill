# Central Asia + Caspian Hybrid Intelligence Skill

<p align="left">
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/stargazers"><img src="https://img.shields.io/github/stars/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub stars"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/network/members"><img src="https://img.shields.io/github/forks/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="GitHub forks"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/blob/main/LICENSE"><img src="https://img.shields.io/github/license/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/vassiliylakhonin/central-asia-caspian-hybrid-intelligence-skill/validate.yml?branch=main&style=for-the-badge" alt="Validate"></a>
</p>

> **CENTRAL ASIA + CASPIAN RISK REASONING SKILL** — a reasoning method for AI agents working on regional sanctions, AML, banking, corridor, logistics and energy risk. Open-source. No live data. No legal or compliance advice.

## 1. What this is

A reasoning method that runs inside an AI agent (Claude, ChatGPT, or a custom assistant) and produces mechanism-first, evidence-aware risk analysis on Central Asia and the Caspian — instead of the generic regional essays that default LLM output usually returns.

It does not replace sanctions screening, AML monitoring, legal review or human analyst judgement. It changes the *shape* of the reasoning your AI tool produces before any of those steps.

## 2. Who it is for

- compliance and risk leadership at banks, fintechs and payment providers with SME, correspondent or routing exposure to Kazakhstan, Uzbekistan, Azerbaijan, Turkmenistan, Kyrgyzstan or Tajikistan
- sanctions desks tracking transshipment, beneficial-ownership opacity and re-export risk across the region
- logistics, energy and trading firms operating Caspian, trans-Caspian or Middle Corridor routes
- analysts and researchers covering the region for institutional clients
- AI builders embedding regional risk reasoning into agents or assistants

## 3. What you get

- mechanism-first reasoning: primary driver → transmission channel → exposure
- explicit uncertainty labels: `Verified` / `Plausible` / `Judgment` / `Unknown`
- role-based actions and trigger points — not "monitor closely"
- an explicit evidence mode and a limitation note on every output
- no fabricated citations, sanctions designations, or dates

**Where this sits in the production AI stack**

Reasoning skills (markdown-first reasoning contracts for agents):
- [Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst) — horizontal: policy, sanctions, regulatory, geopolitical, trade memos
- **→ Central Asia + Caspian Hybrid Intelligence Skill (this repo)** — vertical: sanctions, AML, banking, corridor risk in Central Asia / Caspian
- [Gulf + Middle East Hybrid Intelligence Skill](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill) — vertical: Iran sanctions, GCC banking, sovereign wealth, maritime chokepoint risk

Evidence & audit layer (CI / MCP / schemas):
- [Agenda Intelligence MD](https://github.com/vassiliylakhonin/agenda-intelligence-md) — validate, score and audit strategic-risk agent output structure

The skills define how agents *reason*. Agenda Intelligence MD defines how the output is *audited*. Together they let agents produce auditable strategic-intelligence — not just plausible-sounding summaries.

## 4. Try it

Paste this into an AI agent using the Codex, Claude or OpenClaw skill file:

```text
Use the Central Asia + Caspian Hybrid Intelligence Skill.

Question: A European fintech is onboarding SME exporters in Kazakhstan and Uzbekistan that trade through Caspian-connected routes. What sanctions, AML, payment-rail and routing risks matter over the next 6-12 months?
Audience: fintech risk and compliance leadership.
Time horizon: 6-12 months.
Evidence mode: reasoning-only unless live source tools are available.
Mode: risk / compliance.

State the primary driver, mechanism, exposure map, role-based actions, trigger points, confidence, unknowns, and limitation note.
```

Expected shape of a good answer:
- starts with `Primary driver is: ...`;
- explains how the risk transmits through payment rails, counterparties, ownership, routing or corridors;
- labels uncertainty using `Verified` / `Plausible` / `Judgment` / `Unknown` where useful;
- gives role-based actions and trigger points, not vague "monitor closely" advice;
- includes a clear limitation note and avoids legal or compliance determinations.

## 5. What it does

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

## 6. What it is not

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

## 7. Relationship to Agenda Intelligence MD and Global Think Tank Analyst

This skill is one of four repos in a wider portfolio. Each has a distinct role; do not blur them.

- **Central Asia + Caspian Hybrid Intelligence Skill** *(this repo)* — specialist regional/corridor-risk reasoning, domain-specific risk-transmission logic, sanctions / AML / banking / logistics / energy / corridor analysis patterns.
- **Gulf + Middle East Hybrid Intelligence Skill** — sibling vertical specialist; reference it when a flow crosses both regions (Iran-Caspian routes, Russia-Iran-China junction, Iraq-Kurdistan corridors, Central Asian energy routed through Gulf hubs). See [gulf-middle-east-hybrid-intelligence-skill](https://github.com/vassiliylakhonin/gulf-middle-east-hybrid-intelligence-skill).
- **Global Think Tank Analyst** — broader strategic-risk memo workflow, general policy-risk analysis, scenario and red-team memo modes: https://github.com/vassiliylakhonin/global-think-tank-analyst
- **Agenda Intelligence MD** — schemas, validation, evidence audit, scoring, CLI / MCP / CI tooling where implemented: https://github.com/vassiliylakhonin/agenda-intelligence-md

> Use this repo for specialist Central Asia + Caspian reasoning. Use Global Think Tank Analyst for broader strategic-risk memo workflows. Use Agenda Intelligence MD to validate, score or audit outputs where that functionality is implemented.

This repo does **not** itself perform Agenda Intelligence MD validation, schema enforcement on outputs, or live source retrieval.

[docs/companion-patterns.md](docs/companion-patterns.md) describes structural patterns for using this skill alongside Agenda Intelligence MD (validation / evidence audit / scoring) and Global Think Tank Analyst (broader strategic-risk memo workflow). The patterns are illustrative; for current interfaces, schemas and tooling, consult those repos directly.

## 8. Quick usage

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

## 9. Before / after

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

## 10. Flagship examples

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

Every example states its **evidence mode** and ends with a limitation note. The set covers all four canonical evidence modes: six examples use `reasoning-only`, two use `illustrative source packet`, six are `live-source-backed`, and two are `user-provided sources`.

## 11. Skill files

- `skills/claude/SKILL.md` — Claude-compatible variant with YAML frontmatter and Claude-oriented installation wording.
- `skills/codex/SKILL.md` — Codex-compatible variant with Codex-oriented slug and installation wording.
- `skills/openclaw/SKILL.md` — OpenClaw-compatible variant with underscore-convention name for ClawHub and install command.
- `docs/cold-start-interview.md` — preflight procedure that captures role, geography, decision context, risk appetite, and source access before substantive memo work. STOP rule blocks generic memos when the practice profile is missing or contains `[PLACEHOLDER]` markers.
- `templates/practice-profile.md` — populated profile read by every memo in the session as the default `Decision / Audience / Geography / Time horizon` block.
- `docs/currency-watch.md` — active list of fast-moving regional topics (OFAC Russia/Iran, EU sanctions packages, FATF/EAG status, Middle Corridor, CPC/BTC, etc.) that source-backed memos should re-verify against current primary sources. 90-day staleness rule.
- `scripts/validate_skills.py` — dependency-free validator for skill metadata, required sections, source-handling discipline, safety disclaimers, unsafe determinative language and fenced-code balance.

All variants share the same analytical contract: mechanism-first reasoning, evidence labels, role-based implications, trigger points, confidence footer, and explicit limitation notes. Each variant adds platform-specific behavior: Claude variant adds tool-use awareness and evidence-mode shifting; Codex variant adds agentic-loop output discipline and pipeline compression; OpenClaw is the explicit canonical baseline.

## 12. Source guide

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

## 13. Risk archetypes

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

## 14. Review checklist

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

## 15. Limitations

- This skill helps **structure analysis**; it does not verify facts on its own.
- It does not perform sanctions screening, AML transaction monitoring, or live source retrieval.
- It does not provide legal, regulatory, sanctions, AML, tax, audit or investment advice.
- It does not guarantee correctness, completeness or timeliness of any output.
- It is not production-grade risk control infrastructure.
- Outputs require source-backed verification and qualified professional review before any operational, compliance or commercial use.
- No production-usage, adoption or benchmark numbers are claimed.
- See [STATUS.md](STATUS.md) for an honest status against the Definition of Done in `AGENTS.md`. The repo currently clears the "early but credible" bar; it does **not** clear the "externally validated specialist resource" bar.

### What this skill has not been tested on

Stated honestly so readers can calibrate. These are gaps in observed evidence, not claims of weakness:

- **No labeled accuracy dataset.** Adversarial cases in [`evals/adversarial/`](evals/adversarial/) are author-designed traps, not a held-out test set. Pass/fail is judged manually against per-case criteria.
- **No multi-agent or long-horizon trials.** Behavior has been exercised in single-turn and short-multi-turn memo production; long autonomous research loops have not been measured.
- **No cross-model regression tracking.** Behavior has been observed primarily on Claude. Codex and OpenClaw variants exist but have not been systematically compared head-to-head against the same prompts.
- **No live-source automation.** `live-source-backed` examples were produced with manual source retrieval. There is no integrated retrieval layer here; recency cannot be enforced automatically.
- **Limited non-English source coverage.** Russian-, Kazakh-, Uzbek-, and Azerbaijani-language regulatory and registry sources have not been systematically tested as inputs.

## 16. Roadmap

Indicative direction, not a commitment:

- continued refinement of `docs/risk-archetypes.md` indicator catalogues as the field evolves — crypto/VASP archetype (#13) added 2026-05-12
- additional worked memos in each evidence mode as new use cases arise
- pairing of `live-source-backed` memos with primary-list URLs (OFAC SDN, BIS Entity List, EU consolidated, FATF/EAG MER PDFs) once retrieved at point of use

This roadmap is additive. It will not turn this repo into a CLI, MCP server, screening engine or validation platform.

## Disclaimer

This repository provides analytical guidance only and does not constitute legal, regulatory, sanctions, AML, tax, audit or investment advice. Outputs require source-backed verification before any operational, compliance or commercial use.
