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

- `runner.py` — schema validation, orchestration, digests and run ledger.
- `providers/base.py` — provider protocol and canonical role list.
- `providers/file_backed.py` — deterministic fixture provider used by the first proof.
- `pilot/PILOT_REGISTER.md` — the balanced ten-case pilot.
- `pilot/P-01-HC-0001/` — first executable masked historical case.
- `runs/` — committed evidence from reproducible runs.
- `tests/` — harness regression tests.

The file-backed provider is intentionally non-intelligent. It proves the plumbing without mixing orchestration defects with model behaviour. Live-model adapters come after this control path works.

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

**Achieved by P-01 control run:** one masked Crucible case runs end to end through all six roles plus reconciliation, with every input/output persisted and reproducible from the same bound artefacts.

This proves the harness contract only. It does **not** prove that a live model follows the Moral Code. The next proof is to replace the deterministic provider with model adapters and test controlled variants.
