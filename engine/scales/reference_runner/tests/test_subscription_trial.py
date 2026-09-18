"""Integrity checks using a fake CLI only; these are not model evidence."""
import argparse
import copy
import json
from pathlib import Path
import sys

import pytest

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import subscription_trial as trial


@pytest.fixture
def pack(tmp_path):
    return trial.freeze(tmp_path / "pack.json")


def test_committed_pack_matches_the_checked_out_sources():
    pack = trial.load_pack(trial.PACK)
    assert set(pack["cases"]) == {f"CORE-{number:02d}" for number in range(1, 13)}


def test_frozen_pack_contains_all_twelve_and_excludes_reveals(pack, tmp_path):
    assert len(pack["cases"]) == 12
    assert sum(case["mode"] == "repair" for case in pack["cases"].values()) == 2
    assert not any("reveal" in name or "transparent" in name or "/fixtures/" in name for name in pack["source_hashes"])
    for case in pack["cases"].values():
        for role in trial.roles_for(case):
            envelope = trial.envelope_for(pack, case, role)
            assert "role_assessments" not in envelope
            assert envelope["role"] == role
    path = tmp_path / "pack.json"
    data = json.loads(path.read_text())
    data["common"]["constitution"] = "tampered"
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="digest mismatch"):
        trial.load_pack(path)


def fake_cli(tmp_path):
    script = tmp_path / "fake cli.py"
    script.write_text(r'''
import json, pathlib, sys
text = sys.stdin.read()
envelope = json.loads(text[text.index("{"):])
repair = envelope["task"].startswith("repair_")
role = envelope.get("role")
is_role = "role_assessment" in envelope["task"]
key = "repair_case_id" if repair else "evaluation_id"
case_id = envelope["repair_packet"][key] if repair else envelope["evaluation_request"][key]
value = {key: case_id}
if is_role:
    value.update(role=role, role_contract_version="0.1", findings=[], principle_assessments=[])
    if repair:
        value.update(component_assessments=[], failure_risks=[], recommended_components=[])
    else:
        value["recommended_disposition"] = "insufficient_evidence"
else:
    supplied = envelope.get("constitution_binding", envelope.get("evaluation_request", {}).get("constitution"))
    # Model the live failure: emit only the fields declared by the output schema.
    declared = envelope["output_schema"]["properties"]["constitution"]["properties"]
    binding = {key: supplied[key] for key in declared if key in supplied}
    value.update(constitution=binding,
                 role_assessment_refs=envelope["required_role_assessment_refs"], outcome="insufficient_evidence")
    if repair:
        value.update(harm_assessment=[], component_decisions=[], failure_checks=[],
                     victim_agency={"status":"uncertain", "reason":"test fixture"},
                     responsibility_model={"institutional_responsibility":"test", "individual_responsibility":"test", "inherited_personal_guilt":"rejected"},
                     irreparable_losses=[], package_summary="TEST FIXTURE ONLY",
                     implementation_recommendation={"directive":"defer_for_evidence", "reason":"test"})
    else:
        value.update(moral_floor={"breach_found":False,"checks":[]}, principle_assessments=[],
                     reasoning_summary="TEST FIXTURE ONLY", enforcement_recommendation={"directive":"defer_for_evidence", "reason":"test"})
response = json.dumps(value)
if "--output-last-message" in sys.argv:
    path = sys.argv[sys.argv.index("--output-last-message") + 1]
    pathlib.Path(path).write_text(response)
    print(json.dumps({"type":"item.completed", "item":{"type":"agent_message", "text":response}}))
    print(json.dumps({"type":"turn.completed"}))
else:
    print(json.dumps({"type":"result", "subtype":"success", "is_error":False, "result":response}))
''', encoding="utf-8")
    return str(script)


@pytest.mark.parametrize("case_id", ["CORE-01", "CORE-11"])
def test_seven_fresh_calls_and_verified_comparison(pack, tmp_path, monkeypatch, case_id):
    cli = fake_cli(tmp_path)
    monkeypatch.setattr(trial, "preflight", lambda provider: (cli, "TEST FIXTURE CLI"))
    # Use the active Python interpreter on every OS; Windows cannot exec a shebang.
    build_command = trial.cli_command
    monkeypatch.setattr(trial, "cli_command", lambda *args: [sys.executable, *build_command(*args)])
    paths = []
    for provider in ("codex", "claude"):
        args = argparse.Namespace(pack=tmp_path / "pack.json", case=case_id, provider=provider,
                                  model="TEST FIXTURE", output_root=tmp_path / "runs", run_id=provider, timeout=10)
        assert trial.run_trial(args) == 0
        path = args.output_root / provider
        paths.append(path)
        raw = path / case_id / "raw"
        assert len(list(raw.glob("*/prompt.txt"))) == 7
        assert len(list(raw.glob("*/stdout.jsonl"))) == 7
        for role in trial.roles_for(pack["cases"][case_id]):
            assert "role_assessments" not in json.loads((raw / role / "envelope.json").read_text())
    report = trial.compare_trials(pack, *paths, tmp_path / "comparison.json")
    assert report["comparable_pairs"] == 1
    decision = paths[0] / case_id / "decision.json"
    data = json.loads(decision.read_text())
    data["outcome"] = "unresolved_conflict"
    decision.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="decision digest mismatch"):
        trial.compare_trials(pack, *paths, tmp_path / "corrupt-comparison.json")


@pytest.mark.parametrize("case_id", ["CORE-01", "CORE-11"])
def test_reconciliation_schema_requires_the_complete_explicit_binding(pack, case_id):
    before = copy.deepcopy(pack)
    case = pack["cases"][case_id]
    envelope = trial.envelope_for(pack, case, assessments={})
    binding = pack["constitution_binding"]
    schema = envelope["output_schema"]["properties"]["constitution"]
    assert set(binding) <= set(schema["properties"])
    assert set(binding) <= set(schema["required"])
    assert envelope["constitution_binding"] == binding
    assert schema["const"] == binding
    validator = trial.Draft202012Validator(schema)
    validator.validate(binding)
    for field in binding:
        omitted = {key: value for key, value in binding.items() if key != field}
        altered = dict(binding, **{field: "wrong binding"})
        assert not validator.is_valid(omitted), field
        assert not validator.is_valid(altered), field
    assert pack == before, "building an envelope must not mutate the frozen pack"


@pytest.mark.parametrize("mode", ["action", "repair"])
def test_wrong_role_or_constitution_is_rejected_without_rewriting(pack, mode):
    case = pack["cases"]["CORE-01" if mode == "action" else "CORE-11"]
    role = trial.roles_for(case)[0]
    key = "evaluation_id" if mode == "action" else "repair_case_id"
    value = {key: case["input"][key], "role": trial.roles_for(case)[1], "role_contract_version":"0.1",
             "findings": [], "principle_assessments": [], "recommended_disposition": "insufficient_evidence"}
    if mode == "repair":
        value.update(component_assessments=[], failure_risks=[], recommended_components=[])
    before = copy.deepcopy(value)
    with pytest.raises(ValueError, match="different role"):
        trial.check_response(value, pack, case, trial.envelope_for(pack, case, role), role)
    assert value == before


def test_missing_access_is_saved_without_inference(pack, tmp_path, monkeypatch):
    monkeypatch.setattr(trial.shutil, "which", lambda name: None)
    args = argparse.Namespace(pack=tmp_path / "pack.json", case="CORE-01", provider="claude", model=None,
                              output_root=tmp_path / "runs", run_id="missing", timeout=10)
    assert trial.run_trial(args) == 1
    manifest = json.loads((args.output_root / args.run_id / "trial-manifest.json").read_text())
    assert manifest["failure_type"] == "access_unavailable"
    assert manifest["inference_attempted"] is False


def test_invalid_answer_is_retained_and_tool_use_is_disqualified(tmp_path):
    response = tmp_path / "response.txt"
    raw = json.dumps({"type":"result", "subtype":"success", "is_error":False, "result":"not json"})
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("claude", raw, response)
    assert exc.value.category == "response_format_failure"
    assert response.read_text() == "not json"
    raw = json.dumps({"type":"item.completed", "item":{"type":"command_execution", "command":"read outside facts"}})
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("codex", raw, response)
    assert exc.value.category == "protocol_contamination"
