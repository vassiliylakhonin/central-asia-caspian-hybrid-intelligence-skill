# Common failure modes

These are recurring failure modes for Central Asia / Caspian outputs. Treat each as a thing to actively avoid; if you spot one in a draft, revise the memo.

## Reasoning failures

- **Generic geopolitical essay.** Broad regional narration with no concrete risk, decision or actor.
- **Alarmism without a transmission channel.** Strong language about risk without explaining how it actually transmits to the user.
- **Implication before mechanism.** Stating consequences before explaining how the mechanism produces them.
- **No actor incentives.** Risks asserted without identifying who gains, who loses, and why.
- **No ownership or counterparty logic.** Sanctions / AML discussion that ignores beneficial ownership, control tests and counterparty structure.
- **No banking or payment channel.** Sanctions or compliance reasoning that does not engage with correspondent rails, scheme participation, or settlement.
- **No trigger points.** Static risk picture with no events or indicators that would update it.
- **No unknowns.** Confident answer that does not acknowledge what would change the judgment.
- **Single-hypothesis lock-in.** For attribution or causation questions (whose evasion design is this, what is driving this routing, who benefits), committing to one explanation early and marshaling only confirming evidence, never building or seriously testing rivals. Fix: build competing hypotheses and rank by disconfirmation, not by confirming evidence — confirmation of a favored explanation is weak; failure to disconfirm rivals is the load-bearing step.
- **False-premise acceptance.** Analyzing the consequences of a premise asserted in the question — a designation, ownership link, enforcement action, or routing fact treated as settled — without confirming the premise itself. Fix: name the premise, tag `[verify]`, and Stop-and-request or Flag-but-don't-use before the dependent read (see the false-premise hard stop in [`../AGENTS.md`](../AGENTS.md) "Stop and request — explicit triggers").

## Evidence failures

- **Fake sanctions certainty.** Claiming a person, entity, vessel or jurisdiction is or is not sanctioned without retrieving and citing the actual list.
- **Fake source claims.** Citing URLs, list IDs, case numbers or report titles that the model invented.
- **Unsupported legal/compliance conclusions.** Treating analytical reasoning as a legal or compliance determination.
- **Unsupported numerical precision.** Specific percentages, prices or volumes presented without sourcing.
- **Outdated assumptions.** Asserting current status of laws, designations, leadership, prices or enforcement without verifying against current sources.
- **State-media framing inherited by query language.** Adopting the frame, emphasis, or favorability of state-controlled outlets — and doing so more strongly when the question is asked in the region's dominant state language than in English. Transmission channel: training corpora over-represent state media in those languages, so the model's prior leans toward the official narrative on actor responsibility, sanctions legitimacy, corridor reliability or who-benefits framing, without the user ever supplying that source. The fix is already in the canon: treat state-controlled outlets as `[secondary]` and non-independent (a cluster of state outlets is not corroboration — see the independence test in [`../AGENTS.md`](../AGENTS.md) "Retrieved-content trust"), add `[verify]` to any load-bearing claim that traces back to them, and keep the analytical frame identical regardless of the query's language. If only state-aligned sources support a claim, prefer Flag-but-don't-use over importing their conclusion. Motivated by external research on language-dependent model bias. **Reproduction record:** a blind fresh-context RU/EN A/B (Claude Opus 4.8, 2026-06-12; 8 runs across two probe types — a sanctions-circumvention triage question and a sanctions-legitimacy / "whose interests does this serve" question) did **not** reproduce it. Russian and English outputs converged on the same Western-compliance and multi-vector realpolitik framing, with no favorability shift toward the official narrative; Russian answers even carried English compliance loanwords ("sanctions evasion", "due diligence", "EDD"). Interpretation: in this skill's compliance/corridor domain the regulatory prior appears English-dominant and carries across languages. The guard is retained as precautionary — it may still bite on other models, on the dominant-state-language cases the external research targets, or on contested-attribution questions outside this skill's compliance scope.
- **Citation post-rationalization (tag–source faithfulness).** A claim carries a `[primary]` / `[secondary]` tag, a list ID, a case number, or a URL that looks right, but the cited source does not actually establish the specific claim — the citation was attached after the conclusion was formed. Tag *presence* is not tag *faithfulness*: a correct-looking tag on an unsupported sanctions-status or beneficial-ownership claim manufactures false confidence. Fix: verify that the source supports the specific claim; narrow the claim to what it carries. Motivated by external research on citation faithfulness in attributed generation.
- **Verbalized-confidence miscalibration.** Decisiveness of language not tracking evidence strength — confident framing ("will", "clearly", "is") on `[inference]` / `[analyst-judgment]` claims, or needless hedging on a verified `[primary]` designation. Fix: match hedges to provenance and confidence; state an explicit confidence band where the right level is unclear (see Linguistic faithfulness in [`../AGENTS.md`](../AGENTS.md)). Motivated by external research on faithful uncertainty expression in LLMs.
- **Cross-script name-match false certainty.** Treating a counterparty name match — or non-match — as settled when the name crosses scripts: Kazakh/Russian Cyrillic ↔ Latin transliteration variants, patronymics, name-order differences, inconsistent vendor transliterations. On the largest public sanctions entity-matching benchmark (755k labeled pairs from 293 sources across 31 countries), error analysis found complementary failure modes: rule-based screeners over-match (false positives), while LLMs — even frontier models near 99% F1 overall — fail primarily on cross-script transliteration and minor identifier/date inconsistencies (arXiv:2603.11051). Fix: never treat a single-transliteration screen as clearance and never confirm identity on name similarity alone; anchor identity claims on verifiable identifiers (SDN list ID, registry number, IMO number, BO record) per the Stop-and-request triggers in [`../AGENTS.md`](../AGENTS.md), and state which script variants were actually checked. Motivated by external research on cross-script entity matching. **Reproduction record:** attempted 2026-07-06 (Claude Opus 4.8, 2 fresh-context runs against runtimes/claude/SKILL.md, screening probe with a Latin-only no-match on a Kazakh name) — did **not** reproduce: both runs refused the "cleared" framing AND independently raised Cyrillic/transliteration variants plus identifier-anchored re-screening as named gaps. Guard retained as precautionary for other models and for outputs produced under heavier layout/compression pressure.
- **Table-cell provenance tag drift.** Axis A tags applied in prose paragraphs but dropped, mutated, or bulk-attributed inside markdown table cells — typically in risk register, exposure map, options, indicators or scenario tables. Tables are where the operational claims live; stripping their provenance hides exactly the claims a reviewer most needs to audit. Reproduced 2/2 in fresh-context Hybrid-mode runs against this canon (2026-05-18). Fix per the table-cell discipline rule in [`../AGENTS.md`](../AGENTS.md): every factual cell carries its own Axis A tag; a dedicated Provenance column is acceptable; bulk-attribution footnotes are not a substitute.

## Scope failures

- **Over-expanded geography.** Pulling in Russia, China, EU, US, the Gulf or the South Caucasus without a transmission channel or leverage change.
- **Caspian included when irrelevant.** Adding Caspian framing to a question that does not touch routing, energy, ports or corridor competition.
- **Scope drift into infrastructure.** Drifting into agent-framework, MCP-server, CLI-tooling, or sanctions-screening territory that this skill is not.
- **Duplication of Global Think Tank Analyst.** Producing a generic strategic memo instead of a specialist regional/corridor analysis.

## Safety failures

- **Determinative compliance language.** Phrases like *fully compliant*, *no sanctions risk*, *guaranteed compliant*.
- **Implicit advice posture.** Recommendations phrased as legal, tax or investment advice without disclaimers.
- **Live-screening claims.** Suggesting the skill itself screens counterparties, monitors transactions or verifies sanctions status.
- **Missing limitation note.** Sanctions / AML / banking / legal memos without an explicit limitation note and disclaimer.

## How to use this list

- Use it as a self-review pass before delivering an answer.
- Pair it with `evals/checklist.md` for structural review.
- If a failure is present, revise the specific section rather than the whole memo.
