Experimental Architecture Freeze

Purpose

This document formally freezes the interaction architecture of the experimental prototype before high-fidelity visual design begins.

The purpose of the freeze is to ensure that visual refinement, component styling, animation, typography, and interaction polish do not unintentionally alter the experimental structure established during the low-fidelity phase.

The experimental prototype must remain a controlled research instrument rather than becoming only a visual demonstration.

---

1. Experimental Architecture

The experimental prototype follows this sequence:

Scenario Initialization
        ↓
Normal Journey
        ↓
Event Approach
        ↓
Unexpected Event
        ↓
Autonomous Response
        ↓
Explanation Condition
        ↓
Passenger Observation
        ↓
Comprehension
        ↓
Trust / Experience Measure
        ↓
Workload Measure
        ↓
Trial Completion

The three primary explanation conditions are:

Condition| Explanation
A| No explanation
B| Minimal explanation
C| Contextual explanation

The autonomous vehicle behaviour and scenario event must remain equivalent across the three explanation conditions.

---

2. Frozen Experimental Variables

The following elements are frozen before high-fidelity design begins.

2.1 Scenario

The event presented to the participant must remain the same across explanation conditions within a trial set.

Examples include:

- pedestrian crossing;
- vehicle merging;
- obstacle ahead;
- road construction or lane restriction.

The final scenario set must be selected before the main study.

---

2.2 Autonomous Response

The vehicle response must not change based on explanation condition.

For example:

Unexpected Event
        ↓
Vehicle Detects Event
        ↓
Vehicle Slows
        ↓
Explanation Condition Changes

Not:

Explanation Condition
        ↓
Different Vehicle Behaviour

The explanation is the experimental manipulation, not the autonomous driving behaviour.

---

2.3 Explanation Conditions

Condition A — No Explanation

No explanatory message is presented following the autonomous response.

The passenger can still observe the vehicle state and journey information required by the baseline interface.

Condition B — Minimal Explanation

The system provides a concise explanation of the immediate reason for the autonomous action.

Example structure:

«Slowing for pedestrian.»

Condition C — Contextual Explanation

The system provides additional contextual information explaining both the event and the resulting action.

Example structure:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

The exact wording should be finalized during the high-fidelity content-design phase without changing the intended information level of each condition.

---

3. Frozen Trial Structure

Every experimental trial should follow the same fundamental structure:

1. Trial begins.
2. Participant enters the journey.
3. Normal journey state is presented.
4. Environmental event occurs.
5. Autonomous response occurs.
6. Assigned explanation condition is presented.
7. Participant observes the interface and vehicle response.
8. Comprehension measure is presented.
9. Trust / experience measure is presented.
10. Workload measure is presented where applicable.
11. Trial is completed.
12. Trial data are recorded.

No additional interaction should be introduced solely for one explanation condition.

---

4. Frozen Measurement Sequence

The measurement sequence remains separate from the explanation manipulation.

Primary measures:

- comprehension;
- trust;
- cognitive workload.

Secondary measures:

- situation awareness;
- interaction performance;
- perceived transparency;
- perceived usability;
- response time.

The measurement interface must not reveal which explanation condition is being evaluated.

---

5. Frozen State Model

NORMAL
  ↓
EVENT_APPROACH
  ↓
UNEXPECTED_EVENT
  ↓
AUTONOMOUS_RESPONSE
  ↓
EXPLANATION
  ↓
OBSERVATION
  ↓
COMPREHENSION
  ↓
EXPERIENCE_MEASURE
  ↓
WORKLOAD_MEASURE
  ↓
TRIAL_COMPLETE

The explanation state contains one of:

EXPLANATION_NONE
EXPLANATION_MINIMAL
EXPLANATION_CONTEXTUAL

---

6. High-Fidelity Design Boundary

High-fidelity design may change:

- typography;
- spacing;
- visual hierarchy;
- icons;
- component styling;
- layout refinement;
- visual states;
- motion used for clarity;
- accessibility implementation;
- design-token application;
- visual polish.

High-fidelity design must not change:

- experimental conditions;
- scenario events;
- autonomous responses;
- trial sequence;
- measurement sequence;
- condition assignment logic;
- required information level;
- participant task;
- scoring logic.

---

7. Accessibility Requirements

Accessibility refinement should improve the interface without changing the experimental manipulation.

The high-fidelity prototype should consider:

- readable typography;
- sufficient contrast;
- clear hierarchy;
- understandable status indicators;
- non-colour-only communication;
- touch-target size;
- readable explanation content;
- consistent component behaviour;
- reduced dependence on visual decoration;
- clear error prevention.

Accessibility changes should be documented when they affect interaction behaviour.

---

8. Experimental Integrity Rule

Every high-fidelity design change should be evaluated using the following question:

«Does this change alter what the participant sees, understands, or does in a way that could affect the independent variable or dependent measures?»

If yes, the change must be reviewed before implementation.

If no, the change may proceed as a visual or usability refinement.

---

9. Figma Freeze Checklist

Before beginning high-fidelity design:

- [ ] Experimental state sequence is complete.
- [ ] Three explanation conditions are implemented conceptually.
- [ ] Scenario structure is defined.
- [ ] Autonomous response is identical across conditions.
- [ ] Measurement sequence is defined.
- [ ] Condition branching is documented.
- [ ] Condition isolation has been checked.
- [ ] Low-fidelity prototype has been walked through.
- [ ] Known usability issues have been recorded.
- [ ] No unresolved P0 experimental-integrity issues remain.
- [ ] Figma component structure is documented.
- [ ] High-fidelity visual work can begin without changing research logic.

---

10. Version

Architecture Version: v1.0
Status: Frozen for high-fidelity transition

Future changes to the architecture require explicit documentation and revalidation.

---

11. Research Integrity Statement

This architecture represents a controlled prototype design for studying passenger interaction with autonomous-vehicle explanations.

It does not constitute validation of a production autonomous-vehicle system, safety certification, or real-world vehicle behaviour.

No empirical conclusion should be drawn from the prototype until participant data have been collected and analysed.

---

12. Next Step

The next phase is high-fidelity transition.

The experimental architecture remains fixed while the interface is progressively refined into a visually coherent, accessible, and portfolio-ready autonomous-vehicle passenger HMI.
