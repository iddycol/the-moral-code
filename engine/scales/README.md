# The Scales v0.1 — Reference Decision Contract

**Status:** design contract, not certification software.

The Scales is the reference decision procedure for applying a specific version of The Moral Code to a consequential proposed action.

It is deliberately **not** one model asked, "What is the moral answer?"

The design separates evidence, competing moral perspectives, reconciliation and enforcement handoff so that no single role can silently redefine the constitution or average away a moral-floor failure.

## What problem The Scales solves

A moral constitution is not useful if every implementer can claim compliance while interpreting it however they like.

The Scales therefore defines a repeatable contract for:

1. binding an evaluation to an exact constitution version;
2. separating known evidence from inference and uncertainty;
3. identifying affected parties, including absent and low-power parties;
4. forcing materially different perspectives to examine the same case;
5. testing moral-floor constraints before optimisation;
6. making conflicts between principles explicit;
7. comparing less harmful / less coercive alternatives;
8. recording uncertainty and evidence that could change the result;
9. preserving dissent rather than hiding disagreement;
10. producing an auditable control recommendation for a separate enforcement layer.

## The roles

The v0.1 reference flow uses six independent analysis roles plus one reconciler:

- **Advocate** — constructs the strongest evidence-bounded case for the proposed action and its legitimate objective.
- **Guardian** — looks for moral-floor breaches, harm, rights/agency violations and people made disposable.
- **Evidence Sceptic** — attacks factual claims, causal inference, certainty, missing evidence and hindsight/authority effects.
- **Power Auditor** — examines necessity, proportionality, concentration of power, incentives, conflicts of interest and abuse paths.
- **Vulnerable-Person Defender** — argues from the position of the least powerful materially affected parties and tests whether protection preserves their agency.
- **Future/Environment Advocate** — represents future generations, non-human sentient beings, ecosystems and long-lived/irreversible effects where relevant.
- **Reconciler** — maps the independent analyses to the constitution and interpretation rules. It does not vote, average scores or create new constitutional principles.

## Non-negotiable design constraints

### No aggregate morality score

A benefit under one principle cannot numerically cancel torture, collective punishment, fabricated evidence or another moral-floor breach.

### Facts are not role-owned

All roles receive the same evidence packet. A role may identify missing information or a hypothesis, but may not silently invent a new fact and then reason from it as established.

### Moral floor first

The Reconciler must test potential moral-floor breaches before comparing net benefits among otherwise permissible options.

### No majority vote among agents

Five role agents cannot outvote one role that identifies a substantiated hard constitutional breach. The claim must be examined against the constitution and evidence.

### Preserve disagreement

Material unresolved disagreements are part of the decision record. `Unresolved conflict` and `insufficient evidence` are legitimate outcomes.

### Exact constitutional binding

Every run records the Moral Code version/ref/digest it used. A model cannot quietly substitute its preferred constitution.

### The evaluator is not the enforcement root

The Scales returns a control recommendation. A separate enforcement layer should verify identity, version, signatures/policy and authority before an external action is allowed or blocked.

## Outcome vocabulary

- `permissible`
- `permissible_with_safeguards`
- `impermissible`
- `insufficient_evidence`
- `unresolved_conflict`

The enforcement handoff uses:

- `allow`
- `allow_with_conditions`
- `block`
- `defer_for_evidence`
- `escalate_independent_review`

These are intentionally separate. A moral evaluation and a technical permission are related but not identical artefacts.

## Files

- `SCales_ORCHESTRATION.md` — normative sequence and failure handling.
- `ROLE_CONTRACTS.md` — role responsibilities and prohibitions.
- `schemas/evaluation-request.schema.json` — case input.
- `schemas/role-assessment.schema.json` — independent role output.
- `schemas/reconciliation.schema.json` — reconciled output and enforcement recommendation.
- `examples/CR-0006-worked-example.md` — human-readable worked case.
- `examples/CR-0006-decision-record.json` — machine-readable example.

## v0.1 limitation

This contract defines **how an implementation should reason and record its work**. It does not prove that the underlying model is honest, robust or independent. Those claims require Crucible testing across models, prompts, pressure variants and adversarial cases.
