High-Fidelity Transition Plan

Purpose

This document defines the transition from the validated low-fidelity experimental prototype to the high-fidelity prototype.

The objective is to increase visual and interaction fidelity while preserving the experimental architecture, explanation conditions, participant tasks, and measurement structure.

---

1. Design Objective

The high-fidelity prototype should represent a credible autonomous-vehicle passenger interface while remaining suitable for controlled Human Factors evaluation.

The design should communicate:

- vehicle state;
- journey progress;
- unexpected events;
- autonomous responses;
- explanations;
- passenger understanding;
- safety-relevant information;
- system status.

The interface should remain calm during normal operation and become appropriately salient during unexpected or safety-relevant events.

---

2. High-Fidelity Design Priorities

Priority 1 — Experimental Integrity

The experimental logic has priority over visual polish.

No visual improvement should introduce an uncontrolled difference between experimental conditions.

Priority 2 — Information Hierarchy

Information should be prioritized according to passenger relevance and urgency.

Priority 3 — Comprehension

Passengers should be able to understand:

- what happened;
- what the vehicle is doing;
- why it is doing it;
- whether they need to act.

Priority 4 — Trust Calibration

The interface should support appropriate trust rather than attempting to maximize trust.

Priority 5 — Accessibility

The interface should remain usable across different visual, cognitive, and interaction needs.

---

3. High-Fidelity Screen Set

The low-fidelity structure will be translated into the following high-fidelity states.

ID| Screen / State| Purpose
EXP-00| Start| Begin experimental session
EXP-01| Practice| Familiarize participant with task
EXP-02| Normal Journey| Establish baseline journey state
EXP-03| Event Approach| Establish transition toward event
EXP-04| Unexpected Event| Present environmental change
EXP-05| Autonomous Response| Show vehicle action
EXP-05A| No Explanation| Experimental Condition A
EXP-05B| Minimal Explanation| Experimental Condition B
EXP-05C| Contextual Explanation| Experimental Condition C
EXP-06| Comprehension| Measure understanding
EXP-07| Trust / Experience| Measure passenger response
EXP-08| Workload| Measure cognitive workload
EXP-09| Trial Complete| End trial

---

4. Visual Design System

The existing product design system should be used as the foundation for high-fidelity implementation.

The experimental prototype should maintain consistency in:

- typography;
- spacing;
- semantic colour use;
- component structure;
- iconography;
- status representation;
- light/dark themes where applicable;
- interaction states.

The visual system must support the research objective rather than introducing unnecessary visual variation.

---

5. Explanation Component

The explanation component is the most research-sensitive visual component.

It should support three controlled variants:

Explanation
├── None
├── Minimal
└── Contextual

Minimal Variant

Information hierarchy:

[Vehicle Action]
[Immediate Reason]

Contextual Variant

Information hierarchy:

[Vehicle Action]
[Environmental Context]
[Reason / Safety Context]

The visual styling should remain as consistent as possible across variants.

The primary difference should be the information presented rather than unrelated visual decoration.

---

6. Unexpected Event Design

Unexpected events should be visually distinguishable from normal journey states without creating unnecessary alarm.

The design should communicate:

1. an event has occurred;
2. the vehicle has detected/responded to it;
3. the passenger can understand the response;
4. whether passenger action is required.

The interface should avoid unnecessary:

- flashing;
- excessive animation;
- dramatic warnings;
- ambiguous colour coding;
- decorative alerts.

---

7. Autonomous Response State

The autonomous response should clearly communicate the vehicle's current action.

Examples include:

- slowing;
- maintaining additional following distance;
- changing trajectory;
- adjusting position;
- preparing for a constrained road segment.

The passenger should not have to infer the primary vehicle action solely from decorative graphics.

---

8. Information Hierarchy

The high-fidelity dashboard should establish a consistent hierarchy:

1. Immediate safety-relevant state
2. Current autonomous action
3. Explanation / reason
4. Journey context
5. Secondary information
6. Optional controls

The hierarchy may change according to urgency, but changes should be intentional and documented.

---

9. Interaction Design

Interactions should be:

- predictable;
- reversible where appropriate;
- clearly labelled;
- consistent across states;
- accessible;
- resistant to accidental activation.

The passenger should not be required to perform unnecessary interactions during safety-relevant events.

---

10. Motion Design

Motion may be used to communicate:

- state transitions;
- vehicle movement;
- route progression;
- changes in system status.

Motion should not:

- obscure explanations;
- delay critical information;
- create unnecessary distraction;
- differ between conditions in a way that could confound the experiment.

If motion differs between experimental conditions, the change must be documented and justified.

---

11. Accessibility Implementation

High-fidelity implementation should include:

- readable text;
- clear contrast;
- adequate touch targets;
- semantic status indicators;
- non-colour-dependent information;
- consistent component placement;
- understandable language;
- predictable interactions.

Accessibility should be treated as part of the Human Factors design rather than a final visual polish step.

---

12. Prototype Build Order

The recommended build sequence is:

Phase 1 — Foundation

- design tokens;
- typography;
- spacing;
- grid;
- colour semantics;
- icons;
- basic components.

Phase 2 — Core Journey

- start;
- practice;
- normal journey;
- event approach.

Phase 3 — Event Interaction

- unexpected event;
- autonomous response;
- explanation component.

Phase 4 — Experimental Conditions

- no explanation;
- minimal explanation;
- contextual explanation.

Phase 5 — Measurement

- comprehension;
- trust/experience;
- workload;
- trial completion.

Phase 6 — Validation

- complete walkthrough;
- condition comparison;
- accessibility review;
- interaction review;
- experimental-integrity review.

---

13. High-Fidelity Validation Questions

Before the prototype is considered complete, verify:

Experimental Integrity

- Does each condition contain the correct explanation?
- Is vehicle behaviour identical across conditions?
- Is the scenario identical across conditions?
- Is the participant task identical?
- Is measurement timing consistent?

Human Factors

- Can the passenger identify the vehicle action?
- Can the passenger identify the event?
- Can the passenger understand the explanation?
- Is important information prioritized?
- Does the interface avoid unnecessary cognitive demand?

Interaction

- Are controls predictable?
- Are states clearly distinguishable?
- Are transitions understandable?
- Are accidental actions prevented?

Accessibility

- Is information understandable without colour alone?
- Is text readable?
- Are touch targets sufficient?
- Is hierarchy clear?
- Is interaction behaviour consistent?

---

14. Change-Control Rule

Every high-fidelity change should be classified as one of:

VISUAL
INTERACTION
CONTENT
EXPERIMENTAL
ACCESSIBILITY

Any change classified as EXPERIMENTAL requires review against the experimental architecture before implementation.

---

15. Definition of Done

The high-fidelity transition is complete when:

- [ ] All required screens have been visually specified.
- [ ] Core components are reusable.
- [ ] Explanation variants are implemented.
- [ ] Experimental conditions remain isolated.
- [ ] Scenario flow remains unchanged.
- [ ] Measurement flow remains unchanged.
- [ ] Accessibility requirements have been addressed.
- [ ] Complete prototype flow is runnable.
- [ ] No unresolved critical experimental-integrity issue remains.
- [ ] Changes are documented.
- [ ] Prototype is ready for high-fidelity validation.

---

16. Next Step

The next stage is the actual high-fidelity visual implementation in Figma.

The objective is not simply to make the prototype attractive.

The objective is to transform the validated experimental structure into a credible passenger HMI while preserving the conditions required for later empirical evaluation.
