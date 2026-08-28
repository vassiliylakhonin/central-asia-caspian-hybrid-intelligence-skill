"""MCP server skeleton for the Central Asia and Caspian skill.

Nothing here screens anything yet. Each tool is declared so the transport and
tool surface can be exercised, and each one refuses instead of answering.

The first version of this file returned `{"status": "clear", "confidence": 0.95}`
for any entity name it was given, and AGENTS.md points an agent at this file to
"expose tools to the agent". A fabricated clearance is worse than no tool: an
agent has no way to tell it apart from a real screening result. Until a tool is
backed by an actual source, it must say so.
"""

from mcp.server.fastmcp import FastMCP
from mcp_contract import unimplemented_response

mcp = FastMCP("central-asia-caspian-compliance-server")

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


if __name__ == "__main__":
    mcp.run(transport="stdio")
