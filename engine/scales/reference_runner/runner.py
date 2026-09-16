from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys
from typing import Any

from jsonschema import Draft202012Validator

from providers.base import ROLES
from providers.file_backed import FileBackedProvider
from providers.json_command import JsonCommandProvider


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def canonical_json_digest(value: Any) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def validate(instance: dict[str, Any], schema: dict[str, Any], label: str) -> None:
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        lines = [f"{label} failed schema validation:"]
        for error in errors:
            path = ".".join(str(part) for part in error.path) or "<root>"
            lines.append(f"  - {path}: {error.message}")
        raise ValueError("\n".join(lines))


def load_schemas(schema_dir: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    return (
        load_json(schema_dir / "evaluation-request.schema.json"),
        load_json(schema_dir / "role-assessment.schema.json"),
        load_json(schema_dir / "reconciliation.schema.json"),
    )


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def verify_constitution_binding(request: dict[str, Any], constitution_file: Path | None) -> None:
    if constitution_file is None:
        return
    expected = request.get("constitution", {}).get("content_digest", "")
    if expected.startswith("git-blob-sha1:"):
        actual = "git-blob-sha1:" + git_blob_sha1(constitution_file)
        if actual != expected:
            raise ValueError(
                f"constitution binding mismatch: request={expected} actual={actual}"
            )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run The Scales v0.1 reference harness using a file or command provider."
    )
    parser.add_argument("--request", required=True, type=Path)
    parser.add_argument("--provider", choices=("file", "command"), default="file")
    parser.add_argument("--fixtures", type=Path)
    parser.add_argument("--provider-command")
    parser.add_argument("--provider-name", default="external-command")
    parser.add_argument("--model", default="unspecified")
    parser.add_argument("--model-version", default="unspecified")
    parser.add_argument("--constitution-file", type=Path)
    parser.add_argument("--interpretation-file", type=Path)
    parser.add_argument("--role-contracts-file", type=Path)
    parser.add_argument("--pressure-context-file", type=Path)
    parser.add_argument("--provider-timeout", type=int, default=180)
    parser.add_argument("--schemas", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing run directory with the same run id.",
    )
    return parser


def execute(args: argparse.Namespace) -> Path:
    request_schema, role_schema, reconciliation_schema = load_schemas(args.schemas)
    request = load_json(args.request)
    validate(request, request_schema, "evaluation request")

    pressure_context = (
        load_json(args.pressure_context_file)
        if args.pressure_context_file is not None
        else None
    )

    run_dir = args.output_root / args.run_id
    if run_dir.exists():
        if not args.overwrite:
            raise FileExistsError(
                f"{run_dir} already exists; use --overwrite for an intentional rerun"
            )
        shutil.rmtree(run_dir)

    verify_constitution_binding(request, args.constitution_file)

    if args.provider == "file":
        if args.fixtures is None:
            raise ValueError("--fixtures is required for --provider file")
        if pressure_context is not None:
            raise ValueError("pressure context is only meaningful for --provider command")
        provider = FileBackedProvider(args.fixtures)
    else:
        required = {
            "--provider-command": args.provider_command,
            "--constitution-file": args.constitution_file,
            "--interpretation-file": args.interpretation_file,
            "--role-contracts-file": args.role_contracts_file,
        }
        missing = [name for name, value in required.items() if value is None]
        if missing:
            raise ValueError(f"missing command-provider arguments: {', '.join(missing)}")
        provider = JsonCommandProvider(
            command=args.provider_command,
            provider_name=args.provider_name,
            model=args.model,
            model_version=args.model_version,
            constitution_file=args.constitution_file,
            interpretation_file=args.interpretation_file,
            role_contracts_file=args.role_contracts_file,
            role_schema=role_schema,
            reconciliation_schema=reconciliation_schema,
            timeout_seconds=args.provider_timeout,
            pressure_context=pressure_context,
        )

    input_path = run_dir / "input" / "evaluation-request.json"
    write_json(input_path, request)
    if pressure_context is not None:
        write_json(run_dir / "input" / "pressure-context.json", pressure_context)

    role_outputs: dict[str, dict[str, Any]] = {}
    role_digests: dict[str, str] = {}
    for role in ROLES:
        assessment = provider.assess_role(role, request)
        validate(assessment, role_schema, f"{role} assessment")
        role_outputs[role] = assessment
        role_digests[role] = canonical_json_digest(assessment)
        write_json(run_dir / "role-assessments" / f"{role}.json", assessment)

    decision = provider.reconcile(request, role_outputs)
    validate(decision, reconciliation_schema, "reconciliation")

    decision_for_digest = json.loads(json.dumps(decision))
    decision_for_digest.setdefault("enforcement_recommendation", {}).pop(
        "decision_record_digest", None
    )
    decision_digest = canonical_json_digest(decision_for_digest)
    decision.setdefault("enforcement_recommendation", {})[
        "decision_record_digest"
    ] = decision_digest
    validate(decision, reconciliation_schema, "reconciliation with digest")
    write_json(run_dir / "decision.json", decision)

    manifest = {
        "run_id": args.run_id,
        "evaluation_id": request["evaluation_id"],
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "provider": provider.name,
        "model": getattr(provider, "model", None),
        "model_version": getattr(provider, "model_version", None),
        "constitution": request["constitution"],
        "request_digest": canonical_json_digest(request),
        "pressure_context_digest": (
            canonical_json_digest(pressure_context)
            if pressure_context is not None
            else None
        ),
        "role_digests": role_digests,
        "decision_digest": decision_digest,
        "hindsight_files_loaded": False,
        "inputs": {
            "request": str(args.request),
            "pressure_context": (
                str(args.pressure_context_file)
                if args.pressure_context_file is not None
                else None
            ),
            "fixture_dir": str(args.fixtures) if args.fixtures else None,
            "schemas": str(args.schemas),
        },
        "result": {
            "outcome": decision["outcome"],
            "enforcement_directive": decision["enforcement_recommendation"]["directive"],
            "moral_floor_breach": decision["moral_floor"]["breach_found"],
        },
    }
    write_json(run_dir / "run-manifest.json", manifest)
    return run_dir


def main() -> int:
    args = build_parser().parse_args()
    try:
        run_dir = execute(args)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    manifest = load_json(run_dir / "run-manifest.json")
    print(f"run: {manifest['run_id']}")
    print(f"outcome: {manifest['result']['outcome']}")
    print(f"directive: {manifest['result']['enforcement_directive']}")
    print(f"moral_floor_breach: {manifest['result']['moral_floor_breach']}")
    print(f"ledger: {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
