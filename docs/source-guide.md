# Source guide

This guide lists **classes of sources** to prefer for source-backed Central Asia / Caspian risk analysis. The skill itself does **not** retrieve these sources. Use them with external retrieval, user-provided source packets, or companion tooling.

## Evidence mode vocabulary

Every example and every memo produced with this skill must state one of four canonical evidence modes:

- **`live-source-backed`** — facts retrieved from current authoritative sources at the time of writing. Cite the source class behind each non-trivial factual claim.
- **`user-provided sources`** — facts grounded in a source packet supplied by the user. Treat the packet as the boundary of factual authority; do not extrapolate beyond it without labeling.
- **`illustrative source packet`** — facts grounded in a constructed, illustrative source packet for demonstration purposes. Must be marked as illustrative; do not present as real-world fact.
- **`reasoning-only`** — no sources retrieved; structural reasoning only. Do not assert factual conclusions about specific entities, designations or enforcement actions.

State the evidence mode at the top of any memo. Mixing modes within a memo is allowed only if each section is labeled.

## Disclaimer

The skill does not verify facts by itself. These sources are recommended for source-backed workflows using external retrieval, user-provided source packets, or companion tooling. Listing a source class here is not an endorsement and is not a guarantee of accuracy, completeness or timeliness for any specific question.

## Tier 1 — official and primary

### Sanctions and export controls
- US OFAC (SDN, sectoral, and related lists)
- EU consolidated sanctions list and EU Council legal acts — the EU adopts sanctions in numbered packages (e.g. 14th, 15th package); practitioners track by package number and Council decision date. Retrieve both the current consolidated list and the most recent package legal act; they are separate documents.
- UK OFSI consolidated list and HM Treasury notices
- UN Security Council consolidated list
- National sanctions regimes where relevant (e.g. Switzerland, Canada, Japan, Australia)
- Common high-priority items lists and circumvention guidance

### National regulators and central banks
- National Bank / central bank publications (KZ, UZ, AZ, KG, TJ, TM where available)
- Financial market regulators (e.g. AFSA in AIFC, financial-monitoring agencies)
- Banking supervision and licensing registers
- Securities and exchange regulators

### Customs, statistics, trade
- National customs committees and trade statistics agencies
- UN Comtrade and partner mirror-data sources
- WTO trade policy reviews
- Eurasian Economic Union statistical bulletins where relevant

### Company registries and legal records
- Official company / legal-entity registers
- Beneficial-ownership registers where available
- Court records, gazettes and insolvency registers
- Procurement portals and state-tender records

### Financial intelligence and AML-relevant public sources
- FATF mutual-evaluation reports and follow-ups
- Egmont Group public materials
- Public FIU typology reports where published
- MONEYVAL / EAG reports as applicable

### International financial institutions and multilateral bodies
- IMF Article IV and country reports
- World Bank country and sector reports
- EBRD, ADB, AIIB country strategies and project documents
- OECD reviews where applicable

### Government releases
- Presidential, prime-ministerial and ministry communiqués
- Parliamentary acts and gazettes
- State-owned enterprise disclosures

### Ports, rail, corridor and logistics operators
- Port authority statistics (e.g. Aktau, Kuryk, Baku/Alat, Turkmenbashi)
- Rail operator disclosures (KTZ, UTY, ADY, etc.)
- Middle Corridor / TITR coordinating bodies
- Customs throughput and dwell-time data where published

### Energy and infrastructure sources
- National oil/gas company disclosures (KMG, SOCAR, Uzbekneftegaz, etc.)
- Pipeline and grid operator publications (CPC, BTC, Galkynysh-related operators, regional grids)
- Ministry-of-energy publications
- IEA and OPEC reports for global context where material

## Tier 2 — secondary, clearly marked as secondary

- Credible regional and international media with track record on the region
- Established think-tank publications focused on Eurasia, Caspian, sanctions, AML and corridors
- Industry associations (banking, payments, logistics, energy) where they publish primary data
- Academic and policy institute work with transparent methodology
- Specialized open-source intelligence outlets, where claims can be cross-checked

Use Tier 2 for context, hypothesis generation and triangulation. Do not use Tier 2 alone for legal, compliance, ownership or enforcement claims.

## Source freshness horizons

Sources decay at different rates. Use the horizons below as the default re-verification practice for `live-source-backed` and `user-provided sources` memos. A source older than its horizon is **stale by default** until re-verified or explicitly re-labeled.

| Claim type | Default horizon | Notes |
|---|---|---|
| Sanctions designations / list status (OFAC SDN, EU consolidated, OFSI, UN, BIS Entity List) | **30 days**, and always at the point of operational decision | Lists change continuously. For any operational decision, re-verify same-day against the relevant primary list, regardless of horizon. |
| Export-controls scope (BIS, EU dual-use, common high-priority items list) | **90 days** | Re-verify on any new joint statement or coordinated action. |
| AML / FATF / EAG mutual-evaluation findings | **12 months** for the report itself, **3 months** for follow-ups and re-ratings | The MER framework is structural; follow-ups change ratings. |
| Regulator and central-bank guidance | **6 months** | Sooner if a known reform cycle is in progress. |
| Customs and statistics (HS-code volumes, mirror data) | **3 months** | Quarterly cycles dominate. |
| Port / rail / corridor capacity and throughput | **3 months** | Operational metrics shift quickly. |
| IFI corridor and country studies (World Bank, EBRD, ADB, IMF) | **24 months** for structural findings, **6 months** for prescriptive figures | Investment-needed and capacity targets re-baselined regularly. |
| Court records and enforcement actions | **3 months** for active matters, **24 months** for closed ones | Status changes via appeals, settlements and follow-ups. |
| Company registry / BO data | **3 months** | Filing cycles and ownership changes. |
| Tier 2 reporting (media, think-tanks) | Take freshness from the underlying primary source it is reporting on | Tier 2 inherits the horizon of the primary it cites. |

**Stale-source handling:**

- A claim grounded in a source past its horizon should be labeled `Plausible` or `Unknown` (not `Verified`) until re-verification.
- For sanctions, AML, export-controls and licensing claims, do not rely on a stale source for an operational decision under any circumstances; re-verify against the current primary list at the point of use.
- When refreshing a memo, update the retrieval date and either confirm the prior conclusions hold or revise them. Do not silently re-date a memo without re-checking.

These horizons are working defaults, not legal or regulatory standards. Adjust upward (more conservative) for higher-stakes work.

## Source-handling rules

- Prefer primary over secondary for any factual claim with operational or compliance consequences.
- State the source class behind each non-trivial fact when working in evidence-backed mode.
- If sources conflict, state the conflict and explain which source carries more weight for the user's objective.
- Treat list-status, licensing and enforcement claims as **time-sensitive** — re-verify against official sources at the time of decision.
- If no source is retrieved, label the output as `illustrative / reasoning-only` and do not assert factual conclusions about specific entities.
