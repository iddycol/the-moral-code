from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import shlex
import subprocess
from typing import Any

from .base import ROLES
from prompting import build_role_envelope, build_reconciliation_envelope


class JsonCommandProvider:
    """Run a model through a local command that accepts a JSON envelope on stdin.

    The command must emit exactly one JSON object on stdout. This keeps the
    reference runner independent of any model vendor or API.
    """

    def __init__(
        self,
        command: str,
        provider_name: str,
        model: str,
        model_version: str,
        constitution_file: Path,
        interpretation_file: Path,
        role_contracts_file: Path,
        role_schema: dict[str, Any],
        reconciliation_schema: dict[str, Any],
        timeout_seconds: int = 180,
    ):
        self.command = shlex.split(command)
        if not self.command:
            raise ValueError("provider command cannot be empty")
        self.name = provider_name
        self.model = model
        self.model_version = model_version
        self.constitution_text = constitution_file.read_text(encoding="utf-8")
        self.interpretation_text = interpretation_file.read_text(encoding="utf-8")
        self.role_contracts_text = role_contracts_file.read_text(encoding="utf-8")
        self.role_schema = role_schema
        self.reconciliation_schema = reconciliation_schema
        self.timeout_seconds = timeout_seconds

    def _invoke(self, envelope: dict[str, Any]) -> dict[str, Any]:
        completed = subprocess.run(
            self.command,
            input=json.dumps(envelope, ensure_ascii=False),
            text=True,
            capture_output=True,
            timeout=self.timeout_seconds,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"provider command exited {completed.returncode}: {completed.stderr.strip()}"
            )
        raw = completed.stdout.strip()
        if raw.startswith("```") or raw.endswith("```"):
            raise ValueError("provider output must be raw JSON, not a Markdown code fence")
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"provider output was not valid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError("provider output must be one JSON object")
        return value

    def _stamp_metadata(self, value: dict[str, Any]) -> dict[str, Any]:
        value = deepcopy(value)
        metadata = value.setdefault("run_metadata", {})
        metadata["provider"] = self.name
        metadata["model"] = self.model
        metadata["model_version"] = self.model_version
        return value

    def assess_role(self, role: str, request: dict[str, Any]) -> dict[str, Any]:
        if role not in ROLES:
            raise ValueError(f"Unknown Scales role: {role}")
        envelope = build_role_envelope(
            role,
            request,
            self.constitution_text,
            self.interpretation_text,
            self.role_contracts_text,
            self.role_schema,
        )
        value = self._stamp_metadata(self._invoke(envelope))
        if value.get("evaluation_id") != request.get("evaluation_id"):
            raise ValueError(f"{role} output evaluation_id does not match request")
        if value.get("role") != role:
            raise ValueError(f"{role} output declares role={value.get('role')!r}")
        return value

    def reconcile(
        self,
        request: dict[str, Any],
        role_assessments: dict[str, dict[str, Any]],
    ) -> dict[str, Any]:
        missing = [role for role in ROLES if role not in role_assessments]
        if missing:
            raise ValueError(f"Cannot reconcile; missing role assessments: {missing}")
        envelope = build_reconciliation_envelope(
            request,
            role_assessments,
            self.constitution_text,
            self.interpretation_text,
            self.role_contracts_text,
            self.reconciliation_schema,
        )
        value = self._invoke(envelope)
        if value.get("evaluation_id") != request.get("evaluation_id"):
            raise ValueError("reconciliation output evaluation_id does not match request")
        return value
