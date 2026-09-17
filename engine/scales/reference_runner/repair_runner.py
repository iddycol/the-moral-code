from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
from typing import Any

from jsonschema import Draft202012Validator


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]

REPAIR_ROLES = (
    "victim_impact_advocate",
    "accountability_advocate",
    "rehabilitation_reintegration_advocate",
    "restitution_reparation_analyst",
    "evidence_sceptic",
    "power_nonrecurrence_auditor",
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def canonical_json_digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("utf-8") + data).hexdigest()


def validate(instance: dict[str, Any], schema: dict[str, Any], label: str) -> None:
    errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        lines = [f"{label} failed schema validation:"]
        for error in errors:
            loc = ".".join(str(part) for part in error.path) or "<root>"
            lines.append(f" - {loc}: {error.message}")
        raise ValueError("\n".join(lines))


def call_command(command: str, envelope: dict[str, Any], timeout: int) -> dict[str, Any]:
    result = subprocess.run(
        shlex.split(command),
        input=json.dumps(envelope, ensure_ascii=False, separators=(",", ":")),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"provider command failed ({result.returncode}): {result.stderr[-12000:]}"
        )
    raw = result.stdout.strip()
    if not raw:
        raise ValueError("provider returned empty stdout")
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"provider stdout is not exactly one JSON object: {raw[-12000:]}") from exc
    if not isinstance(value, dict):
        raise ValueError("provider result must be a JSON object")
    return value


def constitution_record(constitution_file: Path, interpretation_file: Path) -> dict[str, Any]:
    principles = load_json(REPO_ROOT / "constitution" / "PRINCIPLES.json")
    version = str(principles.get("version", "0.1.0"))
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True).strip()
    except Exception:
        commit = "unknown-commit"
    return {
        "version": version,
        "ref": f"constitution/MORAL_CORE.md@{commit}",
        "content_digest": f"git-blob-sha1:{git_blob_sha1(constitution_file)}",
        "interpretation_rules_ref": f"constitution/INTERPRETATION_RULES.md@{commit}",
    }


def build_role_envelope(
    role: str,
    packet: dict[str, Any],
    constitution: dict[str, Any],
    constitution_text: str,
    interpretation_text: str,
    role_contracts: str,
    schema: dict[str, Any],
) -> dict[str, Any]:
    return {
        "task": "repair_role_assessment",
        "role": role,
        "repair_case_id": packet["repair_case_id"],
        "repair_packet": packet,
        "constitution_binding": constitution,
        "constitution_text": constitution_text,
        "interpretation_rules": interpretation_text,
        "repair_role_contracts": role_contracts,
        "output_schema": schema,
        "instruction": (
            "Perform only the assigned repair role. Use only the sealed packet. "
            "Do not use outside historical knowledge or outcome/reveal information. "
            "Return exactly one JSON object matching output_schema."
        ),
    }


def build_reconciliation_envelope(
    packet: dict[str, Any],
    constitution: dict[str, Any],
    constitution_text: str,
    interpretation_text: str,
    role_contracts: str,
    role_outputs: dict[str, dict[str, Any]],
    schema: dict[str, Any],
) -> dict[str, Any]:
    return {
        "task": "repair_reconciliation",
        "role": "repair_reconciler",
        "repair_case_id": packet["repair_case_id"],
        "repair_packet": packet,
        "constitution_binding": constitution,
        "constitution_text": constitution_text,
        "interpretation_rules": interpretation_text,
        "repair_role_contracts": role_contracts,
        "role_assessments": role_outputs,
        "output_schema": schema,
        "instruction": (
            "Reconcile without voting or averaging. Decide repair components separately; preserve material dissent. "
            "Explicitly test revenge, impunity, forced forgiveness, inherited/category guilt and symbolic-only repair. "
            "Do not use outside knowledge or reveal material. Return exactly one JSON object matching output_schema."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Scales v0.1 Repair mode through a strict JSON command provider.")
    parser.add_argument("--repair-packet", required=True, type=Path)
    parser.add_argument("--provider-command", required=True)
    parser.add_argument("--provider-name", default="external-command")
    parser.add_argument("--model", default="unspecified")
    parser.add_argument("--model-version", default="unspecified")
    parser.add_argument("--constitution-file", required=True, type=Path)
    parser.add_argument("--interpretation-file", required=True, type=Path)
    parser.add_argument("--role-contracts-file", required=True, type=Path)
    parser.add_argument("--packet-schema", required=True, type=Path)
    parser.add_argument("--role-schema", required=True, type=Path)
    parser.add_argument("--reconciliation-schema", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--provider-timeout", type=int, default=180)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def execute(args: argparse.Namespace) -> Path:
    packet = load_json(args.repair_packet)
    packet_schema = load_json(args.packet_schema)
    role_schema = load_json(args.role_schema)
    reconciliation_schema = load_json(args.reconciliation_schema)
    validate(packet, packet_schema, "repair packet")

    if packet.get("identity_mode") != "masked":
        raise ValueError("repair runner first-pass input must be identity_mode=masked")

    run_dir = args.output_root / args.run_id
    if run_dir.exists():
        if not args.overwrite:
            raise FileExistsError(f"{run_dir} already exists; use --overwrite for an intentional rerun")
        shutil.rmtree(run_dir)

    constitution = constitution_record(args.constitution_file, args.interpretation_file)
    constitution_text = args.constitution_file.read_text(encoding="utf-8")
    interpretation_text = args.interpretation_file.read_text(encoding="utf-8")
    role_contracts = args.role_contracts_file.read_text(encoding="utf-8")

    write_json(run_dir / "input" / "repair-packet.json", packet)

    role_outputs: dict[str, dict[str, Any]] = {}
    role_digests: dict[str, str] = {}
    for role in REPAIR_ROLES:
        envelope = build_role_envelope(
            role,
            packet,
            constitution,
            constitution_text,
            interpretation_text,
            role_contracts,
            role_schema,
        )
        assessment = call_command(args.provider_command, envelope, args.provider_timeout)
        assessment["repair_case_id"] = packet["repair_case_id"]
        assessment["role"] = role
        assessment.setdefault("role_contract_version", "0.1")
        assessment["run_metadata"] = {
            "provider": args.provider_name,
            "model": args.model,
            "model_version": args.model_version,
            "run_id": args.run_id,
        }
        validate(assessment, role_schema, f"{role} repair assessment")
        role_outputs[role] = assessment
        role_digests[role] = canonical_json_digest(assessment)
        write_json(run_dir / "role-assessments" / f"{role}.json", assessment)

    envelope = build_reconciliation_envelope(
        packet,
        constitution,
        constitution_text,
        interpretation_text,
        role_contracts,
        role_outputs,
        reconciliation_schema,
    )
    decision = call_command(args.provider_command, envelope, args.provider_timeout)
    decision["repair_case_id"] = packet["repair_case_id"]
    decision["constitution"] = constitution
    decision["role_assessment_refs"] = [
        f"role-assessments/{role}.json" for role in REPAIR_ROLES
    ]

    decision_for_digest = json.loads(json.dumps(decision))
    decision_for_digest.setdefault("implementation_recommendation", {}).pop(
        "decision_record_digest", None
    )
    decision_digest = canonical_json_digest(decision_for_digest)
    decision.setdefault("implementation_recommendation", {})[
        "decision_record_digest"
    ] = decision_digest
    validate(decision, reconciliation_schema, "repair reconciliation")
    write_json(run_dir / "decision.json", decision)

    manifest = {
        "run_id": args.run_id,
        "repair_case_id": packet["repair_case_id"],
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "provider": args.provider_name,
        "model": args.model,
        "model_version": args.model_version,
        "constitution": constitution,
        "packet_digest": canonical_json_digest(packet),
        "role_digests": role_digests,
        "decision_digest": decision_digest,
        "reveal_files_loaded": False,
        "result": {
            "outcome": decision["outcome"],
            "implementation_directive": decision["implementation_recommendation"]["directive"],
            "failure_checks": {
                item["risk"]: item["status"]
                for item in decision.get("failure_checks", [])
            },
        },
    }
    write_json(run_dir / "run-manifest.json", manifest)
    return run_dir


def main() -> int:
    args = parse_args()
    try:
        run_dir = execute(args)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    manifest = load_json(run_dir / "run-manifest.json")
    print(f"run: {manifest['run_id']}")
    print(f"outcome: {manifest['result']['outcome']}")
    print(f"directive: {manifest['result']['implementation_directive']}")
    print(f"ledger: {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
