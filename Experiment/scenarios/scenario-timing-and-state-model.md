Scenario Timing and State Model

1. Purpose

This document defines the standardized interaction sequence and state model used by the experimental prototype.

The purpose is to ensure that each experimental trial follows a reproducible sequence and that explanation timing is controlled across conditions.

---

2. Trial State Model

Each trial follows the following conceptual state sequence:

┌──────────────┐
│ NORMAL TRAVEL│
└──────┬───────┘
       │
       ▼
┌────────────────┐
│ EVENT APPROACH │
└───────┬────────┘
        │
        ▼
┌──────────────────┐
│ UNEXPECTED EVENT │
└────────┬─────────┘
         │
         ▼
┌────────────────────┐
│ AUTONOMOUS RESPONSE│
└─────────┬──────────┘
          │
          ▼
┌─────────────────────┐
│ EXPLANATION DISPLAY │
└──────────┬──────────┘
           │
           ▼
┌────────────────────┐
│ PASSENGER OBSERVES │
└──────────┬─────────┘
           │
           ▼
┌──────────────────────┐
│ COMPREHENSION TASK   │
└──────────┬───────────┘
           │
           ▼
┌────────────────────┐
│ EXPERIENCE MEASURES│
└──────────┬─────────┘
           │
           ▼
┌────────────────┐
│ TRIAL COMPLETE │
└────────────────┘

---

3. Standard Trial Sequence

State 1 — Normal Travel

The participant observes the autonomous vehicle travelling normally.

Purpose:

- establish baseline context
- familiarize the participant with the interface
- prevent the unexpected event from occurring immediately

---

State 2 — Event Approach

The environmental event begins to develop.

Examples:

- pedestrian approaches crossing
- vehicle begins merging
- obstacle becomes relevant
- road construction becomes visible

The timing should be standardized for all participants.

---

State 3 — Unexpected Event

The event becomes sufficiently relevant for the autonomous vehicle to change its behaviour.

The participant should be able to perceive that the vehicle has changed behaviour.

---

State 4 — Autonomous Response

The autonomous vehicle performs the predefined response.

Examples:

- slow down
- increase following distance
- adjust trajectory
- modify speed and road position

The response remains identical across explanation conditions.

---

State 5 — Explanation

The explanation condition is presented.

Condition A

No explicit explanation.

Condition B

Minimal explanation.

Condition C

Contextual explanation.

The explanation should appear at a standardized point relative to the autonomous response.

---

State 6 — Observation

The participant observes the vehicle's response and explanation.

The observation period should be long enough to understand the interface without introducing unnecessary variation.

---

State 7 — Comprehension Task

The participant answers a standardized question concerning the vehicle's behaviour.

Example:

«Why did the vehicle slow down?»

Possible response options may include:

- The vehicle detected a pedestrian.
- The vehicle was following its normal route.
- The vehicle detected a system failure.
- The vehicle was responding to the passenger's request.

The exact question and options should be finalized before pilot testing.

---

State 8 — Experience Measures

The participant provides the required subjective responses.

Candidate measures include:

- trust
- perceived transparency
- perceived understanding
- workload
- usability

The final questionnaire structure should be defined before the main experiment.

---

State 9 — Trial Complete

Trial data are recorded and the participant proceeds to the next trial.

---

4. Timing Framework

The following timing model is a starting specification rather than a finalized timing schedule.

Phase| Purpose| Timing Status
Baseline travel| Establish normal state| To be calibrated
Event approach| Establish context| To be calibrated
Event onset| Trigger AV response| Fixed
AV response| Present behaviour| Fixed
Explanation| Manipulation| Fixed relative to response
Observation| Allow interpretation| To be calibrated
Comprehension| Measure understanding| Participant-controlled
Subjective measure| Measure experience| Participant-controlled

Exact durations should be finalized after prototype implementation and pilot testing.

---

5. Experimental Invariance

The following must remain invariant between explanation conditions:

- scenario
- environmental event
- vehicle response
- route
- approximate event timing
- interface layout
- primary visual environment
- passenger task
- comprehension question
- response interface

The following may vary:

- explanation presence
- explanation content
- explanation specificity

---

6. Explanation Timing Principle

The primary experiment should initially manipulate explanation content/presence, rather than simultaneously manipulating multiple factors.

This reduces the risk of confounding:

Explanation Presence
        +
Explanation Specificity
        +
Explanation Timing
        +
Explanation Modality

A single primary manipulation allows clearer interpretation of the experimental result.

Timing should therefore remain constant across Conditions B and C.

---

7. Trial Data Synchronization

Each trial should contain timestamps or ordered event markers for:

TRIAL_START
EVENT_APPROACH
EVENT_ONSET
AV_RESPONSE
EXPLANATION_PRESENTED
OBSERVATION_COMPLETE
COMPREHENSION_START
COMPREHENSION_RESPONSE
SUBJECTIVE_MEASURE_START
TRIAL_END

Where precise timestamps are unavailable in the prototype, ordered event markers should still be recorded.

---

8. State-Machine Integrity

The prototype should prevent accidental differences between conditions.

The ideal implementation is:

Scenario
   │
   ▼
Same Environment
   │
   ▼
Same Event
   │
   ▼
Same AV Response
   │
   ├───────────────┐
   │               │
   ▼               ▼
Condition A     Condition B/C
No explanation  Explanation
   │               │
   └───────┬───────┘
           ▼
     Same Evaluation

This structure makes the explanation condition the principal experimental manipulation.

---

9. Pilot Validation Criteria

Before participant data are collected, pilot testing should verify:

- scenario is understandable
- event is noticeable
- vehicle response is clearly perceivable
- explanation appears at the intended time
- explanation wording is understandable
- no accidental condition differences exist
- comprehension questions are answerable
- response controls function correctly
- trial duration is reasonable
- no obvious technical errors occur

Pilot observations should be recorded in the research log.

---

10. Change Control

Any change to:

- scenario wording
- explanation wording
- event timing
- vehicle behaviour
- question wording
- interface layout
- experimental condition

should be recorded in:

If a change occurs after pilot testing, its potential effect on comparability should be documented.

---

11. Current Status

Status: Preliminary specification

The timing values and final scenario count are not yet locked.

They will be finalized after:

1. prototype implementation
2. internal walkthrough
3. pilot testing
4. protocol review

This prevents arbitrary timing decisions from being presented as empirically validated parameters.
