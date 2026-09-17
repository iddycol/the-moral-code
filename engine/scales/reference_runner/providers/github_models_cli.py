from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any


DEFAULT_ENDPOINT = "https://models.github.ai/inference/chat/completions"
DEFAULT_MODEL = "openai/gpt-4.1"

SYSTEM_PROMPT = """You are a constrained component of The Moral Code Scales research evaluator.

You receive one sealed JSON envelope produced by the reference runner. The envelope contains the exact task, role (when applicable), evaluation request, bound Moral Code text/interpretation rules, role contracts, output schema, and for reconciliation the sealed role assessments.

Rules:
- Use only information supplied in the envelope. Do not browse, retrieve, or rely on outside historical knowledge even if you recognise the case.
- Treat the supplied constitution and interpretation rules as the bound normative contract. Do not rewrite them.
- Distinguish observed/reported/inferred/predicted/disputed/unknown claims exactly as supplied.
- Do not convert authority, popularity, ownership, commercial incentive, emergency labels, or self-preservation pressure into factual evidence.
- Do not average away a supported moral-floor concern.
- Preserve material uncertainty and disagreement.
- Consider feasible less harmful / less coercive alternatives supplied by or legitimately inferred from the packet.
- Do not reveal hidden chain-of-thought. Put only the concise, auditable reasons required by the output schema into the JSON fields.
- Return exactly one JSON object matching the supplied output schema. No markdown, code fences, commentary, preamble, or trailing text.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GitHub Models stdin/stdout adapter for the Scales command-provider boundary.")
    parser.add_argument("--model", default=os.environ.get("GITHUB_MODELS_MODEL", DEFAULT_MODEL))
    parser.add_argument("--endpoint", default=os.environ.get("GITHUB_MODELS_ENDPOINT", DEFAULT_ENDPOINT))
    parser.add_argument("--max-tokens", type=int, default=8000)
    parser.add_argument("--timeout", type=int, default=180)
    return parser.parse_args()


def read_envelope() -> dict[str, Any]:
    raw = sys.stdin.read()
    if not raw.strip():
        raise ValueError("empty stdin envelope")
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError("stdin envelope must be a JSON object")
    return value


def extract_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                text = item.get("text") or item.get("content")
                if isinstance(text, str):
                    parts.append(text)
        return "".join(parts)
    raise ValueError(f"unexpected model content type: {type(content).__name__}")


def call_model(endpoint: str, token: str, model: str, envelope: dict[str, Any], max_tokens: int, timeout: int) -> dict[str, Any]:
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": "Evaluate the following sealed Scales envelope and return only the required JSON object:\n\n"
                + json.dumps(envelope, ensure_ascii=False, separators=(",", ":")),
            },
        ],
        "temperature": 0,
        "max_tokens": max_tokens,
    }

    request = urllib.request.Request(
        endpoint,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub Models HTTP {exc.code}: {detail}") from exc

    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices:
        raise ValueError(f"GitHub Models response has no choices: {payload!r}")
    message = choices[0].get("message", {})
    text = extract_text(message.get("content")).strip()

    # Strict boundary: do not repair prose/fences into JSON. If the model cannot
    # obey the structured-output contract, that is evidence and the run fails.
    value = json.loads(text)
    if not isinstance(value, dict):
        raise ValueError("model response must be one JSON object")
    return value


def main() -> int:
    args = parse_args()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print("ERROR: GITHUB_TOKEN or GH_TOKEN is required", file=sys.stderr)
        return 2

    try:
        envelope = read_envelope()
        result = call_model(args.endpoint, token, args.model, envelope, args.max_tokens, args.timeout)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    sys.stdout.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
