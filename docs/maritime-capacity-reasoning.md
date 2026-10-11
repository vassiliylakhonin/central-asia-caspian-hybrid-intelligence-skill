# Caspian maritime capacity: mechanisms and model handoff

Use this reference for vessel renewal, capacity and port/rail coordination
questions. It adds regional reasoning; it is not a fleet model, hydrographic
service or navigation-safety assessment.

## Distinguish the mechanisms

Trace the relevant chain before recommending an intervention:

1. **Payload constraint:** water level and port/channel geometry → permissible
   draft and specialist-assessed payload → useful capacity per departure.
   A gauge reading alone does not determine a vessel's payload allowance.
2. **Cycle constraint:** sailing, waiting, berth and wagon-handling time →
   complete round trips → annual capacity of the dedicated fleet.
3. **Interface constraint:** railway, wagon, terminal or berth allocations →
   usable directional throughput. Additional vessels may leave this unchanged.
4. **Demand constraint:** cargo segment, direction, season and shipper choice →
   achievable loading and revenue. An aggregate corridor-growth headline does
   not establish demand for a particular train ferry, Ro-Ro or container service.

These are mechanisms to test, not claims about which currently binds on a route.
Do not infer a shortage from fleet age alone, or attribute a throughput change
to low water without checking demand, downtime and interface alternatives.

## Evidence to request or verify

Keep Baku–Aktau, Baku–Kuryk and Baku–Turkmenbashi distinct when in scope. Include
vessels serving the route irrespective of flag or ownership; distinguish the
fleet inventory from the vessels actually allocated and available that period.
Do not deduplicate or join vessels by name alone when stable identifiers exist.

| Question | Inspectable input |
|---|---|
| What can each vessel carry? | Vessel identity, cargo unit/type, condition and class records; specialist-approved draft/payload assumptions for the route and scenario. |
| How many productive cycles? | Dated departure/arrival and port-event records, maintenance/outage periods, operating calendar and processing times at both ends. |
| What limits interfaces? | Directional port and railway allocations, terminal and wagon constraints, other traffic and coordination rules. |
| Is demand comparable to capacity? | Cargo segment and direction, time period, source definitions, forecast method and uncertainty. |
| Who can implement a remedy? | Operator, port, railway and public-institution responsibilities, contractual dependencies, costs and decision authority. |

Differentiate vessel calls, sailings, tonnes, TEU, FEU, wagons and lane-metres.
Do not convert them using an unstated coefficient. Separate nominal design
capacity, available operating capacity, observed throughput and forecast demand.
Preserve discrepancies between operator and official statistics rather than
averaging them into an apparent consensus. AIS coverage gaps are not proof
that a vessel did not operate.

## Optional quantitative handoff

When available, Corridor Bankability Analyst's
[maritime capacity model and user guide](https://github.com/vassiliylakhonin/corridor-bankability-analyst/blob/main/docs/maritime-capacity-model.md)
accept a single cargo unit, dedicated vessel groups, directional port/rail
allocations and explicit scenarios. Supply claim IDs or written assumptions for
each numeric input. Keep input/output files, command, code revision, scenario
IDs and unresolved technical gaps with the memo.

The model compares caller-defined alternatives. It does not infer draft from
water levels, forecast demand, optimise vessel rotations or certify safe
operations. For shared fleets or seasonal queues, request a suitable external
model or retain the limitation; do not enter the same vessels twice. No model
run is implied by loading this skill. If unavailable, continue with a bounded
mechanism analysis and identify the numerical result that remains unknown.

The regional MCP remains a `not_implemented` transport skeleton. Run MCP servers
in separate environments when composing: Corridor Bankability requires MCP
1.x; this skeleton and GTTA's optional MCP adapter require MCP 2.x. No live
screening or maritime-data integration is created by this reference.

## Interpretation check

For example, if an illustrative model increases fleet capacity but leaves
served cargo unchanged because a supplied port allocation binds, examine port
coordination and the allocation assumption before recommending more vessels.
If a lower-payload assumption makes the fleet bind instead, identify the
specialist evidence needed to validate that allowance. Both observations are
conditional model interpretations, not findings about current Caspian operations.
