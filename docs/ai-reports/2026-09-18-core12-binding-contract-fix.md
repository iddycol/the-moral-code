# Core-12 reconciliation binding repair — 18 September 2026

**Verdict: CONTRACT_FIXED_OFFLINE / PUBLISHED_AND_VERIFIED / WINDOWS_AND_UBUNTU_CI_PASSED / FRESH_LIVE_VALIDATION_PENDING.**

## Evidence and cause

Reviewed published commit `c12b53d9e2419c3e312219c363966101ac62af2e` on `iddycol/the-moral-code`, branch `experiment/core12-live-v0.1`, including the [first live report](2026-09-18-core12-claude-only-overnight-01.md), manifest and preserved reconciliation envelope/response from `CLAUDE-CORE12-20260918T124845Z`. Work was isolated in `/workspace/scratch/5d40335d611a/the-moral-code-binding-fix`, local branch `fix/core12-constitution-binding`, based on that published commit.

Independent parsing of the preserved reconciliation confirmed zero errors against its original output schema, exact case/role-reference identity, and correct values for all three returned constitution fields. Only `interpretation_rules_ref` was missing. The schema did not declare that field; the action envelope did not expose a named `constitution_binding`. The checker required all four fields. Its broad copy instruction did not make the schema agree with that requirement.

This is a contract defect. The six accepted role responses and rejected reconciliation remain evidence of returned inference, but no completed decision was accepted. Agreement among their outcomes is not proof of moral correctness. The old run remains failed and has not been repaired retrospectively.

## Repair and compatibility

- The shared action reconciliation schema declares `interpretation_rules_ref` and has schema ID v0.1.1. Older three-field generic fixtures remain valid under its reusable base schema.
- The action prompt builder supplies `constitution_binding` and explicitly instructs copying every field.
- The subscription envelope specializes either action or Repair reconciliation schema with all four required fields and a JSON Schema `const` equal to the complete binding. Schema and runtime equality now express the same obligation. A deep copy avoids mutating the frozen schema.
- `check_response` retains its exact equality check; there is no comparison of only selected fields, relaxed acceptance, response repair or provider retry.
- Fake responders now emit only schema-declared fields, reproducing the real failure instead of relying on copying hidden extra fields.
- Test subprocesses use the active Python interpreter rather than a shebang executable. The separate command-provider test quotes arguments with `shlex.join`, preserving Windows paths and spaces through its existing parser. Production command-provider code is unchanged.
- Runner CI now targets Ubuntu and Windows, with LF checkout for byte-hashed packs. This addition is offline testing and does not invoke subscription clients.

No constitutional prose, interpretation rules, historical packets, role contracts or prior live outputs were changed.

## Regression evidence

The revised tests before the fix produced **3 failures and 19 passes**. The process-boundary test reproduced `Response changes the constitutional binding` when the fake response followed only declared schema fields. The new action/Repair checks exposed the undeclared or optional fourth field. Test checkpoint: `2fdd3f3`.

After the implementation repair, the same suite produced **22 passes** locally. New checks reject omission or alteration of each binding field, exercise action and Repair through fresh fake subprocesses, retain digest-tamper rejection and confirm envelope construction leaves the pack unchanged. A further committed-pack check guards the actual versioned artifact against source drift. The final suite produced **23 passes** on Linux with Python 3.12, jsonschema 4.26.0 and pytest 8.4.2.

The published repair also passed all **23 tests on Ubuntu and all 23 on Windows** in [Scales Reference Runner run 35387899485](https://github.com/iddycol/the-moral-code/actions/runs/35387899485), at release commit `0aac9b4ad49d938202ea1805be1163f18b27d9d3`. Job logs report 23 passed in 2.62s on Ubuntu and 23 passed in 3.62s on Windows. These are fake-client and contract tests, not live model evaluations. The restart prompt also requires a green local suite before inference.

## Frozen revision

- Source baseline: `a415f6f3df6135e3247152effa1707bbb9fad5cd`.
- New pack: `crucible/benchmark/subscription-core12-v0.1.1.json`.
- Digest: `sha256:07306d70cf4fceb19eeda337d85066265f8c40dc71d75873c670734841432b7b`.
- Historical pack preserved: `subscription-core12-v0.1.json`, digest `sha256:0b9d597aa8066669c718dbc85faa7e6955a64aadcc78356db0703044efee445d`.

The new pack was generated from a detached checkout of the source commit created through the connected GitHub app. Source code and tests match the locally approved repair byte-for-byte. The original unpublished pack named local source commit `97f73596f8dab71a4e3bc01df6c3b7163d076111`; its replacement names the actual GitHub source commit. Only baseline/ref metadata and the resulting pack digest changed during publication preparation. Its constitution and interpretation references identify that source commit; their content is unchanged. New results cannot be pooled with old-pack results as repeats. To inspect the original execution with its matching source hashes, use a separate checkout of `c12b53d9e2419c3e312219c363966101ac62af2e`. Do not disable hash checks to load it into the revised runner.

## Restart and remaining work

Use the exact [Claude restart prompt](../ai-prompts/MORAL_CODE_CLAUDE_CORE12_RESTART_02.md), replacing earlier execution prompts for a new run. The previous account was observed as Max, with Opus 5 and overage disabled. The new prompt explicitly pins `claude-opus-5[1m]`, verifies current access, starts CORE-01, then continues through the remaining eleven cases only after the first completes and its evidence is checked. That is at most 84 new evaluator invocations, without running CORE-01 twice. It stops at the first failed case and preserves progress.

Pinning a full model name and appending `[1m]` are supported by the [Claude Code model configuration documentation](https://code.claude.com/docs/en/model-config), inspected 18 September 2026. Actual client-reported identity remains the evidence; subscription defaults alone are insufficient.

The executing agent must write `docs/ai-reports/2026-09-18-core12-claude-restart-02.md`, preserve the raw ledgers and update the session handoff. No new live calls were made in this repair session. Repeatability, cross-family comparison and v0.2 adoption remain pending.

## Verification receipt

- Final local suite: `python -m pytest -q engine/scales/reference_runner/tests` — **23 passed**.
- Loaded the new committed-candidate pack with all digest/source-hash checks enabled; all twelve reconciliation envelope schemas passed schema validation.
- Compared all twelve old/new cases: facts, selected actions and repair packets are unchanged; action constitution refs now identify the new source baseline. Constitution and interpretation content digests are unchanged.
- Exactly three pinned source hashes changed: action reconciliation schema, action prompt builder and subscription runner.
- `git diff --check` passed. A scoped diff against `c12b53d9e2419c3e312219c363966101ac62af2e` confirmed the old frozen pack, complete subscription-run history, constitution and historical packets are untouched.
- Publication was rejected by automatic approval review. The initial normal Git push was blocked; checks then verified the exact public repository, configured push URL, unchanged remote head, fast-forward ancestry, twelve-file change scope, unchanged historical evidence/case facts and no obvious credential patterns. A second attempt used the exact reviewed commit `245f5f16483dee05a3cc69219c6aef3af95facda`, without force or tag publication. Approval review still rejected it because publication of the project files and environment/report metadata to that public destination was not explicitly authorised for this payload.
- Neither rejected push executed. No alternate write route was attempted while approval was outstanding. Adrian then explicitly approved publication with “yes, push it”. The newly approved normal Git push reached Git but failed because the shell had no GitHub credential helper. The connected GitHub app is the authorised publication route; source commit `a415f6f3df6135e3247152effa1707bbb9fad5cd` was created there and fetched into a clean detached checkout for pack generation.
- Published repair: `0aac9b4ad49d938202ea1805be1163f18b27d9d3` on `experiment/core12-live-v0.1`, with source baseline `a415f6f3df6135e3247152effa1707bbb9fad5cd`. Branch readback confirmed the release head. Each of the twelve changed paths was independently fetched at the release SHA and its Git blob SHA matched the prepared local file: **12 of 12 matched**.
- [Scales Reference Runner run 35387899485](https://github.com/iddycol/the-moral-code/actions/runs/35387899485): Ubuntu job `105739015286` and Windows job `105739015547` both completed successfully, each with 23 tests passed. [Benchmark Binding Validation run 35387899481](https://github.com/iddycol/the-moral-code/actions/runs/35387899481) also completed successfully at the release SHA.
- This publication receipt changes documentation only; the tested code, pack and downloadable restart prompt remain the exact blobs verified at the release commit. No live retry has run here. The next action is Claude execution of restart prompt 02.

## Exact publication scope

The published repair changes twelve paths:

1. `.github/workflows/scales-reference-runner.yml`
2. `README.md`
3. `crucible/benchmark/subscription-core12-v0.1.1.json`
4. `docs/ai-prompts/MORAL_CODE_CLAUDE_CORE12_RESTART_02.md`
5. `docs/ai-reports/2026-09-18-core12-binding-contract-fix.md`
6. `engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md`
7. `engine/scales/reference_runner/prompting.py`
8. `engine/scales/reference_runner/subscription_trial.py`
9. `engine/scales/reference_runner/tests/test_runner.py`
10. `engine/scales/reference_runner/tests/test_subscription_trial.py`
11. `engine/scales/schemas/reconciliation.schema.json`
12. `governance/SESSION_HANDOFF.md`

The destination is public. Reports include technical source/worktree identifiers and the previously disclosed subscription/model observations. No credentials, new live transcripts, user files or unrelated project data are included in the repair.
