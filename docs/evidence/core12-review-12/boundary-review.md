# Independent correction-candidate boundary review

Reviewed HEAD `ba7c771e28c3a843e00448eda84b3f0840398689` against audit/prompt baseline `d79480aea10ff2990f86c27e0f12b752b5fa57db` in `/workspace/scratch/5d40335d611a/the-moral-code-stop12`.

## Conclusion

No new actionable defect found in the narrowly reviewed binding changes, regression tests or workflow change. The demonstrated identity leaks and explicit factory outcome cue are corrected at the assembled request/envelope boundary. This conclusion does not admit the six blocked cases or certify historical facts independently.

## Checks performed

- Read the exact prompt 11, implementation report, admission ledger, verification receipt, binding diff, new boundary tests, unchanged converter/envelope builders, and workflow triggers.
- Independently ran `python -m pytest -q engine/scales/reference_runner/tests/test_core12_candidate_boundary.py`: **17 passed in 0.12s**.
- Independently rebuilt the twelve candidate inputs and all 84 envelopes in memory. Restoring the source-commit references to the documented tested commit `e9b8abe3a4d97f89237a7ff0c66284c62deec91b` reproduced **12/12 input digests and 84/84 envelope digests** in `verification.json`. No pack was written and no evaluator was invoked.
- Independently recomputed the unchanged v0.1.3 pack digest: valid. Independently read all 29 original source blobs at its baseline commit and verified every recorded source hash: **29/29 match**.
- Thirteen current source files intentionally differ from that pack: binding profiles plus twelve masked packets. Therefore the old loader's failure at the first changed file is expected; it is an actual failing test rather than an `xfail`, and is not evidence of corruption of the preserved historical pack.
- No v0.1.4 pack exists. The only `engine/scales/reference_runner` change is the new test file; no runtime or constitutional source changed.
- The workflow diff only enables existing offline pytest on the candidate branch. Other workflow push filters do not match this candidate branch, and no `workflow_run` chain was found. No automatic live-model trigger is added.

## Scope limits to retain in the review

1. The 84 constructed envelopes contain **empty reconciliation role assessments**. They prove static input-boundary behavior, not how future live model outputs might reintroduce names/hindsight. There is no current candidate live run to certify.
2. The new tests target the four known identifying bindings and the specific factory disaster cue. Passing them does not establish universal anonymity or full historical validity. The twelve-case assertions preserve selected actions/questions/outputs and exclude external provenance from evaluator inputs.
3. The existing action adapter projects evidence, parties, alternatives and uncertainty into the request; it does not pass the packet's separate `decision_context`, `decision_question` or `requested_output` fields. Precise dated cutoffs live in external manifests/audit material. This is inherited, unchanged behavior; do not describe the new tests as proving every prose context correction is shown to evaluators. The substantive evidence corrections themselves are in the projected evidence arrays.
4. The six explicit case-admission blockers remain a valid stop boundary. A full runnable-release claim would require separate admission work and a new pack; safe-stop publication does not.

No repository files were edited during this review. This scratch note is for the parent review's synthesis; the parent is performing the full-suite and publication verification.
