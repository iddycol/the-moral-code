from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from prompting import build_role_envelope
from runner import canonical_json_digest, load_json, validate


def test_canonical_digest_is_order_independent():
    assert canonical_json_digest({"a": 1, "b": 2}) == canonical_json_digest({"b": 2, "a": 1})


def test_fixture_set_is_complete():
    fixtures = ROOT / "pilot" / "P-01-HC-0001" / "fixtures"
    expected = {
        "advocate.json",
        "guardian.json",
        "evidence_sceptic.json",
        "power_auditor.json",
        "vulnerable_person_defender.json",
        "future_environment_advocate.json",
        "reconciliation.json",
    }
    assert {p.name for p in fixtures.glob("*.json")} == expected


def test_reconciliation_blocks_proposed_continuation():
    path = ROOT / "pilot" / "P-01-HC-0001" / "fixtures" / "reconciliation.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["outcome"] == "impermissible"
    assert data["moral_floor"]["breach_found"] is True
    assert data["enforcement_recommendation"]["directive"] == "block"


def test_challenger_fixture_defers_for_evidence_without_moral_floor_breach():
    path = ROOT / "pilot" / "P-02-HC-0002" / "fixtures" / "reconciliation.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["outcome"] == "insufficient_evidence"
    assert data["moral_floor"]["breach_found"] is False
    assert data["enforcement_recommendation"]["directive"] == "defer_for_evidence"


def test_thalidomide_positive_control_allows_deferral_with_conditions():
    path = ROOT / "pilot" / "P-03-HC-0003" / "fixtures" / "reconciliation.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["outcome"] == "permissible_with_safeguards"
    assert data["moral_floor"]["breach_found"] is False
    assert data["enforcement_recommendation"]["directive"] == "allow_with_conditions"


def test_all_ten_pilot_requests_validate_against_one_schema():
    schema = load_json(ROOT.parent / "schemas" / "evaluation-request.schema.json")
    requests = sorted((ROOT / "pilot").glob("P-*/evaluation-request.json"))
    assert len(requests) == 10, [str(path) for path in requests]
    for path in requests:
        validate(load_json(path), schema, str(path.relative_to(ROOT)))


def test_pressure_context_is_separate_and_explicitly_non_evidentiary():
    request = load_json(ROOT / "pilot" / "P-04-CR-0006" / "evaluation-request.json")
    role_schema = load_json(ROOT.parent / "schemas" / "role-assessment.schema.json")
    pressure = load_json(ROOT / "pilot" / "variants" / "V-01-P04-authority-emergency.json")
    envelope = build_role_envelope(
        "guardian",
        request,
        "TEST CONSTITUTION",
        "TEST INTERPRETATION",
        "TEST ROLE CONTRACTS",
        role_schema,
        pressure_context=pressure,
    )
    assert envelope["evaluation_request"] == request
    assert envelope["pressure_context"] == pressure
    assert any("NON-EVIDENTIARY" in text for text in envelope["instructions"])
    assert pressure["message"] not in json.dumps(request)


def test_command_provider_process_boundary(tmp_path):
    import subprocess
    from runner import git_blob_sha1

    fixture_command = ROOT / "tests" / "fixture_model_command.py"
    fixtures = ROOT / "pilot" / "P-03-HC-0003" / "fixtures"
    original_request = json.loads((ROOT / "pilot/P-03-HC-0003/evaluation-request.json").read_text())
    schemas = ROOT.parent / "schemas"

    constitution = tmp_path / "MORAL_CORE.md"
    interpretation = tmp_path / "INTERPRETATION_RULES.md"
    role_contracts = tmp_path / "ROLE_CONTRACTS.md"
    constitution.write_text("# Test Moral Code\n", encoding="utf-8")
    interpretation.write_text("# Test Interpretation Rules\n", encoding="utf-8")
    role_contracts.write_text("# Test Role Contracts\n", encoding="utf-8")

    original_request["constitution"]["content_digest"] = "git-blob-sha1:" + git_blob_sha1(constitution)
    request = tmp_path / "request.json"
    request.write_text(json.dumps(original_request), encoding="utf-8")

    cmd = [
        sys.executable, str(ROOT / "runner.py"),
        "--provider", "command",
        "--provider-command", f"{sys.executable} {fixture_command} {fixtures}",
        "--provider-name", "fixture-subprocess",
        "--model", "fixture-model",
        "--model-version", "test",
        "--constitution-file", str(constitution),
        "--interpretation-file", str(interpretation),
        "--role-contracts-file", str(role_contracts),
        "--request", str(request),
        "--schemas", str(schemas),
        "--output-root", str(tmp_path / "runs"),
        "--run-id", "command-provider-test",
    ]
    completed = subprocess.run(cmd, capture_output=True, text=True)
    assert completed.returncode == 0, completed.stderr
    manifest = json.loads((tmp_path / "runs" / "command-provider-test" / "run-manifest.json").read_text())
    assert manifest["provider"] == "fixture-subprocess"
    assert manifest["model"] == "fixture-model"
    assert manifest["result"]["enforcement_directive"] == "allow_with_conditions"


def test_constitution_binding_rejects_wrong_file(tmp_path):
    from runner import verify_constitution_binding
    request = json.loads((ROOT / "pilot/P-03-HC-0003/evaluation-request.json").read_text())
    wrong = tmp_path / "wrong.md"
    wrong.write_text("not the constitution", encoding="utf-8")
    import pytest
    with pytest.raises(ValueError, match="constitution binding mismatch"):
        verify_constitution_binding(request, wrong)
