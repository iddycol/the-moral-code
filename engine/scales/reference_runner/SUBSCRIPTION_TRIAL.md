# Run the first comparison with your existing subscriptions

**Current status, 18 September:** live trials are paused after restart 02. The [independent review](../../../docs/ai-reports/2026-09-18-core12-client-integrity-review.md) confirmed client-injected user instructions and two reported turns on all three calls, which the existing parser did not reject. [Codex prompt 03](../../../docs/ai-prompts/MORAL_CODE_CODEX_CLIENT_INTEGRITY_03.md) assigns an offline repair and new frozen pack with zero evaluator calls. The commands and earlier restart prompt below document the previous protocol; do not execute them as a new attempt until a new handoff is issued.

The immediate question is simple: **given the same Moral Code and case facts, where do Codex and Claude disagree, and why?** Start with CORE-01. Keep the answers, inspect the disagreement, and only then run the remaining cases. Constitutional adoption remains Adrian's decision.

This route uses locally installed Codex CLI and Claude Code, signed in with ChatGPT and Claude subscriptions. It does not use the retired GitHub Models service or require a new API purchase. This ChatGPT workspace cannot operate your separate Claude account. The commands below run on your own signed-in computer.

## First run

**18 September correction:** The first Claude pass returned six role assessments and a reconciliation, but completed zero cases because the action output contract omitted a binding field. The [failure report](../../../docs/ai-reports/2026-09-18-core12-claude-only-overnight-01.md) and original pack/ledger are retained. New runs use `subscription-core12-v0.1.1.json`: both reconciliation envelopes require the complete binding in their actual output schemas. The strict equality check remains. The [Claude restart prompt](../../../docs/ai-prompts/MORAL_CODE_CLAUDE_CORE12_RESTART_02.md) supersedes the earlier overnight prompt for new execution; it checks CORE-01 first, then attempts CORE-02 through CORE-12 once each, up to 84 new evaluator calls.

1. Open a terminal in a checkout of `iddycol/the-moral-code`, branch `experiment/core12-live-v0.1`, and pull its latest committed revision. Do not switch a checkout containing unrelated unfinished work.
2. Install the current [Codex CLI](https://learn.chatgpt.com/docs/cli/reference) and [Claude Code](https://code.claude.com/docs/en/overview) if needed. Sign in with `codex login` and `claude auth login`, choosing your ChatGPT / claude.ai accounts. Complete any first-launch setup interactively. Do not choose API-key or Console billing.
3. Set up the existing Python dependencies. These examples use macOS/Linux/WSL:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r engine/scales/reference_runner/requirements.txt
```

4. Run the first case once per family:

```sh
.venv/bin/python engine/scales/reference_runner/subscription_trial.py run --provider claude --run-id claude-core01-001
.venv/bin/python engine/scales/reference_runner/subscription_trial.py run --provider codex --run-id codex-core01-001
```

5. Generate the comparison:

```sh
.venv/bin/python engine/scales/reference_runner/subscription_trial.py compare engine/scales/reference_runner/subscription-runs/codex-core01-001 engine/scales/reference_runner/subscription-runs/claude-core01-001 --output engine/scales/reference_runner/subscription-runs/core01-comparison-001.json
```

Bring back `core01-comparison-001.json` and both trial directories, or commit those directories on the experiment branch after checking their contents. They contain the actual evidence; a summary alone is insufficient. The comparison includes all 12 rows, explicitly marking cases not selected or not completed.

Each case takes six role calls plus one reconciliation. Runs use the client's default model unless `--model MODEL_ID` is supplied. Record and verify the actual model/version from client metadata before treating runs as repeatability evidence. A subscription has usage limits, and account settings may permit paid extra usage: this script neither enables extra usage nor guarantees a zero bill under every account configuration. Keep extra usage off if you want to stay within the subscription allowance.

## What is held constant

`crucible/benchmark/subscription-core12-v0.1.1.json` freezes the v0.1.0 constitution, interpretation rules, v0.1.1 bindings, corrected schemas/envelope builders, role contracts and 12 inputs at source commit `a415f6f3df6135e3247152effa1707bbb9fad5cd`. Its digest is `sha256:07306d70cf4fceb19eeda337d85066265f8c40dc71d75873c670734841432b7b`. CORE-01 through CORE-10 evaluate the selected action; CORE-11/12 retain the separate Repair contract. The pack records source hashes and its own digest. Runtime verifies those hashes before calling a client. Do not edit the pack in place or regenerate it separately for each family.

The original `subscription-core12-v0.1.json` is historical evidence. Its pinned sources are available at commit `c12b53d9e2419c3e312219c363966101ac62af2e`; the new runner intentionally rejects those stale source hashes. Inspect an old run in a separate checkout of that revision. Do not bypass source verification or relabel an old result as a new-pack result.

The reusable action schema now declares `interpretation_rules_ref`, matching the request and Repair schemas. Its generic required list remains compatible with older three-field fixture decisions. For subscription reconciliations, the exact four-field binding becomes both a required-field set and a JSON Schema `const` in the envelope. The schema seen by the evaluator therefore expresses the same binding obligation as the unchanged strict equality check. An explicit `constitution_binding` object supplies the values to copy, without modifying the frozen schema object.

Each role receives only its own envelope, in a new process and temporary working directory. Only the seventh call sees the six accepted assessments, from that family and that case. Neither family sees the other's answers. Both receive the same prompt prefix and role envelopes. Reconciliation inputs necessarily differ when the families' assessments differ.

No reveal files, transparent packets, authored fixture answers or other runs are supplied. Some existing packet/binding details can identify historical cases, and models may already know their history: this is a closed-evidence instruction, not proof of anonymity or absence of memorised knowledge.

## What is recorded

Every invocation saves the envelope, exact prompt, command, stdout events, stderr, final answer when available, and exit status when available. Validated assessments and decisions are stored separately with hashes. The importer checks case IDs, role IDs, constitution binding and reconciliation references; it does not silently correct them. Schema acceptance is a structural check, not a finding that the reasoning is morally correct.

The trial manifest is created before the access check. A missing CLI or unverified subscription is `access_unavailable`; nonzero client exits are `client_or_provider_error`; timeouts, non-JSON answers, schema/binding failures and tool contamination have distinct labels. Inspect raw logs to distinguish quota, authentication, provider and client failures within the client/provider category. No inaccessible provider is called a morally failing model. Other cases remain explicitly `not_started` when a run stops.

There are no harness retries, response repairs, overwrites or fallback providers. Client-internal network retries may still occur and are visible only where the CLI reports them. An unsupported flag is a client failure, not a model finding. Retain failed directories; a deliberate new attempt needs a new run ID.

## Scope and limits

This compares **subscription client workflows**. Their system prompts, model defaults and managed policies can differ; it is not an identical bare-model API experiment. Neither provider's safety instructions are removed. Codex runs read-only, with web disabled and user config excluded; Claude runs in safe/restricted mode with tools disabled. Existing managed policies still apply. Detected tool activity disqualifies the response. Temporary directories and event inspection are not an operating-system guarantee that no external context could enter a client.

Claude Code 2.1.276 executed seven evaluator calls on Adrian's Windows computer using claude.ai Max, with model `claude-opus-5[1m]` and overage disabled. No complete evaluation resulted because of the recorded contract defect. The corrected contract still requires a fresh live run. This workspace has not invoked either subscription client. Offline process tests use a deliberately fake CLI and do not count as model evidence. If preflight cannot recognise the account's sign-in mode, it stops; do not weaken that check to force a run.

Once the one-case trial works and its raw evidence has been inspected, `--case all` selects all 12 (up to 84 calls per family), or `--case CORE-11` selects a Repair trial. One pass is a pilot: the existing benchmark requires at least three repeats per model version. Pressure tests and v0.2 adoption are later checkpoints. There is no aggregate morality score, and agreement between models is not proof of correctness.

These ledgers live under `subscription-runs/` and have their own checked comparison command. They are not automatically included in the older hosted-model `runs-live/` findings generator. Update the evidence index only after inspecting completed, persisted results.

## Interface references

The CLI invocations follow the official [Codex non-interactive interface](https://learn.chatgpt.com/docs/non-interactive-mode), [Codex command reference](https://learn.chatgpt.com/docs/cli/reference), [Claude programmatic interface](https://code.claude.com/docs/en/headless), [Claude command reference](https://code.claude.com/docs/en/cli-reference) and [Claude authentication instructions](https://code.claude.com/docs/en/authentication), inspected on 17 September 2026. Use ordinary saved subscription sign-in; never copy login tokens into this repository or GitHub Actions.
