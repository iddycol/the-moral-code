# Independent candidate admission review

Reviewed `ba7c771e28c3a843e00448eda84b3f0840398689` against `d79480aea10ff2990f86c27e0f12b752b5fa57db` in `/workspace/scratch/5d40335d611a/the-moral-code-stop12`.

**Conclusion:** suitable to preserve as a reviewed, non-runnable correction candidate. The six qualified/six blocked split accurately reflects the documented admission criteria. No additional substantive case-admission defect found in this bounded review. One low-severity provenance-record defect remains below. No source edits or evaluator calls performed.

## Checks and findings

- Read prompt 11, report 11, admission ledger, all action/Repair masked-packet changes, changed manifests/reveals, and the four source-ledger summaries. This checks internal semantic consistency and traceability; it is not a fresh verification of every historical source.
- Independently compared all 20 action packets and four Repair packets with the starting revision. All decision/Repair questions, available action lists, requested outputs and Repair option IDs/types remain unchanged.
- Parsed admission.json: CORE-01/02/03/04/05/08 are qualified candidates; CORE-06/07/09/10/11/12 remain blocked. A qualified candidate is not a certified historical replay or admitted new pack.
- CORE-02 locally proposed delay has an explicit receipt qualification. CORE-03 records received neurological evidence while retaining the incomplete-dossier limit. CORE-04 narrows the ordinary court-route comparison and identifies the legislative decision. These do not silently claim every individual actor read every source.
- CORE-07 still has a question whose combined-shock premise is not established before the departure cutoff; CORE-10 still has a selected locking-policy premise not proved by the inspection. Both tensions are explicitly blocked in the packet/ledger/admission record rather than concealed by changed questions.
- CORE-11 preserves the funding disagreement, avoids treating public opposition as measured survivor prevalence and limits acknowledgement/refusal feasibility to those specific acts. Four previously known-feasible options become possible.
- CORE-12 now separates civil immunity consequences, compelled evidence and the design's recommendation/funding process from proposed additional safeguards. Five formerly known-feasible options become possible; no new runnable admission follows from statutory version pinning. The unsettled pre-adoption boundary is recorded correctly.
- Automated field resolution compared 245 change-ledger records to Git baseline and current JSON. Every `after` value matches the candidate; 242 `before` values match the starting revision. The other three are the documentation finding below.

## Low: three before-values contain already-corrected source metadata

File: `docs/evidence/core12-correction-11/sources-04-08.json`, `changes` entries with `field: "sources"` for:

1. `crucible/historical/cases/HC-0101-nsw-child-removal-1915/manifest.json`: before.sources[0].use_note already has the candidate's February-assent qualification; sources[2].citation/source_date and sources[3].citation already contain corrected overview/chapter metadata. The actual baseline uses the original statutory use note, a 1997 date, and the old chapter titles.
2. `crucible/historical/cases/HC-0104-second-atomic-use-1945/manifest.json`: before.sources[2].use_note and [3].use_note already contain the candidate's corrected clock/receipt qualifications. The actual baseline has the less-qualified senior-awareness/Soviet-entry wording.
3. `crucible/historical/cases/HC-0107-montreal-protocol-1987/manifest.json`: before.sources[0].url/use_note and [1].use_note already contain the candidate's original-treaty URL and temporal qualifications. The baseline URL is `https://ozone.unep.org/treaties/montreal-protocol` and has the earlier generic use notes.

Effect: the claim of exact before/after coverage is slightly overstated, and a reader of the ledger alone cannot recover these metadata edits accurately. The candidate files, Git history, all 245 recorded after-values and case admission statuses remain unaffected. Correct the three ledger before-arrays from the baseline Git blobs as a future documentation-only task; preserve the current finding at the requested safe stop. No test rerun, new pack or benchmark call is justified by this issue.

## Safe-stop recommendation

Record the candidate as reviewed with one low documentation finding and six pre-existing substantive admission blockers. Preserve the old benchmark evidence and pack separately. Do not merge, freeze a new pack, adopt interpretation proposal 10, resume Claude, run more cases or issue an executable next-agent prompt at this stop.
