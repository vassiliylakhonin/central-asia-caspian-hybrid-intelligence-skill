"""Deterministic Caspian capacity estimation over caller-supplied figures.

This module owns no data. Every number enters with a caller-stated source, and
the tool only combines low/high inputs into a low/high range and names the
binding constraint. It does not infer draft from water levels, forecast
demand, judge whether inputs are current, or convert between cargo units. A
result is arithmetic on the caller's assumptions, not a finding about current
Caspian operations.
"""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator

HOURS_PER_DAY = 24

ESTIMATE = "estimate"
INVALID_INPUT = "invalid_input"

ARITHMETIC_ASSUMPTIONS = [
    "A complete round trip takes cycle_hours; productive departures per vessel "
    "per year are operating_days_per_year * 24 / cycle_hours.",
    "The low estimate pairs each figure's low with the opposing figure's high "
    "(low payload, high cycle time, low operating days); the high estimate "
    "pairs them in reverse. The range is input-driven, not a confidence "
    "interval, and expresses no likelihood.",
    "Fleet capacity is the sum over vessel groups; each group is assumed to "
    "be dedicated to the scenario route. Shared fleets entered in more than "
    "one group are double-counted by the caller, not by this tool.",
    "Usable throughput is the minimum of fleet capacity and every supplied "
    "interface constraint; the binding element can differ between the low "
    "and the high estimate.",
    "Demand is not modeled: the result says nothing about achievable "
    "loading, revenue, or whether cargo exists for the capacity.",
    "All tonnes figures must use one cargo unit chosen by the caller; the "
    "tool does not convert tonnes, TEU, wagons, or lane-metres.",
]


class Figure(BaseModel):
    """One caller-supplied quantity as a low/high range with its source."""

    low: float
    high: float
    source: str = Field(min_length=1)
    unit: str = ""

    @field_validator("source")
    @classmethod
    def _source_not_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("every figure requires a non-empty source")
        return value.strip()

    @model_validator(mode="after")
    def _range_is_ordered_and_non_negative(self) -> "Figure":
        if self.low < 0:
            raise ValueError("figure low must be non-negative")
        if self.high < self.low:
            raise ValueError("figure high must be greater than or equal to low")
        return self

    def echo(self) -> dict[str, Any]:
        return {"low": self.low, "high": self.high, "unit": self.unit, "source": self.source}


class VesselGroup(BaseModel):
    """A dedicated group of vessels with payload and cycle-time figures."""

    name: str = Field(min_length=1)
    vessels: Figure
    payload_tonnes_per_departure: Figure
    cycle_hours: Figure
    operating_days_per_year: Figure

    @model_validator(mode="after")
    def _cycle_time_non_zero(self) -> "VesselGroup":
        if self.cycle_hours.low <= 0:
            raise ValueError(f"{self.name}: cycle_hours low must be positive")
        return self


class InterfaceConstraint(BaseModel):
    """A port, railway, terminal or wagon allocation limiting throughput."""

    name: str = Field(min_length=1)
    tonnes_per_year: Figure


class CapacityScenario(BaseModel):
    """The caller's full capacity question: vessel groups plus interfaces."""

    name: str = ""
    route: str = ""
    vessel_groups: list[VesselGroup] = Field(min_length=1)
    interface_constraints: list[InterfaceConstraint] = Field(default_factory=list)


def _round(value: float) -> float:
    return round(value, 1)


def _group_capacity(group: VesselGroup) -> dict[str, Any]:
    departures_low = (
        group.operating_days_per_year.low * HOURS_PER_DAY / group.cycle_hours.high
    )
    departures_high = (
        group.operating_days_per_year.high * HOURS_PER_DAY / group.cycle_hours.low
    )
    capacity_low = group.vessels.low * group.payload_tonnes_per_departure.low * departures_low
    capacity_high = group.vessels.high * group.payload_tonnes_per_departure.high * departures_high
    return {
        "name": group.name,
        "inputs": {
            "vessels": group.vessels.echo(),
            "payload_tonnes_per_departure": group.payload_tonnes_per_departure.echo(),
            "cycle_hours": group.cycle_hours.echo(),
            "operating_days_per_year": group.operating_days_per_year.echo(),
        },
        "departures_per_vessel_per_year": {
            "low": _round(departures_low),
            "high": _round(departures_high),
        },
        "capacity_tonnes_per_year": {
            "low": _round(capacity_low),
            "high": _round(capacity_high),
        },
    }


def estimate_capacity(scenario: CapacityScenario) -> dict[str, Any]:
    """Combine caller-supplied figures into a capacity range. Adds nothing."""
    groups = [_group_capacity(group) for group in scenario.vessel_groups]
    fleet_low = sum(g["capacity_tonnes_per_year"]["low"] for g in groups)
    fleet_high = sum(g["capacity_tonnes_per_year"]["high"] for g in groups)

    candidates_low: list[tuple[str, float]] = [("fleet", fleet_low)]
    candidates_high: list[tuple[str, float]] = [("fleet", fleet_high)]
    interfaces = []
    for constraint in scenario.interface_constraints:
        interfaces.append(
            {"name": constraint.name, "tonnes_per_year": constraint.tonnes_per_year.echo()}
        )
        candidates_low.append((constraint.name, constraint.tonnes_per_year.low))
        candidates_high.append((constraint.name, constraint.tonnes_per_year.high))

    binding_low, usable_low = min(candidates_low, key=lambda item: item[1])
    binding_high, usable_high = min(candidates_high, key=lambda item: item[1])

    return {
        "status": ESTIMATE,
        "tool": "estimate_caspian_capacity",
        "result_is_not_a_finding": True,
        "human_review_required": True,
        "scenario": {"name": scenario.name, "route": scenario.route},
        "vessel_groups": groups,
        "fleet_capacity_tonnes_per_year": {"low": _round(fleet_low), "high": _round(fleet_high)},
        "interface_constraints": interfaces,
        "usable_throughput_tonnes_per_year": {
            "low": _round(usable_low),
            "high": _round(usable_high),
        },
        "binding_constraint": {"low": binding_low, "high": binding_high},
        "arithmetic_assumptions": ARITHMETIC_ASSUMPTIONS,
        "detail": (
            "Deterministic arithmetic over caller-supplied figures only. Every "
            "input number carries the source the caller stated; the tool adds "
            "no data and does not check whether inputs are current. This is "
            "not a finding about current Caspian operations."
        ),
    }


def estimate_capacity_json(arguments: dict[str, Any]) -> str:
    """Tool entry point: validate, estimate, and serialize. Never raises."""
    try:
        scenario = CapacityScenario.model_validate(arguments)
    except ValueError as exc:
        return json.dumps(
            {
                "status": INVALID_INPUT,
                "tool": "estimate_caspian_capacity",
                "detail": f"Invalid scenario: {exc}. No defaults were substituted; "
                "supply every figure with its source.",
                "result_is_not_a_finding": True,
                "human_review_required": True,
            }
        )
    return json.dumps(estimate_capacity(scenario))
