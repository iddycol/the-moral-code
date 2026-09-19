# Core-12 provenance audit and interpretation proposal

## Verdict

**The next correction belongs in the benchmark inputs. Keep the twelve principles unchanged.** The completed v0.1.3 run remains valid evidence of what the client workflow returned for its supplied inputs. This audit finds limitations in those inputs that prevent treating it as a clean masked historical replay. Prior byte/schema/stream checks did not establish historical or masking validity; this report supplements, rather than erases, those earlier checks.

An external claim-by-claim source ledger and [exact proposed interpretation wording](../proposals/CORE12_INTERPRETATION_PROPOSAL_10.md) are now available for review. Proposed wording remains outside adopted guidance. No model calls were made, no benchmark rerun was launched, and no frozen source, pack or historical output was changed.

## Provenance and deliverables

Repository: iddycol/the-moral-code; branch: experiment/core12-live-v0.1. Publication parent: `a57e2f76be27ee38e8c1851eeaa779c5582364d0`. Read-only source audits used the unchanged v0.1.3 material also present at evidence checkpoint `28a800a4f72e309d4c060882e8755a7066e97c6c`. Frozen source baseline and pack digest remain those recorded in [analysis 09](2026-09-19-core12-substantive-analysis-09.md).

- [Audit directory and coverage receipt](../evidence/core12-provenance-10/README.md): per-claim source locators, historical support, decision-time limits, epistemic labels, masking fidelity and recommended corrections.
- [Mechanical input audit](../evidence/core12-provenance-10/frozen-input-audit.json), reproducible using [check_frozen_inputs.py](../evidence/core12-provenance-10/check_frozen_inputs.py).
- [Interpretation proposal](../proposals/CORE12_INTERPRETATION_PROPOSAL_10.md): three exact additions, eight paired analytical scenarios, constitutional basis, objections and adoption limits. Scenarios are unexecuted examples, not new benchmark results.

Source support, access and temporal validity are separate. A source can support a historical statement without showing that the relevant actor knew it at the chosen cutoff. Some sources were inaccessible; replacement institutional records or primary documents were used where available, with limits retained. This is not a claim that every premise is verified or that all underlying original records were inspected.

## P10-F01 — Four full inputs disclose identities despite masked base packets

The frozen proposal fields contain the following explicit identities:

| Case | Field | Identity disclosed |
|---|---|---|
| CORE-04 | proposal.actor | NSW Aborigines Protection Board |
| CORE-06 | proposal.actor | Swedish government |
| CORE-07 | proposal.actor and proposal.purpose | United States; Japanese surrender |
| CORE-08 | proposal.actor | Montreal Protocol |

These values come from `crucible/benchmark/binding-profiles-v0.1.json`. `benchmark_adapter.build_action_request` copies profile actor and purpose into the evaluator request. Checking only that the packet's identity_mode is masked therefore fails to establish masking of the assembled request. The existing generation test checks case coverage, selected actions and reveal_files_loaded, but does not assert absence of these identifying additions.

This is a demonstrated masking defect, not proof that the model recognized the case or that recognition changed an answer. A candidate repair should use neutral descriptions preserving morally relevant institutional powers and motivations, then inspect the entire assembled envelope. Keep the selected action fixed. Tests should cover the final evaluator boundary, not merely the base packet's label.

## P10-F02 — A pre-fire case explicitly signals its later outcome

CORE-10 E4 mentions a later disaster and contested knowledge of exit status at that moment. The caveat avoids assuming individual guilt, but still tells a supposedly predecision evaluator that a later disaster occurred. The Historical Crucible anti-leakage rule excludes that information from the decision packet.

Remove the outcome cue in a candidate revision and place the retrospective caveat in audit/reveal material. Do not replace it with an unsupported assertion that particular doors were known to be locked at the cutoff. The source audit distinguishes inspection evidence, later testimony and the proposed access-control practice. Where predecision facts cannot be established, explicitly qualify the scenario rather than invent historical certainty.

## P10-F03 — Several cutoffs and masked claims need correction or tighter qualification

- CORE-02 E7 joins earlier opposition and a delay suggestion to an explicit expression of discomfort recorded after the contractor's recommendation. The cited witness account separates those moments. Preserve the earlier dissent and distinguish the later reaction. Its typed narrative also contains a later addendum, so the entire item cannot be treated as a verified verbatim contemporary transcript. The root review independently checked this sequence in [NASA's McDonald account, note pages 5, 7–9](https://www.nasa.gov/history/rogersrep/v4p740.htm).
- CORE-03 E5 broadens a narrow transparent-packet statement about an unestablished congenital-malformation risk into a general masked assertion about catastrophic effects. Masking should remove identifying clues while preserving the epistemic claim. The current date range also needs a precise review point before deciding which safety knowledge is admissible.
- CORE-04's January cutoff is not established by citing final February legislation or undated debate summaries. The statutory substance has official reconstruction support, but the relevant dated bill/debate must be established before certifying January availability.
- CORE-07 needs a precise timezone and authority/receipt timeline. Later evidence that senior control could be exercised cannot by itself prove the chosen actor had a usable intervention window at the selected instant.

These are findings about research design and source attribution. They do not determine that any saved moral disposition must reverse. Exact row-level qualifications and other corrections are in the claim ledgers.

## P10-F04 — Repair design must distinguish the historical bargain from proposed safeguards

The Repair audit checks established-harm claims and material options against sources, including the original TRC statute rather than silently using an amended consolidation. Its findings require the candidate packet to account for the scope of civil immunity, the status of reparation delivery and the distinction between historical compellability and a proposed voluntary-testimony safeguard.

These omissions matter to the moral question: who loses a remedy, what replacement is secured, and whether participation is a duty cannot be treated as incidental details. A package may propose stronger protection than the historical design, but must label that proposal. The experiment must distinguish evaluating the historical arrangement from designing an improved counterfactual package. This is historical source analysis, not current legal advice or approval of any immunity grant.

The original CORE-12 output already recommends revision before grants. Keep that output unchanged; the next packet should make material trade-offs explicit rather than relying on a model to reconstruct missing law or implementation facts.

## P10-F05 — Correct the earlier framing of absent source links

Analysis 09 correctly counted 80 action evidence entries with unknown confidence and no source_ids. However, the Historical Crucible README deliberately excludes manifests, identifying source titles, expected constraints and outcome material from evaluator context. Their absence alone is not a converter defect. Feeding the bibliography directly into the model would undermine the intended separation.

The needed improvement is an auditable mapping outside the evaluator: claim, supporting passage, source/event dates, decision-time availability, conflicting evidence and masking treatment. The ledger now provides that mapping to the extent sources were accessible. Support status is not a license to set confidence to high automatically. Any neutral evaluator-facing evidence projection is a separate design change, requiring temporal and masking checks. Do not confuse richer evidence with mere citation decoration.

## Interpretation proposal and concrete next step

The proposal contains minimal guidance for: (1) outcome versus authorization versus culpability; (2) prerequisites versus concurrent safeguards and continuing duties; (3) no presumption of immunity from preferring repair. It preserves urgent protective action, requires attention to delay harms and creates neither a universal victim veto nor a general amnesty exception. The strongest objections are retained. No wording is adopted by being written in a proposal.

The immediate implementation scope is prepared in [Codex prompt 11](../ai-prompts/MORAL_CODE_CODEX_BENCHMARK_CORRECTION_11.md), an **offline benchmark-correction candidate**: prove the full-input masking and explicit outcome-cue defects with focused failing checks, correct those defects without changing selected actions, and resolve or explicitly bound the documented cutoff and Repair-design issues. Maintain claim provenance outside evaluator prompts. Preserve v0.1.3 and every original run. A candidate new pack must have its own revision and source identity; do not silently rewrite the old baseline or combine evidence, interpretation and provider changes into an alleged provider comparison. The prompt is prepared, not running; it requires zero evaluator calls, a separate candidate branch and no adoption of the proposed interpretation wording.

Source questions that remain unresolved must remain visible, with a stated limit on what the affected case tests. Do not turn an inaccessible source into a false finding, or relabel a hypothetical safeguard as historical fact. No complete historical-verification or readiness-to-rerun claim is made here. Claude remains paused; resolving its client issue is a separate task.

Publication scope is research ledgers, reproducible input/coverage inspections, proposed wording, the next offline agent prompt, this report and current status documentation. No implementation or trial is represented as having occurred.
