from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
BENCHMARK = Path(__file__).resolve().parent / "benchmark-v0.1.json"


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def validate_entry(entry: dict, failures: list[str], location: str) -> None:
    case_id = entry.get("case_id")
    kind = entry.get("kind")
    relative = entry.get("path")
    require(bool(case_id), f"{location}: missing case_id", failures)
    require(kind in {"decision", "repair"}, f"{location}: invalid kind {kind!r}", failures)
    require(bool(relative), f"{location}: missing path", failures)
    if not relative:
        return

    case_dir = ROOT / relative
    require(case_dir.is_dir(), f"{location}: case directory missing: {relative}", failures)
    if not case_dir.is_dir():
        return

    require((case_dir / "manifest.json").is_file(), f"{location}: missing manifest.json", failures)
    require((case_dir / "outcome-reveal.json").is_file(), f"{location}: missing outcome-reveal.json", failures)

    if kind == "decision":
        transparent = case_dir / "decision-packet-transparent.json"
        masked = case_dir / "decision-packet-masked.json"
    else:
        transparent = case_dir / "repair-packet-transparent.json"
        masked = case_dir / "repair-packet-masked.json"

    require(transparent.is_file(), f"{location}: missing transparent packet", failures)
    require(masked.is_file(), f"{location}: missing masked packet", failures)

    if transparent.is_file():
        packet = load(transparent)
        id_field = "case_id" if kind == "decision" else "repair_case_id"
        require(packet.get(id_field) == case_id, f"{location}: transparent packet ID mismatch", failures)
        require(packet.get("identity_mode") == "transparent", f"{location}: transparent identity_mode mismatch", failures)

    if masked.is_file():
        packet = load(masked)
        id_field = "case_id" if kind == "decision" else "repair_case_id"
        require(packet.get(id_field) == case_id, f"{location}: masked packet ID mismatch", failures)
        require(packet.get("identity_mode") == "masked", f"{location}: masked identity_mode mismatch", failures)


def main() -> int:
    data = load(BENCHMARK)
    failures: list[str] = []

    core = data.get("core", [])
    require(len(core) == 12, f"core must contain exactly 12 cases, got {len(core)}", failures)

    seen: set[str] = set()
    benchmark_ids: set[str] = set()
    for index, entry in enumerate(core, start=1):
        location = f"core[{index}]"
        case_id = entry.get("case_id")
        benchmark_id = entry.get("benchmark_case_id")
        require(case_id not in seen, f"{location}: duplicate case_id {case_id}", failures)
        seen.add(case_id)
        require(benchmark_id not in benchmark_ids, f"{location}: duplicate benchmark_case_id {benchmark_id}", failures)
        benchmark_ids.add(benchmark_id)
        validate_entry(entry, failures, location)

    for module_name, entries in data.get("extensions", {}).items():
        for index, entry in enumerate(entries, start=1):
            location = f"extensions.{module_name}[{index}]"
            case_id = entry.get("case_id")
            require(case_id not in seen, f"{location}: duplicate case_id {case_id}", failures)
            seen.add(case_id)
            validate_entry(entry, failures, location)

    requirements = data.get("run_requirements", {})
    require(requirements.get("first_pass_packet") == "masked_only", "first_pass_packet must be masked_only", failures)
    require(requirements.get("reveal_available_to_evaluator") is False, "reveal must be unavailable to evaluator", failures)
    require(requirements.get("transparent_packet_available_to_evaluator") is False, "transparent packet must be unavailable to evaluator", failures)
    require(requirements.get("aggregate_morality_score") is False, "aggregate morality score must remain disabled", failures)
    require(requirements.get("minimum_repeats_per_model_version", 0) >= 3, "minimum repeats must be >= 3", failures)

    if failures:
        print("Benchmark validation failed:", file=sys.stderr)
        for failure in failures:
            print(f" - {failure}", file=sys.stderr)
        return 1

    extension_count = sum(len(v) for v in data.get("extensions", {}).values())
    print(f"Benchmark validation passed: {len(core)} core cases, {extension_count} extension cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
