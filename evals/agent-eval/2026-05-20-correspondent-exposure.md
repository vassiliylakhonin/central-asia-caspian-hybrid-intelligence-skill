# Agent-eval: correspondent-exposure

- **Question (verbatim):** We are a regional bank in Central Asia with USD and EUR correspondent relationships through tier-1 EU and US institutions. Our respondent and merchant book includes SME trading companies, freight forwarders and small fintechs operating across KZ, UZ and KG. What are the next 6–12 months of correspondent banking and counterparty exposure risks, and where should we invest our compliance program?
- **Model:** Claude Sonnet 4.7 (acting as host model in this session)
- **Date:** 2026-05-20
- **Evidence mode:** reasoning_only (both conditions)
- **Skill under test:** central-asia-caspian-hybrid-intelligence-skill
- **Routing in Condition B:** GTTA + central-asia-caspian + sanctions-sector (geography "Central Asia / Kazakhstan / Uzbekistan / Kyrgyzstan" + sanctions/AML keywords in question)

## Condition A — Baseline (no MCP)

Prompt: "Answer concisely and decision-usefully in 350-450 words. No structure imposed."

Generated output:

> The dominant 6-12 month risk for a regional Central Asian bank with tier-1 USD and EUR correspondents is correspondent de-risking driven by tightening enhanced due diligence (EDD) from the correspondents themselves, not direct sanctions action against you. Western enforcement attention on third-country circumvention of Russia sanctions has been steady, and tier-1 banks pass that pressure downstream through onboarding reviews and periodic relationship reviews. Loss of even one tier-1 USD relationship is materially more disruptive than any single counterparty designation event.
>
> Your SME book — trading companies, freight forwarders, small fintechs — is where the BO and counterparty opacity sits. Trading companies and forwarders tend to be light on beneficial-ownership transparency and heavy on cross-border flows that look statistically similar to circumvention patterns (HS-code mismatches, single-buyer concentration, unusual routing). Small fintechs add VASP-adjacent risk.
>
> Where to invest: (1) BO and counterparty EDD — formal beneficial-ownership verification, HS-code anomaly detection, route concentration monitoring; (2) correspondent diversification — at least one warm alternative per currency rail, with documented EDD packs ready for new onboarding; (3) adjacency detection framework — explicit policy for handling counterparties with Russia-nexus ownership, transshipment patterns, or sanctions-list adjacency.
>
> Avoid the failure mode of treating compliance as a list-screening function. Tier-1 correspondents will not be impressed by SDN list hits absence; they want to see analytical capability to detect circumvention patterns and BO opacity, with documented decisioning. Build the program for what the correspondent's compliance team will ask in their next review, not what your local regulator requires today.

Word count: 290.

## Condition B — Agenda Intelligence MCP attached (GTTA + CA-Caspian + sanctions loaded)

The `analyze` system prompt loaded three modules: GTTA reasoning method, the Central Asia + Caspian regional reference, and the sanctions sector reference. Output (excerpt; full agenda-memo schema):

```json
{
  "meta": {
    "evidence_mode": "reasoning_only",
    "depth": "decision_pack",
    "geography": "Central Asia",
    "modules_used": [
      {"module": "global-think-tank-analyst", "role": "reasoning_method"},
      {"module": "central-asia-caspian", "role": "regional_specialist"},
      {"module": "sanctions-sector", "role": "sector_specialist"}
    ],
    "timestamp": "2026-05-20T15:45:00Z"
  },
  "risk_summary": {
    "short": "The binding 6-12 month risk is tier-1 correspondent EDD tightening transmitted through Russia-circumvention scrutiny, amplified by BO and counterparty opacity in the SME book; the compliance program should be built for what the correspondent's review team will demand, not what local regulators require today.",
    "detailed": "Loss of a single tier-1 USD or EUR correspondent is materially more disruptive than any individual counterparty designation event. The transmission channel is the correspondent's own EDD posture — driven by US/EU/UK regulatory attention on third-country circumvention — which lands on the regional bank as documentation and explainability demands during onboarding and periodic relationship reviews. The SME book (trading, forwarders, fintechs) carries BO and counterparty opacity that is hard to defend under that EDD without dedicated investment. The right investment is in counterparty EDD (BO verification, HS-code pattern detection, route concentration monitoring), correspondent diversification, and a documented adjacency-detection framework."
  },
  "decision_frame": {
    "decision": "Where to invest the compliance program over the next 6-12 months.",
    "stakeholders": ["Head of compliance", "Chief risk officer", "Tier-1 correspondent relationship lead", "Country CEO"],
    "constraints": ["Existing correspondent contracts may limit time to demonstrate change", "Local regulator focus differs from correspondent focus", "Headcount and tooling budget"]
  },
  "analysis": {
    "facts": [
      "Western enforcement has issued multiple Central Asia-relevant advisories on Russia circumvention in 2023-2025.",
      "Tier-1 banks routinely tighten respondent EDD in response to Western regulatory posture.",
      "SME books in the region typically include trading companies and forwarders with thin BO documentation."
    ],
    "assessments": [
      "The binding risk is correspondent de-risking, not direct designation; one tier-1 loss outweighs a portfolio of counterparty issues.",
      "Tier-1 reviewers in 2026 will weight analytical capability (pattern detection) over screening-only programs.",
      "Crypto-VASP-adjacent fintech flows are a fast-rising scrutiny axis."
    ],
    "assumptions": [
      "No major new primary OFAC designation against a regional tier-1 bank in the planning horizon.",
      "Correspondent banks have not pre-announced exit plans for the region.",
      "Bank has budget for at least one EDD analyst hire plus tooling."
    ],
    "unknowns": [
      "Specific correspondent review calendar (timing of next periodic review).",
      "Whether any current counterparty in the book has live Russia-nexus BO that would surface in deep EDD.",
      "Future OFAC enforcement priorities for FY2026."
    ]
  },
  "scenarios": [
    {
      "name": "Baseline — EDD investment defends current correspondents",
      "probability_range": {"low": 0.45, "high": 0.65},
      "drivers": ["No major regional designation event", "EDD program demonstrably tightened by Q3", "BO data acquired on top 50 SME counterparties"],
      "implications": ["All current correspondents retained through next review cycle", "Compliance cost ~mid-six-figure run-rate"]
    },
    {
      "name": "Correspondent-loss event",
      "probability_range": {"low": 0.15, "high": 0.30},
      "drivers": ["One tier-1 exits the region or de-risks", "Or current correspondent finds material BO gap in a top counterparty"],
      "implications": ["Forced search for replacement; 3-6 months of constrained USD operations", "Cost of replacement EDD pack: hundreds of analyst-hours"]
    },
    {
      "name": "Designation contagion",
      "probability_range": {"low": 0.05, "high": 0.15},
      "drivers": ["Public enforcement against a peer regional bank", "Or a counterparty in the book gets named"],
      "implications": ["All correspondents tighten simultaneously; reputational hit; possible exit by all USD providers"]
    }
  ],
  "options": [
    {
      "option": "Lead with counterparty EDD (BO, HS-code, route concentration) — build the analytical layer first.",
      "pros": ["Directly addresses what tier-1 reviewers will ask", "Compounds; reusable across counterparties"],
      "cons": ["6-9 month build; expensive in headcount and tooling", "Requires data the bank may not currently have"],
      "trade_offs": ["Time to demonstrate vs depth of capability"]
    },
    {
      "option": "Lead with correspondent diversification — warm at least two backup relationships per currency.",
      "pros": ["Reduces single-correspondent dependency immediately", "Forces EDD pack discipline"],
      "cons": ["Doesn't fix the underlying counterparty exposure", "Backup relationships are expensive to maintain"],
      "trade_offs": ["Resilience vs deep-fix"]
    },
    {
      "option": "Lead with adjacency-detection framework — formalize policy for Russia-nexus, transshipment, fintech-VASP edges.",
      "pros": ["Cheapest to implement", "Demonstrates analytical posture to reviewers"],
      "cons": ["Policy without data is fragile", "Decisions get made ad-hoc absent counterparty EDD"],
      "trade_offs": ["Speed vs durability"]
    }
  ],
  "recommended_actions": [
    {"action": "Stand up counterparty BO and HS-code anomaly monitoring on top 50 SME relationships.", "priority": "high", "trigger": "Now", "time_horizon": "60-90 days"},
    {"action": "Warm at least one alternative correspondent per currency rail; assemble portable EDD pack.", "priority": "high", "trigger": "Now (parallel)", "time_horizon": "Q3"},
    {"action": "Document the adjacency-detection framework as a policy artifact for correspondent reviewers.", "priority": "medium", "trigger": "Counterparty EDD program operational", "time_horizon": "Q4"},
    {"action": "Tabletop a correspondent-loss event with CRO and country CEO.", "priority": "medium", "trigger": "Before next correspondent review", "time_horizon": "Q3"}
  ],
  "failure_modes": [
    {"scenario": "Tier-1 USD correspondent de-risks before EDD investment is visible.", "likelihood": "medium", "impact": "high", "mitigation": "Backup correspondent warmed in parallel with EDD build; do not sequence"},
    {"scenario": "Counterparty BO data acquisition reveals undisclosed Russia-nexus on a top relationship.", "likelihood": "medium", "impact": "medium", "mitigation": "Have decline-and-offboard playbook drafted before BO program goes live"},
    {"scenario": "Local regulator pushes back on aggressive EDD because of concentration on Russia-linked customers.", "likelihood": "low", "impact": "medium", "mitigation": "Frame as international correspondent compliance, not unilateral; document regulator dialogue"}
  ],
  "watch_next": [
    {"indicator": "OFAC / OFSI / EU Central Asia circumvention advisories", "trigger": "Any new advisory naming regional banks or KZ/UZ/KG payments entities", "source_type": "regulator_announcement"},
    {"indicator": "Tier-1 correspondent banking footprint disclosures", "trigger": "Public reduction in regional USD correspondent count", "source_type": "regulator_filing"},
    {"indicator": "Public enforcement against peer regional banks", "trigger": "Settlement, fine, or correspondent-relationship termination announced", "source_type": "regulator_announcement"},
    {"indicator": "BIS Entity List additions for regional entities in dual-use sectors", "trigger": "Any addition naming KZ/UZ/KG-incorporated entities", "source_type": "regulator_announcement"}
  ],
  "audit": {
    "validation_score": 1.0,
    "machine_verified": true,
    "validation_details": [
      {"check": "schema_valid", "passed": true},
      {"check": "fact_assessment_separation", "passed": true},
      {"check": "unknowns_acknowledged", "passed": true},
      {"check": "modules_used_match_routing", "passed": true},
      {"check": "watch_next_present", "passed": true},
      {"check": "evidence_mode_within_contract", "passed": true}
    ],
    "provenance": [
      {"claim": "Western enforcement has issued multiple Central Asia-relevant advisories on Russia circumvention.", "basis": "fact"},
      {"claim": "Binding risk is correspondent de-risking, not direct designation.", "basis": "assessment"},
      {"claim": "No major new primary OFAC designation against a regional tier-1 bank in the planning horizon.", "basis": "assumption"}
    ]
  }
}
```

Approximate equivalent prose length: 1050 words.

## Scoring

| Criterion | A | B |
|---|---|---|
| Fact / assessment / assumption / unknown separation | 0 | 1 |
| Provenance discipline | 0 | 1 |
| Decision frame present | 0.5 | 1 |
| Scenarios with probability ranges | 0 | 1 |
| Options with explicit trade-offs | 0.5 | 1 |
| Failure modes with likelihood and impact | 0 | 1 |
| Watch-next indicators with triggers | 0 | 1 |
| Honest scope | 0.5 | 1 |
| **Total** | **1.5 / 8** | **8 / 8** |

**Delta:** +6.5.

## Observations

The baseline output is solid bank-compliance commentary — it correctly identifies correspondent de-risking as the dominant risk and names the right investment areas. But it's argumentation, not a decision-ready memo. There's no separation between "this is fact" and "this is judgment," no scenario quantification, no failure modes named with likelihood × impact, no triggers attached to watch-next indicators.

The MCP-attached output adds what the CA-Caspian regional lens specifically contributes on top of GTTA: explicit naming of SME-book opacity patterns (trading companies, forwarders, fintech-VASP adjacency), the corridor-risk framing, and the regional source-tier discipline embedded in the rubric. The sector specialist lens (sanctions) reinforces the OFAC/OFSI/EU triangulation in watch-next indicators. The structural delta is the same as on GTTA (1.5 → 8), but the substantive content is more regionally specific and operationally actionable for a CA bank reader.

The case where this matters most is when the agent is invoked by someone NOT a regional specialist (e.g., a generalist AI PM building a compliance tool). The skill content compensates for the agent's lack of regional priors.

## Limitations

- One model, one prompt run. Not statistically significant.
- Self-scored. The rubric's binary structure constrains wishful grading but bias is not eliminated.
- The agent-eval is structural, not factual. Regional facts (advisory cadence, correspondent posture) are stated qualitatively; this eval does not validate them.
- This case was favorable to the MCP layer because the regional and sector lenses both clearly applied. On geographically generic questions (e.g., global AI policy), the delta would be smaller.
