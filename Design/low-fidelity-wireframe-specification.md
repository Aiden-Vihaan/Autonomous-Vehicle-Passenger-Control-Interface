Low-Fidelity Wireframe Specification

Project

Autonomous Vehicle Passenger Control Interface

Day

Day 15 — Low-Fidelity Experimental Prototype

---

1. Purpose

This document translates the experimental information architecture into a low-fidelity wireframe specification.

The objective is to establish the structural layout, information hierarchy, interaction points, and experimental condition boundaries before high-fidelity visual design begins.

The wireframes are not intended to represent the final visual design.

At this stage, the prototype must prioritize:

- experimental control
- information hierarchy
- consistent interaction
- clear state transitions
- measurement integrity
- accessibility
- reproducibility

---

2. Prototype Scope

The experimental prototype contains the following primary states:

EXP-00 — Start
EXP-01 — Practice Trial
EXP-02 — Normal Journey
EXP-03 — Unexpected Event
EXP-04 — Autonomous Response
EXP-05-A — No Explanation
EXP-05-B — Minimal Explanation
EXP-05-C — Contextual Explanation
EXP-06 — Comprehension
EXP-07 — Trust / Experience
EXP-08 — Workload
EXP-09 — Trial Complete

---

3. Global Wireframe Structure

The primary prototype is designed for the in-cabin passenger display.

The general layout should follow:

┌─────────────────────────────────────────────────────┐
│ SYSTEM / JOURNEY STATUS                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│                                                     │
│              PRIMARY JOURNEY CONTENT                │
│                                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│ SECONDARY STATUS / CONTROL INFORMATION              │
└─────────────────────────────────────────────────────┘

The exact visual treatment will be determined during high-fidelity design.

---

4. EXP-00 — Start

Purpose

Introduce the experimental interface and allow the participant to begin.

Wireframe

┌─────────────────────────────────────────────────────┐
│ Autonomous Vehicle Passenger Interface              │
│                                                     │
│                                                     │
│              Study Introduction                     │
│                                                     │
│              [ Begin ]                              │
│                                                     │
└─────────────────────────────────────────────────────┘

Required Elements

- project/interface title
- participant instructions
- begin control

Interaction

BEGIN
  ↓
EXP-01

---

5. EXP-01 — Practice Trial

Purpose

Allow the participant to understand the basic interaction and measurement procedure.

Wireframe

┌─────────────────────────────────────────────────────┐
│ Practice Trial                                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│ This practice journey will show you how the         │
│ interface works.                                    │
│                                                     │
│ Follow the instructions presented on screen.        │
│                                                     │
│                 [ Start Practice ]                  │
│                                                     │
└─────────────────────────────────────────────────────┘

The practice trial must be clearly distinguishable from experimental trials.

---

6. EXP-02 — Normal Journey

Purpose

Establish the baseline journey state.

Wireframe

┌─────────────────────────────────────────────────────┐
│ ● Journey active                         ETA 18 min │
├─────────────────────────────────────────────────────┤
│                                                     │
│                  JOURNEY AREA                       │
│                                                     │
│              Destination: Airport                  │
│                                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│ Vehicle status: Autonomous                          │
│                                                     │
│ [ Safety ]                              [ Help ]    │
└─────────────────────────────────────────────────────┘

Requirements

The interface should remain stable during normal journey conditions.

No experimental explanation should be visible.

---

7. EXP-03 — Unexpected Event

Purpose

Represent the environmental event detected by the autonomous vehicle.

Example

Pedestrian crossing scenario.

Wireframe

┌─────────────────────────────────────────────────────┐
│ ● Journey active                                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│                EVENT DETECTED                      │
│                                                     │
│              Pedestrian ahead                       │
│                                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│ Vehicle responding to road conditions               │
└─────────────────────────────────────────────────────┘

The event should be visually salient without creating unnecessary alarm.

---

8. EXP-04 — Autonomous Response

Purpose

Communicate what the vehicle is doing.

Wireframe

┌─────────────────────────────────────────────────────┐
│ ● Vehicle response                                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│                 VEHICLE SLOWING                     │
│                                                     │
│                                                     │
│              [Response indicator]                   │
│                                                     │
├─────────────────────────────────────────────────────┤
│ Autonomous response active                          │
└─────────────────────────────────────────────────────┘

The vehicle action must be identical across explanation conditions.

---

9. EXP-05-A — No Explanation

Purpose

Create the baseline explanation condition.

Wireframe

┌─────────────────────────────────────────────────────┐
│ ● Vehicle response                                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│                 VEHICLE SLOWING                     │
│                                                     │
│                                                     │
│              [Response indicator]                   │
│                                                     │
├─────────────────────────────────────────────────────┤
│ Autonomous response active                          │
└─────────────────────────────────────────────────────┘

No additional explanation card is presented.

---

10. EXP-05-B — Minimal Explanation

Purpose

Present a concise explanation of the vehicle action.

Wireframe

┌─────────────────────────────────────────────────────┐
│ ● Vehicle response                                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│                 VEHICLE SLOWING                     │
│                                                     │
│          ┌───────────────────────────────┐          │
│          │ Slowing for pedestrian.      │          │
│          └───────────────────────────────┘          │
│                                                     │
├─────────────────────────────────────────────────────┤
│ Autonomous response active                          │
└─────────────────────────────────────────────────────┘

The explanation should remain concise.

---

11. EXP-05-C — Contextual Explanation

Purpose

Present a more detailed explanation containing event context and response rationale.

Wireframe

┌─────────────────────────────────────────────────────┐
│ ● Vehicle response                                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│                 VEHICLE SLOWING                     │
│                                                     │
│       ┌───────────────────────────────────┐         │
│       │ Pedestrian entering the crossing  │         │
│       │ ahead.                            │         │
│       │                                   │         │
│       │ Slowing to maintain a safe        │         │
│       │ distance.                         │         │
│       └───────────────────────────────────┘         │
│                                                     │
├─────────────────────────────────────────────────────┤
│ Autonomous response active                          │
└─────────────────────────────────────────────────────┘

The contextual condition should contain more information than the minimal condition while avoiding unnecessary information.

---

12. Explanation Component Rules

The explanation card must be implemented as one reusable component with variants.

Explanation Card
├── None
├── Minimal
└── Contextual

The following properties should remain consistent:

- position
- container structure
- typography hierarchy
- interaction behaviour
- visual prominence

The principal difference should be the information presented.

---

13. EXP-06 — Comprehension

Purpose

Measure whether the participant understood the autonomous vehicle's behaviour.

Wireframe

┌─────────────────────────────────────────────────────┐
│ Understanding Check                                │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Why did the vehicle slow down?                     │
│                                                     │
│ ○ The vehicle detected a pedestrian.               │
│                                                     │
│ ○ The vehicle was approaching its destination.     │
│                                                     │
│ ○ The vehicle encountered a system failure.        │
│                                                     │
│ ○ I do not know.                                   │
│                                                     │
│                  [ Continue ]                       │
└─────────────────────────────────────────────────────┘

Question wording must remain identical across experimental conditions.

---

14. EXP-07 — Trust / Experience

Purpose

Collect post-event subjective measures.

Wireframe

┌─────────────────────────────────────────────────────┐
│ Experience Rating                                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│ How much did you trust the vehicle's response?      │
│                                                     │
│ 1        2        3        4        5        6      │
│ ○        ○        ○        ○        ○        ○      │
│                                                     │
│ How well did you understand why it responded?      │
│                                                     │
│ 1        2        3        4        5        6      │
│ ○        ○        ○        ○        ○        ○      │
│                                                     │
│                  [ Continue ]                       │
└─────────────────────────────────────────────────────┘

The final scale and wording must follow the finalized measurement protocol.

The wireframe does not establish the final validated measurement instrument.

---

15. EXP-08 — Workload

Purpose

Collect the selected workload measure after the required experimental exposure.

Wireframe

┌─────────────────────────────────────────────────────┐
│ Workload                                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Please rate the workload you experienced during     │
│ the previous journey event.                         │
│                                                     │
│              [ Workload Measure ]                   │
│                                                     │
│                  [ Continue ]                       │
└─────────────────────────────────────────────────────┘

The exact instrument and implementation will be finalized before participant testing.

---

16. EXP-09 — Trial Complete

Purpose

Clearly terminate the current trial and transition to the next scenario.

Wireframe

┌─────────────────────────────────────────────────────┐
│ Trial Complete                                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│          This trial has been completed.             │
│                                                     │
│                                                     │
│                 [ Next Trial ]                      │
│                                                     │
└─────────────────────────────────────────────────────┘

---

17. Interaction Rules

The prototype should use a consistent interaction model.

Primary action:
Continue / Next

Secondary actions:
Only where required by the study protocol

Participants should not be required to navigate through unrelated product functions during the experimental task.

---

18. Error Prevention

The prototype should prevent:

- accidental skipping of required measures
- accidental exposure to another explanation condition
- returning to a previous experimental state
- changing the scenario after trial initialization
- changing the explanation condition during a trial

---

19. Condition Isolation

Each experimental trial must load exactly one explanation condition.

Trial
  ↓
Scenario ID
  ↓
Condition ID
  ↓
Vehicle Response
  ↓
Explanation Variant
  ↓
Measurement

The participant should not be able to select or identify the experimental condition manually.

---

20. Low-Fidelity Validation Checklist

Structure

- [ ] Every required state exists.
- [ ] Every state has a defined purpose.
- [ ] Every state has a clear next action.
- [ ] No unnecessary screens are introduced.

Experimental control

- [ ] Vehicle response remains constant.
- [ ] Explanation variants are isolated.
- [ ] Measurement wording is consistent.
- [ ] Condition cannot be changed by the participant.

Interaction

- [ ] Navigation is predictable.
- [ ] Required actions are obvious.
- [ ] No accidental skips are possible.
- [ ] Trial completion is explicit.

Accessibility

- [ ] Information does not depend only on colour.
- [ ] Text hierarchy is clear.
- [ ] Controls have meaningful labels.
- [ ] Content remains readable at the intended display size.

---

21. Design Principle

The low-fidelity prototype should answer one question:

«Can the experimental procedure be executed consistently before visual styling is introduced?»

If the answer is no, the flow should be corrected before proceeding to high-fidelity design.

---

22. Day 15 Completion Criteria

Day 15 is complete when:

- [ ] All experimental states have wireframes.
- [ ] All three explanation conditions are represented.
- [ ] The explanation component has defined variants.
- [ ] Navigation between states is mapped.
- [ ] Measurement screens are structurally defined.
- [ ] Error-prevention rules are documented.
- [ ] Condition isolation is documented.
- [ ] Accessibility requirements are represented.
- [ ] Figma frame naming follows the project convention.

---

23. Next Step

Day 16 will focus on converting the low-fidelity structure into a Figma component and state system.

The next stage will establish:

- reusable components
- component variants
- states
- interaction connections
- scenario variables
- explanation variants
- prototype branching
