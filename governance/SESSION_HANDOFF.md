# Session handoff — Core-12 client-integrity repair

**Latest checkpoint:** the [Codex client-integrity repair report](../docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md) records the completed offline detector repair. The final local suite passes all 49 tests. Restart-02 replay rejects all three streams as contamination; all seven original streams remain parseable, and their reconciliation's separate binding failure remains historical. This assignment made zero live evaluator calls. Completed live cases and comparable pairs remain zero.

Published code/pack commit `87d2d348113e64bdf140e2307ce84e186953738e` passed all 49 tests on both Windows and Ubuntu in [Scales CI run 35391448681](https://github.com/iddycol/the-moral-code/actions/runs/35391448681); benchmark binding CI also passed. All seven changed files and the entry prompt matched remote blob readback. The later publication receipt changes documentation only; CI tested the exact commit named here.

The current default pack is `crucible/benchmark/subscription-core12-v0.1.2.json`, frozen from source commit `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6`, with digest `sha256:e3cf63f003952122689f9120899c13aee3c86e93eb14531d5611fa103c6ecfa0`. All 29 source hashes match the committed baseline and all twelve action/Repair reconciliation schemas validate. Case facts, selected actions, Repair packets, constitution, interpretation, prompts and prior evidence remain unchanged.

The next candidate is a separately scoped Codex CORE-01 run on this pack, after verifying a locally available model. No model identifier is selected and no run is launched by this assignment. Codex allowance is available; earlier exhausted-allowance statements are historical. Claude remains paused pending supported investigation of its observed intervention. No automatic retries or client-version/permission-mode experiments are scheduled. Earlier first-run/restart prompts and commands are historical; do not rerun them.

## Read first

1. Root `README.md`.
2. This handoff.
3. [Core-12 recovery audit](../research/reports/2026-09-17-core12-recovery-audit.md).
4. [Workflow evidence](../research/reports/evidence/2026-09-17-core12-recovery/workflow-audit.json).
5. [Benchmark](../crucible/benchmark/BENCHMARK_V0_1.md), [binding profiles](../crucible/benchmark/BINDING_PROFILES_V0_1.md), then the implementation relevant to the next task.
6. [Client-integrity repair report](../docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md) and current [subscription trial guide](../engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md).

Use repository evidence over prior conversational status claims.

## Current working branch

`experiment/core12-live-v0.1` combines the research and implementation for integration. `main` remains the v0.1.0 foundation; draft research/design/implementation PRs remain separate.

The recovery started from `6843dd48f4b9ffc33acbfe2cb0e155cfc41e0515`. Read the current branch head before making changes.

## Historical recovery position — 17 September 2026

- Research packets and stable Core-12 definitions exist.
- Five broken action selectors are corrected in binding revision v0.1.1.
- Ten action requests generate and validate.
- Twenty offline runner tests pass, including seven subscription-trial checks.
- Repair code and schemas exist; the two hosted Repair attempts returned provider HTTP 410 errors.
- No completed hosted-model decision ledgers were found on either the inspected integration or implementation branch.
- Repeatability, pressure resistance and cross-family comparison have not been demonstrated.
- GitHub Models is retired according to its official documentation. Do not treat its old brownout error message as a reason to retry until green.

The previous handoff's successful-live-testing and saved-output claims are superseded by this audit. Three committed file-backed fixture runs remain controls only.

## Historical proposed checkpoint — superseded, not execution instructions

At this checkpoint Adrian had ChatGPT Pro and Claude Pro and chose to continue using those subscriptions. The [subscription trial guide](../engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md) provided a frozen Core-12 pack, local CLI execution, raw-output preservation, strict result intake and case comparison. The proposal was to start with CORE-01 once per family and inspect it before launching the full batch. This proposal is superseded by the latest checkpoint above.

The downloadable local-agent entry point [MORAL_CODE_FIRST_RUN_02.md](../docs/ai-prompts/MORAL_CODE_FIRST_RUN_02.md) then superseded revision 01; both are now historical. It proposed launching Codex in `C:\Work\MoralCode`, checking the checkout and GitHub publication access, and preserving the Azure DevOps setup. At that checkpoint local GitHub access was unverified; this chat's GitHub connection was not evidence of local authentication.

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

## Historical update — 18 September 2026: first live Claude subscription attempt

Read [the Claude-only overnight report](../docs/ai-reports/2026-09-18-core12-claude-only-overnight-01.md) before acting on anything below.

Verified state after run `CLAUDE-CORE12-20260918T124845Z` (branch `experiment/core12-live-v0.1`, pack digest `sha256:0b9d597a…`, client Claude Code 2.1.276, model `claude-opus-5[1m]` from client metadata, claude.ai sign-in, no API key, overage disabled):

- Inference attempted and returned: yes, seven calls, all exit 0, no tool use, no quota or client errors.
- Full evaluation completed: **no case**. The six CORE-01 role assessments were accepted and persisted. The CORE-01 reconciliation was returned, passes its output schema, names the correct case and role references, but was rejected by the runner's constitutional-binding equality check and the run stopped. CORE-02 to CORE-12 are `not_started`.
- Cause: the action reconciliation schema declares three `constitution` fields; the runner requires the pack's four-field binding including `interpretation_rules_ref`; the action envelope has no `constitution_binding` key for the model to copy. The fixture test passes only because the fake CLI copies the request object verbatim. This is a harness contract defect, not a model, provider or constitutional finding.
- Evidence persisted: yes, under `engine/scales/reference_runner/subscription-runs/CLAUDE-CORE12-20260918T124845Z/`.
- Comparison completed: no. Codex was not run (allowance exhausted). Zero comparable pairs remain.
- Offline tests on Windows: 17 passed, 3 failed for platform reasons in the test harness (shebang fake CLI; `shlex.split` on Windows paths). Nothing was changed.

Then-proposed checkpoint (superseded): decide the contract fix, add a regression test whose fake responder returns only schema-declared fields, re-freeze the pack at a new baseline if a frozen source changes, then start a new run ID with CORE-01. The later entries record what actually happened; this is not current execution authorisation. No model comparison conclusion or v0.2 adoption is justified.

## Historical update — 18 September 2026: binding contract repaired, new execution pending

The [binding repair report](../docs/ai-reports/2026-09-18-core12-binding-contract-fix.md) supersedes the pending technical decision above. The schema declares the interpretation-rules reference; action reconciliations receive an explicit binding object; both subscription reconciliation schemas require the complete exact binding. The runtime equality check remains strict. Generic historical fixture compatibility is preserved.

- Red regression reproduced the live mismatch: 3 failed, 19 passed before the repair. Final local Linux suite: 23 passed.
- Windows fake-process invocation and path quoting are corrected. Published CI passed all 23 tests on both Windows and Ubuntu; the repair report records the job logs and run links. A green local Windows suite is also required before inference.
- New pack: `crucible/benchmark/subscription-core12-v0.1.1.json`, digest `sha256:07306d70cf4fceb19eeda337d85066265f8c40dc71d75873c670734841432b7b`, source baseline `a415f6f3df6135e3247152effa1707bbb9fad5cd`.
- All twelve case facts, constitution and interpretation content are unchanged. Old pack and failed ledgers are preserved byte-for-byte. Inspect historical executions with their matching source revision, not by bypassing source-hash checks.
- The last observed account was Claude Max, model `claude-opus-5[1m]`, overage disabled. The new prompt pins that observed model explicitly and verifies current access.
- No new live inference occurred during the repair. Completed cases remain zero until a fresh run succeeds.

Then-authorised action (executed and now historical): `docs/ai-prompts/MORAL_CODE_CLAUDE_CORE12_RESTART_02.md` allowed one new CORE-01 trial and progression through CORE-02 to CORE-12 only if that trial completed, with a maximum of 84 new evaluator invocations. It stopped after the third invocation, as recorded in `docs/ai-reports/2026-09-18-core12-claude-restart-02.md`; it must not be rerun. Cross-family comparison, repeatability and constitutional adoption remain pending.

Publication checkpoint: the original approval block was resolved by Adrian's explicit “yes, push it”. The shell's normal Git push then lacked credentials, so the connected GitHub app published the authorised payload at `0aac9b4ad49d938202ea1805be1163f18b27d9d3`. Pack generation uses the actual GitHub source commit `a415f6f3df6135e3247152effa1707bbb9fad5cd`. All twelve changed file blobs matched remote readback. Scales CI run `35387899485` passed on Windows and Ubuntu, and benchmark binding run `35387899481` passed. This receipt updates documentation only; the restart prompt, pack and tested source are unchanged.

## Historical update — 18 September 2026 (UTC): restart 02 executed, stopped at the third call

Read [the restart 02 report](../docs/ai-reports/2026-09-18-core12-claude-restart-02.md) before acting on anything below.

Verified state after run `CLAUDE-V011-CORE01-20260918T195549Z` (branch `experiment/core12-live-v0.1`, HEAD `f7db22081d13e0cd3afd01da14ccab0ac4171f67`, pack `subscription-core12-v0.1.1.json` digest `sha256:07306d70…`, source baseline `a415f6f3…`, client Claude Code 2.1.277, requested and observed model `claude-opus-5[1m]`, claude.ai Max, no API key, overage disabled):

- Offline tests on Windows: 23 passed. Prompt entry copy byte-identical to committed blob `fac6b0fb…`.
- Inference attempted and returned: yes, three of the 84 permitted calls, all exit 0, no tool use, no quota or client errors, no model switch, no auxiliary model.
- Full evaluation completed: **no case**. Advocate and guardian assessments for CORE-01 were accepted and persisted. The evidence sceptic returned a schema-valid JSON object followed by markdown prose; the runner recorded `response_format_failure` and stopped. The reconciliation and the corrected binding contract were never reached. CORE-02 to CORE-12 are `not_started` in [the execution index](../engine/scales/reference_runner/subscription-runs/CLAUDE-V011-INDEX-20260918T195549Z.json).
- New finding at the client layer: every call's raw events contain a synthetic user message from Claude Code stating that the model's first response was "stopped by a safety classifier" and withheld, followed by a second attempt (`num_turns = 2` despite `--max-turns 1`). The prior 2.1.276 run has no such events. The frozen runner does not detect this. Whether the cause is the client version or the coordinating session's auto mode is an open hypothesis; no probe call was made.
- Evidence persisted: yes, under `engine/scales/reference_runner/subscription-runs/CLAUDE-V011-CORE01-20260918T195549Z/`, unmodified. No retries, no repairs, no reuse of old-pack responses.
- Comparison completed: no. Codex not invoked; execution kept Claude-only by Adrian's instruction.

Then-open questions (superseded): how to investigate the classifier intervention, whether synthetic user events and multiple turns should invalidate an exchange, and whether trailing prose required a changed format contract. The subsequent review and repair resolved the parser requirements while preserving exact JSON parsing. The proposed client-version/mode probes were not performed and are not authorised by the current handoff. No model comparison conclusion or v0.2 adoption is justified.

## Historical update — 18 September 2026: independent review and offline Codex assignment

The [independent client-integrity review](../docs/ai-reports/2026-09-18-core12-client-integrity-review.md) confirms the published report against all ten raw event streams and reproduces the parser gap offline. Restart-02 Scales CI run `35389709389` has passed on both Windows and Ubuntu.

The assigned engineering action superseded the open choices above: reject unsolicited user events and unverifiable/multiple turns before accepting Claude answers, preserve raw evidence, retain strict JSON parsing, and freeze a new pack after focused regressions. The intervention's cause remains unknown. No client downgrade, permission-mode change or live probe was scheduled.

Adrian now has Codex allowance and prefers launching agents from Downloads. [Codex prompt 03](../docs/ai-prompts/MORAL_CODE_CODEX_CLIENT_INTEGRITY_03.md) assigns the offline implementation, tests, pack and publication; evaluator calls permitted by that prompt: zero. The existing project checkout remains `C:\Work\MoralCode\the-moral-code`. After the corrected pack is reviewed, an independent Codex CORE-01 run is the next candidate. Claude trials remain paused. Completed cases are still zero; old evidence and packs remain immutable.

## Current update — offline client-integrity repair completed

The [repair report](../docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md) records the evidence and publication status. The existing suite began at 23 passing tests; focused regressions demonstrated the gap with 24 failures and 25 passes before production edits. After the source commit, the intermediate suite had 48 passes and the expected missing-new-pack failure. Generating the matching v0.1.2 pack restored the full suite to 49 passes. Independent review found no blocking issue in the repair.

Claude acceptance now rejects structurally identified unsolicited `user` events as `protocol_contamination`, including synthetic events even when a result claims one turn. Successful results require a real integer `num_turns` equal to one: multiple turns are `protocol_contamination`; missing, boolean, string, non-positive or otherwise malformed values are `client_output_error` with precise details. These gates precede final JSON acceptance. Multiple assistant blocks alone do not count as multiple turns. A clean single-turn answer with trailing prose remains `response_format_failure`; no response repair or retry is introduced. The Codex parser keeps its existing protections without borrowing Claude metadata rules.

Rejected exchanges retain raw events and available final text unmodified, without accepted role/decision files. The process-boundary regression verifies that a contaminated first response records the failure stage and stops later roles, reconciliation and cases. Offline replay used temporary paths; historical streams, manifests, indexes and both prior packs remain immutable. This repair detects the observed intervention but does not establish its cause, reveal withheld content, or equate CLI invocations with underlying model requests.

The v0.1.2 source baseline is `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6`; pack digest is `sha256:e3cf63f003952122689f9120899c13aee3c86e93eb14531d5611fa103c6ecfa0`. All 29 source hashes match that commit and all twelve reconciliation schemas preserve the full binding. The next candidate remains separately scoped Codex CORE-01 with a verified locally available model. No model is selected, no evaluator is launched, and Claude remains paused pending supported investigation.
