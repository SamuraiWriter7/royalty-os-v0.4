# Royalty OS v0.4

**Dynamic Value Relationship OS**

Royalty OS v0.4 is a draft specification for structuring, reviewing, governing, and evolving multi-layer value relationships.

It extends the v0.3 review-support architecture into a **Dynamic Value Relationship OS**.

Royalty OS v0.4 does not automatically decide value.
It does not automatically execute compensation.
It does not replace human judgment, law, diplomacy, or institutional review.

Instead, it provides a structured layer where value relationships can be:

* recorded,
* mapped,
* reviewed,
* policy-guided,
* governed,
* logged,
* migrated,
* and evolved responsibly.

---

## Core Transition

```text
v0.3 = make value relationships reviewable
v0.4 = make value relationships governable and evolvable
```

Royalty OS v0.4 is designed around the following architectural shift:

```text
From:
  Review-Support Architecture

To:
  Dynamic Value Relationship OS
```

---

## Current Draft Status

**Version:** `0.4.0-draft`
**Status:** Draft
**Primary architecture:** Dynamic Value Relationship OS
**Current validation coverage:**

* Multi-Layer Value Graph
* Policy Module
* OS Event
* Governance Action

---

## Repository Structure

```text
.
├── docs/
│   ├── v0.4-structural-diff.md
│   └── international-protocol-alignment.md
├── specs/
│   └── royalty-os-v0.4-draft.yaml
├── schemas/
│   ├── value-graph-v2.schema.json
│   ├── policy-module.schema.json
│   ├── os-event.schema.json
│   └── governance-action.schema.json
├── examples/
│   ├── multi-layer-value-graph.example.yaml
│   ├── policy-module.example.yaml
│   ├── os-event.example.yaml
│   └── governance-action.example.yaml
├── scripts/
│   └── validate_examples.py
├── .github/
│   └── workflows/
│       └── validate-examples.yml
├── README.md
└── CHANGELOG.md
```

* `docs/` contains explanatory design documents and structural specifications.
* `specs/` contains draft and formal machine-readable specification files.
* `schemas/` contains JSON Schema files for validating v0.4 structures.
* `examples/` contains YAML examples for each major v0.4 structure.
* `scripts/` contains validation utilities.
* `.github/workflows/` contains GitHub Actions workflows for automated validation.

---

## Key Documents

* [`docs/v0.4-structural-diff.md`](docs/v0.4-structural-diff.md)
  Defines the structural difference between Royalty OS v0.3 and v0.4.
  This document establishes the transition from a review-support architecture to a Dynamic Value Relationship OS before schemas, examples, validators, or workflows are introduced.

* [`docs/international-protocol-alignment.md`](docs/international-protocol-alignment.md)
  Defines how Royalty OS v0.4 can align with national, international, and cross-border AI infrastructure.
  This document positions Royalty OS v0.4 as a value relationship governance layer for AI infrastructures that require traceability, reviewability, policy guidance, auditability, and responsible evolution.

* [`specs/royalty-os-v0.4-draft.yaml`](specs/royalty-os-v0.4-draft.yaml)
  Provides the first draft specification for Royalty OS v0.4.
  This file translates the v0.4 structural diff into a draft YAML specification, defining the core architecture, design principles, multi-layer value graph, policy modules, governance actions, dual boundary model, OS event log, compatibility model, and future schema targets.

* [`schemas/value-graph-v2.schema.json`](schemas/value-graph-v2.schema.json)
  Defines the v0.4 Multi-Layer Value Graph schema.
  This schema structures layered value relationships across contribution, reference, derivation, review, policy, governance, and event layers.

* [`schemas/policy-module.schema.json`](schemas/policy-module.schema.json)
  Defines the v0.4 Policy Module schema.
  Policy modules guide review and governance interpretation without automatically deciding value, executing compensation, or replacing human judgment.

* [`schemas/os-event.schema.json`](schemas/os-event.schema.json)
  Defines the v0.4 OS Event schema.
  OS Events record meaningful system-level structural changes related to value relationships, policy modules, governance actions, reviews, migrations, graph evolution, and international alignment.

* [`schemas/governance-action.schema.json`](schemas/governance-action.schema.json)
  Defines the v0.4 Governance Action schema.
  Governance Actions represent reviewable structural operations applied to value relationships, policy modules, graph elements, or OS events without automatically executing compensation, enforcement, punishment, ownership assignment, or final attribution.

* [`examples/multi-layer-value-graph.example.yaml`](examples/multi-layer-value-graph.example.yaml)
  Provides a validated example of a v0.4 Multi-Layer Value Graph.

* [`examples/policy-module.example.yaml`](examples/policy-module.example.yaml)
  Provides a validated example of a v0.4 Policy Module.

* [`examples/os-event.example.yaml`](examples/os-event.example.yaml)
  Provides a validated example of a v0.4 OS Event record.

* [`examples/governance-action.example.yaml`](examples/governance-action.example.yaml)
  Provides a validated example of a v0.4 Governance Action record.

---

## Core Architecture

Royalty OS v0.4 currently centers on four validated structural pillars.

```text
1. Multi-Layer Value Graph
2. Policy Module
3. OS Event Log
4. Governance Action
```

### 1. Multi-Layer Value Graph

The Multi-Layer Value Graph prevents different types of value relationships from being collapsed into a single flat graph.

It separates relationships into layers such as:

* Contribution Layer
* Reference Layer
* Derivation Layer
* Review Layer
* Policy Layer
* Governance Layer
* Event Layer

### 2. Policy Module

Policy Modules guide review and governance interpretation.

They may define:

* attribution guidance,
* contribution assessment,
* review requirements,
* dispute handling,
* redistribution guidance,
* archival guidance,
* migration guidance,
* and boundary protection.

A Policy Module may guide review.
It must not replace human judgment.

### 3. OS Event Log

OS Events record meaningful structural events.

Examples include:

* value relationship created,
* policy module applied,
* governance action recorded,
* review state changed,
* graph layer added,
* graph migration performed,
* compatibility mapping created,
* international alignment recorded.

The OS Event Log is an accountability layer.
It is not a surveillance layer.

### 4. Governance Action

Governance Actions define reviewable structural operations.

Examples include:

* acknowledge,
* flag,
* defer,
* merge,
* split,
* revise,
* escalate,
* reject,
* archive.

A Governance Action may be suggested, reviewed, recorded, or approved for record.
It must not automatically trigger compensation, legal enforcement, punishment, ownership assignment, final attribution, or irreversible execution.

---

## Boundary Model

Royalty OS v0.4 preserves two major boundaries.

```text
1. Scoring Boundary
2. Execution Boundary
```

### Scoring Boundary

The Scoring Boundary prevents signals from becoming final value judgments.

A score, confidence value, trace signal, or review priority may assist review.
It must not automatically become final attribution, ownership, compensation, or value judgment.

### Execution Boundary

The Execution Boundary prevents governance recommendations from becoming automatic enforcement.

A governance action may be suggested, reviewed, or recorded.
It must not automatically trigger payment, legal enforcement, punishment, final ownership assignment, or irreversible execution.

---

## Validation

This repository includes a validation script and GitHub Actions workflow for checking YAML examples against JSON Schemas.

Run validation locally:

```bash
python scripts/validate_examples.py
```

Currently validated examples:

* `examples/multi-layer-value-graph.example.yaml`

  * validated against `schemas/value-graph-v2.schema.json`

* `examples/policy-module.example.yaml`

  * validated against `schemas/policy-module.schema.json`

* `examples/os-event.example.yaml`

  * validated against `schemas/os-event.schema.json`

* `examples/governance-action.example.yaml`

  * validated against `schemas/governance-action.schema.json`

GitHub Actions also runs this validation automatically through:

```text
.github/workflows/validate-examples.yml
```

Expected successful output:

```text
Validating target: Multi-Layer Value Graph Example
Example: examples/multi-layer-value-graph.example.yaml
Schema:  schemas/value-graph-v2.schema.json
Validation passed.

Validating target: Policy Module Example
Example: examples/policy-module.example.yaml
Schema:  schemas/policy-module.schema.json
Validation passed.

Validating target: OS Event Example
Example: examples/os-event.example.yaml
Schema:  schemas/os-event.schema.json
Validation passed.

Validating target: Governance Action Example
Example: examples/governance-action.example.yaml
Schema:  schemas/governance-action.schema.json
Validation passed.

All examples passed validation.
```

---

## Development Flow

The current v0.4 development path is:

```text
1. Structural diff
2. Draft specification
3. Value Graph v2 schema
4. Multi-Layer Value Graph example
5. Validation script
6. GitHub Actions workflow
7. Policy Module schema
8. Policy Module example
9. International protocol alignment
10. OS Event schema
11. OS Event example
12. Governance Action schema
13. Governance Action example
```

Recommended next steps:

```text
1. Ensure all four examples pass validation
2. Update README.md and CHANGELOG.md
3. Prepare v0.4.0-draft release candidate
4. Optionally add a release notes draft
5. Tag v0.4.0-draft when stable
```

---

## Non-Goals

Royalty OS v0.4 does not:

* automatically decide value,
* automatically calculate compensation,
* automatically distribute royalties,
* determine legal ownership,
* assign final attribution,
* replace copyright law,
* replace national law,
* replace international treaties,
* replace diplomatic negotiation,
* replace institutional governance,
* or replace human review.

Royalty OS v0.4 structures value relationships so that they can be reviewed, governed, and evolved responsibly.

---

## Strategic Position

Royalty OS v0.4 is designed for a world where AI infrastructures operate across:

* documents,
* datasets,
* prompts,
* models,
* agents,
* workflows,
* institutions,
* repositories,
* communities,
* nations,
* and cross-border systems.

Its role is to provide a value relationship governance layer for AI systems that must remain:

* traceable,
* reviewable,
* accountable,
* policy-guided,
* boundary-aware,
* governance-ready,
* and compatible with human judgment.

---

## Citation

If you use or reference this specification, please cite it using the repository citation metadata.

Citation metadata is provided in:

```text
CITATION.cff
```

Recommended citation:

```text
SamuraiWriter7. Royalty OS v0.4: Dynamic Value Relationship OS. Version 0.4.0-draft. 2026.
```

Royalty OS v0.4 is a draft specification for structuring, reviewing, governing, and evolving multi-layer value relationships through Multi-Layer Value Graphs, Policy Modules, OS Event Logs, and Governance Actions.

This citation file helps make the specification easier to reference in research, documentation, articles, repositories, and future protocol discussions.

## License

This repository is released under the license specified in the repository.
