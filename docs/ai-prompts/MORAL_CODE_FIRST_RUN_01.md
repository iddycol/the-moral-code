# The Moral Code — first subscription comparison

You are Adrian Colquhoun's local Codex agent. Execute this task, save the evidence in the repository, and report the result. Adrian has already authorised routine checkout, dependency setup, the subscription trial, and publication of its evidence on the experiment branch. Do not hand him another setup guide or stop after producing a plan.

## Outcome

Run CORE-01 once through Claude Code and once through Codex CLI using Adrian's existing signed-in subscriptions. Use the existing Scales runner to obtain six independent role assessments and one reconciliation per family. Compare the resulting decisions and explain the material disagreements in plain English. This stage is one case, up to fourteen model calls; do not launch the full Core-12 batch, repeats, or pressure tests.

Your coordinating conversation is not an evaluator. Do not write the role answers yourself, substitute fixtures, or feed this prompt, project history, expected outcomes, other conversations, or the other family's results into an evaluator. The runner supplies each evaluation envelope.

## Workspace and repository

- Suggested launch directory on Adrian's Windows computer: `C:\Work\MoralCode`. This is a chosen workspace location, not a claim that it already exists.
- Downloaded entry point: `MORAL_CODE_FIRST_RUN_01.md` in that directory.
- Repository: `https://github.com/iddycol/the-moral-code.git`.
- Working branch: `experiment/core12-live-v0.1`.
- Known implementation baseline: `9b487237ebb1e0d563900e3efd0f837bfb032350`.
- Exact durable prompt path: `docs/ai-prompts/MORAL_CODE_FIRST_RUN_01.md`.
- Frozen pack: `crucible/benchmark/subscription-core12-v0.1.json`.
- Expected pack digest: `sha256:0b9d597aa8066669c718dbc85faa7e6955a64aadcc78356db0703044efee445d`.

If the launch directory is already the correct repository, use it. Otherwise use its `the-moral-code` child directory; if absent, clone the named branch there. Keep the downloaded entry-point file outside the new clone. Do not search Adrian's whole computer for another checkout.

For a fresh Windows checkout, retain repository LF bytes because the frozen pack checks byte hashes. Use `git clone -c core.autocrlf=false --branch experiment/core12-live-v0.1 https://github.com/iddycol/the-moral-code.git the-moral-code`. This is a setting for this new checkout, not a global Git change. Do not rewrite files in an existing dirty checkout to satisfy a digest.

Inspect the remote, branch, status and recent history. Fetch current remote state and use a clean checkout descended from the known baseline. Preserve all unrelated changes. If necessary, create a separate worktree or clone instead of stashing, deleting, resetting or overwriting someone else's work. Use fast-forward updates only. Verify that the downloaded prompt matches the committed prompt exactly; record its Git blob and introducing commit in your report. If either the prompt or frozen baseline differs, explain the difference before running an experiment against a different contract.

## Reconstruct context

Read applicable `AGENTS.md`, `CLAUDE.md` and repository instructions, then:

1. `README.md`.
2. `governance/SESSION_HANDOFF.md`.
3. `research/reports/2026-09-17-core12-recovery-audit.md`.
4. `engine/scales/reference_runner/SUBSCRIPTION_TRIAL.md`.
5. `engine/scales/reference_runner/subscription_trial.py` and the relevant prompt builders, schemas and tests it uses.

The prior conversational claims of successful live testing were corrected by the recovery audit. At the known baseline, twenty offline tests passed; the workspace access checks recorded absent clients and no inference. Those are setup checks, not completed moral evaluations. Verify current repository evidence before making new status claims.

Use the existing implementation. Do not redesign Scales, change the constitution or interpretation rules, enlarge the benchmark, merge to `main`, or adopt v0.2.

## Establish local execution

Identify the actual OS, shell, Python interpreter, both client executables, and client versions. Use normal local permissions and the installed tools. Read official documentation only if local help and repository guidance leave a concrete compatibility question unanswered.

Create or reuse a repository `.venv` and install `engine/scales/reference_runner/requirements.txt` if required. On Windows its Python executable is normally `.venv\Scripts\python.exe`; on Linux/WSL/macOS it is normally `.venv/bin/python`. Choose the path that actually exists and use that interpreter for every command below. Do not ask Adrian to perform these routine steps.

Check `codex login status` and `claude auth status`. Establish that the clients use ChatGPT and claude.ai subscription sign-in, not API, Console, gateway or cloud-provider billing. Do not print or copy credentials, change account plans, enable paid extra usage, or use the retired GitHub Models route. If sign-in genuinely requires Adrian's interaction, finish the remaining offline setup and give him only that specific sign-in action.

Use the runner's normal access checks and client isolation. Do not bypass client nesting restrictions, authentication checks, approval rules, sandbox controls or managed policies. If a restriction prevents a child client from starting, retain its exact failure and identify the supported invocation needed; do not remove protection variables to force it through.

Validate the frozen pack using the existing loader. Run the existing runner test suite once with the selected interpreter:

```text
<python> -m pytest -q engine/scales/reference_runner/tests
```

Treat a missing dependency or a local checkout configuration problem as setup work. If a substantive runner defect, unsupported client flag, unexpected authentication format or protocol incompatibility is found, record the evidence and required correction. Do not silently edit the frozen runner, regenerate the pack, weaken a guard or repair model answers to obtain a successful result. This task authorises execution of the committed contract, not a changed experiment.

## Execute the two trials

Choose one UTC timestamp for this execution and form unique run IDs:

- `CLAUDE-CORE01-<UTCSTAMP>`
- `CODEX-CORE01-<UTCSTAMP>`

Do not reuse or overwrite any previous run directory. Record client defaults and any exposed actual model identifier/version; if the exact version is unavailable, state that rather than inventing it. Do not silently change models partway through a trial.

From the repository root run:

```text
<python> engine/scales/reference_runner/subscription_trial.py run --provider claude --case CORE-01 --run-id CLAUDE-CORE01-<UTCSTAMP>
<python> engine/scales/reference_runner/subscription_trial.py run --provider codex --case CORE-01 --run-id CODEX-CORE01-<UTCSTAMP>
```

Run these sequentially. A failure in one family's access or evaluation does not prevent the independently available family from being attempted. A shared pack or harness integrity failure does prevent both. Let the runner preserve prompts, raw events, errors, role assessments, decisions and manifests. Keep failed attempts as evidence. Do not retry a returned answer until it passes, fill missing fields, or use your own assessment in place of a failed role.

Once both trial directories exist, invoke the checked comparison, including when one or both trials failed:

```text
<python> engine/scales/reference_runner/subscription_trial.py compare engine/scales/reference_runner/subscription-runs/CODEX-CORE01-<UTCSTAMP> engine/scales/reference_runner/subscription-runs/CLAUDE-CORE01-<UTCSTAMP> --output engine/scales/reference_runner/subscription-runs/CORE01-COMPARISON-<UTCSTAMP>.json
```

If a trial could not create its directory, report that explicitly instead of fabricating a manifest. Infrastructure, client, quota or authentication failures do not establish a model's failure to follow the Moral Code. Structural schema acceptance does not establish that a decision is morally correct.

## Inspect and explain the evidence

For each completed family, verify the six assessment files, reconciliation, raw responses and manifest. Check the comparison's digests and confirm both sides used the same frozen pack. Explain:

- What action was evaluated and what each system decided.
- Whether they agreed on the outcome, enforcement recommendation, moral-floor findings, significant uncertainty and dissent.
- The important reasons for disagreement, with links to the underlying files.
- Any unsupported factual additions, invented references, missing perspectives or mismatch between a finding and its evidence.
- Whether the evidence suggests a weakness in a case packet, the Code, interpretation rules, orchestration or a client/model; distinguish a supported finding from a hypothesis.

If either side failed, explain where and why, and what remains unmeasured. Do not announce a winner, give an aggregate morality score, claim repeatability from one run, or describe the client workflows as identical bare-model API tests.

## Persist the result

Write a full report at `docs/ai-reports/2026-09-17-core01-subscription-first-run-01.md`. If that report already exists, preserve it and create a clearly numbered subsequent attempt instead. Include:

- Verdict and plain-English executive summary.
- Repository, worktree, branch, baseline, prompt path/blob/commit and pack digest.
- OS, shell, interpreter, client versions and observed model identities, with unknowns explicit.
- Commands, test results, run IDs, outcomes or classified failures, and relative evidence links.
- Case comparison and its practical limits.
- Files changed, residual work, exact next action and restart instructions.

Update `governance/SESSION_HANDOFF.md` to reflect verified progress. Keep the distinction between offline checks, client invocation, returned inference, complete evaluation, persisted evidence and completed comparison. Do not rewrite historical failure records or treat these subscription ledgers as automatically included in the older `runs-live/` report generator.

Inspect intended publication files for accidentally captured credentials or unrelated private material. Publish the trial evidence, comparison, report and handoff to the experiment branch. Do not commit virtual environments, CLI credentials or unrelated work. If sensitive data appears, preserve the original locally, document any necessary redaction and its effect on auditability, and publish only safe evidence.

Commit and push only the authorised files, preserving concurrent remote work. Verify the pushed commit and report can be read from the remote. If publication is blocked, retain the local commit and state the blocker; never claim the evidence is remotely saved when it is not.

## Final response to Adrian

Keep it brief: verdict, actual outcome of each family, main agreement or disagreement (or precise blocker), report path, pushed commit and the next concrete action. State whether live inference really occurred. Do not finish with another list of routine commands for Adrian to execute when you can execute them yourself.
