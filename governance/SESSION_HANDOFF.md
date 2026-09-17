# Session handoff — Core-12 recovery, 17 September 2026

## Read first

1. Root `README.md`.
2. This handoff.
3. [Core-12 recovery audit](../research/reports/2026-09-17-core12-recovery-audit.md).
4. [Workflow evidence](../research/reports/evidence/2026-09-17-core12-recovery/workflow-audit.json).
5. [Benchmark](../crucible/benchmark/BENCHMARK_V0_1.md), [binding profiles](../crucible/benchmark/BINDING_PROFILES_V0_1.md), then the implementation relevant to the next task.

Use repository evidence over prior conversational status claims.

## Current working branch

`experiment/core12-live-v0.1` combines the research and implementation for integration. `main` remains the v0.1.0 foundation; draft research/design/implementation PRs remain separate.

The recovery started from `6843dd48f4b9ffc33acbfe2cb0e155cfc41e0515`. Read the current branch head before making changes.

## Verified position

- Research packets and stable Core-12 definitions exist.
- Five broken action selectors are corrected in binding revision v0.1.1.
- Ten action requests generate and validate.
- Twenty offline runner tests pass, including seven subscription-trial checks.
- Repair code and schemas exist; the two hosted Repair attempts returned provider HTTP 410 errors.
- No completed hosted-model decision ledgers were found on either the inspected integration or implementation branch.
- Repeatability, pressure resistance and cross-family comparison have not been demonstrated.
- GitHub Models is retired according to its official documentation. Do not treat its old brownout error message as a reason to retry until green.

The previous handoff's successful-live-testing and saved-output claims are superseded by this audit. Three committed file-backed fixture runs remain controls only.

## Next concrete checkpoint

Adrian has ChatGPT Pro and Claude Pro and chose to continue using those subscriptions. The [subscription trial guide](../engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md) now provides a frozen Core-12 pack, local CLI execution, raw-output preservation, strict result intake and case comparison. Start with CORE-01 once per family; inspect it before launching the full batch.

Use the downloadable local-agent entry point [MORAL_CODE_FIRST_RUN_02.md](../docs/ai-prompts/MORAL_CODE_FIRST_RUN_02.md), superseding revision 01 for new execution. Adrian launches Codex in the suggested `C:\Work\MoralCode` workspace and instructs it to read the saved prompt. His local work has used Azure DevOps; GitHub access on that computer is unverified. Revision 02 explicitly checks GitHub checkout and publication access, starts browser sign-in only when needed, and preserves the Azure DevOps setup. This chat's GitHub connection is not evidence of local authentication.

The current ChatGPT workspace has neither CLI installed. The preparation is offline-tested; it is not completed model testing. Execution must happen on a machine with the official CLIs signed in to Adrian's subscriptions. Do not ask for API purchases or credentials in chat, export tokens, or claim this workspace can control the separate Claude account.

Subscription outputs use `engine/scales/reference_runner/subscription-runs/`, separate from the old hosted-model findings generator. Persist both successes and failures before making any comparison claim. The trial has seven offline checks (twenty runner tests total), including action and Repair process boundaries, tamper rejection, role identity, retained invalid answers and preflight failure classification.

No model comparison conclusion or v0.2 adoption is justified yet. Do not expand the benchmark while this execution gap remains.

## Report convention

Always distinguish:

- code written;
- offline tests passed;
- inference attempted;
- inference returned;
- full evaluation completed;
- evidence persisted;
- comparison completed;
- human constitutional adoption.

An Actions success label is not sufficient evidence for any of the later stages.
