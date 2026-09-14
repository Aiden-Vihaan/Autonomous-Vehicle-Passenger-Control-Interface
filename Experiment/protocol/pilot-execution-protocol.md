Pilot Execution Protocol

Project: Autonomous Vehicle Passenger Control Interface
Research Focus: Explanations for Unexpected Autonomous-Vehicle Behaviour
Research Phase: Pilot Execution
Day: 27
Status: Pilot Execution Protocol Complete

---

1. Purpose

Day 27 marks the transition from pilot preparation to pilot execution.

The purpose of the pilot is to evaluate whether the experimental prototype and research procedure can be executed consistently before formal participant data collection.

The pilot is designed to identify:

- technical problems;
- procedural problems;
- unclear participant instructions;
- ambiguous interface communication;
- measurement problems;
- accessibility issues;
- timing problems;
- unintended differences between experimental conditions;
- situations requiring experimenter intervention.

The pilot is not treated as formal hypothesis-testing data.

---

2. Research Question

The pilot supports the preparation of the following primary research question:

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

The pilot itself does not determine the answer to this question.

Its purpose is to determine whether the experimental procedure is sufficiently reliable to investigate it.

---

3. Experimental Conditions

The prototype contains three explanation conditions.

Condition A — No Explanation

The autonomous vehicle performs the predefined response without presenting an explanatory rationale.

Condition B — Minimal Explanation

The system presents a short explanation describing the immediate reason for the vehicle's behaviour.

Example:

«“Slowing for pedestrian.”»

Condition C — Contextual Explanation

The system presents a more informative explanation containing relevant context and the reason for the vehicle's response.

Example:

«“Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.”»

---

4. Controlled Variables

The following elements remain constant across explanation conditions:

- scenario;
- unexpected event;
- autonomous vehicle response;
- scenario progression;
- passenger task;
- comprehension procedure;
- trust/experience assessment;
- workload assessment;
- general interface structure.

The intended experimental manipulation is the presentation of explanation information.

No other interface change should intentionally distinguish the conditions.

---

5. Pilot Session Configuration

The pilot uses:

- the current high-fidelity experimental prototype;
- the predefined experimental scenarios;
- standardized participant instructions;
- standardized measurement sequence;
- pilot observation log;
- timing record;
- protocol deviation record.

The exact prototype version used during the pilot must be recorded in the repository so that subsequent changes remain traceable.

---

6. Pre-Pilot Verification

Before the participant begins, the experimenter verifies:

Prototype

- [x] Prototype opens successfully.
- [x] Required screens are available.
- [x] Navigation is functional.
- [x] Scenario sequence is defined.
- [x] Measurement screens are available.
- [x] Completion flow is available.

Experimental Manipulation

- [x] No-explanation condition is defined.
- [x] Minimal-explanation condition is defined.
- [x] Contextual-explanation condition is defined.
- [x] Autonomous response remains conceptually constant across conditions.
- [x] Explanation content is explicitly documented.

Procedure

- [x] Participant instructions are prepared.
- [x] Practice procedure is prepared.
- [x] Comprehension assessment is prepared.
- [x] Trust/experience assessment is prepared.
- [x] Workload assessment is prepared.
- [x] Debriefing procedure is prepared.

---

7. Participant Briefing

The participant is introduced to the interaction as an autonomous-vehicle passenger.

The participant is instructed to:

1. behave naturally as a passenger;
2. observe the autonomous vehicle's behaviour;
3. pay attention to unexpected events;
4. consider the information presented by the interface;
5. answer questions independently;
6. provide honest ratings;
7. request help only when a technical or procedural problem prevents continuation.

The research hypothesis is not disclosed.

The participant is not told that any explanation condition is expected to be superior.

---

8. Practice Interaction

A practice interaction is completed before experimental trials.

The practice establishes familiarity with:

- interface navigation;
- event observation;
- comprehension questions;
- trust/experience ratings;
- workload assessment.

Practice responses are excluded from formal experimental analysis.

---

9. Experimental Trial Procedure

Each experimental trial follows the predefined architecture:

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
Observation
        ↓
Comprehension
        ↓
Trust / Experience
        ↓
Workload
        ↓
Trial Completion

The experimenter follows this sequence consistently.

---

10. Experimenter Behaviour

The experimenter should remain neutral throughout the session.

The experimenter must not:

- suggest that an explanation is correct or incorrect;
- encourage a particular trust rating;
- explain why the vehicle behaved in a particular way;
- indicate which condition is expected to perform better;
- correct participant answers;
- reinterpret participant responses.

If a participant encounters a technical problem, the experimenter may provide the minimum intervention necessary to restore the procedure.

Any such intervention must be documented.

---

11. Observation Protocol

The experimenter records observations in five categories.

A. Comprehension

Record whether the participant:

- understands what happened;
- understands the vehicle's response;
- understands the explanation;
- asks for clarification;
- misinterprets the event.

B. Interaction

Record:

- navigation difficulty;
- hesitation;
- incorrect interaction;
- repeated actions;
- difficulty locating controls;
- unexpected interaction paths.

C. Communication

Record:

- unclear terminology;
- insufficient information;
- excessive information;
- ambiguous system state;
- unclear explanation;
- difficulty distinguishing system status from explanation.

D. Measurement

Record:

- difficulty answering comprehension questions;
- uncertainty about rating scales;
- confusion during workload assessment;
- excessive interruption between trials.

E. Technical

Record:

- loading failure;
- interaction failure;
- incorrect state transition;
- missing content;
- unexpected visual behaviour;
- prototype instability.

---

12. Timing Observation

Timing is observed primarily to identify procedural inefficiencies.

Relevant timing points include:

- trial start;
- unexpected event;
- autonomous response;
- explanation presentation;
- comprehension assessment;
- trust/experience assessment;
- workload assessment;
- trial completion.

Timing observations are not interpreted as formal performance results unless the final study protocol explicitly defines them as dependent variables.

---

13. Explanation Integrity Check

For every condition, verify:

No Explanation

The participant receives the autonomous response without an intentional explanatory rationale.

Minimal Explanation

The participant receives only the predefined concise explanation.

Contextual Explanation

The participant receives the predefined contextual explanation.

The experimenter must verify that no additional information accidentally differentiates the conditions.

---

14. Accessibility Verification

During the pilot, the experimenter verifies:

- readable text;
- clear hierarchy;
- adequate interaction target size;
- understandable warning states;
- consistent icon use;
- information not dependent solely on colour;
- clear distinction between normal and unexpected states;
- concise critical information.

Any accessibility issue capable of affecting comprehension or task completion is treated as a research-relevant issue rather than merely a visual-design issue.

---

15. Protocol Deviations

A protocol deviation is recorded whenever the actual session differs from the predefined procedure.

Examples include:

- experimenter providing unplanned clarification;
- participant skipping a required screen;
- technical interruption;
- incorrect scenario presentation;
- incorrect explanation condition;
- measurement screen failure.

A deviation does not automatically invalidate the pilot.

Its potential impact on the formal study must be assessed separately.

---

16. Issue Severity

Critical

The issue changes the experimental manipulation, prevents completion, or makes the procedure unusable.

Required action: Fix and repeat the affected pilot procedure.

Major

The issue may substantially influence participant understanding, behaviour, or measurement.

Required action: Correct before formal data collection and determine whether re-piloting is necessary.

Minor

The issue affects usability or efficiency but is unlikely to alter the experimental variables.

Required action: Correct where practical and document.

Cosmetic

The issue concerns presentation without meaningful methodological impact.

Required action: Correct during normal design refinement.

---

17. Pilot Decision Rule

Following execution, the project enters one of four states:

Pilot Complete
      ↓
Review Observations
      ↓
 ┌───────────────┬────────────────────┬──────────────────┐
 ↓               ↓                    ↓                  ↓
Proceed       Minor Revision     Revise + Re-Pilot    Redesign

Proceed

No critical methodological problems are identified.

Minor Revision

Only low-impact issues are identified.

Revise + Re-Pilot

A problem could influence experimental validity.

Redesign

The experimental manipulation or procedure requires substantial modification.

---

18. Research Integrity

The pilot does not provide evidence that one explanation condition is superior.

Statements such as:

- “participants trusted contextual explanations more”;
- “minimal explanations reduced workload”;
- “participants understood the vehicle better with explanations”;

must not be made unless supported by formal empirical data.

Pilot observations are used only to improve the study procedure and prototype.

---

19. Data Handling

No personally identifiable participant information will be committed to GitHub.

Pilot data and observations are stored separately from public-facing project documentation.

Any public research artifact will use anonymized information.

---

20. Day 27 Completion Criteria

Day 27 is considered procedurally complete when:

- the pilot session has been conducted according to the protocol;
- observations have been recorded;
- technical issues have been documented;
- protocol deviations have been documented;
- explanation-condition integrity has been checked;
- accessibility observations have been recorded;
- measurement procedure has been reviewed;
- the pilot decision has been documented;
- any required revisions have been identified.

Day 27 status: PILOT EXECUTION STAGE COMPLETE.

Next stage: Incorporate evidence-based pilot observations and determine whether the prototype is ready for formal data collection.
