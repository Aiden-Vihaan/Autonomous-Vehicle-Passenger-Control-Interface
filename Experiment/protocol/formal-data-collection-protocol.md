Formal Data Collection Protocol

Project: Autonomous Vehicle Passenger Control Interface
Study: Explanation Design for Unexpected Autonomous-Vehicle Behaviour
Experimental Version: EV-1.0
Protocol Version: FDC-1.0
Milestone: Day 29
Status: Final formal data-collection protocol

---

1. Purpose

This protocol defines the formal empirical data-collection procedure for the Autonomous Vehicle Passenger Control Interface research project.

The study investigates whether different forms of passenger-facing explanations influence understanding, trust, perceived workload, and perceived understanding when an autonomous vehicle performs an unexpected action.

The experimental interface is a controlled simulation.

No conclusion regarding the actual safety, reliability, or certification of autonomous vehicles is made from this study.

---

2. Primary Research Question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

---

3. Experimental Conditions

The formal study uses three explanation conditions.

Condition| Explanation
A| No explanation
B| Minimal explanation
C| Contextual explanation

Condition A — No Explanation

The vehicle performs the represented action without an explanation card.

Condition B — Minimal Explanation

«Slowing for pedestrian.»

Condition C — Contextual Explanation

«Pedestrian entering the crossing ahead.
Slowing to maintain a safe distance.»

The underlying event remains equivalent across conditions.

---

4. Participant Role

Participants interact with the prototype as passengers in a simulated Level 4 autonomous vehicle.

Participants are not asked to operate the vehicle.

They are instructed to behave as passengers who are attempting to understand what the vehicle is doing.

The interface therefore focuses on passenger understanding rather than driving performance.

---

5. Pre-Session Procedure

Before beginning the session, the experimenter verifies:

- prototype version = EV-1.0;
- correct experimental condition mapping;
- scenario files are available;
- questionnaire is operational;
- response recording is operational;
- participant identifier is assigned;
- data directory is available;
- observation log is available;
- participant instructions are ready;
- consent procedure has been completed where applicable.

The experimenter does not begin the experimental trials until all required checks have passed.

---

6. Participant Briefing

The following standardized briefing is used:

«You will interact with a simulated passenger interface for an autonomous vehicle.

Please imagine that you are travelling as a passenger. The vehicle is responsible for navigating the journey.

During the journey, the vehicle may perform actions such as slowing down, stopping, or changing its behaviour.

Your task is to interact with the passenger interface naturally and pay attention to what happens.

After selected events, you will answer questions about your understanding and provide ratings about your experience.

There are no right or wrong opinions about the interface. We are evaluating the interface rather than your performance.

Please ask questions only if you are unable to continue because of a technical or procedural problem.»

The research hypothesis is not disclosed.

---

7. Practice Trial

A practice trial is conducted before formal trials.

The participant learns:

- how the interface is operated;
- how to respond to prompts;
- how the journey progresses;
- how comprehension questions are answered;
- how rating scales are completed.

Practice data are not included in the primary experimental analysis.

---

8. Formal Trial Procedure

Each formal trial follows this sequence:

Journey begins
      ↓
Normal autonomous travel
      ↓
Unexpected event
      ↓
Experimental explanation condition
      ↓
Vehicle response
      ↓
Passenger continues journey
      ↓
Comprehension measurement
      ↓
Trust measurement
      ↓
Workload / understanding measurement
      ↓
Trial ends

The procedure is kept consistent across conditions.

---

9. Experimenter Behaviour

The experimenter must not:

- explain why the vehicle performed an action;
- indicate which condition is being tested;
- suggest that one explanation is better;
- correct a participant's answer during the experiment;
- encourage a particular trust rating;
- provide additional information that is not part of the protocol.

The experimenter may intervene when:

- the participant cannot continue because of a technical failure;
- a safety or accessibility problem occurs;
- the participant asks to stop;
- continuing would compromise participant welfare or study integrity.

All material interventions are recorded.

---

10. Condition Verification

Before each experimental trial, the experimenter verifies:

Scenario ID
      +
Condition ID
      +
Expected explanation

The displayed interface must match the intended condition.

A condition mismatch is recorded as a protocol deviation.

---

11. Comprehension Measurement

After the relevant event, the participant answers predefined comprehension questions.

The questions evaluate:

Event recognition

What happened around the vehicle?

Vehicle response

What did the vehicle do?

Reason

Why did the vehicle perform that action?

Responses are coded using the predefined scoring scheme.

The scoring scheme is fixed before formal analysis.

---

12. Trust Measurement

Following the relevant trial, participants provide a trust rating using the predefined questionnaire scale.

The rating represents perceived trust in the automated system/interface presented during the scenario.

It is not interpreted as an objective measure of system reliability.

---

13. Workload Measurement

Participants complete the predefined workload assessment.

The workload measure represents subjective perceived task demand.

No physiological workload measure is implied.

---

14. Perceived Understanding

Participants provide a rating of how well they believe they understood the reason for the vehicle's behaviour.

This is retained as a separate variable from objective comprehension.

---

15. Response-Time Measurement

Where the prototype supports automatic timestamps:

Prompt displayed
      ↓
Timer starts
      ↓
Participant responds
      ↓
Response submitted
      ↓
Timer stops

If reliable automatic timing is unavailable, the response-time field remains unavailable.

Response times are never reconstructed from memory.

---

16. Observation Procedure

The experimenter may record structured observations concerning:

- hesitation;
- interaction errors;
- navigation problems;
- confusion;
- requests for clarification;
- explanation dismissal;
- technical problems;
- accessibility difficulties;
- protocol deviations.

Observations must distinguish what was actually seen from interpretation.

Example:

Acceptable:

«Participant paused approximately several seconds before selecting the response.»

Not acceptable without evidence:

«Participant was cognitively overloaded.»

The second statement is an interpretation rather than a direct observation.

---

17. Data Recording

Each formal trial receives a unique trial identifier.

The dataset records:

- anonymous participant ID;
- trial ID;
- scenario ID;
- explanation condition;
- comprehension result;
- response time where available;
- trust rating;
- workload rating;
- perceived understanding;
- task completion;
- interaction errors;
- protocol deviations;
- relevant qualitative observations.

---

18. Participant Anonymity

The analytical dataset uses participant identifiers rather than names.

Personal identifying information is not required for the primary analysis.

If a separate consent or contact record is required, it must be stored separately from the analytical dataset.

---

19. Missing Data

If a measurement cannot be collected:

- leave the measurement missing;
- record the reason where known;
- do not estimate the value;
- do not replace it with an assumed score.

Missing data will be reviewed during analysis.

---

20. Technical Failures

If the prototype fails:

1. pause the trial;
2. identify the failure;
3. record the affected trial;
4. determine whether the trial can legitimately continue;
5. restart only according to the predefined procedure;
6. document any repeated trial.

Technical failures are not converted into participant errors.

---

21. Participant Withdrawal

Participants may stop participation at any time.

If a participant withdraws:

- stop the session;
- record the withdrawal;
- preserve only data that may ethically and procedurally be retained;
- do not attempt to persuade the participant to continue.

---

22. Accessibility

Participants who require an accessibility accommodation should receive the accommodation defined by the study procedure.

Accessibility-related issues are documented separately from participant performance.

An accessibility barrier is not automatically classified as an interaction error.

---

23. End-of-Session Procedure

After the final trial:

1. complete final questionnaire items;
2. conduct the debrief;
3. invite optional qualitative feedback;
4. check the data record for completeness;
5. record protocol deviations;
6. save the session data;
7. assign the session status.

Possible session statuses:

COMPLETE
PARTIAL
WITHDRAWN
TECHNICAL FAILURE
INVALIDATED

Invalidation must always have a documented reason.

---

24. Data Quality Check

Immediately after each session, verify:

- participant ID is present;
- trial IDs are unique;
- condition labels are correct;
- responses are recorded;
- missing values are identifiable;
- technical failures are documented;
- deviations are documented;
- qualitative notes are distinguishable from quantitative data.

No analytical conclusions are made during this quality check.

---

25. Data Storage

The analytical dataset is stored separately from:

- participant-identifying information;
- consent documentation;
- raw prototype files;
- design files;
- experimenter notes containing identifying information.

The repository should contain only information appropriate for the project and its intended sharing level.

---

26. Formal Data-Collection Status

The project has now completed its methodological preparation.

Research question              COMPLETE
Experimental conditions        FROZEN
Protocol                       FINAL
Measurement framework          FINAL
Data dictionary                FINAL
Collection procedure            FINAL
Analysis structure             FINAL
Formal empirical results        NOT YET CLAIMED

This distinction is intentional.

The project is methodologically ready for formal empirical data collection.

---

27. Research Integrity Statement

No participant result, statistical finding, or qualitative observation is entered into the project unless it is based on an actual study observation.

The project therefore maintains a strict separation between:

- designed methodology;
- pilot observations;
- formal empirical evidence;
- interpretation.

---

28. Version

Protocol: FDC-1.0
Experimental build: EV-1.0
Milestone: Day 29
Status: Ready for formal data collection
