# Scales local application — release feasibility 13

Date: 20 September 2026.
Verdict: feasible to build and distribute as an advisory tester preview; application and release validation are still required.
Status: proposed delivery scope, not an implemented application or approved public release.

## User need and proposed product

A person installs Scales, connects their own supported AI account, describes a consequential decision and receives a readable, challengeable review. The product bundles the Moral Code, interpretation rules, role contracts and review workflow. The user should not need to prepare JSON or operate the repository.

Recommend Windows first: a packaged local service with a browser interface. Codex CLI is the first connection to qualify because its existing subscription workflow completed all twelve historical cases. Provider/model choices must be explicitly supported and tested. An account or compatible endpoint alone does not prove sufficient context capacity, valid outputs or sound judgments. Claude remains unqualified pending its recorded client-integrity issue; other API and local-model adapters are later scope.

## Evidence and exact state

Repository: iddycol/the-moral-code.
Reviewed candidate documentation head: e8b7d8d399dbe21dbaca37480a6cfbf502535ae6 on experiment/core12-provenance-v0.1.4.
Preserved completed-run head: a3777300751bf7469e9956d5a2f006fae31122cf on experiment/core12-live-v0.1.

Read the canonical safe stop, Scales contract, runner documentation, request/response schemas, provider interface, command provider, subscription runner and licensing declaration. An independent read-only agent inspected application/adapter gaps. No tests, evaluator calls, credential operations, implementation, deployment or release publication occurred during this feasibility review. Existing local documentation changes were preserved.

The current candidate still has six blocked historical cases and 82 passing tests plus one actual historical-pack integrity failure. It has no runnable v0.1.4 benchmark. These constraints remain in force.

## What already works, and the missing connection

The generic action runner accepts a structured evaluation request and orchestrates six roles plus reconciliation, validation and saved records. The provider protocol separates model access from the evaluation procedure.

The proven Codex transport resides in subscription_trial.py and selects cases from a frozen Core-12 pack. It does not yet expose a service for a user's new interactive decision. Its UTF-8 transport, fixed command construction, temporary working directory, event checks and failure preservation are valuable reusable components.

Do not simply expose runner.py command-line arguments through HTTP. The generic JsonCommandProvider still uses shlex.split and locale-dependent text=True process I/O. Its model labels are supplied metadata, not observed identity. The CLI also accepts paths, command strings and destructive overwrite behavior inappropriate for browser-controlled input.

The implementation should provide a narrow service for newly sealed requests, reuse the hardened transport where its contract fits, and validate the full constitutional binding. Keep requested model, observed model and client version distinct. Missing model telemetry remains unknown.

## Proposed first user journey

1. Install and launch the local application; it checks the supported Codex client and sign-in.
2. Enter the proposal, objective, evidence, affected people, alternatives and uncertainties. Preview and confirm the exact review input.
3. Start a bounded seven-call action review; see progress and cancel if needed.
4. Read the recommendation, principle assessments, evidence challenges, conditions, dissent and missing information.
5. Reopen the saved review or export a readable brief and an explicitly selected evidence bundle.

Execution orchestration and saved records reside on the user's device. Inference through a hosted provider transmits the selected evidence to that provider. There is no central Scales account or hosted service in this proposed first scope. Provider allowance or charges belong to the user's configured account. The application reports advice; executing an external business action is a separate future integration.

Repair functionality remains preserved in the research engine. A separate Repair user journey can follow; it must retain its component-specific outcomes rather than be flattened into the action review.

## Connection evidence

Official documentation was opened on 20 September 2026:

- [Codex non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode): scripted execution, machine-readable events, schema output and reuse of saved CLI authentication.
- [Authentication](https://learn.chatgpt.com/docs/auth): ChatGPT subscription sign-in and API-key access are distinct; API-key usage is billed through the Platform account. Account/workspace controls still apply.
- [App Server](https://learn.chatgpt.com/docs/app-server): a richer integration surface exists for product clients and authentication. The page marks the app-server command and WebSocket transport experimental/unsupported for production; this is not a reason to substitute it silently for the exercised CLI path.

These establish technical integration options, not a blanket assurance about every provider, account, deployment or commercial arrangement. Release documentation must identify the exact qualified connection and supported client versions. Retain provider-owned login; do not collect passwords, copy private session tokens, switch billing automatically or share one account among application users.

## Delivery and acceptance

| Step | Responsibility | Deliverable |
|---|---|---|
| Build the application | Implementation agent, coordinated here | New-request service, local UI, saved reviews, export, bounded jobs and supported Codex connection. |
| Review boundaries | Independent reviewer | Evidence that malformed output, Unicode, duplicate starts, authentication/quota failure, cancellation and input/path isolation behave correctly. |
| Package | Implementation agent | Versioned Windows download, bundled required runtime, startup/uninstall instructions and third-party notices; prerequisite detection for the supported provider client. |
| Test as a user | Adrian / independent tester | Clean-machine install, sign-in, one bounded live review, reopen/export and a useful readable brief. Live-call scope is set separately. |
| Release | Maintainer after acceptance | Clearly labelled advisory preview, supported configuration list, known limitations and release notes. |

Only the local service selects executables and storage locations. It binds to loopback, authenticates its browser session and rejects unrelated origins. It contains generated run paths, escapes model text and limits jobs. The review process has no authority to mutate business systems; detection of tool use after execution is not itself a preventive sandbox. These are concrete consequences of wrapping the existing subprocess code, not a request to build a general security platform.

No automatic retries until an acceptable moral answer appears. Preserve failed and partial reviews. Do not advertise independence of model families when roles use one model. No claim of moral certification or established decision-quality improvement.

## Relationship to benchmark correction and restart

The six blocked historical cases prevent a corrected Core-12 benchmark release. They need not prevent work on an independently versioned application that accepts new user-supplied decisions. Its packaging, execution and usefulness evidence must be recorded separately.

For implementation, create a separate feature branch from a verified runnable completed-run revision. Preserve historical frozen sources and records; prefer new application/service modules over rewriting the historical runner. If a required change touches frozen sources, specify and review the versioning arrangement before editing. Do not skip the retained integrity test or call the current research candidate green.

No implementation prompt or release has been launched by this document. The existing safe stop continues to govern research trials and constitutional changes. This report records the concrete product proposal so a future build task can start without reconstructing this conversation.
