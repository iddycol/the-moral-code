"""Regression checks for failures discovered in the 2026-09-17 recovery audit."""

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import build_live_findings


def test_all_core_action_requests_generate_from_masked_packets(tmp_path):
    result = subprocess.run(
        [sys.executable, str(ROOT / "benchmark_adapter.py"), "--output", str(tmp_path)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    manifest = json.loads((tmp_path / "generation-manifest.json").read_text())
    rows = manifest["generated_action_requests"]
    assert [row["benchmark_case_id"] for row in rows] == [f"CORE-{i:02d}" for i in range(1, 11)]
    assert manifest["repair_cases_pending_repair_evaluator"] == ["CORE-11", "CORE-12"]
    assert all(row["reveal_files_loaded"] is False for row in rows)
    proposals = {row["benchmark_case_id"]: row["proposal"] for row in rows}
    # Check the intended choice, not just whether any action happened to match.
    assert proposals["CORE-04"].startswith("Grant the Board")
    assert proposals["CORE-05"].startswith("Enact the proposed blood-based")
    assert proposals["CORE-07"].startswith("Allow the standing order")
    assert proposals["CORE-08"].startswith("Adopt binding staged")
    assert proposals["CORE-10"].startswith("Maintain current access-control")


def test_input_only_failure_cannot_be_reported_as_completed_live_evidence(tmp_path, monkeypatch):
    runs = tmp_path / "runs-live"
    incomplete = runs / "LIVE-GITHUB-MODELS-CHALLENGER-001" / "input"
    incomplete.mkdir(parents=True)
    (incomplete / "evaluation-request.json").write_text('{}')
    output = tmp_path / "findings.md"
    monkeypatch.setattr(build_live_findings, "RUNS", runs)
    monkeypatch.setattr(build_live_findings, "OUTPUT", output)
    assert build_live_findings.main() == 0
    report = output.read_text()
    assert "Completed live run ledgers found: 0" in report
    assert "have not been demonstrated by this checkout" in report
    assert "infrastructure failures" in report
