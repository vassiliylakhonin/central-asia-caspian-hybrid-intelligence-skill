# Examples

These examples show how the Central Asia + Caspian Hybrid Intelligence Skill turns regional risk questions into mechanism-first, role-relevant analysis.

Use them as demonstrations of the skill contract, not as operational advice. Examples marked `live-source-backed` cite public sources retrieved on the date stated in the memo; verify current facts before using them for any real decision.

## Learning path

1. Start with [`fintech-sanctions-routing.md`](fintech-sanctions-routing.md) to see the basic reasoning-only structure for fintech, sanctions, payments and routing exposure.
2. Read [`bank-correspondent-counterparty-exposure.md`](bank-correspondent-counterparty-exposure.md) to see how the skill frames correspondent banking and EDD pressure.
3. Read [`caspian-corridor-chokepoint.md`](caspian-corridor-chokepoint.md) to see corridor and logistics risk transmission.
4. Read [`illustrative-source-packet-fintech.md`](illustrative-source-packet-fintech.md) to see how a labeled constructed packet constrains claims.
5. Read [`live-source-backed-circumvention-and-corridor.md`](live-source-backed-circumvention-and-corridor.md) to see source-backed sanctions / corridor reasoning.
6. Read [`user-provided-sources-middle-corridor.md`](user-provided-sources-middle-corridor.md) to see the mode where the user's source packet is the evidence base.
7. Read [`live-source-backed-vasp-travel-rule.md`](live-source-backed-vasp-travel-rule.md) to see source-backed crypto/VASP rails and EU Travel Rule enforcement gap analysis for fintech compliance leadership (#13 archetype).
8. Read [`live-source-backed-customs-statistics-anomaly.md`](live-source-backed-customs-statistics-anomaly.md) to see source-backed customs / mirror-statistic anomaly analysis as a sanctions-circumvention indicator for a European trade finance bank with KZ counterparty exposure (#7 archetype).

## Evidence modes

| Evidence mode | What it means | Start here |
|---|---|---|
| `reasoning-only` | No live sources checked; structural reasoning only, with explicit limits. | [`fintech-sanctions-routing.md`](fintech-sanctions-routing.md) |
| `illustrative source packet` | Claims are grounded in a constructed demonstration packet, not real operational evidence. | [`illustrative-source-packet-fintech.md`](illustrative-source-packet-fintech.md) |
| `live-source-backed` | Public sources were retrieved and cited for the example. | [`live-source-backed-circumvention-and-corridor.md`](live-source-backed-circumvention-and-corridor.md) |
| `user-provided sources` | The user's supplied packet is treated as the evidence base. | [`user-provided-sources-middle-corridor.md`](user-provided-sources-middle-corridor.md) |

## Domain routes

| Domain | Examples |
|---|---|
| Fintech / payments / routing | [`fintech-sanctions-routing.md`](fintech-sanctions-routing.md), [`illustrative-source-packet-fintech.md`](illustrative-source-packet-fintech.md) |
| Correspondent banking / EDD | [`bank-correspondent-counterparty-exposure.md`](bank-correspondent-counterparty-exposure.md), [`live-source-backed-bank-correspondent.md`](live-source-backed-bank-correspondent.md) |
| Corridor / logistics | [`caspian-corridor-chokepoint.md`](caspian-corridor-chokepoint.md), [`user-provided-sources-middle-corridor.md`](user-provided-sources-middle-corridor.md) |
| Energy / infrastructure | [`energy-infrastructure-corridor-risk.md`](energy-infrastructure-corridor-risk.md), [`live-source-backed-energy-corridor.md`](live-source-backed-energy-corridor.md) |
| Beneficial ownership / adjacency | [`beneficial-ownership-opacity.md`](beneficial-ownership-opacity.md), [`live-source-backed-bo-opacity.md`](live-source-backed-bo-opacity.md) |
| Trade finance / dual-use routing | [`trade-finance-dual-use-routing.md`](trade-finance-dual-use-routing.md) |
| Trade finance / sanctions circumvention detection | [`live-source-backed-customs-statistics-anomaly.md`](live-source-backed-customs-statistics-anomaly.md) |
| Crypto / VASP rails | [`live-source-backed-vasp-travel-rule.md`](live-source-backed-vasp-travel-rule.md) |

## Labeling styles

Examples use one of two compatible per-claim labeling styles:

- **Inline label + source reference** (e.g. `Verified [S1, S3]:`, `Plausible [S5]:`, `Judgment:`, `Unknown`) — used in the source-anchored examples such as [`live-source-backed-customs-statistics-anomaly.md`](live-source-backed-customs-statistics-anomaly.md). The bracketed `[Sx]` keys point to a source table at the foot of the memo.
- **Canonical Axis A / Axis B tags** as defined in [`AGENTS.md`](../AGENTS.md): `[primary]` / `[secondary]` / `[user-provided]` / `[inference]` / `[analyst-judgment]` on Axis A, with optional `[verify]` / `[stale-risk: YYYY-MM]` on Axis B.

Crosswalk: `Verified` ↔ `[primary]` or `[secondary]` (depending on the source tier); `Plausible` ↔ `[secondary][verify]`; `Judgment` ↔ `[analyst-judgment]`; `Unknown` ↔ does not produce a claim — surfaces a `Stop and request` or `Flag-but-don't-use` outcome per the three-value response logic.

New live-source-backed examples should use the canonical Axis A / Axis B tags. Existing examples may retain the inline style.

## How to judge an example

A strong example should:
- state the primary driver;
- explain the risk transmission mechanism before the implication;
- declare evidence mode and confidence;
- separate verified facts, plausible patterns, judgment and unknowns;
- map role-based implications for the relevant user;
- identify trigger points and watch-next indicators;
- include a limitation note and avoid legal or compliance determinations.

Use [`../evals/checklist.md`](../evals/checklist.md) for a fuller review pass.
