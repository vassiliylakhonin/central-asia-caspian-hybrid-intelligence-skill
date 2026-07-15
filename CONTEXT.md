# Central Asia + Caspian Hybrid Intelligence

This context defines the language for the Central Asia + Caspian vertical specialist inside the broader Agenda Intelligence stack. It exists to keep regional reasoning, evidence discipline, and validation boundaries distinct.

## Language

**Vertical Specialist**:
A regional reasoning skill that adds Central Asia and Caspian domain depth to a strategic-risk agent workflow.
_Avoid_: Platform, MCP server, validation engine, screening tool

**Agenda Intelligence MD**:
The deterministic evidence-packet linter that checks caller-supplied claim/source packets before human review. Older routing, memo validation, scoring, MCP, HTTP, and A2A behavior remains available for compatibility.
_Avoid_: Parent skill, source retriever, factual verifier, compliance product, commercial umbrella for this repo

**Evidence-Packet Handoff**:
The JSON seam from a **Specialist Memo** to Agenda Intelligence MD: externally checkable `claims[]`, declared `source_ids`, optional verbatim `quotes`, and caller-supplied `sources[]` text.
_Avoid_: Full memo serialization, factuality result, source-discovery step, analyst-judgment ledger

**Global Think Tank Analyst**:
The general strategic-risk reasoning method for policy-risk memos, scenarios, red-team framing, and broad analytical workflow.
_Avoid_: Regional specialist, source validator, Central Asia doctrine

**Regional Lens**:
A packaged regional frame used by Agenda Intelligence MD to route geography-specific analysis.
_Avoid_: Full specialist repo, source database, standalone analyst

**Regional Mechanism Logic**:
The Central Asia and Caspian-specific explanation of how risk transmits through local actors, corridors, banks, ownership structures, state capacity, and chokepoints.
_Avoid_: Generic memo method, universal strategy framework, geopolitical essay structure

**Risk Archetype**:
A reusable regional transmission pattern that explains how a class of risk typically moves through actors, flows, evidence, false positives, and watch-next triggers.
_Avoid_: Topic, sector label, generic risk category

**Agent-Validated Specialist Resource**:
A specialist repo whose historical usefulness evidence includes with/without agent-eval deltas against Agenda Intelligence MD's older `analyze` compatibility runtime.
_Avoid_: Externally validated resource, factual benchmark, practitioner-approved product

**Practitioner Trust Layer**:
Optional evidence from domain-practitioner review used when the audience needs buying-side trust beyond agent-integration validation.
_Avoid_: Hard agent-integration gate, benchmark, accuracy authority

**Authoring Source**:
The human-editable source of truth for the full Central Asia and Caspian regional reasoning logic.
_Avoid_: Runtime copy, packaged mirror, derived lens

**Runtime Projection**:
A condensed copy or reference used by Agenda Intelligence MD at runtime for routing and prompt assembly.
_Avoid_: Authoring source, complete regional doctrine, independent fork

**Sync Boundary**:
The rule for deciding which Authoring Source changes should be reflected in an Agenda Intelligence MD Runtime Projection.
_Avoid_: Mirror policy, automatic copy, fork maintenance

**Evidence Mode**:
The label that states what kind of evidence was available during a memo workflow.
_Avoid_: Retrieval capability, factual truth status, source guarantee

**Compatibility Analyze Evidence Mode**:
The evidence-mode vocabulary accepted by Agenda Intelligence MD's older `analyze` request and memo contract.
_Avoid_: Specialist example label, live retrieval mode, factual verification claim

**Specialist Memo**:
A mechanism-first analytical output produced using the Vertical Specialist's regional risk-transmission logic.
_Avoid_: Screening result, compliance determination, factual verification report

## Relationships

- Agenda Intelligence MD may route a request to one or more **Regional Lenses** through its older compatibility runtime.
- A **Regional Lens** is a **Runtime Projection** derived from a **Vertical Specialist**.
- The Central Asia + Caspian **Vertical Specialist** repo is the **Authoring Source** for full regional logic, including archetypes, source guidance, examples, and evidence discipline.
- A **Runtime Projection** should preserve the boundaries of its **Authoring Source** without trying to duplicate the full specialist repo.
- A **Sync Boundary** requires Agenda Intelligence MD updates only when the **Authoring Source** changes routing criteria, default regional checks, output skeleton, evidence-mode boundary, or anti-patterns.
- Changes to full archetypes, source-guide depth, examples, validation status, or practitioner-review evidence remain in the **Authoring Source** unless they affect compatibility routing or prompt assembly.
- The primary **Evidence-Packet Handoff** does not carry a memo-level evidence mode. It carries explicit claims, full source text, and optional verbatim quotes.
- When the older `analyze` compatibility runtime is used, `live-source-backed` examples map to `user_provided` or `mixed` because live retrieval happens upstream of that contract.
- **Global Think Tank Analyst** owns the generic memo method; the Central Asia + Caspian **Vertical Specialist** owns **Regional Mechanism Logic**.
- A concept belongs in this **Vertical Specialist** only when it changes the Central Asia or Caspian transmission channel, exposure, leverage, or decision.
- The **Risk Archetype** catalogue is extensible, but a new archetype must describe a regional transmission pattern, not merely name a sector or topic.
- A **Risk Archetype** should include mechanism, typical indicators, evidence needed, false positives, watch-next triggers, and role-based mitigation questions.
- An **Agent-Validated Specialist Resource** is validated through agent-output structure deltas, not through claims of factual accuracy or practitioner approval.
- A **Practitioner Trust Layer** may be added for compliance, AML, sanctions, banking, logistics, energy, or regional-risk practitioner audiences, but it is optional for agent-first validation.
- A **Vertical Specialist** produces the reasoning pattern behind a **Specialist Memo**.
- The primary **Evidence-Packet Handoff** lets Agenda Intelligence MD lint claim/source packet completeness without making the **Vertical Specialist** a validation engine or asserting factual truth.

## Example dialogue

> **Dev:** "Should the Central Asia + Caspian repo implement its own MCP validation tool?"
> **Domain expert:** "No — the **Vertical Specialist** owns regional reasoning. **Agenda Intelligence MD** owns routing, validation, audit, scoring, and MCP surfaces."
>
> **Dev:** "Where should we update a new Central Asia sanctions-routing archetype?"
> **Domain expert:** "In the **Authoring Source** first. Then update the **Runtime Projection** in Agenda Intelligence MD only if routing or prompt assembly needs the condensed version."
>
> **Dev:** "Should every new example in the specialist repo be copied into Agenda Intelligence MD?"
> **Domain expert:** "No. The **Sync Boundary** says examples stay in the **Authoring Source** unless they change routing behavior, the output skeleton, evidence-mode boundaries, or anti-patterns."
>
> **Dev:** "Can this specialist add `live_source_backed` to Agenda Intelligence MD's `analyze` request?"
> **Domain expert:** "No. Keep `live-source-backed` as a specialist example label. If the older `analyze` compatibility runtime is used, map it to a **Compatibility Analyze Evidence Mode** such as `user_provided` or `mixed`."
>
> **Dev:** "Should scenario framing rules live here?"
> **Domain expert:** "Only if the rule is about Central Asia or Caspian **Regional Mechanism Logic**. Generic scenario or red-team method belongs in **Global Think Tank Analyst**."
>
> **Dev:** "Can we add 'critical minerals' as a new archetype?"
> **Domain expert:** "Only if it is framed as a **Risk Archetype** with a transmission mechanism, indicators, evidence, false positives, triggers, and role-based mitigation. As a topic label alone, it belongs in examples or source guidance, not the archetype catalogue."
>
> **Dev:** "Do we need practitioner reviews to clear Bar 2?"
> **Domain expert:** "Not for an **Agent-Validated Specialist Resource**. Practitioner reviews belong in the optional **Practitioner Trust Layer** when the audience requires that kind of trust signal."

## Flagged ambiguities

- "part of Agenda Intelligence MD" was ambiguous. Resolved: Central Asia + Caspian is a **Vertical Specialist** in the broader Agenda Intelligence stack; Agenda Intelligence MD may package or route a **Regional Lens** derived from it, but the specialist repo remains the regional reasoning source rather than a validation or MCP product.
- "Regional Lens" and "Vertical Specialist" were easy to conflate. Resolved: the **Vertical Specialist** repo is the **Authoring Source**; the **Regional Lens** in Agenda Intelligence MD is a **Runtime Projection** for compatibility routing and prompt assembly.
- "sync" could mean byte-equal mirroring or selective projection. Resolved: synchronization follows the **Sync Boundary**; Agenda Intelligence MD is updated only for routing and prompt-assembly relevant changes.
- "evidence mode" spans multiple surfaces. Resolved: the specialist repo may keep example-facing **Evidence Modes**; the primary **Evidence-Packet Handoff** uses claim/source references, while the older `analyze` runtime uses the narrower **Compatibility Analyze Evidence Mode** vocabulary.
- "specialist reasoning" could mean either generic memo method or regional mechanism depth. Resolved: **Global Think Tank Analyst** owns generic method; this repo owns **Regional Mechanism Logic**.
- "risk archetype" could mean a sector/topic list. Resolved: a **Risk Archetype** is a regional transmission pattern with evidence and false-positive discipline.
- "validated specialist resource" could mean practitioner-reviewed or agent-tested. Resolved: hard Bar 2 means **Agent-Validated Specialist Resource**; practitioner review is a separate **Practitioner Trust Layer**.
