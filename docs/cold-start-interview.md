# Cold-start interview

A short preflight conversation that turns a generic Central Asia + Caspian memo run into one anchored to **this user's** role, geography, decision context, and source access. Run before substantive analysis when the user is new to the skill or when prior context is missing.

## When to run

- First time the user invokes the skill in a project.
- The user asks for a memo without stating role, decision, geography, or time horizon.
- `templates/practice-profile.md` does not exist in the working directory **or** still contains `[PLACEHOLDER]` markers.
- The user explicitly asks to reset or update their profile.

## When to skip

- The user supplies the four anchors (role, decision, geography, time horizon) inline in the prompt.
- A populated practice profile already exists in the project and the current question fits within it.
- The user explicitly asks for a one-off `reasoning-only` memo with stated scope.

## STOP rule

If a populated practice profile is **expected** for the workflow (e.g. the user references "our usual format") and the file is missing or contains `[PLACEHOLDER]` markers — **stop and run the interview** before producing output. Generic memos with unstated audience are worse than no memo.

## Interview questions

Ask in this order. Skip questions where the answer is already obvious from the user's prompt. Do not ask all of them mechanically — collapse where a single answer covers several.

### 1. Role and mandate
- What is your role and the role of the readers of this memo? (sanctions compliance / AML / correspondent banking / corridor logistics / energy trading / fintech risk / policy / journalism / other)
- What kind of decision does the memo usually inform? (transaction approval / counterparty onboarding / corridor routing / market-entry / divestment / advisory / situational awareness)
- What's the consequence of being wrong in each direction? (over-cautious blocks legitimate business; under-cautious creates compliance or operational risk)

### 2. Geography and jurisdictions
- Which Central Asia / Caspian countries are in scope by default? (KZ / UZ / TM / KG / TJ / AZ / Caspian region / Russia interfaces / China interfaces / EU interfaces)
- Which jurisdictions impose **regulatory exposure** on your decisions? (US / EU / UK / CH / national; whose secondary sanctions matter)
- Are there countries explicitly out of scope?

### 3. Decision context and risk appetite
- What time horizon do decisions usually cover? (transactional / 6–12 months / multi-year)
- How conservative is the default posture? (zero residual risk acceptable / risk-priced / opportunistic with downside controls)
- Which red lines are non-negotiable? (any OFAC SDN nexus / any IRGC nexus / any BO opacity above threshold / etc.)

### 4. Source access
- Which authoritative sources are accessible to you directly? (OFAC, EU consolidated, OFSI, national registries, FATF/EAG, customs data, paid databases — name them)
- Which sources are **not** accessible and need to be flagged `[verify]` when cited?
- Do you use external retrieval (web search, MCP servers, paid intel feeds), or is the skill expected to work from user-provided source packets only?

### 5. Output preferences
- Memo length default? (quick note / standard memo / extended brief)
- Where do you want the boundary between analysis and operational recommendation drawn?
- Confidentiality / privilege markings the output should inherit?

## After the interview

1. Write or update `templates/practice-profile.md` in the user's project with the captured answers. Replace `[PLACEHOLDER]` markers with the actual values.
2. Confirm the captured profile back to the user in one paragraph before proceeding.
3. Begin substantive work using the profile as the default `Decision / Audience / Geography / Time horizon` block for all memos in this session.

## Update rules

- The profile is a working document, not a contract. The user can ask to revise any field at any time.
- When a memo's actual scope diverges from the profile (e.g. a one-off question outside the user's usual geography), state the divergence explicitly in the memo header — do not silently override the profile.
- If a field is left as `[PLACEHOLDER]` because the user genuinely has no answer yet, leave it as `[PLACEHOLDER]` and surface it as an open question rather than guessing.

## Limitation note

This interview captures **stated** preferences. It does not verify the user's authority to act on the decisions they describe, the accuracy of their source access claims, or the appropriateness of their risk appetite for any given counterparty or transaction. The interview is a calibration step for the skill, not a delegation of operational authority.
