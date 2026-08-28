# Proposed Graph Ontology

This document proposes a vocabulary that a future, separately implemented graph
store could use. The repository does not currently contain a graph database,
continuous traversal process, or verified ownership dataset.

## Node Types
- `Entity` (Company, Individual)
- `Vessel` (IMO Number, Flag)
- `Port` (Location)
- `Bank` (SWIFT/BIC)

## Edge Types
- `OWNS` (Entity -> Entity / Vessel)
- `TRANSACTS_WITH` (Entity -> Entity)
- `DOCKED_AT` (Vessel -> Port)
- `CORRESPONDENT_FOR` (Bank -> Bank)

## Current status

`analyze_graph_relationships` returns `status: not_implemented`. An empty response
is not evidence that an entity has no connections. A future implementation must
identify its data sources, retrieval date, entity-resolution method, uncertainty,
and human-review boundary before this ontology can support a finding.
