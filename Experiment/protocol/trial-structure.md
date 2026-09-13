Experimental Trial Structure

Project: Autonomous Vehicle Passenger Control Interface
Status: Trial structure v1
Date: 23 September 2026

---

1. Objective

This document defines the internal structure of one experimental trial.

The purpose is to ensure that every trial follows a predictable sequence and that the explanation condition is the principal experimental difference.

---

2. Trial State Machine

TRIAL START
    |
    v
NORMAL JOURNEY
    |
    v
EVENT APPROACH
    |
    v
UNEXPECTED EVENT
    |
    v
AUTONOMOUS RESPONSE
    |
    v
EXPLANATION PRESENTATION
    |
    v
PARTICIPANT OBSERVATION
    |
    v
COMPREHENSION TASK
    |
    v
TRUST / EXPERIENCE MEASURE
    |
    v
TRIAL COMPLETE

---

3. State Definitions

State 1 — Trial Start

The system initializes the scenario.

Recorded:

- participant ID;
- trial ID;
- scenario ID;
- explanation condition;
- timestamp.

---

State 2 — Normal Journey

The participant observes normal autonomous-vehicle operation.

No experimental event occurs during this stage.

The purpose is to establish a baseline context before the unexpected event.

---

State 3 — Event Approach

The environmental situation begins to change.

The participant should have sufficient context to interpret the subsequent vehicle behaviour.

---

State 4 — Unexpected Event

The relevant event occurs.

Example:

«Pedestrian enters crossing.»

The event must be consistent across the explanation conditions.

---

State 5 — Autonomous Response

The vehicle performs the predetermined response.

Example:

«Vehicle slows.»

The vehicle response should not change according to explanation condition.

---

State 6 — Explanation Presentation

The passenger interface presents the assigned explanation condition.

Example:

No explanation

«Vehicle slowing.»

Minimal

«Slowing for pedestrian.»

Contextual

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

---

State 7 — Participant Observation

The participant observes the resulting interface state.

If interaction is required, the interaction task begins according to the predefined protocol.

---

State 8 — Comprehension Task

The participant answers the scenario-specific comprehension question.

Example:

«Why did the vehicle slow down?»

The response is recorded.

---

State 9 — Trust / Experience Measure

The participant provides the required subjective rating.

The exact measurement schedule will be finalized after selecting the validated instrument.

---

State 10 — Trial Complete

The trial data are stored.

The next trial begins after the predefined transition.

---

4. Required Trial Data

Each trial should record, where applicable:

Field| Description
Participant ID| Anonymous study identifier
Trial ID| Unique trial identifier
Scenario ID| Scenario used
Explanation condition| A / B / C
Scenario order| Position within session
Condition order| Position of explanation condition
Comprehension response| Participant response
Comprehension score| Scored response
Trust measure| Selected trust measure
Workload measure| Selected workload measure
Response time| If collected
Interaction errors| If applicable
Completion status| Complete / incomplete
Notes| Protocol deviations

---

5. Timing Requirements

Exact timings should be determined during prototype development.

The following timing relationships should remain controlled:

- event onset;
- vehicle response;
- explanation onset;
- explanation visibility;
- question onset;
- response window.

Timing should not vary unintentionally between explanation conditions.

---

6. Experimental Control

The following should remain constant where possible:

- scenario;
- environmental event;
- vehicle response;
- interface layout;
- visual hierarchy;
- question;
- interaction method;
- task instructions.

The explanation content is the primary manipulation.

---

7. Trial Completion Criteria

A trial is complete when:

1. the scenario has been presented;
2. the participant has encountered the experimental event;
3. the explanation has been presented where applicable;
4. the required comprehension response has been recorded;
5. required subjective measures have been completed.

Incomplete trials should be documented rather than silently removed.

---

8. Protocol Deviations

Any deviation from the predefined trial structure should be recorded.

Examples:

- technical failure;
- participant missed the event;
- explanation failed to display;
- audio failed;
- participant requested clarification;
- trial restarted.

Protocol deviations should be considered during data cleaning and analysis.

---

9. Design Principle

The experiment should separate:

What the autonomous vehicle does

from

What the passenger interface tells the passenger about what it does.

This separation is central to the validity of the experimental manipulation.

---

Status

Trial structure: v1
Next step: Define exact scenario scripts and participant-facing instructions.
