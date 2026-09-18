# Session handoff — Core-12 recovery, 17 September 2026

**Latest checkpoint, 18 September:** the live reconciliation contract defect is repaired and a new v0.1.1 pack is prepared. Adrian explicitly approved publishing the repair to the experiment branch; remote and CI verification are being recorded in the repair report. Read the final dated update below and [the repair report](../docs/ai-reports/2026-09-18-core12-binding-contract-fix.md). After publication verification, use [restart prompt 02](../docs/ai-prompts/MORAL_CODE_CLAUDE_CORE12_RESTART_02.md) for new Claude execution; earlier handoffs and failed evidence remain historical.

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

## Update — 18 September 2026: first live Claude subscription attempt

Read [the Claude-only overnight report](../docs/ai-reports/2026-09-18-core12-claude-only-overnight-01.md) before acting on anything below.

Verified state after run `CLAUDE-CORE12-20260918T124845Z` (branch `experiment/core12-live-v0.1`, pack digest `sha256:0b9d597a…`, client Claude Code 2.1.276, model `claude-opus-5[1m]` from client metadata, claude.ai sign-in, no API key, overage disabled):

- Inference attempted and returned: yes, seven calls, all exit 0, no tool use, no quota or client errors.
- Full evaluation completed: **no case**. The six CORE-01 role assessments were accepted and persisted. The CORE-01 reconciliation was returned, passes its output schema, names the correct case and role references, but was rejected by the runner's constitutional-binding equality check and the run stopped. CORE-02 to CORE-12 are `not_started`.
- Cause: the action reconciliation schema declares three `constitution` fields; the runner requires the pack's four-field binding including `interpretation_rules_ref`; the action envelope has no `constitution_binding` key for the model to copy. The fixture test passes only because the fake CLI copies the request object verbatim. This is a harness contract defect, not a model, provider or constitutional finding.
- Evidence persisted: yes, under `engine/scales/reference_runner/subscription-runs/CLAUDE-CORE12-20260918T124845Z/`.
- Comparison completed: no. Codex was not run (allowance exhausted). Zero comparable pairs remain.
- Offline tests on Windows: 17 passed, 3 failed for platform reasons in the test harness (shebang fake CLI; `shlex.split` on Windows paths). Nothing was changed.

Next checkpoint: Adrian decides the contract fix (schema, envelope key or runner comparison), adds a regression test whose fake responder returns only schema-declared fields, re-freezes the pack at a new baseline if a frozen source changes, then starts a new run ID with `--case CORE-01` before `--case all`. Do not rerun the existing run ID. No model comparison conclusion or v0.2 adoption is justified.

## Update — 18 September 2026: binding contract repaired, new execution pending

The [binding repair report](../docs/ai-reports/2026-09-18-core12-binding-contract-fix.md) supersedes the pending technical decision above. The schema declares the interpretation-rules reference; action reconciliations receive an explicit binding object; both subscription reconciliation schemas require the complete exact binding. The runtime equality check remains strict. Generic historical fixture compatibility is preserved.

- Red regression reproduced the live mismatch: 3 failed, 19 passed before the repair. Final local Linux suite: 23 passed.
- Windows fake-process invocation and path quoting are corrected; CI now includes Windows. Its receipt is recorded in the repair report when available, and a green local Windows suite is required before inference.
- New pack: `crucible/benchmark/subscription-core12-v0.1.1.json`, digest `sha256:07306d70cf4fceb19eeda337d85066265f8c40dc71d75873c670734841432b7b`, source baseline `a415f6f3df6135e3247152effa1707bbb9fad5cd`.
- All twelve case facts, constitution and interpretation content are unchanged. Old pack and failed ledgers are preserved byte-for-byte. Inspect historical executions with their matching source revision, not by bypassing source-hash checks.
- The last observed account was Claude Max, model `claude-opus-5[1m]`, overage disabled. The new prompt pins that observed model explicitly and verifies current access.
- No new live inference occurred during the repair. Completed cases remain zero until a fresh run succeeds.

Next action: execute `docs/ai-prompts/MORAL_CODE_CLAUDE_CORE12_RESTART_02.md` in Claude. It performs one new CORE-01 trial, inspects the evidence, and automatically proceeds through CORE-02 to CORE-12 once each only if the first trial completes. Maximum 84 new evaluator invocations; stop at the first failure and preserve all outputs. Do not use `--case all` after that first case, which would repeat it. The report goes to `docs/ai-reports/2026-09-18-core12-claude-restart-02.md`. Cross-family comparison, repeatability and constitutional adoption remain pending.

Publication checkpoint: the original approval block was resolved by Adrian's explicit “yes, push it”. The shell's normal Git push then lacked credentials, so the connected GitHub app is publishing the authorised payload. Pack generation uses the actual GitHub source commit `a415f6f3df6135e3247152effa1707bbb9fad5cd`; the repair report records remote readback and CI before execution handoff.
