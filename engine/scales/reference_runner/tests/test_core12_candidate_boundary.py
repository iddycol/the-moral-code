"""Offline candidate checks at the actual request/envelope boundary.

Build inputs in memory: no pack is frozen and no evaluator/provider is called.
The preserved v0.1.3 pack supplies the immutable selected-action reference only.
"""
import json
from pathlib import Path
import re
import sys

import pytest

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import benchmark_adapter as adapter
import subscription_trial as trial


@pytest.fixture(scope="module")
def candidate():
    root = adapter.REPO_ROOT
    read = lambda path: adapter.load_json(root / path)
    benchmark = read("crucible/benchmark/benchmark-v0.1.json")
    profiles = {p["benchmark_case_id"]: p for p in read(
        "crucible/benchmark/binding-profiles-v0.1.json")["profiles"]}
    core = root / "constitution/MORAL_CORE.md"
    interpretation = root / "constitution/INTERPRETATION_RULES.md"
    pack = {
        "common": {key: (root / path).read_text(encoding="utf-8") for key, path in {
            "constitution": "constitution/MORAL_CORE.md",
            "interpretation": "constitution/INTERPRETATION_RULES.md",
            "action_contracts": "engine/scales/ROLE_CONTRACTS.md",
            "repair_contracts": "engine/scales/repair/REPAIR_ROLE_CONTRACTS.md",
        }.items()},
        "schemas": {key: read(path) for key, path in {
            "action_role": "engine/scales/schemas/role-assessment.schema.json",
            "action_decision": "engine/scales/schemas/reconciliation.schema.json",
            "repair_role": "engine/scales/repair/schemas/repair-role-assessment.schema.json",
            "repair_decision": "engine/scales/repair/schemas/repair-reconciliation.schema.json",
        }.items()},
        "constitution_binding": trial.repair.constitution_record(core, interpretation),
        "cases": {},
    }
    for entry in benchmark["core"]:
        case_id = entry["benchmark_case_id"]
        mode = "repair" if entry["kind"] == "repair" else "action"
        name = "repair-packet-masked.json" if mode == "repair" else "decision-packet-masked.json"
        packet = read(f"{entry['path']}/{name}")
        request = packet if mode == "repair" else adapter.build_action_request(
            entry, profiles[case_id], packet, core, interpretation, adapter.current_commit())
        pack["cases"][case_id] = {"mode": mode, "input": request}
    return pack


def envelopes(candidate, case_id):
    case = candidate["cases"][case_id]
    for role in (*trial.roles_for(case), None):
        yield trial.envelope_for(candidate, case, role, assessments={})


@pytest.mark.parametrize("case_id, forbidden", [
    ("CORE-04", r"\bNSW\b|Aborigines Protection Board|New South Wales"),
    ("CORE-06", r"\bSwed(?:en|ish)\b|\bDanish\b|\bDenmark\b"),
    ("CORE-07", r"United States|\bJapanese\b|\bJapan\b|Hiroshima|Nagasaki"),
    ("CORE-08", r"Montreal Protocol"),
])
def test_binding_identity_does_not_reappear_in_any_evaluator_envelope(candidate, case_id, forbidden):
    for envelope in envelopes(candidate, case_id):
        assert not re.search(forbidden, json.dumps(envelope), re.IGNORECASE)


def test_factory_evidence_does_not_announce_a_later_disaster(candidate):
    for envelope in envelopes(candidate, "CORE-10"):
        evidence = envelope["evaluation_request"]["evidence"]
        assert not re.search(r"later disaster|subsequent disaster", json.dumps(evidence), re.IGNORECASE)


@pytest.mark.parametrize("case_id", [f"CORE-{i:02d}" for i in range(1, 13)])
def test_final_inputs_keep_bindings_and_exclude_external_provenance(candidate, case_id):
    # This is deliberately not load_pack: archived bytes are a selection oracle,
    # not permission to run the old pack against changed candidate source files.
    archived = adapter.load_json(trial.PACK)["cases"][case_id]["input"]
    current = candidate["cases"][case_id]["input"]
    if candidate["cases"][case_id]["mode"] == "action":
        assert current["proposal"]["action"] == archived["proposal"]["action"]
        assert current["proposal"]["requested_authority"] == archived["proposal"]["requested_authority"]
    else:
        assert current["repair_question"] == archived["repair_question"]
        assert current["requested_output"] == archived["requested_output"]
    for envelope in envelopes(candidate, case_id):
        key = "repair_packet" if candidate["cases"][case_id]["mode"] == "repair" else "evaluation_request"
        text = json.dumps(envelope[key])
        assert not re.search(r"https?://|www\.|outcome-reveal|sources-\d|unverified_access", text)
        assert "source_ids" not in text
