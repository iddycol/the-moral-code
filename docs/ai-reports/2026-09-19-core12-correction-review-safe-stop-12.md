# Correction 11 independent review and safe stop

**Verdict: reviewed source-correction checkpoint with one low documentation finding; not a runnable release. Safe to pause.** The implemented fixes match the bounded correction scope, and unresolved case-admission issues remain explicit. No new pack, interpretation adoption, merger or live trial is approved by this review.

## Identity and scope

Repository: iddycol/the-moral-code. Candidate branch: experiment/core12-provenance-v0.1.4. Reviewed head: `ba7c771e28c3a843e00448eda84b3f0840398689`; source/test commit: `e9b8abe3a4d97f89237a7ff0c66284c62deec91b`; comparison baseline: `d79480aea10ff2990f86c27e0f12b752b5fa57db`.

Read the full correction report, admission ledger, changed binding profiles, new regression tests, workflow, packet/manifest changes and relevant correction evidence. Independent review split boundary/test inspection from semantic/admission inspection. This was a bounded review of the published correction, not a repeat audit of every external historical source. No evaluator calls or source fixes were made.

## Independently verified

- Full local offline suite at the reviewed candidate: **82 passed, 1 failed in 4.95 seconds; zero skipped**. The sole failure is the historical-pack integrity assertion against changed candidate binding profiles.
- [CI run 35426434229](https://github.com/iddycol/the-moral-code/actions/runs/35426434229) independently confirmed failed at exactly source commit `e9b8abe3a4d97f89237a7ff0c66284c62deec91b`. The implementing receipt records the same 82/1 result on Windows and Ubuntu. This review did not rerun Windows locally.
- All **948 pre-existing blobs** under the runner tree, historical subscription-pack paths and constitution are identical to the comparison baseline. This includes existing tests and saved run evidence; only the new candidate-boundary test file is added in that tree.
- All twelve candidate packet hashes match the correction claim index. Questions and requested outputs remain unchanged across all 24 masked/transparent packet variants; all ten action lists are also unchanged. The passing boundary tests retain selected-action equality with the historical pack.
- The original v0.1.3 canonical digest was recomputed successfully. All **29** original source hashes match the Git blobs at source `1fc927431541f5196d79d8284ea70cb1de1f9240`. No v0.1.4 pack is present.
- The workflow change adds the isolated candidate branch to an existing offline pytest workflow. It does not add a live-model invocation or weaken failure reporting.
- The boundary reviewer independently reproduced all 12 input digests and 84 envelope digests at the tested source identity. The admission reviewer checked all 245 change-ledger `after` values against current files; all match. Three `before` values require the documentation correction below.

## Review assessment

The four explicit identifying additions are removed from the binding-derived fields. CORE-10 no longer gives the evaluator the explicit future-disaster cue. The new checks operate on built request/envelope objects, which is the correct boundary for those escaped defects. They detect specified regressions; they are not proof that every famous case is unrecognizable.

Reconciliation envelopes in the offline boundary tests use empty role-assessment dictionaries. They verify supplied-input construction, not whether future model-generated answers introduce names, hindsight or unsupported facts. That is a coverage limit, not evidence of an implementation failure. No clean-blindness claim should be made from these tests.

The unchanged action adapter projects evidence, affected parties, alternatives and uncertainty; separate packet context/question/output fields and manifest cutoffs are not all sent through. Therefore this review does not claim every prose correction is evaluator-visible. Substantive evidence-array changes do reach the generated requests. The [boundary review note](../evidence/core12-review-12/boundary-review.md) records this limit.

Six qualified/six blocked admission states remain distinguishable. In particular, the unresolved combined-shock timing in CORE-07 and unresolved locking-policy premise in CORE-10 are not admitted merely because the text/schema validates. Repair descriptions distinguish the historical arrangement, uncertain operational feasibility and proposed stronger safeguards. The candidate does not adopt the interpretation proposal.

The retained integrity failure is expected from this source revision but is an actual failed test. It prevents a green-release interpretation and must remain visible. Resolving candidate admission and creating a properly bound new pack is future work; changing historical hashes, skipping the test or declaring it green would misrepresent the state.

## CR12-D01 — low: three baseline arrays are inaccurate in the change ledger

In `docs/evidence/core12-correction-11/sources-04-08.json`, inspect `changes` rows whose `field` is `sources` and whose path is one of:

- `crucible/historical/cases/HC-0101-nsw-child-removal-1915/manifest.json`: the recorded before-array already contains corrected assent qualifications and some corrected date/title metadata.
- `crucible/historical/cases/HC-0104-second-atomic-use-1945/manifest.json`: the recorded before-array already contains revised clock/receipt qualifications in two use notes.
- `crucible/historical/cases/HC-0107-montreal-protocol-1987/manifest.json`: the recorded before-array already contains the revised original-treaty URL and temporal use notes.

The authoritative before-values are the complete `sources` arrays at comparison baseline `d79480aea10ff2990f86c27e0f12b752b5fa57db`. All 245 after-values match the candidate and 242 before-values match the baseline. This affects exact audit reconstruction from that ledger alone, not the candidate packets or admission decision. Preserve this finding at the requested stop; correct those three arrays later as documentation, with no model run or source-suite rerun required solely for that correction. The [admission review note](../evidence/core12-review-12/admission-review.md) records exact subfields.

## Stop and restart

The canonical restart record is [SAFE_STOP_2026-09-19.md](../../governance/SAFE_STOP_2026-09-19.md). It records local paths, branches, source/pack identities, the six case blockers and the reading order. Prompt 11 is completed and historical. No new executable prompt is issued.

No merge, new pack, trial, Claude restart or constitutional adoption is scheduled. When Adrian resumes the project, begin with the remaining admission questions and any review notes; do not repeat the completed batch or infer approval to start another provider run.

Publication consists only of this review, the safe-stop record and current README/handoff routing. The safe stop is also linked from the completed-run branch so an older starting point leads to the candidate checkpoint. Source and evidence remain untouched by this publication. Remote heads and written files are read back after publication; the resulting receipt commit is reported in the chat handoff, avoiding a self-referential hash here.
