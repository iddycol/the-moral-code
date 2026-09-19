# The Moral Code

**A testable moral constitution for human and AI systems.**

The Moral Code is an open project to extract a defensible common moral core from humanity's ethical traditions, philosophy, human-rights thinking, and accumulated experience — then express it in forms that can be read, challenged, tested and applied by both humans and machines.

It is not a religion, an AI ruler, or a claim to moral infallibility.

> **Power should be constrained by moral law, evidence, independent challenge, and the continuing dignity of those subject to it.**

## Start here

**Project paused:** correction 11 was completed on `experiment/core12-provenance-v0.1.4` and independently reviewed. Read the [canonical safe-stop checkpoint](https://github.com/iddycol/the-moral-code/blob/e8b7d8d399dbe21dbaca37480a6cfbf502535ae6/governance/SAFE_STOP_2026-09-19.md). The reviewed candidate has no runnable new pack, six remaining admission blockers and low documentation finding CR12-D01. No evaluator calls, pack freeze, merge, interpretation adoption or Claude restart is scheduled. Prompt 11 is historical; do not execute it again. Resume only when Adrian asks.

For the integration experiment's verified execution status, read [the current session handoff](governance/SESSION_HANDOFF.md). The recovery audit corrects earlier live-testing claims.

The [remaining Codex Core-12 batch](docs/ai-reports/2026-09-19-core12-codex-remaining-07.md) completed **11 new client-workflow cases in exactly 77 evaluator CLI invocations**. With [historical CORE-01](docs/ai-reports/2026-09-19-core12-codex-core01-06.md), **all 12 cases are complete**. Every new case passed evidence review. Nine new action decisions comprise six blocks and three conditional permissions; both Repair packages are conditionally permissible, with CORE-12 requiring revision before amnesty grants. Role disagreement and substantive uncertainties remain in the report.

Requested model: `gpt-6-astra`, advertised locally using Codex CLI `0.155.0` and ChatGPT sign-in. Per-call observed model and effective reasoning effort remain unknown. This is completed client-workflow evidence with an identity limitation; comparable pairs remain zero and no repeatability or adoption claim follows.

The unchanged frozen pack is `subscription-core12-v0.1.3.json`, sourced from `1fc927431541f5196d79d8284ea70cb1de1f9240`, with digest `sha256:746a346b5b31314c7e49088b0f6ba058ad33f0a26be839e46860c9e970e63ced`. All 66 local tests passed before the batch. Frozen sources, packs and historical evidence remain unchanged.

[Prompt 07](docs/ai-prompts/MORAL_CODE_CODEX_REMAINING_CORE12_07.md) is historical. The [source audit and proposal 10](docs/ai-reports/2026-09-19-core12-provenance-proposal-10.md) identifies four full-input identity disclosures, a future-disaster cue and decision-cutoff/Repair-design limitations. **Next: [Codex prompt 11](docs/ai-prompts/MORAL_CODE_CODEX_BENCHMARK_CORRECTION_11.md), an offline benchmark-correction candidate with zero evaluator calls.** The [interpretation proposal](docs/proposals/CORE12_INTERPRETATION_PROPOSAL_10.md) is not adopted. Claude and all further trials remain paused.

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
