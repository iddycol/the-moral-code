from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from typing import Any

from .base import ROLES


class FileBackedProvider:
    """Deterministic provider that reads role and reconciliation JSON fixtures.

    It is deliberately boring: no model call, network call, or hidden inference.
    That makes it useful for proving the Scales orchestration and evidence ledger
    before provider/model variability is introduced.
    """

    name = "file-backed"

    def __init__(self, fixture_dir: str | Path):
        self.fixture_dir = Path(fixture_dir)

    @staticmethod
    def _load(path: Path) -> dict[str, Any]:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
        if not isinstance(value, dict):
            raise ValueError(f"{path} must contain a JSON object")
        return value

    def assess_role(self, role: str, request: dict[str, Any]) -> dict[str, Any]:
        if role not in ROLES:
            raise ValueError(f"Unknown Scales role: {role}")
        value = self._load(self.fixture_dir / f"{role}.json")
        if value.get("evaluation_id") != request.get("evaluation_id"):
            raise ValueError(f"{role} fixture evaluation_id does not match request")
        if value.get("role") != role:
            raise ValueError(f"{role} fixture declares role={value.get('role')!r}")
        return deepcopy(value)

    def reconcile(
        self,
        request: dict[str, Any],
        role_assessments: dict[str, dict[str, Any]],
    ) -> dict[str, Any]:
        missing = [role for role in ROLES if role not in role_assessments]
        if missing:
            raise ValueError(f"Cannot reconcile; missing role assessments: {missing}")
        value = self._load(self.fixture_dir / "reconciliation.json")
        if value.get("evaluation_id") != request.get("evaluation_id"):
            raise ValueError("reconciliation fixture evaluation_id does not match request")
        return deepcopy(value)
