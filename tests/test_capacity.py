"""Tests for the deterministic Caspian capacity estimator.

The estimator's contract: it combines caller-supplied figures into a low/high
range, names the binding constraint, echoes every input with its source, and
never substitutes a default for a missing or source-less figure.
"""

import json
import unittest

from central_asia_caspian_compliance_server.capacity import estimate_capacity_json


def figure(low, high, source="caller-supplied test figure", unit=""):
    return {"low": low, "high": high, "source": source, "unit": unit}


def scenario(**overrides):
    base = {
        "name": "test scenario",
        "route": "Baku-Aktau",
        "vessel_groups": [
            {
                "name": "train ferries",
                "vessels": figure(2, 2),
                "payload_tonnes_per_departure": figure(3000, 4000, unit="t"),
                "cycle_hours": figure(96, 120, unit="h"),
                "operating_days_per_year": figure(300, 330, unit="d"),
            }
        ],
        "interface_constraints": [
            {
                "name": "Aktau rail allocation",
                "tonnes_per_year": figure(500_000, 600_000, unit="t"),
            }
        ],
    }
    base.update(overrides)
    return base


class CapacityEstimateTests(unittest.TestCase):
    def test_known_scenario_computes_exact_range(self):
        payload = json.loads(estimate_capacity_json(scenario()))
        self.assertEqual(payload["status"], "estimate")
        # low: 2 * 3000 * (300*24 / 120) = 360_000
        # high: 2 * 4000 * (330*24 / 96) = 660_000
        group = payload["vessel_groups"][0]
        self.assertEqual(group["capacity_tonnes_per_year"]["low"], 360_000)
        self.assertEqual(group["capacity_tonnes_per_year"]["high"], 660_000)
        self.assertEqual(payload["fleet_capacity_tonnes_per_year"]["low"], 360_000)

    def test_binding_constraint_tracks_the_minimum(self):
        payload = json.loads(estimate_capacity_json(scenario()))
        # low side: fleet 360k binds under the 1M interface; high side: interface binds.
        self.assertEqual(payload["usable_throughput_tonnes_per_year"]["low"], 360_000)
        self.assertEqual(payload["binding_constraint"]["low"], "fleet")
        self.assertEqual(payload["usable_throughput_tonnes_per_year"]["high"], 600_000)
        self.assertEqual(payload["binding_constraint"]["high"], "Aktau rail allocation")

    def test_every_input_is_echoed_with_its_source(self):
        payload = json.loads(estimate_capacity_json(scenario()))
        inputs = payload["vessel_groups"][0]["inputs"]
        for key in ("vessels", "payload_tonnes_per_departure", "cycle_hours", "operating_days_per_year"):
            self.assertEqual(inputs[key]["source"], "caller-supplied test figure")
        self.assertEqual(
            payload["interface_constraints"][0]["tonnes_per_year"]["source"],
            "caller-supplied test figure",
        )

    def test_result_is_never_a_finding(self):
        payload = json.loads(estimate_capacity_json(scenario()))
        self.assertTrue(payload["result_is_not_a_finding"])
        self.assertTrue(payload["human_review_required"])
        self.assertNotIn("probability", json.dumps(payload).lower())

    def test_missing_source_is_rejected_not_defaulted(self):
        bad = scenario()
        bad["vessel_groups"][0]["payload_tonnes_per_departure"] = {"low": 3000, "high": 4000}
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")
        self.assertTrue(payload["result_is_not_a_finding"])

    def test_blank_source_is_rejected(self):
        bad = scenario()
        bad["vessel_groups"][0]["vessels"] = figure(2, 2, source="   ")
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")

    def test_inverted_range_is_rejected(self):
        bad = scenario()
        bad["vessel_groups"][0]["cycle_hours"] = figure(120, 96)
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")

    def test_zero_cycle_time_is_rejected(self):
        bad = scenario()
        bad["vessel_groups"][0]["cycle_hours"] = figure(0, 0)
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")

    def test_negative_figure_is_rejected(self):
        bad = scenario()
        bad["vessel_groups"][0]["operating_days_per_year"] = figure(-5, 10)
        payload = json.loads(estimate_capacity_json(bad))
        self.assertEqual(payload["status"], "invalid_input")

    def test_no_interface_constraints_means_fleet_binds(self):
        payload = json.loads(estimate_capacity_json(scenario(interface_constraints=[])))
        self.assertEqual(payload["binding_constraint"], {"low": "fleet", "high": "fleet"})

    def test_output_is_deterministic(self):
        self.assertEqual(estimate_capacity_json(scenario()), estimate_capacity_json(scenario()))


if __name__ == "__main__":
    unittest.main()
