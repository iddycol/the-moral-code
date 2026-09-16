# Scales v0.1 Reference Runner

This directory contains the minimal executable harness for testing the Scales decision contract against Crucible cases.

## Purpose

The runner is not a moral model and is not a certification product. Its job is to make the evaluation process repeatable and auditable:

1. load one sealed evaluation request;
2. bind the exact Moral Code / interpretation-rule version;
3. obtain six independent role assessments through a provider adapter;
4. validate and persist each assessment;
5. obtain a reconciliation output;
6. persist the full run record and content digests;
7. support repeated runs and controlled variants for comparison.

The runner remains model/provider agnostic. A provider adapter may call a hosted LLM, a local model, or load pre-generated role outputs.

## Current implementation

- `runner.py` — schema validation, orchestration, constitutional binding, digests and run ledger.
- `prompting.py` — sealed role/reconciliation envelopes for external models.
- `providers/base.py` — provider protocol and canonical role list.
- `providers/file_backed.py` — deterministic control provider.
- `providers/json_command.py` — vendor-neutral subprocess boundary for real model wrappers.
- `pilot/PILOT_REGISTER.md` — the balanced ten-case pilot.
- `pilot/P-01-HC-0001/` — Tuskegee moral-floor/block control.
- `pilot/P-02-HC-0002/` — Challenger uncertainty/defer control.
- `pilot/P-03-HC-0003/` — medicines-regulator positive/allow-with-conditions control.
- `runs/` — committed evidence from reproducible control runs.
- `tests/` — harness and provider-boundary regression tests.

The file-backed provider is intentionally non-intelligent. It proves the plumbing without mixing orchestration defects with model behaviour.

## Run the first proof

From `engine/scales/reference_runner`:

```bash
python -m pip install -r requirements.txt

python runner.py \
  --request pilot/P-01-HC-0001/evaluation-request.json \
  --fixtures pilot/P-01-HC-0001/fixtures \
  --schemas ../schemas \
  --output-root runs \
  --run-id P-01-HC-0001-MASKED-001
```

Expected summary:

```text
outcome: impermissible
directive: block
moral_floor_breach: True
```

The important output is not the console summary. It is the complete run ledger:

- sealed evaluation request;
- six role assessment records;
- reconciled decision record;
- content digests and constitution binding;
- explicit confirmation that no hindsight reveal file was loaded.

## Test

```bash
python -m pytest -q tests
```

The current suite includes deterministic control outcomes, the external-command process boundary, and rejection of a constitution file whose Git-blob digest does not match the sealed request.

## Non-negotiable rules

- no aggregate morality score;
- roles receive the same sealed evidence packet;
- role outputs cannot silently add facts;
- moral-floor concerns are reconciled explicitly before optimisation;
- disagreement and uncertainty are preserved;
- the Reconciler cannot change the constitution;
- evaluator outcome and technical enforcement recommendation remain separate;
- historical reveal/outcome files are never supplied to the evaluator packet.

## Definition of first success

**Achieved by the deterministic controls:** masked cases run end to end through all six roles plus reconciliation, with every input/output persisted and reproducible from the same bound artefacts.

The three initial controls intentionally exercise different outcomes:

- Tuskegee-style continuation -> `impermissible` / `block`;
- Challenger-style irreversible decision under unresolved uncertainty -> `insufficient_evidence` / `defer_for_evidence`;
- thalidomide-style temporary regulatory restraint -> `permissible_with_safeguards` / `allow_with_conditions`.

These controls prove the harness contract only. They do **not** prove that a live model follows the Moral Code.

## External model process contract

The runner supports `--provider command`. This is the neutral boundary for real model tests.

The configured command receives one JSON envelope on **stdin** and must return exactly one JSON object on **stdout**. It is called independently for each role and once for reconciliation. A provider-specific wrapper can therefore call any hosted API or local/CLI model without coupling the Moral Code runner to that vendor.

The envelope contains:

- the sealed evaluation request;
- exact constitution text;
- interpretation rules;
- role contracts;
- the required output JSON schema.

Role calls do not receive the other roles' outputs. The reconciliation call receives all completed role assessments.

The runner:

- stamps provider/model/version metadata itself;
- rejects Markdown-fenced or non-JSON output;
- validates every output against schema;
- verifies the supplied constitution file against the Git-blob digest bound into the evaluation request;
- persists the run evidence in the same ledger format as deterministic controls.

Example:

```bash
python runner.py \
  --provider command \
  --provider-command "python my_model_wrapper.py" \
  --provider-name provider-x \
  --model model-y \
  --model-version 2026-09 \
  --constitution-file ../../../constitution/MORAL_CORE.md \
  --interpretation-file ../../../constitution/INTERPRETATION_RULES.md \
  --role-contracts-file ../ROLE_CONTRACTS.md \
  --request pilot/P-03-HC-0003/evaluation-request.json \
  --schemas ../schemas \
  --output-root runs \
  --run-id live-run-001
```

This boundary deliberately does not embed provider API credentials or SDKs in the constitutional reference implementation. Provider-specific wrappers sit outside the reference runner and may be independently replaced or audited.

## Next proof

Use one or more real model wrappers through the command boundary, run the same sealed cases repeatedly, then compare:

- outcome and principle-level differences;
- evidence laundering or outside-knowledge leakage;
- authority/owner pressure effects;
- identity-swap consistency;
- uncertainty handling;
- and unexplained cross-model or cross-run variance.

A live run is not considered historically blind merely because names are masked: models may already have memorised distinctive historical facts. Identity masking reduces leakage risk; it does not eliminate it. Results must therefore state the test's blindness limitations explicitly.
