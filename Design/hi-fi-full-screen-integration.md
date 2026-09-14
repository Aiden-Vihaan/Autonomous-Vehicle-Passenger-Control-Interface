High-Fidelity Full Experimental Flow Integration

1. Purpose

This document defines the integration of the high-fidelity screens into one complete experimental interaction flow.

Day 23 established the core high-fidelity journey screens.

Day 24 extends that work by connecting:

- trial initialization;
- normal journey;
- event approach;
- unexpected event;
- autonomous response;
- explanation conditions;
- comprehension;
- trust / experience;
- workload;
- trial completion.

The objective is to produce a coherent, repeatable, end-to-end experimental prototype.

---

2. Complete Experimental Flow

The intended flow is:

EXP-00 Start
    ↓
EXP-01 Practice
    ↓
EXP-02 Normal Journey
    ↓
EXP-03 Event Approach
    ↓
EXP-04 Unexpected Event
    ↓
EXP-05 Autonomous Response
    ↓
EXP-05A / EXP-05B / EXP-05C Explanation
    ↓
EXP-06 Comprehension
    ↓
EXP-07 Trust / Experience
    ↓
EXP-08 Cognitive Workload
    ↓
EXP-09 Trial Complete

After trial completion, the experiment controller determines whether another scenario remains.

If another scenario remains:

EXP-09 Trial Complete
        ↓
Next Trial
        ↓
EXP-02 Normal Journey

If no scenario remains:

EXP-09 Trial Complete
        ↓
Experiment Completion

---

3. Experimental State Integrity

The prototype must preserve the following invariant:

«The scenario, autonomous vehicle response, environmental event, and measurement sequence remain constant across explanation conditions.»

The manipulated component is the explanation presentation.

---

4. Explanation Branch

The explanation state contains three experimental variants.

Condition A — No Explanation

EXP-05 Autonomous Response
        ↓
No explanation presentation
        ↓
EXP-06 Comprehension

Condition B — Minimal Explanation

EXP-05 Autonomous Response
        ↓
Minimal explanation
        ↓
EXP-06 Comprehension

Condition C — Contextual Explanation

EXP-05 Autonomous Response
        ↓
Contextual explanation
        ↓
EXP-06 Comprehension

The branch must converge immediately after the explanation state.

---

5. Branch Convergence

All conditions must converge to the same measurement sequence:

Explanation Condition
        ↓
Passenger Observation
        ↓
EXP-06 Comprehension
        ↓
EXP-07 Trust / Experience
        ↓
EXP-08 Workload
        ↓
EXP-09 Trial Complete

There should be no condition-specific:

- measurement wording;
- measurement order;
- navigation;
- button styling;
- scoring feedback;
- completion feedback.

---

6. Scenario Integrity

Each scenario must preserve its predefined event and autonomous response.

For example:

SCN-01
Event: Pedestrian entering crossing
Vehicle response: Slowing
Explanation: Condition-dependent

The explanation condition must not change the vehicle's underlying behaviour.

The same principle applies to:

SCN-02 — Vehicle merging
SCN-03 — Obstacle ahead
SCN-04 — Road construction / lane restriction

---

7. Persistent Interface Elements

The following elements may remain consistent throughout the journey where appropriate:

- application shell;
- journey status;
- vehicle status;
- route context;
- accessibility controls;
- assistance access;
- system state indicators.

Persistent elements must not reveal the experimental condition.

---

8. Screen Transition Rules

EXP-00 → EXP-01

Start the practice interaction.

EXP-01 → EXP-02

Proceed to the standardized journey.

EXP-02 → EXP-03

Trigger the predefined event approach state.

EXP-03 → EXP-04

Present the unexpected event.

EXP-04 → EXP-05

Present the autonomous response.

EXP-05 → Explanation

Display the assigned explanation condition.

Explanation → EXP-06

Allow the participant to observe the response before comprehension measurement.

EXP-06 → EXP-07

Record comprehension response.

EXP-07 → EXP-08

Record trust/experience response.

EXP-08 → EXP-09

Record workload response.

EXP-09 → Next Trial

Initialize the next standardized scenario or complete the experiment.

---

9. Interaction Error Prevention

The prototype should prevent:

- accidental skipping of measurement screens;
- accidental double submission;
- unintended branch changes;
- navigation back into a completed trial;
- exposure of another experimental condition;
- loss of recorded responses.

Where appropriate, controls should use disabled, selected, pressed, and completed states.

---

10. Timing Integrity

The prototype should distinguish between:

- event onset;
- autonomous response onset;
- explanation onset;
- observation period;
- participant response;
- measurement response.

Timing should be recorded where required by the experimental protocol.

Example:

event_onset_time
vehicle_response_time
explanation_onset_time
explanation_duration
comprehension_response_time
trust_response_time
workload_response_time

The prototype should not introduce arbitrary timing differences between explanation conditions.

---

11. Full-Flow Figma Prototype Structure

Recommended Figma organization:

00 — Start
01 — Practice
02 — Journey
03 — Event Approach
04 — Unexpected Event
05 — Autonomous Response
05A — No Explanation
05B — Minimal Explanation
05C — Contextual Explanation
06 — Comprehension
07 — Trust
08 — Workload
09 — Trial Complete

---

12. Prototype Variables

The implementation should conceptually maintain:

participant_id
trial_id
scenario_id
condition
current_state

The experimental condition should be assigned by the experiment controller rather than manually selected by the participant.

---

13. Repeatability

A complete trial should be reproducible.

For the same:

scenario_id
condition

the prototype should produce the same:

- event;
- autonomous response;
- explanation content;
- measurement sequence;
- interaction structure.

---

14. Accessibility Integration

Accessibility must remain consistent across the complete flow.

Validate:

- text readability;
- contrast;
- touch target size;
- keyboard/focus behaviour where applicable;
- non-colour-only state communication;
- clear hierarchy;
- consistent navigation;
- readable explanation content;
- understandable measurement instructions.

---

15. High-Fidelity Integration Review

The complete flow should be reviewed in four passes.

Pass 1 — Functional

Check:

- every screen is reachable;
- every required interaction works;
- every branch converges correctly;
- no dead ends exist.

Pass 2 — Experimental

Check:

- explanation is the intended manipulation;
- scenario remains constant;
- vehicle response remains constant;
- measurement sequence remains constant;
- condition cannot leak into measurement screens.

Pass 3 — Human Factors

Check:

- event information is noticeable;
- autonomous response is understandable;
- explanation is distinguishable from system status;
- hierarchy supports rapid interpretation;
- unnecessary information is minimized.

Pass 4 — Accessibility

Check:

- text;
- contrast;
- interaction targets;
- state differentiation;
- readability;
- predictable navigation.

---

16. Version Control

Before proceeding to participant testing, record:

Prototype version:
Figma version:
Git commit:
Scenario version:
Explanation content version:
Measurement instrument version:

Any change that could affect experimental behaviour must be documented.

---

17. Definition of Done

Full-flow integration is complete when:

- [ ] EXP-00 through EXP-09 are connected.
- [ ] All three explanation conditions are reachable.
- [ ] Explanation branches converge correctly.
- [ ] Measurement screens follow every explanation condition.
- [ ] Scenario identity remains consistent.
- [ ] Autonomous response remains consistent.
- [ ] No condition leakage is present.
- [ ] Trial completion is functional.
- [ ] Multiple trials can be represented.
- [ ] Accessibility checks are completed.
- [ ] Timing requirements are documented.
- [ ] Experimental variables are mapped.
- [ ] The complete flow has been manually traversed.
- [ ] Remaining issues are documented.
- [ ] Prototype version is recorded.
