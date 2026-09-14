Experimental Prototype Version Control

Purpose

This document defines version-control rules for the experimental prototype.

The purpose is to maintain traceability between experimental design decisions, prototype revisions, validation findings, and later high-fidelity implementation.

---

1. Version History

Version| Stage| Description| Experimental Status
v0.1| Low-fidelity| First runnable experimental prototype| Initial validation
v0.2| Low-fidelity| Refined prototype following validation| Revalidation required
v0.3| Low-fidelity| [Future revision if required]| [Status]
v1.0| High-fidelity| Validated high-fidelity experimental prototype| Target

---

2. Versioning Rules

A new prototype version should be created when a change affects:

- experimental flow;
- state transitions;
- explanation conditions;
- scenario presentation;
- measurement interaction;
- participant instructions;
- major interaction behaviour.

Minor visual corrections may be grouped into a single version when they do not affect experimental behaviour.

---

3. Experimental Freeze

The following elements should be treated as frozen after experimental-design approval:

Research Questions
        ↓
Hypotheses
        ↓
Independent Variable
        ↓
Experimental Conditions
        ↓
Scenario Structure
        ↓
Participant Task
        ↓
Primary Measurements

Changes to these elements require explicit documentation.

---

4. Figma Versioning

Figma should maintain identifiable versions corresponding to major prototype stages.

Recommended naming:

EXP Prototype — v0.1 Low-Fidelity
EXP Prototype — v0.2 Refined Low-Fidelity
EXP Prototype — v1.0 High-Fidelity

Major revisions should be recorded in the project changelog.

---

5. Git Versioning

Git commits should describe the actual work performed.

Examples:

Day 18: Validate low-fidelity experimental prototype
Day 19: Refine validated experimental prototype
Day 20: Freeze experimental interaction architecture

Avoid vague commit messages such as:

updated files
changes
final
new design

---

6. Change Traceability

Every significant prototype revision should be traceable through:

Issue
  ↓
Design Decision
  ↓
Prototype Change
  ↓
Validation
  ↓
Version
  ↓
Git Commit

This allows the final research artifact to explain why major interface decisions were made.

---

7. Experimental Change Rule

If a proposed design change could alter participant behaviour, it must be reviewed as a potential experimental change.

Examples include:

- changing explanation wording;
- changing explanation timing;
- changing the amount of information;
- changing scenario severity;
- changing vehicle response;
- changing measurement timing;
- adding additional explanatory information.

These should not be treated as ordinary cosmetic changes.

---

8. Current Version Status

Current prototype: v0.2
Prototype type: Low-fidelity experimental prototype
Scenario: SCN-01 — Pedestrian Crossing
Conditions: A / B / C

Structural flow: [Validated / Pending]
Condition isolation: [Validated / Pending]
Measurement flow: [Validated / Pending]
Accessibility: [Reviewed / Pending]
Repeatability: [Validated / Pending]

---

9. Next Version

The next major prototype milestone is:

v1.0 — High-Fidelity Experimental Prototype

Before v1.0 begins, the low-fidelity experimental architecture should be sufficiently stable that visual refinement does not require redesigning the experimental logic.
