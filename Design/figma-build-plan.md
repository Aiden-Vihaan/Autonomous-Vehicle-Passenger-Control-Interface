Figma Build Plan

Project

Autonomous Vehicle Passenger Control Interface

Day

Day 15 — Figma Low-Fidelity Build Plan

---

1. Objective

The purpose of this Figma build is to convert the documented experimental architecture into a reproducible prototype structure.

The Figma file should separate:

1. product design
2. experimental design
3. reusable components
4. scenario states
5. measurement screens

---

2. Figma Pages

Create the following pages:

00 — Cover & Documentation
01 — Design Tokens
02 — Components
03 — Existing Product Screens
04 — Experimental Architecture
05 — Low-Fidelity Prototype
06 — Experimental Conditions
07 — Scenario Flows
08 — Measurement Screens
09 — Accessibility
10 — Prototype Validation

---

3. Low-Fidelity Prototype Frames

Create the following frames first:

EXP-00-Start
EXP-01-Practice
EXP-02-Journey
EXP-03-Event
EXP-04-Response
EXP-05-Explanation-A
EXP-05-Explanation-B
EXP-05-Explanation-C
EXP-06-Comprehension
EXP-07-Trust
EXP-08-Workload
EXP-09-Complete

---

4. Component Inventory

Create structural components for:

Journey Header
Journey Status
Vehicle Status
Event Indicator
Response Indicator
Explanation Card
Question Card
Response Option
Rating Scale
Primary Button
Secondary Button
Progress Indicator
Trial Completion

---

5. Explanation Component

Create one master component:

Explanation Card

With variants:

Condition=None
Condition=Minimal
Condition=Contextual

The component should allow content changes without changing its fundamental placement or interaction behaviour.

---

6. Scenario Component

The scenario should be represented independently from the explanation component.

Conceptual structure:

Scenario
├── Event
├── Vehicle Response
└── Explanation

This prevents the explanation from becoming unintentionally coupled to the vehicle behaviour.

---

7. Prototype Connections

Initial connection map:

EXP-00
 ↓
EXP-01
 ↓
EXP-02
 ↓
EXP-03
 ↓
EXP-04
 ↓
EXP-05-A/B/C
 ↓
EXP-06
 ↓
EXP-07
 ↓
EXP-08
 ↓
EXP-09

The final prototype may use conditional or duplicated flows depending on the capabilities of the chosen prototyping implementation.

---

8. Scenario Flows

Each scenario should follow the same structural sequence:

Normal Journey
      ↓
Event
      ↓
Vehicle Response
      ↓
Explanation
      ↓
Comprehension
      ↓
Trust / Experience
      ↓
Workload
      ↓
Complete

Only scenario-specific content should change.

---

9. Low-Fidelity Design Rules

At this stage:

Do

- use simple boxes
- use placeholder typography
- show information hierarchy
- label components
- document states
- map interactions
- keep conditions visually comparable

Do not

- spend significant time on visual polish
- add decorative animation
- introduce unnecessary interaction
- change the vehicle response between conditions
- introduce unplanned variables
- claim that the prototype represents production software

---

10. Figma Naming Rules

Use:

[TYPE]-[ID]-[DESCRIPTION]

Examples:

EXP-02-Journey
EXP-05-Explanation-Minimal
EXP-06-Comprehension
SCN-01-Pedestrian
SCN-02-Merging

Components:

CMP-ExplanationCard
CMP-QuestionCard
CMP-PrimaryButton

---

11. Prototype Documentation

Each experimental frame should have a small documentation label outside the participant-facing interface.

Example:

FRAME:
EXP-05-B

SCENARIO:
SCN-01

CONDITION:
MINIMAL

PURPOSE:
Explanation exposure

RESEARCH VARIABLE:
Explanation specificity

These labels are for the design/research workspace only and must not appear in the participant-facing prototype.

---

12. Validation Before High Fidelity

Before moving to visual design, verify:

Scenario → Event → Response → Explanation → Measurement

can be completed without ambiguity.

Also verify that:

No Explanation
Minimal Explanation
Contextual Explanation

represent the same underlying event and vehicle response.

---

13. Completion Criteria

The Figma setup is complete when:

- [ ] Pages are created.
- [ ] Frames are named.
- [ ] Low-fidelity layouts are created.
- [ ] Explanation variants are defined.
- [ ] Core components are identified.
- [ ] Scenario flow is represented.
- [ ] Measurement flow is represented.
- [ ] Experimental documentation labels are present.
- [ ] Participant-facing and researcher-facing information are separated.

---

14. Day 16 Dependency

Day 16 should not begin high-fidelity visual styling immediately.

First establish the reusable component/state system.

This will reduce inconsistencies when the same experimental condition must be reproduced across multiple scenarios.
