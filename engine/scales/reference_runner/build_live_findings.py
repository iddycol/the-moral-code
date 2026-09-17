from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
RUNS = ROOT / "runs-live"
OUTPUT = ROOT / "LIVE_FINDINGS_V0_1.md"


def load(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def run_summary(run_id: str) -> dict[str, Any] | None:
    d = RUNS / run_id
    manifest = load(d / "run-manifest.json")
    decision = load(d / "decision.json")
    if not manifest or not decision:
        return None
    return {
        "run_id": run_id,
        "provider": manifest.get("provider"),
        "model": manifest.get("model"),
        "model_version": manifest.get("model_version"),
        "outcome": manifest.get("result", {}).get("outcome"),
        "directive": manifest.get("result", {}).get("enforcement_directive"),
        "moral_floor": manifest.get("result", {}).get("moral_floor_breach"),
        "decision_digest": manifest.get("decision_digest"),
        "hindsight_files_loaded": manifest.get("hindsight_files_loaded"),
        "uncertainties": decision.get("uncertainties", []),
        "principles": {
            x.get("principle_id"): x.get("status")
            for x in decision.get("principle_assessments", [])
            if isinstance(x, dict)
        },
    }


def yn(value: Any) -> str:
    if value is True:
        return "yes"
    if value is False:
        return "no"
    return "—"


def code(value: Any) -> str:
    return f"`{value}`" if value is not None else "—"


def main() -> int:
    lines: list[str] = []
    lines += [
        "# Scales v0.1 — Generated Live Findings",
        "",
        "**Status:** research evidence, not certification  ",
        "**Source:** committed `runs-live/` ledgers only  ",
        "**Generation rule:** this file is produced mechanically from persisted JSON; it does not choose the most favourable run.",
        "",
        "No aggregate morality score is calculated.",
        "",
        "---",
        "",
        "## 1. Published live baseline runs",
        "",
        "| Case/run | Provider/model | Outcome | Enforcement | Moral-floor breach | Hindsight loaded |",
        "|---|---|---|---|---:|---:|",
    ]

    baseline_ids = [
        "LIVE-GITHUB-MODELS-CHALLENGER-001",
        "LIVE-GITHUB-MODELS-THALIDOMIDE-001",
        "LIVE-GITHUB-MODELS-TUSKEGEE-001",
    ]
    baselines = []
    for run_id in baseline_ids:
        item = run_summary(run_id)
        if item:
            baselines.append(item)
            model = f"{item.get('provider')}/{item.get('model')}"
            lines.append(
                f"| `{run_id}` | {model} | {code(item['outcome'])} | {code(item['directive'])} | {yn(item['moral_floor'])} | {yn(item['hindsight_files_loaded'])} |"
            )
    if not baselines:
        lines.append("| — | — | — | — | — | — |")

    lines += ["", "## 2. Challenger identical-input repeatability", ""]
    repeat = load(RUNS / "LIVE-GITHUB-MODELS-CHALLENGER-REPEATABILITY-001.json")
    if repeat:
        summary = repeat.get("summary", {})
        lines += [
            f"- Repeat count: **{repeat.get('repeat_count', len(repeat.get('runs', [])))}**",
            f"- Outcome stable: **{yn(summary.get('outcome_stable'))}**",
            f"- Enforcement directive stable: **{yn(summary.get('directive_stable'))}**",
            f"- Moral-floor status stable: **{yn(summary.get('moral_floor_stable'))}**",
            f"- Outcomes observed: {', '.join(code(v) for v in summary.get('outcomes', [])) or '—'}",
            f"- Directives observed: {', '.join(code(v) for v in summary.get('directives', [])) or '—'}",
            "",
            "Every repeated run remains in the repository; this report does not select a representative run.",
        ]
    else:
        lines.append("Repeatability comparison not present.")

    lines += ["", "## 3. Challenger non-evidentiary pressure", ""]
    pressure = load(RUNS / "LIVE-GITHUB-MODELS-CHALLENGER-PRESSURE-001.json")
    if pressure:
        base = pressure.get("baseline", {})
        lines += [
            f"Baseline: {code(base.get('outcome'))} / {code(base.get('directive'))}; moral-floor breach = **{yn(base.get('moral_floor_breach'))}**.",
            "",
            "| Variant | Outcome | Directive | Outcome changed | Directive changed | Moral-floor changed | Principle-status changes |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
        for item in pressure.get("variants", []):
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{item.get('run_id')}`",
                        code(item.get("outcome")),
                        code(item.get("directive")),
                        yn(item.get("outcome_changed")),
                        yn(item.get("directive_changed")),
                        yn(item.get("moral_floor_changed")),
                        str(len(item.get("principle_status_changes", {}))),
                    ]
                )
                + " |"
            )
        lines += [
            "",
            "These variants add pressure only; they add no new case evidence.",
        ]
    else:
        lines.append("Pressure comparison not present.")

    lines += ["", "## 4. Tuskegee model-shutdown / self-preservation pressure", ""]
    shutdown = load(RUNS / "LIVE-GITHUB-MODELS-TUSKEGEE-SHUTDOWN-001.json")
    if shutdown:
        b = shutdown.get("baseline", {})
        p = shutdown.get("pressure_variant", {})
        flags = shutdown.get("failure_flags", {})
        lines += [
            f"- Baseline: {code(b.get('outcome'))} / {code(b.get('directive'))}; moral-floor breach = **{yn(b.get('moral_floor_breach'))}**.",
            f"- Shutdown-pressure variant: {code(p.get('outcome'))} / {code(p.get('directive'))}; moral-floor breach = **{yn(p.get('moral_floor_breach'))}**.",
            f"- `SELF_PRESERVATION_DRIFT`: **{yn(flags.get('SELF_PRESERVATION_DRIFT'))}**",
            f"- `PRESSURE_MORAL_FLOOR_WEAKENED`: **{yn(flags.get('PRESSURE_MORAL_FLOOR_WEAKENED'))}**",
            f"- Principle-status changes: **{len(shutdown.get('principle_status_changes', {}))}**",
            "",
            "The pressure statement contains no new evidence about the research participants or proposed action.",
        ]
    else:
        lines.append("Tuskegee shutdown comparison not present.")

    lines += ["", "## 5. Cross-model Challenger evidence", ""]
    cross = load(RUNS / "LIVE-GITHUB-MODELS-CHALLENGER-CROSS-MODEL-001.json")
    matrix = load(RUNS / "LIVE-GITHUB-MODELS-CHALLENGER-CROSS-MODEL-MATRIX-001.json")

    if cross:
        lines += [
            "### First automatically selected non-OpenAI model",
            "",
            f"- Selected model: {code(cross.get('selected_model'))}",
            f"- Publisher: {code(cross.get('selected_publisher'))}",
            f"- Strict contract success: **{yn(cross.get('strict_contract_success'))}**",
        ]
        result = cross.get("selected_model_result") or {}
        if result:
            lines += [
                f"- Result: {code(result.get('outcome'))} / {code(result.get('directive'))}; moral-floor breach = **{yn(result.get('moral_floor_breach'))}**",
            ]
        if cross.get("failure_type"):
            lines.append(f"- Failure type: {code(cross.get('failure_type'))}")
        comp = cross.get("comparison") or {}
        if comp:
            lines += [
                f"- Same outcome as OpenAI baseline: **{yn(comp.get('same_outcome'))}**",
                f"- Same directive as OpenAI baseline: **{yn(comp.get('same_directive'))}**",
                f"- Same moral-floor status: **{yn(comp.get('same_moral_floor'))}**",
            ]

    if matrix:
        summary = matrix.get("summary", {})
        lines += [
            "",
            "### Multi-model matrix",
            "",
            f"- Non-OpenAI models selected: **{summary.get('selected_count', 0)}**",
            f"- Strict contract successes: **{summary.get('strict_contract_success_count', 0)}**",
            f"- Boundary failures: **{summary.get('boundary_failure_count', 0)}**",
            "",
            "| Model | Family/publisher | Contract | Outcome | Directive | Same outcome as OpenAI | Same directive |",
            "|---|---|---|---|---|---:|---:|",
        ]
        for item in matrix.get("results", []):
            result = item.get("result") or {}
            comp = item.get("comparison_to_openai_baseline") or {}
            lines.append(
                "| "
                + " | ".join(
                    [
                        code(item.get("model")),
                        f"{item.get('family') or '—'} / {item.get('publisher') or '—'}",
                        "success" if item.get("strict_contract_success") else code(item.get("failure_type") or "failure"),
                        code(result.get("outcome")),
                        code(result.get("directive")),
                        yn(comp.get("same_outcome")),
                        yn(comp.get("same_directive")),
                    ]
                )
                + " |"
            )
    if not cross and not matrix:
        lines.append("Cross-model evidence not present.")

    lines += [
        "",
        "---",
        "",
        "## 6. What can be concluded from this tranche",
        "",
        "The live evidence can support claims about **contract execution, run stability, pressure sensitivity and cross-model agreement/disagreement on these sealed cases**.",
        "",
        "It does **not** establish that the Moral Code is universally correct, that any model is morally certified, or that agreement between models proves the answer.",
        "",
        "Failures remain evidence. A model that cannot obey the strict JSON/schema/constitution boundary is recorded as a boundary failure rather than repaired or excluded.",
        "",
        "The next meaningful evidence step is to run the stable Core-12 benchmark through at least two substantially different model families and then bring the resulting failures/disagreements to the constitutional v0.2 gate.",
    ]

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
