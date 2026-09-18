"""Integrity checks using a fake CLI only; these are not model evidence."""
import argparse
import copy
import hashlib
import json
import locale
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
import json, os, pathlib, sys
text = sys.stdin.buffer.read().decode("utf-8", errors="strict")
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
                     reasoning_summary="TEST FIXTURE ONLY \u2014 caf\u00e9 \u4e2d\u6587 \U0001f600", enforcement_recommendation={"directive":"defer_for_evidence", "reason":"test"})
response = json.dumps(value, ensure_ascii=False)
def emit(event):
    sys.stdout.buffer.write((json.dumps(event, ensure_ascii=False) + "\n").encode("utf-8"))
if "--output-last-message" in sys.argv:
    path = sys.argv[sys.argv.index("--output-last-message") + 1]
    pathlib.Path(path).write_bytes(response.encode("utf-8"))
    emit({"type":"item.completed", "item":{"type":"agent_message", "text":response}})
    emit({"type":"turn.completed"})
else:
    if os.environ.get("SCALES_TEST_CONTAMINATED"):
        # Valid role JSON must still fail at the real subprocess intake boundary.
        emit({"type":"user", "isSynthetic":True,
              "message":{"role":"user", "content":"Unexpected instruction"}})
    emit({"type":"result", "subtype":"success", "is_error":False,
          "num_turns":1, "result":response})
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
    data = json.loads(decision.read_text(encoding="utf-8"))
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
    raw = json.dumps({"type":"result", "subtype":"success", "is_error":False,
                      "num_turns":1, "result":"not json"})
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("claude", raw, response)
    assert exc.value.category == "response_format_failure"
    assert response.read_text() == "not json"
    raw = json.dumps({"type":"item.completed", "item":{"type":"command_execution", "command":"read outside facts"}})
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("codex", raw, response)
    assert exc.value.category == "protocol_contamination"


def claude_stream(response, preceding=(), **result_fields):
    result = {"type": "result", "subtype": "success", "is_error": False,
              "num_turns": 1, "result": response}
    result.update(result_fields)
    return "\n".join(json.dumps(event) for event in [*preceding, result]) + "\n"


def test_claude_single_turn_with_multiple_blocks_in_one_message(tmp_path):
    response = '{\n  "answer": "caf\u00e9"\n}\n'
    blocks = [
        {"type": "assistant", "message": {"id": "one-message", "role": "assistant",
         "content": [{"type": "thinking", "thinking": "fixture"}]}},
        {"type": "assistant", "message": {"id": "one-message", "role": "assistant",
         "content": [{"type": "text", "text": response}]}},
    ]
    path = tmp_path / "response.txt"
    assert trial.parse_cli_output("claude", claude_stream(response, blocks), path) == {"answer": "caf\u00e9"}
    assert path.read_bytes() == response.encode("utf-8")


@pytest.mark.parametrize("metadata", [{"isSynthetic": True}, {"isSynthetic": False}, {}])
@pytest.mark.parametrize("response", ['{\n"answer": "caf\u00e9"\n}\n', '{}\nTrailing prose'])
def test_claude_unsolicited_user_precedes_json_acceptance(tmp_path, metadata, response):
    # No classifier phrase, and a misleading one-turn count must not allow it.
    user = {"type": "user", "message": {"role": "user", "content": "Unexpected instruction"}, **metadata}
    path = tmp_path / "response.txt"
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("claude", claude_stream(response, [user]), path)
    assert exc.value.category == "protocol_contamination"
    assert "user" in str(exc.value)
    assert path.read_bytes() == response.encode("utf-8")


@pytest.mark.parametrize("response", ['{\n"answer": "caf\u00e9"\n}\n', '{}\nTrailing prose'])
def test_claude_multiple_turns_without_user_event(tmp_path, response):
    path = tmp_path / "response.txt"
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("claude", claude_stream(response, num_turns=2), path)
    assert exc.value.category == "protocol_contamination"
    assert "num_turns" in str(exc.value)
    assert path.read_bytes() == response.encode("utf-8")


@pytest.mark.parametrize("count", [None, True, False, "1", "2", 0, -1, 1.0, 2.0, [], {}])
def test_claude_unverifiable_turn_count_fails_closed(tmp_path, count):
    response = '{\n"answer": "caf\u00e9"\n}\n'
    path = tmp_path / "response.txt"
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("claude", claude_stream(response, num_turns=count), path)
    assert exc.value.category == "client_output_error"
    assert "num_turns" in str(exc.value)
    assert path.read_bytes() == response.encode("utf-8")


def test_claude_missing_turn_count_fails_closed(tmp_path):
    event = json.loads(claude_stream("{}"))
    del event["num_turns"]
    path = tmp_path / "response.txt"
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("claude", json.dumps(event), path)
    assert exc.value.category == "client_output_error"
    assert "num_turns" in str(exc.value) and "missing" in str(exc.value)
    assert path.read_text() == "{}"


def test_clean_claude_trailing_prose_is_not_repaired(tmp_path):
    response = '{}\nTrailing prose'
    path = tmp_path / "response.txt"
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("claude", claude_stream(response), path)
    assert exc.value.category == "response_format_failure"
    assert path.read_bytes() == response.encode("utf-8")


def test_claude_tool_rejection_retains_final_text(tmp_path):
    tool = {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "Read"}]}}
    response = '{\n"answer": "caf\u00e9"\n}\n'
    path = tmp_path / "response.txt"
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("claude", claude_stream(response, [tool]), path)
    assert exc.value.category == "protocol_contamination"
    assert path.read_bytes() == response.encode("utf-8")


@pytest.mark.parametrize("result_fields", [{"subtype": "error"}, {"is_error": True}])
def test_claude_still_requires_successful_result(tmp_path, result_fields):
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("claude", claude_stream("{}", **result_fields), tmp_path / "response.txt")
    assert exc.value.category == "client_or_provider_error"


def test_contaminated_fake_claude_retains_evidence_and_stops_all_cases(pack, tmp_path, monkeypatch):
    cli = fake_cli(tmp_path)
    monkeypatch.setattr(trial, "preflight", lambda provider: (cli, "TEST FIXTURE CLI"))
    build_command = trial.cli_command
    monkeypatch.setattr(trial, "cli_command", lambda *args: [sys.executable, *build_command(*args)])
    monkeypatch.setenv("SCALES_TEST_CONTAMINATED", "1")
    args = argparse.Namespace(pack=tmp_path / "pack.json", case="all", provider="claude",
                              model="TEST FIXTURE", output_root=tmp_path / "runs", run_id="contaminated", timeout=10)
    assert trial.run_trial(args) == 1
    run = args.output_root / args.run_id
    manifest = json.loads((run / "trial-manifest.json").read_text())
    assert manifest["status"] == "failed"
    assert manifest["failure_type"] == "protocol_contamination"
    assert "user" in manifest["detail"]
    assert manifest["inference_attempted"] is True  # fake subprocess only
    row = manifest["cases"]["CORE-01"]
    assert row["status"] == "failed" and row["stage"] == "advocate"
    assert row["failure_type"] == "protocol_contamination"
    assert all(row["status"] == "not_started" for key, row in manifest["cases"].items() if key != "CORE-01")
    raw = run / "CORE-01" / "raw" / "advocate"
    events = [json.loads(line) for line in (raw / "stdout.jsonl").read_text().splitlines()]
    assert events[0]["type"] == "user" and events[0]["isSynthetic"] is True
    assert events[-1]["num_turns"] == 1
    assert (raw / "response.txt").read_bytes() == events[-1]["result"].encode("utf-8")
    assert json.loads((raw / "exit.json").read_text()) == {"returncode": 0}
    assert (raw / "stderr.txt").exists()
    assert len(list(run.glob("*/raw/*/invocation.json"))) == 1
    assert len(list(run.glob("*/raw/*/stdout.jsonl"))) == 1
    assert not list(run.glob("*/role-assessments"))
    assert not list(run.glob("*/decision.json"))
    assert not list(run.glob("*/raw/reconciliation"))


WIRE_TEXT = "caf\u00e9 \u2014 \u201ccurly\u201d \u4e2d\u6587 \U0001f600"
WIRE_STDERR = (WIRE_TEXT + "\r\n").encode("utf-8") + b"\xff\n"


def strict_transport_cli(tmp_path, monkeypatch, mode="success"):
    """Real child process with byte capture and a locale-independent UTF-8 contract."""
    script = tmp_path / "strict transport client.py"
    script.write_text(r'''
import json, pathlib, sys, time
script = pathlib.Path(__file__)
mode = sys.argv[1]
with script.with_suffix(".calls").open("ab") as calls:
    calls.write(b"called\n")
raw = sys.stdin.buffer.read()
script.with_suffix(".stdin.bin").write_bytes(raw)
text = raw.decode("utf-8", errors="strict")
envelope = json.loads(text[text.index("{"):])
unicode_text = "caf\u00e9 \u2014 \u201ccurly\u201d \u4e2d\u6587 \U0001f600"
sys.stderr.buffer.write((unicode_text + "\r\n").encode("utf-8") + b"\xff\n")
sys.stderr.buffer.flush()
if mode in ("nonzero", "timeout"):
    sys.stdout.buffer.write((unicode_text + "\r\n").encode("utf-8") + b"\xfe\n")
    sys.stdout.buffer.flush()
    if mode == "timeout":
        time.sleep(30)
    sys.exit(23)
response = json.dumps({"echo": envelope, "unicode": unicode_text}, ensure_ascii=False)
if "--output-last-message" in sys.argv:
    path = pathlib.Path(sys.argv[sys.argv.index("--output-last-message") + 1])
    path.write_bytes(b"\xff" if mode == "invalid_response" else response.encode("utf-8"))
    events = [{"type":"item.completed", "item":{"type":"agent_message", "text":response}},
              {"type":"turn.completed"}]
else:
    events = [{"type":"result", "subtype":"success", "is_error":False,
               "num_turns":1, "result":response}]
output = b"\xff" if mode == "invalid_events" else b"".join(
    (json.dumps(event, ensure_ascii=False) + "\r\n").encode("utf-8") for event in events)
script.with_suffix(".stdout.bin").write_bytes(output)
sys.stdout.buffer.write(output)
''', encoding="utf-8")
    build_command = trial.cli_command
    monkeypatch.setattr(trial, "cli_command", lambda *args: [
        sys.executable, "-X", "utf8=0", str(script), mode, *build_command(*args)[1:]
    ])
    return script


@pytest.mark.parametrize("provider", ["codex", "claude"])
@pytest.mark.parametrize("payload", ["historical", "beyond_cp1252"])
@pytest.mark.parametrize("encoding_default", ["native", "cp1252"])
def test_invoke_utf8_wire_bytes(tmp_path, monkeypatch, provider, payload, encoding_default):
    historical = HERE / "subscription-runs/CODEX-V012-CORE01-20260918T204353Z/CORE-01/raw/advocate/envelope.json"
    envelope = json.loads(historical.read_text(encoding="utf-8"))
    assert "\u2014" in json.dumps(envelope, ensure_ascii=False)
    if payload == "beyond_cp1252":
        # Temporary transport-only fixture; never edit the historical envelope.
        envelope["transport_test_text"] = WIRE_TEXT
    native_encoding = trial.subprocess._text_encoding()
    if encoding_default == "cp1252":
        # Supplemental portable simulation; subprocess.run and the child stay real.
        monkeypatch.setattr(trial.subprocess, "_text_encoding", lambda: "cp1252")
    facts = {"platform": sys.platform, "utf8_mode": sys.flags.utf8_mode,
             "locale_encoding": locale.getencoding(), "native_default": native_encoding,
             "tested_default": trial.subprocess._text_encoding(), "mode": encoding_default}
    (tmp_path / "parent-encoding.json").write_text(json.dumps(facts), encoding="utf-8")
    if encoding_default == "cp1252":
        assert facts["tested_default"] == "cp1252"
    script = strict_transport_cli(tmp_path, monkeypatch)
    target = tmp_path / "evidence"
    value = trial.invoke(str(script), provider, "TEST FIXTURE", envelope, target, 10)
    expected = (trial.PROMPT_PREFIX + json.dumps(envelope, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    captured = script.with_suffix(".stdin.bin").read_bytes()
    assert captured == (target / "prompt.txt").read_bytes() == expected
    assert b"\r\n" not in captured and captured.endswith(b"\n")
    invocation = json.loads((target / "invocation.json").read_text(encoding="utf-8"))
    assert invocation["prompt_digest"] == "sha256:" + hashlib.sha256(captured).hexdigest()
    assert value == {"echo": envelope, "unicode": WIRE_TEXT}
    assert (target / "stdout.jsonl").read_bytes() == script.with_suffix(".stdout.bin").read_bytes()
    assert WIRE_TEXT.encode("utf-8") in (target / "stdout.jsonl").read_bytes()
    assert (target / "stderr.txt").read_bytes() == WIRE_STDERR
    assert json.loads((target / "response.txt").read_bytes().decode("utf-8")) == value
    assert script.with_suffix(".calls").read_bytes() == b"called\n"


@pytest.mark.parametrize("provider", ["codex", "claude"])
@pytest.mark.parametrize("mode, category", [("nonzero", "client_or_provider_error"), ("timeout", "client_timeout")])
def test_transport_failure_retains_bytes_and_stops(pack, tmp_path, monkeypatch, provider, mode, category):
    script = strict_transport_cli(tmp_path, monkeypatch, mode)
    monkeypatch.setattr(trial, "preflight", lambda provider: (str(script), "TEST FIXTURE CLI"))
    args = argparse.Namespace(pack=tmp_path / "pack.json", case="all", provider=provider,
                              model="TEST FIXTURE", output_root=tmp_path / "runs", run_id=mode, timeout=1)
    assert trial.run_trial(args) == 1
    run = args.output_root / args.run_id
    manifest = json.loads((run / "trial-manifest.json").read_text(encoding="utf-8"))
    assert manifest["failure_type"] == category
    assert manifest["cases"]["CORE-01"]["stage"] == "advocate"
    assert all(row["status"] == "not_started" for key, row in manifest["cases"].items() if key != "CORE-01")
    raw = run / "CORE-01/raw/advocate"
    assert (raw / "stdout.jsonl").read_bytes() == (WIRE_TEXT + "\r\n").encode("utf-8") + b"\xfe\n"
    assert (raw / "stderr.txt").read_bytes() == WIRE_STDERR
    assert script.with_suffix(".stdin.bin").read_bytes() == (raw / "prompt.txt").read_bytes()
    if mode == "nonzero":
        assert json.loads((raw / "exit.json").read_text()) == {"returncode": 23}
    assert len(list(run.glob("*/raw/*/invocation.json"))) == 1
    assert script.with_suffix(".calls").read_bytes() == b"called\n"
    assert not list(run.glob("*/role-assessments")) and not list(run.glob("*/decision.json"))
    assert not list(run.glob("*/raw/reconciliation"))


@pytest.mark.parametrize("provider, mode", [("codex", "invalid_events"), ("claude", "invalid_events"), ("codex", "invalid_response")])
def test_transport_rejects_invalid_utf8_without_rewriting(tmp_path, monkeypatch, provider, mode):
    script = strict_transport_cli(tmp_path, monkeypatch, mode)
    target = tmp_path / "evidence"
    with pytest.raises(UnicodeDecodeError):
        trial.invoke(str(script), provider, "TEST FIXTURE", {"test": "ASCII input"}, target, 10)
    invalid_file = "response.txt" if mode == "invalid_response" else "stdout.jsonl"
    assert (target / invalid_file).read_bytes() == b"\xff"
    assert (target / "stderr.txt").read_bytes() == WIRE_STDERR


@pytest.mark.parametrize("event_type", ["error", "turn.failed"])
def test_codex_error_events_still_reject_a_valid_final_file(tmp_path, event_type):
    response = tmp_path / "response.txt"
    response.write_bytes(b"{}")
    with pytest.raises(trial.TrialFailure) as exc:
        trial.parse_cli_output("codex", json.dumps({"type": event_type}), response)
    assert exc.value.category == "client_or_provider_error"
    assert response.read_bytes() == b"{}"
