# GraphRAG Ontology

To move beyond flat markdown archetypes, this skill relies on a graph-based understanding of risk.

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

## Usage
Agents should use the `analyze_graph_relationships` tool to evaluate these edges (e.g., detecting if a Kazakhstan bank is `CORRESPONDENT_FOR` an entity that `TRANSACTS_WITH` a sanctioned Russian node).

## Dark Factory Execution
The graph is traversed continuously in the background. Node risk scores are autonomously updated without prompting, supporting the Infinity scale ratio.
