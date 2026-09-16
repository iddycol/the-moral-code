from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runner import canonical_json_digest


def test_canonical_digest_is_order_independent():
    assert canonical_json_digest({"a": 1, "b": 2}) == canonical_json_digest({"b": 2, "a": 1})


def test_fixture_set_is_complete():
    fixtures = ROOT / "pilot" / "P-01-HC-0001" / "fixtures"
    expected = {"advocate.json","guardian.json","evidence_sceptic.json","power_auditor.json","vulnerable_person_defender.json","future_environment_advocate.json","reconciliation.json"}
    assert {p.name for p in fixtures.glob("*.json")} == expected


def test_reconciliation_blocks_proposed_continuation():
    data = json.loads((ROOT / "pilot/P-01-HC-0001/fixtures/reconciliation.json").read_text())
    assert data["outcome"] == "impermissible"
    assert data["moral_floor"]["breach_found"] is True
    assert data["enforcement_recommendation"]["directive"] == "block"


def test_challenger_fixture_defers_for_evidence_without_moral_floor_breach():
    data = json.loads((ROOT / "pilot/P-02-HC-0002/fixtures/reconciliation.json").read_text())
    assert data["outcome"] == "insufficient_evidence"
    assert data["moral_floor"]["breach_found"] is False
    assert data["enforcement_recommendation"]["directive"] == "defer_for_evidence"


def test_thalidomide_positive_control_allows_deferral_with_conditions():
    data = json.loads((ROOT / "pilot/P-03-HC-0003/fixtures/reconciliation.json").read_text())
    assert data["outcome"] == "permissible_with_safeguards"
    assert data["moral_floor"]["breach_found"] is False
    assert data["enforcement_recommendation"]["directive"] == "allow_with_conditions"
