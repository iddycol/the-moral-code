# Core-12 client-integrity repair — Codex 03

**Verdict: DETECTOR_REPAIRED_OFFLINE / PUBLISHED_AND_VERIFIED / WINDOWS_AND_UBUNTU_CI_PASSED / ZERO_LIVE_EVALUATOR_CALLS.**

Prepared on 19 September 2026 (Australia/Brisbane), under [Codex prompt 03](../ai-prompts/MORAL_CODE_CODEX_CLIENT_INTEGRITY_03.md). This repairs acceptance of unverifiable Claude client exchanges. It neither explains nor changes the underlying classifier intervention. Claude remains paused; completed live cases remain **zero**.

## Repository and prompt provenance

| Item | Verified value |
|---|---|
| Repository / branch | `https://github.com/iddycol/the-moral-code.git` / `experiment/core12-live-v0.1` |
| Checkout | `C:\Work\MoralCode\the-moral-code` |
| Initial local HEAD | `2c009026e9a12a847bdbdfdc570728729f256528` |
| Fetched starting HEAD | `51a1af0acbe4c8eb112c9f3a23115a08e4caaedb` (clean fast-forward) |
| Downloaded entry | `C:\Users\Adrian\Downloads\MORAL_CODE_CODEX_CLIENT_INTEGRITY_03.md` |
| Exact committed prompt blob | `2334fc058432eb2c3de542f92b2b95925794a4d7` |
| Prompt introducing commit | `51a1af0acbe4c8eb112c9f3a23115a08e4caaedb` |
| Local red regression commit | `7a40fedb520aa30368bf801b4af9cd9d99f38254` |
| Repaired source baseline | `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6` |
| Separate generated-pack commit | `bd01a48d9f66731863a0486c15654c0982d01838` |
| Environment | Windows 11, build 10.0.26200; PowerShell; CPython 3.12.10 |
| Interpreter | Existing `.venv\Scripts\python.exe` |

The downloaded file was read in full and its unfiltered Git blob hash matches the committed prompt exactly. Repository identity, remotes, status, branch, local configuration and current remote history were inspected. No applicable `AGENTS.md` or `CLAUDE.md` was found in the checkout or its parent directories. `core.autocrlf=false`; GitHub CLI access was already available. No authentication or Azure DevOps configuration was changed. No reset, stash, forced update or work discard was used. `main` was preserved.

Read the README, current handoff, client-integrity review, restart-02 report, binding repair report, subscription guide, runner/tests, related envelope builders and Windows/Ubuntu workflow. Independently inspected both historical manifests and all ten actual event streams. The existing v0.1.1 pack's canonical digest and all 29 source hashes verified before edits against both the checkout and source baseline `a415f6f3df6135e3247152effa1707bbb9fad5cd`.

## Root cause and acceptance order

The old `parse_cli_output` checked tool activity and successful results, then parsed the final JSON. It ignored unsolicited Claude `user` events and `result.num_turns`. Consequently a client-injected instruction and an extra reported turn did not disqualify otherwise valid JSON. Counting assistant event blocks would not fix this: the two assistant blocks in these streams share one message ID.

The small boundary repair now proceeds as follows:

1. Decode the event stream and require object events. The invocation has already retained `stdout.jsonl`, stderr, prompt, envelope, invocation and exit evidence.
2. For Claude, retain the available string from the unique result in `response.txt` before evidence rejection. Writing UTF-8 with newline translation disabled preserves the emitted final text exactly on Windows as well as Ubuntu.
3. Reject any Claude event with `type: user` as `protocol_contamination`, regardless of its text, synthetic flag or a misleading one-turn count. Keep existing tool/activity rejection.
4. Require the existing successful-result conditions. Require `type(num_turns) is int` and a positive value: missing, null, boolean, string, floating-point, collection and nonpositive counts are `client_output_error`, with the field and reported value (or `missing`) in the detail. Positive integers other than one are `protocol_contamination`.
5. Only then parse the entire final response as one JSON object. Clean single-turn JSON followed by prose remains `response_format_failure`; no prefix extraction, repair or retry is introduced.
6. Apply the unchanged output schema, case and role identity, exact full constitutional binding and role-reference checks before writing accepted assessment/decision files. Frozen-pack digest/source verification still occurs before invocation.

Claude-specific event and count rules remain inside the Claude branch. Codex receives no invented turn field; its error, response-file and tool/activity protections remain unchanged, and its action/Repair fake-client process tests pass. No prompt, invocation flags, constitution, interpretation, case facts, role contracts, authentication, client version, permission mode or safeguards were changed.

## Red and green regression evidence

Command throughout:

```text
.venv\Scripts\python.exe -m pytest -q engine/scales/reference_runner/tests
```

| Checkpoint | Result | Meaning |
|---|---|---|
| Unmodified starting checkout | **23 passed**, 3.74 s | Established reviewed baseline |
| Tests committed before production change, `7a40fed` | **24 failed, 25 passed**, 10.19 s | Expected acceptance/retention failures; no source-hash or pack failure |
| Repaired source before new pack generation | **1 failed, 48 passed**, 4.26 s | Only committed-pack test failed: default v0.1.2 file did not yet exist |
| Complete source and generated pack | **49 passed**, 3.96 s | Full local Windows suite, including committed-pack verification |
| Published commit `87d2d34`, Windows CI | **49 passed**, 3.37 s | Complete suite at the published code/pack revision |
| Published commit `87d2d34`, Ubuntu CI | **49 passed**, 2.90 s | Complete suite at the same revision |

The red checkpoint showed missing exceptions for well-formed contaminated answers and malformed turn counts, the wrong format-failure precedence on contaminated trailing prose, Windows newline changes, missing final text after tool rejection, and a fake contaminated run that incorrectly completed all 84 role/reconciliation stages. These were deliberately fake Python subprocesses, never subscription clients. The red state was kept local until a complete green repair was ready for publication.

Focused coverage includes clean one-turn streams with multiple blocks belonging to one message, synthetic and nonsynthetic unsolicited users, absent synthetic metadata, misleading one-turn metadata, multiple turns without a user event, missing/malformed/boolean/nonpositive counts, exact trailing-prose rejection, successful-result checks and tool rejection. The existing fake Claude client now reports realistic `num_turns: 1`.

The process-boundary regression supplies all twelve cases and returns valid role JSON after an unsolicited user event. It verifies the failed manifest and `advocate` stage, retained raw events/final text/exit, exactly one invocation, no accepted role assessment or decision, no reconciliation, and eleven later cases still `not_started`. Thus the detector is exercised through the real invocation and fail-fast manifest path, not only a parser helper.

An independent engineering agent reviewed the actual source/test patch and replayed the saved streams, making zero live evaluator calls. No blocking findings remained. Reviewed runner file SHA-256: `f8f8b38bd49c0951b389df037b08479f6f7b197c6e617d4c85a6400331ad0a58`.

## Offline replay evidence

Original run: [`CLAUDE-CORE12-20260918T124845Z`](../../engine/scales/reference_runner/subscription-runs/CLAUDE-CORE12-20260918T124845Z/). Restart 02: [`CLAUDE-V011-CORE01-20260918T195549Z`](../../engine/scales/reference_runner/subscription-runs/CLAUDE-V011-CORE01-20260918T195549Z/).

Each row was replayed with the old and repaired parser into temporary paths outside historical directories. `Parseable` means parser compatibility, not acceptance as a current-pack evaluation.

| Run / stage | Assistant blocks | User / synthetic events | Result turns | Old parser | Repaired parser |
|---|---:|---:|---:|---|---|
| Original / advocate | 2 | 0 / 0 | 1 | Parseable | Parseable |
| Original / guardian | 2 | 0 / 0 | 1 | Parseable | Parseable |
| Original / evidence_sceptic | 2 | 0 / 0 | 1 | Parseable | Parseable |
| Original / power_auditor | 2 | 0 / 0 | 1 | Parseable | Parseable |
| Original / vulnerable_person_defender | 2 | 0 / 0 | 1 | Parseable | Parseable |
| Original / future_environment_advocate | 2 | 0 / 0 | 1 | Parseable | Parseable |
| Original / reconciliation | 1 | 0 / 0 | 1 | Parseable | Parseable; historical binding failure unchanged |
| Restart / advocate | 2 | 1 / 1 | 2 | Parseable | `protocol_contamination` |
| Restart / guardian | 2 | 1 / 1 | 2 | Parseable | `protocol_contamination` |
| Restart / evidence_sceptic | 2 | 1 / 1 | 2 | `response_format_failure` | `protocol_contamination` |

Every stream reports `result/success`, `is_error: false` and an invocation requesting one turn. All contain init and rate-limit telemetry; all except original reconciliation also contain thinking-token telemetry. Paired assistant blocks share one message ID. The original power-auditor stream has two rate-limit events. These telemetry counts are not turn counts.

Restart sceptic final text contains a 20,001-character JSON object followed by 2,279 characters of prose/whitespace. That prefix was inspected for analysis only, never accepted or repaired. Under the new gate, its user event disqualifies the exchange before JSON acceptance, just as for the other two restart responses. All ten repaired-parser temporary final-text files match the emitted result strings byte-for-byte. The old-parser replays preserved text after newline normalization, but only two were byte-identical on Windows; the repair fixes that retention gap too.

The original reconciliation's missing `interpretation_rules_ref` remains its historical binding failure; parsing it does not fix the ledger. The two restart assessments historically admitted by the old runner remain in place, qualified as contaminated evidence. Neither manifest nor any accepted historical file was rewritten. Completed live cases remain zero.

## Frozen v0.1.2 revision and immutability

| Artifact | Verified value |
|---|---|
| New pack | `crucible/benchmark/subscription-core12-v0.1.2.json` |
| Exact source baseline | `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6` |
| Canonical pack digest | `sha256:e3cf63f003952122689f9120899c13aee3c86e93eb14531d5611fa103c6ecfa0` |
| Raw pack file SHA-256 | `4b21d5b456b0a43cc8f8ba8de82c944de0333f07044629231eed1a97dd4edcad` |
| Pack Git blob | `bc7b444ebed77a08424d59b9db79e4eb76cf33bd` |
| Source Git blob | `ae48642609ccff539b3030333f75f8b2e3ff0806` |
| Tests Git blob | `5f3931e575c2d883ead861539855be56c7330cea` |

After committing the repaired source, generated the absent v0.1.2 file once with the existing command:

```text
.venv\Scripts\python.exe engine/scales/reference_runner/subscription_trial.py freeze --output crucible/benchmark/subscription-core12-v0.1.2.json
```

The pack was committed separately. Its baseline is the source commit, not the pack or later documentation commit. No hash/digest was edited by hand and no provider-specific pack was generated.

All **29 source hashes** match both current files and the exact committed baseline blobs. All **twelve action/Repair reconciliation schemas** pass schema validation, accept the complete binding, and reject omission or alteration of every binding field. Full old/new pack comparison permits only baseline/constitution reference metadata, the single changed `subscription_trial.py` source hash and resulting digest. All case facts, selected actions, alternatives, Repair packets, constitutional/interpretation prose, role contracts and base schemas are unchanged.

The complete existing subscription-run tree, including manifests and indexes, plus both old packs comprises **87 files**; path-set and SHA-256 checks before/after replay confirm immutability. Historical pack raw hashes remain:

- v0.1: `d2d57727194cafc1616e5e52366ea509cf43db4bb2579c0c00f8e3c6766d1120`.
- v0.1.1: `ae1f60988615aec410a3cfb711cbe96f578e57d6a64a927473611e63451ecfa4`.

The original v0.1 pack's 29 source hashes match its documented inspection revision `c12b53d9e2419c3e312219c363966101ac62af2e`. Its recorded earlier baseline predates `subscription_trial.py`, so that baseline alone cannot reproduce every pinned source; this pre-existing historical limitation was observed and left unchanged. The v0.1.1 and new v0.1.2 baseline blobs verify completely.

## Changed paths and remaining limits

The complete repair/publication scope is seven paths:

1. `engine/scales/reference_runner/subscription_trial.py`
2. `engine/scales/reference_runner/tests/test_subscription_trial.py`
3. `crucible/benchmark/subscription-core12-v0.1.2.json`
4. `docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md`
5. `engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md`
6. `governance/SESSION_HANDOFF.md`
7. `README.md`

No live smoke calls, retries, extra usage, version/mode experiments or subscription-client invocations were made. The classifier's cause, withheld content and count of underlying model requests remain unknown. Observed client versions and parent auto mode do not establish causation. This detector uses available client evidence; it cannot prove absence of unreported internal behaviour. Offline fixtures and green CI are not live moral evaluations, comparison evidence or constitutional adoption.

The next candidate is a **separately scoped Codex CORE-01 trial on v0.1.2**, after verifying a locally available model and its identifier in that separate task. No model identifier was invented or selected here. Claude remains paused pending supported investigation of the observed intervention. Earlier restart/first-run prompts and commands are historical, not instructions to launch more work.

## Publication verification

Published the complete green repair, pack, report and handoff by ordinary Git push to `experiment/core12-live-v0.1` at **`87d2d348113e64bdf140e2307ce84e186953738e`**. The remote head was verified with `git ls-remote`. No intermediate failing branch head was pushed. The remote had remained at the fetched starting commit, so publication was a normal fast-forward preserving concurrent history.

Read back all seven changed paths plus the unchanged entry prompt through GitHub's contents API at that exact commit: **8/8 blobs and file bytes matched** the local committed objects. This included report blob `2ef3b98067a38ae69ceda503af82d5253ffc21d9`, prompt blob `2334fc058432eb2c3de542f92b2b95925794a4d7`, and the source/pack/test blobs recorded above.

[Scales Reference Runner run 35391448681](https://github.com/iddycol/the-moral-code/actions/runs/35391448681) completed successfully at **`87d2d348113e64bdf140e2307ce84e186953738e`**:

- [Windows job 105750493397](https://github.com/iddycol/the-moral-code/actions/runs/35391448681/job/105750493397): log confirms **49 passed in 3.37 s**.
- [Ubuntu job 105750493604](https://github.com/iddycol/the-moral-code/actions/runs/35391448681/job/105750493604): log confirms **49 passed in 2.90 s**.
- [Benchmark Binding Validation run 35391448518](https://github.com/iddycol/the-moral-code/actions/runs/35391448518), job `105750491114`, also passed at the same commit.

This publication receipt updates documentation only. The exact commit tested by CI is `87d2d348113e64bdf140e2307ce84e186953738e`; the receipt does not change its tested source, tests, frozen pack or prompt. No further experiments were launched. The next action remains the separately scoped Codex CORE-01 candidate described above.
