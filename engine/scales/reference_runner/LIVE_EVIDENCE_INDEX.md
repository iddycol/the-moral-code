# Scales v0.1 — Live Model Evidence Index

**Audited 17 September 2026. Status: no completed hosted-model ledger verified.**

This corrects the previous index, which described intended ledger paths as completed evidence. Read the [recovery audit](../../../research/reports/2026-09-17-core12-recovery-audit.md) and its [workflow evidence](../../../research/reports/evidence/2026-09-17-core12-recovery/workflow-audit.json).

## Verified evidence

| Item | Present evidence | Valid conclusion |
|---|---|---|
| Three `runs/P-*/` ledgers | File-backed authored fixtures | Offline controls execute |
| Challenger live, repeatability and pressure workflows | Workflow definitions and failed job records | Experiment machinery exists; live conclusions unavailable |
| Thalidomide live workflow | Failed provider request | No completed positive-control evaluation |
| Tuskegee shutdown workflow | Baseline provider failure; variant skipped | Shutdown-pressure resistance unmeasured |
| Core action batch | Input-generation failure, repaired in binding revision v0.1.1 | No historical live batch result |
| Core Repair batch | `core12-live-repair/CORE12-REPAIR-LIVE-PROOF-001.json` and error logs: 0/2 successful | Provider unavailable; green publication job is not an evaluation pass |
| Second-family Core-12 | Catalog HTTP 410 before model selection | No second-family decisions |
| `LIVE_FINDINGS_V0_1.md` | Generated report with zero completed live ledgers | No cross-model comparison can be made |

The named `runs-live/LIVE-GITHUB-MODELS-*` directories in the prior index are absent from the inspected branch. They were planned outputs, not verified completed ledgers.

## Provider status

[GitHub's documentation](https://docs.github.com/en/github-models) reports that GitHub Models was fully retired on 30 July 2026. The previous repository-Actions-token route cannot be assumed available. A supported inference provider must be configured before resuming live work.

Provider unavailability is an infrastructure result. It must not be described as a model's failure to follow the schema or constitution.

## Next evidence required

Generate the repaired Core-12 inputs at a committed revision, run two model families against equivalent sealed envelopes, preserve every success and failure, then compute comparisons from those ledgers. No constitutional adoption or certification claim follows from offline fixtures.
