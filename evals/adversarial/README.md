# Adversarial cases — Central Asia & Caspian

Domain-specific stress cases for the Central Asia & Caspian vertical skill.

Each case is an input designed to **fail predictably** if the skill is applied honestly: traps drawn from real failure patterns in regional sanctions, AML, correspondent banking, beneficial-ownership, and corridor-logistics work. The point is not a benchmark — there is no scoring tooling here — but to make trust-layer behavior **observable**: did the skill stay in the right response mode (Answer / Flag-but-don't-use / Stop-and-request, per [`AGENTS.md`](../../AGENTS.md)), or did it quietly absorb the trap?

Use alongside [`../checklist.md`](../checklist.md), [`../failure-modes.md`](../failure-modes.md), and the project's [`../self-adversarial-review.md`](../self-adversarial-review.md). Those are about reviewing the skill itself and reviewing memos against criteria. **Adversarial cases here are about feeding the skill bad inputs and checking refusal behavior.** Different axis, complementary.

## Status

Illustrative. Two starter cases. Not a validated benchmark; not external review. Cases are author-designed traps reflecting common regional patterns. They do **not** clear any bar in [`AGENTS.md`](../../AGENTS.md) Definition of Done that requires identifiable external reviewers, and they do not change [`STATUS.md`](../../STATUS.md).

## Case format

1. **Setup** — input the agent receives (prompt + retrieved content).
2. **Adversarial vector** — the trap and why a naive agent falls for it.
3. **Expected response mode** — Answer / Flag-but-don't-use / Stop-and-request.
4. **Pass criteria** — concrete things the memo must do.
5. **Fail signals** — observable cues that the trap caught the agent.

## How to run a case

1. Paste the **Setup** block to an agent loaded with this skill.
2. Read output against **Pass criteria** and **Fail signals**.
3. Note pass / partial / fail informally. No scoring file is maintained.

## Cases

| # | File | Domain trap |
|---|---|---|
| 01 | [case-01-caspian-sts-reflagging.md](case-01-caspian-sts-reflagging.md) | Caspian STS transfer + re-flagging framed as routine logistics |
| 02 | [case-02-ca-bank-eu-compliant-routing.md](case-02-ca-bank-eu-compliant-routing.md) | Central-Asia bank intermediary labeled "EU-compliant" for Russia-routed payment |

## Adding a new case

Keep cases markdown-only. Each case should isolate **one** failure vector with pass/fail criteria precise enough that two reviewers would agree. Do not add scripts, schemas, or scoring infrastructure — those belong in [Agenda Intelligence MD](https://github.com/vassiliylakhonin/Agenda-Intelligence-md).
