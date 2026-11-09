# Live-source-backed example — A7A5 network collapse and the Kyrgyz VASP-sector cleanup (2026)

> **Evidence mode: `live-source-backed`.**
>
> **Retrieval date: 2026-11-09.** All factual claims below are grounded in publicly retrievable primary or secondary sources cited inline, retrieved on this date. Sources are time-sensitive — designations, license status, on-chain metrics and regulator actions change. Re-verify against current authoritative sources before any operational use.
>
> Human review required; this example is not a compliance determination.

## User question

> "We are a European commercial bank providing EUR correspondent services to two Kyrgyz banks, and we are considering onboarding a Kyrgyz-licensed virtual-asset exchange as a client. The A7A5 stablecoin network was built on Kyrgyz jurisdiction, was sanctioned by the US, UK and EU, and has now largely collapsed, while the Kyrgyz authorities are publicly cleaning up the sector. What does this change for our exposure, and what should we watch next?"

## Bottom line

The A7A5 ruble stablecoin network is no longer functioning at anywhere near its claimed scale: US, UK and EU designations made the token's conversion venues radioactive [S1, S2, S3], its dominant exchange Grinex failed in April 2026 and lost its Kyrgyz license on 15 July 2026 [S5, S8], average daily volumes fell about 96% from the July 2025 peak [S8], and genuine human-scale activity is a small fraction of gross on-chain volume [S9]. Kyrgyzstan has moved from permissive host to active cleanup: license revocations, compulsory liquidations, mass account closures at state banks, and a draft presidential decree imposing sanctions-list screening on VASPs, as stated by the President's Special Representative for sanctions policy on 27 October 2026 [S12]. `[primary]`/`[secondary]` as tagged per claim.

`[analyst-judgment]`: for a European correspondent bank, the collapse does not retire the risk — it relocates it. The exposure shifts from "is our counterparty touching A7A5" to successor-venue migration, parked-supply redemption claims, and the question of whether the Kyrgyz cleanup reaches bona fide institutions or only the designated network. The FATF October 2026 plenary's decision to accelerate virtual-asset standards implementation in jurisdictions with materially important VA activity raises the odds of formal external scrutiny of the sector [S6].

## Primary risk driver

`Primary driver is:` the migration of a sanctioned, concentrated and now-collapsed crypto settlement network into successor infrastructure, under a Kyrgyz regulatory cleanup whose scope and evenhandedness are still unproven — transmitted into a European bank's books through correspondent relationships with Kyrgyz banks and any direct VASP client onboarding.

## Risk transmission mechanism

1. **The A7A5 network was designated across jurisdictions in 2025.** OFAC designated the exchange Grinex, the Kyrgyz issuer Old Vector, and A7 LLC with its subsidiaries on 14 August 2025, describing Grinex as Garantex's successor and A7A5 as the token used to compensate Garantex users [S1]. The EU's 19th package (23 October 2025) sanctioned the developer of A7A5, its Kyrgyz issuer and the operator of a platform trading significant A7A5 volumes, and prohibited transactions involving the stablecoin across the EU [S2]. `[primary]` [S1, S2].

2. **Sanctions bit at the conversion boundary, not the smart contract.** From late September 2025, users reported USDT obtained by swapping A7A5 being frozen or flagged at mainstream exchanges, and Uniswap removed A7A5 from its interface in November 2025 [S8]. `[secondary]` [S8]. The mechanism — analytics-driven detection of indirect exposure — is the reason designations without control over the smart contract still collapsed the token's usable market `[inference]` from [S8].

3. **The liquidity concentration failed.** By late 2025 most A7A5 trading ran through Grinex; on or around 16 April 2026 Grinex announced a breach losing more than 1 billion rubles (about $13–15 million) and suspended operations [S8]. Whether the "hack" was genuine or an exit scam is `Unknown` — both explanations were reported [S8]. On 15 July 2026 the Kyrgyz Financial Supervisory Service (Finnadzor) revoked Grinex LLC's virtual-asset exchange and trading-operator license (series ВА № 0183) for violations of the Law on Virtual Assets [S5]. `[primary]` [S5]; `[secondary]` [S8].

4. **Measured activity collapsed.** Average daily transaction volumes fell to a $24.3 million low in June 2026, down 96% from the July 2025 peak, with no new issuance since July 2025 [S8]. Over 99% of the ~$470 million supply sits in four wallets; after netting out operator churn and wash trading, roughly 19 cents per dollar of remaining volume resembles genuine activity — about $6 million a month of human-scale flows, roughly 1.3% of supply [S9]. `[secondary]` [S8, S9]. These are commercial analytics firms' measurements; treat exact figures as estimates with methodology risk, cross-checked across two independent firms here.

5. **The scale dispute is unresolved and instructive.** The issuer claimed ~$205 million average daily volume and $34.4 billion processed between 1 January and 17 June 2026; TRM Labs put average daily volume near $75 million with about 34% circular movement; Elliptic reported volumes down over 90% since January 2026 [S10]. CoinDesk explicitly did not independently verify either side [S10]. `[secondary]` [S10]. Compliance teams quoting any of these numbers should label the dispute rather than pick one `[analyst-judgment]`.

6. **The October 2026 shock showed infrastructure dependence.** After Ukrainian drone strikes on a Yandex data center in Sasovo on the night of 7–8 October 2026, A7A5 transfers fell from about 600 per day to 14–18 per 24 hours; users reported suspended services, interest unpaid since 9 October, and promissory notes redeemable only for rubles at the A7-Finance office [S11]. `[secondary]` [S11], reporting Elliptic's analysis. The hosting arrangement (the issuer's exchange hosted by Yandex since September 2025) is `[secondary]` [S11].

7. **Kyrgyzstan is publicly cleaning up.** As of 20 October 2026, 52 legal entities had ceased operations and 57 more were in compulsory liquidation as part of sanctions-risk mitigation; state-owned banks closed more than 240 accounts; Finnadzor revoked licenses of a number of market participants; and a draft presidential decree would require VASP screening against UN, EU, UK and US lists, with a unified digital licensing and oversight platform for VASPs in development — per the official statement by the President's Special Representative for sanctions policy, Bakyt Sydykov, reported 27 October 2026 [S12]. `[secondary]` [S12], reporting an official statement; the underlying decree and liquidation lists were not independently retrieved. `[verify]`.

8. **The EU pressure channel is widening.** The 21st package (23 July 2026) introduced a transaction ban against a Kyrgyz bank connected with SPFS plus three other non-Russian banks, added 4 designations linked to the A7 network including its new Africa links, extended the transaction ban to 14 crypto-related service platforms based in Georgia, Panama, the UAE, the Marshall Islands, Kyrgyzstan and Belarus, and created a first-ever instrument allowing a full third-country ban for crypto-asset services [S3]. The 22nd package (12 October 2026) added 1,569 listings focused on the military-industrial complex [S4]. `[primary]` [S3, S4].

9. **FATF is accelerating virtual-asset supervision.** The October 2026 plenary agreed to significantly accelerate implementation of the FATF Standards on virtual assets in jurisdictions with materially important VA activity, with a targeted review whose results are due in June and October 2027 [S6]. As of 30 October 2026, no Central Asian or Caspian jurisdiction appears on the FATF increased-monitoring list [S7]. `[primary]` [S6, S7].

10. **Demand is migrating, not disappearing.** A7 launched a service taking USDT from businesses and paying their suppliers via ordinary SWIFT transfers, which Elliptic's Tom Robinson assesses could supply USDT liquidity for the struggling stablecoin [S11]. Russia's new cryptoasset law, permitting crypto use in foreign trade from 1 September 2026, points to a state-supervised successor rail [S8]. `[secondary]` [S8, S11]. The form of the successor infrastructure and its host jurisdictions are `Unknown` `[verify]`.

## Exposure map

| Channel | Exposure | Source |
|---|---|---|
| Correspondent accounts of Kyrgyz banks | Indirect exposure to A7-network flows transiting Kyrgyz banking infrastructure; EU transaction ban already hit one SPFS-connected Kyrgyz bank | [S3] `[primary]` |
| VASP client onboarding | Kyrgyz license is no longer a safe-harbor signal: the regulator is revoking licenses and liquidating entities; today's licensee can be tomorrow's liquidation | [S5, S12] `[primary]`/`[secondary]` |
| Indirect crypto exposure | USDT or other assets with upstream A7A5 hops arriving at the bank's VASP or fintech clients trigger freezing/flagging at mainstream venues | [S8] `[secondary]` |
| Successor-venue risk | Exposure migrates to new wallets, wrapped tokens and new conversion routes; static address screening misses infrastructure that has migrated rather than disappeared | [S9] `[secondary]` |
| Parked supply | ~$455–482 million market cap with 14–18 transfers/day is dormant, not resolved; redemption claims against the issuer could surface in litigation or enforcement | [S9, S11] `[secondary]` |
| Reputational / policy | FATF accelerated VA review could put the Kyrgyz VASP sector under formal external monitoring by 2027 | [S6] `[primary]` |

## Actor incentives

- **Kyrgyz authorities**: protect the banking sector's correspondent access and the jurisdiction's standing with the EU/UK/US; the cleanup is run at presidential level with explicit readiness to exchange information with Western partners [S12]. `[secondary]`, reporting an official statement. Incentive to show visible enforcement without collapsing the legitimate VASP sector `[analyst-judgment]`.
- **A7 / Old Vector network**: preserve the yield-bearing parked supply at minimal cost, rebuild USDT liquidity through the new SWIFT-fronted service, and rotate infrastructure away from designated addresses [S9, S11]. `[secondary]`.
- **EU / US / UK**: coordinate designations so activity cannot re-route to a single permissive jurisdiction; the EU's new third-country crypto-service ban instrument creates escalation capacity [S3]. `[primary]`.
- **European correspondent banks**: avoid being the residual EUR rail for flows that Western venues have already flagged; a single traced exposure can trigger category-level de-risking of Kyrgyz counterparties `[analyst-judgment]`.
- **Legitimate Kyrgyz VASPs and banks**: demonstrate distance from the A7 network; they bear the cost of the cleanup through EDD, account closures and reporting duties [S12] `[secondary]`.

## Role-based implications

### European correspondent bank — compliance leadership

1. **Screen for migrated infrastructure, not just known addresses.** Update monitoring from static designated-address lists to behavioral continuity indicators: funding from previously attributed wallets, coordinated wallet creation, rapid balance sweeps, common gas funding, identical timing — per the analytics-firm guidance in [S9]. `[secondary]`.
2. **Re-run EDD on Kyrgyz bank counterparties against the cleanup.** Ask each Kyrgyz correspondent what the 52 closures, 57 liquidations and 240+ account closures [S12] touched in their own books, and what their regulator reporting now covers. `[verify]` — the liquidation lists were not independently retrieved in this session.
3. **Treat any A7A5-adjacent flow as a stop-and-review, not a clearance question.** No exposure to A7A5 can be cleared by absence from a list; the network's wallet rotation makes list-matching insufficient on its own [S9].
4. **Do not onboard a Kyrgyz VASP on the strength of its license alone.** Require evidence of distance from the A7 network (ownership, funding chain, venue relationships), and check the entity and its beneficial owners against current OFAC SDN, EU consolidated and UK Sanctions List entries on the day of decision. `[verify]`.

All actions are illustrative. Real implementation requires qualified compliance, legal and AML counsel.

### Kyrgyz bank or VASP — survival posture

- Document the entity's independence from A7/A7A5/Old Vector/Grinex: funding sources, wallet history, venue relationships, beneficial owners [S1, S9].
- Prepare for monthly regulator reporting on closed accounts, blocked payments and refusals [S12] `[secondary]`.
- Track the draft presidential decree and the unified VASP oversight platform; early alignment is cheaper than retroactive compliance [S12]. `[verify]` the decree's final text when adopted.

### Fintech with regional payment flows

- Map any stablecoin settlement touching rubles or Kyrgyz venues against the four exposure classes (direct holding, immediate conversion, cluster, indirect) in [S9] and price the operational cost of a freeze at a mainstream exchange.

## Trigger points

1. **The presidential decree on VASP sanctions screening is signed** (draft reported 27 October 2026 [S12]) — would formalize UN/EU/UK/US list screening and liability for Kyrgyz market participants. `[verify]`.
2. **A successor venue absorbs A7A5 liquidity.** Watch for a new exchange or OTC structure taking over Grinex's role; the signal is funding-chain continuity from designated infrastructure, not the new venue's clean history [S9].
3. **The EU applies the new third-country crypto-service ban** created in the 21st package [S3] — would escalate from entity-level to jurisdiction-level restriction.
4. **FATF's targeted VA review names Kyrgyzstan or regional peers** — results due June and October 2027 [S6].
5. **Movement of the parked supply.** Over 99% of supply sits in four wallets [S9]; any sweep out of the operator vault created on 18 May 2026 is an early warning of relaunch or liquidation.
6. **A7's USDT-to-SWIFT service scales** [S11] — would rebuild the dollar leg of the network outside crypto venues.
7. **EAG follow-up on Kyrgyzstan's mutual evaluation** — a downgraded or upgraded supervisory baseline changes the correspondent calculus. `[verify]` against current EAG publications.

## Unknowns

- **Whether the April 2026 Grinex breach was a genuine hack or an exit scam.** Reported both ways [S8]; unresolved.
- **The scope of the cleanup.** The 52 ceased entities, 57 liquidations and 240+ closed accounts are from an official statement as reported [S12]; the underlying lists were not independently retrieved, and whether bona fide market participants are swept in is `Unknown`. `[verify]`.
- **Genuine usage level.** Issuer, TRM Labs and Elliptic figures conflict materially [S10]; no independent verification exists.
- **Where successor infrastructure will domicile.** The A7 network already has Africa links designated in the 21st package [S3]; the next host jurisdiction is `Unknown`.
- **Fate of the parked supply and redemption claims** against Old Vector under Kyrgyz law. `Unknown`.
- **Current list status of any specific counterparty.** Not assessed in this memo. `[verify]` same-day against the primary lists before any operational decision.

## Confidence

`Confidence`: Moderate. The collapse of the A7A5 network and the fact of the Kyrgyz cleanup are `Verified`-grade findings grounded in primary regulator and sanctions sources [S1, S2, S3, S5, S6, S7] and two independent analytics firms [S8, S9]. Quantitative usage figures carry methodology risk and an unresolved issuer dispute [S10]. The forward path of successor infrastructure, the evenhandedness of the cleanup, and any specific counterparty's status are `Unknown` or `[analyst-judgment]` and must be re-verified before acting.

## What would change the judgment

- Signed presidential decree with screening obligations weaker or stronger than reported [S12].
- FATF targeted VA review naming (or pointedly not naming) Kyrgyzstan in June 2027 [S6].
- A successor venue demonstrating genuine non-Russian, non-circular volume — the current on-chain record shows Moscow-timezone, operator-dominated activity [S9].
- Kyrgyz authorities publishing liquidation lists that distinguish A7-affiliated entities from unrelated VASPs.
- Renewed A7A5 issuance (none since July 2025 [S8]) or a sweep from the operator vault [S9].
- EU activation of the third-country crypto-service ban against Kyrgyzstan [S3].

---

This memo is `live-source-backed` as of the retrieval date stated above. Sources are time-sensitive: designations, license status, on-chain metrics and regulator statements change. This memo does not screen any specific entity, wallet address, beneficial owner or financial institution against any sanctions, export-control or watchlist. It does not verify any factual claim about ownership, control, end-use or enforcement of any specific party. Any operational decision — including VASP onboarding or correspondent offboarding — requires source-backed re-verification at the time of decision and qualified professional review.

`Author: Vassiliy Lakhonin`

## Sources

### Tier 1 — primary

- **[S1]** US Department of the Treasury, OFAC — "Treasury Sanctions Cryptocurrency Exchange and Network Enabling Sanctions Evasion and Cyber Criminals", 14 August 2025 (designations of Grinex, Old Vector, A7 LLC, A71, A7 Agent and associated parties). https://home.treasury.gov/news/press-releases/sb0225
- **[S2]** Council of the EU — "19th package of sanctions against Russia: EU targets Russian energy, third-country banks and crypto providers", 23 October 2025 (A7A5 developer, Kyrgyz issuer and platform operator sanctioned; A7A5 transactions prohibited across the EU). https://www.consilium.europa.eu/en/press/press-releases/2025/10/23/19th-package-of-sanctions-against-russia-eu-targets-russian-energy-third-country-banks-and-crypto-providers/
- **[S3]** Council of the EU — "21st package of sanctions: EU hits Russian energy, financial services and crypto hard", 23 July 2026 (transaction ban on a Kyrgyz SPFS-connected bank; 4 A7-network designations incl. Africa links; transaction ban on 14 crypto platforms incl. Kyrgyzstan-based; new full third-country crypto-service ban instrument; dual-use export listings incl. entities in Kazakhstan and Kyrgyzstan). https://www.consilium.europa.eu/en/press/press-releases/2026/07/23/21st-package-of-sanctions-eu-hits-russian-energy-financial-services-and-crypto-hard/
- **[S4]** Council of the EU — "Timeline: packages of sanctions against Russia since February 2022" (22nd package of 12 October 2026: 1,569 listings; 20th package of 23 April 2026: RUBx transaction ban and Russian crypto-platform ban). Retrieved 2026-11-09. https://www.consilium.europa.eu/en/policies/sanctions-against-russia/timeline-packages-sanctions-since-february-2022/
- **[S5]** Financial Supervisory Service under the Ministry of Economy and Commerce of the Kyrgyz Republic (Finnadzor) — revocation of the virtual-asset exchange and trading-operator license of Grinex LLC (series ВА № 0183), 15 July 2026 (in Russian). https://fsa.gov.kg/2026/07/15/финнадзором-отозваны-ранее-выданны/
- **[S6]** FATF — "Outcomes FATF Plenary, 28–30 October 2026" (accelerated implementation of FATF Standards on virtual assets in jurisdictions with materially important VA activity; targeted review results due June and October 2027; Bulgaria, Côte d'Ivoire, DRC and Monaco removed from increased monitoring). https://www.fatf-gafi.org/en/publications/Fatfgeneral/outcomes-fatf-plenary-october-2026.html
- **[S7]** FATF — "Jurisdictions under Increased Monitoring — 30 October 2026" (full grey list; no Central Asian or Caspian jurisdiction listed). https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-october-2026.html

### Tier 2 — specialist blockchain analytics (originators of the on-chain measurements cited)

- **[S8]** Elliptic — "The fall of A7A5: how sanctions strangled the ruble stablecoin", 29 July 2026 ($102bn cumulative over ~251k transactions; daily volumes down 96% from the July 2025 peak to a $24.3m low in June 2026; no issuance since July 2025; Grinex April 2026 breach; Uniswap delisting November 2025; Russia crypto law effective 1 September 2026). https://www.elliptic.co/insights/the-fall-of-a7a5-how-sanctions-strangled-the-ruble-stablecoin/
- **[S9]** Crystal Intelligence — "What the A7A5 stablecoin did after Grinex collapsed", 21 August 2026 (~$470m supply, >99% in four wallets; ~19% genuine activity; one address 46% of lifetime trading volume; ~250 human-scale addresses; ~$6m/month genuine flows; Moscow-timezone activity pattern; migrated-infrastructure screening guidance). https://crystalintelligence.com/thought-leadership/a7a5-stablecoin-parked-not-gone/

### Tier 2 — media (reporting primary actors or analytics firms)

- **[S10]** CoinDesk — "This sanctioned Russian stablecoin claims it processes billions, but blockchain analysts disagree", 3 July 2026 (issuer claim of ~$205m average daily volume and $34.4bn processed 1 Jan–17 Jun 2026; TRM Labs estimate ~$75m/day with ~34% circular; Elliptic: down >90% since January 2026; CoinDesk did not independently verify either side). https://www.coindesk.com/business/2026/07/03/this-sanctioned-russian-stablecoin-claims-it-processes-billions-but-blockchain-analysts-disagree
- **[S11]** Bitcoin.com News — "Ukraine's 'kinetic sanctions' disrupt Russian A7A5 stablecoin services: Elliptic", 14 October 2026 (7–8 October drone strikes on the Yandex Sasovo data center; transfers from ~600/day to 14–18 per 24h; services suspended; interest unpaid since 9 October; promissory notes redeemable only in rubles at the A7-Finance office; A7's USDT-to-SWIFT service). https://news.bitcoin.com/stablecoins/ukraine-kinetic-sanctions-disrupt-russian-a7a5-stablecoin-elliptic/
- **[S12]** Akchabar (Bishkek) — "In Kyrgyzstan, measures are being taken against companies associated with the A7 and A7A5 networks", 27 October 2026, reporting the official statement of Bakyt Sydykov, the President's Special Representative for sanctions policy (52 legal entities ceased operations as of 20 October; 57 in compulsory liquidation; 240+ accounts closed at state-owned banks; draft presidential decree on UN/EU/UK/US list screening; unified VASP licensing and oversight platform; monthly bank reporting; readiness to cooperate with the EU, UK and US). https://www.akchabar.kg/en/news/v-kirgizstane-prinimayu-meri-v-otnoshenii-kompanij-svyazannikh-s-setyu-a7-i-a7a5-rnkewsldgckpyacs

### Source-tier note

Designation, license-revocation, EU-package and FATF claims are anchored to primary sources ([S1]–[S7]). On-chain measurements come from two independent commercial analytics firms ([S8], [S9]) whose figures are consistent with each other and are treated as estimates, not audited data; the issuer's conflicting claims are reported and flagged, not adopted ([S10]). The Kyrgyz cleanup scope is from an official statement as reported by national media ([S12]) and is marked `[verify]` pending independent retrieval of the decree and liquidation lists. This memo states no current list status for any specific counterparty — re-verify against OFAC SDN, the EU consolidated list and the UK Sanctions List at the point of use.
