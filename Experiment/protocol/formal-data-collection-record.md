Day 30 — Formal Data Collection Record

Project: Autonomous Vehicle Passenger Control Interface
Research Phase: Formal Empirical Data Collection
Experimental Version: EV-1.0
Day: 30
Status: Formal data-collection phase initiated
Primary Research Question:

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

---

1. Purpose

Day 30 marks the transition from experimental preparation to the formal data-collection phase of the project.

The experimental design, protocol, measurement framework, data dictionary, and dataset structure were established before formal data collection. The purpose of this phase is to collect observations using the frozen experimental version without changing the independent variable, participant instructions, scenario structure, interface hierarchy, or measurement definitions during collection.

The project distinguishes clearly between:

- pilot observations,
- formal empirical observations,
- technical/procedural issues,
- and researcher interpretation.

No empirical result is treated as established until it is supported by recorded data and the predefined analysis procedure.

---

2. Experimental Configuration

Experimental Version

EV-1.0

The following elements are frozen for formal collection:

- explanation-condition definitions;
- scenario structure;
- unexpected-event sequence;
- passenger role;
- interface environment;
- visual hierarchy;
- interaction structure;
- participant instructions;
- comprehension measurement;
- trust measurement;
- workload measurement;
- perceived-understanding measurement;
- response-time measurement;
- task-success criteria;
- error coding;
- protocol-deviation coding;
- technical-issue coding.

Any change that could alter the experimental manipulation or dependent measures requires documented review before continued formal collection.

---

3. Independent Variable

The primary manipulated variable is explanation condition.

Condition| Description
A| No explanation
B| Minimal explanation
C| Contextual explanation

Condition A — No Explanation

The autonomous vehicle communicates the relevant vehicle state without providing an explanatory rationale.

Condition B — Minimal Explanation

The interface provides a concise explanation identifying the immediate event.

Example:

«“Slowing for pedestrian.”»

Condition C — Contextual Explanation

The interface provides a concise contextual explanation identifying the event and the reason for the vehicle response.

Example:

«“Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.”»

The examples above describe the experimental manipulation and do not constitute empirical findings.

---

4. Primary Dependent Variable

Comprehension

The primary outcome is the passenger's ability to correctly understand the autonomous vehicle's behaviour.

Comprehension is recorded using the predefined comprehension measure.

The primary analysis will therefore focus on whether explanation condition is associated with differences in comprehension.

---

5. Secondary Measures

The following variables are collected as secondary outcomes:

- response time;
- trust score;
- workload score;
- perceived understanding;
- task success;
- interaction errors;
- protocol deviations;
- technical issues;
- qualitative observations.

These measures are interpreted according to the analysis plan established before formal data collection.

---

6. Formal Collection Procedure

Each formal session follows the standardized sequence below.

Step 1 — Session Preparation

Before the session:

1. Verify that EV-1.0 is being used.
2. Verify that the intended scenario version is loaded.
3. Verify the explanation condition.
4. Verify that measurement instruments are available.
5. Verify that the recording structure is ready.
6. Confirm that no experimental manipulation has been unintentionally changed.

Step 2 — Participant Briefing

The participant receives the standardized instructions defined in the formal experimental protocol.

The participant is informed that they should behave as a passenger using an autonomous vehicle.

The participant is not informed of the specific hypothesis concerning explanation conditions.

Step 3 — Practice

A practice interaction is completed before formal trials.

Practice data are not treated as formal experimental observations unless explicitly designated otherwise by the protocol.

Step 4 — Formal Trials

The participant completes the predefined experimental scenarios.

For each trial:

1. the scenario begins from the defined baseline state;
2. the autonomous vehicle encounters the predefined unexpected event;
3. the relevant explanation condition is presented;
4. the participant interprets the vehicle's behaviour;
5. comprehension is measured;
6. trust is measured;
7. workload is measured;
8. perceived understanding is measured;
9. response-time information is recorded where applicable;
10. task success and interaction errors are recorded;
11. protocol deviations and technical issues are documented separately.

Step 5 — Session Completion

At the end of the session:

- required measurements are checked for completeness;
- technical problems are documented;
- participant withdrawal or interruption is recorded where applicable;
- the participant receives the standardized debrief;
- the dataset entry is checked for missing or inconsistent fields.

---

7. Data Recording Standard

Each formal observation receives a unique "participant_id" and "trial_id".

The predefined data structure is:

Variable| Purpose
"participant_id"| Anonymous participant identifier
"trial_id"| Unique trial identifier
"scenario_id"| Scenario identifier
"condition"| Explanation condition A/B/C
"comprehension_score"| Continuous/defined comprehension measure
"comprehension_correct"| Correctness indicator
"response_time_ms"| Response time in milliseconds
"trust_score"| Trust measurement
"workload_score"| Workload measurement
"perceived_understanding"| Perceived understanding measure
"task_success"| Task-success indicator
"interaction_error"| Interaction-error indicator
"protocol_deviation"| Protocol-deviation record
"technical_issue"| Technical-issue record
"qualitative_note"| Structured qualitative observation

---

8. Missing Data

Missing observations are recorded as:

"NA"

Missing values are not replaced with estimated values during data collection.

The reason for missingness is documented whenever known.

Examples include:

- participant skipped an item;
- technical failure;
- trial interruption;
- participant withdrawal;
- measurement unavailable;
- protocol deviation.

---

9. Experimental Integrity Rules

The following rules apply throughout formal collection:

1. No participant responses are fabricated.
2. No missing values are silently replaced.
3. No participant is coached toward a desired response.
4. No explanation condition is altered during a trial.
5. The explanation wording remains consistent with EV-1.0.
6. Pilot observations are not presented as formal findings.
7. Technical problems are not converted into participant behaviour.
8. Researcher impressions are not treated as quantitative results.
9. Null or unexpected findings will be retained.
10. Analysis will follow the predefined analysis plan.
11. Any deviation from the protocol is documented.
12. Changes to the experimental manipulation require version control and review.

---

10. Quality-Control Check

Before a dataset is considered analysis-ready, the following checks are required:

- [ ] Unique participant identifiers
- [ ] Unique trial identifiers
- [ ] Valid scenario identifiers
- [ ] Valid explanation-condition coding
- [ ] No impossible condition labels
- [ ] No accidental duplicate trials
- [ ] Missing values explicitly coded
- [ ] Technical issues separated from participant responses
- [ ] Protocol deviations documented
- [ ] Comprehension variables complete where applicable
- [ ] Trust variables complete where applicable
- [ ] Workload variables complete where applicable
- [ ] Perceived-understanding variables complete where applicable
- [ ] Response-time units consistent
- [ ] Qualitative notes separated from quantitative fields
- [ ] Raw data preserved
- [ ] Cleaned data created separately
- [ ] Data dictionary version retained

---

11. Separation of Data Layers

The project maintains three conceptual data layers.

Raw Data

Original recorded observations.

Raw data are preserved without overwriting.

Cleaned Data

A documented derivative of the raw dataset in which formatting and explicitly defined data-quality issues are corrected.

Cleaning does not alter the substantive meaning of participant responses.

Analysis Data

The dataset used for statistical and qualitative analysis after the predefined cleaning rules have been applied.

Every transformation should be reproducible and documented.

---

12. Formal Collection Status

Experimental design: Complete
Experimental protocol: Complete
Experimental version: Frozen at EV-1.0
Data dictionary: Complete
Dataset structure: Established
Formal collection procedure: Established
Formal empirical results: Not claimed at this stage
Statistical findings: Not claimed at this stage

---

13. Day 30 Outcome

Day 30 establishes the formal data-collection execution record and maintains a controlled separation between experimental procedure and empirical interpretation.

The project is now positioned to accumulate formal observations under the frozen EV-1.0 protocol.

The next analytical stage will use the recorded dataset rather than assumptions, expected outcomes, or fabricated values.

---

14. Git Commit

Day 30: Initiate formal data collection and establish controlled dataset workflow
