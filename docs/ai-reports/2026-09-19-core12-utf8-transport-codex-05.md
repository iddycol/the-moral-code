# Core-12 offline UTF-8 transport repair — Codex prompt 05

The runner now saves and sends the same explicit UTF-8 prompt bytes. The complete local Windows suite passes **66 tests, zero skipped**, with native `cp1252` encoding and Python UTF-8 mode disabled. The new v0.1.3 pack verifies against the committed repair. This assignment made **zero real evaluator/client CLI calls**, including preflight, help and smoke calls. Completed live cases and comparable pairs remain **zero**. Stop for review; both providers' trials remain paused.

## Entry and provenance

Read the complete downloaded `C:\Users\Adrian\Downloads\MORAL_CODE_CODEX_UTF8_REPAIR_05.md` and the exact committed entry [prompt 05](../ai-prompts/MORAL_CODE_CODEX_UTF8_REPAIR_05.md). Both have Git blob `125ba7ed2cde706183265afb9396fe40da0d7c0c`, introduced by `000ccf4b85633d45afc68f20451aa79d9ad9727a`.

The existing checkout `C:\Work\MoralCode\the-moral-code` began clean at reviewed checkpoint `df091e0325bc76c4a8a4f5ebed3d6d700b567bdf`. Identity, branch, remotes, status and applicable instruction files were inspected. No applicable `AGENTS.md` or `CLAUDE.md` was found. A normal fetch and fast-forward incorporated the prompt/document commit `000ccf4b85633d45afc68f20451aa79d9ad9727a` on `experiment/core12-live-v0.1`, origin `https://github.com/iddycol/the-moral-code.git`. No reset, stash, force-push, configuration change or discarded work was used; `main` and Azure DevOps configuration were preserved.

The README, session handoff, subscription guide, [prompt 04 result](2026-09-19-core12-codex-core01-04.md), [transport review](2026-09-19-core12-utf8-transport-review-05.md), runner/preflight/parser/tests and preserved Codex failure/encoding receipt were inspected. Before edits, v0.1.2 verified its canonical digest `sha256:e3cf63f003952122689f9120899c13aee3c86e93eb14531d5611fa103c6ecfa0` and all 29 source hashes from baseline `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6`.

## Root cause and bounded repair

Previously `invoke` saved UTF-8 text but passed a Python string to `subprocess.run(..., text=True)` without specifying encoding. The native Windows default was `cp1252`; the saved bytes and bytes delivered to the client could therefore differ. Windows text newline translation also made the saved prompt CRLF. The original failed evaluator's stdin was **not captured**. Re-encoding its saved prompt reproduces byte `0x97` at offset 1320, consistent with its stderr; that remains a reconstruction, not an original byte trace.

The new regressions capture actual stdin in independent Python children before strict UTF-8 decoding. They reproduce the same offset with the unchanged production runner. Text outside cp1252 additionally raises a parent-side encoding error before delivery, exposing a separate lossy/locale-dependent failure path.

Production changes are confined to `subscription_trial.py`: construct one payload with `json.dumps(..., ensure_ascii=False, indent=2)`, append LF, encode explicitly as UTF-8, write it with `write_bytes`, and pass that same bytes object to subprocess stdin without text mode. Raw stdout and stderr use binary file handles. The default pack becomes v0.1.3. CLI flags, model selection, authentication routes, preflight, prompt prefix, envelope builders, strict UTF-8/final-JSON parsing, identity/binding checks and provider acceptance gates are unchanged.

**New prompt byte convention:** UTF-8 without BOM, LF line separators and one appended trailing LF. JSON preserves literal Unicode through `ensure_ascii=False`; embedded control characters retain JSON escaping. `prompt.txt` and subprocess stdin are byte-identical, and `invocation.json` records the SHA-256 of those same bytes. Historical prompt files retain their original CRLF bytes and valid original digests. Raw output bytes, including CRLF and invalid UTF-8 diagnostics, are retained without normalization.

## Windows red/green evidence

The existing repository virtual environment used CPython **3.12.10** on Windows **10.0.26200** (Windows 11), PowerShell **7.6.6**. Native locale/preferred encoding and subprocess text default were `cp1252`; `sys.flags.utf8_mode` was `0`. No global `PYTHONUTF8`, `PYTHONIOENCODING`, console code page or client setting was changed. The test command's `-X utf8=0` explicitly keeps UTF-8 mode disabled for that Python process.

| Checkpoint | Command using the repository `.venv` | Result |
| --- | --- | --- |
| Unchanged baseline | `python -m pytest -q engine/scales/reference_runner/tests` | 49 passed in 5.14s |
| Added strict-child regressions, unchanged production | `python -X utf8=0 -m pytest -q engine/scales/reference_runner/tests` | 15 failed, 51 passed in 3.97s |
| Repaired source before v0.1.3 generation | same command | 1 failed, 65 passed in 7.91s |
| Repaired source plus generated v0.1.3 | same command | 66 passed in 8.43s, zero skipped |

The red tests were committed locally as `46b40cc4a73fbbd7e90c355109d128438e8b7e7c` **before production edits**. All eight primary byte-transport cells failed; stricter existing process fixtures and timeout/nonzero process checks also exposed the defective input before their intended assertions. The intermediate single failure was the expected absent `subscription-core12-v0.1.3.json`, not a disabled hash check. Intermediate failing branch heads were never pushed.

The primary test matrix covers Codex and Claude paths, the real failed advocate envelope and a temporary wider-Unicode envelope, each with native encoding and a supplemental forced-`cp1252` subprocess default. Native Windows cells do not patch encoding. Supplemental cells patch only Python's default-encoding helper; every cell runs the real `invoke` and real `subprocess.run` against a real Python child. Each child captures `sys.stdin.buffer` before strict decoding, emits literal non-ASCII UTF-8 events and writes the Codex final-response file explicitly as UTF-8. Synthetic fixture content is `café — “curly” 中文 😀`; no benchmark packet is edited.

Captured historical-envelope bytes, identical across both provider paths and both native/supplemental Windows modes:

| Phase/artifact | Bytes | CRLF count | SHA-256 |
| --- | ---: | ---: | --- |
| Red: actual child stdin | 29,588 | 301 | `4f4112918138503b02426c4fe89dbbfea720dfb0f2ce7127f0fdecb3065cc454` |
| Red: saved prompt | 29,670 | 301 | `c7aaa0e198d3649e357d50433e138095499f0ccb7f3c3f8b7b6a5e3dbdfdd859` |
| Green: actual child stdin and saved prompt | 29,369 | 0 | `7e36778481f4fffa48b6d01c463c2a8d345e8fa604dcbc1f48d3d86061fd3cc6` |
| Green: wider-Unicode stdin and saved prompt | 29,431 | 0 | `b09c907420996a5a33748db5ea5085efc006548f34c29c23a3e46690beb872aa` |

Strict decoding of the red captured historical stdin fails at offset **1320**, byte **0x97**. In green cells, captured stdin equals saved prompt equals the bytes covered by the invocation digest, and the parsed echo preserves the entire envelope and Unicode string. Raw stdout equals a child-written sidecar byte-for-byte; stderr preserves Unicode, CRLF and deliberate invalid byte `0xff`.

The existing action and Repair tests still execute seven fresh fake processes for each provider. Their fake client was corrected to require UTF-8 stdin and emit UTF-8 bytes; acceptance rules were not weakened. Added timeout/nonzero tests retain partial binary evidence, assert the failure stage and later cases' `not_started` state, exactly one child invocation, no accepted role/decision/reconciliation and no retry. Invalid UTF-8 events/final-file tests preserve the offending bytes and reject decoding. Codex error/failed-turn checks still reject an otherwise valid final file. Existing tool, unsolicited-user, malformed/multiple-turn, strict JSON, schema, binding and identity checks remain green.

## Frozen source, pack and immutability

Repaired source commit: **`1fc927431541f5196d79d8284ea70cb1de1f9240`**, following the red-test commit. With that exact HEAD, the existing freeze command generated the previously absent filename:

```text
.venv\Scripts\python.exe engine/scales/reference_runner/subscription_trial.py freeze --output crucible/benchmark/subscription-core12-v0.1.3.json
```

The pack was committed separately as **`681327330c900e26146747668872cbb760bc69b1`**.

- Canonical pack digest: **`sha256:746a346b5b31314c7e49088b0f6ba058ad33f0a26be839e46860c9e970e63ced`**.
- Raw pack-file SHA-256: `83c6f44c5fbb2ebc0fb980b8ffd0d1cad5d425cc9932424fe22149f88d8c55e7`.
- Pack Git blob: `ae4747bb3779d06ec69b08979495bd54039691f0`.

The normal loader verifies all **29** source hashes. Each was also independently matched to `git show <source-baseline>:<path>` bytes. All **twelve** reconciliation envelope schemas pass Draft 2020-12 schema checks; each binding validates, and omitting or altering any binding field is rejected. Building envelopes leaves the pack unchanged. The local benchmark binding validator also passed: ten action bindings and two Repair-package bindings.

A recursive v0.1.2/v0.1.3 comparison permits and observes only `baseline_commit`, `pack_digest`, the `subscription_trial.py` source hash, and normal `ref`/`interpretation_rules_ref` changes in the pack binding and ten action-request bindings. All case facts, selected actions, Repair packets, schemas, constitution, interpretation and role contracts are otherwise identical. No hashes were hand-edited or verification bypassed.

Before edits an independent reviewer recorded byte lengths and SHA-256 for all **98 historical subscription-run files and three prior frozen packs**. All 101 remain byte-for-byte unchanged; the historical tree has no added or missing files. The snapshot's SHA-256 is `8a4f3852b10f9941391706fd276c6ca6597cbcfbd05eec19cb0d78691b0a9b67`. Historical CRLF evidence was not normalized. Local audit logs, snapshot and actual fake-child captures were retained outside the repository at `C:\Users\Adrian\AppData\Local\Temp\moral-code-utf8-audit-rdra_8zd`; the committed tests reproduce the transport checks, and the values above record the inspected red/green evidence.

## Review, scope and limits

An independent read-only reviewer inspected the actual source/test patch, all eight successful Windows process artifacts, native versus simulated encoding facts, captured bytes and preserved historical tree. **No blocking findings**. The reviewer also independently verified the final pack, source blobs, all 25 permitted comparison differences, report claims and current documentation, with no blocking findings. That reviewer made no evaluator calls. The repair has seven changed paths relative to the prompt-entry commit:

- `engine/scales/reference_runner/subscription_trial.py`
- `engine/scales/reference_runner/tests/test_subscription_trial.py`
- `crucible/benchmark/subscription-core12-v0.1.3.json`
- this report
- `README.md`
- `engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md`
- `governance/SESSION_HANDOFF.md`

The result proves the offline process-byte contract. It does not prove real client/server acceptance, inference, a completed moral evaluation, cross-provider comparability, repeatability or constitutional adoption. Historical attempts remain stopped. No next agent prompt, fresh CORE-01 attempt, retry, Claude classifier probe, client downgrade or settings change was created or executed.

## Publication verification

The complete green repair, pack, report and documentation were pushed normally to `experiment/core12-live-v0.1` as **`e5cb0e7f9382b4e1f381a69393dd80269353ff79`**, after fetching and verifying that the remote still pointed to the prompt-entry commit. No intermediate red integration head was published. The local commit history retains the red, repaired-source, pack and documentation checkpoints.

[Scales CI run 35396229116](https://github.com/iddycol/the-moral-code/actions/runs/35396229116) completed successfully at exactly that published commit:

- [Ubuntu job](https://github.com/iddycol/the-moral-code/actions/runs/35396229116/job/105765569877): **66 passed in 5.09s**, zero skipped.
- [Windows job](https://github.com/iddycol/the-moral-code/actions/runs/35396229116/job/105765570014): **66 passed in 12.01s**, zero skipped.
- [Benchmark binding CI run 35396229147](https://github.com/iddycol/the-moral-code/actions/runs/35396229147) also passed at the same commit.

The regression counts were read from the actual job logs. All seven changed files and the unchanged entry prompt were read back through GitHub's contents API at the published commit; decoded remote bytes and Git blob IDs matched the local committed bytes. The remote branch ref also matched `e5cb0e7f9382b4e1f381a69393dd80269353ff79`. Principal verified blobs at that commit:

| File | Git blob |
| --- | --- |
| Runner source | `2cfed7c7b7ebd57284f7b5c04c22be4ccce1544c` |
| Subscription tests | `40680466484ab30873d88f85d732fd3ba160b4f9` |
| v0.1.3 pack | `ae4747bb3779d06ec69b08979495bd54039691f0` |
| Report before this receipt | `12cc80616b145f8c62788334de2fd29f0b936058` |

This publication receipt changes only this report and the session handoff. The **CI-tested commit is `e5cb0e7f9382b4e1f381a69393dd80269353ff79`**, distinct from the later documentation-only receipt commit. Source, tests, pack and historical evidence are unchanged by the receipt. No operation remains blocked; stop for review with zero live evaluator calls in this assignment.
