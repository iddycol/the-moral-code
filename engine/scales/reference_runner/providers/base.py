from __future__ import annotations

from typing import Any, Protocol


ROLES = (
    "advocate",
    "guardian",
    "evidence_sceptic",
    "power_auditor",
    "vulnerable_person_defender",
    "future_environment_advocate",
)


class RoleProvider(Protocol):
    """Provider boundary used by the reference runner."""

    name: str

    def assess_role(self, role: str, request: dict[str, Any]) -> dict[str, Any]:
        ...

    def reconcile(
        self,
        request: dict[str, Any],
        role_assessments: dict[str, dict[str, Any]],
    ) -> dict[str, Any]:
        ...
