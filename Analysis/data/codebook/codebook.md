EV-1.0 Data Codebook

Dataset Status

"SYNTHETIC_DEMONSTRATION"

The variables below define the analysis-ready schema for EV-1.0.

---

Identification Variables

Variable| Type| Description
"participant_id"| string| Anonymous participant identifier
"trial_id"| string| Unique trial identifier
"scenario_id"| categorical| Experimental scenario
"condition"| categorical| Explanation condition

Condition coding

Code| Condition
A| No explanation
B| Minimal explanation
C| Contextual explanation

---

Primary Outcome

"comprehension_correct"

Binary variable.

1 = correct interpretation
0 = incorrect interpretation

The primary outcome operationalises objective comprehension of the autonomous vehicle's behaviour.

---

Secondary Outcomes

"response_time_ms"

Time taken to provide the comprehension response, measured in milliseconds.

"trust_score"

Likert-style trust rating.

1 = very low trust
5 = very high trust

Trust is interpreted as an indicator of passenger confidence and calibration rather than as a metric that should simply be maximised.

"workload_score"

Self-reported cognitive workload.

1 = very low workload
5 = very high workload

"perceived_understanding"

Self-reported understanding.

1 = very low perceived understanding
5 = very high perceived understanding

"task_success"

Binary task-completion indicator.

1 = successful
0 = unsuccessful

"interaction_error"

Binary interaction-error indicator.

1 = error occurred
0 = no error

---

Context Variables

Variable| Description
"event_type"| Type of unexpected vehicle behaviour
"urgency"| Relative urgency of scenario
"explanation_timing"| Temporal relationship between explanation and behaviour
"modality"| Presentation modality
"passenger_activity"| Activity being performed during event

---

Quality Variables

Variable| Description
"technical_issue"| Technical problem during trial
"protocol_deviation"| Deviation from study protocol
"missing_response"| Required response missing
"trial_interrupted"| Trial interrupted
"invalid_trial"| Trial excluded from analysis

---

Recommended Analysis Variables

Primary:

comprehension_correct

Secondary:

response_time_ms
trust_score
workload_score
perceived_understanding
task_success
interaction_error

Exploratory/contextual:

event_type
urgency
explanation_timing
modality
passenger_activity

---

Analysis Principle

Objective comprehension and perceived understanding must remain separate constructs.

A participant may report high understanding while failing an objective comprehension question.

Conversely, a participant may correctly interpret an event without reporting high subjective confidence.

This distinction is retained throughout the analysis.
