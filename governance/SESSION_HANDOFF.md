# Session handoff — UTF-8 repair reviewed, fresh Codex CORE-01 prepared

**Current action:** [readiness review 06](../docs/ai-reports/2026-09-19-core12-codex-core01-readiness-06.md) passed after inspecting the repair, reproducing all 66 tests and verifying the source/pack. Use [Codex prompt 06](../docs/ai-prompts/MORAL_CODE_CODEX_CORE01_06.md) from Downloads for one fresh CORE-01 on v0.1.3, at most seven evaluator CLI invocations, then stop for review even on success. The model remains `gpt-6-astra`, conditional on local availability. Prompt 05's stop-for-review checkpoint is satisfied; its execution restrictions remain historical. No live run has been launched here, the failed run must not be resumed, and Claude remains paused.

**Latest checkpoint:** the runner saves and sends one identical UTF-8 prompt payload, with LF newlines, and preserves stdout/stderr as raw bytes. The local Windows suite passes all 66 tests with no skips using native cp1252 and Python UTF-8 mode disabled. Strict fake children captured the old invalid byte at offset 1320 before the fix and verified saved-prompt/stdin/digest equality afterward, including accented text, curly punctuation, CJK and emoji. Independent patch review found no blocking issue. This proves the transport contract offline; completed live cases and comparable pairs remain zero.

The current default pack is `crucible/benchmark/subscription-core12-v0.1.3.json`, frozen from source commit `1fc927431541f5196d79d8284ea70cb1de1f9240`, with digest `sha256:746a346b5b31314c7e49088b0f6ba058ad33f0a26be839e46860c9e970e63ced`. All 29 source hashes match that commit and all twelve reconciliation schemas validate. Case facts, selected actions, Repair packets, constitution, interpretation, role contracts, prompt prefix and JSON serialization are unchanged. The repair report records pack verification and publication status; any publication receipt must distinguish its exact CI-tested commit from later documentation commits.

The [Codex CORE-01 report](../docs/ai-reports/2026-09-19-core12-codex-core01-04.md) remains the latest live-attempt record: one evaluator CLI invocation stopped at advocate because stdin was not valid UTF-8. No evaluator output, accepted role or decision was produced; reconciliation was not reached. Requested model was `gpt-6-astra`; locally advertised availability was verified, but per-call observed model and effective reasoning effort remain unknown. [Prompt 04](../docs/ai-prompts/MORAL_CODE_CODEX_CORE01_04.md) has been executed and stopped and is historical. CORE-02 through CORE-12 remain `not_started` and outside scope.

All 98 historical subscription-run files and the three prior packs remain byte-for-byte unchanged. New v0.1.3 prompts use UTF-8 without a BOM, LF line endings and one trailing LF; `prompt.txt`, stdin and the recorded digest refer to the same bytes. Historical CRLF artifacts retain their original valid byte digests. No global encoding settings, client settings, CLI flags, model selection or acceptance rules were changed.

The earlier [client-integrity repair](../docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md) continues to reject unsolicited Claude user events and malformed/multiple turns before accepting JSON. Its replay findings and the original reconciliation's binding failure remain historical. Claude's intervention cause and withheld content remain unknown.

## Read first

1. Root `README.md`.
2. This handoff.
3. [Core-12 recovery audit](../research/reports/2026-09-17-core12-recovery-audit.md).
4. [Workflow evidence](../research/reports/evidence/2026-09-17-core12-recovery/workflow-audit.json).
5. [Benchmark](../crucible/benchmark/BENCHMARK_V0_1.md), [binding profiles](../crucible/benchmark/BINDING_PROFILES_V0_1.md), then the implementation relevant to the next task.
6. [UTF-8 repair report](../docs/ai-reports/2026-09-19-core12-utf8-transport-codex-05.md), [client-integrity repair report](../docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md) and current [subscription trial guide](../engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md).

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

## Historical update — offline client-integrity repair completed

The [repair report](../docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md) records the evidence and publication status. The existing suite began at 23 passing tests; focused regressions demonstrated the gap with 24 failures and 25 passes before production edits. After the source commit, the intermediate suite had 48 passes and the expected missing-new-pack failure. Generating the matching v0.1.2 pack restored the full suite to 49 passes. Independent review found no blocking issue in the repair.

Claude acceptance now rejects structurally identified unsolicited `user` events as `protocol_contamination`, including synthetic events even when a result claims one turn. Successful results require a real integer `num_turns` equal to one: multiple turns are `protocol_contamination`; missing, boolean, string, non-positive or otherwise malformed values are `client_output_error` with precise details. These gates precede final JSON acceptance. Multiple assistant blocks alone do not count as multiple turns. A clean single-turn answer with trailing prose remains `response_format_failure`; no response repair or retry is introduced. The Codex parser keeps its existing protections without borrowing Claude metadata rules.

Rejected exchanges retain raw events and available final text unmodified, without accepted role/decision files. The process-boundary regression verifies that a contaminated first response records the failure stage and stops later roles, reconciliation and cases. Offline replay used temporary paths; historical streams, manifests, indexes and both prior packs remain immutable. This repair detects the observed intervention but does not establish its cause, reveal withheld content, or equate CLI invocations with underlying model requests.

The v0.1.2 source baseline is `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6`; pack digest is `sha256:e3cf63f003952122689f9120899c13aee3c86e93eb14531d5611fa103c6ecfa0`. All 29 source hashes match that commit and all twelve reconciliation schemas preserve the full binding. At repair completion no model had been selected and no evaluator was launched; the subsequent dated handoff below specifies the next trial. Claude remains paused pending supported investigation.

Historical publication receipt: code/pack commit `87d2d348113e64bdf140e2307ce84e186953738e` passed all 49 tests on both Windows and Ubuntu in [Scales CI run 35391448681](https://github.com/iddycol/the-moral-code/actions/runs/35391448681); benchmark binding CI also passed. All seven changed files and the entry prompt matched remote blob readback. Its later publication receipt changed documentation only; that CI tested the exact commit named here.

## Historical update — 18 September 2026 UTC: one-case Codex handoff prepared

The [readiness review](../docs/ai-reports/2026-09-18-core12-codex-core01-readiness-04.md) reverified the repaired source and pack, reproduced 49 passing offline tests and confirmed successful Windows/Ubuntu CI. [Prompt 04](../docs/ai-prompts/MORAL_CODE_CODEX_CORE01_04.md) was then prepared as the execution entry point, launched from Downloads against `C:\Work\MoralCode\the-moral-code`; its subsequent attempted execution is recorded below.

The then-authorised scope was one CORE-01 attempt with explicit `--model gpt-6-astra`, after non-inference local availability and exact-flag checks: maximum seven evaluator CLI invocations, no smoke calls, retries or further cases. Requested model and per-call observed identity were to be reported separately; missing metadata remains unverified. The runner, packs and historical evidence were unchanged by this handoff. Claude remained paused. The subsequent result is recorded in `docs/ai-reports/2026-09-19-core12-codex-core01-04.md`.

## Historical update — 18 September 2026 UTC / 19 September Brisbane: Codex CORE-01 attempted and stopped

Read [the prompt 04 result report](../docs/ai-reports/2026-09-19-core12-codex-core01-04.md) and [execution index](../engine/scales/reference_runner/subscription-runs/CODEX-V012-INDEX-20260918T204353Z.json). Run `CODEX-V012-CORE01-20260918T204353Z` used branch `experiment/core12-live-v0.1` at HEAD `27f186fb2a3ce700d1a21b7b03d2e488c2ffcff9`, the unchanged v0.1.2 pack and source baseline `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6`. The execution started at `2026-09-18T20:44:04.9764245Z` and ended at `2026-09-18T20:44:05.8257237Z` (19 September, UTC+10 in Brisbane).

- The local Windows test gate passed all 49 tests in 4.53 seconds. Codex CLI was `0.155.0`, signed in through ChatGPT. Non-inference local model metadata advertised `gpt-6-astra` from a catalog cached at `2026-09-18T20:42:11.776811200Z`; this establishes advertised availability, not server acceptance.
- The unchanged runner was executed once with explicit `--model gpt-6-astra`. It saved one evaluator CLI invocation, for the advocate role, and stopped as `client_or_provider_error` with CLI exit 1. Stderr states: `Failed to read prompt from stdin: input is not valid UTF-8 (invalid byte at offset 1320).` Stdout is empty, no final response or accepted role exists, and no decision was produced. The repaired reconciliation contract was not reached or accepted.
- The responsible observed layer is client stdin decoding. Offline inspection found Python 3.12 using locale `cp1252` with UTF-8 mode disabled, and the runner uses subprocess text mode without an explicit encoding. The saved prompt itself is UTF-8. Encoding that prompt as cp1252 with Windows newline translation reproduces byte `0x97` at offset 1320, consistent with the failure. Actual subprocess stdin bytes were not captured, so that reproduction is supporting evidence, not a captured byte trace.
- Requested model: `gpt-6-astra`; per-call observed model and effective reasoning effort: unknown. The failed call returned no model or usage metadata, and the invocation count does not establish a model-request count. Completed cases: zero. All eleven later cases remain `not_started` and outside scope. Claude was not invoked and remains paused.
- Raw unsuccessful evidence was preserved without a retry, response repair or source/pack change. Publication verification is recorded in the result report; this entry makes no claim about a new CI run.

Publication receipt: `554b40a6bd6b4141b86cbfa4868a4b5b50d87eb8` was pushed normally to the integration branch. All 17 changed file blobs, including the report, index, manifest and raw evidence, matched remote byte readback. [Scales CI run 35393609548](https://github.com/iddycol/the-moral-code/actions/runs/35393609548) passed all 49 tests on Windows and Ubuntu at that commit. The later receipt changes documentation only; the failed attempt and its evidence remain unchanged.

Then-required action, now completed by prompt 05: investigate and repair UTF-8 transport offline, demonstrate a meaningful Windows regression and freeze a new pack from the repaired source. Prompt 04 authorises no retry; the unsuccessful run remains unchanged. No cross-provider comparison, repeatability finding, aggregate morality score or v0.2 adoption follows from this failed attempt.

## Update — 19 September 2026: offline UTF-8 transport repair completed

The [repair report](../docs/ai-reports/2026-09-19-core12-utf8-transport-codex-05.md) records the full regression evidence and publication status. The existing suite began at 49 passes. The locally committed red checkpoint reproduced the defect with 15 failures and 51 passes before production edits. After the source repair, 65 tests passed and the committed-pack test failed as expected because v0.1.3 had not yet been generated. Freezing the pack from source commit `1fc927431541f5196d79d8284ea70cb1de1f9240` restored the complete suite to 66 passes in 8.43 seconds on Windows, with no skipped tests.

Both provider paths run strict UTF-8 fake children that capture raw stdin before decoding. The native Windows run used Python 3.12.10, cp1252 and UTF-8 mode disabled. Historical-envelope and wider-Unicode cases verify exact saved/wire bytes and digests; response parsing preserves Unicode. Binary logs retain partial and invalid bytes on timeout, nonzero exit or strict decoding failure. Existing action/Repair, identity, binding, turn/user, tool/error and no-retry checks remain in force. The fake clients' explicit UTF-8 contract replaces their prior locale assumption without changing acceptance rules.

The new pack digest is `sha256:746a346b5b31314c7e49088b0f6ba058ad33f0a26be839e46860c9e970e63ced`. All three earlier packs and all 98 historical run files remain unchanged, including CRLF evidence and its original digests. The assignment made zero real evaluator/client calls and did not change client or machine settings. Completed live cases remain zero. Stop for review here; both providers stay paused and no next agent prompt or trial is scheduled.

Publication receipt: complete green code/pack/report/docs commit `e5cb0e7f9382b4e1f381a69393dd80269353ff79` was pushed normally. [Scales CI run 35396229116](https://github.com/iddycol/the-moral-code/actions/runs/35396229116) passed all 66 tests with no skips on Ubuntu (5.09s) and Windows (12.01s); [benchmark binding CI](https://github.com/iddycol/the-moral-code/actions/runs/35396229147) also passed. All seven changed files and the entry prompt matched remote byte readback, and the published branch head matched that commit. This later receipt changes only the report and handoff; source, tests, pack and historical evidence remain unchanged. The exact CI-tested commit is the one named here, not the later documentation receipt. Stop for review.
