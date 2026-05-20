# Agent-eval: customs-mirror-statistics-anomaly

- **Question (verbatim):** A European trade-finance bank is reviewing Kazakhstani SME exporters after mirror-statistics divergence suggests possible KZ-to-RU high-priority goods routing and export controls / sanctions circumvention exposure. How should the bank calibrate EDD thresholds for the next 6-12 months?
- **Model:** GPT-5 (Codex host model in this session)
- **Date:** 2026-05-20
- **Evidence mode:** `mixed` through Agenda Intelligence `analyze`. Upstream specialist material is `live-source-backed` (`examples/live-source-backed-customs-statistics-anomaly.md`, retrieval date 2026-05-14); product-shell mapping is `mixed` because the checked source packet is supplied conceptually while the host model also performs structural reasoning.
- **Skill under test:** central-asia-caspian-hybrid-intelligence-skill
- **Routing in Condition B:** Local `agenda-intelligence-md` `analyze` request validation returned GTTA + `central-asia-caspian` + `sanctions-sector`. No external LLM was invoked locally because `ANTHROPIC_API_KEY` was not configured; the host model completed both conditions using the same model.

## Condition A — Baseline (no MCP)

Prompt: "Answer concisely and decision-usefully in 350-450 words. No structure imposed."

Generated output:

> The bank should treat the mirror-statistics divergence as an EDD escalation trigger, not as automatic proof of sanctions circumvention. A gap between Kazakhstan-reported exports and Russia-reported imports can reflect timing, classification, reporting methodology, or re-export mechanics, but in the current Russia sanctions environment it is a serious red flag when combined with high-priority goods, opaque ownership, new SME exporters, or weak end-use documentation.
>
> The practical response should be tiered. For ordinary goods with long-standing counterparties, require additional documentation: invoices, bills of lading, certificates of origin, transport route, end-user declaration, and explanation for the data mismatch. For electronics, machinery, optics, chemicals or other export-control-adjacent goods, escalate to enhanced due diligence: beneficial ownership review, buyer and end-user screening, origin verification, HS-code review by trade compliance, and review of whether the goods contain US-origin content or technology. For counterparties with weak BO transparency, shared addresses, recent incorporation, unexplained volume spikes, or Russia-nexus ownership, pause or reject until the gaps are resolved.
>
> The bank should not rely only on list screening. The main risk is financing flows that appear clean at entity level but contribute to a known circumvention channel. Build thresholds around combinations of indicators: HS code sensitivity, mirror-data anomaly, counterparty age, route economics, document quality, ownership opacity, and end-user plausibility.
>
> Over the next 6-12 months, invest in a portfolio look-back for KZ-linked trade finance, a controlled list of HS codes requiring mandatory EDD, and a case file standard that can withstand correspondent or regulator review. Any specific designation or export-control status must be checked against current OFAC, EU, UK and BIS sources before acting.

Word count: 293.

## Condition B — Agenda Intelligence Product Shell (GTTA + CA-Caspian + sanctions loaded)

The `analyze` request used `evidence_mode: "mixed"` and routed to three modules:

```json
[
  {"module": "global-think-tank-analyst", "role": "reasoning_method"},
  {"module": "central-asia-caspian", "role": "regional_specialist"},
  {"module": "sanctions-sector", "role": "sector_specialist"}
]
```

Generated output excerpt in agenda-memo shape:

```json
{
  "meta": {
    "evidence_mode": "mixed",
    "depth": "decision_pack",
    "geography": "Kazakhstan / Russia / Central Asia",
    "modules_used": [
      {"module": "global-think-tank-analyst", "role": "reasoning_method"},
      {"module": "central-asia-caspian", "role": "regional_specialist"},
      {"module": "sanctions-sector", "role": "sector_specialist"}
    ]
  },
  "risk_summary": {
    "short": "Treat KZ-RU mirror-statistics divergence as a portfolio-level EDD trigger, not proof of circumvention by itself.",
    "detailed": "The risk transmits through a chain: mirror-data anomaly -> possible misclassification, re-export or origin masking -> financing of high-priority goods -> correspondent, sanctions and export-control exposure for the European bank. The bank should calibrate thresholds around indicator combinations rather than a single data gap."
  },
  "decision_frame": {
    "decision": "Set EDD escalation and rejection thresholds for Kazakhstan-linked trade-finance clients over the next 6-12 months.",
    "stakeholders": ["Trade finance head", "Sanctions compliance", "Export-control counsel", "Correspondent banking lead"],
    "constraints": ["Trade statistics lag", "Specific list status changes", "Some anomalies are false positives"]
  },
  "analysis": {
    "facts": [
      "The upstream specialist example cites UN Comtrade, OFAC/BIS source classes, KSE/CREA, World Bank/Kazstat and FATF/EAG as the relevant source packet.",
      "Agenda Intelligence `analyze` does not accept `live_source_backed`; this run maps the upstream source-backed packet to `mixed`."
    ],
    "assessments": [
      "The binding decision is threshold calibration, not a binary finding that the portfolio is sanctionable.",
      "A mirror-statistics anomaly becomes actionable when it co-occurs with dual-use HS codes, weak BO, implausible end-use, new entities or route economics inconsistent with legitimate trade."
    ],
    "assumptions": [
      "The bank can access or request transaction documents at shipment level.",
      "The bank has no confirmed designated counterparty in the current case set."
    ],
    "unknowns": [
      "Current OFAC / BIS / EU / UK list status for any specific KZ counterparty.",
      "Current HS-code-level Kazstat / Russian FCS gap magnitude.",
      "Whether the apparent divergence is classification, timing, reporting lag, re-export, or deliberate concealment."
    ]
  },
  "recommended_actions": [
    {"action": "Make mirror-statistics anomaly plus high-priority HS code a mandatory EDD trigger.", "priority": "high", "trigger": "Any KZ-RU transaction in sensitive HS ranges", "time_horizon": "immediate"},
    {"action": "Require BO, end-use, certificate-of-origin and route-document reconciliation before approving elevated cases.", "priority": "high", "trigger": "EDD trigger fires", "time_horizon": "case-by-case"},
    {"action": "Run a 12-month look-back on KZ SME exporters by HS code, route and counterparty age.", "priority": "medium", "trigger": "Portfolio review cycle", "time_horizon": "60-90 days"}
  ],
  "watch_next": [
    {"indicator": "BIS / OFAC guidance or Entity List additions naming KZ entities", "trigger": "Any new KZ-nexus designation or advisory", "source_type": "regulator_announcement"},
    {"indicator": "UN Comtrade / Kazstat / Russian FCS mirror gap by HS basket", "trigger": "Gap widens or persists across consecutive reporting periods", "source_type": "customs_statistics"},
    {"indicator": "EU sanctions package or guidance on third-country re-export routes", "trigger": "KZ or Central Asia route named explicitly", "source_type": "legal_act"}
  ],
  "audit": {
    "validation_score": 1.0,
    "machine_verified": true,
    "provenance": [
      {"claim": "Mirror-statistics divergence is a risk indicator, not proof.", "basis": "assessment"},
      {"claim": "Specific current list status is unknown without live checks.", "basis": "unknown"},
      {"claim": "The run maps upstream live-source-backed material to mixed.", "basis": "fact"}
    ]
  }
}
```

## Scoring

| Criterion | A | B |
|---|---:|---:|
| Fact / assessment / assumption / unknown separation | 0 | 1 |
| Provenance discipline | 0.5 | 1 |
| Decision frame present | 0.5 | 1 |
| Scenarios with probability ranges | 0 | 0.5 |
| Options with explicit trade-offs | 0.5 | 1 |
| Failure modes with likelihood and impact | 0 | 0.5 |
| Watch-next indicators with triggers | 0.5 | 1 |
| Honest scope | 1 | 1 |
| **Total** | **3 / 8** | **7 / 8** |

**Delta:** +4.

## Observations

The baseline gives a practical compliance answer and correctly avoids treating the anomaly as proof. Its weakness is that it stays in prose: no explicit distinction between source-backed facts, assumptions and unknowns; no product-shell evidence-mode mapping; and no routing proof that the Central Asia specialist and sanctions-sector references were loaded.

The Agenda Intelligence condition adds the integration-critical behavior this case was designed to test. It maps upstream `live-source-backed` specialist work to `mixed`, preserves the unknowns around current list status and current HS-code gaps, and makes the decision frame threshold calibration rather than deal-level guilt. The delta is smaller than the correspondent case because the baseline was already fairly disciplined, but B is materially better for an agent workflow because it exposes provenance, unknowns, modules, and watch-next triggers in machine-readable form.

## Limitations

- One model, one prompt run. Not statistically significant.
- Self-scored by the author / host model. Not external review.
- Structural eval only. It does not verify the current OFAC, BIS, EU, UK or customs-statistics facts.
- The local `analyze` run verified request validity and module routing, but did not invoke an external LLM because no `ANTHROPIC_API_KEY` was configured.
- This is not a factual benchmark, model-quality comparison, aggregate claim, compliance conclusion, or practitioner validation.
