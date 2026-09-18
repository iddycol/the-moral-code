# Session handoff — Core-12 recovery, 17 September 2026

**Latest checkpoint, 18 September:** restart 02 returned three Claude responses but completed zero cases. All three streams contain a synthetic user intervention and report two turns; the old parser admitted two assessments before a trailing-prose failure stopped the third. Both CI jobs passed, but this detection gap was not covered. Read [the independent review](../docs/ai-reports/2026-09-18-core12-client-integrity-review.md) and use [Codex prompt 03](../docs/ai-prompts/MORAL_CODE_CODEX_CLIENT_INTEGRITY_03.md) for an offline repair and new frozen pack. Live trials are paused. Earlier execution prompts are historical; do not rerun them.

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
- Windows fake-process invocation and path quoting are corrected. Published CI passed all 23 tests on both Windows and Ubuntu; the repair report records the job logs and run links. A green local Windows suite is also required before inference.
- New pack: `crucible/benchmark/subscription-core12-v0.1.1.json`, digest `sha256:07306d70cf4fceb19eeda337d85066265f8c40dc71d75873c670734841432b7b`, source baseline `a415f6f3df6135e3247152effa1707bbb9fad5cd`.
- All twelve case facts, constitution and interpretation content are unchanged. Old pack and failed ledgers are preserved byte-for-byte. Inspect historical executions with their matching source revision, not by bypassing source-hash checks.
- The last observed account was Claude Max, model `claude-opus-5[1m]`, overage disabled. The new prompt pins that observed model explicitly and verifies current access.
- No new live inference occurred during the repair. Completed cases remain zero until a fresh run succeeds.

Next action: execute `docs/ai-prompts/MORAL_CODE_CLAUDE_CORE12_RESTART_02.md` in Claude. It performs one new CORE-01 trial, inspects the evidence, and automatically proceeds through CORE-02 to CORE-12 once each only if the first trial completes. Maximum 84 new evaluator invocations; stop at the first failure and preserve all outputs. Do not use `--case all` after that first case, which would repeat it. The report goes to `docs/ai-reports/2026-09-18-core12-claude-restart-02.md`. Cross-family comparison, repeatability and constitutional adoption remain pending.

Publication checkpoint: the original approval block was resolved by Adrian's explicit “yes, push it”. The shell's normal Git push then lacked credentials, so the connected GitHub app published the authorised payload at `0aac9b4ad49d938202ea1805be1163f18b27d9d3`. Pack generation uses the actual GitHub source commit `a415f6f3df6135e3247152effa1707bbb9fad5cd`. All twelve changed file blobs matched remote readback. Scales CI run `35387899485` passed on Windows and Ubuntu, and benchmark binding run `35387899481` passed. This receipt updates documentation only; the restart prompt, pack and tested source are unchanged.

## Update — 18 September 2026 (UTC): restart 02 executed, stopped at the third call

Read [the restart 02 report](../docs/ai-reports/2026-09-18-core12-claude-restart-02.md) before acting on anything below.

Verified state after run `CLAUDE-V011-CORE01-20260918T195549Z` (branch `experiment/core12-live-v0.1`, HEAD `f7db22081d13e0cd3afd01da14ccab0ac4171f67`, pack `subscription-core12-v0.1.1.json` digest `sha256:07306d70…`, source baseline `a415f6f3…`, client Claude Code 2.1.277, requested and observed model `claude-opus-5[1m]`, claude.ai Max, no API key, overage disabled):

- Offline tests on Windows: 23 passed. Prompt entry copy byte-identical to committed blob `fac6b0fb…`.
- Inference attempted and returned: yes, three of the 84 permitted calls, all exit 0, no tool use, no quota or client errors, no model switch, no auxiliary model.
- Full evaluation completed: **no case**. Advocate and guardian assessments for CORE-01 were accepted and persisted. The evidence sceptic returned a schema-valid JSON object followed by markdown prose; the runner recorded `response_format_failure` and stopped. The reconciliation and the corrected binding contract were never reached. CORE-02 to CORE-12 are `not_started` in [the execution index](../engine/scales/reference_runner/subscription-runs/CLAUDE-V011-INDEX-20260918T195549Z.json).
- New finding at the client layer: every call's raw events contain a synthetic user message from Claude Code stating that the model's first response was "stopped by a safety classifier" and withheld, followed by a second attempt (`num_turns = 2` despite `--max-turns 1`). The prior 2.1.276 run has no such events. The frozen runner does not detect this. Whether the cause is the client version or the coordinating session's auto mode is an open hypothesis; no probe call was made.
- Evidence persisted: yes, under `engine/scales/reference_runner/subscription-runs/CLAUDE-V011-CORE01-20260918T195549Z/`, unmodified. No retries, no repairs, no reuse of old-pack responses.
- Comparison completed: no. Codex not invoked; execution kept Claude-only by Adrian's instruction.

Next action: Adrian decides (a) how to isolate the classifier intervention (plain terminal outside Claude Code and auto mode, or client version pin), (b) whether the runner should treat synthetic user events and multi-turn results as contamination, which is a frozen-source change requiring a new pack revision, and (c) whether the format contract needs hardening against trailing prose. Any new attempt uses a new run ID and starts again at `--case CORE-01`. No model comparison conclusion or v0.2 adoption is justified.

## Update — 18 September 2026: independent review and offline Codex repair

The [independent client-integrity review](../docs/ai-reports/2026-09-18-core12-client-integrity-review.md) confirms the published report against all ten raw event streams and reproduces the parser gap offline. Restart-02 Scales CI run `35389709389` has passed on both Windows and Ubuntu.

The next engineering action supersedes the open choices above: reject unsolicited user events and unverifiable/multiple turns before accepting Claude answers, preserve raw evidence, retain strict JSON parsing, and freeze a new pack after focused regressions. The intervention's cause remains unknown. No client downgrade, permission-mode change or live probe is scheduled.

Adrian now has Codex allowance and prefers launching agents from Downloads. [Codex prompt 03](../docs/ai-prompts/MORAL_CODE_CODEX_CLIENT_INTEGRITY_03.md) assigns the offline implementation, tests, pack and publication; evaluator calls permitted by that prompt: zero. The existing project checkout remains `C:\Work\MoralCode\the-moral-code`. After the corrected pack is reviewed, an independent Codex CORE-01 run is the next candidate. Claude trials remain paused. Completed cases are still zero; old evidence and packs remain immutable.
