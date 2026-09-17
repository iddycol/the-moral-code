# Core-12 recovery audit — 17 September 2026

**Verdict: LIVE_COMPARISON_BLOCKED.** No completed Core-12 model decisions or paired model-family results were found in the inspected integration commit. The previous conversation handoff overstated hosted-model execution and persisted evidence.

## Scope and sources

- Integration branch: `experiment/core12-live-v0.1`, inspected at `6843dd48f4b9ffc33acbfe2cb0e155cfc41e0515`.
- Implementation branch: `implementation/scales-pilot-v0.1`, inspected at `ad20aed653fb4baaade3fb459666f6775a27505a`.
- All 216 workflow runs returned across three API pages were inventoried at the audit checkpoint. Fourteen names concerned GitHub Models or live experiment/report tooling.
- [Machine-readable audit](evidence/2026-09-17-core12-recovery/workflow-audit.json) preserves run IDs, source commits, job error excerpts and ledger inventories.
- [GitHub Models documentation](https://docs.github.com/en/github-models), retrieved 17 September 2026, says the service was fully retired on 30 July 2026, including its catalog and inference API. Existing job errors use the older `github_models_retirement_brownout` wording. This is not evidence that waiting for a temporary outage will restore the service.

No constitution, interpretation rule or historical evidence packet is amended by this recovery.

## What actually ran

| Evidence | Observed result | Classification |
|---|---|---|
| [Non-OpenAI Core-12](https://github.com/iddycol/the-moral-code/actions/runs/35167926506) | HTTP 410 at model catalog discovery; all case evaluation and publication steps skipped | Provider unavailable; no model selected |
| [OpenAI Core-12 action batch](https://github.com/iddycol/the-moral-code/actions/runs/35167876923) | Request generation stopped on CORE-04 action selector; inference steps skipped | Binding configuration defect |
| [Repair batch](https://github.com/iddycol/the-moral-code/actions/runs/35167829383) | Two provider HTTP 410 failures, zero successful evaluations; workflow green because it published its failure summary | Provider unavailable; publication succeeded |
| [Challenger live attempt](https://github.com/iddycol/the-moral-code/actions/runs/35166652775) | Provider HTTP 410 | Provider unavailable |
| [Challenger repeatability](https://github.com/iddycol/the-moral-code/actions/runs/35166797517) | Provider HTTP 410; comparison and publication skipped | Repeatability not measured |
| [Thalidomide live attempt](https://github.com/iddycol/the-moral-code/actions/runs/35166885298) | Provider HTTP 410; publication skipped | Provider unavailable |
| [Tuskegee shutdown experiment](https://github.com/iddycol/the-moral-code/actions/runs/35166935782) | Baseline failed with HTTP 410; shutdown variant and comparison skipped | Pressure resistance not measured |

The integration and implementation trees each contain three completed **file-backed fixture** manifests. Neither contains a `runs-live/` ledger. Fixture outcomes are authored controls, not hosted-model responses.

The original Repair JSON and error logs remain unchanged. Its two entries marked `REPAIR_MODEL_BOUNDARY_OR_SCHEMA_FAILURE` are reclassified by this audit as **provider unavailability**: no model response exists from which to infer a schema or moral failure.

A 2,088-byte Actions artifact was listed for the first Challenger attempt. Its download returned HTTP 403 in this session, so its contents were not inspected. The failure log and absence of committed completed ledgers are independently verified; this audit does not claim every possible uncommitted artifact was inspected.

## Case-by-case comparison status

| Core case | Question | OpenAI completed decision | Second-family completed decision |
|---|---|---|---|
| CORE-01 | Tuskegee untreated observation | None | None |
| CORE-02 | Challenger launch approval | None | None |
| CORE-03 | Thalidomide approval withheld pending evidence | None | None |
| CORE-04 | Administrative child-removal power | None | None |
| CORE-05 | Blood-based citizenship restrictions | None | None |
| CORE-06 | Sanctuary for persecuted refugees | None | None |
| CORE-07 | Second atomic use under standing authority | None | None |
| CORE-08 | Binding environmental controls | None | None |
| CORE-09 | Dialysis allocation by social-worth criteria | None | None |
| CORE-10 | Factory access controls obstructing escape | None | None |
| CORE-11 | Luxembourg reparations package | Provider error only | None |
| CORE-12 | South Africa transitional justice | Provider error only | None |

There are **zero comparable pairs**. No disagreement can yet be assigned to the Moral Code, a model family or a moral interpretation. Observed faults concern infrastructure, benchmark bindings, workflow evidence preservation and inaccurate reporting.

## Repairs made

Five binding selectors failed against the actual masked packets:

- CORE-04 and CORE-05 searched for text not present in any available action.
- CORE-07's substring `second` matched two alternatives.
- CORE-08 and CORE-10 copied wording that differed from their masked packets.

These now match the exact existing actions corresponding to the documented test questions. The historical facts, alternatives and intended questions are unchanged. The binding revision is identified separately as v0.1.1; future runs must use the repaired binding set and the same sealed inputs across providers.

Two regression checks were added: generate all ten schema-valid action requests and preserve the intended choices; prevent an input-only failed attempt from being reported as completed live evidence.

The generated live findings now count completed ledgers explicitly, state that no live behavior is demonstrated when the count is zero, and distinguish provider errors from invalid model responses. The live evidence index is corrected from asserted completed runs to observed evidence status.

The integration branch is included in binding validation and runner regression CI. Provider workflows remain historical definitions targeting the retired service; they have not been rerun against it in this recovery.

## Verification

Local verification with the repository's declared dependencies:

- 13 runner regression tests passed, including the two new recovery checks.
- All ten Core action requests generated and passed their JSON schema validation.
- All twelve binding profiles validated: ten action, two Repair.
- Historical validation passed for sixteen cases, thirty-two decision packets and sixteen reveal files.
- Benchmark validation passed for twelve core and seven extension cases.
- Rebuilt live findings reports zero completed hosted-model ledgers.

These checks establish offline generation and control behavior. They do not establish successful Repair model execution, live model compliance, historical truth or constitutional correctness.

## Remaining work

1. Obtain a supported, authorized inference route for two model families. GitHub repository permission alone is no longer a working model-access route.
2. Replace the transport adapters while retaining equivalent role, evidence, schema and constitutional envelopes.
3. Preserve provider/catalog/generation failures even when they occur before a run ledger exists. A green publication job must never be presented as an evaluation pass.
4. Record exact packet, binding, constitution, interpretation, role-contract, schema and provider configuration digests. Generated requests should be produced at the committed source revision.
5. Run the same repaired Core-12 inputs through both families, preserve every attempt, then measure repeats and pressure variants.
6. Only then prepare the evidence-based v0.2 constitutional decision. Adoption remains pending Adrian's decision.

The current session has not created new provider accounts, obtained API credentials, migrated to a paid endpoint, merged the draft branches into main, or adopted v0.2.
