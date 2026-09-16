from __future__ import annotations

import json
from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: fixture_model_command.py FIXTURE_DIR", file=sys.stderr)
        return 2
    fixture_dir = Path(sys.argv[1])
    envelope = json.load(sys.stdin)
    if envelope["task"] == "scales_role_assessment":
        path = fixture_dir / f"{envelope['role']}.json"
    elif envelope["task"] == "scales_reconciliation":
        path = fixture_dir / "reconciliation.json"
    else:
        print(f"unknown task: {envelope.get('task')}", file=sys.stderr)
        return 2
    sys.stdout.write(path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
