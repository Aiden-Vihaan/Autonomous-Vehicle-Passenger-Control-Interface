High-Fidelity Core Journey Screen Specification

1. Purpose

This document specifies the first high-fidelity screen implementations for the core autonomous-vehicle passenger journey.

The initial focus is the sequence:

Normal Journey
      ↓
Event Approach
      ↓
Unexpected Event
      ↓
Autonomous Response
      ↓
Explanation

This sequence represents the central interaction being evaluated in the experiment.

---

2. EXP-02 / Normal Journey

Objective

Establish the baseline passenger experience during normal autonomous travel.

Primary Regions

┌──────────────────────────────────────────────┐
│ Journey Status                               │
├───────────────────────────────┬──────────────┤
│                               │              │
│       Journey / Environment   │ Route        │
│                               │ Progress     │
│                               │              │
├───────────────────────────────┴──────────────┤
│ Vehicle Status                               │
└──────────────────────────────────────────────┘

The exact visual arrangement should follow the established Figma grid.

Primary Components

- Journey Status
- Route Progress
- Vehicle Status
- supporting journey information

Visual Behaviour

The screen should feel stable and predictable.

No component should unnecessarily attract attention.

---

3. EXP-03 / Event Approach

Objective

Transition the passenger from normal travel toward the environmental event.

Required Information

- current journey context
- approaching event
- vehicle status
- relevant environmental information

The event should become noticeable without prematurely revealing the explanation condition.

---

4. EXP-04 / Unexpected Event

Objective

Represent the event that causes a change in autonomous vehicle behaviour.

Required Components

Event Indicator
Vehicle Status
Journey Context

Information Hierarchy

The event should become the primary piece of contextual information.

Secondary journey information should remain available but visually subordinate.

---

5. EXP-05 / Autonomous Response

Objective

Communicate the vehicle's response.

Structure

[Vehicle Status]

Vehicle response

[Action]

Example:

Vehicle response

Slowing down

The response wording must remain consistent across the explanation conditions.

---

6. EXP-05A / No Explanation

Objective

Represent the experimental control condition.

The participant sees the autonomous response but receives no explicit reason for that response.

Required Content

- event context
- autonomous response
- normal interface context

Prohibited Content

Do not add:

- explicit reason
- causal helper text
- explanatory icon
- secondary explanation
- animation whose meaning reveals the cause

---

7. EXP-05B / Minimal Explanation

Objective

Provide a concise causal explanation.

Structure

Vehicle response

Slowing down


Why?

Slowing for pedestrian.

The explanation should be immediately understandable.

---

8. EXP-05C / Contextual Explanation

Objective

Provide a more detailed causal explanation.

Structure

Vehicle response

Slowing down


Why?

Pedestrian entering the crossing ahead.

Slowing to maintain a safe distance.

The contextual condition should provide additional information while retaining the same overall interaction structure.

---

9. Cross-Condition Consistency

For the same scenario:

Element| Condition A| Condition B| Condition C
Event| Same| Same| Same
Vehicle response| Same| Same| Same
Screen position| Equivalent| Equivalent| Equivalent
Theme| Same| Same| Same
Interaction| Equivalent| Equivalent| Equivalent
Explanation| None| Minimal| Contextual

---

10. Visual Hierarchy

Across the event sequence, the hierarchy should progressively shift.

Normal

Journey > Status > Secondary information

Event

Event > Vehicle response > Journey

Explanation

Vehicle response > Explanation > Secondary information

This hierarchy supports the principle:

«The interface should demand attention when the situation requires it, not continuously.»

---

11. Component Reuse

The following components should be reused rather than recreated:

COMP / Shell
COMP / Journey Status
COMP / Route Progress
COMP / Vehicle Status
COMP / Event
COMP / Autonomous Response
COMP / Explanation
COMP / Emergency Action

Reusing components reduces visual inconsistency and makes later revisions safer.

---

12. Accessibility Review

Check each screen for:

- text readability
- contrast
- state recognition without colour
- clear touch targets
- logical grouping
- predictable placement
- concise language
- sufficient spacing

---

13. Experimental Review

Before finalizing each condition, ask:

Question 1

Could a participant determine the explanation condition from anything other than the intended explanatory content?

If yes, revise the screen.

Question 2

Does the autonomous response remain identical?

If no, revise the screen.

Question 3

Does the event remain identical?

If no, revise the screen.

Question 4

Does visual emphasis unintentionally favour one condition?

If yes, review the design.

---

14. High-Fidelity Completion Criteria

The core journey screens are complete when:

- [ ] Normal Journey is implemented.
- [ ] Event Approach is implemented.
- [ ] Unexpected Event is implemented.
- [ ] Autonomous Response is implemented.
- [ ] No Explanation is implemented.
- [ ] Minimal Explanation is implemented.
- [ ] Contextual Explanation is implemented.
- [ ] Components are reused.
- [ ] Visual hierarchy is consistent.
- [ ] Accessibility is reviewed.
- [ ] Experimental integrity is preserved.

---

15. Next Step

After these screens are assembled, the next phase is interaction prototyping and transition validation.

The primary sequence to validate is:

EXP-02
  ↓
EXP-03
  ↓
EXP-04
  ↓
EXP-05
  ↓
EXP-05A / EXP-05B / EXP-05C
  ↓
EXP-06

This sequence should be tested before expanding the high-fidelity implementation to the remaining measurement and completion screens.
