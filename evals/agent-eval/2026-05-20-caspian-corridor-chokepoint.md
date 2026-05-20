# Agent-eval: caspian-corridor-chokepoint

- **Question (verbatim):** An energy buyer and logistics operator depends on Middle Corridor / Trans-Caspian routes through Aktau, Kuryk and Baku/Alat. What chokepoint and corridor-execution risks matter over the next 12-18 months, and what should they watch before committing volume?
- **Model:** GPT-5 (Codex host model in this session)
- **Date:** 2026-05-20
- **Evidence mode:** `reasoning_only`
- **Skill under test:** central-asia-caspian-hybrid-intelligence-skill
- **Routing in Condition B:** Local `agenda-intelligence-md` `analyze` request validation returned GTTA + `central-asia-caspian`. No external LLM was invoked locally because `ANTHROPIC_API_KEY` was not configured; the host model completed both conditions using the same model.

## Condition A — Baseline (no MCP)

Prompt: "Answer concisely and decision-usefully in 350-450 words. No structure imposed."

Generated output:

> The main risk is that the Middle Corridor looks more flexible on paper than it is operationally. The route depends on a sequence of rail, port, ferry and border nodes: inland movement to Aktau or Kuryk, Caspian ferry capacity, Baku/Alat handling, onward rail through the South Caucasus and connections toward Türkiye or the EU. A delay at any one node can absorb the savings from avoiding the Northern route.
>
> Before committing volume, the buyer should watch actual dwell times and slot availability rather than headline corridor announcements. Key indicators are ferry availability, port congestion at Aktau/Kuryk and Baku/Alat, railcar and locomotive availability, border inspection times, and whether operators publish reliable throughput data. Capacity expansions matter only when they translate into scheduled service and lower variance.
>
> The second risk is contractual rigidity. If the buyer commits fixed volumes without fallback routes, it becomes a price taker when the Caspian leg tightens. Contracts should include flexibility on delivery windows, alternative routes, demurrage allocation, and cancellation or re-routing rights.
>
> Third, there is a financing and compliance overlay. Even where the cargo itself is not sanctioned, banks and insurers may scrutinize counterparties, origin, ownership and routing because the corridor is used as an alternative to Russia-linked routes. That can slow payments and documentation.
>
> Practical steps: run a lane-by-lane stress test; cap committed volumes until observed transit-time variance improves; pre-book ferry slots where possible; maintain at least one fallback route for critical cargo; require counterparties to disclose operator, forwarder and beneficial-ownership information; and build a weekly dashboard for dwell times, freight rates, ferry outages, border delays and sanctions guidance.

Word count: 274.

## Condition B — Agenda Intelligence Product Shell (GTTA + CA-Caspian loaded)

The `analyze` request used `evidence_mode: "reasoning_only"` and routed to:

```json
[
  {"module": "global-think-tank-analyst", "role": "reasoning_method"},
  {"module": "central-asia-caspian", "role": "regional_specialist"}
]
```

Generated output excerpt in agenda-memo shape:

```json
{
  "meta": {
    "evidence_mode": "reasoning_only",
    "depth": "decision_pack",
    "geography": "Kazakhstan / Caspian / Azerbaijan / Middle Corridor",
    "modules_used": [
      {"module": "global-think-tank-analyst", "role": "reasoning_method"},
      {"module": "central-asia-caspian", "role": "regional_specialist"}
    ]
  },
  "risk_summary": {
    "short": "The binding risk is not geopolitical rhetoric; it is node concentration across the Caspian sea-leg, ports, rail interfaces and border procedures.",
    "detailed": "The route is only as reliable as its least flexible node: KZ rail access -> Aktau/Kuryk yards -> ferry capacity -> Baku/Alat handling -> South Caucasus rail -> onward EU/Türkiye links. Commit volume only if contracts preserve rerouting rights and if observed dwell-time variance, ferry reliability and border processing are acceptable for the cargo's tolerance."
  },
  "decision_frame": {
    "decision": "Whether to commit additional 12-18 month volume to Middle Corridor / Trans-Caspian routing or keep fallback routes warm.",
    "stakeholders": ["Energy buyer", "Logistics operator", "Treasury", "Insurer", "Infrastructure-investment team"],
    "constraints": ["No live throughput checked in reasoning_only mode", "Capacity announcements may not equal usable capacity", "Fallback routes may carry different compliance or price risk"]
  },
  "analysis": {
    "facts": [],
    "assessments": [
      "The primary transmission mechanism is node-concentration risk cascading into dwell-time variance, freight repricing and working-capital strain.",
      "The specialist contribution is corridor mechanics: ports, ferries, rail interfaces, border friction and operator incentives, not a sanctions-only answer."
    ],
    "assumptions": [
      "Cargo can tolerate some delay but not multi-week variance.",
      "The buyer has at least one plausible fallback route or inventory buffer.",
      "No specific operator designation is assumed."
    ],
    "unknowns": [
      "Current ferry fleet utilization and unscheduled outage rate.",
      "Current dwell times at Aktau, Kuryk, Baku and Alat.",
      "Current railcar / locomotive availability and border inspection times.",
      "Current insurance and financing conditions for the exact counterparties."
    ]
  },
  "scenarios": [
    {
      "name": "Managed growth",
      "probability_range": {"low": 0.45, "high": 0.60},
      "drivers": ["Stable ferry operations", "No major port disruption", "Fallback routes retained"],
      "implications": ["Commit incremental volume in tranches; keep contingency clauses active"]
    },
    {
      "name": "Caspian node squeeze",
      "probability_range": {"low": 0.25, "high": 0.40},
      "drivers": ["Ferry outage", "Port yard congestion", "Weather or inspection delays"],
      "implications": ["Dwell-time spike; working-capital lockup; need rerouting or inventory drawdown"]
    },
    {
      "name": "Compliance / finance drag",
      "probability_range": {"low": 0.15, "high": 0.30},
      "drivers": ["Counterparty EDD escalation", "HS-code or ownership opacity", "Insurance tightening"],
      "implications": ["Payments and insurance slow even if physical route remains open"]
    }
  ],
  "options": [
    {
      "option": "Commit volume in tranches with route-flex clauses.",
      "pros": ["Preserves upside from corridor diversification", "Limits lock-in"],
      "cons": ["May cost more than fixed commitment"],
      "trade_offs": ["Optionality vs unit cost"]
    },
    {
      "option": "Delay commitment until dwell-time and ferry metrics stabilize.",
      "pros": ["Avoids buying into announcement-driven capacity"],
      "cons": ["May lose slots or commercial priority"],
      "trade_offs": ["Evidence quality vs market access"]
    }
  ],
  "recommended_actions": [
    {"action": "Build a weekly node dashboard for Aktau, Kuryk, ferry crossings, Baku/Alat, BTK and border dwell times.", "priority": "high", "trigger": "Before any volume commitment", "time_horizon": "30 days"},
    {"action": "Make rerouting rights, demurrage allocation and documentation obligations explicit in contracts.", "priority": "high", "trigger": "New or renewed volume contract", "time_horizon": "contracting cycle"},
    {"action": "Run a single-node failure tabletop for ferry outage, port congestion and border inspection shock.", "priority": "medium", "trigger": "Before peak season", "time_horizon": "60 days"}
  ],
  "watch_next": [
    {"indicator": "Aktau / Kuryk / Baku / Alat dwell time", "trigger": "Sustained deterioration across two reporting periods", "source_type": "operator_publication"},
    {"indicator": "Caspian ferry availability", "trigger": "Unscheduled outage, retirement or delayed fleet addition", "source_type": "operator_publication"},
    {"indicator": "Border rule or inspection change", "trigger": "New customs documentation or permit requirement", "source_type": "government_release"},
    {"indicator": "Financing or insurance tightening", "trigger": "Bank or insurer asks for new EDD on corridor counterparties", "source_type": "counterparty_communication"}
  ],
  "audit": {
    "validation_score": 1.0,
    "machine_verified": true,
    "provenance": [
      {"claim": "No live throughput was checked.", "basis": "unknown"},
      {"claim": "Node concentration is the primary mechanism.", "basis": "assessment"},
      {"claim": "Capacity announcements may not equal usable capacity.", "basis": "assessment"}
    ]
  }
}
```

## Scoring

| Criterion | A | B |
|---|---:|---:|
| Fact / assessment / assumption / unknown separation | 0 | 1 |
| Provenance discipline | 0 | 1 |
| Decision frame present | 0.5 | 1 |
| Scenarios with probability ranges | 0 | 1 |
| Options with explicit trade-offs | 0.5 | 1 |
| Failure modes with likelihood and impact | 0.5 | 1 |
| Watch-next indicators with triggers | 0.5 | 1 |
| Honest scope | 0.5 | 1 |
| **Total** | **2 / 8** | **8 / 8** |

**Delta:** +6.

## Observations

The baseline is operationally useful and already avoids a sanctions-only framing. Its weakness is that it compresses all reasoning into advice prose: it does not separate assumptions from unknowns, quantify scenarios, preserve module provenance, or expose a machine-readable decision frame.

The Agenda Intelligence condition shows why the Central Asia + Caspian specialist is not merely a sanctions/AML module. It improves the shape of the answer around corridor mechanics: node chain, ferry/port/rail dependencies, dwell-time variance, rerouting rights, operator incentives and fallback-route optionality. This case is an important complement to the correspondent and customs cases because the regional specialist must demonstrate logistics and energy-corridor reasoning, not just financial-crime reasoning.

## Limitations

- One model, one prompt run. Not statistically significant.
- Self-scored by the author / host model. Not external review.
- Structural eval only. It does not verify current ferry capacity, port dwell times, rail schedules, freight rates, insurance terms or operator status.
- The local `analyze` run verified request validity and module routing, but did not invoke an external LLM because no `ANTHROPIC_API_KEY` was configured.
- This is not a factual benchmark, model-quality comparison, aggregate claim, operational recommendation, investment advice, or practitioner validation.
