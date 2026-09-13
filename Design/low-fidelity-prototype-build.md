Low-Fidelity Experimental Prototype Build

1. Purpose

Day 17 translates the previously defined component system, state system, and experimental information architecture into the first functional low-fidelity Figma prototype.

The objective is not visual polish.

The objective is to verify that:

- the complete experimental journey can be represented;
- the three explanation conditions can be isolated;
- the same scenario and autonomous response can be maintained across conditions;
- the measurement sequence can be completed;
- the prototype can be modified efficiently before high-fidelity design begins.

---

2. Prototype Scope

The low-fidelity prototype contains the following states:

EXP-00-START
        ↓
EXP-01-PRACTICE
        ↓
EXP-02-NORMAL
        ↓
EXP-03-EVENT-APPROACH
        ↓
EXP-04-UNEXPECTED-EVENT
        ↓
EXP-05-RESPONSE
        ↓
EXP-05A-NO-EXPLANATION
EXP-05B-MINIMAL-EXPLANATION
EXP-05C-CONTEXTUAL-EXPLANATION
        ↓
EXP-06-COMPREHENSION
        ↓
EXP-07-TRUST
        ↓
EXP-08-WORKLOAD
        ↓
EXP-09-COMPLETE

---

3. Low-Fidelity Design Principle

The prototype should communicate structure and interaction before aesthetics.

The following elements should be intentionally simplified:

- color;
- typography styling;
- decorative imagery;
- animation;
- branding details;
- visual effects;
- advanced map styling.

The following elements must remain clear:

- hierarchy;
- information location;
- interaction;
- state transitions;
- explanation differences;
- measurement sequence;
- navigation;
- error prevention.

---

4. Figma Page Structure

Create or maintain the following pages:

00 — Cover
01 — Foundations
02 — Components
03 — Experimental States
04 — Scenario Flows
05 — Low-Fidelity Prototype
06 — High-Fidelity Prototype
07 — Measurement Screens
08 — Accessibility
09 — Prototype Testing

Day 17 primarily uses:

03 — Experimental States
04 — Scenario Flows
05 — Low-Fidelity Prototype

---

5. Frame Structure

Create frames using the established naming convention.

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

Each frame should have a clear label identifying its experimental state.

---

6. EXP-00 — Start

Purpose:

Introduce the experimental prototype and begin the task.

Required elements:

Project / Study Title
Brief Instructions
Start Button

The start screen should not reveal the experimental hypothesis.

---

7. EXP-01 — Practice

Purpose:

Familiarize the participant with the interaction sequence.

Required elements:

Journey Interface
Example Event
Example Vehicle Response
Example Explanation
Continue Button

The practice screen should clearly indicate that it is a practice interaction.

Practice data must not be treated as experimental data.

---

8. EXP-02 — Normal Journey

Required elements:

Journey Status
Destination
Route / Environmental Context
Vehicle Status
Progress Information

The interface should establish a calm baseline state.

No experimental explanation should appear at this stage.

---

9. EXP-03 — Event Approach

The interface transitions from normal journey to the predefined event.

Required elements:

Current Journey
Environmental Context
Event Indicator
Vehicle State

The transition should be understandable without requiring unnecessary interaction.

---

10. EXP-04 — Unexpected Event

The predefined environmental event is presented.

For the initial prototype, use:

SCN-01 — Pedestrian Crossing

Event:

A pedestrian enters the crossing ahead.

The event representation should be identical across all explanation conditions.

---

11. EXP-05 — Autonomous Response

The vehicle responds to the event.

For SCN-01:

Vehicle response:
Slowing to maintain a safe distance.

The response must be identical across conditions.

This is important because the experimental manipulation concerns the explanation presentation rather than the autonomous behaviour.

---

12. EXP-05A — No Explanation

The vehicle responds but no explanation card is presented.

Structure:

Journey Interface
        ↓
Vehicle Response
        ↓
No Explanation

Do not replace the explanation with another message.

The absence of the explanation is the experimental condition.

---

13. EXP-05B — Minimal Explanation

Present the minimal explanation.

Example:

Slowing for pedestrian.

The message should be concise and directly related to the autonomous response.

No additional contextual information should be introduced.

---

14. EXP-05C — Contextual Explanation

Present the contextual explanation.

Example:

Pedestrian entering the crossing ahead.

Slowing to maintain a safe distance.

The contextual condition provides more information than the minimal condition while referring to the same event and response.

---

15. EXP-06 — Comprehension

After the explanation/observation stage, present the scenario-specific comprehension question.

Example:

Why did the vehicle slow down?

○ A pedestrian entered the crossing
○ The destination changed
○ The vehicle encountered a system failure
○ The passenger requested a stop

The response options should be randomized later if required by the finalized experimental protocol.

For the low-fidelity prototype, the main objective is to validate the interaction structure.

---

16. EXP-07 — Trust

Present the finalized trust measure.

Structure:

Question
Response Scale
Continue / Submit

The interface should not communicate that a high-trust response is desirable.

The research objective is to measure passenger trust rather than encourage it.

---

17. EXP-08 — Workload

Present the selected workload measurement interface.

The final implementation should follow the finalized workload protocol.

For the low-fidelity stage:

Question / Scale
Response
Continue

The visual implementation can be refined after the measurement protocol is finalized.

---

18. EXP-09 — Trial Complete

Required elements:

Trial Complete
Confirmation
Next Trial / End Study

The participant should receive an unambiguous indication that the current trial has ended.

---

19. Prototype Connections

Create the following basic prototype connections:

START
 ↓
PRACTICE
 ↓
NORMAL
 ↓
EVENT APPROACH
 ↓
UNEXPECTED EVENT
 ↓
RESPONSE

From RESPONSE:

RESPONSE
 ├── NO EXPLANATION
 ├── MINIMAL
 └── CONTEXTUAL

Each branch must then converge:

NO EXPLANATION ─┐
MINIMAL ────────┼→ COMPREHENSION
CONTEXTUAL ─────┘
                    ↓
                  TRUST
                    ↓
                 WORKLOAD
                    ↓
                 COMPLETE

---

20. Branching Integrity

The branches must differ only where the experimental condition requires a difference.

The following should remain constant:

Scenario
Environmental Event
Vehicle Response
Comprehension Question
Trust Measurement
Workload Measurement
Trial Completion

The primary manipulated element is:

Explanation Condition

---

21. Scenario Variable

Create a scenario variable or documented scenario property.

Initial value:

scenario_id = SCN-01

Scenario:

Pedestrian Crossing

Future scenarios:

SCN-02 — Vehicle Merging
SCN-03 — Obstacle Ahead
SCN-04 — Road Construction

The first prototype should prioritize one fully validated scenario before expanding to all scenarios.

---

22. Condition Variable

Define:

condition_id

with:

A = No Explanation
B = Minimal Explanation
C = Contextual Explanation

The condition must remain fixed throughout the trial.

---

23. Low-Fidelity Visual Rules

Use a deliberately simple visual language.

Prioritize:

1. hierarchy;
2. spacing;
3. information placement;
4. interaction clarity;
5. state visibility.

Avoid spending significant time on:

- gradients;
- shadows;
- complex illustrations;
- final iconography;
- decorative animations;
- detailed map rendering.

These belong to later design stages.

---

24. Interaction Rules

The prototype should:

- use predictable navigation;
- provide visible interaction states;
- avoid hidden actions;
- prevent accidental progression;
- make required responses clear;
- maintain consistent button placement;
- preserve the experimental sequence.

---

25. Accessibility Checks

At low fidelity, verify:

- text is readable;
- labels are understandable;
- controls are distinguishable;
- status is not communicated through color alone;
- interaction order is logical;
- important information is not dependent on tiny visual elements.

Accessibility refinement will continue during high-fidelity design.

---

26. Prototype Validation

Run the complete prototype manually.

Test:

START
→ PRACTICE
→ NORMAL
→ EVENT
→ RESPONSE
→ CONDITION
→ COMPREHENSION
→ TRUST
→ WORKLOAD
→ COMPLETE

Repeat the test for:

Condition A
Condition B
Condition C

---

27. Validation Questions

After running each branch, record:

Navigation

- Does every required state connect correctly?
- Are there dead ends?
- Are there accidental loops?

Experimental control

- Does the scenario remain identical?
- Does the autonomous response remain identical?
- Does only the explanation change?

Comprehension

- Is the question clearly presented?
- Is the participant able to answer without interface confusion?

Measurement

- Are trust and workload screens clearly separated from the passenger interface?
- Are required responses obvious?

Accessibility

- Is the information hierarchy understandable?
- Can important information be identified without relying on color alone?

---

28. Prototype Testing Log

Record issues using:

Issue ID:
Date:
Frame:
Problem:
Severity:
Observed Behaviour:
Expected Behaviour:
Proposed Fix:
Status:

Severity:

Critical
High
Medium
Low

---

29. Completion Criteria

Day 17 is complete when:

- [ ] all experimental frames exist;
- [ ] the first scenario is represented;
- [ ] the three explanation conditions are implemented;
- [ ] the prototype branches correctly;
- [ ] all branches converge on the same measurement sequence;
- [ ] no explanation condition changes the vehicle response;
- [ ] the prototype can be run from start to completion;
- [ ] major navigation errors are documented;
- [ ] low-fidelity visual complexity remains controlled;
- [ ] the Figma structure is ready for iteration.

---

30. Day 17 Principle

The objective is not to make the prototype look finished.

The objective is to make the experimental logic runnable.

A visually simple prototype with controlled experimental branching is more valuable at this stage than a polished interface with uncontrolled differences between conditions.
