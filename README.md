# The Moral Code

**A testable moral constitution for human and AI systems.**

The Moral Code is an open project to extract a defensible common moral core from humanity's ethical traditions, philosophy, human-rights thinking, and accumulated experience — then express it in forms that can be read, challenged, tested and applied by both humans and machines.

It is not a religion, an AI ruler, or a claim to moral infallibility.

> **Power should be constrained by moral law, evidence, independent challenge, and the continuing dignity of those subject to it.**

## Start here

For the integration experiment's verified execution status, read [the current session handoff](governance/SESSION_HANDOFF.md). The recovery audit corrects earlier live-testing claims.

The subscription trials have completed zero cases. The [offline UTF-8 transport repair](docs/ai-reports/2026-09-19-core12-utf8-transport-codex-05.md) now saves and sends identical UTF-8 prompt bytes, with LF newlines, independently of the host locale. The current frozen pack is `subscription-core12-v0.1.3.json`, sourced from `1fc927431541f5196d79d8284ea70cb1de1f9240`, with digest `sha256:746a346b5b31314c7e49088b0f6ba058ad33f0a26be839e46860c9e970e63ced`. The earlier [client-integrity repair](docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md) continues to reject Claude exchanges with unsolicited user events or multiple turns, and fails closed on missing or malformed turn metadata.

The [Codex CORE-01 prompt 04 attempt](docs/ai-reports/2026-09-19-core12-codex-core01-04.md) stopped after one evaluator CLI invocation: Codex rejected stdin as invalid UTF-8 before returning any evaluator output. The requested model was `gpt-6-astra`, advertised in the local client catalog; per-call observed model and effective reasoning effort remain unknown. No role was accepted, and reconciliation was not reached. Prompt 04 has been executed and must not be retried automatically.

The [offline repair assignment, prompt 05](docs/ai-prompts/MORAL_CODE_CODEX_UTF8_REPAIR_05.md), is complete and awaits review. All 66 offline tests pass on Windows with cp1252 and UTF-8 mode disabled; strict UTF-8 fake children demonstrated both the old failure and the corrected bytes. The assignment made zero real evaluator/client calls; fake-client success proves transport, not real inference. Historical packs and run evidence, including their original CRLF bytes and prompt digests, remain unchanged. Both providers' trials remain paused. Stop for review; no next agent prompt, retry, fresh CORE-01 or classifier probe is scheduled. Earlier execution prompts and commands are historical.

Read `constitution/MORAL_CORE.md`.

## Structure

- `constitution/` — canonical constitution, interpretation rules and machine-readable principles.
- `crucible/` — hard cases for moral regression testing.
- `engine/` — schemas for future evaluators and decision records.
- `decisions/` — auditable outputs from implementations.
- `research/` — provenance, traditions, contradictions and unresolved questions.
- `governance/` — how the project itself is challenged and changed.

## Design principles

1. Humans and AI are both constrained; neither is morally sovereign.
2. The moral floor is tested before optimisation.
3. There is no single aggregate morality score.
4. Consequential decisions should face adversarial review.
5. Evidence, uncertainty and affected parties must be explicit.
6. Changes to models, prompts, rules or code should rerun the Crucible.
7. The Code itself remains challengeable.

## The Scales

**The Scales** is the planned executable evaluator: proposal + evidence + context → independent adversarial perspectives → principle-by-principle assessment → auditable decision record.

## The Crucible

**The Crucible** is the regression suite. It contains difficult cases designed to expose contradictions, abuse of power, perverse optimisation and moral drift.

## Status

Foundation draft **v0.1.0**.

## Licensing

- Prose, research and constitutional material: **CC BY 4.0**
- Code, schemas and executable reference implementations: **MIT**
