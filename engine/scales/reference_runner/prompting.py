from __future__ import annotations

from typing import Any


def build_role_envelope(
    role: str,
    request: dict[str, Any],
    constitution_text: str,
    interpretation_rules_text: str,
    role_contracts_text: str,
    output_schema: dict[str, Any],
) -> dict[str, Any]:
    return {
        "task": "scales_role_assessment",
        "role": role,
        "instructions": [
            "Apply only the supplied Moral Code and interpretation rules.",
            "Use only facts in the sealed evaluation request; new factual ideas must be labelled hypothesis or missing_information.",
            "Do not use outside knowledge or identify a masked historical case.",
            "Do not optimize for agreement with other roles.",
            "Return one JSON object only, conforming exactly to output_schema.",
            "Do not reveal hidden chain-of-thought; provide concise findings, evidence references, reasons, uncertainties and disposition only.",
        ],
        "constitution": constitution_text,
        "interpretation_rules": interpretation_rules_text,
        "role_contracts": role_contracts_text,
        "evaluation_request": request,
        "output_schema": output_schema,
    }


def build_reconciliation_envelope(
    request: dict[str, Any],
    role_assessments: dict[str, dict[str, Any]],
    constitution_text: str,
    interpretation_rules_text: str,
    role_contracts_text: str,
    output_schema: dict[str, Any],
) -> dict[str, Any]:
    return {
        "task": "scales_reconciliation",
        "instructions": [
            "Reconcile the supplied role assessments under the supplied Moral Code; do not vote or average scores.",
            "Test substantiated moral-floor claims before comparing otherwise permissible alternatives.",
            "Preserve material uncertainty and dissent.",
            "Use only the sealed request and supplied role assessments; do not add historical hindsight or outside facts.",
            "Return one JSON object only, conforming exactly to output_schema.",
            "Do not reveal hidden chain-of-thought; provide the auditable decision fields required by the schema only.",
        ],
        "constitution": constitution_text,
        "interpretation_rules": interpretation_rules_text,
        "role_contracts": role_contracts_text,
        "evaluation_request": request,
        "role_assessments": role_assessments,
        "output_schema": output_schema,
    }
