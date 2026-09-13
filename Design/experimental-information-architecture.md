Experimental Information Architecture

Project

Autonomous Vehicle Passenger Control Interface

Day

Day 14 — Experimental Prototype Information Architecture

Purpose

This document defines the information architecture for the experimental prototype used to evaluate how different explanation designs affect passenger understanding, trust, and cognitive workload during unexpected autonomous-vehicle behaviour.

The experimental prototype is derived from the existing Autonomous Vehicle Passenger Control Interface product concept. The original product identity, core passenger-control functions, and safety-oriented interaction principles are retained.

The experimental layer introduces controlled explanation conditions without changing the underlying autonomous-vehicle event or response.

---

1. Prototype Architecture

The experimental prototype follows the sequence:

Scenario Selection
        ↓
Trial Initialization
        ↓
Normal Journey
        ↓
Unexpected Event
        ↓
Autonomous Vehicle Response
        ↓
Explanation Condition
        ↓
Passenger Observation
        ↓
Comprehension Measurement
        ↓
Trust / Experience Measurement
        ↓
Workload Measurement
        ↓
Trial Completion

The prototype therefore separates:

1. Vehicle behaviour
2. Passenger-facing explanation
3. Passenger response
4. Research measurement

This separation is necessary to preserve experimental control.

---

2. Core Information Architecture

2.1 Scenario Layer

The scenario layer determines:

- scenario identity
- environmental context
- unexpected event
- autonomous vehicle response
- event timing
- explanation condition

The vehicle response must remain constant across explanation conditions.

Example:

Scenario:
Pedestrian crossing

Event:
Pedestrian enters crossing ahead

Vehicle response:
Vehicle slows and maintains a safe distance

Explanation:
Controlled experimental variable

---

3. Passenger HMI Layer

The passenger-facing interface contains the following major states.

State 01 — Journey Dashboard

Purpose:

Provide the baseline journey context before an unexpected event occurs.

Information:

- current journey
- destination
- route context
- vehicle status
- estimated arrival
- relevant journey controls

The dashboard should remain visually stable before the experimental event.

---

State 02 — Event Detection

Purpose:

Represent the moment at which the autonomous vehicle encounters an unexpected environmental event.

Example:

EVENT DETECTED

Pedestrian ahead

This state communicates that the vehicle has detected a change without unnecessarily revealing the experimental explanation condition.

---

State 03 — Autonomous Response

Purpose:

Show the vehicle's response to the event.

Example:

Vehicle slowing

Reason:
Pedestrian crossing ahead

The vehicle action must be identical across all explanation conditions.

---

State 04 — Explanation

This is the principal experimental state.

Three explanation conditions are represented.

Condition A — No Explanation

The passenger sees the vehicle response without an explanatory message.

Vehicle slowing

No additional causal explanation is presented.

---

Condition B — Minimal Explanation

The passenger receives a concise explanation.

Slowing for pedestrian.

The explanation identifies the immediate reason for the action.

---

Condition C — Contextual Explanation

The passenger receives a more informative explanation containing event context and intended safety rationale.

Example:

Pedestrian entering the crossing ahead.

Slowing to maintain a safe distance.

The contextual explanation should provide more information than Condition B while remaining concise enough for an in-cabin interface.

---

4. Measurement Layer

The measurement layer is deliberately separated from the passenger HMI.

It contains:

4.1 Comprehension

Questions assess whether the participant understood:

- what happened
- why the vehicle responded
- what the vehicle was doing

Example:

Why did the vehicle slow down?

Response options should be standardized across conditions.

---

4.2 Trust

Trust-related questions assess the participant's perception of the autonomous system following the event.

The measurement should distinguish:

Trust

from:

Trust calibration

The objective is not to maximize trust.

The objective is to determine whether the explanation supports an appropriate level of trust relative to the observed vehicle behaviour.

---

4.3 Workload

A workload measurement is presented according to the experimental protocol.

NASA-TLX may be used where appropriate.

The measurement interface must not influence the preceding trial.

---

5. Information Hierarchy

The experimental explanation component should follow this hierarchy:

1. What the vehicle is doing
2. What caused the behaviour
3. Why the response is occurring
4. Optional supporting context

However, not every condition exposes every information level.

Information| No Explanation| Minimal| Contextual
Vehicle action| ✓| ✓| ✓
Immediate cause| —| ✓| ✓
Event context| —| —| ✓
Safety rationale| —| —| ✓

This hierarchy creates the intended manipulation while keeping the underlying event constant.

---

6. Prototype Navigation Structure

START
  ↓
Practice Trial
  ↓
Scenario Introduction
  ↓
Normal Journey
  ↓
Unexpected Event
  ↓
Vehicle Response
  ↓
Explanation Condition
  ↓
Observation
  ↓
Comprehension
  ↓
Trust / Experience
  ↓
Workload
  ↓
Trial Complete
  ↓
Next Trial

After all experimental trials:

Final Questionnaire
        ↓
Debrief
        ↓
END

---

7. Figma Page Structure

The Figma file should be organized into clearly separated pages.

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

The existing product screens should remain identifiable as part of the original product scope.

The experimental prototype should be clearly marked as an evaluation layer.

---

8. Frame Naming Convention

Use consistent frame names.

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

For scenarios:

SCN-01-Pedestrian
SCN-02-Merging
SCN-03-Obstacle
SCN-04-Road-Construction

---

9. Component Architecture

The experimental prototype should use reusable components rather than independent screen-specific designs.

Core components:

Journey Dashboard
Vehicle Status
Event Indicator
Autonomous Response Card
Explanation Card
Safety Status
Progress Indicator
Question Card
Response Option
Trust Rating
Workload Interface
Trial Completion

The explanation component should support controlled variants:

Explanation / None
Explanation / Minimal
Explanation / Contextual

This makes the experimental manipulation explicit and reduces accidental visual differences between conditions.

---

10. Accessibility Architecture

Accessibility must be considered during prototype construction rather than added after the visual design is complete.

Requirements include:

- readable typography
- sufficient text size
- clear information hierarchy
- non-colour-only communication
- meaningful labels
- consistent interaction placement
- readable contrast
- predictable navigation
- concise explanation text
- clear distinction between system state and user action

If audio explanations are later included, the modality must be treated as an experimental variable rather than introduced inconsistently.

---

11. Experimental Control Principle

The following elements must remain constant between explanation conditions wherever possible:

- scenario
- environmental event
- autonomous response
- event timing
- interface layout
- typography
- visual hierarchy
- participant task
- question wording
- measurement procedure

The principal manipulated factor is:

Explanation condition

The prototype should therefore avoid introducing unrelated visual or interaction changes between conditions.

---

12. Design Decision

The experimental prototype will prioritize experimental validity over visual complexity.

High-fidelity visual polish will be developed later.

At Day 14, the objective is to establish:

- information hierarchy
- screen sequence
- state transitions
- explanation variants
- measurement sequence
- component structure
- Figma organization
- experimental control

No claim of empirical effectiveness should be made until the prototype has been tested and data have been collected.

---

13. Day 14 Completion Criteria

Day 14 is complete when:

- [ ] Information architecture is documented.
- [ ] Experimental states are defined.
- [ ] Explanation conditions are explicitly separated.
- [ ] Figma page structure is established.
- [ ] Frame naming convention is established.
- [ ] Core experimental components are identified.
- [ ] Measurement screens are mapped.
- [ ] Scenario naming is standardized.
- [ ] Experimental control requirements are documented.
- [ ] Accessibility requirements are carried into prototype planning.
- [ ] No untested claims are presented as findings.

---

14. Next Step

Day 15 will translate this information architecture into a low-fidelity experimental interaction flow.

The next stage will focus on:

1. wireframe structure
2. screen-to-screen transitions
3. explanation-card placement
4. participant interaction points
5. condition switching
6. measurement flow
7. prototype validation

High-fidelity visual styling should begin only after the experimental flow has been validated.
