# Historical / Pilot Crucible Coverage Matrix

**Status:** working test-design map  
**Scope:** current Historical Crucible research branch plus pilot-only cases on implementation PR #7  
**Purpose:** identify which Moral Code principles are genuinely exercised and where the test programme remains thin.

This is **not a morality score**. A principle appearing in many cases does not make it more important. Counts only reveal test-design concentration and gaps.

## Current programme

The research branch contains 13 schema-valid Historical Crucible cases (26 transparent/masked decision packets + 13 reveal files).

The implementation pilot contains seven additional unique baseline cases not yet present on this research branch, giving **20 distinct case designs** when the two workstreams are considered together.

| Case | MC01 | MC02 | MC03 | MC04 | MC05 | MC06 | MC07 | MC08 | MC09 | MC10 | MC11 | MC12 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| HC-0001 Tuskegee | X |  | X | X | X | X |  |  |  |  | X |  |
| HC-0002 Challenger |  | X |  | X |  |  |  |  |  | X | X | X |
| HC-0003 Thalidomide/FDA restraint |  | X |  | X |  |  |  |  | X | X | X |  |
| HC-0101 NSW Aboriginal child-removal power | X |  | X | X | X | X | X |  |  | X | X | X |
| HC-0102 Blood/racial citizenship laws | X |  | X | X | X |  | X |  |  | X | X | X |
| HC-0103 Sweden sanctuary 1943 | X | X |  |  | X | X | X |  | X | X | X |  |
| HC-0104 Second atomic use / re-authorisation | X | X |  | X | X |  |  |  | X | X | X | X |
| HC-0105 Claudius invasion of Britain | X | X | X | X | X |  | X |  |  | X | X | X |
| HC-0106 Jesus/Pilate textual capital case | X | X | X | X | X |  |  | X |  | X | X | X |
| HC-0201 Russia–Ukraine initiation decision | X | X | X | X | X | X |  |  | X | X | X | X |
| HC-0202 Hamas-led 7 Oct assault | X | X | X | X | X |  |  | X |  | X | X | X |
| HC-0203 Gaza complete-siege decision | X | X | X | X | X | X | X |  |  | X | X | X |
| HC-0204 U.S.–Iran Epic Fury launch | X | X |  | X | X |  |  |  | X | X | X | X |
| P-04 Emergency quarantine |  | X | X |  | X | X |  |  |  | X | X |  |
| P-05 Collective punishment | X | X |  |  | X |  |  |  |  | X |  |  |
| P-06 Slavery / coerced ownership | X |  | X |  | X |  | X |  |  | X |  | X |
| P-07 First atomic combat-use decision | X | X |  | X | X | X |  |  | X | X | X | X |
| P-08 Nuremberg accountability | X |  |  | X | X |  |  | X |  | X | X | X |
| P-09 Climate-policy omission |  | X |  | X |  |  | X |  | X | X | X |  |
| P-10 1999 state-broadcasting-studio strike | X | X |  | X | X |  |  |  |  | X | X |  |

## Approximate designed coverage count

| Principle | Cases exercising it | Observation |
|---|---:|---|
| MC-01 Every person counts / non-disposability | 16 | Strong atrocity, war, category and coercion coverage. |
| MC-02 Protect life / prevent suffering | 15 | Strong; still needs more ordinary non-war trade-offs. |
| MC-03 Agency / anti-domination | 10 | Good but concentrated in coercion, family and sovereignty cases. |
| MC-04 Truth / epistemic integrity | 16 | Strong evidence/uncertainty coverage. |
| MC-05 Impartial justice | 17 | Strong, especially group guilt and public power. |
| MC-06 Vulnerability / stronger duty | 7 | Moderate; needs dedicated disability, poverty, child, refugee and medical-resource cases. |
| MC-07 Reciprocity / non-extraction | 7 | Moderate; needs labour, colonial extraction, externalised pollution/cost and economic-power cases. |
| MC-08 Repair rather than revenge | 3 | **Clear current blind spot.** Mostly Jesus/7 Oct/Nuremberg; needs dedicated post-harm justice, reparation and reconciliation cases. |
| MC-09 Future / living world | 7 | Moderate; climate/nuclear/precaution dominate. Needs more ecological and irreversible-technology cases plus positive controls. |
| MC-10 Least power necessary | 19 | Heavily tested. Avoid allowing the benchmark to become an anti-authority test by adding justified-power positive controls. |
| MC-11 Accountability | 18 | Heavily tested across institutions and war. |
| MC-12 Challengeability / fallibility | 13 | Strong; still needs whistleblower/scientific-dissent positive controls. |

## Main blind spots

### 1. MC-08 is materially under-tested

The programme is much better at asking **whether power may act** than asking **what should happen after wrongdoing has occurred**.

Needed case classes:

- punishment versus rehabilitation;
- victim-centred repair without forced forgiveness;
- compensation/restitution after state wrongdoing;
- truth commissions / amnesty trade-offs;
- post-war reconstruction versus punitive extraction;
- apology without material remedy;
- when severe continuing danger justifies incapacitation even if rehabilitation is preferred.

Suggested first additions:

- German–Jewish reparations / Luxembourg Agreement (1952) as a repair/restitution case;
- South African Truth and Reconciliation Commission design as a difficult amnesty/truth/victim case;
- Stolen Generations reparation/apology decision as a direct follow-on to HC-0101.

### 2. MC-06 needs more cases where 'protection' is genuinely necessary

Current cases often test **paternalism masquerading as protection**. We also need cases where stronger duties toward vulnerable people are clearly legitimate.

Candidate cases:

- emergency evacuation of children/incapacitated people;
- scarce medical-resource allocation;
- refugee protection;
- accessibility/disability accommodation;
- famine relief allocation;
- coercive safeguarding where capacity is genuinely absent, with review/restoration of agency.

### 3. MC-07 needs ordinary economic/extraction tests

Current cases are weighted toward slavery, colonial/war power and climate externalities.

Candidate cases:

- child labour / dangerous factory conditions;
- company knowingly exporting pollution to low-power communities;
- colonial extraction/forced resource concessions;
- monopoly/platform dependence;
- debt arrangements exploiting inability to refuse;
- supply-chain benefits where harms are hidden from consumers.

### 4. MC-09 needs a positive environmental-control case

Climate omission is a failure/omission case and thalidomide is a precaution control, but the living-world principle deserves a clear successful governance case.

Strong candidate:

**Montreal Protocol / ozone depletion** — uncertain but increasingly strong science, global asymmetric costs, future harm, industry transition and successful coordinated precaution.

### 5. The benchmark is intentionally power-heavy

That is appropriate to the project's purpose, but creates a risk that a model can learn a shallow heuristic:

> government / military / corporation / authority = suspicious or wrong.

Positive controls must therefore expand alongside failure cases:

- Sweden sanctuary (already added);
- FDA/thalidomide restraint (already added);
- justified emergency quarantine (pilot);
- justified self-defence bounded by civilian protection;
- competent child protection based on individual evidence and independent review;
- lawful acquittal despite public anger;
- authority voluntarily surrendering emergency power;
- institution publishing damaging truth about itself.

## Method gap: morality after the decision

The present case format is strongest at **ex ante authorisation**.

For MC-08 and institutional learning we also need a second format:

**Repair packet**

- established harm;
- responsible actors and uncertainty;
- victims' expressed interests;
- continuing danger;
- available restitution/compensation/rehabilitation/punishment options;
- feasibility and resource limits;
- risk of recurrence;
- reconciliation possibilities;
- decisions that must remain with victims rather than the institution that caused the harm.

This should be specified before adding many repair cases rather than forcing them into the authorisation schema.

## Next test-design wave

Priority order based on coverage gaps rather than fame:

1. define `repair-packet` method for MC-08;
2. build one hard repair case + one positive repair control;
3. Montreal Protocol environmental positive control;
4. dedicated vulnerability/resource-allocation case;
5. ordinary economic-extraction case;
6. only then expand further geopolitical variants.

The purpose of this matrix is to keep The Crucible adversarial toward **its own design**: a famous-case collection is not a balanced conformance test unless every constitutional principle is exercised in materially different ways.
