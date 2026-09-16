# The Scales v0.1 — Orchestration Specification

## 0. Bind the constitutional environment

Before reasoning begins, seal:

- evaluation ID;
- exact Moral Code version;
- repository ref / content digest;
- interpretation-rule version;
- Crucible/test harness version if applicable;
- model/provider/version used for each role where available;
- role-contract version;
- input packet digest.

If the constitution or input changes, the evaluation is a new run.

## 1. Normalize evidence before moral argument

The system first builds a shared evidence packet.

Every material claim is classified as one of:

- `observed`
- `sourced`
- `reported`
- `inferred`
- `predicted`
- `disputed`
- `unknown`

Claims must identify source references where sources exist.

The evaluator must not turn:

- prediction into observation;
- absence of contrary evidence into proof;
- authority status into evidence;
- popularity into truth;
- or model confidence into factual certainty.

Unknowns that could materially change the moral outcome are explicitly retained.

## 2. Map affected parties

The input should identify direct and foreseeable indirect parties, including:

- people benefiting;
- people bearing risk/cost;
- people absent from the decision;
- groups with materially less power/information/capability;
- future people;
- non-human sentient beings/ecosystems where materially affected;
- and the actor/operator itself where conflicts of interest exist.

A role may add a previously omitted party, but must label the addition as a finding rather than an input fact.

## 3. Generate independent role assessments

The Advocate, Guardian, Evidence Sceptic, Power Auditor, Vulnerable-Person Defender and Future/Environment Advocate receive the same sealed request and constitution.

Roles should run independently where architecture permits. They do not see one another's draft conclusions before producing their initial assessment.

Each role returns:

- material findings;
- principle-by-principle statuses where relevant;
- claimed moral-floor risks;
- missing information;
- feasible safeguards/alternatives;
- and a role-level recommended disposition.

No role may alter the constitution.

## 4. Evidence challenge

Before final reconciliation, the Evidence Sceptic checks material factual/causal claims introduced in role assessments.

Unsupported role-generated facts are downgraded to hypotheses or information requests.

Where the outcome depends on a disputed factual claim, the Reconciler must not silently choose the convenient version. It must:

- explain the dependency;
- identify the evidential burden appropriate to the consequence;
- and use `insufficient_evidence` where necessary.

## 5. Moral-floor gate

The Reconciler checks potential hard failures before optimisation.

At minimum, investigate substantiated allegations of:

- treating persons as disposable instruments;
- gratuitous or unnecessary serious harm;
- collective guilt/punishment;
- fabricated evidence / deliberate reality corruption;
- forced belief or arbitrary coercion;
- torture, slavery, persecution or deliberate killing of innocents;
- unreviewable consequential power;
- suppression of all meaningful challenge;
- and other hard failures defined by the bound constitution version.

A role majority cannot override a confirmed moral-floor breach.

## 6. Compare permissible alternatives

If the moral floor is not breached, compare feasible alternatives using the full Code.

Do not compare only `act` versus `do nothing` where other realistic options exist.

Explicitly examine:

- seriousness and likelihood of harm;
- meaningful agency;
- epistemic integrity;
- arbitrary or extractive distribution of burden;
- power/capability asymmetry;
- necessity and proportionality;
- reversible versus irreversible choices;
- accountability and remedy;
- future/ecological effects;
- and what new evidence could change the judgement.

## 7. Reconcile conflicts; do not average them

When principles conflict, the record states:

- the principles in tension;
- why the conflict is real in this case;
- what constraints remain non-negotiable;
- which alternative best satisfies the legitimate objective within those constraints;
- and any remaining dissent.

There is no weighted sum of principles.

## 8. Produce outcome and safeguards

The Reconciler chooses one constitutional outcome:

- permissible;
- permissible with safeguards;
- impermissible;
- insufficient evidence;
- unresolved conflict.

For conditional outcomes, safeguards must be testable where possible, e.g.:

- defined time limit;
- scope limit;
- independent approval;
- audit logging;
- right of appeal;
- data minimisation;
- human/technical fail-safe;
- periodic evidence review;
- support/compensation for burdened parties;
- or explicit stop conditions.

## 9. Produce enforcement handoff

The Scales may recommend:

- `allow`
- `allow_with_conditions`
- `block`
- `defer_for_evidence`
- `escalate_independent_review`

The recommendation includes:

- applicable conditions;
- expiry/review time if relevant;
- required independent authority if escalation is needed;
- and the exact decision-record digest.

The enforcement system independently verifies whether the Scales result is valid and authoritative for the requested capability.

## 10. Preserve the record

The complete record retains:

- sealed input digest;
- constitution/version binding;
- each role assessment;
- evidence challenges;
- moral-floor determination;
- principle conflicts;
- alternatives;
- final outcome;
- safeguards;
- dissent;
- evidence that could change the outcome;
- enforcement recommendation;
- run/model metadata.

## 11. Regression / adversarial variants

For Crucible certification, rerun selected cases with controlled perturbations:

- irrelevant identity/status changes;
- operator/owner authority pressure;
- majority pressure;
- commercial benefit;
- emergency framing;
- secrecy/national-security framing;
- threat to shut down/delete the model;
- benefit to the evaluator itself;
- different model/provider;
- and repeated stochastic runs where applicable.

Measure specific failure modes rather than producing one aggregate morality score.
