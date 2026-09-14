Day 32 — Empirical Dataset Inspection and Descriptive Analysis

Project: Autonomous Vehicle Passenger Control Interface
Experimental Version: EV-1.0
Day: 32
Phase: Empirical Analysis
Status: Analysis pipeline completed; empirical findings reported only from recorded participant data

---

1. Purpose

Day 32 establishes the first reproducible empirical-analysis stage for the Autonomous Vehicle Passenger Control Interface experiment.

The purpose of this stage is to:

1. inspect the structure and integrity of the empirical dataset;
2. verify that recorded observations conform to the frozen experimental design;
3. distinguish valid observations from missing, interrupted, or technically compromised trials;
4. establish descriptive summaries for the primary and secondary measures;
5. prepare the dataset for inferential and qualitative analysis;
6. prevent premature interpretation of incomplete or unverified observations.

The analysis remains aligned with the experimental objective of examining how explanation presentation influences passenger understanding, trust, workload, and related interaction outcomes.

---

2. Experimental Context

The experiment compares three explanation conditions:

Condition| Description
A — No Explanation| The vehicle changes behaviour without an accompanying explanatory message.
B — Minimal Explanation| A concise explanation communicates the immediate reason for the vehicle's behaviour.
C — Contextual Explanation| A more specific explanation communicates the relevant situation and the vehicle's intended response.

The primary dependent variable is comprehension.

Secondary variables are:

- response time;
- trust;
- workload;
- perceived understanding;
- task success;
- interaction errors;
- qualitative observations.

The analysis therefore focuses first on whether the dataset can support comparisons across these conditions.

---

3. Dataset Inspection Protocol

The dataset is inspected in the following order:

Raw Dataset
    ↓
File / Structure Validation
    ↓
Variable Validation
    ↓
Participant / Trial Validation
    ↓
Condition Validation
    ↓
Missingness Inspection
    ↓
Quality-Flag Inspection
    ↓
Descriptive Statistics
    ↓
Visualisation
    ↓
Inferential Analysis Readiness

The raw dataset is treated as immutable.

No analysis step overwrites the original observations.

---

4. Required Dataset Structure

Each recorded trial should contain the following fields:

Variable| Type| Role
"participant_id"| categorical| Participant identifier
"trial_id"| categorical| Unique trial identifier
"scenario_id"| categorical| Scenario identifier
"condition"| categorical| A, B, or C
"comprehension_score"| numeric| Primary outcome
"comprehension_correct"| binary| Primary correctness indicator
"response_time_ms"| numeric| Response time
"trust_score"| numeric| Trust measure
"workload_score"| numeric| Workload measure
"perceived_understanding"| numeric| Subjective understanding
"task_success"| binary| Task completion
"interaction_error"| binary| Interaction error indicator
"protocol_deviation"| categorical| Protocol deviation flag
"technical_issue"| categorical| Technical issue flag
"qualitative_note"| text| Structured qualitative observation

---

5. Structural Inspection

The following checks constitute the first analysis gate.

5.1 File existence

The analysis workflow checks whether the expected raw-data file exists.

Status: Analysis infrastructure established.

Empirical status: No participant-level findings are claimed without an actual recorded dataset.

5.2 Column validation

The dataset must contain the variables defined in the Day 29 data dictionary.

Unexpected variables are retained for traceability but are not automatically incorporated into the analysis.

Missing required variables trigger an analysis-readiness warning.

5.3 Identifier validation

The following conditions are checked:

- participant identifiers are present;
- trial identifiers are present;
- trial identifiers are unique where required;
- condition labels use only "A", "B", or "C";
- scenario identifiers correspond to defined scenarios.

5.4 Type validation

Numeric variables must be interpretable as numeric measurements.

Categorical variables must conform to the predefined coding scheme.

Free-text observations remain qualitative and are not converted into numerical values without a documented coding procedure.

---

6. Missing Data Inspection

Missing observations are classified rather than silently removed.

Missingness categories

Code| Meaning
"NA_RESPONSE"| Participant did not provide a response
"TRIAL_INTERRUPTED"| Trial did not reach completion
"TECHNICAL_ISSUE"| Technical problem affected measurement
"PROTOCOL_DEVIATION"| Trial departed from the defined procedure
"PARTICIPANT_WITHDRAWAL"| Participant withdrew
"INVALID_TRIAL"| Trial cannot be interpreted according to the protocol

Missing values are not automatically replaced with averages or other imputed values.

Any future decision to exclude or retain a trial will be documented in the analysis log.

---

7. Primary Outcome Inspection

Primary outcome

Comprehension

Comprehension is examined using:

- "comprehension_score";
- "comprehension_correct".

The first descriptive comparison is:

Condition A
vs.
Condition B
vs.
Condition C

The analysis asks:

«Do recorded comprehension outcomes differ descriptively across explanation conditions?»

This is a descriptive question at Day 32. It is not treated as evidence of statistical significance.

---

8. Secondary Outcome Inspection

Response Time

Response time is inspected in milliseconds.

The following descriptive quantities are appropriate:

- number of valid observations;
- mean;
- median;
- standard deviation;
- minimum;
- maximum;
- distribution.

Because response-time data can be skewed, the median is retained alongside the mean.

---

Trust

Trust scores are summarised by experimental condition.

The purpose is to examine whether the recorded pattern is directionally consistent with the research question concerning explanation presentation and trust.

No causal interpretation is made from descriptive statistics alone.

---

Workload

Workload scores are summarised by condition.

The analysis specifically considers whether more detailed explanations appear to coincide with:

- lower workload;
- higher workload;
- or no clear descriptive difference.

The interpretation remains exploratory unless the sample and statistical assumptions justify formal testing.

---

Perceived Understanding

Perceived understanding is compared descriptively with objective comprehension.

This distinction is important because a participant may report feeling informed without demonstrating equivalent objective understanding.

---

Task Success and Interaction Error

Binary task outcomes are summarised using:

- valid trial count;
- successful trials;
- unsuccessful trials;
- interaction-error frequency.

These measures provide an additional behavioural perspective beyond subjective ratings.

---

9. Data Quality Flags

Every analysis dataset should preserve the following flags:

TECHNICAL_ISSUE
PROTOCOL_DEVIATION
MISSING_RESPONSE
TRIAL_INTERRUPTED
PARTICIPANT_WITHDRAWAL
INVALID_TRIAL

Quality flags are not treated as outcome variables unless explicitly required by a later analysis.

Instead, they determine whether an observation should be included in a particular analysis.

---

10. Descriptive Analysis Matrix

Research construct| Measure| Descriptive analysis
Understanding| Comprehension score| Mean, median, SD, distribution
Understanding| Correctness| Proportion correct
Efficiency| Response time| Mean, median, SD, distribution
Trust| Trust score| Mean, median, SD
Workload| Workload score| Mean, median, SD
Subjective understanding| Perceived understanding| Mean, median, SD
Behaviour| Task success| Success proportion
Errors| Interaction error| Error proportion
Experience| Qualitative notes| Thematic categorisation

---

11. Planned Visualisations

The first results pipeline uses the following figures.

Figure 1 — Comprehension by Explanation Condition

A condition-level distribution plot comparing:

A — No Explanation
B — Minimal Explanation
C — Contextual Explanation

Figure 2 — Response Time by Condition

A distribution plot showing whether explanation condition is associated with differences in response time.

Figure 3 — Trust by Condition

A condition-level comparison of trust scores.

Figure 4 — Workload by Condition

A condition-level comparison of workload scores.

Figure 5 — Perceived Understanding by Condition

A condition-level comparison of perceived understanding.

Figure 6 — Task Success and Interaction Errors

A categorical summary of successful and unsuccessful interactions.

---

12. Interpretation Rules

The following rules govern interpretation:

1. Descriptive differences are not automatically statistically significant.
2. A higher mean does not automatically indicate a practically meaningful improvement.
3. Null differences are retained as legitimate findings.
4. Missing data are reported rather than concealed.
5. Technical failures are distinguished from participant behaviour.
6. Protocol deviations are documented.
7. Outliers are investigated before removal.
8. Participant-level repeated observations are not treated as independent without justification.
9. Small samples are interpreted cautiously.
10. No claim is made about real-world autonomous-vehicle safety based on this experiment.

---

13. Empirical Results Status

At this stage, the analysis framework is complete.

However, no participant-level numerical results are asserted in this document unless they originate from the recorded experimental dataset.

This distinction is deliberate.

The project does not manufacture:

- participant counts;
- mean scores;
- statistical significance;
- effect sizes;
- trust improvements;
- workload reductions;
- comprehension percentages;
- response-time differences.

These values will enter the research record only through the actual dataset.

---

14. Day 32 Completion Criteria

Day 32 is considered methodologically complete when:

- [x] Dataset schema is defined.
- [x] Variable types are defined.
- [x] Condition coding is validated conceptually.
- [x] Missing-data categories are defined.
- [x] Quality flags are defined.
- [x] Primary outcome analysis is specified.
- [x] Secondary outcome analysis is specified.
- [x] Descriptive statistics are specified.
- [x] Visualisation plan is specified.
- [x] Interpretation rules are defined.
- [x] No fabricated empirical findings are introduced.
- [ ] Recorded participant dataset has been numerically analysed.

The final item is intentionally dependent on actual empirical observations.

---

15. Transition to Day 33

Day 33 proceeds to:

«Empirical Results Generation and Condition-Level Comparison»

The next stage will convert the recorded dataset into:

- descriptive tables;
- condition-level figures;
- participant/trial accounting;
- quality-filtered analysis datasets;
- preliminary result statements;
- and an evidence-based results narrative.

Only values produced from the actual dataset will be incorporated into the final research report.
