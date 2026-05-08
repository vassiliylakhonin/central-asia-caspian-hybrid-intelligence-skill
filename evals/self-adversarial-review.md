# Self-adversarial review

> **What this is:** an adversarial stress-test of the repo by the LLM that helped build it.
>
> **What this is not:** external validation. Per [`AGENTS.md`](../AGENTS.md) Definition of Done, B2.2 and B2.7 require an identifiable external reviewer; that bar is **not** cleared by this file. This document does not change [`STATUS.md`](../STATUS.md).
>
> **Purpose:** to surface concrete weaknesses that a domain practitioner might flag, before such a reviewer is available, so the issues are visible rather than hidden. Findings are hypotheses to test against real practitioner review, not pre-emptive corrections.

## Method

Self-adversarial review tries to argue *against* the artifacts on three axes:

1. **Factual reliability** — could a careful reader catch an unsupported or stretched claim?
2. **Practitioner usefulness** — would a real compliance / corridor / banking analyst find the output decision-useful, or just structurally tidy?
3. **Scope and coverage gaps** — is something material to the domain missing?

Each finding is severity-labeled: 🔴 likely-flagged-by-practitioner, 🟡 borderline, 🟢 nice-to-have.

## Findings

### A. Factual reliability

🔴 **A1. The October 30, 2024 jy2700 fact about a "Kazakhstan-based intermediary" is one chain-link from primary.** The claim is supported by a search snippet from a Treasury announcement; the Treasury press release page itself timed out on retrieval. A practitioner doing legal-grade review would expect either a direct extract from the OFAC SDN entry naming the entity, or a Federal Register citation, before citing this in a memo. *Mitigation:* before any operational reuse, retrieve the named-entity OFAC entry directly and cite by SDN list ID.

🔴 **A2. Tier 2 sources still carry quantitative weight.** Specific numbers — €18.5 bn, 76,900 TEUs, 36% growth, 100+ million tonnes Northern Corridor — come from Caliber.az and Asia House, not from EBRD/operator publications directly. Tiering is honestly disclosed, but a reviewer can argue that for capacity numbers, primary EBRD and port-authority disclosures should be retrieved. *Mitigation:* fetch the EBRD original report and port-authority statistics where possible.

🟡 **A3. "Wind-day downtime at Aktau" reads as a primary capacity constraint.** The World Bank study identifies wind-related operational issues, but a port-operations practitioner may push back that wind days are a manageable scheduling factor, not the binding capacity ceiling — equipment, berth count, ferry tonnage and rail-port interface may matter more. The memo conflates *one named issue* with the whole capacity story.

🟡 **A4. The August 23, 2024 OFAC action is named but not parsed.** The memo links to `recent-actions/20240823` but does not enumerate what the action actually contained beyond the page title. A practitioner would expect either omission or a one-paragraph summary of the GLs and FAQ updates issued that day.

### B. Practitioner usefulness

🔴 **B1. Mode selection guidance is too generic.** A real analyst hitting a question rarely knows in advance whether to pick Risk/Compliance, Strategic or Hybrid. The skill files describe each mode but don't give *concrete decision rules* (e.g. "if the question contains a counterparty name and a timeline shorter than 90 days, use Risk/Compliance"). Result: in practice the skill defaults to Hybrid and produces over-broad answers.

🔴 **B2. Confidence labels are vibes, not a scale.** "Medium-high" is everywhere; there is no operational definition of when "medium" should drop to "low" or rise to "high". A risk officer will not be able to act on this differentially.

🔴 **B3. No coverage of digital assets / crypto rails.** Central Asia is materially exposed to crypto-VASP flows, P2P off-ramps, stablecoin corridors and OTC desks; this is a top-3 AML topic for KZ/UZ/KG. The skill mentions "crypto-VASP-adjacent" once in passing. Real EDD work in the region engages this much more.

🔴 **B4. Russia's parallel financial system is missing.** SPFS, Mir, NSPK, ruble settlement, regional CB swap lines — none of these appear in the corridor or banking memos despite being the actual workaround that SME flows use when USD/EUR rails tighten. A bank correspondent practitioner would notice this gap immediately.

🟡 **B5. Role-based actions are uniformly worded.** "Subject to internal policy and regulatory review" appears almost verbatim across roles. A compliance officer's actions are not the same shape as a logistics operator's; the current memos sometimes flatten that.

🟡 **B6. EU sanctions package iterations not surfaced.** EU Council adopts packages in numbered cycles; practitioners track them by number. The skill is silent on this taxonomy.

🟢 **B7. Out-of-scope handling is implicit.** If a user asks about Iran sanctions or Afghanistan financial flows, neither the skill files nor `docs/regional-logic.md` give clear redirect language. Result: the skill may answer with low quality rather than declining.

### C. Scope and coverage gaps

🔴 **C1. AML predicates other than circumvention are under-served.** Kleptocracy, real-estate proceeds, kompromat-driven flows, drug trafficking through KG/TJ, are all material AML topics in the region and absent from the archetypes and examples.

🔴 **C2. Practitioner workflows are not addressed.** The skill outputs memos. Real practitioners do screening cycles, periodic reviews, transaction-monitoring tuning, regulatory reporting. The skill produces nothing tailored to those rhythms — a practitioner may say "this is a position paper, not a workflow tool."

🟡 **C3. Cross-border tax angle missing.** Tax residency of trading shells, treaty-shopping through CIS jurisdictions, transfer pricing on commodity chains — these intersect AML/sanctions and the skill is silent.

🟡 **C4. Climate / energy transition exposure lightly addressed.** Methane, CBAM, and stranded-asset risk on Caspian fossil infrastructure are touched briefly in `examples/energy-infrastructure-corridor-risk.md` but not as a first-class archetype.

🟢 **C5. Skill variants are near-identical.** This is already noted in DoD as B2.4 (open). Three platforms × the same content is a discoverability issue, not a quality issue, but a reviewer will mention it.

🟢 **C6. "Author: Vassiliy Lakhonin" is required everywhere.** Validation enforces this string, which awkwardly couples skill content to a single named human even when other contributors edit the files. A reviewer may flag the validation rule as overly personal.

## What this review does not establish

- It does **not** prove the findings are correct. A real practitioner may agree, disagree or surface different issues entirely.
- It does **not** close any Bar 2 criterion. B2.2 / B2.7 still require an identifiable external reviewer.
- It does **not** justify changes to `STATUS.md`.
- It is **not** a substitute for soliciting practitioner review when access is available.

## How to use this file

When a real external reviewer arrives, give them a memo, the rubric, and *do not* show them this file in advance — let their findings stand independently. After their review, compare. If a practitioner surfaces something here, that is mild signal the self-review tracked reality. If a practitioner surfaces something not here, that is more useful — it shows where self-review is blind.
