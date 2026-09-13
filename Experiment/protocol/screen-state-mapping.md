Screen and State Mapping

1. Purpose

This document maps the existing product interface to the experimental states required for the Human Factors study.

The intention is to preserve the original product architecture while identifying the minimum set of screens and states required for controlled experimentation.

---

2. Existing Product → Experimental Mapping

Existing Product Surface| Experimental Role
Journey Dashboard| Primary experimental environment
Contextual Explanation Card| Main experimental manipulation
Route Visualization| Environmental/route context
Vehicle Diagnostics| Optional supporting transparency context
Emergency Interface| Safety boundary / non-experimental control
Accessibility Settings| Accessibility support
Trip Completion| End-of-journey context

The Journey Dashboard is especially important because the original PRD defines it as the central ride surface and explicitly includes contextual explanation cards when events occur.

---

3. Experimental Screen Flow

START
  │
  ▼
Pre-Trial Instructions
  │
  ▼
Normal Journey Dashboard
  │
  ▼
Scenario Event
  │
  ▼
Vehicle Behaviour Changes
  │
  ├──────────────┬───────────────┐
  ▼              ▼               ▼
No Explanation   Minimal        Contextual
Condition A      Condition B    Condition C
  │              │               │
  └──────────────┴───────────────┘
                 │
                 ▼
          Observation Period
                 │
                 ▼
          Comprehension Task
                 │
                 ▼
             Trust Measure
                 │
                 ▼
           Workload Measure
                 │
                 ▼
             Trial Complete

---

4. Journey Dashboard States

The existing Journey Dashboard should support at least these experimental states:

State JD-01 — Cruising Normal

Normal ride.

No event explanation is visible.

---

State JD-02 — Event Active

The vehicle is responding to an unexpected event.

The interface should make the change in vehicle behaviour perceivable.

---

State JD-03A — Event Without Explanation

Condition A.

Vehicle behaviour changes but no explanation card appears.

---

State JD-03B — Event With Minimal Explanation

Condition B.

A concise explanation card appears.

---

State JD-03C — Event With Contextual Explanation

Condition C.

A contextual explanation card appears.

---

State JD-04 — Event Resolved

The event has passed and the vehicle returns to normal operation.

This state should be visually consistent across conditions.

---

5. State Transition Rules

JD-01
Cruising
   │
   ▼
JD-02
Event Active
   │
   ├── Condition A → JD-03A
   ├── Condition B → JD-03B
   └── Condition C → JD-03C
                         │
                         ▼
                     JD-04
                   Event Resolved
                         │
                         ▼
                  Comprehension

---

6. Scenario-to-Screen Mapping

Scenario| Event State| Vehicle Response| Explanation
SCN-01 Pedestrian| Event active| Slow| Pedestrian explanation
SCN-02 Merging vehicle| Event active| Slow/increase gap| Merging explanation
SCN-03 Obstacle| Event active| Slow/change trajectory| Obstacle explanation
SCN-04 Construction| Event active| Slow/change position| Construction explanation

---

7. Explanation Card Structure

The explanation card should follow a consistent structure.

Minimal

[Event icon]

Slowing for pedestrian.

Contextual

[Event icon]

Pedestrian entering the crossing ahead.

Slowing to maintain a safe distance.

The visual structure should remain consistent.

The content is what changes.

---

8. Visual Hierarchy

The experimental explanation should not visually overpower the rest of the interface.

Priority:

1. immediate safety-relevant state
2. autonomous vehicle behaviour
3. explanation
4. route/context information
5. secondary controls

The interface should remain calm rather than presenting every event as an emergency.

This follows the original product principle that the cabin should remain calm by default while becoming present and informative during critical situations.

---

9. Figma Component Requirements

The experimental prototype should include reusable components for:

- Journey Dashboard
- Vehicle Status
- Route/ETA Card
- Event Indicator
- Explanation Card
- Vehicle Behaviour Indicator
- Comprehension Question
- Response Option
- Trust Rating
- Workload Interface
- Trial Progress Indicator
- Trial Completion

Components should use the existing design system rather than introducing unrelated visual styles.

---

10. Component Variants

The Explanation Card should have at least three variants:

ExplanationCard
├── Hidden
├── Minimal
└── Contextual

The same component should be used for all scenarios.

Only the content should change according to the scenario.

---

11. Design-System Consistency

The existing PRD specifies semantic design tokens for colour, typography, spacing, radius, elevation, motion, and opacity, with support for light and dark themes.

The experimental prototype should therefore:

- reuse existing semantic tokens
- preserve light/dark behaviour
- preserve typography hierarchy
- preserve touch-target principles
- preserve status-language conventions
- avoid introducing experimental styling that itself becomes a confounding variable

---

12. Prototype Branching

The preferred architecture is:

COMMON JOURNEY
      │
      ▼
COMMON EVENT
      │
      ▼
COMMON VEHICLE RESPONSE
      │
      ├───────────────┐
      │               │
      ▼               ▼
Condition A       Condition B/C
      │               │
No explanation    Explanation
      │               │
      └───────┬───────┘
              ▼
       COMMON MEASURES

This minimizes unintended variation.

---

13. Research-Critical Screens

The following screens are considered research-critical:

Tier 1

- Journey Dashboard
- Event state
- Explanation state
- Comprehension task
- Trust measure
- Workload measure

Tier 2

- Pre-trial instructions
- Trial completion
- Route context

Tier 3

- Diagnostics
- Entertainment
- Profile
- Other product surfaces

Tier 3 surfaces should not be expanded unless required by the experimental scenario.

---

14. Prototype Navigation Principle

The participant should not need to navigate through the complete product.

The experimental flow should be controlled and linear:

Start
 ↓
Journey
 ↓
Event
 ↓
Explanation
 ↓
Observation
 ↓
Question
 ↓
Measures
 ↓
Next Trial

This prevents navigation skill from becoming an unintended experimental variable.

---

15. Validation Checklist

Before prototype testing:

- [ ] All required states exist.
- [ ] Conditions A/B/C are clearly separated.
- [ ] Vehicle response is identical between conditions.
- [ ] Explanation timing is consistent.
- [ ] Explanation placement is consistent.
- [ ] Question wording is identical.
- [ ] Response controls work.
- [ ] Trial reset works.
- [ ] No accidental condition information is visible.
- [ ] Light/dark themes remain consistent.
- [ ] Accessibility checks have been performed.
- [ ] Prototype can be demonstrated without improvisation.

---

16. Current Status

Status: Prototype architecture defined.

Next implementation step:

Translate this state map into Figma frames, components, and prototype connections.
