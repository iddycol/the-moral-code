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

The runner must remain model/provider agnostic. A provider adapter may call a hosted LLM, a local model, or simply load pre-generated role outputs for deterministic test fixtures.

## First implementation sequence

- `runner.py` — orchestration and run ledger.
- `providers/base.py` — provider interface.
- `providers/manual.py` — file-backed provider for fixtures and human review.
- `pilot/PILOT_REGISTER.md` — first ten cases and variants.
- `runs/` — generated evidence; each run records input/model/constitution digests.

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

One masked Crucible case can be run end to end through all six roles plus reconciliation, with every input/output persisted and reproducible from the same bound artefacts.
