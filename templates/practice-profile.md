# Practice profile — Central Asia + Caspian

> **Status:** [DRAFT — contains `[PLACEHOLDER]` markers | POPULATED | STALE: last reviewed YYYY-MM-DD]
>
> Populate via `docs/cold-start-interview.md`. The skill should **STOP and run the interview** if this file is missing or still contains `[PLACEHOLDER]` markers when a memo is requested in a workflow that expects a profile.

**Last reviewed:** [YYYY-MM-DD]

---

## 1. Role and mandate

- **User role:** [e.g. sanctions compliance officer at a Tier 1 European bank]
- **Memo readers:** [e.g. head of financial-crime compliance, MLRO, transaction approval committee]
- **Decision type the memo informs:** [e.g. counterparty onboarding / transaction approval / corridor routing / market-entry / advisory]
- **Cost of being wrong — over-cautious direction:** [e.g. losing legitimate corridor business to a competitor]
- **Cost of being wrong — under-cautious direction:** [e.g. OFAC enforcement action; correspondent de-risking by USD clearer]

## 2. Geography and jurisdictions

- **Countries in scope by default:** [e.g. KZ, UZ, AZ; Russia and China only as interface]
- **Countries out of scope:** [e.g. TM unless oil-and-gas; Iran except via Caspian routing]
- **Regulatory exposure jurisdictions:** [e.g. US (OFAC, secondary sanctions); EU; UK OFSI]
- **Operational jurisdictions:** [e.g. EU-licensed entity with USD clearing through US correspondent]

## 3. Decision context and risk appetite

- **Default time horizon:** [e.g. transactional / 6–12 months / multi-year]
- **Posture:** [e.g. zero residual risk on OFAC nexus; risk-priced on BO opacity; opportunistic with mitigation on emerging-corridor exposure]
- **Non-negotiable red lines:** [e.g. any direct or indirect OFAC SDN nexus; any documented BO link to designated person; any transit through a designated port]
- **Acceptable mitigations:** [e.g. enhanced due diligence + officer attestation; restructured routing; counterparty-level guarantees]

## 4. Source access

- **Primary sources accessible directly:** [e.g. OFAC SDN online, EU consolidated list, OFSI, FATF MERs, national registries — name what you actually have access to]
- **Paid databases / feeds available:** [e.g. Dow Jones Risk, World-Check, S&P Global Capital IQ, customs data subscription — name them]
- **Sources not accessible (flag `[verify]` when cited):** [e.g. national-language gazettes in TM and TJ; certain regional court records]
- **External retrieval available to the skill:** [yes — web search / MCP / WebFetch | no — user-provided source packets only]
- **Live retrieval limitations:** [e.g. corporate proxy blocks Treasury.gov; FATF blocks automated fetch — sources will be marked `[verify]`]

## 5. Output preferences

- **Default memo length:** [quick note / standard memo / extended brief]
- **Analysis vs operational recommendation boundary:** [e.g. memo presents options + trade-offs; operational call belongs to MLRO]
- **Confidentiality / privilege markings:** [e.g. "Privileged & Confidential — Prepared at the request of counsel"]
- **Output format conventions:** [e.g. Risk Severity + Decision Relevance dual rating per the AGENTS.md dual-severity rule]

## 6. Standing assumptions and disclaimers

- **Standing assumptions:** [e.g. user has primary responsibility for sanctions screening against current OFAC list at point of operational decision; skill output is not screening]
- **Standing disclaimers:** [e.g. all memos are draft for compliance review; not legal or compliance advice]

---

## How to use this profile

1. The skill reads this file at the start of any memo request in this project.
2. The first six sections become the default `Decision / Audience / Geography / Time horizon / Evidence mode / Depth` block of every memo.
3. If a one-off question diverges from the profile, state the divergence in the memo header rather than overriding the profile silently.
4. To update the profile, ask the skill to re-run the cold-start interview, or edit this file directly.

## STOP rule

If any field above still reads `[PLACEHOLDER]` when a memo is requested in a workflow that expects a profile — **stop and run the cold-start interview before producing output**. Generic memos with unstated audience are worse than no memo.
