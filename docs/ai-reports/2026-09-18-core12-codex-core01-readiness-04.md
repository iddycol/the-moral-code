# Core-12 v0.1.2 — Codex CORE-01 readiness review

**Verdict: OFFLINE_REPAIR_VERIFIED / ONE_CASE_CODEX_HANDOFF_PREPARED / LIVE_EXECUTION_PENDING.**

Reviewed `iddycol/the-moral-code`, branch `experiment/core12-live-v0.1`, at published head `960b72275f9a4cd171b418a12ca7f1f4f48b970a`. Source baseline is `fe2311ab7d76ea6a0e88933f964429d3fd77a8f6`; the v0.1.2 canonical pack digest is `sha256:e3cf63f003952122689f9120899c13aee3c86e93eb14531d5611fa103c6ecfa0`.

## Verification

Read the complete [Codex repair report](2026-09-18-core12-client-integrity-codex-03.md), current handoff, trial guide, source diff and relevant tests. An independent read-only reviewer found no concrete blocker to one bounded Codex attempt. The Claude acceptance gate is provider-specific; Codex invocation and parser behaviour are unchanged.

- Reproduced the full suite locally at the published checkout: `python -m pytest -q engine/scales/reference_runner/tests` — **49 passed in 2.13 s**. These are offline tests only.
- Independently verified the pack digest and all 29 source hashes against both checkout files and source-baseline Git blobs. All twelve cases remain present. Differences from v0.1.1 are source/binding commit references, the runner hash and the resulting pack digest; case facts and constitutional content are unchanged.
- Historical run files and old packs have no diff across the repair.
- Queried [Scales CI run 35391448681](https://github.com/iddycol/the-moral-code/actions/runs/35391448681): Windows job `105750493397` and Ubuntu job `105750493604` both completed successfully. Its tested commit is `87d2d348113e64bdf140e2307ce84e186953738e`; the final repair receipt is documentation only.

## Selected experiment and model

Use [Codex prompt 04](../ai-prompts/MORAL_CODE_CODEX_CORE01_04.md) from Downloads. It permits one new CORE-01 attempt only, up to seven evaluator CLI invocations, then stops even on success. It requires preflight using the installed client's help, current sign-in and non-inference model availability evidence. There is no new pack generation, implementation change, smoke call, automatic retry or continuation through Core-12.

Selected requested model: **`gpt-6-astra`**, conditional on local availability. Official [OpenAI model documentation](https://learn.chatgpt.com/docs/models), inspected during this review, lists that CLI identifier and explains that availability varies with sign-in and client. This workspace's model catalog also lists it, but that is not evidence of Adrian's Windows account availability. The executing agent must verify that locally without an inference probe; otherwise it reports a preflight blocker rather than selecting a fallback.

The [CLI reference](https://learn.chatgpt.com/docs/cli/reference) confirms explicit model selection and that excluding user configuration retains the authentication location. The frozen runner supplies its own model argument and does not inherit a verified model/effort merely because the coordinating session uses it. No new CLI flags or reasoning settings are introduced.

## Evidence limits and retained pause

The Codex parser does not verify per-call model identity or require a particular count of completed-turn events. Its manifest intentionally leaves resolved identity unverified. Prompt 04 therefore requires raw-event inspection and separate reporting of requested model, local availability and observed identity. Missing telemetry remains unknown; it is not repaired or fabricated. Explicit observed anomalies qualify the result even if the parser accepted it.

Seven CLI invocations do not guarantee seven underlying requests, a fixed token charge or absence of unreported client behaviour. This remains a subscription-client workflow pilot. Claude's earlier intervention is not explained by this repair or by a successful Codex case; Claude remains paused. There are still zero completed live cases at handoff preparation, and no comparable pairs, repeatability finding or constitutional adoption.

This publication changes only the prompt and current documentation. Source, tests, packs and all prior evidence remain unchanged. No live evaluator was invoked by this review. The next result belongs in `docs/ai-reports/2026-09-19-core12-codex-core01-04.md` and must include the exact execution and publication evidence.
