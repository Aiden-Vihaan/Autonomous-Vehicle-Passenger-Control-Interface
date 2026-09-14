High-Fidelity Screen Assembly Plan

1. Purpose

This document defines the process for assembling the high-fidelity experimental screens using the foundations and reusable components established during the previous phase.

The objective is to create a visually coherent passenger interface while preserving the experimental architecture.

The high-fidelity phase must not alter:

- research questions
- experimental conditions
- scenario sequence
- autonomous vehicle response
- explanation manipulation
- measurement sequence
- participant task

---

2. High-Fidelity Screen Set

The experimental prototype will contain the following primary screens:

EXP-00 / Start
EXP-01 / Practice
EXP-02 / Normal Journey
EXP-03 / Event Approach
EXP-04 / Unexpected Event
EXP-05 / Autonomous Response
EXP-05A / No Explanation
EXP-05B / Minimal Explanation
EXP-05C / Contextual Explanation
EXP-06 / Comprehension
EXP-07 / Trust
EXP-08 / Workload
EXP-09 / Complete

---

3. Screen Assembly Strategy

Screens should be assembled in the following order:

Phase 1 — Entry

- Start
- Practice

Phase 2 — Normal Journey

- Normal Journey
- Event Approach

Phase 3 — Safety-Relevant Event

- Unexpected Event
- Autonomous Response

Phase 4 — Experimental Manipulation

- No Explanation
- Minimal Explanation
- Contextual Explanation

Phase 5 — Measurement

- Comprehension
- Trust
- Workload

Phase 6 — Completion

- Trial Complete

This order follows the experimental state model.

---

4. EXP-00 / Start

Purpose

Introduce the experimental interaction and provide the participant with a clear starting point.

Primary Content

- experiment introduction
- participant instructions
- start action

Design Priority

The screen should be visually simple.

The participant should understand:

1. what they are about to do;
2. what their role is;
3. how to begin.

Avoid unnecessary information.

---

5. EXP-01 / Practice

Purpose

Allow the participant to become familiar with the interaction format before experimental trials begin.

Content

- brief practice instructions
- representative interaction
- continuation action

The practice trial must not reveal the expected response to the experimental conditions.

---

6. EXP-02 / Normal Journey

Purpose

Represent normal autonomous travel before the relevant event occurs.

Primary Components

- Journey Status
- Route Progress
- Vehicle Status
- primary journey information

Design Principle

The normal journey should remain calm and visually stable.

The interface should not continuously demand passenger attention.

---

7. EXP-03 / Event Approach

Purpose

Represent the transition from normal travel toward an environmental event.

The screen should provide sufficient contextual continuity without prematurely revealing the experimental explanation.

Components

- Journey Status
- Event context
- Vehicle Status
- Route information where applicable

The event should remain understandable without introducing the explanation manipulation early.

---

8. EXP-04 / Unexpected Event

Purpose

Represent the unexpected environmental event that causes the autonomous vehicle to modify its behaviour.

Components

- Event Indicator
- Vehicle Status
- Journey context
- relevant autonomous-system information

The screen should establish:

Environmental Event
        ↓
Autonomous System Awareness

The explanatory reason should remain controlled according to the experimental state.

---

9. EXP-05 / Autonomous Response

Purpose

Communicate the vehicle's response to the detected event.

Primary Information

The passenger should be able to identify:

- what the vehicle is doing;
- that the behaviour is intentional;
- the current system state.

Example response:

Vehicle response
Slowing down

The wording must remain identical across explanation conditions for the same scenario.

---

10. EXP-05A / No Explanation

Purpose

Implement the control condition.

The screen communicates the autonomous response without providing an explanatory reason.

The design must be carefully audited for accidental explanation leakage.

Do not introduce explanatory information through:

- icons
- helper text
- labels
- route descriptions
- animations
- secondary cards
- status messages

---

11. EXP-05B / Minimal Explanation

Purpose

Provide a concise explanation of why the autonomous vehicle is responding as it is.

Structure:

Why?

[Concise explanation]

Example:

Why?

Slowing for pedestrian.

The explanation should be concise and directly related to the autonomous response.

---

12. EXP-05C / Contextual Explanation

Purpose

Provide a more detailed explanation containing environmental context and response rationale.

Structure:

Why?

[Environmental context]

[Response rationale]

Example:

Why?

Pedestrian entering the crossing ahead.

Slowing to maintain a safe distance.

The additional information is the intended experimental difference.

---

13. Explanation Screen Comparability

The three explanation screens must remain visually comparable.

Maintain equivalent:

- layout
- component placement
- typography system
- interaction structure
- system response
- scenario
- visual quality

The contextual condition may contain more text because explanatory specificity is being manipulated.

However, additional visual decoration must not be used to make it appear inherently more trustworthy or important.

---

14. EXP-06 / Comprehension

Purpose

Measure whether the participant understood the autonomous event and response.

The screen should be visually separated from the vehicle interface enough to establish that the participant is now answering a research question.

Design Requirements

- one clear question
- consistent response format
- no leading visual cues
- no immediate correctness feedback unless required by the protocol
- accessible text

---

15. EXP-07 / Trust

Purpose

Capture the participant's evaluation of the autonomous system following the relevant trial.

The exact measurement wording should follow the selected research instrument.

The interface should not visually suggest that a positive or negative answer is preferred.

---

16. EXP-08 / Workload

Purpose

Measure perceived cognitive workload using the selected workload procedure.

The screen should prioritize:

- clarity
- consistency
- low interaction friction

The measurement interface should not be interpreted as part of the autonomous vehicle experience itself.

---

17. EXP-09 / Complete

Purpose

Confirm completion of the current trial.

Content:

- completion confirmation
- continuation action where applicable

Avoid unnecessary feedback that could influence subsequent trials.

---

18. Persistent Interface Elements

Where appropriate, persistent elements should remain visually stable across the journey.

Possible elements include:

- journey status
- current destination
- vehicle operational state
- emergency access

However, persistence must not cause irrelevant information to remain visually dominant during safety-relevant states.

---

19. Information Hierarchy

The primary hierarchy should generally follow:

1. Immediate safety-relevant information
2. Autonomous vehicle response
3. Explanation
4. Passenger action
5. Journey context
6. Secondary information

The exact hierarchy may vary by system state.

---

20. Safety-Relevant Hierarchy

When the system enters a safety-relevant state:

Event
  ↓
Vehicle Response
  ↓
Why
  ↓
Passenger Action

The passenger should not need to search through secondary journey information to understand the event.

---

21. Motion and Transition Principles

Motion should support state recognition.

Use transitions to communicate:

- change in system state
- appearance of an event
- change in vehicle response
- appearance of explanation information

Avoid:

- decorative animation
- unnecessary motion
- excessive transitions
- animations that delay comprehension

Motion should never become the primary carrier of safety information.

---

22. Accessibility

Each screen should be checked for:

- readable typography
- sufficient contrast
- clear interaction targets
- non-colour state communication
- predictable navigation
- understandable wording
- consistent component placement

Accessibility must be considered before screen completion rather than added afterward.

---

23. Experimental Integrity Checklist

Before approving each screen:

- [ ] Correct experimental state
- [ ] Correct scenario
- [ ] Correct vehicle response
- [ ] Correct explanation condition
- [ ] No unintended explanation
- [ ] No additional information that changes the condition
- [ ] Correct transition
- [ ] Correct measurement sequence
- [ ] Consistent component use
- [ ] Accessibility reviewed

---

24. Screen Assembly Order in Figma

Build the first high-fidelity screens in this order:

1. EXP-02 / Normal Journey
2. EXP-03 / Event Approach
3. EXP-04 / Unexpected Event
4. EXP-05 / Autonomous Response
5. EXP-05A / No Explanation
6. EXP-05B / Minimal Explanation
7. EXP-05C / Contextual Explanation
8. EXP-06 / Comprehension
9. EXP-07 / Trust
10. EXP-08 / Workload
11. EXP-09 / Complete
12. EXP-00 / Start
13. EXP-01 / Practice

The event-to-explanation sequence is prioritized because it is central to the research question.

---

25. Definition of Done

The screen assembly phase is complete when:

1. All experimental states have corresponding high-fidelity frames.
2. Core components are used consistently.
3. The three explanation conditions are visually comparable.
4. The event-to-response sequence is clear.
5. Measurement screens are distinguishable from vehicle-interface screens.
6. Accessibility has been reviewed.
7. No experimental variable has been unintentionally changed.
8. The prototype can proceed to interaction-level validation.
