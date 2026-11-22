"""Deterministic consistency checks over caller-supplied trade-document fields.

This module compares structured fields the caller extracted from a trade
packet (contract, invoice, bill of lading, certificate of origin): HS-code
sets across documents, date ordering, and Incoterms freight/insurance
allocation. It reads no external data, checks no prices, and cannot judge
authenticity. A flag means "these supplied fields disagree", never a finding
of fraud; a "consistent" result is not a clearance.

Checks are grouped into per-field verdicts (HS codes, amount, currency,
dates, parties, Incoterms) and the packet aggregate is worst-of, not an
average: one failed critical field fails the packet, and a field with too
little data to compare is marked ``needs_human_review`` rather than passed.
This non-compensatory, human-routing shape follows the evaluation argument
of arXiv:2611.02775 (a single methodological preprint, not an empirical
result, and written for financial document recognition, not trade packets).
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import date
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field, ValidationError, field_validator

AUDIT = "audit"
INVALID_INPUT = "invalid_input"

CONSISTENT = "consistent"
INCONSISTENT = "inconsistent"
NOT_CHECKED = "not_checked"

# Per-field verdict vocabulary. Deliberately different from the per-check
# results above: a verdict is a gate decision on one critical field.
PASS = "pass"
FAIL = "fail"
NEEDS_REVIEW = "needs_human_review"

# Which checks decide each critical field's verdict, in output order.
FIELD_TO_CHECKS: dict[str, tuple[str, ...]] = {
    "hs_code": ("hs_code_format", "hs_code_consistency", "hs_heading_subdivision"),
    "amount": ("amount_consistency",),
    "currency": ("currency_consistency",),
    "dates": ("date_ordering",),
    "parties": ("party_consistency",),
    "incoterms": ("incoterms_allocation",),
}

_AMOUNT_RE = re.compile(r"^-?\d+(\.\d+)?$")
_CURRENCY_RE = re.compile(r"^[A-Z]{3}$")

# Legal-form suffixes stripped when comparing party names. Normalization is
# a comparison aid only; two names that survive it as equal can still be
# different legal entities, and two different spellings can be one entity.
_LEGAL_SUFFIXES = (
    "llp", "llc", "ltd", "jsc", "ojsc", "cjsc", "gmbh", "inc", "co",
    "ooo", "ao", "too", "ip", "plc", "sarl", "sa", "bv",
)

DOCUMENT_TYPES = (
    "contract",
    "invoice",
    "bill_of_lading",
    "certificate_of_origin",
    "insurance",
    "other",
)

# Main-carriage freight and insurance allocation per ICC Incoterms 2020
# definitions. Definitional and stable; not market or regulatory data.
INCOTERMS_ALLOCATION: dict[str, tuple[str, str]] = {
    "EXW": ("buyer", "buyer"),
    "FCA": ("buyer", "buyer"),
    "FAS": ("buyer", "buyer"),
    "FOB": ("buyer", "buyer"),
    "CFR": ("seller", "buyer"),
    "CPT": ("seller", "buyer"),
    "CIF": ("seller", "seller"),
    "CIP": ("seller", "seller"),
    "DPU": ("seller", "seller"),
    "DAP": ("seller", "seller"),
    "DDP": ("seller", "seller"),
}

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class TradeDocument(BaseModel):
    """Fields the caller extracted from one document in the packet."""

    type: Literal[  # noqa: A003 - field name required by the tool contract
        "contract", "invoice", "bill_of_lading", "certificate_of_origin", "insurance", "other"
    ]
    label: str = ""
    hs_codes: list[str] = Field(default_factory=list)
    date: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    seller: Optional[str] = None
    buyer: Optional[str] = None

    @field_validator("amount")
    @classmethod
    def _amount_format(cls, value: Optional[str]) -> Optional[str]:
        if value is not None:
            normalized = re.sub(r"[\s,]", "", value)
            if not _AMOUNT_RE.fullmatch(normalized):
                raise ValueError(
                    f"amount must be a plain number (digits, optional . decimals), got {value!r}"
                )
            return normalized
        return value

    @field_validator("currency")
    @classmethod
    def _currency_format(cls, value: Optional[str]) -> Optional[str]:
        if value is not None:
            normalized = value.strip().upper()
            if not _CURRENCY_RE.fullmatch(normalized):
                raise ValueError(f"currency must be a 3-letter code, got {value!r}")
            return normalized
        return value

    @field_validator("seller", "buyer")
    @classmethod
    def _party_format(cls, value: Optional[str]) -> Optional[str]:
        if value is not None:
            normalized = value.strip()
            return normalized or None
        return value

    @field_validator("date")
    @classmethod
    def _date_format(cls, value: Optional[str]) -> Optional[str]:
        if value is not None:
            if not _DATE_RE.fullmatch(value):
                raise ValueError(f"date must be YYYY-MM-DD, got {value!r}")
            date.fromisoformat(value)
        return value


class TradePacket(BaseModel):
    """The caller's structured view of one shipment's documents."""

    documents: list[TradeDocument] = Field(min_length=2)
    incoterm: Optional[str] = None
    freight_paid_by: Optional[Literal["seller", "buyer"]] = None
    insurance_paid_by: Optional[Literal["seller", "buyer"]] = None

    @field_validator("incoterm")
    @classmethod
    def _upper_rule(cls, value: Optional[str]) -> Optional[str]:
        return value.strip().upper() if value else value


def _normalize_hs(code: str) -> str:
    return re.sub(r"[^0-9]", "", code)


def _document_name(document: TradeDocument) -> str:
    return f"{document.type} ({document.label})" if document.label else document.type


def _check_hs_codes(documents: list[TradeDocument]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    with_codes = [d for d in documents if d.hs_codes]
    if len(with_codes) < 2:
        checks.append(
            {
                "check": "hs_code_consistency",
                "result": NOT_CHECKED,
                "detail": "Fewer than two documents carry HS codes.",
            }
        )
        return checks

    malformed = sorted(
        {c for d in with_codes for c in d.hs_codes if not 6 <= len(_normalize_hs(c)) <= 10}
    )
    if malformed:
        checks.append(
            {
                "check": "hs_code_format",
                "result": INCONSISTENT,
                "detail": "Codes outside the 6-10 digit range after normalization: "
                + ", ".join(malformed)
                + ". Format only; validity against the HS nomenclature is not checked.",
            }
        )
    else:
        checks.append(
            {
                "check": "hs_code_format",
                "result": CONSISTENT,
                "detail": "All codes normalize to 6-10 digits.",
            }
        )

    document_codes = [(d, {_normalize_hs(code) for code in d.hs_codes}) for d in with_codes]
    union = set().union(*(codes for _, codes in document_codes))
    disagreements = sorted(
        f"{_document_name(document)} lacks: {', '.join(sorted(union - codes))}"
        for document, codes in document_codes
        if codes != union
    )
    checks.append(
        {
            "check": "hs_code_consistency",
            "result": INCONSISTENT if disagreements else CONSISTENT,
            "detail": "; ".join(disagreements)
            if disagreements
            else "Identical normalized HS-code sets across documents.",
        }
    )

    headings: dict[str, set[str]] = {}
    for code in sorted(union):
        headings.setdefault(code[:6], set()).add(code)
    split = {h: sorted(c) for h, c in headings.items() if len(c) > 1}
    checks.append(
        {
            "check": "hs_heading_subdivision",
            "result": INCONSISTENT if split else CONSISTENT,
            "detail": (
                "Same 6-digit heading with different national subdivisions: "
                + "; ".join(f"{h}: {', '.join(c)}" for h, c in split.items())
                if split
                else "No heading splits across subdivisions."
            ),
        }
    )
    return checks


def _check_dates(documents: list[TradeDocument]) -> list[dict[str, Any]]:
    dated: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for document in documents:
        if document.date is not None:
            dated[document.type].append((document.date, _document_name(document)))
    pairs = [
        ("contract", "invoice"),
        ("invoice", "bill_of_lading"),
        ("certificate_of_origin", "bill_of_lading"),
    ]
    compared = False
    violations = []
    for earlier, later in pairs:
        if not (dated[earlier] and dated[later]):
            continue
        compared = True
        # If these extremes are in order, so is every pair of these types.
        latest_date, latest_document = max(dated[earlier])
        earliest_date, earliest_document = min(dated[later])
        if latest_date > earliest_date:
            violations.append(
                f"{latest_document} dated {latest_date} is after "
                f"{earliest_document} dated {earliest_date}"
            )
    if not compared:
        return [
            {
                "check": "date_ordering",
                "result": NOT_CHECKED,
                "detail": "No supported document pair contains two dates.",
            }
        ]
    return [
        {
            "check": "date_ordering",
            "result": INCONSISTENT if violations else CONSISTENT,
            "detail": "; ".join(violations)
            if violations
            else "Comparable dates are in the expected order (contract <= invoice "
            "<= bill of lading; certificate of origin <= bill of lading).",
        }
    ]


def _check_incoterms(packet: TradePacket) -> list[dict[str, Any]]:
    if packet.incoterm is None:
        return [
            {
                "check": "incoterms_allocation",
                "result": NOT_CHECKED,
                "detail": "No Incoterm rule supplied.",
            }
        ]
    allocation = INCOTERMS_ALLOCATION.get(packet.incoterm)
    if allocation is None:
        return [
            {
                "check": "incoterms_allocation",
                "result": NOT_CHECKED,
                "detail": f"Unknown Incoterm rule {packet.incoterm!r}; allocation not checked.",
            }
        ]
    expected_freight, expected_insurance = allocation
    mismatches = []
    if packet.freight_paid_by and packet.freight_paid_by != expected_freight:
        mismatches.append(
            f"{packet.incoterm} allocates main-carriage freight to the {expected_freight}, "
            f"but freight_paid_by is {packet.freight_paid_by}"
        )
    if packet.insurance_paid_by and packet.insurance_paid_by != expected_insurance:
        mismatches.append(
            f"{packet.incoterm} allocates insurance to the {expected_insurance}, "
            f"but insurance_paid_by is {packet.insurance_paid_by}"
        )
    if not packet.freight_paid_by and not packet.insurance_paid_by:
        return [
            {
                "check": "incoterms_allocation",
                "result": NOT_CHECKED,
                "detail": "Incoterm supplied but neither freight_paid_by nor "
                "insurance_paid_by was supplied.",
            }
        ]
    return [
        {
            "check": "incoterms_allocation",
            "result": INCONSISTENT if mismatches else CONSISTENT,
            "detail": "; ".join(mismatches)
            if mismatches
            else f"Supplied payers match the {packet.incoterm} allocation "
            "(ICC Incoterms 2020 definitions).",
        }
    ]


def _normalize_party(name: str) -> str:
    # Dots go first so "L.L.P." collapses to the "llp" suffix token.
    tokens = re.sub(r"[^a-z0-9 ]", " ", name.lower().replace(".", "")).split()
    return " ".join(t for t in tokens if t not in _LEGAL_SUFFIXES)


def _check_amounts(documents: list[TradeDocument]) -> list[dict[str, Any]]:
    from decimal import Decimal

    with_amount = [d for d in documents if d.amount is not None]
    if len(with_amount) < 2:
        return [
            {
                "check": "amount_consistency",
                "result": NOT_CHECKED,
                "detail": "Fewer than two documents carry an amount.",
            }
        ]
    values = {_document_name(d): Decimal(d.amount) for d in with_amount}
    distinct = sorted(set(values.values()))
    if len(distinct) == 1:
        return [
            {
                "check": "amount_consistency",
                "result": CONSISTENT,
                "detail": "All supplied amounts are numerically equal. "
                "Whether the amount is the right one is not assessed.",
            }
        ]
    detail = "; ".join(f"{name}: {value}" for name, value in values.items())
    return [
        {
            "check": "amount_consistency",
            "result": INCONSISTENT,
            "detail": f"Amounts disagree across documents ({detail}). "
            "Numeric equality only; currency conversion is not attempted.",
        }
    ]


def _check_currencies(documents: list[TradeDocument]) -> list[dict[str, Any]]:
    with_currency = [d for d in documents if d.currency is not None]
    if len(with_currency) < 2:
        return [
            {
                "check": "currency_consistency",
                "result": NOT_CHECKED,
                "detail": "Fewer than two documents carry a currency.",
            }
        ]
    codes = {_document_name(d): d.currency for d in with_currency}
    if len(set(codes.values())) == 1:
        return [
            {
                "check": "currency_consistency",
                "result": CONSISTENT,
                "detail": "All supplied currencies are the same code. "
                "Code validity against ISO 4217 is not checked.",
            }
        ]
    detail = "; ".join(f"{name}: {code}" for name, code in codes.items())
    return [
        {
            "check": "currency_consistency",
            "result": INCONSISTENT,
            "detail": f"Currency codes differ across documents ({detail}).",
        }
    ]


def _check_parties(documents: list[TradeDocument]) -> list[dict[str, Any]]:
    disagreements: list[str] = []
    compared = False
    for role in ("seller", "buyer"):
        named = [d for d in documents if getattr(d, role) is not None]
        if len(named) < 2:
            continue
        compared = True
        variants: dict[str, list[str]] = defaultdict(list)
        for d in named:
            variants[_normalize_party(getattr(d, role))].append(
                f"{_document_name(d)} '{getattr(d, role)}'"
            )
        if len(variants) > 1:
            disagreements.append(
                f"{role} differs after normalization: "
                + "; ".join(
                    ", ".join(holders) for holders in variants.values()
                )
            )
    if not compared:
        return [
            {
                "check": "party_consistency",
                "result": NOT_CHECKED,
                "detail": "Fewer than two documents name the same party role.",
            }
        ]
    return [
        {
            "check": "party_consistency",
            "result": INCONSISTENT if disagreements else CONSISTENT,
            "detail": "; ".join(disagreements)
            if disagreements
            else "Named sellers and buyers match across documents after "
            "normalization (case, punctuation, legal-form suffixes). Name "
            "equality is not entity verification.",
        }
    ]


def _field_verdicts(checks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_check = {c["check"]: c["result"] for c in checks}
    verdicts: list[dict[str, Any]] = []
    for field_name, check_names in FIELD_TO_CHECKS.items():
        # A check that never ran (e.g. HS format/subdivision when fewer than
        # two documents carry codes) counts as not checked, never as passed.
        results = [by_check.get(name, NOT_CHECKED) for name in check_names]
        if INCONSISTENT in results:
            verdict = FAIL
        elif NOT_CHECKED in results:
            verdict = NEEDS_REVIEW
        else:
            verdict = PASS
        verdicts.append(
            {"field": field_name, "verdict": verdict, "checks": list(check_names)}
        )
    return verdicts


def _aggregate_verdict(verdicts: list[dict[str, Any]]) -> str:
    values = [v["verdict"] for v in verdicts]
    if FAIL in values:
        return FAIL
    if NEEDS_REVIEW in values:
        return NEEDS_REVIEW
    return PASS


def audit_packet(packet: TradePacket) -> dict[str, Any]:
    checks = (
        _check_hs_codes(packet.documents)
        + _check_amounts(packet.documents)
        + _check_currencies(packet.documents)
        + _check_dates(packet.documents)
        + _check_parties(packet.documents)
        + _check_incoterms(packet)
    )
    flags = [c["detail"] for c in checks if c["result"] == INCONSISTENT]
    verdicts = _field_verdicts(checks)
    return {
        "status": AUDIT,
        "tool": "audit_trade_packet",
        "result_is_not_a_finding": True,
        "human_review_required": True,
        "checks": checks,
        "flags": flags,
        "field_verdicts": verdicts,
        "aggregate": _aggregate_verdict(verdicts),
        "human_review_fields": [
            v["field"] for v in verdicts if v["verdict"] == NEEDS_REVIEW
        ],
        "detail": (
            "Consistency of caller-supplied fields only: HS-code sets, "
            "amounts, currencies, date ordering, named parties, and "
            "Incoterms allocation. The aggregate is worst-of across fields, "
            "not an average: one failed field fails the packet, and a field "
            "with too little data to compare is marked needs_human_review. "
            "No external data is read, prices are not assessed, and "
            "authenticity is not judged. A flag means the supplied fields "
            "disagree; a pass is not a clearance."
        ),
    }


def audit_trade_packet_json(arguments: dict[str, Any]) -> str:
    """Tool entry point: validate, audit, and serialize. Never raises."""
    try:
        packet = TradePacket.model_validate(arguments)
    except ValidationError as exc:
        return json.dumps(
            {
                "status": INVALID_INPUT,
                "tool": "audit_trade_packet",
                "detail": f"Invalid packet: {exc}. No defaults were substituted.",
                "result_is_not_a_finding": True,
                "human_review_required": True,
            }
        )
    return json.dumps(audit_packet(packet))
