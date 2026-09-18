# The Moral Code

**A testable moral constitution for human and AI systems.**

The Moral Code is an open project to extract a defensible common moral core from humanity's ethical traditions, philosophy, human-rights thinking, and accumulated experience — then express it in forms that can be read, challenged, tested and applied by both humans and machines.

It is not a religion, an AI ruler, or a claim to moral infallibility.

> **Power should be constrained by moral law, evidence, independent challenge, and the continuing dignity of those subject to it.**

## Start here

For the integration experiment's verified execution status, read [the current session handoff](governance/SESSION_HANDOFF.md). The recovery audit corrects earlier live-testing claims.

The subscription trials have completed zero cases. The [offline client-integrity repair](docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md) now rejects Claude exchanges with unsolicited user events or multiple turns before accepting their answers, and fails closed on missing or malformed turn metadata. The current frozen pack is `subscription-core12-v0.1.2.json`, sourced from `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6`, with digest `sha256:e3cf63f003952122689f9120899c13aee3c86e93eb14531d5611fa103c6ecfa0`.

The repair and its review made zero live evaluator calls. The next step is [Codex CORE-01 prompt 04](docs/ai-prompts/MORAL_CODE_CODEX_CORE01_04.md): verify local access to `gpt-6-astra`, run one case on the unchanged pack with at most seven evaluator invocations, then stop for review. Claude remains paused pending supported investigation of the observed intervention. Earlier first-run and restart prompts and commands are historical.

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
