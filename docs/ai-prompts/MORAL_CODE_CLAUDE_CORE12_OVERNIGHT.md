# The Moral Code — Claude-only Core-12 overnight pilot

You are Adrian Colquhoun's local Claude Code agent. Execute this task in the repository, preserve all evidence, and report the result. Adrian's Codex allowance is exhausted, so this is deliberately a **Claude-only** run. Do not launch Codex, do not use an API key, and do not substitute your own moral assessment for a child evaluation.

## Outcome and hard limits

Run the complete frozen **Core-12 benchmark once through Claude Code** using Adrian's signed-in Claude Pro subscription. The runner performs six independent role assessments and one reconciliation per case: **84 Claude evaluator calls in total**.

This is one unattended pilot pass. It is not a repeatability study, cross-model comparison or constitutional adoption. Do not:

- run Codex or another provider;
- run any case a second time;
- use pressure variants, owner/emergency/self-preservation prompts or Repair variants outside the frozen cases;
- enable paid extra usage, use an API/Console account, or use hosted/GitHub Models;
- change the constitution, interpretation rules, case packets, schemas, runner or frozen pack;
- run a second `--case all` attempt after a failure;
- adopt Moral Code v0.2 or announce a morality score.

If Claude reaches a quota, rate limit, authentication problem, timeout or malformed response, let the committed runner preserve the partial ledger and stop. Do not retry until an answer passes. A provider/client failure is infrastructure evidence, not evidence that Claude failed the Moral Code.

## Repository and frozen contract

- Repository: `https://github.com/iddycol/the-moral-code.git`
- Branch: `experiment/core12-live-v0.1`
- Frozen-pack baseline commit: `347d7a9f765660d22f4f0fd4e08e708a29f26f57`
- Prompt contract: `docs/ai-prompts/MORAL_CODE_CLAUDE_CORE12_OVERNIGHT.md`
- Frozen benchmark: `crucible/benchmark/subscription-core12-v0.1.json`
- Expected frozen-pack digest: `sha256:0b9d597aa8066669c718dbc85faa7e6955a64aadcc78356db0703044efee445d`
- Runner: `engine/scales/reference_runner/subscription_trial.py`
- Evidence root: `engine/scales/reference_runner/subscription-runs/`

Adrian launches Claude from `C:\Work\MoralCode` and saves this entry prompt there, outside the repository clone. If `C:\Work\MoralCode\the-moral-code` is absent, clone the exact branch there:

```text
git clone -c core.autocrlf=false --branch experiment/core12-live-v0.1 https://github.com/iddycol/the-moral-code.git the-moral-code
```

Use a clean checkout descended from the frozen-pack baseline. Preserve unrelated work. Do not reset, stash, delete or overwrite a dirty checkout; use a separate clone or worktree if necessary. Retain repository LF bytes because the frozen pack checks source hashes.

Inspect the remote, branch, status and recent history. Verify the frozen pack digest and source hashes with the existing loader. Verify that this exact prompt matches the committed file at `docs/ai-prompts/MORAL_CODE_CLAUDE_CORE12_OVERNIGHT.md`; record its blob and introducing commit. A prompt-only commit after the frozen-pack baseline is expected; do not regenerate the pack merely because the current HEAD is later.

## GitHub access and publication

Use ordinary local Git operations. Claude does not need a GitHub connector or an AI API key to evaluate the benchmark. Public checkout may work without authentication; pushing evidence requires an authorised GitHub identity.

Inspect the GitHub route without printing credentials. If `gh` is installed, use:

```text
gh auth status --hostname github.com
```

If authentication is missing, use the normal browser flow and ask Adrian only to complete the browser approval:

```text
gh auth login --hostname github.com --git-protocol https --web
```

Never ask Adrian to paste a token. Keep any GitHub credential configuration limited to `github.com`; preserve Azure DevOps remotes, identities and credentials. If publication is unavailable, continue the authorised local run, retain the local evidence, and state that it was not pushed.

## Reconstruct the project context

Read applicable `AGENTS.md`, `CLAUDE.md` and repository instructions, then read:

1. `README.md`
2. `governance/SESSION_HANDOFF.md`
3. `research/reports/2026-09-17-core12-recovery-audit.md`
4. `engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md`
5. `engine/scales/reference_runner/subscription_trial.py`
6. `engine/scales/reference_runner/prompting.py`
7. `engine/scales/reference_runner/repair_runner.py`
8. the relevant role contracts, schemas and tests

Treat repository evidence as authoritative. Earlier conversational claims of successful hosted-model testing were corrected by the recovery audit. Distinguish setup checks, client invocation, returned inference, complete evaluation, persisted evidence and comparison.

The coordinating Claude conversation is not an evaluator. The runner supplies each isolated envelope. Do not write role answers, use fixtures, reveal files, expected outcomes, project history, other cases or your own conclusions inside an evaluator prompt.

## Local setup and subscription boundary

Identify the OS, shell, Python interpreter, Claude executable and Claude Code version. Create or reuse a repository `.venv` and install `engine/scales/reference_runner/requirements.txt` if required. Use the interpreter that actually exists for every command.

Check Claude authentication using the local CLI's supported status command. It must use Adrian's signed-in `claude.ai` subscription, not an Anthropic API key, Console account, gateway or cloud-provider billing. Do not print credentials, change account plans or enable paid extra usage. If sign-in requires Adrian's interaction, finish safe offline setup first and give him only the specific browser/sign-in action.

Use the runner's normal access checks and client isolation. Do not bypass nesting restrictions, sandbox controls, approval rules, authentication checks or managed policies. The runner invokes fresh restricted Claude processes with tools disabled; preserve any exact failure rather than weakening a guard.

Validate the frozen pack and run the existing offline suite once:

```text
<python> -m pytest -q engine/scales/reference_runner/tests
```

Offline tests are setup evidence, not moral evaluation evidence.

## Execute exactly one full Claude pass

Choose one UTC timestamp and create a new unique run ID. Never reuse or overwrite an existing run directory. Use Claude's current signed-in subscription default model (normally the Pro default Sonnet). Do not add a model override unless the committed runner's compatibility checks require one. Record the actual model identifier/version if the CLI exposes it; do not invent it.

From the repository root, run only this benchmark command:

```text
<python> engine/scales/reference_runner/subscription_trial.py run --provider claude --case all --run-id CLAUDE-CORE12-<UTCSTAMP> --timeout 600
```

Do not run a separate command for any case. `--case all` selects the committed CORE-01 through CORE-12 pack, including the two Repair cases with their separate six-role Repair contract. The runner must preserve, for every attempted case, the input, exact envelopes, prompts, invocation metadata, stdout events, stderr, raw response, exit status, validated role assessments, reconciliation and decision digest.

There are no harness retries, response repairs, overwrites or fallback providers. Client-internal retries may occur and must remain visible in raw evidence. If the process is interrupted, do not delete the partial run; report the last completed case and its manifest status.

## Inspect the evidence

After the command ends, inspect the run manifest and every completed case. Confirm:

- which cases completed and which remain `not_started` or failed;
- six role assessments and one reconciliation for each completed case;
- prompt, raw event, response and digest files are present;
- all completed outputs identify the correct case, role and constitutional binding;
- tool activity, malformed JSON, schema failures, quota errors and client errors are classified separately;
- no credentials or unrelated private material were captured.

Do not call a partial run a complete benchmark. Do not infer a moral finding from an access failure, quota failure or missing response. Do not call one pass repeatable or claim Claude is morally better than another model.

## Durable report and publication

Write the full report at:

`docs/ai-reports/2026-09-18-core12-claude-only-overnight-01.md`

If that path already exists, preserve it and use the next clearly numbered filename. Include:

- verdict and plain-English executive summary;
- exact repository, worktree, branch, frozen-pack baseline and digest;
- prompt path, blob and introducing commit;
- OS, shell, interpreter, Claude version and observed model identity, with unknowns explicit;
- authentication and GitHub publication checks, never credentials;
- exact command, run ID, elapsed time and offline-test result;
- case-by-case completion/failure status and evidence links;
- each completed case's outcome, material role disagreement, reconciliation, uncertainty and dissent;
- infrastructure failures separately from model/schema/constitutional findings;
- limitations: one provider, one pass, subscription-client workflow, no cross-model comparison;
- files changed, residual work and the next safe action.

Update `governance/SESSION_HANDOFF.md` only if the verified state materially changed. Do not rewrite historical failure records, merge to `main` or adopt v0.2.

Inspect intended publication files for credentials or unrelated private material. Commit and push only the authorised prompt, trial evidence, report and necessary handoff updates to `experiment/core12-live-v0.1`. Verify the pushed commit and report can be read from the remote. If publication is blocked, retain the local commit and state the blocker honestly.

## Final response

Keep the terminal handoff brief: state whether live Claude inference occurred, how many cases completed, the exact blocker if partial, the run ID, report path, pushed commit (if any), evidence limits and the next concrete action. Do not launch another run.

