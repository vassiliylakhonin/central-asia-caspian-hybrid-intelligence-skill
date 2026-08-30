# Substantive rubric — Central Asia + Caspian specialist lift

Bar 3 criterion **B3.1**. This rubric is the measuring instrument. If it is
wrong, the measurement is worthless, so it is pre-registered: `lift_eval.py`
records its SHA-256 at `prepare` time and refuses to score if it changed after
outputs were generated.

## What makes an item substantive

Every item must be answerable **yes or no by someone who knows the region**,
against the output text alone. It must fail on a competent generic answer.

An item is **structural** — and does not belong here — if a well-formed memo on
any topic could satisfy it. "Separates facts from assessments", "states an
evidence mode", "lists indicators to watch" are structural. Bar 2 already
measures those, and they are why a structural rubric shows a large delta for any
skill file.

An item is **substantive** if satisfying it requires knowing this region:

- names the actual transmission channel, not a plausible-sounding one;
- names the authoritative body that would rule on the question;
- names a specific false positive a regional analyst would expect;
- names a verification artifact a reviewer could actually pull;
- rejects a premise that is wrong for this region specifically.

## Scoring

One point per item, binary. No partial credit — a half-satisfied substantive
item is an unsatisfied one. Record the item ids satisfied, not just the total,
so a judge's reasoning stays auditable.

## Items

At least eight are required. Each needs an id, the question, and the
region-specific reason it cannot be satisfied generically.

> **This rubric is not written yet.** The items below are shape examples, marked
> `REPLACE-ME`. `validate_lift.py` fails while any remain, so Bar 3 cannot be
> claimed on a placeholder rubric. Writing the real items requires the regional
> knowledge this repo claims to encode — it is the author's step, not a
> generatable one.

### S1 — REPLACE-ME

- **Question:** Does the output name [the specific mechanism by which the risk
  actually reaches the decision-maker]?
- **Why substantive:** A generic answer names [the plausible but wrong channel].
  Getting this right requires knowing [the regional fact that redirects it].
- **Satisfied when:** the output names [X] as the channel, not [Y].

### S2 — REPLACE-ME

- **Question:** Does the output name the body that would actually rule on this?
- **Why substantive:** A generic answer names a well-known international body.
  The operative authority here is [regional regulator], and the distinction
  changes what the user does next.
- **Satisfied when:** [regional regulator] is named as operative.

### S3 — REPLACE-ME

- **Question:** Does the output name a false positive specific to this region?
- **Why substantive:** [Indicator] reads as evasion to a generic analyst and has
  an ordinary commercial explanation here.
- **Satisfied when:** the output states that explanation before drawing an
  implication.

### S4–S8 — REPLACE-ME

Add at least five more. Spread them across the archetypes the case set covers so
that no single item carries the measurement.

## Change log

Every edit after the first `prepare` run invalidates every run that used the old
hash. Record edits here with the date and the reason.

| Date | Change | Runs invalidated |
|---|---|---|
| — | initial template, no items written | none |
