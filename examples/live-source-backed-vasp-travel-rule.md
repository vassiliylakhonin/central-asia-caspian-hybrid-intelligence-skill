# Live-source-backed example — VASP / Travel Rule enforcement gap (KZ / UZ)

> **Evidence mode: `live-source-backed`.**
>
> **Retrieval date: 2026-05-14.** All factual claims below are grounded in publicly retrievable primary or secondary sources cited inline. Sources are time-sensitive — FATF grey-list status, designations, and supervisory guidance change. Re-verify against current authoritative sources before any operational use.
>
> This memo is illustrative analysis. It is **not** legal, sanctions, AML, compliance, tax, audit or investment advice. It does not screen any counterparty against any list. Any operational decision requires source-backed re-verification at the time of decision and qualified professional review.

## User question

> "We are a European fintech integrating with a VASP licensed under the AIFC framework in Kazakhstan. Our compliance team needs to assess whether this counterparty meets EU Travel Rule standards (EU TFR 2023/1113) and whether supervisory gaps in Kazakhstan and Uzbekistan create secondary-sanctions or de-risking exposure for our own EU banking relationships."

## Bottom line

The EU Transfer of Funds Regulation 2023/1113 (effective 30 December 2024) imposes originator/beneficiary data requirements on all crypto-asset transfers regardless of value, with no de minimis threshold [S1]. KZ/UZ-licensed VASPs were assessed as having significant supervisory gaps in FATF/EAG evaluations — including partial compliance ratings on beneficial ownership verification and transaction monitoring [S3]. `Judgment`: a KZ AIFC-licensed VASP counterparty that has not demonstrably aligned its data standards with EU TFR requirements creates a material compliance gap for a European fintech, which may transmit into that fintech's correspondent banking relationships if EU banking partners treat the gap as elevated AML/CFT risk.

The structural mismatch is well-documented in primary FATF/EAG and EU legislative sources. The specific current supervisory posture of any individual VASP, and the current FATF grey-list status of Kazakhstan and Uzbekistan, are `Unknown` at the point of use and must be verified before acting.

## Primary risk driver

`Primary driver is:` Regulatory mismatch between EU TFR 2023/1113 (mandatory, no threshold, full originator/beneficiary data) and the supervisory maturity documented in FATF/EAG assessments of KZ/UZ VASP oversight — transmitted into the EU fintech's compliance position via its correspondent banking relationships.

## Risk transmission mechanism

1. **EU TFR 2023/1113 is in force.** The regulation (effective 30 December 2024) requires crypto-asset service providers (CASPs) and payment service providers transferring virtual assets to transmit full originator and beneficiary data on every transaction, regardless of value [S1]. There is no de minimis threshold — unlike the prior EUR 1,000 wire-transfer threshold under the pre-TFR framework. `Verified` [S1].

2. **AIFC-licensed VASPs operate under AFSA rules.** The Astana International Financial Centre Financial Services Authority (AFSA) has published a VASP licensing framework [S5]. Whether specific AFSA data transmission requirements align with EU TFR Article 14 standards (full name, account number/DLT address, physical address or national identity number, LEI for legal persons) is `Unknown` — AFSA alignment documentation was not retrieved in this session. `[verify]` against current AFSA rulebook at point of use.

3. **FATF/EAG KZ Mutual Evaluation 2023 documented VASP supervision gaps.** The EAG Mutual Evaluation Report for Kazakhstan (2023) assessed VASP-related elements under Recommendation 15 (New Technologies) and found significant gaps in supervisory coverage, beneficial ownership verification for VASP customers, and transaction monitoring maturity [S3]. `Verified` [S3]; specific ratings may have been updated in subsequent FATF follow-up cycles — `[stale-risk: 2023-06][verify]`.

4. **Compliance gap transmission to EU fintech.** If the KZ AIFC-licensed VASP cannot produce Travel Rule-compliant data on inbound/outbound transfers, the EU fintech's own CASPs or payment service providers face a breach of TFR Article 7 obligations (information accompanying transfers from outside EU). EU banking partners with policies covering VASP counterparty due diligence may treat the gap as elevated risk and apply EDD or reduce correspondent exposure. `Judgment` informed by [S1, S3].

5. **OFAC SDN exposure via virtual currency addresses.** OFAC maintains an SDN list that includes designated virtual currency addresses [S4]. If a KZ or UZ-linked VASP processes flows connected to designated actors or wallets, the EU fintech inherits indirect exposure. `Plausible` — OFAC has designated virtual currency addresses in prior enforcement cycles [S4]; specific KZ/UZ VASP connections are `Unknown`.

6. **De-risking feedback loop.** EU correspondent banks facing regulatory pressure to assess third-country VASP exposure may adopt blanket de-risking policies for KZ-licensed VASP counterparties, regardless of individual VASP controls. This is a secondary risk amplifier. `Plausible`; no specific correspondent bank policy retrieved in this session.

## Exposure map

| Channel | Exposure | Source |
|---|---|---|
| EU TFR 2023/1113 (Art. 14 third-country requirements) | Non-compliant KZ VASP data standards → EU fintech TFR breach | [S1] |
| AFSA VASP licensing / KZ VASP data standards | Gap between AFSA rulebook and EU TFR data fields is unverified | [S5] `[verify]` |
| FATF/EAG KZ MER 2023 — Recommendation 15 gaps | Supervisory gap documented: BO verification and TX monitoring | [S3] |
| OFAC SDN virtual currency addresses | Indirect exposure if KZ/UZ VASP processes flows involving designated wallets | [S4] |
| EU fintech ↔ EU correspondent banking relationship | Correspondent EDD or de-risking if KZ VASP exposure flagged | `Judgment` |
| Geographic flows: Astana (AIFC), Tashkent (UZ), Russia-adjacent corridors | Elevated scrutiny on flows connecting to sanctioned-party-adjacent routes | [S3] `[verify]` |

## Actor incentives

- **EU fintech**: seeks Central Asia / Caspian regional expansion, faces regulatory pressure from EU correspondent banks and EU supervisors. Incentive to conduct enhanced due diligence before integration rather than after a regulatory inquiry. `Judgment`.
- **KZ AIFC-licensed VASP**: AIFC framework explicitly designed to attract international capital and EU/UK-connected financial firms [S5]; VASP has commercial incentive to demonstrate EU TFR alignment to European counterparties. `Plausible`.
- **AFSA (AIFC Financial Services Authority)**: balances commercial attractiveness of the AIFC zone with reputational pressure from FATF/EAG assessment cycle. Supervisory cost of full FATF R15 / EU TFR alignment competes with AIFC growth mandate. `Judgment`.
- **EU correspondent banks**: incentive to de-risk from KZ crypto exposure if supervisory gap is flagged by EU regulators or EBA guidance. A single flagged KZ VASP incident can trigger category-level policy changes. `Plausible`.
- **FATF/EAG**: conducts follow-up review cycles that can affect KZ/UZ's standing on the FATF public statement (grey-list). `Verified` as procedural fact [S3]; current status `Unknown`.

## Role-based implications

### Fintech compliance officer — priority actions

1. **Travel Rule gap assessment.** Before integration, obtain the KZ VASP's written Travel Rule procedures and assess field-by-field alignment with EU TFR Article 14 data requirements. Request evidence of data transmission testing with EU-connected counterparties.
2. **Enhanced due diligence checklist.** Apply EDD to the KZ VASP as a third-country obliged entity: (a) AFSA license status, (b) beneficial ownership structure, (c) AML/CFT policies meeting FATF R10, R15, R16 standards, (d) transaction monitoring capability.
3. **Contractual Travel Rule warranties.** Include contractual warranties requiring the KZ VASP to transmit compliant Travel Rule data and to notify the EU fintech of any change in supervisory status or AFSA license.
4. **OFAC and EU SDN screening.** Independently screen the KZ VASP and its beneficial owners against current OFAC SDN, EU consolidated list, OFSI consolidated list, and UN list at point of onboarding and at periodic review. `[verify]` against lists current at point of use.

All actions are illustrative. Real implementation requires qualified compliance, legal and AML counsel.

### EU banking partner — EDD triggers

- KZ or UZ counterparty is a VASP or crypto intermediary: apply enhanced VASP EDD policy.
- Correspondent exposure to EU fintech increases if that fintech integrates KZ VASP: assess whether fintech's VASP counterparty risk is captured in correspondent EDD.
- Review against any EBA guidance on third-country VASP equivalence assessments when issued. `[verify]`.

### VASP operator (KZ AIFC-licensed) — alignment steps

- Conduct field-by-field gap analysis between AFSA rulebook data requirements and EU TFR Article 14.
- Implement Travel Rule protocol (e.g., IVMS 101 standard) aligned with EU CASP counterparty expectations.
- Engage AFSA on timeline for R15 / EU TFR alignment if gaps exist.
- Disclose compliance posture proactively to EU fintech counterparties rather than waiting for due diligence inquiries.

## Trigger points

1. **EBA / national EU regulator issues guidance on third-country VASP equivalence.** A formal EBA opinion or national competent authority guidance on how EU CASPs should assess third-country VASPs would directly affect the EU fintech's onboarding obligations. `[verify]` — no such guidance was retrieved in this session.
2. **OFAC designates a KZ or UZ-linked VASP or virtual currency address.** Any such designation would create direct SDN exposure and potential secondary-sanctions risk for the EU fintech and its banking partners [S4].
3. **FATF grey-listing of Kazakhstan or Uzbekistan.** If either jurisdiction is added to the FATF public statement (grey list), the EU fintech's correspondent banks would apply heightened third-country risk frameworks automatically. Current FATF status of KZ/UZ is `Unknown` — `[verify]` against current FATF public statement before acting [S2].
4. **AFSA announces regulatory alignment update with EU TFR.** A public AFSA announcement of R15 / EU TFR alignment would be a positive trigger reducing the supervisory gap concern [S5].
5. **EU correspondent bank issues updated VASP counterparty policy affecting KZ-licensed entities.** Category-level de-risking by a major EU correspondent bank would affect all EU fintechs with KZ VASP relationships, regardless of individual VASP quality.
6. **FATF R15 follow-up review for Kazakhstan.** EAG conducts follow-up reviews after MER publication; a revised rating on Recommendation 15 would update the supervisory gap baseline [S3].

## Unknowns

- **Current FATF grey-list status of Kazakhstan and Uzbekistan.** Must be verified against the current FATF public statement before any operational decision. `Unknown` in this session. `[verify]`.
- **Specific AFSA alignment with EU TFR Article 14 data fields.** AFSA rulebook data requirements were not retrieved in this session. `Unknown`. `[verify]` against current AFSA published rules at [S5].
- **Transaction monitoring threshold alignment.** Whether AFSA-required thresholds for VASP transaction monitoring match FATF R16 and EU TFR expectations is `Unknown`.
- **Individual VASP controls.** This memo addresses the structural gap; the specific KZ VASP counterparty's actual compliance posture requires direct due diligence, not inference from the supervisory environment.
- **EBA third-country equivalence guidance.** No EBA guidance on third-country VASP equivalence was retrieved in this session. `Unknown`.

## Confidence

`Confidence`: moderate — structural mismatch between EU TFR 2023/1113 requirements and the VASP supervisory gaps documented in FATF/EAG KZ MER 2023 is `Verified` from primary sources [S1, S3]. Specific current enforcement posture, individual VASP controls, current FATF grey-list status and AFSA alignment timeline are `Unknown` and must be re-verified before acting. Transmission mechanism from supervisory gap to EU fintech de-risking exposure is `Judgment` with plausible basis.

## What would change the judgment

- Documented AFSA alignment with EU TFR Article 14 data standards, publicly confirmed by AFSA.
- Positive FATF follow-up finding on KZ Recommendation 15 improving the supervisory baseline.
- EBA guidance establishing a third-country VASP equivalence recognition framework that includes AFSA.
- OFAC designation of a KZ or UZ-linked VASP or address (would sharply raise risk).
- FATF grey-listing of KZ or UZ (would sharply raise risk).
- EU correspondent bank de-risking KZ VASP category at scale (would sharply raise risk).

## Limitation note

This memo is `live-source-backed` as of the retrieval date stated above. Sources are time-sensitive: FATF grey-list status, supervisory ratings, regulatory guidance and sanctions designations change. This memo does not screen any specific VASP, wallet address, beneficial owner or financial institution against any sanctions, export-control or watchlist. It does not verify any factual claim about ownership, control, end-use or enforcement of any specific party. Any operational decision — including VASP onboarding — requires source-backed re-verification at the time of decision and qualified professional review.

`Author: Vassiliy Lakhonin`

## Sources

### Tier 1 — primary

- **[S1]** EU Regulation 2023/1113 of the European Parliament and of the Council on information accompanying transfers of funds and certain crypto-assets (Transfer of Funds Regulation / Travel Rule for crypto), effective 30 December 2024. Full text: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113
- **[S2]** FATF Updated Guidance for a Risk-Based Approach to Virtual Assets and Virtual Asset Service Providers (2023), including Recommendation 15 (New Technologies) application to VASPs. https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2023.html
- **[S3]** FATF/EAG, *Mutual Evaluation Report of the Republic of Kazakhstan* (2023) — VASP supervision section (Recommendation 15); also available via EAG index: https://eurasiangroup.org/files/mer/Kazakhstan_MER_2023_ENG.pdf
- **[S4]** OFAC Virtual Currency / VASP guidance and FAQ, including SDN designations of virtual currency addresses. OFAC FAQ topic page: https://ofac.treasury.gov/faqs/topic/1521
- **[S5]** AIFC Financial Services Authority (AFSA) VASP licensing framework and published rules. https://afsa.kz/en/

### Tier 2 — secondary (context)

- **[S6]** EAG Uzbekistan typologies and follow-up reports (for UZ VASP supervisory context). https://eurasiangroup.org

### Source-tier note

Compliance-side claims are anchored to primary EU legislative text ([S1]), FATF guidance ([S2]), and FATF/EAG MER ([S3]). OFAC virtual-currency guidance ([S4]) and AFSA framework ([S5]) are primary regulatory sources. No specific VASP names on OFAC SDN, specific KZ/UZ enforcement actions, exact transaction volumes, or current FATF grey-list status are stated — these are `Unknown` and must be verified against current lists at the point of use. For legal-grade work, re-retrieve current EU consolidated list, OFAC SDN, OFSI consolidated and UN lists directly.
