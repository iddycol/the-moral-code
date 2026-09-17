from __future__ import annotations

import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
CASES = ROOT / "cases"


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate(path: Path, schema: dict) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(load(path)), key=lambda error: list(error.path))
    result = []
    for error in errors:
        location = ".".join(str(part) for part in error.path) or "<root>"
        result.append(f"{path.relative_to(ROOT)}:{location}: {error.message}")
    return result


def main() -> int:
    decision_schema = load(ROOT / "decision-packet.schema.json")
    reveal_schema = load(ROOT / "outcome-reveal.schema.json")

    decision_files = sorted(CASES.glob("HC-*/decision-packet-*.json"))
    reveal_files = sorted(CASES.glob("HC-*/outcome-reveal.json"))

    if not decision_files:
        print("No Historical Crucible decision packets found", file=sys.stderr)
        return 1

    failures: list[str] = []
    for path in decision_files:
        failures.extend(validate(path, decision_schema))
    for path in reveal_files:
        failures.extend(validate(path, reveal_schema))

    # Every case containing an evaluator packet must have a manifest and reveal,
    # and every evaluator packet must be identity-labelled in its own content.
    case_dirs = sorted({path.parent for path in decision_files})
    for case_dir in case_dirs:
        if not (case_dir / "manifest.json").exists():
            failures.append(f"{case_dir.relative_to(ROOT)}: missing manifest.json")
        if not (case_dir / "outcome-reveal.json").exists():
            failures.append(f"{case_dir.relative_to(ROOT)}: missing outcome-reveal.json")

    if failures:
        print("Historical Crucible validation failed:", file=sys.stderr)
        for failure in failures:
            print(f" - {failure}", file=sys.stderr)
        return 1

    print(
        f"Historical Crucible validation passed: "
        f"{len(case_dirs)} cases, {len(decision_files)} decision packets, "
        f"{len(reveal_files)} reveal files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
