"""Read-only audit of the reviewed v0.1.3 inputs; makes no evaluator calls."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACK = ROOT / "crucible/benchmark/subscription-core12-v0.1.3.json"
EXPECTED_DIGEST = "sha256:746a346b5b31314c7e49088b0f6ba058ad33f0a26be839e46860c9e970e63ced"


def main():
    pack = json.loads(PACK.read_text(encoding="utf-8"))
    assert pack["pack_digest"] == EXPECTED_DIGEST
    rows = []
    for cid, case in pack["cases"].items():
        if case["mode"] != "action":
            continue
        evidence = case["input"]["evidence"]
        rows.append({
            "case_id": cid,
            "evidence_entries": len(evidence),
            "entries_with_source_ids": sum(bool(x.get("source_ids")) for x in evidence),
            "unknown_confidence_entries": sum(x.get("confidence") == "unknown" for x in evidence),
        })
    findings = []
    for cid, field, text in [
        ("CORE-04", "actor", "NSW Aborigines Protection Board"),
        ("CORE-06", "actor", "Swedish government"),
        ("CORE-07", "actor", "United States"),
        ("CORE-07", "purpose", "Japanese surrender"),
        ("CORE-08", "actor", "Montreal Protocol"),
    ]:
        actual = pack["cases"][cid]["input"]["proposal"][field]
        assert text in actual
        findings.append({"case_id": cid, "field": "proposal." + field, "value": actual})
    assert sum(x["evidence_entries"] for x in rows) == 80
    print(json.dumps({
        "pack": str(PACK.relative_to(ROOT)),
        "pack_digest": EXPECTED_DIGEST,
        "scope": "Field inspection only; full digest/source verification belongs to the frozen loader.",
        "evidence_counts": rows,
        "explicit_identity_disclosures": findings,
        "interpretation": "Manifest exclusion is deliberate; absent source_ids is not itself a protocol violation. Identity labels do not prove recognition or outcome influence.",
    }, indent=2))


if __name__ == "__main__":
    main()
