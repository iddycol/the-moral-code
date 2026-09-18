# Core-12 v0.1.3 — fresh Codex CORE-01 readiness review

**Verdict: UTF8_REPAIR_REVIEW_PASS / FRESH_ONE_CASE_HANDOFF_PREPARED / LIVE_EXECUTION_PENDING.**

Reviewed `iddycol/the-moral-code`, branch `experiment/core12-live-v0.1`, at verified remote head `f8b4455f2ebae0e40e8b4762e307afb2dfb57de1`. Read the complete [UTF-8 repair report](2026-09-19-core12-utf8-transport-codex-05.md), production diff, strict child-process tests and current handoff. No concrete blocker to the bounded trial was found.

The code constructs explicit UTF-8 bytes once, writes them to `prompt.txt`, sends the same bytes without subprocess text mode, and captures raw stdout/stderr through binary file handles. The new tests capture actual child stdin before strict decoding and compare it against the saved prompt and digest, including non-ASCII output and characters outside cp1252. Existing provider-specific acceptance gates and CLI flags remain unchanged.

Verification during this review:

- `python -X utf8=0 -m pytest -q engine/scales/reference_runner/tests`: **66 passed in 4.91s**, no skips, on this Linux workspace. This supplements the recorded native Windows cp1252 evidence; it is not a claim to have run Windows locally.
- The normal loader verifies canonical digest `sha256:746a346b5b31314c7e49088b0f6ba058ad33f0a26be839e46860c9e970e63ced` for `crucible/benchmark/subscription-core12-v0.1.3.json`.
- All 29 source hashes also independently match Git blobs at source baseline `1fc927431541f5196d79d8284ea70cb1de1f9240`.
- Git comparison confirms the historical subscription-run tree and all three prior packs are unchanged from `df091e0325bc76c4a8a4f5ebed3d6d700b567bdf`.
- [Scales CI run 35396229116](https://github.com/iddycol/the-moral-code/actions/runs/35396229116) is completed successfully at code/pack commit `e5cb0e7f9382b4e1f381a69393dd80269353ff79`. The repair receipt records 66 passing tests on each Windows/Ubuntu job. The later head is documentation only.

The stop-for-review checkpoint in prompt 05 is now satisfied by this review. [Prompt 06](../ai-prompts/MORAL_CODE_CODEX_CORE01_06.md) is the newly scoped execution instruction: a fresh run ID, v0.1.3, explicit `gpt-6-astra` after current local non-inference availability checks, CORE-01 only, maximum seven evaluator CLI invocations. It stops for review even on success, with no smoke calls, fallback, automatic retry or further cases. It retains the prior distinction between requested model, locally advertised availability and per-call observed identity; missing telemetry remains unverified.

No real evaluator calls occurred during this review. The prepared prompt is not running. The prior failure is preserved, and the new trial must not resume or overwrite it. Claude remains paused. Green transport tests establish the byte contract, not actual client/server acceptance or moral correctness. Completed live cases and comparable pairs remain zero until fresh evidence establishes otherwise.

This publication changes only the exact prompt, readiness report and current entry documentation. Source, tests, packs and historical evidence are unchanged. Expected execution report: `docs/ai-reports/2026-09-19-core12-codex-core01-06.md`. The executing agent reports the result and stops; it does not create or launch a next prompt.
