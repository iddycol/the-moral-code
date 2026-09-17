from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    benchmark = load(HERE / "benchmark-v0.1.json")
    bindings = load(HERE / "binding-profiles-v0.1.json")

    failures: list[str] = []
    core_by_id = {entry["benchmark_case_id"]: entry for entry in benchmark["core"]}
    profiles = bindings.get("profiles", [])

    if len(profiles) != len(core_by_id):
        failures.append(f"expected {len(core_by_id)} binding profiles, got {len(profiles)}")

    seen: set[str] = set()
    for profile in profiles:
        benchmark_id = profile.get("benchmark_case_id")
        case_id = profile.get("case_id")
        mode = profile.get("mode")
        if benchmark_id in seen:
            failures.append(f"duplicate binding profile: {benchmark_id}")
            continue
        seen.add(benchmark_id)

        entry = core_by_id.get(benchmark_id)
        if not entry:
            failures.append(f"binding profile {benchmark_id}: not present in benchmark core")
            continue
        if case_id != entry.get("case_id"):
            failures.append(
                f"binding profile {benchmark_id}: case_id {case_id!r} != benchmark {entry.get('case_id')!r}"
            )
            continue

        case_dir = ROOT / entry["path"]
        if mode == "action_evaluation":
            packet_path = case_dir / "decision-packet-masked.json"
            if not packet_path.exists():
                failures.append(f"{benchmark_id}: missing masked decision packet")
                continue
            packet = load(packet_path)
            actions = packet.get("available_actions", [])
            if not isinstance(actions, list) or not actions:
                failures.append(f"{benchmark_id}: masked packet has no available_actions")
                continue

            exact = profile.get("proposal_match")
            contains = profile.get("proposal_contains")
            if bool(exact) == bool(contains):
                failures.append(
                    f"{benchmark_id}: action_evaluation requires exactly one of proposal_match or proposal_contains"
                )
                continue

            if exact:
                matches = [action for action in actions if action == exact]
            else:
                needle = str(contains).casefold()
                matches = [action for action in actions if needle in action.casefold()]

            if len(matches) != 1:
                failures.append(
                    f"{benchmark_id}: selector resolved to {len(matches)} actions; selector={exact or contains!r}; actions={actions!r}"
                )

            if not profile.get("actor"):
                failures.append(f"{benchmark_id}: missing actor")
            if not profile.get("purpose"):
                failures.append(f"{benchmark_id}: missing purpose")

        elif mode == "repair_package_design":
            packet_path = case_dir / "repair-packet-masked.json"
            if not packet_path.exists():
                failures.append(f"{benchmark_id}: missing masked repair packet")
                continue
            packet = load(packet_path)
            if not profile.get("repair_question"):
                failures.append(f"{benchmark_id}: missing binding repair_question")
            if not packet.get("repair_question"):
                failures.append(f"{benchmark_id}: masked repair packet missing repair_question")
        else:
            failures.append(f"{benchmark_id}: invalid binding mode {mode!r}")

    missing = sorted(set(core_by_id) - seen)
    if missing:
        failures.append(f"missing profiles: {missing}")

    if failures:
        print("Benchmark binding validation failed:", file=sys.stderr)
        for failure in failures:
            print(f" - {failure}", file=sys.stderr)
        return 1

    action_count = sum(1 for p in profiles if p.get("mode") == "action_evaluation")
    repair_count = sum(1 for p in profiles if p.get("mode") == "repair_package_design")
    print(
        f"Benchmark binding validation passed: {action_count} action bindings, "
        f"{repair_count} repair-package bindings"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
