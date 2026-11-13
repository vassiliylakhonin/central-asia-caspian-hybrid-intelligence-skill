"""Field due-diligence checklist for local counsel in Central Asia / Caspian.

This module produces a template of documents to request and questions to ask
local counsel when open-source data is insufficient. It produces no finding,
screens nothing, and holds no jurisdiction data: document and registry names
vary by country and change over time, so every item is marked for verification
with local counsel before use.
"""

from __future__ import annotations

import json
from typing import Any

CHECKLIST = "checklist"
INVALID_INPUT = "invalid_input"

VERIFY_NOTE = (
    "Document and registry names vary by jurisdiction and change over time. "
    "Confirm each item's current local name, issuing authority and expected "
    "form with local counsel before requesting or relying on it."
)

# (area, what to request or ask). Generic by design: jurisdiction-specific
# names belong to local counsel, not to this template.
ITEMS: list[tuple[str, str]] = [
    (
        "incorporation",
        "Current state registration / incorporation extract for the entity, "
        "dated close to the decision date.",
    ),
    (
        "incorporation",
        "Charter or foundation documents with all registered amendments.",
    ),
    (
        "ownership",
        "Shareholder register or filed ownership declaration, including any "
        "beneficial-ownership filing the jurisdiction requires.",
    ),
    (
        "ownership",
        "Ask counsel how ownership changes are registered locally and how a "
        "recent change would appear in the record.",
    ),
    (
        "tax",
        "Tax registration certificate and a current tax-standing letter from "
        "the local authority.",
    ),
    (
        "licensing",
        "Licenses or permits for the declared activity; ask counsel which "
        "activities in the planned transaction require a license locally.",
    ),
    (
        "litigation",
        "Court and enforcement-proceedings extracts for the entity and its "
        "principals; ask counsel which registers exist and how far back they "
        "reach.",
    ),
    (
        "insolvency",
        "Bankruptcy / insolvency register extract for the entity.",
    ),
    (
        "banking",
        "Bank account confirmation and whether the entity's declared banking "
        "route matches locally registered accounts.",
    ),
    (
        "trade",
        "Import/export registration and customs authorizations where the "
        "counterparty declares cross-border trade.",
    ),
    (
        "authority",
        "Signatory authority evidence (power of attorney, board decision) for "
        "the people signing for the counterparty.",
    ),
    (
        "assets",
        "Registration extracts for assets offered as collateral (vessels, "
        "wagons, warehouses, real estate) and any registered pledges over them.",
    ),
    (
        "sanctions-aml",
        "Ask counsel which local screening lists, financial-intelligence "
        "reporting duties and currency-control rules apply to the planned "
        "transaction. This checklist is not screening and returns no verdict.",
    ),
]


def build_checklist(country: str, counterparty_type: str = "company") -> dict[str, Any]:
    return {
        "status": CHECKLIST,
        "tool": "draft_field_dd_checklist",
        "result_is_not_a_finding": True,
        "human_review_required": True,
        "country": country,
        "counterparty_type": counterparty_type,
        "note": VERIFY_NOTE,
        "items": [
            {"area": area, "request": request, "verify_with_local_counsel": True}
            for area, request in ITEMS
        ],
        "detail": (
            "A template of documents to request and questions for local counsel "
            "when open-source data is insufficient. It contains no jurisdiction "
            "data and no assessment of the counterparty."
        ),
    }


def draft_field_dd_checklist_json(country: str, counterparty_type: str = "company") -> str:
    """Tool entry point: validate and serialize. Never raises."""
    if not country or not country.strip():
        return json.dumps(
            {
                "status": INVALID_INPUT,
                "tool": "draft_field_dd_checklist",
                "detail": "A country is required; no default jurisdiction is assumed.",
                "result_is_not_a_finding": True,
                "human_review_required": True,
            }
        )
    return json.dumps(build_checklist(country.strip(), counterparty_type.strip() or "company"))
