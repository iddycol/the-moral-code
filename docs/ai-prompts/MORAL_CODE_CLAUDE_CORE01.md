# The Moral Code — Claude-only CORE-01 subscription trial

You are Adrian Colquhoun's local Claude Code agent. Execute this task in the repository, preserve the evidence, and report the result. Adrian's Codex allowance is exhausted for this trial, so this is deliberately a **Claude-only** run. Do not attempt to launch Codex, do not substitute your own moral assessment, and do not expand the scope.

## Outcome

Run **CORE-01 once through Claude Code** using Adrian's existing Claude Pro subscription and the committed Scales subscription runner. The runner must obtain six independent role assessments and one reconciliation: seven Claude evaluator calls in total.

This produces one Claude-family evidence ledger. It is **not** a cross-model comparison and does not establish repeatability. Do not run CORE-02 through CORE-12, `--case all`, repeats, pressure tests, Repair cases, hosted APIs, GitHub Models, or constitutional adoption.

The coordinating Claude conversation is not an evaluator. Do not write role answers yourself, substitute fixtures, use expected outcomes, or feed project history or your own conclusions into an evaluator. The runner supplies each evaluation envelope.

## Repository and exact contract

- Repository: `https://github.com/iddycol/the-moral-code.git`
- Branch: `experiment/core12-live-v0.1`
- Known baseline: `3cc1c9678de7d6a97d39c05d8cb91ef686f67a53`
- Prompt contract: `docs/ai-prompts/MORAL_CODE_CLAUDE_CORE01.md`
- Frozen benchmark: `crucible/benchmark/subscription-core12-v0.1.json`
- Expected frozen-pack digest: `sha256:0b9d597aa8066669c718dbc85faa7e6955a64aadcc78356db0703044efee445d`
- Runner: `engine/scales/reference_runner/subscription_trial.py`
- Evidence root: `engine/scales/reference_runner/subscription-runs/`

Use a clean checkout descended from the known baseline. Preserve unrelated work. Do not reset, stash, delete or overwrite an existing dirty checkout; use a separate clone or worktree if necessary. Retain repository LF bytes because the frozen pack checks source hashes.

Inspect the remote, branch, status and recent history. Verify that this exact prompt matches the committed file at `docs/ai-prompts/MORAL_CODE_CLAUDE_CORE01.md`; record its blob and introducing commit in the report. If the checkout or prompt differs, stop before inference and report the discrepancy.

## GitHub access

This task uses ordinary local Git operations for checkout and publication. Claude does not need a GitHub connector or an AI API key to evaluate the case. The repository is public, so read access may work without authentication; publication requires an authorised GitHub identity.

Inspect the existing GitHub route without printing credentials. If `gh` is installed, use `gh auth status --hostname github.com` without `--show-token`. If authentication is missing, use the normal browser login flow:

```text
gh auth login --hostname github.com --git-protocol https --web
```

Ask Adrian only to complete the browser approval if that is required. Never ask him to paste a token. Keep GitHub credential configuration limited to `github.com`; preserve Azure DevOps remotes, identities and credentials. If publication remains unavailable, continue the authorised local run, retain the evidence, and state that it was not pushed.

## Reconstruct the project context

Read applicable `AGENTS.md`, `CLAUDE.md` and repository instructions, then read:

1. `README.md`
2. `governance/SESSION_HANDOFF.md`
3. `research/reports/2026-09-17-core12-recovery-audit.md`
4. `engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md`
5. `engine/scales/reference_runner/subscription_trial.py`
6. The prompt builders, schemas and tests used by that runner

The recovery audit corrected earlier conversational claims of live hosted-model testing. Treat repository evidence as authoritative. Distinguish setup checks, client invocation, returned inference, complete evaluation, persisted evidence and comparison.

Use the committed implementation. Do not redesign Scales, change the constitution or interpretation rules, regenerate the frozen pack, weaken a guard, or repair a model response until it passes.

## Local setup and account boundary

Identify the OS, shell, Python interpreter, Claude executable and Claude Code version. Create or reuse a repository `.venv` and install `engine/scales/reference_runner/requirements.txt` if required. Use the interpreter that actually exists for every command.

Check Claude authentication with the local CLI's supported status command. It must use Adrian's signed-in Claude subscription, not an Anthropic API key, Console account, gateway or cloud-provider billing. Do not print credentials, change account plans, enable paid extra usage, or use another provider. If Claude sign-in requires Adrian's interaction, finish safe offline setup first and give him only the specific sign-in action.

Use the runner's normal access checks and client isolation. Do not bypass authentication checks, nesting restrictions, sandbox controls, approval rules or managed policies. If a restriction prevents a child Claude evaluator from starting, preserve the exact failure; do not remove protection variables to force it through.

Validate the frozen pack and run the existing offline suite once:

```text
<python> -m pytest -q engine/scales/reference_runner/tests
```

Offline tests are setup evidence, not moral evaluation evidence.

## Execute exactly one Claude trial

Choose one UTC timestamp and create a new, unique run ID. Never reuse or overwrite a previous run directory. Use Claude's current signed-in subscription default model (normally the Pro default Sonnet); do not add a model override unless the runner's committed instructions require it. Record the actual model identifier/version if the CLI exposes it. Do not silently change models during the trial.

From the repository root, run only:

```text
<python> engine/scales/reference_runner/subscription_trial.py run --provider claude --case CORE-01 --run-id CLAUDE-CORE01-<UTCSTAMP>
```

The runner should preserve the manifest, access result, prompts, raw events, errors, six role assessments, reconciliation and decision digest. There are no harness retries, response repairs, overwrites or fallback providers. Client-internal retries may occur; retain their evidence. A quota, authentication or client failure is an infrastructure result, not evidence that Claude failed the Moral Code.

After the run, inspect the trial directory. Verify the six assessment files, reconciliation, raw responses and manifest. If the run stopped early, report precisely what was and was not measured. Do not fabricate missing files or infer a moral result from an access failure.

## Report and publication

Write the full report at:

`docs/ai-reports/2026-09-18-core01-claude-only-01.md`

If that path already exists, preserve it and use a clearly numbered subsequent filename. Include:

- verdict and plain-English executive summary;
- repository, worktree, branch, baseline, prompt path/blob/commit and frozen-pack digest;
- OS, shell, interpreter, Claude version and observed model identity, with unknowns explicit;
- authentication and GitHub publication checks, never credentials;
- exact command, run ID, test result, outcome or classified failure;
- evidence links to the manifest, raw responses, assessments, reconciliation and digest;
- the evaluated action and the six role findings;
- the reconciliation decision, uncertainty and dissent;
- limitations: one case, one provider, one pass, subscription-client workflow;
- files changed, residual work and the next safe action.

Update `governance/SESSION_HANDOFF.md` only if the verified state materially changed. Do not rewrite historical failure records or claim that a cross-model comparison occurred.

Inspect intended publication files for credentials or unrelated private material. Commit and push only the authorised prompt, trial evidence, report and necessary handoff updates to `experiment/core12-live-v0.1`. Verify the pushed commit and report can be read from the remote. If push is blocked, retain the local commit and state the blocker honestly.

## Final response

Keep the terminal handoff brief: state whether live Claude inference occurred, the exact outcome or blocker, the run ID, report path, pushed commit (if any), the evidence limits, and the next concrete action. Do not launch any further cases.

