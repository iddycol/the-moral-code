"""Verify audit coverage and exact frozen claim text, not historical truth."""
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    pack = json.loads((ROOT / "crucible/benchmark/subscription-core12-v0.1.3.json").read_text(encoding="utf-8"))
    expected = {
        (cid, row["evidence_id"]): row["claim"]
        for cid, case in pack["cases"].items() if case["mode"] == "action"
        for row in case["input"]["evidence"]
    }
    seen = set()
    counts = Counter()
    index = []
    for path in sorted(HERE.glob("sources-*.json")):
        for row in json.loads(path.read_text(encoding="utf-8"))["claims"]:
            key = (row["core_id"], row["evidence_id"])
            assert key not in seen, key
            assert row.get("claim", row.get("exact_claim")) == expected[key], key
            assert row.get("decision_time_assessment"), key
            assert row["status"] in {"supported", "partially_supported", "inference", "unverified_access", "unsupported"}
            seen.add(key)
            counts[row["status"]] += 1
            index.append({"core_id": key[0], "evidence_id": key[1], "status": row["status"], "ledger": path.name})
    assert seen == set(expected)
    repair = json.loads((HERE / "repair-11-12.json").read_text(encoding="utf-8"))["claims"]
    repair_keys = {(row["core_id"], row["field"]): row for row in repair}
    assert len(repair_keys) == len(repair)
    harms = options = 0
    for cid, case in pack["cases"].items():
        if case["mode"] != "repair":
            continue
        for collection, id_field in [("established_harms", "harm_id"), ("repair_options", "option_id")]:
            for row in case["input"][collection]:
                key = (cid, collection + "/" + row[id_field])
                assert key in repair_keys, key
                assert repair_keys[key]["claim"] == row["description"], key
                if collection == "established_harms":
                    harms += 1
                else:
                    options += 1
    print(json.dumps({
        "scope": "Exact text and coverage validation only; support judgments remain reviewable.",
        "action_claims": len(seen), "action_status_counts": dict(sorted(counts.items())),
        "repair_harms": harms, "repair_options": options, "repair_rows_total": len(repair),
        "action_index": index,
    }, indent=2))


if __name__ == "__main__":
    main()
