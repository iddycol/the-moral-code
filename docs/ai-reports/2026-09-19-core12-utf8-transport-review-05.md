# Core-12 — UTF-8 transport failure review

**Verdict: TRANSPORT_DEFECT_REPRODUCED_OFFLINE / CODEX_REPAIR_ASSIGNED / LIVE_TRIALS_PAUSED.**

Reviewed GitHub repository `iddycol/the-moral-code`, branch `experiment/core12-live-v0.1`, at `df091e0325bc76c4a8a4f5ebed3d6d700b567bdf`. The remote branch matched that checkpoint. Read the complete [attempt-04 report](2026-09-19-core12-codex-core01-04.md), saved encoding inspection, source invocation/parser and fake-client tests. The current frozen pack remains v0.1.2; no runtime source or historical evidence was changed in this review.

## Findings

The production `invoke` writes `prompt.txt` with UTF-8, but calls `subprocess.run(input=prompt, text=True, ...)` without an encoding. The published Windows inspection records Python 3.12, UTF-8 mode disabled and cp1252 as the default subprocess text encoding. The actual Codex process returned an invalid-UTF-8 stdin diagnostic before producing an event stream or answer.

Independently decoding the saved prompt file as UTF-8, then encoding that text as cp1252, reproduces the first invalid UTF-8 byte **0x97 at offset 1320**, exactly as reported. Historical stdin bytes were not captured, so this is reconstruction, not a wire recording.

The review also exercised the unchanged real `invoke` in a temporary directory against a Python child which reads `sys.stdin.buffer` and decodes strict UTF-8. With Python's default subprocess text encoding forced to cp1252 for this offline test, the child raised `UnicodeDecodeError` and the runner recorded `client_or_provider_error`. The real subscription clients were not invoked. This proves the locale dependency through the process boundary without another model attempt.

The existing fake client reads `sys.stdin.read()` and emits mostly ASCII-escaped JSON. It does not independently check the real client's UTF-8 input contract. Matching locale assumptions can therefore let its process tests pass while the real client rejects the bytes. This is an owned harness defect and a missing regression, not a moral or model-performance finding.

[Scales CI run 35393609548](https://github.com/iddycol/the-moral-code/actions/runs/35393609548) is completed successfully on Windows and Ubuntu. Those pre-existing tests do not cover the exposed transport contract. This review did not repeat that unchanged full suite; it ran the targeted offline reproduction instead.

## Repair decision and handoff

Use [Codex UTF-8 repair prompt 05](../ai-prompts/MORAL_CODE_CODEX_UTF8_REPAIR_05.md) from Downloads. The repair must construct explicit UTF-8 prompt bytes, save and send identical bytes, retain raw outputs, and prove strict decoding across a real fake-child boundary under a non-UTF-8 Windows locale. Test punctuation from the real failure and characters outside cp1252. Exercise both provider paths and preserve every existing response-integrity check.

The assignment includes source-first freezing of a new v0.1.3 pack and verified Windows/Ubuntu CI/publication. It makes zero evaluator calls and does not alter machine-wide encodings, client flags or safeguards. Runtime implementation and new pack generation are pending; this change publishes only the diagnosis, exact prompt and current handoff.

All prior packs and failed ledgers remain immutable, including original CRLF evidence and recorded digests. Claude remains paused. There are zero completed live cases and no comparable pairs. The executing agent must report at `docs/ai-reports/2026-09-19-core12-utf8-transport-codex-05.md` and stop for review; it must not author or execute a further trial prompt.
