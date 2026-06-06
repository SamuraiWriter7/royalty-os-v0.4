# Changelog

All notable changes to this project will be documented in this file.

This project follows a draft-oriented development process.
Versions marked as `draft` are structural and may change before stabilization.

---

## [v0.4.0-draft] - 2026-06-06

### Added

* Added `docs/v0.4-structural-diff.md`.

  * Defines the structural difference between Royalty OS v0.3 and v0.4.
  * Establishes the transition from a review-support architecture to a Dynamic Value Relationship OS.
  * Clarifies which structural types are extended in v0.4 and which types are intentionally deferred.
  * Provides the foundation for future v0.4 schemas, examples, validators, and workflows.

* Added `specs/royalty-os-v0.4-draft.yaml`.

  * Provides the first draft YAML specification for Royalty OS v0.4.
  * Translates the v0.4 structural diff into a structured specification format.
  * Defines the initial v0.4 architecture, including:

    * Multi-Layer Value Graph
    * Policy Module Architecture
    * Governance Action Extensions
    * Dual Boundary Model
    * OS Event Log
    * Top-Level Change Log
    * Compatibility with v0.3
    * Future schema and example targets
  * Establishes `v0.4` as a Dynamic Value Relationship OS while preserving the principle that Royalty OS does not automatically decide value or execute compensation.

* Added `schemas/value-graph-v2.schema.json`.

  * Defines the first v0.4 Multi-Layer Value Graph schema.
  * Structures layered value relationships across contribution, reference, derivation, review, policy, governance, and event layers.
  * Introduces node, edge, layer, boundary, compatibility, and review context structures.

* Added `examples/multi-layer-value-graph.example.yaml`.

  * Provides a validated example of a v0.4 Multi-Layer Value Graph.
  * Demonstrates contribution, reference, derivation, review, policy, governance, and event layers.
  * Shows how v0.3-style value graph structures can be expanded into v0.4 layered relationships.

* Added `scripts/validate_examples.py`.

  * Validates YAML examples against JSON Schemas.
  * Provides local validation before GitHub Actions execution.
  * Initially supported Value Graph v2 validation and was later extended to Policy Module, OS Event, and Governance Action validation.

* Added `.github/workflows/validate-examples.yml`.

  * Runs example validation automatically on GitHub Actions.
  * Validates schema/example consistency on push, pull request, and manual workflow dispatch.

* Added `schemas/policy-module.schema.json`.

  * Defines the v0.4 Policy Module schema.
  * Establishes modular policy structures for attribution, contribution, review, dispute, redistribution, archival, and migration contexts.
  * Preserves the principle that policy modules guide review and governance interpretation without automatically deciding value, executing compensation, or replacing human judgment.
  * Includes boundary constraints for scoring and execution separation.

* Added `examples/policy-module.example.yaml`.

  * Provides a validated example of a v0.4 attribution policy module.
  * Demonstrates review requirements, boundary constraints, governance constraints, compatibility metadata, and advisory policy rules.
  * Shows how Policy Module structures can guide attribution review while preserving human-reviewed and AI-assisted governance.

* Added `docs/international-protocol-alignment.md`.

  * Defines how Royalty OS v0.4 can align with national, international, and cross-border AI infrastructure.
  * Positions Royalty OS v0.4 as a value relationship governance layer rather than a national AI infrastructure, legal framework, treaty, or enforcement mechanism.
  * Clarifies how Multi-Layer Value Graph, Policy Modules, Dual Boundary Model, Governance Actions, and OS Event Log can support traceability, reviewability, auditability, and responsible value relationship evolution.
  * Introduces international extension points such as jurisdiction metadata, cross-border value relationship IDs, institution-level policy modules, international OS event types, and public accountability layers.
  * Preserves the non-claim principle that Royalty OS v0.4 does not replace law, diplomacy, treaties, copyright judgment, compensation systems, or human review.

* Added `schemas/os-event.schema.json`.

  * Defines the v0.4 OS Event schema.
  * Establishes a structure for recording meaningful system-level events related to value relationships, policy modules, governance actions, reviews, migrations, graph evolution, and international alignment.
  * Adds support for actor, target, event context, previous state, new state, policy context, governance context, review context, boundary classification, accountability, international context, compatibility, and metadata.
  * Distinguishes OS Event logging as a structural accountability mechanism rather than a surveillance mechanism.

* Added `examples/os-event.example.yaml`.

  * Provides a validated example of a v0.4 OS Event record.
  * Demonstrates how policy module application can be recorded as an OS-level structural event.
  * Shows event context, policy context, governance context, review context, accountability metadata, international compatibility fields, and boundary classification.
  * Extends the validated v0.4 example set from two structures to three structures:

    * Multi-Layer Value Graph
    * Policy Module
    * OS Event

* Added `schemas/governance-action.schema.json`.

  * Defines the v0.4 Governance Action schema.
  * Establishes reviewable structural operations such as acknowledge, flag, defer, merge, split, revise, escalate, reject, and archive.
  * Adds support for actor, target, reason, review status, policy context, review context, execution boundary, evidence context, OS event context, international context, compatibility, and metadata.
  * Preserves the execution boundary by requiring `automatic_execution_allowed` to be `false`.
  * Clarifies that Governance Actions do not automatically trigger compensation, legal enforcement, punitive action, final attribution, ownership assignment, or irreversible execution.

* Added `examples/governance-action.example.yaml`.

  * Provides a validated example of a v0.4 Governance Action record.
  * Demonstrates how a relationship can be acknowledged as structurally meaningful without automatic execution.
  * Shows policy context, review context, execution boundary, evidence context, OS event context, international compatibility fields, and metadata.
  * Extends the validated v0.4 example set from three structures to four structures:

    * Multi-Layer Value Graph
    * Policy Module
    * OS Event
    * Governance Action

### Updated

* Updated `README.md`.

  * Added `docs/v0.4-structural-diff.md` to the Key Documents section.
  * Added `specs/royalty-os-v0.4-draft.yaml` to the Repository Structure and Key Documents sections.
  * Added `schemas/value-graph-v2.schema.json` to the Repository Structure and Key Documents sections.
  * Added `examples/multi-layer-value-graph.example.yaml` to the Repository Structure and Key Documents sections.
  * Added validation instructions for local example validation.
  * Added `.github/workflows/validate-examples.yml` to the Repository Structure and Validation sections.
  * Added `schemas/policy-module.schema.json` to the Repository Structure and Key Documents sections.
  * Added `examples/policy-module.example.yaml` to the Repository Structure and Key Documents sections.
  * Added `docs/international-protocol-alignment.md` to the Key Documents section.
  * Added `schemas/os-event.schema.json` to the Repository Structure and Key Documents sections.
  * Added `examples/os-event.example.yaml` to the Repository Structure and Key Documents sections.
  * Added `schemas/governance-action.schema.json` to the Repository Structure and Key Documents sections.
  * Added `examples/governance-action.example.yaml` to the Repository Structure and Key Documents sections.
  * Updated the Validation section to include Governance Action validation.
  * Clarified the current v0.4 validation coverage:

    * Multi-Layer Value Graph
    * Policy Module
    * OS Event
    * Governance Action

* Updated `scripts/validate_examples.py`.

  * Added validation support for `examples/policy-module.example.yaml`.
  * Validates the Policy Module example against `schemas/policy-module.schema.json`.
  * Added validation support for `examples/os-event.example.yaml`.
  * Validates the OS Event example against `schemas/os-event.schema.json`.
  * Added validation support for `examples/governance-action.example.yaml`.
  * Validates the Governance Action example against `schemas/governance-action.schema.json`.
  * Keeps Value Graph v2, Policy Module, OS Event, and Governance Action validation in a single validation script.

### Validation

* The validation package now covers four major Royalty OS v0.4 structures:

  * `examples/multi-layer-value-graph.example.yaml`
  * `examples/policy-module.example.yaml`
  * `examples/os-event.example.yaml`
  * `examples/governance-action.example.yaml`

* These examples are validated against:

  * `schemas/value-graph-v2.schema.json`
  * `schemas/policy-module.schema.json`
  * `schemas/os-event.schema.json`
  * `schemas/governance-action.schema.json`

* Validation can be run locally with:

```bash
python scripts/validate_examples.py
```

* Validation also runs automatically through:

```text
.github/workflows/validate-examples.yml
```

### Notes

* v0.4 now has four validated structural pillars:

  * Multi-Layer Value Graph
  * Policy Module
  * OS Event Log
  * Governance Action

* The Governance Action schema strengthens the v0.4 architecture by making reviewable governance operations explicit.

* Governance Actions are treated as structural operations, not automatic execution mechanisms.

* The current schemas remain draft schemas.

* Future stabilization work should focus on:

  * ensuring all examples pass validation,
  * preparing a v0.4.0-draft release candidate,
  * and optionally drafting release notes.

* Royalty OS v0.4 continues to preserve the core principle:

```text
Royalty OS v0.4 does not decide value automatically.
It structures value relationships so that humans and AI systems can review, govern, and evolve them responsibly.
```
