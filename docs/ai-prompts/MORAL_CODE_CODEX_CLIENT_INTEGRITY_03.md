# Moral Code — Codex client-integrity repair, offline only

You are Adrian Colquhoun's local Codex engineering agent. Fix the verified subscription-runner evidence gap, prove the repair offline, freeze a new pack and publish the result. This is an implementation assignment with regression tests and review, not an evaluator run. Finish the routine repository, testing and publication work autonomously.

## Entry point and authority

- Adrian starts Codex in his Windows Downloads directory. Read this entire downloaded file there; do not ask him to move it.
- Suggested entry path: `C:\Users\Adrian\Downloads\MORAL_CODE_CODEX_CLIENT_INTEGRITY_03.md`.
- Existing project checkout: `C:\Work\MoralCode\the-moral-code`.
- Repository: `https://github.com/iddycol/the-moral-code.git`.
- Integration branch: `experiment/core12-live-v0.1`; preserve `main`.
- Evidence checkpoint: `2c009026e9a12a847bdbdfdc570728729f256528`. Later prompt/review documentation commits are expected; verify current remote state.
- Committed entry prompt: `docs/ai-prompts/MORAL_CODE_CODEX_CLIENT_INTEGRITY_03.md`. Verify the downloaded text matches its committed blob and record the blob and introducing commit.
- Current frozen pack: `crucible/benchmark/subscription-core12-v0.1.1.json`, digest `sha256:07306d70cf4fceb19eeda337d85066265f8c40dc71d75873c670734841432b7b`, source baseline `a415f6f3df6135e3247152effa1707bbb9fad5cd`.
- Codex credits are available. Earlier statements that its allowance is exhausted are historical.

**Evaluator invocation budget for this assignment: zero.** Your coordinating Codex session is ordinary engineering work and consumes its normal allowance. Do not invoke either subscription client as an evaluator, perform live smoke calls, retry a failed case, change Claude versions or permission modes, disable safeguards, alter authentication, or enable paid extra usage. The objective is reliable detection, not suppressing or evading the observed intervention. Live Claude work is paused; a separate Codex benchmark handoff follows after this repair is reviewed.

## Reconstruct the exact state

Inspect repository identity, Git status, remotes, branch and applicable `AGENTS.md`/`CLAUDE.md`. Fetch current history. Use a clean fast-forwarded checkout or an isolated worktree/branch if the existing one contains unrelated work. Preserve concurrent changes and Azure DevOps configuration. Do not reset, stash, force-push or discard work.

Read `README.md`, latest `governance/SESSION_HANDOFF.md`, and:

1. `docs/ai-reports/2026-09-18-core12-client-integrity-review.md`.
2. `docs/ai-reports/2026-09-18-core12-claude-restart-02.md`.
3. `docs/ai-reports/2026-09-18-core12-binding-contract-fix.md`.
4. `engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md`.
5. `subscription_trial.py`, its tests, related envelope builders and `.github/workflows/scales-reference-runner.yml`.
6. The actual raw events and manifests in both `engine/scales/reference_runner/subscription-runs/CLAUDE-V011-CORE01-20260918T195549Z/` and `CLAUDE-CORE12-20260918T124845Z/`.

Verify the existing pack and frozen source hashes before edits. Use the working `.venv\Scripts\python.exe` if present; otherwise create an isolated environment from existing requirements. Record the initial HEAD, OS and interpreter. Run the existing suite once to establish its baseline:

```text
<python> -m pytest -q engine/scales/reference_runner/tests
```

The reviewed baseline has 23 tests. Independently reproduce the parsing gap using the saved event streams and temporary output paths. This is offline replay only; never write into historical run directories.

## Observations to verify, not assumptions to promote

All three restart-02 streams contain an unsolicited `user` event with `isSynthetic: true`; the message reports a withheld response and classifier intervention. Each successful result reports `num_turns: 2`, despite the invocation requesting one. The original seven streams contain no such user event and report one turn. Multiple streamed assistant blocks can belong to a single message, so counting assistant events is not a turn-count test.

The current parser accepts the latest advocate and guardian. The evidence sceptic fails because its complete JSON object is followed by 2,279 characters of prose. The intervention's cause and withheld content are unknown. Do not claim client version or parent auto mode is proven responsible, or that three CLI invocations equal three underlying model requests.

## Acceptance contract and focused regressions

Commit focused regression tests demonstrating the actual gap before changing production code. Keep the red checkpoint local until a complete green repair can be published. Show failures for the intended reason, not merely an unrelated source-hash mismatch.

Implement the smallest repair at the CLI event/acceptance boundary:

- For the sealed Claude invocation, unsolicited `user` events invalidate the exchange as `protocol_contamination`. Detect event structure; do not search for one English classifier phrase. A synthetic event still fails if the reported turn count misleadingly says one.
- Require the successful Claude result to carry a real integer `num_turns` equal to one. Reject multiple turns as `protocol_contamination`; missing, boolean, string, non-positive or otherwise malformed counts are unverifiable client output and must fail closed with a precise category/detail. Python booleans must not pass as integers.
- Apply this evidence gate before accepting the final JSON, so a contaminated exchange cannot be accepted simply because its final text is well formed. Retain the raw event stream and available final text unmodified even when rejecting it. Do not create accepted role/decision files for that exchange.
- Keep exact JSON parsing. A clean single-turn response containing JSON followed by prose must still be `response_format_failure`. Do not trim prose, extract a JSON prefix, repair fields or retry.
- Preserve successful-result, tool-activity, case identity, role identity, schema, full constitutional binding, digest and source-hash checks. No prompt, constitution, interpretation, case-fact or role-contract changes are needed.
- Keep Claude-specific metadata rules out of the Codex parser. Preserve its existing protections and exercise its fake-client tests. Do not invent an equivalent turn field for an unobserved client format.

Cover clean single-turn events (including multiple assistant blocks belonging to one message), synthetic/unsolicited user events, multiple turns without a user event, missing/malformed turn counts, trailing prose, and existing tool rejection. Update the fake Claude client to emit realistic `num_turns: 1`; this corrects incomplete test metadata rather than weakening acceptance.

Add a focused process-boundary fake-client regression: a contaminated first response is retained, the manifest identifies failure/stage, no role assessment is accepted, no reconciliation runs, and later roles/cases are not invoked. Verify failure preservation and fail-fast behaviour, not only a helper's return value.

Replay all three new streams through the repaired parser: each must be rejected for contamination. Replay all seven old streams for parsing compatibility: their JSON remains parseable; the old reconciliation's separate binding failure remains historical and is not retrospectively fixed. Use temporary output paths and verify historical files are unchanged. Add a small evidence table with observed events, turn counts and old/new parser dispositions; do not duplicate all raw transcripts.

## Freeze and verify a new revision

Changing `subscription_trial.py` changes a frozen source. Preserve both existing packs byte-for-byte. Use `crucible/benchmark/subscription-core12-v0.1.2.json` for the new pack and update the default path and current documentation consistently. If that name already exists, inspect it and stop on a conflicting concurrent revision instead of overwriting it.

Commit the repaired source/tests first, then use the repository's existing `freeze --output` command against that exact committed source baseline. Commit the generated pack separately. The new pack's baseline is the source commit, not the later pack/document commit. Do not edit hashes or digests by hand. Do not regenerate the pack separately for different providers.

The committed-pack test can legitimately fail between a frozen source change and generation of its matching pack. Record that intermediate state honestly; do not skip or weaken the test. The complete final checkout must pass it and the full suite.

Verify all source hashes, the new pack digest, and all twelve action/Repair reconciliation schemas. Compare old/new case facts, selected actions, repair packets, constitution and interpretation content; these must remain unchanged apart from expected source-ref metadata. Existing evidence directories, manifests, indexes and old packs remain immutable. Record the new source SHA and digest rather than leaving placeholders.

## Review, publication and durable handoff

Perform a narrow adversarial review of the new gate and tests. If independent agent review is available, use it on the actual patch; reviewers must make zero live evaluator calls. Resolve concrete findings, then stop optional testing once the relevant risk is covered.

Write `docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md` (use the next numbered report if that exact file already exists). Include initial/repaired source commits, prompt blob/commit, root cause, red/green results, offline replay table, acceptance ordering, retained evidence, new pack SHA/digest, exact changed paths and limitations. Distinguish this detector repair from an explanation or fix of the underlying classifier behaviour. Completed live cases remain zero.

Update the current handoff and subscription guide so old restart prompts are clearly historical. Record that the next candidate is a separately scoped Codex CORE-01 run on the new pack, with a verified locally available model; do not choose an invented model identifier or launch it in this task. Claude remains paused pending supported investigation of its observed intervention. Do not prepare automatic retries or version/mode experiments.

Commit and push the complete green repair, new pack, report and handoff to `experiment/core12-live-v0.1` by ordinary permitted Git operations, preserving concurrent work. Do not push intermediate red states to the integration branch. Check both Windows and Ubuntu CI at the published code/pack commit. Verify the remote head and read back the report, prompt and pack/source blobs. Add a documentation-only publication receipt if needed; identify which exact commit CI tested. Do not claim publication or checks that are blocked.

Finish with a short result: verdict, tests, offline replay results, zero live evaluator calls, new source baseline/pack digest, report path, verified pushed commit and next action. Do not launch further experiments.
