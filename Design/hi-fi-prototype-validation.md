High-Fidelity Prototype Validation

1. Purpose

This document defines the validation process for the integrated high-fidelity experimental prototype.

The purpose of validation is to determine whether the prototype is sufficiently coherent, repeatable, accessible, and experimentally controlled to proceed toward pilot testing.

This validation does not establish the effectiveness of any explanation condition.

No participant findings are claimed at this stage.

---

2. Prototype Under Validation

The prototype contains the following experimental sequence:

EXP-00 Start
→ EXP-01 Practice
→ EXP-02 Normal Journey
→ EXP-03 Event Approach
→ EXP-04 Unexpected Event
→ EXP-05 Autonomous Response
→ EXP-05A / EXP-05B / EXP-05C Explanation
→ EXP-06 Comprehension
→ EXP-07 Trust / Experience
→ EXP-08 Workload
→ EXP-09 Trial Complete

The three explanation conditions are:

Condition| Explanation
A| No explanation
B| Minimal explanation
C| Contextual explanation

---

3. Validation Objectives

Validation focuses on six areas:

1. Functional correctness
2. Experimental integrity
3. Interaction consistency
4. Human Factors quality
5. Accessibility
6. Visual and content consistency

---

4. Validation Principle

The central validation question is:

«Can a participant complete the experimental task without encountering interaction problems that could meaningfully interfere with the intended manipulation or measurements?»

The prototype should therefore be evaluated as an experimental instrument, not merely as a visual design.

---

5. Validation Pass 1 — Functional

Check every transition in the complete prototype.

Start

- [ ] Start interaction works.
- [ ] Participant can enter the practice trial.
- [ ] No unexpected navigation occurs.

Practice

- [ ] Practice instructions are understandable.
- [ ] Practice interaction can be completed.
- [ ] Practice does not expose experimental condition information.

Journey

- [ ] Normal journey state loads correctly.
- [ ] Event approach state follows the intended sequence.
- [ ] Unexpected event appears at the intended point.
- [ ] Autonomous response follows the predefined scenario.

Explanation

- [ ] Condition A displays no explanation.
- [ ] Condition B displays the minimal explanation.
- [ ] Condition C displays the contextual explanation.
- [ ] Explanation content is correct.
- [ ] Explanation branch does not alter the underlying vehicle response.

Measurement

- [ ] Comprehension screen works.
- [ ] Trust/experience screen works.
- [ ] Workload screen works.
- [ ] Trial completion works.

---

6. Validation Pass 2 — Experimental Integrity

The following variables must remain controlled:

Scenario
Vehicle behaviour
Event timing
Response timing
Measurement sequence
Question wording
Measurement scale
Interaction structure

The intended manipulation is:

Explanation condition

Any other systematic difference between conditions must be treated as a potential confound.

---

7. Condition Equivalence Check

For each scenario, compare:

Condition A
Condition B
Condition C

Verify that:

- [ ] Same scenario
- [ ] Same environmental event
- [ ] Same vehicle response
- [ ] Same response timing
- [ ] Same observation opportunity
- [ ] Same comprehension question
- [ ] Same trust/experience measurement
- [ ] Same workload measurement
- [ ] Same completion flow

Only the explanation presentation should differ.

---

8. Validation Pass 3 — Human Factors

Review the prototype from the passenger's perspective.

Situation Awareness

Check whether the interface makes it possible to determine:

- What is happening?
- What is the vehicle doing?
- Why is the vehicle responding?
- What should the passenger understand from the event?

The design should support situation understanding without unnecessarily increasing information density.

---

Cognitive Workload

Check for:

- excessive text;
- competing visual elements;
- unnecessary animation;
- ambiguous controls;
- excessive notifications;
- repeated information;
- complex navigation;
- unnecessary decision points.

The explanation should provide useful information without becoming a new source of cognitive burden.

---

Trust Calibration

Check that the interface:

- explains relevant vehicle behaviour;
- avoids exaggerated reassurance;
- avoids implying perfect system reliability;
- avoids unnecessary alarm;
- communicates uncertainty appropriately where applicable.

The design goal is calibrated trust, not maximum trust.

---

Event Salience

Check whether the passenger can notice:

Unexpected event
        ↓
Vehicle response
        ↓
Explanation

The event should be noticeable without creating unnecessary alarm.

---

9. Validation Pass 4 — Accessibility

Review:

Visual

- [ ] Text remains readable.
- [ ] Contrast is sufficient.
- [ ] Important information is not conveyed through colour alone.
- [ ] Icons have understandable meaning.
- [ ] Hierarchy is visually clear.

Interaction

- [ ] Interactive targets are sufficiently large.
- [ ] Selected states are obvious.
- [ ] Disabled states are distinguishable.
- [ ] Controls behave consistently.

Cognitive Accessibility

- [ ] Instructions are concise.
- [ ] Questions are unambiguous.
- [ ] Terminology is consistent.
- [ ] No unnecessary technical language is introduced.

---

10. Validation Pass 5 — Visual Consistency

Check consistency across:

- typography;
- spacing;
- buttons;
- cards;
- icons;
- semantic states;
- explanation components;
- measurement components;
- navigation;
- light/dark themes where implemented.

No individual screen should appear visually disconnected from the rest of the system.

---

11. Validation Pass 6 — Content

Review all participant-facing text.

Check:

- [ ] No spelling errors.
- [ ] No unexplained abbreviations.
- [ ] No placeholder text.
- [ ] No design notes visible to participants.
- [ ] No accidental developer instructions.
- [ ] No condition labels visible to participants.
- [ ] No hypothesis-revealing language.
- [ ] No unsupported safety claims.

---

12. Severity Classification

Issues should be classified as:

P0 — Critical

Prevents the experimental trial from being completed or compromises experimental validity.

Examples:

- wrong condition displayed;
- wrong vehicle response;
- measurement branch inaccessible;
- participant cannot continue.

P1 — Major

Significantly interferes with interaction or interpretation.

Examples:

- explanation is unreadable;
- important event information is obscured;
- incorrect measurement behaviour.

P2 — Moderate

Noticeable problem that does not prevent completion.

Examples:

- confusing secondary control;
- inconsistent hierarchy;
- moderate visual ambiguity.

P3 — Minor

Low-impact issue.

Examples:

- spacing inconsistency;
- minor typography issue;
- small visual alignment problem.

---

13. Issue Log

Use the following structure:

ID| Screen| Category| Severity| Description| Effect| Resolution| Status
HF-001| —| —| —| —| —| —| Open

Categories:

Functional
Experimental
Human Factors
Accessibility
Visual
Content
Interaction
Timing

---

14. Validation Record

Record each validation pass.

Prototype version:
Figma version:
Date:
Validator:
Scenario:
Condition:
Validation pass:
Issues identified:
Issues resolved:
Issues remaining:

---

15. Repeatability Test

Run the same scenario multiple times.

Verify that:

- event sequence remains consistent;
- vehicle response remains consistent;
- explanation condition remains correct;
- measurement sequence remains consistent;
- no state becomes corrupted between trials.

The prototype should not depend on accidental interaction history from a previous trial.

---

16. Validation Boundaries

This validation cannot establish:

- participant comprehension;
- trust effects;
- workload effects;
- statistical significance;
- explanation-condition superiority;
- real-world passenger safety;
- production readiness.

Those questions require appropriate empirical evaluation.

---

17. Exit Criteria

The prototype can proceed toward pilot preparation when:

- [ ] No P0 issues remain.
- [ ] P1 issues are resolved or explicitly justified.
- [ ] Experimental condition integrity has been verified.
- [ ] Complete participant flow has been traversed.
- [ ] All measurement screens work.
- [ ] Accessibility review is complete.
- [ ] Participant-facing content has been reviewed.
- [ ] Repeatability has been checked.
- [ ] Remaining issues are documented.

---

18. Definition of Done

High-fidelity prototype validation is complete when the prototype can be run end-to-end with no unresolved issue that threatens experimental integrity or prevents completion of the intended participant task.
