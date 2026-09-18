# Core-12 restart 02 — independent client-integrity review

**Verdict: REPORT_CONFIRMED / PARSER_DETECTION_GAP_REPRODUCED / OFFLINE_REPAIR_ASSIGNED / LIVE_TRIALS_PAUSED.**

Reviewed repository `iddycol/the-moral-code`, branch `experiment/core12-live-v0.1`, at published checkpoint `2c009026e9a12a847bdbdfdc570728729f256528`. The remote branch matched that commit at review start. Local read-only source/evidence work used a detached worktree at that checkpoint. No live evaluator calls, client changes, source changes or historical evidence edits occurred during this review.

## Evidence and findings

Read the complete [restart report](2026-09-18-core12-claude-restart-02.md), current handoff, subscription guide, production parser/invocation/manifest path and tests. Inspected raw events from all three new calls and all seven original calls. A second independent read-only reviewer confirmed the event and parser findings.

| Evidence | Original attempt | Restart 02 |
|---|---|---|
| Run ID | `CLAUDE-CORE12-20260918T124845Z` | `CLAUDE-V011-CORE01-20260918T195549Z` |
| CLI invocations | 7 | 3 |
| Streams with unsolicited synthetic user events | 0 of 7 | 3 of 3 |
| Reported `result.num_turns` | 1 in every stream | 2 in every stream |
| Completed cases | 0 | 0 |

The new synthetic messages report that a response was withheld by a safety classifier. This proves the emitted conversation includes an intervention; it does not establish the classifier's implementation location, why it acted, what the withheld content contained or exactly how many underlying model requests occurred. Client version and coordinating-session auto mode remain hypotheses. Several assistant events can belong to one streamed message; counting those events as turns would be incorrect.

The current `parse_cli_output` examines tool activity but does not gate unsolicited user events or the reported turn count. Direct offline replay of the three saved streams into temporary response paths reproduced:

| Role | Current parser result |
|---|---|
| advocate | accepted |
| guardian | accepted |
| evidence_sceptic | `response_format_failure` |

The evidence-sceptic response has a schema-valid JSON prefix and 2,279 trailing characters. Independent schema validation of that prefix found zero errors, but no prefix was accepted or written into a historical ledger. Exact JSON rejection remains correct. The relation between the extra prose and the intervention is unknown.

The two accepted assessments are historical facts about what the old runner admitted. They are not clean single-turn benchmark evidence. Preserve their original files and manifest, and record this qualification separately. The repaired reconciliation binding was never reached live.

[Scales CI run 35389709389](https://github.com/iddycol/the-moral-code/actions/runs/35389709389) has now completed successfully on both Windows (job `105744940706`) and Ubuntu (job `105744941041`). This resolves the report's pending CI check, not the missing event-integrity coverage.

## Engineering disposition

1. Repair the acceptance boundary offline. Reject unsolicited Claude user events and multiple reported turns; fail closed when turn metadata cannot establish a single turn. Preserve raw events/final text and all existing JSON, schema, binding, identity and tool checks.
2. Add focused failing regressions first, including a process-boundary test proving no contaminated role is admitted and no later calls occur. Make the fake Claude result realistic with `num_turns: 1`.
3. Generate a new frozen v0.1.2 pack at the repaired source commit. Preserve both old packs and all failed ledgers. This is a protocol-integrity revision, not a constitutional revision.
4. Keep live Claude trials paused. Do not downgrade, change permission modes or alter nesting to get around the reported intervention. This review does not authorize another diagnostic inference call or claim to know the intervention's cause.
5. Codex credits are now available. Assign Codex the offline engineering repair through [prompt 03](../ai-prompts/MORAL_CODE_CODEX_CLIENT_INTEGRITY_03.md), launched from Downloads. Its evaluator-call budget is zero; the coordinating session still uses normal Codex allowance. After review of the corrected pack, an independent Codex CORE-01 trial can test that client workflow. It would not explain Claude's intervention or establish cross-provider agreement by itself.

## Scope and next handoff

This change publishes the review and exact downloadable Codex prompt, and updates current entry-point documentation. It changes no runtime source, tests, frozen packs, model instructions or evidence. The implementation, new pack and live validation are pending. Completed cases remain zero; repeatability, comparison and v0.2 adoption remain unestablished.

The Codex agent must publish its implementation report at `docs/ai-reports/2026-09-18-core12-client-integrity-codex-03.md`, include red/green test receipts and offline replays, verify both operating-system CI jobs, and return the actual new source baseline and pack digest. No further classifier experiment is embedded in that handoff.
