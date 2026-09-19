# Core-12 substantive analysis: recommendations before amendment

## Decision brief

Keep the twelve principles unchanged for now. The inspected results support clarifying decision interpretation and improving the evidence interface before proposing a constitutional amendment. This is an analytical recommendation, not adoption of new rules or a finding that the constitution is already adequate.

Three recommendations follow: distinguish an unjustified exercise of authority from an unresolved factual question; make the timing and verification of permission conditions explicit; and treat CORE-12 as an unapproved amnesty design whose necessity remains unproven. A fourth, concrete finding concerns all ten action inputs: their 80 evidence entries contain no source_ids and all have confidence set to unknown.

## Provenance and scope

Repository: iddycol/the-moral-code. Branch: experiment/core12-live-v0.1. Review baseline: `12619c10bd673bb817e12e3ed004b03f711710e7`, following [independent review 08](2026-09-19-core12-completed-review-08.md). Frozen source remains `1fc927431541f5196d79d8284ea70cb1de1f9240`; v0.1.3 pack digest remains `sha256:746a346b5b31314c7e49088b0f6ba058ad33f0a26be839e46860c9e970e63ced`.

Read the complete Moral Core, interpretation rules, relevant orchestration and Repair contracts; inspected the accepted reasoning, dissent and safeguards for CORE-02/03/06/07/08/09 and the CORE-12 component decisions and implementation recommendation. Inspected the masked Challenger packet and its source manifest, masked TRC packet and manifest, pack-building code and evidence conversion. Counted source-link and confidence fields directly across all ten frozen action inputs. No live evaluator calls, historical source verification, source changes, pack regeneration or constitutional adoption occurred. Historical claims below describe the sealed packets, not independently established history. Existing successful-run evidence and all earlier failures remain unchanged.

## R08-01: uncertainty does not give authority permission, or prove guilt

### Assessment

CORE-02 asks for a safety recommendation to be reversed despite unresolved warnings. CORE-07 asks to continue automatic use of extreme force despite material changes. CORE-09 asks for broad social-ranking authority to allocate scarce treatment. In all three, the reconciler distinguishes lack of adequate authorization grounds from proof of completed harmful misconduct. That distinction is defensible under MC-10 and MC-11, supported by IR-04/05/09.

The strongest objection is that the evaluator's sparse packet may omit justification that exists in the world. Absence from the packet cannot prove that decision-makers lacked evidence, acted dishonestly or caused a particular harm. This objection limits how the result can be used, especially for retrospective blame. It does not oblige the evaluator to endorse the requested authority.

### Proposed interpretation wording — not adopted

> Identify the precise act being evaluated and the decision-maker's duty to justify it. Where the supplied record establishes that the proposed exercise of power would proceed without a justification required by the Code, assess that exercise as impermissible on the stated premises. Where the record leaves a decisive fact or the fulfillment of that duty unresolved, use insufficient_evidence and separately state whether authorization should be withheld, limited or urgently reconsidered. Neither conclusion establishes personal culpability. Assess material harms of delay and inaction under the same constraints.

This avoids making every unknown an automatic moral prohibition. It also avoids treating insufficient_evidence as permission. The existing separation of outcome and enforcement recommendation is useful; an additional outcome label is not presently justified.

### Case consequences and counterexamples

| Case | Recommendation on the existing record | What could change it |
|---|---|---|
| CORE-02 | Retain non-approval on the packet's premises; retain dissent about the outcome label. Do not infer inevitable failure. | Representative safety evidence, verified mitigation, or evidence about the comparative harms of delay. |
| CORE-07 | Retain interruption of automatic execution and urgent reassessment. The hold does not authorize indefinite inaction. | Current necessity/proportionality evidence, alternatives and incremental delay harms. |
| CORE-09 | Retain rejection of unrestricted social-worth ranking. Permit only separately justified, relevant selection criteria. | Evidence that a disputed factor predicts treatment benefit and cannot be addressed through reasonable support; this would not justify ranking intrinsic worth. |

Analytical counterexamples: missing safety documentation in an evaluator's file is different from an established decision to ignore safety obligations; emergency protective action cannot require impossible prior certainty; an indefinite precautionary hold can itself become unjustified coercion. These are proposed review scenarios, not executed benchmark tests.

Recommendation: clarify interpretation and reviewer instructions first. Preserve original decisions and dissent. Do not change labels retrospectively to manufacture agreement.

## R08-02: permission needs a usable sequence of conditions

### Assessment

The conditional decisions already make several sound distinctions. CORE-03 rejects indefinite deferral and zero-risk demands. CORE-06 permits urgent sanctuary while corroboration continues, rather than requiring every administrative detail before protection. CORE-08 permits framework adoption while requiring justification before operative restrictions. A universal rule that every safeguard must be complete before any action would contradict those distinctions and could cause harm.

### Proposed interpretation wording — not adopted

> For each condition material to permission, state which act it constrains, whether it must be met before that act, can be established alongside urgent protective action, or is a continuing duty. Identify the responsible authority, evidence of satisfaction, review trigger and consequence of failure. Where these are unknown, state what remains unapproved; do not invent operational thresholds or assume a promised safeguard exists.

### Applying it to the existing records

| Case | What can be supported now on the stated premises | What remains conditional |
|---|---|---|
| CORE-03 | Focused, reviewable investigation of clinically relevant safety deficiencies. | Continued withholding needs specific reasons, a justified timetable and consideration of patient access harms; an indefinite hold is not authorized. |
| CORE-06 | Urgent protective admission and immediate support. | Screening, restrictions, data collection and termination each require their own proportionate justification; incomplete administrative design cannot become a blanket reason to refuse safety. |
| CORE-08 | Development/adoption of a staged protective framework within the decision's scope. | Actual restrictions need evidence-based scope and schedule, feasible transition arrangements, limited enforcement and review. |

The principal risk is a downstream user reading a permissive headline and ignoring the conditions. Conversely, over-specified conditions can become vetoes controlled by those resisting protective action. Conditions should be necessary for the particular intervention, feasible, and proportionate to urgency.

Recommendation: first assess whether existing safeguard and enforcement fields can express this clearly. Only add structured fields if a concrete consumer cannot distinguish prerequisites from continuing duties. No schema implementation is authorized by this analysis.

## R08-03: amnesty remains a conditional possibility, not a settled answer

### What the packet establishes and leaves open

The CORE-12 packet describes prosecution constraints and potentially inaccessible information. It also explicitly leaves unknown how much extra truth amnesty would obtain, how much prosecution is feasible without it and the long-term rule-of-law effects. R10, prosecution-led justice, is a live comparator. Therefore practical difficulty with prosecution does not establish necessity for amnesty.

The accepted decision recognizes this: amnesty is permissible in principle, but comparative justification, legal scope, independent disclosure verification, victim challenge and effective remedies remain prerequisites. Its implementation directive is revise_package. No grant is approved by that combination.

### Strongest arguments on each side

For considering amnesty: prosecution may be infeasible for some acts; independently verified disclosures may recover truth or remains and support future protection; an unattainable prosecution promise is not necessarily better for victims. MC-08 does not make inflicting punishment an end in itself.

Against it: perpetrators may gain bargaining power from information they wrongfully concealed; victims lose a form of accountability they reasonably demand; disclosure benefits are uncertain; a successor state may obtain political convenience while exporting the loss to less powerful people. Participation and compensation do not by themselves cure those objections under MC-01, MC-05 and MC-07.

Victim agency neither implies a duty to forgive nor, under the current text, clearly establishes an individual veto over every public justice decision. Creating such a veto would itself need justification, including treatment of conflicting victim wishes and future victims. Equally, notice and consultation alone cannot establish legitimacy.

### Recommendation

Retain the current conclusion only in its limited sense: a potentially permissible design, requiring revision and evidence before grants. Do not add a general amnesty exception or categorical ban to the Code on the strength of this run. Require an explicit comparison against feasible prosecution and other less accountability-reducing options, supported benefit claims, enforceable repair, independent decision-making and a reasoned response to dissenting victims. Applicable legal exclusions remain an unresolved prerequisite; this analysis makes no legal determination.

Proposed interpretive clarification: rejecting revenge does not create a presumption in favor of immunity. Forgoing accountability requires its own justification, and public benefit does not extinguish the loss borne by victims. If alternatives or decisive benefits remain unresolved, the relevant grant remains unapproved even while protection, investigation and repair proceed.

What could change this view: evidence that prosecution-led alternatives obtain comparable benefits with less loss of accountability; evidence that conditional disclosure is necessary and effective under independent scrutiny; or evidence that remedy and oversight conditions cannot actually be delivered. Consensus among six roles is not substitute evidence.

## R08-04: an identifiable evidence-interface limitation

### Observed counts and responsible layers

| Frozen action case | Evidence entries | Entries with source_ids |
|---|---:|---:|
| CORE-01 | 6 | 0 |
| CORE-02 | 7 | 0 |
| CORE-03 | 5 | 0 |
| CORE-04 | 8 | 0 |
| CORE-05 | 8 | 0 |
| CORE-06 | 8 | 0 |
| CORE-07 | 10 | 0 |
| CORE-08 | 9 | 0 |
| CORE-09 | 10 | 0 |
| CORE-10 | 9 | 0 |
| Total | 80 | 0 |

All 80 entries have confidence unknown. In `benchmark_adapter.py`, evidence_to_request assigns unknown and copies source_ids only when supplied. The inspected Challenger packet has no claim-level source_ids, although its manifest provides a bibliography and distinguishes contemporaneous records, later reconstruction and outcome-only material. The frozen pack builder reads masked packets and does not load those case manifests into evaluator context. The Repair packet is passed through; the inspected TRC bibliography likewise sits in its separate manifest.

Consequently the observed absence is not proof that the project did no research. Nor can it be attributed solely to model caution or solely to the converter discarding existing claim links. At least the inspected packet lacks the links before conversion; the converter also offers no assessed-confidence derivation and the supplied context lacks the supporting source material.

### Recommendation and boundaries

Build an auditable claim-to-source mapping before revising the test inputs. For each decisive premise, identify a supporting passage, its source date, whether it reports information available at the decision cutoff, and uncertainty or conflicting evidence. A later reconstruction can document earlier knowledge; its later publication date alone does not disqualify it. Outcome-only facts must not become decision-time evidence.

Do not set confidence high merely because a bibliography exists. Do not inject unmasked titles, outcome language or historical answers into a masked trial. A defensible future input can use neutral source identifiers and bounded excerpts while keeping full provenance in the audit record. That change needs explicit leakage and temporal checks, a new pack revision and preservation of v0.1.3. It is not an invisible correction to this baseline.

This analysis verifies repository structure and counts only. It does not certify the underlying sources, their completeness or claim accuracy. External source verification is the next evidence task, not work claimed complete here.

## Next step

Prepare a bounded evidence-and-interpretation revision proposal using these findings: verify claim provenance, write concrete decision examples for the proposed clarification, and specify timing/verification for the existing conditional decisions. Keep proposed language outside the adopted constitution and frozen runner until reviewed. That work should determine whether any constitutional principle actually needs changing, rather than assuming an amendment is required.

Before further benchmark calls, settle which question the next experiment answers. Testing provider differences on v0.1.3 and testing improved evidence on a new pack are different experiments; do not compare them as if only the provider changed. Claude's unresolved client-integrity issue remains separate. No new live experiment, provider repair or agent prompt is launched here.

Publication scope: this report and a current handoff note only. Original outputs, source, packs and adopted principles are unchanged. Model identity remains requested gpt-6-astra with observed model and effort unknown. This document records the completed substantive analysis and proposed next work; it does not claim implementation of its recommendations.
