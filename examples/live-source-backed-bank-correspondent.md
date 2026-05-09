# Live-source-backed example — Bank correspondent and counterparty exposure (KZ)

> **Evidence mode: `live-source-backed`.**
>
> **Retrieval date: 2026-05-08.** All factual claims below are grounded in publicly retrievable secondary or primary sources cited inline. Sources are time-sensitive — designations, lists and supervisory guidance change. Re-verify against current authoritative sources before any operational use.
>
> This memo is illustrative analysis. It is **not** legal, sanctions, AML, compliance, tax, audit or investment advice. It does not screen any counterparty against any list. Any operational decision requires source-backed re-verification at the time of decision and qualified professional review.

## User question

> "We are a Kazakhstani mid-sized bank with USD and EUR correspondents through tier-1 EU and US institutions and a regional SME book (trading companies, freight forwarders, small fintechs). What's the next 12-month picture for correspondent and counterparty exposure, and where should compliance investment go?"

## Bottom line

The dominant near-term risk is **secondary-sanctions transmission via tier-1 correspondent EDD**, anchored by the US Executive Order 14114 (December 2023) framework that exposes non-US financial institutions (including those that "unknowingly" facilitate prohibited activity) to secondary sanctions [S1, S2]. Inside Kazakhstan, **VTB Bank Kazakhstan** is the locally licensed SDN-listed and EU-sanctioned reference point [S3]; the rest of the system has visibly de-risked from sanctioned Russian counterparties and is under sustained pressure [S3, S4]. UK and EU guidance frame the *supplier-bank-counterparty* circumvention pattern explicitly as a designation trigger [S5]. `Judgment` informed by [S1–S5].

For a mid-sized KZ bank, compliance investment is best concentrated on (a) HS-code and end-user-aware EDD on the SME book, (b) defensible BO data on trading companies and forwarders, (c) operational readiness for tier-1 correspondent reviews, and (d) explicit segmentation of any Russia-linked counterparty exposure.

## Primary risk driver

`Primary driver is:` US EO 14114 secondary-sanctions framework + sustained UK/EU coordinated enforcement attention on third-country circumvention, transmitted via tier-1 correspondent EDD onto KZ banks' SME books and the document chain.

## Risk transmission mechanism

1. The US Executive Order 14114 (issued 22 December 2023) authorizes secondary sanctions against foreign financial institutions involved in significant transactions related to Russia's military-industrial base; subsequent OFAC guidance (June 2024) clarified that "unknowing" facilitation does not shield a foreign financial institution from designation [S1, S2]. This is the standing legal trigger that drives tier-1 correspondent EDD.
2. The UK has published explicit sanctions guidance for Kazakh businesses (June 2025; updated August 2025) that names the *exact* circumvention pattern — Kazakh firm receives Russian-importer orders for UK-sanctioned goods, orders from UK suppliers without disclosing Russian end-user, re-exports to Russia — as a designation-eligible behaviour, and identifies the Common High Priority List (CHPL) as particularly concerning [S5].
3. Inside Kazakhstan, **VTB Bank Kazakhstan** is the only locally licensed SDN-listed financial institution as of April 2024 [S3]; the broader Kazakhstani banking sector has visibly ended correspondent relationships with sanctioned Russian counterparties [S3].
4. Sanctions pressure on the *Central Asian banking sector as a whole* has continued: through 2025, EU action expanded to additional Central Asian banks, with transaction bans tied to Russian financial-messaging and payment-system connections [S3, S4]. The Tajikistan SWIFT-bypass coverage in July 2025 illustrates the kind of pattern that draws further attention [S6].
5. Quantitative re-routing pressure visible since 2022 — a ~30% rise in KZ exports to Russia in 2022 (Oxford Economics, June 2024, cited via FPRI), and disproportionately larger figures for Armenia (~193%), against more modest Georgia (~5%) — establishes the underlying trade-flow signal that regulators and tier-1 correspondents are responding to [S3].
6. Net effect: tier-1 correspondents tighten EDD on KZ respondents; respondent banks with weak BO data, opaque SME counterparty structures or Russia-linked exposure feel rejection / delay risk first. AML/CFT supervisory baseline is documented in Kazakhstan's 2nd EAG mutual-evaluation report (2023) [S7, S7a].

## Exposure map

| Channel | Exposure | Source |
|---|---|---|
| US secondary-sanctions trigger via EO 14114 + June 2024 OFAC guidance | Designation risk for foreign financial institutions facilitating prohibited activity, including unknowingly | [S1, S2] |
| UK Russia Sanctions Regulations and CHPL-aligned circumvention patterns | Designation risk + supplier / banking / counterparty relationship loss | [S5] |
| EU coordinated enforcement on Central Asian banks (2025 cycle) | Transaction bans tied to Russian financial-messaging and payment-system connections | [S3, S4] |
| Locally SDN-listed VTB Bank Kazakhstan | Direct adjacency / counterparty exposure for KZ banks dealing with this entity | [S3] |
| Trade-flow re-routing (KZ 2022 +30%, Armenia +193%, GE +5% on exports to Russia) | Background signal driving regulatory and correspondent attention | [S3] |
| KZ AML/CFT supervisory framework (2nd EAG MER 2023) | Jurisdictional EDD baseline; not a designation event | [S7, S7a] |

## Sanctions / AML / banking considerations

- **Sanctions overlay**: SDN, BIS Entity List, EU consolidated, OFSI, UN — all relevant. **Real screening of any specific counterparty requires direct retrieval against current official lists at the time of decision.** `Unknown` here for any specific entity beyond what [S3] confirms (VTB Bank Kazakhstan).
- **EO 14114 and June 2024 OFAC guidance** mean a KZ bank can be designated for *unknowingly* significant Russia-MIB-related transactions; "we didn't know" is not a defence. This raises the bar on EDD and transaction monitoring [S2].
- **UK sanctions reach via "UK nexus"** extends to Kazakh businesses operationally, even though Kazakh firms are not legally obligated to comply with UK sanctions [S5].
- **EU package iterations** continue to add designations and tighten anti-circumvention provisions; verify against the EU consolidated list and current Council legal acts adopting / amending Regulation (EU) No 833/2014 and Regulation (EU) No 269/2014 (see `docs/regional-logic.md` taxonomy note).
- **AML predicate risks beyond circumvention** (kleptocracy proceeds, real-estate flows, drug-trafficking transit through KG/TJ) remain in the supervisory frame per FATF / EAG cycle [S7, S7a]; see `docs/risk-archetypes.md` archetypes 15 and 16.

## Leverage shifts

- **Gains leverage**: tier-1 correspondents (selectivity); Western enforcement bodies (deterrence); KZ banks with mature EDD and BO data quality.
- **Loses leverage**: KZ banks with concentrated Russia-linked exposure or opaque SME books; SME importers in CHPL-overlapping HS clusters; forwarders without BO clarity.

## Trigger points (watch-next)

- Further US Treasury / OFAC actions citing KZ entities or specifying Russia-MIB-related transaction thresholds [S1, S2].
- New EU Council legal acts adding KZ-related designations or anti-circumvention provisions [S3, S4].
- UK OFSI updates referencing KZ businesses or supplier-bank patterns [S5].
- EAG follow-up reports affecting Kazakhstan's 2023 MER ratings [S7].
- Public enforcement on a regional bank for circumvention or AML failure.
- Material expansion or contraction of Russia-linked correspondent relationships in KZ.

## Role-based actions

- **Compliance / sanctions team**: integrate EO 14114 + June 2024 guidance + UK CHPL pattern as standing screening rules; make HS-code-aware EDD a default for SME trading-company onboarding; document defensible BO chains using primary registry data; build adjacency-detection beyond name match (control tests, address / director clustering, post-designation continuity). *Subject to internal policy and regulatory review.*
- **Commercial / treasury**: diversify correspondent relationships across rails where lawful; segment book by HS-code and BO-clarity risk; pre-empt tier-1 EDD inquiries with structured EDD packets.
- **Internal audit**: stress-test transaction monitoring against EO 14114 Russia-MIB-related transaction definition; document evidentiary trail for "knew or should have known" defence.
- **Bank board / risk committee**: review correspondent concentration, KZ-jurisdictional reputational exposure, and de-risking history at the portfolio level.
- **Investor in the bank**: scrutinize correspondent concentration, EDD program maturity, BO data quality and de-risking incidents.

All actions are illustrative. Real implementation requires qualified compliance, legal and banking counsel.

## Unknowns

- Designation status of any specific KZ counterparty as of today (must be re-verified).
- Internal data quality at the bank under review.
- Specific EU package contents and current EU consolidated list state at point of use.
- Live tier-1 correspondent EDD policy at named institutions.

## Confidence

`Confidence`: medium for the structural mechanism (EO 14114 + UK CHPL + EU enforcement transmitted via tier-1 EDD), grounded in retrieved primary and authoritative secondary sources; low for any time-sensitive claim about today's designations or correspondent-bank policies without re-verification.

## What would change the judgment

- Material de-escalation in US/UK/EU secondary-sanctions posture toward third-country circumvention.
- Visible tier-1 correspondent withdrawal from KZ at scale (would sharply raise risk).
- Major designation of a KZ-system-relevant bank or fintech (would sharply raise risk).
- A binding and visibly enforced regional BO regime that materially raises baseline counterparty transparency.
- Further widening of EU transaction bans on Central Asian banks beyond the 2025 cycle [S3, S4].

## Limitation note

This memo is `live-source-backed` as of the retrieval date stated above. Sources are time-sensitive: designations, list status, supervisory guidance and EU packages change. This memo does not screen any specific counterparty, item, vessel, port, financial institution, fintech, forwarder or financier against any sanctions, export-control or watchlist. It does not verify any factual claim about ownership, control, end-use or enforcement of any specific party. Any operational decision requires source-backed re-verification at the time of decision and qualified professional review.

`Author: Vassiliy Lakhonin`

## Sources

### Tier 1 — primary

- **[S1]** Executive Order 14114 (22 December 2023), *Taking Additional Steps With Respect to the Russian Federation's Harmful Activities* — authorizes secondary sanctions against foreign financial institutions involved in significant transactions related to Russia's military-industrial base. Federal Register and Treasury references; consult OFAC Russia-related Sanctions Programs page for current authority. https://ofac.treasury.gov/sanctions-programs-and-country-information/russian-harmful-foreign-activities-sanctions
- **[S2]** OFAC Russia-related guidance and FAQ updates following EO 14114, including the June 2024 update emphasizing that "unknowing" facilitation by foreign financial institutions does not shield from designation. Latest Russia-related FAQ topic page: https://ofac.treasury.gov/faqs/topic/6626
- **[S5]** UK Government, *UK sanctions guidance for Kazakh businesses* (Foreign, Commonwealth & Development Office; published 27 June 2025; last updated 19 August 2025) — explicit circumvention pattern, CHPL emphasis, sectors covered. https://www.gov.uk/guidance/uk-sanctions-guidance-for-kazakh-businesses
- **[S7]** Eurasian Group (EAG), *Mutual evaluation reports* index — including Kazakhstan 2nd MER (2023). https://eurasiangroup.org/en/mutual-evaluation-reports
- **[S7a]** FATF/EAG, *Mutual Evaluation Report of the Republic of Kazakhstan, 2023* — primary report PDF. https://www.fatf-gafi.org/content/dam/fatf-gafi/fsrb-mer/Kazakhstan-EAG-Mutual-Evaluation-2023.pdf.coredownload.inline.pdf

### Tier 2 — secondary reporting (used for accessible interpretation, not as the basis for legal claims)

- **[S3]** Foreign Policy Research Institute, *The Impact of Russia Sanctions on Central Asia* (16 December 2024) — VTB Bank Kazakhstan as the only locally licensed SDN-listed financial institution as of April 2024; Kazakhstani banks ended correspondent relationships with sanctioned Russian counterparties; Oxford Economics (June 2024) trade-flow figures (KZ +30%, AM +193%, GE +5% in 2022 exports to Russia). https://www.fpri.org/article/2024/12/the-impact-of-russia-sanctions-on-central-asia/
- **[S4]** The Diplomat, *More Central Asian Banks Sanctioned by the EU* (October 2025) — coverage of expanded EU action on Central Asian banks with transaction bans tied to Russian financial-messaging and payment-system connections. https://thediplomat.com/2025/10/more-central-asian-banks-sanctioned-by-the-eu/
- **[S6]** The Diplomat, *How Tajikistan's Banks Help Russian Citizens Bypass SWIFT Ban* (July 2025) — illustrative coverage of regional banks acting as SWIFT-bypass channels. https://thediplomat.com/2025/07/how-tajikistans-banks-help-russian-citizens-bypass-swift-ban/

### Source-tier note

Compliance-side claims are anchored to primary OFAC ([S1], [S2]), UK Government ([S5]) and FATF/EAG ([S7], [S7a]) URLs. Trade-flow and bank-system claims rely on Tier 2 reporting ([S3], [S4], [S6]) for accessible numeric framing; primary equivalents (OFAC SDN list entries, EU Council legal acts, EU consolidated list, Oxford Economics original report) should be retrieved directly for legal-grade work. For any operational decision, re-verify against current OFAC SDN, BIS Entity List, EU consolidated, OFSI consolidated and UN lists at the point of use.
