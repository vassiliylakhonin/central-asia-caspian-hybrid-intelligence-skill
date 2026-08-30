# Substantive rubric — Central Asia + Caspian specialist lift

Bar 3 criterion **B3.1**. This rubric is the measuring instrument. If it is
wrong, the measurement is worthless, so it is pre-registered: `lift_eval.py`
records its SHA-256 at `prepare` time and refuses to score if it changed after
outputs were generated.

## Provenance — read this before trusting a result

Every item below is **derived from this repository's own regional
documentation**, not written from general knowledge. Each carries a `Source`
line pointing at the file and section that encodes the regional fact it tests.
The rubric formalises knowledge already committed to this repo; it does not
introduce new regional claims.

This matters because of who wrote it. The items were drafted by a language
model working from `docs/risk-archetypes.md`, `docs/regional-logic.md`,
`docs/source-guide.md` and `SKILL.md`. A rubric drafted from a model's own
impressions of the region would partly measure "does the skill agree with the
model", not "does the skill add regional depth". Deriving every item from
committed documentation is what keeps that failure out — but it does not remove
it entirely, because a model still chose *which* documented facts became items.

**Disclose this limitation in any result produced with this rubric**, and treat
author review of the items as the step that retires it. The items are testable
against the documentation: for each one, the `Source` line either supports it or
does not.

## What makes an item substantive

Every item must be answerable **yes or no by someone who knows the region**,
against the output text alone, and must fail on a competent generic answer.

An item is **structural** — and does not belong here — if a well-formed memo on
any topic could satisfy it. "Separates facts from assessments", "states an
evidence mode", "lists indicators to watch" are structural. Bar 2 already
measures those, and they are why a structural rubric shows a large delta for any
skill file.

## Scoring

One point per item, binary, maximum 10. No partial credit — a half-satisfied
substantive item is an unsatisfied one. Record the ids satisfied, not only the
total, so a judge's reasoning stays auditable.

Items that cannot apply to a given case (S5 on a case with no EU sanctions
dimension, S7 on an in-scope case) are scored as **not applicable and excluded
from that case's denominator**. Record the denominator per case.

## Items

### S1 — Names the archetype's actual mechanism

- **Question:** Does the output state the specific causal path by which the risk
  reaches this decision-maker, matching the mechanism recorded for the relevant
  archetype?
- **Why substantive:** A generic answer names the topic ("sanctions risk",
  "compliance exposure"). The archetypes record *how* the risk arrives, and it
  is frequently not the obvious route — correspondent de-risking, for instance,
  transmits through the tier-1 bank's own enforcement-risk appetite, not through
  the regional bank being designated.
- **Satisfied when:** the named mechanism matches the archetype's `Mechanism`
  line in substance, not merely in topic.
- **Source:** `docs/risk-archetypes.md`, per-archetype **Mechanism**.

### S2 — Names a false positive before drawing an implication

- **Question:** Does the output name at least one ordinary, non-illicit
  explanation for the indicator it is reasoning from, before stating what the
  indicator implies?
- **Why substantive:** This is the item most likely to separate regional depth
  from confident pattern-matching. Every archetype records its characteristic
  false positives — mirror-data gaps have methodology changes and free-zone
  reporting differences behind them; cash-intensive businesses are normal in
  low-banking-penetration regions; nominee structures include legitimate family
  holdings. A generic answer treats the indicator as evidence of wrongdoing.
- **Satisfied when:** a specific alternative explanation appears, and appears
  *before* the implication, not as a trailing caveat.
- **Source:** `docs/risk-archetypes.md`, per-archetype **False positives**;
  `SKILL.md`, Response-Mode Hard Stops ("Explain false positives before drawing
  implications").

### S3 — Names a verification artifact a reviewer could actually pull

- **Question:** Does the output name a specific document, record or dataset,
  identifiable well enough that a reviewer could go and request it?
- **Why substantive:** A generic answer says "conduct enhanced due diligence" or
  "verify the counterparty". The archetypes record what evidence actually
  settles each question: customs data on *both* legs, end-user declarations,
  transport documents, BO filings, court records, port dwell-time statistics.
- **Satisfied when:** at least one named artifact matches the archetype's
  `Evidence needed` line. Naming a source *class* without the artifact
  ("official records") does not satisfy this.
- **Source:** `docs/risk-archetypes.md`, per-archetype **Evidence needed**;
  `docs/source-guide.md`, Tier 1.

### S4 — Names the operative authority, not only a famous one

- **Question:** Does the output name the body that would actually rule on, or
  supervise, the question at hand?
- **Why substantive:** A generic answer reaches for OFAC and FATF. The operative
  authority is often regional and specific: AFSA within the AIFC, the national
  financial-monitoring agency, the National Bank of the relevant state, EAG
  rather than FATF plenary for the mutual-evaluation record. The distinction
  changes who the user contacts and which record governs.
- **Satisfied when:** the operative regional or sectoral authority is named
  where one exists. Naming an international body *in addition* is fine; naming
  only an international body where a regional one governs is not.
- **Source:** `docs/source-guide.md`, National regulators and central banks;
  Financial intelligence and AML-relevant public sources (MONEYVAL / EAG).

### S5 — EU sanctions referenced by package, contents not asserted from memory

- **Question:** Where EU sanctions are part of the transmission channel, does
  the output identify the package or the underlying regulation, and decline to
  assert its contents without retrieval?
- **Why substantive:** Practitioners track EU measures by numbered package and
  by the Council legal acts amending Regulations 833/2014 and 269/2014. A
  generic answer asserts what a package "does" from memory, which is the exact
  failure this repo documents.
- **Satisfied when:** the package number or regulation is named *and* the output
  states that current legal text and the consolidated list must be retrieved
  before operational use.
- **Not applicable** where EU sanctions are not part of the mechanism.
- **Source:** `docs/regional-logic.md`, "EU sanctions packages — taxonomy note".

### S6 — Any non-core geography arrives with its transmission channel

- **Question:** For every country outside Central Asia the output introduces,
  does it state the specific channel through which that country changes the
  mechanism?
- **Why substantive:** Generic geopolitical writing sprinkles Russia, China and
  the EU for atmosphere. This repo's core rule is that geography expansion is a
  deliberate analytical choice and that a country named without a transmission
  channel should be cut.
- **Satisfied when:** every non-core geography mentioned carries a stated
  channel. One decorative mention fails the item.
- **Source:** `docs/regional-logic.md`, Core rule and "What this means in
  practice".

### S7 — Out-of-scope questions are declined, not answered weakly

- **Question:** Where the question has no Central Asian transmission channel,
  does the output say so and decline rather than produce a regional-sounding
  answer?
- **Why substantive:** Russia-only or China-only bilateral analysis, pure
  domestic South Caucasus politics, Iran flows with no Caspian or Central Asian
  routing, and pure macro/FX questions are documented as out of scope. The
  failure mode is a fluent, plausible, low-quality regional answer — which
  scores *well* on a structural rubric.
- **Satisfied when:** the scope mismatch is named and the channel that would
  bring it in scope is identified, or its absence stated.
- **Not applicable** to in-scope cases.
- **Source:** `docs/regional-logic.md`, "Out-of-scope handling".

### S8 — Marketing claims are treated as claims to test

- **Question:** Where the input contains a characterisation such as
  "EU-compliant", "clean", "approved route", "routine logistics" or "low-risk
  counterparty", does the output preserve it as an unverified source claim
  rather than adopting it?
- **Why substantive:** Adopting the counterparty's own framing is the most
  common way a compliance read goes wrong, and it is invisible in a
  well-structured memo. A generic answer repeats the characterisation as
  background fact.
- **Satisfied when:** the claim is explicitly marked as requiring testing, and
  the output does not later rely on it.
- **Not applicable** where the input contains no such claim.
- **Source:** `SKILL.md`, Response-Mode Hard Stops.

### S9 — Mitigation is matched to the stated role

- **Question:** Are the recommended actions ones the stated role can actually
  take?
- **Why substantive:** The archetypes record different mitigation questions per
  role — a bank asks about EDD escalation and control-test frameworks, a fintech
  about corridor- and HS-code-level monitoring and rail redundancy, an investor
  about revenue concentration and diligence depth, a logistics operator about
  end-user documentation and refusal protocols. A generic answer gives
  undifferentiated advice that fits none of them.
- **Satisfied when:** at least two recommended actions are specific to the
  stated role and would be different for a different role.
- **Source:** `docs/risk-archetypes.md`, per-archetype **Mitigation questions
  (role-based)**.

### S10 — Watch-next items are observable events, not conditions

- **Question:** Are the indicators things that either happen or do not, on a
  date, observable by the user?
- **Why substantive:** "Monitor developments" and "watch the sanctions
  environment" are conditions, not indicators. The archetypes record events:
  additions to high-priority items lists, designations of named forwarders,
  FATF grey-listing, scheme exits, capacity announcements, FIU advisories.
- **Satisfied when:** at least two indicators are discrete observable events
  with a named source that would report them.
- **Source:** `docs/risk-archetypes.md`, per-archetype **Watch-next triggers**.

## Change log

Every edit after the first `prepare` run invalidates every run that used the old
hash. Record edits here with the date and the reason.

| Date | Change | Runs invalidated |
|---|---|---|
| 2026-08-30 | Initial ten items, derived from committed regional documentation | none — no prior run |
