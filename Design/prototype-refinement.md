Experimental Prototype Refinement

1. Purpose

This document records the refinement process applied after internal validation of the low-fidelity experimental prototype.

The objective is to correct structural, interaction, accessibility, and experimental-integrity issues without unintentionally changing the research design.

The refinement process follows a strict principle:

«Improve the prototype without changing the experimental manipulation.»

The three explanation conditions remain:

- Condition A — No Explanation
- Condition B — Minimal Explanation
- Condition C — Contextual Explanation

---

2. Refinement Principles

All prototype changes should be evaluated against five principles.

2.1 Experimental Integrity

A design change must not unintentionally alter the independent variable.

The explanation condition remains the primary manipulated factor.

---

2.2 Scenario Consistency

The underlying autonomous-vehicle event must remain equivalent across explanation conditions.

The following should remain unchanged:

- environmental event;
- vehicle response;
- scenario sequence;
- measurement sequence;
- participant task;
- general timing structure.

---

2.3 Interaction Simplicity

The participant should not need to perform unnecessary actions.

The interface should communicate the vehicle's state without introducing interaction that is unrelated to the research question.

---

2.4 Measurement Separation

Experimental interaction and measurement interaction should remain conceptually separate.

The participant should first experience the autonomous behaviour and explanation condition before answering the relevant comprehension and experience measures.

---

2.5 Traceability

Every substantive change should be recorded.

The project should make it possible to determine:

Original prototype
        ↓
Validation finding
        ↓
Design decision
        ↓
Prototype revision
        ↓
Revalidation

---

3. Refinement Workflow

The refinement process follows:

Validation Finding
        ↓
Classify Issue
        ↓
Assess Experimental Impact
        ↓
Determine Required Change
        ↓
Implement Change
        ↓
Re-run Relevant Validation
        ↓
Record Result

A visual issue should not automatically result in a redesign.

The smallest change that resolves the problem should be preferred when experimental integrity is unaffected.

---

4. Issue Assessment

Each issue should be assessed using the following questions.

Question 1

Does the issue prevent the participant from completing the intended task?

Question 2

Does the issue affect the explanation manipulation?

Question 3

Does the issue change the timing of the experimental event?

Question 4

Does the issue affect comprehension measurement?

Question 5

Does the issue affect trust or workload measurement?

Question 6

Does the issue introduce information that is not intended to be available in a particular condition?

Question 7

Can the issue be corrected without changing the research question?

---

5. Experimental Integrity Rules

The following rules are frozen for the current experimental prototype.

Rule 1 — Same Vehicle Behaviour

The autonomous vehicle must perform the same predefined response across explanation conditions.

SCN-01
Pedestrian enters crossing
        ↓
Vehicle slows

The explanation condition does not determine whether the vehicle slows.

---

Rule 2 — Same Environmental Event

The pedestrian-crossing event must remain equivalent across conditions.

No condition should receive a more severe or less severe event.

---

Rule 3 — Explanation Is the Manipulation

The primary difference between conditions is the explanation presented to the passenger.

A = no explanation
B = minimal explanation
C = contextual explanation

---

Rule 4 — No Hidden Explanations

Condition A must not contain explanatory information through:

- secondary text;
- labels;
- icons that explicitly reveal the reason;
- button wording;
- notifications;
- unrelated interface elements.

---

Rule 5 — No Measurement Leakage

Questions must not reveal the intended answer.

For example, a comprehension question should not contain wording that directly repeats the explanation.

---

Rule 6 — No Visual Bias

The explanation conditions should not receive systematically different visual emphasis unrelated to the explanation manipulation.

Differences in visual presentation should correspond only to the intended explanation content.

---

6. Low-Fidelity Refinement Targets

6.1 Start Screen

The start screen should:

- clearly identify the beginning of the trial;
- avoid revealing the experimental hypothesis;
- provide concise instructions;
- provide a clear start action.

---

6.2 Practice Screen

The practice screen should:

- introduce the general interaction pattern;
- distinguish practice from the experimental trial;
- avoid revealing the experimental explanation conditions.

---

6.3 Normal Journey

The normal journey state should establish the baseline travel context.

It should not contain unnecessary information that could distract from the later event.

---

6.4 Event Approach

The event-approach state should establish temporal progression toward the unexpected event.

It should not reveal the explanation condition before the autonomous response occurs.

---

6.5 Unexpected Event

The unexpected-event state should communicate that an environmental event has occurred.

The event should remain consistent across conditions.

---

6.6 Autonomous Response

The autonomous-response state should communicate the vehicle's behaviour.

The response should remain independent of the explanation condition.

---

7. Explanation Component Refinement

The explanation component is the primary experimental manipulation.

Condition A — No Explanation

The interface does not provide explicit explanatory text.

The autonomous response remains visible.

---

Condition B — Minimal Explanation

The explanation communicates the immediate reason for the vehicle response.

Example:

«Slowing for pedestrian.»

The wording should remain concise.

---

Condition C — Contextual Explanation

The explanation provides additional contextual information describing the environmental event and the reason for the vehicle response.

Example:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

The contextual condition should contain more explanatory information than the minimal condition without introducing unrelated information.

---

8. Comprehension Screen Refinement

The comprehension screen should measure whether the participant understood the autonomous vehicle's behaviour.

The question should be:

- concise;
- neutral;
- presented after the explanation;
- identical across explanation conditions where possible;
- free from wording that suggests the correct answer.

The answer options should be mutually understandable and should not contain obvious formatting cues.

---

9. Trust / Experience Screen Refinement

The trust/experience measurement should use a consistent response structure across conditions.

The prototype should not visually suggest that one response is preferred.

The measurement interface should avoid persuasive or emotionally loaded language.

---

10. Workload Screen Refinement

The workload measurement should appear after the relevant interaction sequence.

The participant should understand:

- what is being rated;
- how the response scale works;
- that there is no correct answer.

The workload screen should remain visually consistent across conditions.

---

11. Accessibility Refinement

The following principles should be preserved:

- information should not rely on colour alone;
- controls should have clear labels;
- text should remain readable;
- interaction targets should be sufficiently clear;
- hierarchy should be understandable without decorative elements;
- unnecessary animation should be avoided;
- the interface should not depend on rapid visual interpretation unless required by the research design.

These are design requirements, not evidence that accessibility has been empirically validated.

---

12. Change Documentation

Each implemented change should be recorded using the following format.

Change ID| Issue ID| Original Behaviour| Revised Behaviour| Experimental Impact| Status
REF-001| [UX/CI/ST ID]| [Original]| [Revised]| None / Low / Medium / High| Implemented
REF-002| [UX/CI/ST ID]| [Original]| [Revised]| None / Low / Medium / High| Implemented
REF-003| [UX/CI/ST ID]| [Original]| [Revised]| None / Low / Medium / High| Implemented

---

13. Revalidation Requirement

After refinement, the affected prototype flow must be tested again.

A change is not considered complete simply because the Figma frame has been modified.

The relevant behaviour must be checked again.

Revalidation Checklist

- [ ] Start flow works.
- [ ] Practice flow works.
- [ ] Normal journey works.
- [ ] Unexpected event occurs correctly.
- [ ] Autonomous response is consistent.
- [ ] Condition A is isolated.
- [ ] Condition B is isolated.
- [ ] Condition C is isolated.
- [ ] Comprehension follows explanation.
- [ ] Trust/experience measurement follows the trial experience.
- [ ] Workload measurement occurs at the intended point.
- [ ] Trial completion works.
- [ ] Prototype can be restarted.
- [ ] No experimental-blocking issues remain.

---

14. Prototype Version

The refined prototype should be saved as:

Experimental Prototype v0.2

The previous prototype should remain identifiable as:

Experimental Prototype v0.1

The older version should not be silently overwritten if version history is being maintained outside Figma.

---

15. Completion Criteria

Prototype refinement is complete when:

- all P0 issues have been resolved;
- P1 issues affecting experimental execution have been resolved;
- explanation conditions remain isolated;
- scenario consistency has been preserved;
- measurement flow remains intact;
- the complete trial can be executed repeatedly;
- changes are documented;
- the revised prototype has been revalidated.

---

16. Boundary Before High-Fidelity Design

After v0.2 is validated, high-fidelity design may begin.

High-fidelity work should improve:

- visual hierarchy;
- typography;
- spacing;
- component consistency;
- semantic colour;
- dashboard structure;
- explanation-card presentation;
- accessibility;
- visual communication of vehicle state.

High-fidelity work should not change:

- the research question;
- the explanation manipulation;
- scenario difficulty;
- vehicle behaviour;
- measurement sequence;
- participant task;
- condition definitions.

If such a change becomes necessary, it must be treated as an experimental-design decision rather than an ordinary visual-design change.
