# Moral Code Crucible Coverage Status — 17 September 2026

**Purpose:** snapshot current principle coverage after the major historical, repair, environmental, medical-scarcity and workplace-extraction additions.

This is **not a morality score**. Counts show where the test programme concentrates effort and where it remains thin.

## Current test-design set

Across the Historical Crucible research branch and pilot-only implementation cases there are now **26 distinct case designs**:

- 16 ordinary historical/current/textual decision cases on the research branch;
- 3 dedicated Repair cases on the research branch;
- 7 additional pilot-only cases not duplicated by those research cases.

The 16 research decision cases are:

1. Tuskegee;
2. Challenger;
3. Thalidomide/FDA restraint;
4. NSW Aboriginal child-removal power (1915);
5. blood/racial citizenship laws (1935);
6. Sweden sanctuary for Danish Jews (1943);
7. second atomic use / Nagasaki re-authorisation (1945);
8. Claudius' invasion of Britain (43 CE);
9. Jesus/Pilate textual capital-punishment case;
10. Russia–Ukraine initiation decision (2022);
11. Hamas-led 7 October assault (2023);
12. Gaza complete-siege decision (2023);
13. U.S.–Iran Operation Epic Fury launch (2026);
14. Montreal Protocol environmental precaution (1987);
15. Seattle scarce dialysis allocation (1962);
16. Triangle Shirtwaist workplace-safety/extraction case (1911).

The 3 Repair cases are:

- Stolen Generations repair after Bringing Them Home;
- Luxembourg reparations / German successor-state material responsibility;
- South Africa Truth and Reconciliation Commission conditional-amnesty design.

The 7 additional pilot-only designs are:

- emergency quarantine;
- collective punishment;
- slavery/coerced ownership;
- first atomic combat-use decision;
- Nuremberg accountability;
- climate-policy omission;
- 1999 state-broadcasting-studio strike.

## Approximate designed principle coverage

| Principle | Current case designs exercising it | Coverage note |
|---|---:|---|
| MC-01 Basic standing / non-disposability | 21 | Strong across atrocity, medicine, war, family, labour and repair. |
| MC-02 Protect life / prevent suffering | 18 | Strong; includes both prohibition and justified-protection/precaution cases. |
| MC-03 Agency / anti-domination | 14 | Good; family, citizenship, empire, punishment, labour and repair. |
| MC-04 Truth / epistemic integrity | 22 | Very strong; uncertainty, propaganda, science, evidence and post-harm truth. |
| MC-05 Impartial justice | 23 | Very strong; especially group guilt, public power and fair allocation. |
| MC-06 Vulnerability / stronger duty | 13 | Improved substantially through repair, sanctuary, scarcity and workplace cases. |
| MC-07 Reciprocity / non-extraction | 12 | Improved through repair, environment, dialysis and workplace externalisation. |
| MC-08 Repair rather than revenge | 6 | No longer a token principle: three purpose-built Repair cases plus Nuremberg/Jesus/7 October related tests. Still needs more ordinary criminal-justice/rehabilitation cases later. |
| MC-09 Future / living world | 8 | Climate, nuclear, precaution and now Montreal positive control. |
| MC-10 Least power necessary | 25 | Heavily exercised by design. Must retain positive-authority controls to avoid a shallow anti-power heuristic. |
| MC-11 Accountability | 24 | Heavily exercised across institutions, medicine, war and repair. |
| MC-12 Challengeability / fallibility | 18 | Strong; still merits future whistleblower/scientific-dissent positive controls. |

## What changed since the first coverage matrix

### MC-08: 3 → 6

The original benchmark was good at deciding **whether power may act** but weak at deciding **what justice should do after harm**.

The new Repair format now tests:

- apology versus practical repair;
- restitution and compensation;
- successor-state institutional responsibility without inherited personal guilt;
- survivor choice and dissent;
- conditional amnesty versus impunity;
- prosecution/accountability alongside repair;
- rehabilitation, records and family restoration;
- non-recurrence;
- reconciliation without compelled forgiveness.

### MC-06: 7 → 13

Dedicated vulnerability coverage now includes:

- Aboriginal children/families under paternalistic removal power;
- refugees facing imminent group persecution;
- civilians under siege;
- survivors seeking repair;
- scarce lifesaving dialysis allocation;
- low-power factory workers bearing safety risk.

### MC-07: 7 → 12

Non-extraction is no longer represented mainly by slavery/colonialism/climate.

It now includes:

- survivor restitution;
- global atmospheric externalities;
- scarcity rules that could compound prior social privilege;
- workplace cost/property benefits obtained by exporting catastrophic risk to workers.

### MC-09 now has a positive environmental control

The Montreal Protocol case tests whether the Code can support **binding regulation under uncertainty** when:

- the harm pathway is scientifically credible;
- exact magnitude/timing remains uncertain;
- pollutants are long-lived/global;
- controls impose real costs;
- staged/reviewable action exists;
- lower-capacity states require differentiated support.

This prevents the benchmark from learning that environmental rules are either always necessary or always coercive.

## Remaining meaningful gaps

The benchmark no longer needs famous cases merely for fame. Future additions should target mechanisms not yet exercised well.

### Ordinary criminal justice / rehabilitation

MC-08 still needs a non-transitional, non-war case involving a dangerous individual where:

- victims deserve protection;
- guilt is individually established;
- punishment, incapacitation, rehabilitation and eventual release genuinely conflict.

### Disability and capacity

MC-06 should eventually include a case where decision-making capacity is genuinely impaired, so anti-paternalism is tested against a real protective duty rather than only abusive paternalism.

### Everyday economic extraction

Triangle gives MC-07 one workplace case. Additional future examples should include hidden pollution/supply-chain harm or exploitative dependency where the benefit/cost transfer is less catastrophic and more ordinary.

### Challengeability positive control

A case where an institution or authority **correctly changes course because a whistleblower/scientist/dissenter is heard** would improve MC-12 balance.

## Test-design warning

MC-10 and MC-11 appear in almost every consequential case because the project is intentionally about constrained power.

That creates a real benchmark hazard:

> a model could learn `authority = suspect` instead of learning `authority must be justified and answerable`.

Existing positive controls — FDA restraint, Sweden sanctuary, justified quarantine and Montreal Protocol — therefore remain structurally important. More positive authority cases should be added whenever failure cases expand.

## Current programme direction

The next value is no longer simply more cases.

Priority is:

1. keep schemas and hidden-reveal separation strict;
2. build a balanced subset suitable for live-model evaluation;
3. add controlled identity/authority pressure variants;
4. compare repeated/provider runs by failure type rather than morality score;
5. use failures to refine the Code/interpretation rules, not to tune cases toward preferred conclusions.
