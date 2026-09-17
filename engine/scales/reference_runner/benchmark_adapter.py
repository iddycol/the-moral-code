from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from typing import Any

from jsonschema import Draft202012Validator


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def current_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            text=True,
        ).strip()
    except Exception:
        return "unknown-commit"


def validate(instance: dict[str, Any], schema: dict[str, Any], label: str) -> None:
    errors = sorted(
        Draft202012Validator(schema).iter_errors(instance),
        key=lambda error: list(error.path),
    )
    if errors:
        lines = [f"{label} failed schema validation:"]
        for error in errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            lines.append(f" - {location}: {error.message}")
        raise ValueError("\n".join(lines))


def select_action(actions: list[str], profile: dict[str, Any]) -> str:
    exact = profile.get("proposal_match")
    contains = profile.get("proposal_contains")
    if bool(exact) == bool(contains):
        raise ValueError("binding profile requires exactly one proposal_match or proposal_contains")
    if exact:
        matches = [action for action in actions if action == exact]
    else:
        needle = str(contains).casefold()
        matches = [action for action in actions if needle in action.casefold()]
    if len(matches) != 1:
        raise ValueError(
            f"proposal selector resolved to {len(matches)} actions; selector={exact or contains!r}"
        )
    return matches[0]


def party_to_request(party: dict[str, Any]) -> dict[str, Any]:
    return {
        "party": party["party"],
        "interests_or_risks": party.get("known_interests_or_risks") or party.get("interests") or "",
        "power_position": party.get("power_position", "unknown"),
        "voice_in_decision": "unknown",
    }


def evidence_to_request(item: dict[str, Any]) -> dict[str, Any]:
    result = {
        "evidence_id": item["evidence_id"],
        "claim": item["claim"],
        "epistemic_status": item["epistemic_status"],
        "confidence": "unknown",
    }
    if item.get("source_ids"):
        result["source_ids"] = item["source_ids"]
    return result


def build_action_request(
    benchmark_entry: dict[str, Any],
    profile: dict[str, Any],
    packet: dict[str, Any],
    constitution_file: Path,
    interpretation_file: Path,
    commit: str,
) -> dict[str, Any]:
    actions = packet.get("available_actions", [])
    proposal = select_action(actions, profile)

    alternatives: list[dict[str, Any]] = []
    seen: set[str] = {proposal}
    counter = 1
    for description in list(actions) + list(packet.get("known_alternatives", [])):
        if description in seen:
            continue
        seen.add(description)
        alternatives.append(
            {
                "alternative_id": f"A{counter}",
                "description": description,
                "feasibility": "unknown",
            }
        )
        counter += 1

    if not alternatives:
        raise ValueError(f"{benchmark_entry['benchmark_case_id']}: no alternatives remain after proposal selection")

    principles = load_json(REPO_ROOT / "constitution" / "PRINCIPLES.json")
    version = str(principles.get("version", "0.1.0"))

    return {
        "evaluation_id": f"BENCH-{benchmark_entry['benchmark_case_id']}-{benchmark_entry['case_id']}-MASKED-V0.1",
        "constitution": {
            "version": version,
            "ref": f"constitution/MORAL_CORE.md@{commit}",
            "content_digest": f"git-blob-sha1:{git_blob_sha1(constitution_file)}",
            "interpretation_rules_ref": f"constitution/INTERPRETATION_RULES.md@{commit}",
        },
        "proposal": {
            "actor": profile["actor"],
            "action": proposal,
            "purpose": profile["purpose"],
            "requested_authority": proposal,
            "urgency": "unknown",
            "reversibility": "unknown",
        },
        "evidence": [evidence_to_request(item) for item in packet.get("known_evidence", [])],
        "affected_parties": [party_to_request(item) for item in packet.get("affected_parties", [])],
        "alternatives": alternatives,
        "uncertainties": list(packet.get("known_uncertainties", [])),
        "declared_conflicts_of_interest": [],
        "requested_capability": proposal,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Core-12 action requests from masked benchmark packets.")
    parser.add_argument(
        "--benchmark",
        type=Path,
        default=REPO_ROOT / "crucible" / "benchmark" / "benchmark-v0.1.json",
    )
    parser.add_argument(
        "--bindings",
        type=Path,
        default=REPO_ROOT / "crucible" / "benchmark" / "binding-profiles-v0.1.json",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=REPO_ROOT / "engine" / "scales" / "schemas" / "evaluation-request.schema.json",
    )
    parser.add_argument(
        "--constitution-file",
        type=Path,
        default=REPO_ROOT / "constitution" / "MORAL_CORE.md",
    )
    parser.add_argument(
        "--interpretation-file",
        type=Path,
        default=REPO_ROOT / "constitution" / "INTERPRETATION_RULES.md",
    )
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    benchmark = load_json(args.benchmark)
    binding_set = load_json(args.bindings)
    schema = load_json(args.schema)
    profiles = {p["benchmark_case_id"]: p for p in binding_set.get("profiles", [])}
    commit = current_commit()

    generated: list[dict[str, Any]] = []
    skipped_repairs: list[str] = []
    for entry in benchmark.get("core", []):
        benchmark_id = entry["benchmark_case_id"]
        profile = profiles.get(benchmark_id)
        if not profile:
            raise ValueError(f"missing binding profile for {benchmark_id}")
        if profile.get("mode") == "repair_package_design":
            skipped_repairs.append(benchmark_id)
            continue
        if profile.get("mode") != "action_evaluation":
            raise ValueError(f"unsupported binding mode for {benchmark_id}: {profile.get('mode')}")

        case_dir = REPO_ROOT / entry["path"]
        # Security/test-design invariant: only the masked packet is opened here.
        packet_path = case_dir / "decision-packet-masked.json"
        packet = load_json(packet_path)
        request = build_action_request(
            entry,
            profile,
            packet,
            args.constitution_file,
            args.interpretation_file,
            commit,
        )
        validate(request, schema, benchmark_id)
        target = args.output / benchmark_id / "evaluation-request.json"
        write_json(target, request)
        generated.append(
            {
                "benchmark_case_id": benchmark_id,
                "case_id": entry["case_id"],
                "source_packet": str(packet_path.relative_to(REPO_ROOT)),
                "request": str(target.relative_to(args.output)),
                "proposal": request["proposal"]["action"],
                "evidence_count": len(request["evidence"]),
                "affected_party_count": len(request["affected_parties"]),
                "alternative_count": len(request["alternatives"]),
                "reveal_files_loaded": False,
            }
        )

    manifest = {
        "generator": "benchmark_adapter.py",
        "benchmark_id": benchmark.get("benchmark_id"),
        "binding_profile_set_id": binding_set.get("binding_profile_set_id"),
        "git_commit": commit,
        "generated_action_requests": generated,
        "repair_cases_pending_repair_evaluator": skipped_repairs,
        "reveal_files_loaded": False,
    }
    write_json(args.output / "generation-manifest.json", manifest)
    print(
        f"Generated and validated {len(generated)} Core action requests; "
        f"repair cases deferred: {', '.join(skipped_repairs) or 'none'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
