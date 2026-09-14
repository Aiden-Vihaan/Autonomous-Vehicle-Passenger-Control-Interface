Experimental Data Dictionary

Project: Autonomous Vehicle Passenger Control Interface
Dataset: Formal Experimental Dataset
Version: DD-1.0
Milestone: Day 29

---

1. Purpose

This document defines the structure and meaning of every variable in the formal experimental dataset.

The data dictionary is established before analysis so that variables have predefined meanings and are not redefined after results are observed.

---

2. Dataset Unit

The fundamental analytical unit is:

«One participant × one experimental trial»

Each row represents one experimental trial for one participant.

---

3. Core Variables

Variable| Type| Description
participant_id| categorical| Anonymous participant identifier
trial_id| categorical| Unique identifier for the trial
scenario_id| categorical| Identifier for the experimental scenario
condition| categorical| Explanation condition A, B, or C
comprehension_score| numeric| Predefined comprehension score
comprehension_correct| binary| Whether the predefined comprehension criterion was met
response_time_ms| numeric| Response time in milliseconds, where available
trust_score| numeric| Participant's trust rating
workload_score| numeric| Participant's workload rating
perceived_understanding| numeric| Participant's perceived understanding rating
task_success| binary| Whether the required interaction was successfully completed
interaction_error| categorical| Predefined interaction-error classification
protocol_deviation| binary| Whether a protocol deviation occurred
technical_issue| binary| Whether a technical issue affected the trial
qualitative_note| text| Structured observation/comment where applicable

---

4. Explanation Condition Coding

Code| Meaning
A| No explanation
B| Minimal explanation
C| Contextual explanation

The condition variable is categorical.

It must not be treated as a continuous numerical scale.

---

5. Comprehension Coding

The comprehension score follows the predefined scoring rubric.

Where binary scoring is used:

Value| Meaning
1| Correct
0| Incorrect

If multiple comprehension questions are used, the total score is calculated according to the frozen scoring procedure.

No post-hoc changes to the scoring rule are permitted without documentation.

---

6. Response Time

"response_time_ms" represents the elapsed time between presentation of the predefined response prompt and participant submission.

Unit:

milliseconds

Missing response times are represented as missing values rather than estimated values.

---

7. Trust Score

"trust_score" represents the participant's reported trust rating using the predefined trust questionnaire.

The exact scale is determined by the questionnaire version used during data collection.

The variable represents subjective perception.

It does not represent objective system reliability.

---

8. Workload Score

"workload_score" represents perceived workload using the predefined workload instrument.

Where NASA-TLX is used, the scoring procedure must remain consistent for all participants.

The variable is a subjective human-factors measure.

---

9. Perceived Understanding

"perceived_understanding" represents how well the participant believes they understood the reason for the vehicle's behaviour.

This variable must remain separate from "comprehension_score".

---

10. Task Success

Coding:

Value| Meaning
1| Required task completed
0| Required task not completed

Task failure must not automatically be interpreted as comprehension failure.

---

11. Interaction Error

Interaction errors use predefined categories.

Recommended coding:

NONE
NAVIGATION_ERROR
SELECTION_ERROR
MISINTERPRETATION
TECHNICAL_ERROR
OTHER

An error is coded only when it meets the operational definition established by the study.

---

12. Protocol Deviation

Coding:

Value| Meaning
1| Protocol deviation occurred
0| No protocol deviation

The reason for a deviation is documented separately.

---

13. Technical Issue

Coding:

Value| Meaning
1| Technical issue affected trial
0| No technical issue

Technical issues are distinguished from participant interaction errors.

---

14. Qualitative Notes

Qualitative notes may contain:

- participant comments;
- structured experimenter observations;
- accessibility observations;
- relevant behavioural descriptions;
- technical notes.

Qualitative notes are not treated as quantitative data.

---

15. Missing-Value Convention

The dataset uses an explicit missing-value convention.

Recommended representation:

NA

"NA" means the value was not available or was not collected.

It does not mean zero.

For example:

response_time_ms = NA

means response time was unavailable.

It does not mean:

response_time_ms = 0

---

16. Data Integrity Constraints

The following conditions must hold:

1. Every trial has a valid "participant_id".
2. Every trial has a unique "trial_id".
3. Every trial has a valid "scenario_id".
4. Every trial has a valid explanation condition.
5. Condition codes are restricted to A, B, or C.
6. Binary variables contain only their defined values.
7. Missing values are explicitly represented.
8. No fabricated values are permitted.
9. Protocol deviations remain identifiable.
10. Technical failures remain identifiable.

---

17. Analysis Mapping

Research construct| Dataset variable
Explanation condition| condition
Understanding| comprehension_score
Response performance| response_time_ms
Trust| trust_score
Workload| workload_score
Perceived understanding| perceived_understanding
Task performance| task_success
Interaction problems| interaction_error

---

18. Primary Outcome

The primary outcome is:

«Comprehension of unexpected autonomous-vehicle behaviour.»

Operational dataset variable:

"comprehension_score"

---

19. Secondary Outcomes

Secondary outcomes are:

- response time;
- trust;
- workload;
- perceived understanding;
- task success;
- interaction errors.

---

20. Participant-Level Consideration

If participants complete multiple trials, repeated observations from the same participant must be treated as linked observations.

The analysis must not automatically assume that every trial is statistically independent.

---

21. Data Validation Checklist

Before analysis:

- [ ] IDs validated
- [ ] duplicate trials checked
- [ ] condition coding checked
- [ ] missing values checked
- [ ] impossible values checked
- [ ] technical issues checked
- [ ] protocol deviations checked
- [ ] comprehension scoring checked
- [ ] questionnaire scoring checked
- [ ] dataset version recorded

---

22. Dataset Status

Schema: COMPLETE
Variable definitions: COMPLETE
Coding rules: COMPLETE
Analysis mapping: COMPLETE
Empirical observations: To be populated from actual formal data collection

---

23. Integrity Statement

This dictionary defines how collected observations will be represented.

It does not contain fabricated participant observations or statistical results.
