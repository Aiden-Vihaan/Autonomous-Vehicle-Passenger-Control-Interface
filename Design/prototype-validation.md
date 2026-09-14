Experimental Prototype Validation

1. Purpose

This document defines the validation process for the first runnable low-fidelity experimental prototype of the Autonomous Vehicle Passenger Control Interface.

The purpose of this validation is to determine whether the prototype correctly implements the experimental structure before high-fidelity visual design begins.

The validation focuses on:

- experimental condition integrity;
- scenario consistency;
- state transitions;
- explanation-condition isolation;
- participant task flow;
- measurement flow;
- interaction clarity;
- accessibility;
- prevention of accidental condition contamination;
- reproducibility of the experimental procedure.

This is a prototype validation activity, not a participant study.

No conclusions about trust, comprehension, workload, situation awareness, or passenger behaviour should be drawn from this validation alone.

---

2. Prototype Under Validation

The prototype currently represents one experimental scenario:

SCN-01 — Pedestrian Crossing

The prototype contains the following major states:

EXP-00 Start
    ↓
EXP-01 Practice
    ↓
EXP-02 Normal Journey
    ↓
EXP-03 Event Approach
    ↓
EXP-04 Unexpected Event
    ↓
EXP-05 Autonomous Response
    ↓
EXP-05A / EXP-05B / EXP-05C
Explanation Condition
    ↓
EXP-06 Comprehension
    ↓
EXP-07 Trust / Experience
    ↓
EXP-08 Workload
    ↓
EXP-09 Trial Complete

The three explanation conditions are:

Condition A — No Explanation

The autonomous vehicle performs the predefined response without presenting an explanatory message.

Condition B — Minimal Explanation

The interface presents a concise explanation describing the immediate reason for the vehicle's behaviour.

Example:

«Slowing for pedestrian.»

Condition C — Contextual Explanation

The interface presents a more contextual explanation describing the environmental event and the reason for the vehicle's response.

Example:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

These examples are prototype content only. They do not represent empirical findings or validated wording.

---

3. Validation Objectives

The prototype will be considered structurally valid when the following objectives are satisfied.

Objective 1 — State Integrity

Every required experimental state can be reached through the intended interaction path.

Objective 2 — Condition Integrity

The three explanation conditions remain distinct and do not accidentally expose information belonging to another condition.

Objective 3 — Scenario Integrity

The environmental event and autonomous response remain equivalent across explanation conditions.

Only the explanation presentation should differ between conditions.

Objective 4 — Measurement Integrity

The participant reaches the required comprehension, trust/experience, and workload measures after the appropriate experimental event.

Objective 5 — Interaction Integrity

The prototype does not contain broken links, unintended loops, inaccessible controls, or dead-end states.

Objective 6 — Experimental Reproducibility

The same scenario can be executed repeatedly using the same sequence and timing logic.

Objective 7 — Accessibility

The low-fidelity prototype provides a reasonable basis for later accessibility refinement without relying on colour alone or unnecessarily complex interaction patterns.

---

4. Validation Method

Validation will be conducted as a structured walkthrough of the prototype.

The prototype should be tested from the perspective of a participant rather than only from the perspective of the designer.

The evaluator should complete the entire flow without modifying the prototype during the first pass.

A second pass should specifically inspect experimental condition integrity.

A third pass should inspect accessibility and interaction clarity.

Validation Passes

Pass| Purpose
Pass 1| Complete participant journey
Pass 2| Verify experimental conditions
Pass 3| Verify interaction and accessibility
Pass 4| Verify repeatability

---

5. Pass 1 — Complete Participant Journey

The evaluator should begin at "EXP-00 Start".

Step 1 — Start

Verify that:

- the purpose of the prototype is understandable;
- the participant can identify how to begin;
- no experimental condition is revealed prematurely;
- instructions do not bias the participant toward a preferred explanation condition.

Step 2 — Practice

Verify that:

- the practice trial is clearly distinguished from the experimental trial;
- practice does not expose the experimental hypothesis;
- the participant understands the expected interaction pattern;
- the participant can complete the practice flow without assistance.

Step 3 — Normal Journey

Verify that:

- the journey begins in a normal state;
- the interface communicates the current journey status;
- no unexpected event appears prematurely.

Step 4 — Event Approach

Verify that:

- the prototype transitions into the event state correctly;
- the event occurs at the intended point in the sequence;
- the participant is not required to perform an unnecessary action to trigger the event.

Step 5 — Unexpected Event

Verify that:

- the pedestrian-crossing event is clearly represented;
- the event is consistent across conditions;
- the interface does not reveal the explanation condition through unrelated visual differences.

Step 6 — Autonomous Response

Verify that:

- the vehicle response is clearly communicated;
- the response is identical across explanation conditions;
- the response occurs before the explanation content.

Step 7 — Explanation

Verify that the correct explanation condition appears.

Condition A:

No explanation content.

Condition B:

Minimal explanation.

Condition C:

Contextual explanation.

Step 8 — Comprehension

Verify that:

- the participant can answer the required comprehension question;
- the question appears after the relevant event and explanation;
- the question does not explicitly reveal the correct answer through wording or layout.

Step 9 — Trust / Experience

Verify that:

- the required trust/experience measure is presented;
- the response scale is consistent;
- the participant can select exactly the intended response.

Step 10 — Workload

Verify that:

- the workload measure is presented after the required trial events;
- the participant understands how to provide a response;
- the interface does not accidentally skip or duplicate the workload measurement.

Step 11 — Completion

Verify that:

- the trial ends clearly;
- no unintended navigation back into the trial occurs;
- completion can be recorded consistently.

---

6. Pass 2 — Experimental Condition Validation

The most important validation requirement is that the explanation manipulation remains isolated.

The following elements must remain constant across Conditions A, B, and C:

- scenario;
- environmental event;
- vehicle response;
- journey context;
- event sequence;
- measurement questions;
- measurement scales;
- interaction structure;
- approximate presentation timing.

The intended experimental difference is:

Explanation presentation

Condition A

Expected:

Autonomous response
        ↓
No explanation
        ↓
Comprehension

Condition B

Expected:

Autonomous response
        ↓
Minimal explanation
        ↓
Comprehension

Condition C

Expected:

Autonomous response
        ↓
Contextual explanation
        ↓
Comprehension

Condition Contamination Checklist

- [ ] Condition A contains no explanation text.
- [ ] Condition A does not contain hidden explanatory information.
- [ ] Condition B contains only the predefined minimal explanation.
- [ ] Condition C contains only the predefined contextual explanation.
- [ ] The vehicle response is unchanged across conditions.
- [ ] The environmental event is unchanged across conditions.
- [ ] Measurement questions are unchanged across conditions.
- [ ] Visual hierarchy does not unintentionally communicate a condition.
- [ ] Button labels do not reveal the expected experimental outcome.
- [ ] Condition-specific content is not visible before the relevant event.
- [ ] No condition automatically reveals another condition's content.

---

7. Pass 3 — Interaction and Accessibility Validation

Interaction Validation

Check:

- [ ] Every primary button is clickable.
- [ ] Every button leads to the intended frame.
- [ ] There are no dead-end screens.
- [ ] There are no unintended loops.
- [ ] Back navigation does not bypass required measurements.
- [ ] A participant cannot accidentally skip the experimental event.
- [ ] A participant cannot accidentally return to a previous condition.
- [ ] The trial cannot be completed without the required measurements.
- [ ] The prototype can be restarted for another trial.

Accessibility Validation

Check:

- [ ] Important information is not communicated by colour alone.
- [ ] Text is readable at the intended prototype scale.
- [ ] Important controls have clear labels.
- [ ] Interactive elements have sufficiently large targets for the intended interface.
- [ ] Information hierarchy remains understandable without visual decoration.
- [ ] Explanation text is concise enough to support rapid comprehension.
- [ ] The interface avoids unnecessary animation in the experimental flow.
- [ ] Audio is not required unless audio is explicitly part of the experimental condition.
- [ ] Accessibility assumptions are documented rather than treated as validated findings.

---

8. Pass 4 — Repeatability Validation

The same SCN-01 trial should be executed multiple times.

The evaluator should verify that:

1. the same starting state is produced;
2. the same event occurs;
3. the same autonomous response occurs;
4. the correct explanation condition appears;
5. the same measurement sequence occurs;
6. the trial can be completed without manual correction.

Repeatability Checklist

- [ ] Trial 1 completed successfully.
- [ ] Trial 2 completed successfully.
- [ ] Trial 3 completed successfully.
- [ ] No state changed unexpectedly between trials.
- [ ] No condition-specific content leaked between trials.
- [ ] Restarting the prototype returns it to the intended initial state.

---

9. Validation Severity Levels

Prototype issues will be classified using four levels.

P0 — Experimental Blocking

The issue prevents the experiment from being executed correctly.

Examples:

- explanation condition cannot be isolated;
- participant cannot reach the comprehension measure;
- vehicle response differs between conditions;
- prototype enters the wrong experimental branch.

P1 — Major

The issue does not completely prevent execution but can substantially affect participant interaction or experimental consistency.

Examples:

- important information is ambiguous;
- a required control is difficult to identify;
- a transition behaves inconsistently.

P2 — Moderate

The issue affects usability or clarity but does not fundamentally compromise the experimental structure.

Examples:

- unclear button wording;
- unnecessary interaction;
- inconsistent spacing.

P3 — Minor

A cosmetic or low-impact issue that can be addressed during later refinement.

Examples:

- alignment;
- typography adjustment;
- minor visual inconsistency.

---

10. Validation Acceptance Criteria

The low-fidelity prototype may proceed toward higher-fidelity design when:

Experimental Integrity

- all three explanation conditions are structurally isolated;
- the same scenario and autonomous response are maintained across conditions;
- no experimental-blocking contamination is present.

Flow Integrity

- the complete participant flow can be executed from start to completion;
- all required states are reachable;
- no required state is accidentally bypassed.

Measurement Integrity

- comprehension measurement occurs after the explanation condition;
- trust/experience measurement occurs after the relevant trial experience;
- workload measurement occurs at the defined point;
- measurement screens remain consistent across conditions.

Interaction Integrity

- no P0 issues remain;
- no unresolved P1 issue threatens the experimental procedure.

Reproducibility

- the trial can be restarted;
- the same flow can be repeated;
- the prototype behaves consistently across repeated walkthroughs.

---

11. Validation Limitations

This validation does not establish:

- usability with real participants;
- trust effects;
- comprehension effects;
- cognitive workload effects;
- situation-awareness effects;
- statistical significance;
- ecological validity;
- safety validation;
- production readiness.

It only establishes whether the prototype is sufficiently coherent to proceed toward controlled pilot testing.

---

12. Validation Record

Prototype version: v0.1
Scenario: SCN-01 — Pedestrian Crossing
Conditions: A / B / C
Validation type: Internal structured walkthrough
Participant study: Not conducted
Validation date: [YYYY-MM-DD]

Result

Overall status: [PASS / PASS WITH ISSUES / BLOCKED]

P0 issues: [0]
P1 issues: [number]
P2 issues: [number]
P3 issues: [number]

Decision

[ ] Proceed to high-fidelity refinement
[ ] Fix issues and repeat validation
[ ] Redesign experimental flow

---

13. Next Step

After successful structural validation, the prototype will move into high-fidelity experimental interface development.

The next phase will preserve the validated experimental logic while introducing:

- refined visual hierarchy;
- design-system components;
- typography;
- spacing;
- semantic colour tokens;
- explanation-card styling;
- journey-state visualization;
- accessibility refinement;
- responsive behaviour where required.

The experimental logic should not be changed merely for visual reasons.

Any change that affects the experimental manipulation, scenario timing, participant task, measurement sequence, or condition isolation should be documented as an experimental-design decision.
