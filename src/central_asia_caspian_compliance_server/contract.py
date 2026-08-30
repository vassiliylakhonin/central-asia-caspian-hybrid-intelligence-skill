"""Transport-independent response contract for unavailable regional tools."""

import json

NOT_IMPLEMENTED = "not_implemented"


def unimplemented_response(tool: str, needs: str, **echo: object) -> str:
    """Return an explicit non-finding; never synthesize a screening result."""
    return json.dumps(
        {
            "status": NOT_IMPLEMENTED,
            "tool": tool,
            "detail": f"{tool} has no data source wired up. It requires {needs}.",
            "result_is_not_a_finding": True,
            "human_review_required": True,
            **echo,
        }
    )
