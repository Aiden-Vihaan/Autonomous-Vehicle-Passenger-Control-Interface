Experimental Prototype Flow

Project

Autonomous Vehicle Passenger Control Interface

Purpose

This document defines the interaction flow of the experimental prototype.

The prototype is designed to reproduce a controlled passenger journey in which an autonomous vehicle encounters an unexpected event and responds appropriately. The explanation presented to the passenger is manipulated across experimental conditions.

---

1. Experimental Flow

                    ┌─────────────────┐
                    │      START      │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Practice Trial  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Scenario Begins │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Normal Journey  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Unexpected Event│
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Vehicle Response│
                    └────────┬────────┘
                             ↓
               ┌─────────────┴─────────────┐
               ↓             ↓             ↓
          Condition A    Condition B    Condition C
        No Explanation    Minimal       Contextual
               │             │             │
               └─────────────┼─────────────┘
                             ↓
                    ┌─────────────────┐
                    │    Observation  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │  Comprehension  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Trust / Experience│
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │    Workload     │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Trial Complete  │
                    └─────────────────┘

---

2. State Definitions

EXP-00 — Start

Purpose:

Introduce the experimental interface and begin the study.

Content:

- study introduction
- participant instructions
- start control

No experimental information should be revealed beyond what is required for participant instructions.

---

EXP-01 — Practice Trial

Purpose:

Allow the participant to understand the interaction procedure before experimental trials begin.

The practice trial should not be used as an experimental observation unless explicitly specified in the final methodology.

---

EXP-02 — Normal Journey

Purpose:

Establish the baseline journey context.

The participant observes:

- current journey
- destination
- vehicle state
- route context

No unexpected event is present at this stage.

---

EXP-03 — Unexpected Event

Purpose:

Introduce the standardized environmental event.

Example:

Pedestrian enters crossing ahead.

The event should occur at a predefined point in the scenario.

---

EXP-04 — Autonomous Response

Purpose:

Represent the autonomous vehicle's response.

Example:

Vehicle slowing

The vehicle response must remain identical across explanation conditions.

---

3. Explanation Conditions

EXP-05-A — No Explanation

The participant observes the vehicle response without an explanatory message.

Vehicle slowing

The absence of additional explanation is intentional.

---

EXP-05-B — Minimal Explanation

The participant receives a concise causal explanation.

Slowing for pedestrian.

The explanation communicates the immediate reason for the vehicle action.

---

EXP-05-C — Contextual Explanation

The participant receives a contextual explanation.

Pedestrian entering the crossing ahead.

Slowing to maintain a safe distance.

The explanation provides both event context and response rationale.

---

4. Observation Window

After the explanation is presented, the participant receives a controlled observation period.

During this period:

- no additional explanatory information is introduced
- no unnecessary interaction is required
- the participant observes the vehicle response
- timing is recorded according to the experimental protocol

The purpose is to ensure that comprehension and experience measurements occur after exposure to the experimental condition.

---

5. Comprehension Stage

The participant answers standardized questions.

Example:

Why did the vehicle slow down?

Response options should represent plausible interpretations while maintaining consistent wording across conditions.

Potential measures:

- accuracy
- response time
- confidence, if included in the final protocol

---

6. Trust / Experience Stage

The participant provides post-event ratings.

Potential constructs:

- trust in the autonomous system
- perceived transparency
- perceived understanding
- perceived appropriateness of the vehicle response

Questions must be finalized before the main study.

---

7. Workload Stage

The participant completes the selected workload measurement.

NASA-TLX may be used according to the finalized methodology.

The workload measurement should be presented consistently after each required trial or at the frequency specified by the final study protocol.

---

8. Trial Completion

The system records the trial outcome and moves to the next scenario.

Required recorded information may include:

Participant ID
Scenario ID
Condition
Comprehension score
Response time
Trust rating
Workload score
Protocol deviation
Trial completion status

No personally identifying participant information should be stored in the public repository.

---

9. Condition Logic

The prototype should implement the following conceptual logic:

IF condition = A
    show vehicle response
    hide explanation

IF condition = B
    show vehicle response
    show minimal explanation

IF condition = C
    show vehicle response
    show contextual explanation

The underlying scenario remains unchanged.

---

10. Scenario Independence

Each scenario must be independently identifiable.

SCN-01
Pedestrian crossing

SCN-02
Vehicle merging

SCN-03
Obstacle ahead

SCN-04
Road construction

The same explanation-condition structure should be reusable across scenarios.

---

11. Prototype Validation

Before participant testing, verify:

Behaviour

- [ ] Correct scenario loads.
- [ ] Correct vehicle response occurs.
- [ ] Correct explanation condition appears.
- [ ] No explanation leakage occurs between conditions.
- [ ] Trial completion is recorded.

Timing

- [ ] Event timing is consistent.
- [ ] Explanation timing is consistent within each condition.
- [ ] Measurement begins at the intended point.

Visual consistency

- [ ] Layout remains consistent.
- [ ] Explanation condition is the principal manipulation.
- [ ] No unintended visual cue identifies the condition.
- [ ] Text length is documented.

Research integrity

- [ ] Prototype does not imply findings.
- [ ] No fabricated participant data are included.
- [ ] Pilot results are kept separate from main-study results.
- [ ] Protocol deviations are recorded.

---

12. Figma Prototype Flow

The first low-fidelity Figma flow should contain:

START
 ↓
PRACTICE
 ↓
JOURNEY
 ↓
EVENT
 ↓
RESPONSE
 ↓
EXPLANATION A/B/C
 ↓
COMPREHENSION
 ↓
TRUST
 ↓
WORKLOAD
 ↓
COMPLETE

The three explanation states should be connected as separate prototype branches.

---

13. Day 14 Prototype Rule

Do not optimize the interface for visual impressiveness at this stage.

The prototype must first answer:

«Can a participant experience the intended experimental manipulation clearly, consistently, and without unnecessary interaction?»

Visual refinement comes after this question has been satisfied.
