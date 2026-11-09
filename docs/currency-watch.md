# Currency watch — Central Asia + Caspian

An **active reminder** of fast-moving topics in the region that any source-backed memo should re-verify against current primary sources before relying on. This is **not** a database of current facts. The skill does not retrieve sources. Treat entries below as the list of *what to check now*, not as confirmed status.

**Topic catalogue reviewed:** 2026-11-09
**Primary-source status:** verified at check for the EU sanctions-package, FATF/EAG status, Middle Corridor (TITR), and A7A5 / Kyrgyz VASP-cleanup topics, plus the UK list migration documented below; all other topics remain unverified.
**Previous catalogue review:** 2026-09-30
**Staleness rule:** any entry older than **90 days** must be re-verified before use. A stale watch list is worse than no watch list — it looks current while being wrong.

---

## UK source migration

The OFSI Consolidated List stopped receiving updates on 2026-01-28. Use the
[UK Sanctions List](https://www.gov.uk/government/publications/the-uk-sanctions-list)
for current designations, and OFSI guidance for financial-sanctions interpretation.
The [official migration notice](https://www.gov.uk/guidance/moving-to-a-single-list-for-uk-sanctions-designations-28-january-2026)
was checked on 2026-09-30. This confirms the source migration only; no entity status
or other topic in this catalogue has been re-verified.

## How to use this file

1. Before writing a `live-source-backed` or `user-provided sources` memo, scan the topics below to see which ones touch the memo's scope.
2. For each touched topic, **re-verify against current primary sources** (per `docs/source-guide.md` source classes and freshness horizons).
3. If verification is not performed in the current session, label every claim derived from that topic with `[verify]` and retain `user-provided sources` or `illustrative source packet` when they describe the input; otherwise use `reasoning-only`. `mixed` is a legacy transport value, not a memo evidence mode.
4. Update `Topic catalogue reviewed` for catalogue maintenance. Update a topic's `Last reviewed` only after its primary-source checks; do not re-date unverified topics.

## How to maintain this file

- Add a topic when it becomes a recurring source of factual drift in memos.
- Remove a topic when it has stabilized (no material change for at least two horizons) or when it has resolved.
- Do **not** record specific designations, dates, or numerical facts in this file. Those belong in memos with citation. This file records **what to watch**, not **what is currently true**.

---

## Sanctions, export controls, and financial-crime regime

### Topic: OFAC Russia / Iran secondary sanctions and CHPI list evolution
- **Why it matters:** Touches almost every Central Asia + Caspian corridor analysis, banking exposure, and dual-use trade question. Secondary sanctions risk is the dominant exposure driver for many memos in this region.
- **What to re-verify:** Current SDN status of named counterparties; current CHPI (Common High Priority Items) list scope; any new General Licenses or Determinations affecting Russia or Iran energy / financial sectors.
- **Where to verify:** OFAC SDN search; OFAC recent actions; State / Treasury joint statements; relevant General Licenses.
- **Freshness horizon for derived claims:** 30 days, and always at point of operational decision.
- **Last reviewed:** Not yet verified — topic added 2026-05-15. Re-verify against primary sources before deriving claims.

### Topic: A7A5 network status and Kyrgyz VASP-sector cleanup
- **Why it matters:** The A7A5 ruble-stablecoin network (Kyrgyz-issued, designated by the US, UK and EU) largely collapsed over 2026, and Kyrgyzstan is running a public cleanup of its VASP sector (license revocations, compulsory liquidations, account closures, draft screening decree). Memos that still treat Kyrgyzstan as a permissive host — or that treat the network as dead rather than migrated — are both wrong in opposite directions.
- **What to re-verify:** Current designation status of network entities and any successor venues; progress and scope of the Kyrgyz cleanup (whether it reaches bona fide VASPs); the presidential VASP-screening decree's final text; movement of the parked token supply; the issuer's replacement payment services; analytics-firm updates on genuine vs circular volume.
- **Where to verify:** OFAC SDN / recent actions; Council of the EU package press releases; UK Sanctions List; Kyrgyz Finnadzor and Cabinet announcements; EAG; blockchain-analytics firm publications (Elliptic, TRM Labs, Crystal, Chainalysis) cross-checked against each other.
- **Freshness horizon for derived claims:** 30 days, and always at point of operational decision.
- **Last reviewed:** 2026-11-09 — verified against OFAC, Council of the EU (19th/21st/22nd packages), Kyrgyz Finnadzor (15 July 2026 license revocation), FATF October 2026 plenary, and two independent analytics firms; see `examples/live-source-backed-a7a5-collapse-kg-cleanup.md` for the dated source set. The issuer-vs-analytics volume dispute is unresolved — label it, don't pick a number.

### Topic: EU sanctions package evolution
- **Why it matters:** EU packages introduce new designations, expanded sectoral measures, and new circumvention-focused provisions on a recurring basis. Memos that cite "the latest EU package" without re-verification drift quickly.
- **What to re-verify:** Most recent package number and Council decision date; consolidated list status of named counterparties; sectoral scope changes affecting energy, finance, dual-use; measures aimed at third-country banks, crypto platforms and circumvention enablers in Central Asia / the Caspian.
- **Where to verify:** EU consolidated sanctions list; EU Official Journal Council decisions; Council of the EU package press releases and package timeline.
- **Freshness horizon for derived claims:** 30 days.
- **Last reviewed:** 2026-11-09 — checked against Council of the EU press releases and package timeline; the 22nd package (October 2026) was the latest adopted at check, and the 21st (July 2026) added a first-ever full third-country crypto-service ban instrument plus transaction bans touching Kyrgyz banks and platforms. Re-verify before citing "the latest package" — packages now land several times per year.

### Topic: UK OFSI and other allied regimes
- **Why it matters:** UK, CH, JP, CA, AU regimes diverge from US/EU on specific designations. Memos for users with multi-jurisdictional exposure must not assume convergence.
- **What to re-verify:** Current consolidated list status in each relevant jurisdiction.
- **Where to verify:** UK Sanctions List; SECO; Japan METI; relevant national lists.
- **Freshness horizon for derived claims:** 30 days.
- **Last reviewed:** Not yet verified — topic added 2026-05-15. Re-verify against primary sources before deriving claims.

### Topic: FATF / EAG / MONEYVAL country status
- **Why it matters:** Greylist / blacklist status affects correspondent banking de-risking, EU AML high-risk third-country listings, and EDD requirements. Status changes via plenary cycles.
- **What to re-verify:** Current FATF public statement; latest MER or follow-up rating for in-scope countries (KZ, UZ, TM, KG, TJ, AZ); EAG plenary outcomes; whether the accelerated virtual-asset follow-up process targets any in-scope jurisdiction.
- **Where to verify:** FATF country pages and plenary outcomes; EAG plenary statements; MONEYVAL reports.
- **Freshness horizon for derived claims:** 3 months for follow-ups, 12 months for MER findings.
- **Last reviewed:** 2026-11-09 — checked against the FATF October 2026 plenary outcomes and the 30 October 2026 increased-monitoring list: no Central Asian or Caspian jurisdiction is on the grey list at check; the plenary launched an accelerated VA-standards follow-up targeting jurisdictions with materially important VA activity, with results due June and October 2027.

## Banking and payment rails

### Topic: Correspondent banking de-risking posture toward regional banks
- **Why it matters:** USD and EUR clearing access for KZ / UZ / KG / TJ / AZ banks shifts with each major US/EU enforcement action and with shifts in correspondent appetite. Memos that assume stable correspondent access can be wrong within months.
- **What to re-verify:** Recent enforcement actions against correspondents serving the region; named-bank-level correspondent posture changes; central bank statements on USD/EUR clearing access.
- **Where to verify:** OFAC and DOJ enforcement actions; central bank communiqués; credible secondary reporting cross-checked with primaries.
- **Freshness horizon for derived claims:** 6 months for structural posture; immediately for any named-bank claim.
- **Last reviewed:** Not yet verified — topic added 2026-05-15. Re-verify against primary sources before deriving claims.

### Topic: National central-bank macroprudential and AML rules
- **Why it matters:** Reporting thresholds, BO disclosure requirements, and FX controls update on national cycles, often without clear English-language announcement.
- **What to re-verify:** Latest National Bank statements for each in-scope country; AML/CFT rule amendments; FX restriction changes.
- **Where to verify:** National central bank press releases; financial-monitoring agencies; FATF country updates.
- **Freshness horizon for derived claims:** 6 months.
- **Last reviewed:** Not yet verified — topic added 2026-05-15. Re-verify against primary sources before deriving claims.

## Corridor and logistics

### Topic: Middle Corridor (TITR) capacity, throughput, and bottlenecks
- **Why it matters:** Volumes, transit times, and Caspian shipping capacity move with each season, each infrastructure project completion, and each Russia-route diversion event. Quantitative claims (volumes, days, cost) decay fast.
- **What to re-verify:** Latest TITR coordinating-body statements; port throughput data (Aktau, Kuryk, Baku/Alat, Turkmenbashi); rail operator disclosures (KTZ, ADY); recent IFI corridor studies (World Bank, EBRD, ADB).
- **Where to verify:** TITR press releases; port authority statistics; rail operator publications; IFI corridor publications.
- **Freshness horizon for derived claims:** 3 months for operational metrics; 12 months for structural findings.
- **Last reviewed:** 2026-11-09 — checked against the TITR coordinating body (September 2026 working-group statement) and Kazakh transport-ministry reporting: 2026 volumes were tracking close to plan at check, but national plan figures and operator-reported numbers differ by scope and definition — treat any single published tonnage as definition-bound and cite its source. Quantitative claims remain on the 3-month horizon.

### Topic: Russia-route disruption and re-routing dynamics
- **Why it matters:** Northern Corridor disruptions, rail-network changes, and sanctions-driven re-routing reshape Caspian and Caucasus flows. Memos relying on year-old routing assumptions are unreliable.
- **What to re-verify:** Recent freight diversion volumes; specific carrier exit / entry events; cross-border bottleneck developments.
- **Where to verify:** Sector trade-press cross-checked against carrier disclosures and statistics.
- **Freshness horizon for derived claims:** 3 months.
- **Last reviewed:** Not yet verified — topic added 2026-05-15. Re-verify against primary sources before deriving claims.

## Energy and infrastructure

### Topic: CPC, BTC, and Caspian export routes
- **Why it matters:** Throughput, force-majeure events, capacity expansions, and ownership-structure changes affect both physical flow and counterparty-risk analysis.
- **What to re-verify:** Operator disclosures on throughput, incidents, and capacity; ministry-of-energy announcements; IEA / OPEC context where material.
- **Where to verify:** CPC, BTC, and operator publications; relevant ministry pages; IEA, OPEC.
- **Freshness horizon for derived claims:** 3 months for throughput; 6 months for structural changes.
- **Last reviewed:** Not yet verified — topic added 2026-05-15. Re-verify against primary sources before deriving claims.

### Topic: Caspian gas export developments (Galkynysh, Trans-Caspian discussions)
- **Why it matters:** Long-running file with periodic activations and stalls. Memos must not present multi-year discussion items as imminent without re-verification.
- **What to re-verify:** Latest official statements from TM, AZ, EU on Trans-Caspian; project-level announcements.
- **Where to verify:** Ministry pages; EU Commission energy statements; credible secondary cross-checked against primaries.
- **Freshness horizon for derived claims:** 6 months.
- **Last reviewed:** Not yet verified — topic added 2026-05-15. Re-verify against primary sources before deriving claims.

## Geopolitical and security

### Topic: Russia-China-Iran junction dynamics and regional alignment
- **Why it matters:** Diplomatic statements, joint exercises, summit communiqués, and SCO-level developments affect leverage analysis and risk transmission channels. Snapshot claims age quickly.
- **What to re-verify:** Latest SCO / CIS / CSTO statements; bilateral summit communiqués; specific joint announcements (energy, security, payment infrastructure).
- **Where to verify:** Official communiqué texts; ministry press releases.
- **Freshness horizon for derived claims:** 6 months for structural framing; 3 months for specific commitments.
- **Last reviewed:** Not yet verified — topic added 2026-05-15. Re-verify against primary sources before deriving claims.

### Topic: Afghan border and Tajik / Uzbek security dynamics
- **Why it matters:** Border-security events, trade-flow changes, and refugee or counter-terrorism developments affect logistics, banking exposure, and political risk.
- **What to re-verify:** Recent border-incident reporting; bilateral trade and security agreements.
- **Where to verify:** Government communiqués; credible reporting cross-checked.
- **Freshness horizon for derived claims:** 3 months.
- **Last reviewed:** Not yet verified — topic added 2026-05-15. Re-verify against primary sources before deriving claims.

---

## What this file is not

- Not a database of current sanctions designations, prices, throughput numbers, or designation dates. Those belong in memos with citation.
- Not a substitute for `docs/source-guide.md`, which classifies source tiers and lists freshness horizons by claim type.
- Not legal, sanctions, AML, or operational advice. The skill does not perform sanctions screening or live retrieval by itself.
