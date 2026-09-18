# Moral Code — Claude Core-12 restart after the binding-contract repair

You are Adrian Colquhoun's local Claude Code agent. Continue the authorised Claude-only overnight experiment using the corrected committed contract. Finish the work below without handing Adrian routine checkout, testing or reporting steps. Codex's allowance is exhausted; do not invoke it.

This prompt supersedes `MORAL_CODE_CLAUDE_CORE12_OVERNIGHT.md` for new execution. Preserve that prompt and its failed run. The existing result is seven live responses, six accepted role assessments, zero completed cases. It remains a failed v0.1-pack run; do not edit, complete, replay or relabel it.

## Identity and working context

- Repository: `https://github.com/iddycol/the-moral-code.git`.
- Remote branch: `experiment/core12-live-v0.1`.
- Existing verified Windows checkout: `C:\Work\MoralCode\the-moral-code`.
- Suggested downloaded entry point: `C:\Work\MoralCode\MORAL_CODE_CLAUDE_CORE12_RESTART_02.md`.
- Committed prompt: `docs/ai-prompts/MORAL_CODE_CLAUDE_CORE12_RESTART_02.md`.
- Published failure checkpoint: `c12b53d9e2419c3e312219c363966101ac62af2e`.
- Corrected source baseline: `a415f6f3df6135e3247152effa1707bbb9fad5cd`.
- Required pack: `crucible/benchmark/subscription-core12-v0.1.1.json`.
- Required pack digest: `sha256:07306d70cf4fceb19eeda337d85066265f8c40dc71d75873c670734841432b7b`.
- Historical failed run: `engine/scales/reference_runner/subscription-runs/CLAUDE-CORE12-20260918T124845Z/`.
- Evaluator model: `claude-opus-5[1m]`, the model observed in the prior run. Pass it explicitly on every trial command; do not use an account default or a moving alias.

The previous sign-in reported **Max**, first-party claude.ai, no API key and overage disabled. These are observed prior facts, not a guarantee about the current session. Verify them without displaying credentials. Keep paid extra usage disabled. Use the existing credential route; preserve Azure DevOps settings. No new account, API key or billing change is authorised.

## Reconstruct and update safely

Inspect repository identity, branch, worktree status and recent history, and read applicable `AGENTS.md`/`CLAUDE.md`. Fetch the named branch and fast-forward a clean checkout. If there are unrelated changes or divergence, preserve them and use an isolated worktree at the verified remote commit. Do not reset, stash, force-push or overwrite unrelated work. If the checkout is absent, clone this branch below `C:\Work\MoralCode` with `-c core.autocrlf=false`.

Read:

1. `README.md` and `governance/SESSION_HANDOFF.md` (latest dated correction first).
2. `docs/ai-reports/2026-09-18-core12-claude-only-overnight-01.md`.
3. `docs/ai-reports/2026-09-18-core12-binding-contract-fix.md`.
4. `engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md`.
5. The runner, action prompt builder, reconciliation schemas and regression tests changed by the repair.

Verify ancestry from the corrected baseline, exact pack digest and the loader's frozen source hashes. Record the actual HEAD. Verify the downloaded prompt against the exact committed text and record its Git blob and introducing commit. Do not silently accept a substantively different entry prompt. Subsequent pack/document/test commits are expected; do not regenerate the pack to make its baseline equal HEAD.

The fix declares the interpretation-rules reference, supplies an explicit binding object and requires the entire four-field object in each subscription reconciliation's JSON Schema. The strict equality check is retained. Neither the constitution nor case facts changed. This is a new experiment pack and needs fresh responses.

## Offline gate and access

Reuse the working repository `.venv`, or create it and install the existing requirements. On this Windows checkout the interpreter is normally `.venv\Scripts\python.exe`; verify the actual path and use it consistently. Record OS, shell, interpreter and Claude version.

Run once before inference:

```text
<python> -m pytest -q engine/scales/reference_runner/tests
```

The repaired suite contains 23 tests, including the schema-following fake responder and a check that the committed pack matches source bytes. All tests must pass. The former three Windows failures are addressed by explicit Python invocation of the fake CLI and correct argument quoting. If any test still fails, retain the failure and stop before inference. Do not skip it, rewrite a valid test or alter the frozen implementation.

Use `claude auth status` and the runner's access checks to confirm subscription sign-in. Do not bypass permission decisions, nesting restrictions, managed policies or sandbox controls. The prior run proved these flags worked, so no extra live smoke call is needed. If authentication requires human interaction, preserve a restart checkpoint and give Adrian the precise sign-in action. If a permission classifier rejects an operation, record it; do not change routes to evade that rejection.

## Execution: CORE-01 first, then the remaining eleven

The budget is **one fresh attempt per case, at most 84 evaluator invocations**, plus the coordinating conversation. This is a call limit, not a token or subscription-usage guarantee. Stop the whole execution on the first failed trial, quota/rate-limit response, timeout, model switch, unavailable access or integrity failure. Do not wait for a quota reset and retry. Do not use paid extra usage, fallback providers, repeats or pressure variants.

Choose a single UTC timestamp and create unique run IDs. Save an execution index listing all twelve cases, expected run IDs and initial `not_started` states before inference. Update it after each attempted case, including a failure, so an interrupted coordinator leaves an exact restart point. This is bookkeeping outside the frozen implementation, not a new inference adapter.

First execute exactly:

```text
<python> engine/scales/reference_runner/subscription_trial.py run --provider claude --pack crucible/benchmark/subscription-core12-v0.1.1.json --model "claude-opus-5[1m]" --case CORE-01 --run-id CLAUDE-V011-CORE01-<UTCSTAMP> --timeout 600
```

Require exit 0, manifest `completed`, six persisted assessments and an accepted `decision.json`. Check the prompt's four-field schema requirement and explicit binding, all response digests, the unchanged equality check and the actual model identity in client events. Inspect for tool activity and supported uncertainty/dissent. This is an integrity gate, not a requirement that the moral outcome match the earlier response. Any valid outcome can pass.

If CORE-01 completes and its evidence passes that gate, continue automatically with CORE-02 through CORE-12 in order, once each, using the same command with the matching case ID and unique run ID. Retain the same pack, model argument and timeout. Do not use `--case all`: that would repeat the newly completed CORE-01. CORE-11 and CORE-12 use the runner's existing Repair roles. No separate smoke test or second CORE-01 run is permitted.

Each case uses six isolated child assessments followed by one reconciliation. The coordinating agent must not create evaluator answers, patch model JSON, fill omitted fields, reuse old role responses or provide historical hindsight. Let the runner construct every envelope and retain its unmodified raw outputs. A return code or manifest failure ends the sequence; record remaining cases as `not_started`.

Record requested and observed models separately. The `[1m]` suffix may appear in the init event while assistant messages report `claude-opus-5`. Record client-internal auxiliary model usage separately from the evaluator's identity; it was present in the first run. Do not silently treat another evaluator model as the pinned one.

## Evidence and reporting

Write `docs/ai-reports/2026-09-18-core12-claude-restart-02.md`, or the next numbered name if it exists. Link the execution index and every attempted manifest. Include repository/branch/HEAD, prompt blob/commit, source baseline, pack digest, OS/client/auth facts, actual model, commands, test outcome, elapsed time and observed usage where exposed. Count live calls and completed cases separately.

For each completed case, explain the proposed action or repair package, six role positions, accepted decision, significant dissent, uncertainty and the evidence for any concern. Distinguish unsupported reasoning from transport, schema, binding or quota errors. Report any suspected weakness as a finding or hypothesis at the responsible layer. One provider and one pass establish neither repeatability nor cross-model agreement; do not produce an aggregate morality score or adopt v0.2.

Preserve all raw evidence. Inspect publication files for credentials or unrelated private material before committing. Do not print credentials or include virtual environments. If sensitive material requires redaction, retain originals locally and document exact changes rather than silently modifying evidence. Record the same raw-client metadata limitations as the first report where still present.

Append the verified result and next action to `governance/SESSION_HANDOFF.md`. Commit and push only the new index, trial evidence, report and handoff to `experiment/core12-live-v0.1`, preserving concurrent work. Verify the remote head and read back the published report/evidence by a permitted route. If publication or readback is blocked, retain the local commit and state exactly what is unverified. Never claim a blocked operation succeeded.

Finish with a short handoff: completed case count, actual model, principal findings or blocker, report path, pushed commit if verified, and next action. Do not launch further experiments.
