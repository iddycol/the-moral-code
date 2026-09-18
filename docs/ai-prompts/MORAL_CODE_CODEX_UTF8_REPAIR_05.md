# Moral Code — offline UTF-8 transport repair

You are Adrian Colquhoun's local Codex engineering agent. Repair the proven runner-to-client encoding defect, demonstrate a meaningful failing regression before the fix, freeze the corrected source and publish the verified result. This is implementation and reporting only: **zero live evaluator invocations**, including smoke calls. Claude and further benchmark cases remain paused. Your coordinating session uses normal Codex allowance.

## Start from Downloads

Read this file in full from `C:\Users\Adrian\Downloads\MORAL_CODE_CODEX_UTF8_REPAIR_05.md`. Work in the existing checkout `C:\Work\MoralCode\the-moral-code`; Adrian need not move the prompt.

- Repository: `https://github.com/iddycol/the-moral-code.git`.
- Branch: `experiment/core12-live-v0.1`; preserve `main`.
- Reviewed failure checkpoint: `df091e0325bc76c4a8a4f5ebed3d6d700b567bdf`; subsequent prompt/document commits are expected.
- Current source baseline: `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6`.
- Current pack: `crucible/benchmark/subscription-core12-v0.1.2.json`.
- Current canonical digest: `sha256:e3cf63f003952122689f9120899c13aee3c86e93eb14531d5611fa103c6ecfa0`.
- Exact committed entry: `docs/ai-prompts/MORAL_CODE_CODEX_UTF8_REPAIR_05.md`.

Inspect identity, remotes, branch, Git status and applicable `AGENTS.md`/`CLAUDE.md`. Fetch and fast-forward a clean checkout or use an isolated worktree while preserving unrelated/concurrent changes. No reset, stash, force-push or discarded work; preserve Azure DevOps configuration. Verify this downloaded prompt against its committed blob and record its introducing commit.

Read README, the latest session handoff, subscription guide, `docs/ai-reports/2026-09-19-core12-codex-core01-04.md`, `docs/ai-reports/2026-09-19-core12-utf8-transport-review-05.md`, the actual invocation/preflight/parser code and tests. Inspect the raw run `engine/scales/reference_runner/subscription-runs/CODEX-V012-CORE01-20260918T204353Z/` and the corresponding `CODEX-V012-PREFLIGHT-20260918T204353Z/encoding-inspection.json`. Verify the current pack and all frozen source hashes before edits.

## Established defect and scope

The saved prompt is UTF-8, but `invoke` passes a Python string through `subprocess.run(..., text=True)` without explicit encoding. The observed Windows interpreter used cp1252. Re-encoding the saved prompt in cp1252 reproduces invalid UTF-8 byte `0x97` at offset 1320, matching Codex stderr. Original stdin bytes were not recorded; label this reconstruction accurately. An independent offline exercise of the unchanged real `invoke`, with its default text encoding forced to cp1252 and a strict UTF-8 Python child, reproduced failure without calling a model.

The fake client uses `sys.stdin.read()` and therefore does not independently enforce the actual client's UTF-8 contract. Existing successful fake processes do not prove the wire bytes are UTF-8. Fix this boundary, not case text or model instructions.

## Required implementation and regression

1. Establish the existing 49-test baseline using the repository environment and `python -m pytest -q engine/scales/reference_runner/tests`. Record Windows version, Python version and encoding/UTF-8-mode facts without exposing credentials.
2. Add focused process-boundary regressions and commit the red checkpoint locally before production edits. The primary regression must run the real `invoke` path against a fake executable which captures **raw stdin bytes** and decodes them with strict UTF-8, independently of its locale. Reproduce the old failure under a verified cp1252 default, including on Windows with Python UTF-8 mode disabled. A narrowly scoped simulation of Python's default subprocess encoding may supplement portable tests, but do not replace the actual Windows run with a mock of `subprocess.run`.
3. Use the real failed envelope as a transport fixture/reference without editing the historical run. Include em dash/curly punctuation to reproduce the observed failure. Separately cover text outside cp1252, such as accented text, CJK and an emoji, so replacement, ASCII sanitization or lossy conversion cannot pass. Temporary synthetic fixtures are not benchmark-case edits.
4. Make the smallest robust production repair: construct one explicit UTF-8 byte payload, save those bytes as the new `prompt.txt`, and send those same bytes to subprocess stdin without locale-dependent text conversion. Make LF/newline handling explicit so captured stdin bytes and the saved prompt digest agree on Windows and Ubuntu. Raw stdout/stderr must remain preserved; use binary capture/file handles where appropriate rather than decoding and re-encoding evidence. Keep final-response parsing strict UTF-8 and existing exact-JSON checks.
5. Exercise both provider paths through strict UTF-8 fake clients. They must emit non-ASCII UTF-8 response/event bytes and explicitly write the Codex final-response file in UTF-8. Assert byte-exact stdin versus saved prompt and its recorded digest, plus preserved Unicode in parsed output. Do not settle for assertions about keyword arguments or a decode/encode round trip that never crosses a child-process boundary.
6. Retain action and Repair process coverage, schema/binding/identity checks, Claude unsolicited-user/turn gates, Codex tool/error checks, timeouts/nonzero exits, failure preservation and no-retry behaviour. Do not weaken valid tests. Updating the fake client's locale assumptions to an explicit real-client UTF-8 contract is required; distinguish this from altering acceptance rules.

Do not change CLI flags, model selection, provider/authentication routes, safeguards, constitutional text, role contracts, case facts or JSON serialization to escape Unicode. Do not solve this by setting global `PYTHONUTF8`, `PYTHONIOENCODING`, changing the console code page, downgrading clients or reconfiguring Adrian's machine. The implementation must work under a non-UTF-8 locale. Do not normalize or rewrite historical CRLF evidence. Do not call either real evaluator CLI, even for a transport probe.

## Freeze and validate

Changing the runner requires a new frozen pack. Preserve v0.1, v0.1.1 and v0.1.2 byte-for-byte. Use `crucible/benchmark/subscription-core12-v0.1.3.json` and update the default path consistently. If that filename already exists, inspect concurrent work rather than overwriting it.

Commit repaired source/tests first, then generate the pack with the existing `freeze --output` command at that actual source commit, and commit the pack separately. Record the real source SHA and generated canonical digest. Never hand-edit hashes or disable source verification. An intermediate committed-pack test failure before the new pack exists is expected and must be documented; final verification must pass with no skipped tests.

Run the complete suite after generation, verify all source hashes and twelve reconciliation schemas, and compare all case facts, selected actions, Repair packets, constitution and interpretation against v0.1.2. Only intended transport-source hashes and normal baseline/ref/digest metadata may differ. Verify all prior packs and the complete historical evidence tree are unchanged. The new protocol's prompt-file byte convention must be documented; old prompt digests remain valid for their original bytes.

## Publish and stop

Review the actual patch against the regression contract. Write `docs/ai-reports/2026-09-19-core12-utf8-transport-codex-05.md` (next numbered name if occupied), including root cause, red/green commands/results, the strict child-byte evidence, Windows non-UTF-8 environment evidence, source baseline/new pack digest, exact scope, immutability checks and limitations. A green fake-client test proves the transport contract, not real inference or a completed moral evaluation. Completed live cases remain zero.

Update README, subscription guide and `governance/SESSION_HANDOFF.md` so prompt 04 and previous attempts remain historical. Commit and push the complete green repair/pack/report/docs to `experiment/core12-live-v0.1` without publishing intermediate red integration heads or overwriting concurrent work. Verify Windows and Ubuntu CI at the published code/pack commit and read back source/test/pack/report blobs and branch head. Record a documentation-only publication receipt when necessary; distinguish the tested commit from later receipt commits. Preserve a local checkpoint and state any blocked operation honestly.

Return a short verdict, test results, zero live evaluator calls, report path, new source SHA/pack digest and verified pushed commit. Stop for review here. Do not create or execute the next agent prompt, resume the failed run, launch a fresh CORE-01 or investigate Claude's classifier by changing client settings.
