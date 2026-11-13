"""MCP server for the Central Asia and Caspian skill.

The three screening tools are declared so the transport and tool surface can
be exercised, and each one refuses instead of answering. Two tools are
implemented, both deterministic and data-free: `estimate_caspian_capacity`
combines caller-supplied figures, each with a caller-stated source, and
`draft_field_dd_checklist` returns a template of requests for local counsel.
Neither adds data or produces a finding.

The first version of this file returned `{"status": "clear", "confidence": 0.95}`
for any entity name it was given, and AGENTS.md points an agent at this file to
"expose tools to the agent". A fabricated clearance is worse than no tool: an
agent has no way to tell it apart from a real screening result. Until a tool is
backed by an actual source, it must say so.
"""

from mcp.server.mcpserver import MCPServer

from .capacity import estimate_capacity_json
from .contract import unimplemented_response
from .dd_checklist import draft_field_dd_checklist_json

mcp = MCPServer("central-asia-caspian-compliance-server", version="0.3.0")


def _unimplemented(tool: str, needs: str, **echo: object) -> str:
    return unimplemented_response(tool, needs, **echo)


@mcp.tool()
def query_regional_sanctions(entity_name: str) -> str:
    """Screen an entity against regional sanctions lists. Not yet implemented.

    Returns status ``not_implemented``. Do not read the response as a clearance.
    """
    return _unimplemented(
        "query_regional_sanctions",
        "a sanctions list source (OFAC SDN, EU consolidated, UK OFSI, or UN)",
        entity=entity_name,
    )


@mcp.tool()
def analyze_graph_relationships(node_id: str, depth: int = 2) -> str:
    """Traverse the regional knowledge graph. Not yet implemented.

    Returns status ``not_implemented``. An empty edge list is not evidence of
    an absence of connections.
    """
    return _unimplemented(
        "analyze_graph_relationships",
        "an ownership or control graph to traverse",
        node=node_id,
        depth=depth,
    )


@mcp.tool()
def estimate_caspian_capacity(scenario: dict) -> str:
    """Estimate Caspian route capacity from caller-supplied figures.

    ``scenario`` is a JSON object: ``vessel_groups`` (name, vessels,
    payload_tonnes_per_departure, cycle_hours, operating_days_per_year, and
    an optional ``draft_constraint`` of caller-supplied depth/clearance/design
    draft figures) and optional ``interface_constraints`` (name,
    tonnes_per_year). Every figure is ``{"low": ..., "high": ..., "source":
    ...}``; a figure without a source is rejected, never defaulted. The tool
    holds no sea-level or port-depth data. Returns a low/high capacity range,
    the binding constraint, and the arithmetic assumptions. The result is
    arithmetic on the caller's inputs, not a finding about current operations.
    """
    return estimate_capacity_json(scenario)


@mcp.tool()
def draft_field_dd_checklist(country: str, counterparty_type: str = "company") -> str:
    """List documents to request and questions for local counsel.

    For use when open-source data is insufficient. Returns a generic template
    marked item-by-item for verification with local counsel; document and
    registry names vary by jurisdiction. This is not screening and produces
    no finding about the counterparty.
    """
    return draft_field_dd_checklist_json(country, counterparty_type)


@mcp.tool()
def retrieve_memory_context(client_id: str) -> str:
    """Retrieve a client's recorded risk appetite and past verdicts. Not yet implemented.

    Returns status ``not_implemented``. Absence of escalations here does not mean
    a client has none.
    """
    return _unimplemented(
        "retrieve_memory_context",
        "a persisted client record store",
        client=client_id,
    )


def main() -> None:
    """Console-script entry point declared in ``pyproject.toml``."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
