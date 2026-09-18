# Moral Code — remaining eleven Codex cases, prompt 07

You are Adrian Colquhoun's local Codex coordinating agent. Execute and publish the remaining Core-12 cases using the unchanged v0.1.3 subscription runner. Complete checkout, preflight, execution, evidence review and publication autonomously within this scope. Do not implement repairs or write a next agent prompt.

## Entry and scope

Adrian launches you in Downloads. Read this file there: `C:\Users\Adrian\Downloads\MORAL_CODE_CODEX_REMAINING_CORE12_07.md`. Work in `C:\Work\MoralCode\the-moral-code` afterward. Repository: `https://github.com/iddycol/the-moral-code.git`; branch: `experiment/core12-live-v0.1`. Preserve Azure DevOps configuration and unrelated work.

The completed CORE-01 checkpoint is `9d692e20c09aff1fddd73f6f1776161ebcb3ba61`. Its review is `docs/ai-reports/2026-09-19-core12-codex-core01-review-07.md`. This prompt supersedes the previous stop-for-review instruction for the following work only:

- Run CORE-02 through CORE-12 serially, in order, at most once each.
- Maximum **77 new evaluator CLI invocations**, six roles plus reconciliation per case. Stop at the first execution or integrity failure. No retries, smoke calls, pressure variants, CORE-01 repetition or `--case all`.
- Claude remains paused. Do not invoke or reconfigure it.
- Use requested evaluator **gpt-6-astra** through the existing ChatGPT subscription route. No model substitution, API key, billing change, purchase, allowance-reset retry or permission bypass.
- This cap counts evaluator invocations, not tokens, client-internal requests or coordinating-session use. Usage is not guaranteed by the cap.
- Runner, schemas, evaluator prompts, tests, facts, constitution, interpretation and frozen packs remain unchanged. Preserve every historical evidence file byte-for-byte.

## Verify before inference

Inspect applicable AGENTS.md and repository instructions, identity, remote, branch and status. Fetch and fast-forward a clean checkout; preserve concurrent or unrelated changes using an isolated worktree if necessary. Do not reset, discard, stash or force-push. Stop on incompatible changes.

Read README, governance/SESSION_HANDOFF.md, engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md, the CORE-01 report `docs/ai-reports/2026-09-19-core12-codex-core01-06.md`, its review 07, and the frozen runner's relevant functions. Compare this downloaded file byte-for-byte against `docs/ai-prompts/MORAL_CODE_CODEX_REMAINING_CORE12_07.md`; record its blob and introducing commit. Do not pass reports, previous answers or historical hindsight to evaluator children.

Required source baseline: `1fc927431541f5196d79d8284ea70cb1de1f9240`.
Required pack: `crucible/benchmark/subscription-core12-v0.1.3.json`.
Required canonical digest: `sha256:746a346b5b31314c7e49088b0f6ba058ad33f0a26be839e46860c9e970e63ced`.

Verify source ancestry, the pack digest and all 29 frozen source hashes using the existing loader. Record actual HEAD. Do not regenerate a pack. Reuse the existing Python environment or install existing requirements in an isolated environment. Run the complete offline suite once before inference:

```text
<python> -X utf8=0 -m pytest -q engine/scales/reference_runner/tests
```

Require all 66 tests to pass without skips. Record interpreter, OS and shell. Do not repeat the suite per case.

Use non-inference checks only for `codex --version`, executable path, `codex login status`, frozen runner preflight, supported `codex exec` flags and locally advertised model availability. Do not expose credentials or override values. Require ChatGPT sign-in and availability of gpt-6-astra; missing evidence is a preflight blocker, not permission for a probe call. Keep all frozen invocation flags and reasoning settings unchanged. CORE-01 used codex-cli 0.155.0. Record the current version; if it differs, clearly separate that client revision in the report and do not claim identical-client comparability. Unsupported flags or changed invocation semantics require stopping before inference; do not downgrade or patch around them.

Distinguish requested model, advertised availability and observed per-call model. CORE-01 did not expose observed model or reasoning effort. Missing telemetry remains unknown and does not by itself invalidate completion. Never infer child settings from the coordinating session or a model's self-description.

## Run and inspect serially

Choose one fresh UTC batch timestamp. Create a new execution index beside subscription-runs, with unique planned run IDs `CODEX-V013-CORE02-<UTCSTAMP>` through `CODEX-V013-CORE12-<UTCSTAMP>`. Record pack/source/HEAD, prompt blob, environment, requested model and cap. Reference the existing completed CORE-01 run `CODEX-V013-CORE01-20260918T213604Z` separately: its seven historical calls do not count against this batch's 77. Do not edit its original index. Initialize the eleven new cases as not_started.

For each case, invoke the unchanged runner once, substituting the case and corresponding fresh run ID:

```text
<python> engine/scales/reference_runner/subscription_trial.py run --provider codex --pack crucible/benchmark/subscription-core12-v0.1.3.json --model gpt-6-astra --case CORE-02 --run-id CODEX-V013-CORE02-<UTCSTAMP> --timeout 600
```

CORE-11 and CORE-12 use the existing Repair path automatically. Do not adapt their answers into ordinary allow/block decisions. No parallel evaluator execution or extra agents are needed.

After each case, inspect persisted evidence before starting the next. Verify completed manifest, six accepted roles and decision, canonical digests, case/role identities, four-field binding and exact role references. Compare saved envelopes and UTF-8 prompt bytes against the frozen builder and invocation digests. Verify response.txt against the emitted final answer and accepted JSON. Inspect exits, stderr and raw events for errors, tools/activity, injected context, interventions, unexpected extra turns and coherent completion. Record actual invocation counts and available usage. Any explicit model mismatch or client intervention is an integrity finding even if the parser accepted the answer. Preserve runner status separately from review findings.

Any schema-permitted moral outcome is acceptable for this experiment; do not reject a case for disagreeing with CORE-01 or an expected historical judgment. On failure, timeout, quota/access block, interruption or integrity concern: preserve evidence, update the index, mark later cases not_started and stop inference. Never repair an answer, trim prose, fill fields, resume a partial run or retry. On success, continue automatically through CORE-12 within the cap; no per-case user confirmation is needed.

## Report, publish and stop

Write `docs/ai-reports/2026-09-19-core12-codex-remaining-07.md` (next numbered name if occupied). Include actual timestamps/timezone, HEAD/source/pack/prompt, OS/client/auth metadata, advertised/requested/observed model distinctions, commands, tests, invocation counts, elapsed time, usage and evidence links. Separate newly completed cases from the total including historical CORE-01. Derive counts and outcomes from saved ledgers; do not select only favorable results.

Provide a case-by-case account of selected action or Repair question, role agreement/disagreement, reconciliation, uncertainties and failure layer where applicable. Preserve Repair vocabulary. Distinguish packet limitations, constitutional interpretation questions, orchestration failures and client/model limitations; do not infer causes without evidence. No aggregate morality score, repeatability claim, cross-provider comparison or v0.2 adoption follows from one pass. An unavailable observed model remains a limitation on model-specific claims.

Review new files for credentials and unrelated private material. Do not publish secrets or silently edit raw evidence. If a transformation is necessary, retain the original locally and document it. Exclude environments and account files.

Append the result to governance/SESSION_HANDOFF.md and update the current README/guide status so this prompt becomes historical after execution. Preserve earlier reports and handoff history. Commit and push only new batch evidence, index, report and current documentation to experiment/core12-live-v0.1, without force and without merging main. Verify remote HEAD and read back new report/index/manifests and evidence blobs. Check applicable CI and distinguish the tested commit from later documentation receipts. If publication is blocked, preserve the local commit and report the precise limit; do not bypass rejection.

Finish with completed new/total case counts, new evaluator invocations, requested/observed model, principal findings or blocker, report path and verified pushed commit. Stop for review. Do not create another agent prompt, repeat any case, launch Claude or begin further experiments.
