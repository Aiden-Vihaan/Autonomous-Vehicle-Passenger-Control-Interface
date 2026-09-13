Experimental State System

1. Purpose

This document defines the state model governing the experimental prototype.

The purpose is to ensure that every participant encounters the same logical sequence while allowing the explanation condition to vary in a controlled manner.

---

2. Core State Machine

The experimental prototype follows:

TRIAL INITIALIZATION
        ↓
NORMAL JOURNEY
        ↓
EVENT APPROACH
        ↓
UNEXPECTED EVENT
        ↓
AUTONOMOUS RESPONSE
        ↓
EXPLANATION CONDITION
        ↓
PASSENGER OBSERVATION
        ↓
COMPREHENSION
        ↓
TRUST / EXPERIENCE
        ↓
WORKLOAD
        ↓
TRIAL COMPLETE

---

3. State Definitions

EXP-00 — Trial Initialization

Purpose:

Prepare the participant for the upcoming trial.

Required information:

- trial identifier;
- scenario identifier;
- condition identifier;
- instructions where required.

The participant should not be exposed to unnecessary information about the experimental hypothesis.

---

EXP-01 — Practice

Purpose:

Familiarize the participant with the interaction procedure.

The practice trial should demonstrate:

- how the journey interface works;
- how an event appears;
- how the participant observes the autonomous response;
- how questions are answered;
- how the trial progresses.

Practice data should be clearly separated from experimental data.

---

EXP-02 — Normal Journey

The vehicle is travelling normally.

No experimental event has yet occurred.

The interface should establish a stable baseline state.

---

EXP-03 — Event Approach

The system approaches the predefined scenario event.

The event timing should be standardized within the limits of the prototype.

The participant should not receive condition-specific explanatory information prematurely.

---

EXP-04 — Unexpected Event

The predefined environmental event occurs.

Examples:

Pedestrian entering crossing
Vehicle merging ahead
Obstacle detected
Road construction/lane restriction

The event must be identical across explanation conditions for a given scenario.

---

EXP-05 — Autonomous Response

The vehicle performs the predefined response.

Examples:

Slows
Increases following distance
Adjusts trajectory
Changes position

The response must remain constant across explanation conditions.

---

4. Explanation State

The explanation state is controlled by the experimental condition.

EXP-05
   │
   ├── Condition A → No Explanation
   │
   ├── Condition B → Minimal Explanation
   │
   └── Condition C → Contextual Explanation

---

Condition A

Explanation = NONE

No explanation card is displayed.

---

Condition B

Explanation = MINIMAL

The interface provides a concise reason for the autonomous response.

---

Condition C

Explanation = CONTEXTUAL

The interface provides the environmental context and the corresponding autonomous response.

---

5. Passenger Observation

After the autonomous response and explanation state, the participant receives a controlled observation interval.

The observation interval should be consistent across conditions where feasible.

The participant should not be asked to perform unnecessary actions during this period.

Purpose:

Allow the participant to process the vehicle behaviour before the comprehension measurement.

---

6. Comprehension State

The participant answers a scenario-specific comprehension question.

The question should measure whether the participant understood the relevant reason for the autonomous behaviour.

Required fields:

scenario_id
condition_id
question_id
response
correct
response_time

---

7. Trust / Experience State

The participant provides the selected trust and experience measures.

The interface should:

- use consistent response scales;
- prevent accidental double submission;
- avoid indicating desirable answers;
- record responses without exposing participant identity.

---

8. Workload State

The participant completes the selected workload measurement.

The workload interface should be visually distinct from the vehicle interface.

This separation helps distinguish:

Passenger HMI

from

Research Measurement Interface

---

9. Trial Completion

The trial ends after all required measurements have been submitted.

The prototype records:

trial_id
scenario_id
condition_id
completion_status

The next trial begins only after the previous trial has been completed.

---

10. Transition Rules

Current State| Trigger| Next State
Initialization| Start| Practice / Normal Journey
Practice| Practice complete| Normal Journey
Normal Journey| Event threshold reached| Event Approach
Event Approach| Event occurs| Unexpected Event
Unexpected Event| Vehicle responds| Autonomous Response
Autonomous Response| Response stable| Explanation
Explanation| Display interval complete| Observation
Observation| Observation interval complete| Comprehension
Comprehension| Answer submitted| Trust / Experience
Trust / Experience| Measure submitted| Workload
Workload| Measure submitted| Trial Complete
Trial Complete| Next trial| Trial Initialization

---

11. Error Prevention

The prototype should prevent invalid state transitions.

Examples:

- participant cannot submit comprehension before the question is displayed;
- participant cannot continue without completing required measurements;
- explanation condition cannot change during a trial;
- scenario cannot change after trial initialization;
- completed trials cannot be accidentally overwritten;
- practice data cannot be mixed with experimental data.

---

12. Condition Integrity

The condition must be assigned before the trial begins.

Trial
│
├── Scenario
├── Condition
└── Participant

The condition must remain fixed until the trial is complete.

No participant-facing interaction should allow the participant to select or change the explanation condition.

---

13. Scenario Integrity

Each scenario has a fixed definition.

Example:

SCN-01

Event:
Pedestrian enters crossing.

Vehicle response:
Slows to maintain safe distance.

Condition:
A / B / C

Explanation:
Condition-dependent.

The following must remain constant across conditions:

- event;
- vehicle response;
- scenario context;
- question;
- measurement procedure.

The explanation presentation is the primary manipulated factor.

---

14. Figma Prototype Branching

The prototype should represent the experiment as controlled branches.

START
  ↓
SCENARIO
  ↓
EVENT
  ↓
RESPONSE
  ↓
CONDITION
 ┌───────┼────────┐
 ↓       ↓        ↓
 A       B        C
 ↓       ↓        ↓
Observation
     ↓
Comprehension
     ↓
Trust
     ↓
Workload
     ↓
Complete

The branching structure should not alter the downstream measurement procedure.

---

15. State Naming Convention

Use the following naming system in Figma:

EXP-00-START
EXP-01-PRACTICE
EXP-02-NORMAL
EXP-03-EVENT-APPROACH
EXP-04-UNEXPECTED-EVENT
EXP-05-RESPONSE
EXP-05A-NO-EXPLANATION
EXP-05B-MINIMAL-EXPLANATION
EXP-05C-CONTEXTUAL-EXPLANATION
EXP-06-COMPREHENSION
EXP-07-TRUST
EXP-08-WORKLOAD
EXP-09-COMPLETE

---

16. Validation Criteria

The state system is valid when:

- [ ] every trial follows the defined sequence;
- [ ] all three explanation conditions are reachable;
- [ ] condition assignment occurs before explanation presentation;
- [ ] event and autonomous response remain constant across conditions;
- [ ] measurement screens remain identical across conditions unless intentionally specified;
- [ ] invalid transitions are prevented;
- [ ] practice trials are separated from experimental trials;
- [ ] trial completion is unambiguous;
- [ ] state names are consistent between documentation and Figma.

---

17. Experimental Principle

The prototype must separate what the vehicle does from how that behaviour is explained.

Vehicle Behaviour
        ↓
    [FIXED]
        ↓
Explanation Presentation
        ↓
   [MANIPULATED]
        ↓
Passenger Response
        ↓
   [MEASURED]

This separation is central to maintaining experimental interpretability.
