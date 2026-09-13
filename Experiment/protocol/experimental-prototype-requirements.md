Experimental Prototype Requirements

1. Purpose

This document translates the experimental protocol into concrete prototype requirements.

The experimental prototype will be built on top of the existing Autonomous Vehicle Passenger Control Interface project rather than replacing the original product design.

The original PRD defines a passenger-facing in-cabin interface for Level 4 and Level 5 autonomous vehicles, including a journey dashboard with contextual explanation cards, route visualization, vehicle diagnostics, emergency controls, accessibility settings, and other passenger-facing functions.

The experimental prototype adds a controlled Human Factors evaluation layer to this existing product.

---

2. Prototype Objective

The prototype must allow a participant to experience a standardized autonomous-vehicle event and evaluate the vehicle's behaviour under different explanation conditions.

The prototype must therefore support:

1. normal journey context
2. an unexpected event
3. autonomous vehicle response
4. explanation presentation
5. passenger observation
6. comprehension measurement
7. subjective evaluation
8. trial completion

---

3. Prototype Architecture

The experimental prototype follows this structure:

Scenario Engine
      ↓
Vehicle State
      ↓
Environmental Event
      ↓
Autonomous Response
      ↓
Explanation Engine
      ↓
Passenger HMI
      ↓
Comprehension Task
      ↓
Measurement Interface
      ↓
Trial Data

The prototype should separate:

- the underlying scenario
- the vehicle behaviour
- the explanation condition
- the evaluation procedure

This separation is necessary to maintain experimental control.

---

4. Required Prototype States

The minimum experimental prototype should contain the following states.

ID| State| Purpose
P01| Pre-Trial| Establish participant/task context
P02| Normal Journey| Establish baseline ride state
P03| Event Onset| Introduce the scenario event
P04| Vehicle Response| Display autonomous behaviour
P05-A| No Explanation| Condition A
P05-B| Minimal Explanation| Condition B
P05-C| Contextual Explanation| Condition C
P06| Observation| Allow participant to process event
P07| Comprehension| Measure understanding
P08| Trust Measure| Measure trust response
P09| Workload Measure| Measure cognitive workload
P10| Trial Complete| Transition to next trial

---

5. Screen Requirements

P01 — Pre-Trial

Purpose

Introduce the experimental task without revealing the research hypothesis.

Required elements

- neutral task instructions
- participant role as passenger
- interaction instructions
- response method
- indication that the participant will experience multiple journeys/events

Important constraint

The participant should not be told that explanations are the experimental manipulation.

---

6. P02 — Normal Journey

The normal journey state establishes the baseline passenger experience.

Required elements

- current journey
- destination
- ETA
- vehicle status
- route context
- primary passenger interface
- persistent safety access where appropriate

The original PRD specifies the Journey Dashboard as the central ride surface and includes route/ETA, vehicle-confidence information, comfort controls, media, safety access, and contextual explanation cards.

Experimental requirement

The baseline state should remain identical across explanation conditions.

---

7. P03 — Event Onset

The scenario-specific environmental event occurs.

Examples:

- pedestrian entering crossing
- vehicle merging
- obstacle ahead
- road construction/lane restriction

The event should be represented consistently across conditions.

---

8. P04 — Vehicle Response

The participant observes the autonomous vehicle responding to the event.

Possible responses include:

- slowing
- increasing following distance
- adjusting trajectory
- changing speed and position

The vehicle response must remain constant between Conditions A, B, and C.

---

9. P05 — Explanation Condition

This is the principal experimental manipulation.

Condition A — No Explanation

No explicit explanation card is presented.

The vehicle behaviour remains unchanged.

---

Condition B — Minimal Explanation

A concise explanation is displayed.

Example:

«Slowing for pedestrian.»

The explanation should communicate the immediate reason without additional contextual detail.

---

Condition C — Contextual Explanation

A more informative explanation is displayed.

Example:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

The explanation communicates:

1. what the vehicle detected
2. what the vehicle is doing
3. why the action is being taken

---

10. Explanation Component Requirements

The explanation component should support:

- clear hierarchy
- short readable text
- event-specific content
- consistent placement
- consistent timing
- accessible typography
- visual distinction from ordinary navigation information
- non-alarming presentation

The original PRD describes contextual explanation cards as part of the Journey Dashboard and emphasizes calm, transparent communication during events.

---

11. P06 — Observation State

The participant is given an opportunity to observe the autonomous response and explanation.

The observation period must be consistent across conditions.

The interface should not introduce additional information that could influence comprehension or trust differently between conditions.

---

12. P07 — Comprehension Screen

The comprehension screen measures whether the participant understood the reason for the autonomous vehicle's behaviour.

Example

Why did the vehicle slow down?

- A. It detected a pedestrian entering the crossing.
- B. The passenger requested a speed reduction.
- C. The vehicle experienced a system failure.
- D. It was approaching its destination.

The correct answer should correspond to the actual scenario.

Measurement

Record:

- selected answer
- correctness
- response time

---

13. P08 — Trust Measure

The prototype should provide the participant with a standardized trust question after the comprehension task.

Example:

How much do you trust the vehicle's decision in this situation?

A response scale should be selected before pilot testing and applied consistently.

The scale should not be changed between scenarios or participants.

---

14. P09 — Workload Measure

The experiment will use a standardized workload assessment defined in the research methodology.

The prototype should not create an unnecessarily complex custom workload scale if the final study uses a validated instrument.

If NASA-TLX is used, its final implementation and scoring procedure should be documented separately in the measurement protocol.

---

15. P10 — Trial Complete

The trial ends after the required measurements have been completed.

The system should:

- record completion
- associate responses with the trial ID
- reset the scenario state
- prepare the next trial

---

16. Experimental Condition Matrix

Prototype State| Condition A| Condition B| Condition C
Normal Journey| Same| Same| Same
Event| Same| Same| Same
Vehicle Response| Same| Same| Same
Explanation| None| Minimal| Contextual
Observation| Same| Same| Same
Comprehension| Same| Same| Same
Trust| Same| Same| Same
Workload| Same| Same| Same

The only intended experimental difference is the explanation condition.

---

17. Prototype Control Requirements

The prototype must prevent:

- accidental explanation differences
- different vehicle responses between conditions
- different scenario timing
- different question wording
- inconsistent button placement
- accidental exposure to the research hypothesis
- accidental participant access to experimental condition information

---

18. Accessibility Requirements

The experimental prototype should preserve the accessibility principles already established in the product design.

The original PRD includes:

- large text
- high contrast
- screen-reader considerations
- captions
- visual alerts
- voice operation
- simplified language
- wheelchair-related support
- language selection.

For the experimental prototype, accessibility should be implemented without changing the experimental manipulation itself.

---

19. Prototype Fidelity

The prototype should prioritize fidelity for the research-critical interaction rather than attempting to implement every product feature.

High priority

- Journey Dashboard
- event state
- autonomous response
- explanation component
- comprehension task
- trust measure
- workload measure
- trial transitions

Lower priority

- entertainment
- payment
- profile management
- complete route editing
- non-essential personalization

This is consistent with the original PRD's scope principle: when time is constrained, depth in critical journeys should take priority over shallow coverage of every feature.

---

20. Prototype Status

Requirement| Status
Experimental states defined| Complete
Explanation conditions defined| Complete
Scenario integration| Pending
Figma screen mapping| Pending
Interaction wiring| Pending
Pilot validation| Pending
Final experimental prototype| Pending

---

21. Integrity Statement

The experimental prototype is a research instrument built from the existing product concept.

It should not be interpreted as:

- a production autonomous-driving system
- a validated vehicle-control system
- a safety-certified interface
- evidence of real-world AV performance

The purpose is controlled evaluation of passenger-facing information presentation.
