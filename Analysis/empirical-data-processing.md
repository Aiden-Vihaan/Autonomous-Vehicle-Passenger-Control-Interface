Day 41 — Empirical Data Processing

Project: Autonomous Vehicle Passenger Control Interface
Research Track: Human Factors / HCI / Explainable Autonomous Vehicle Interaction
Experimental Version: EV-1.0
Day: 41

---

1. Purpose

Day 41 establishes the formal workflow for transforming recorded experimental observations into an analysis-ready dataset.

The objective is to ensure that empirical data are processed systematically before statistical interpretation or research conclusions are produced.

The workflow follows:

«Raw Observations → Validation → Cleaning → Quality Control → Analysis Dataset → Descriptive Analysis → Condition-Level Comparison»

No numerical findings are introduced unless they are directly supported by recorded experimental data.

---

2. Experimental Context

The experiment evaluates passenger-facing explanations of unexpected autonomous-vehicle behaviour.

The controlled explanation conditions are:

Condition| Description
A| No explanation
B| Minimal explanation
C| Contextual explanation

The primary research outcome is:

«Passenger comprehension of unexpected autonomous-vehicle behaviour.»

Secondary outcomes include:

- response time
- trust
- cognitive workload
- perceived understanding
- task success
- interaction errors
- qualitative observations

---

3. Research Model

The empirical workflow follows the experimental structure:

Autonomous Vehicle Event
        ↓
Unexpected Behaviour
        ↓
Explanation Condition
        ↓
Passenger Interpretation
        ↓
Comprehension
        ↓
Trust / Workload / Perceived Understanding
        ↓
Passenger Response

This structure preserves the distinction between the experimental manipulation, measured outcomes, and contextual variables.

---

4. Data Processing Principles

The following principles govern all empirical processing.

4.1 Data Integrity

Raw observations must remain unchanged after collection.

4.2 Traceability

Every analytical observation should be traceable to its corresponding participant, trial, scenario, and experimental condition.

4.3 Reproducibility

Cleaning and transformation decisions must be documented rather than performed through unexplained manual modification.

4.4 Separation of Raw and Cleaned Data

Raw data and analysis-ready data must be stored separately.

data/
├── raw/
├── cleaned/
└── codebook/

4.5 No Fabricated Results

Participant counts, means, standard deviations, significance values, effect sizes, correlations, and other empirical statistics must only be generated from actual recorded observations.

---

5. Required Dataset Structure

The analysis dataset should contain the following variables.

Variable| Type| Role
"participant_id"| Identifier| Participant tracking
"trial_id"| Identifier| Trial tracking
"scenario_id"| Categorical| Scenario tracking
"condition"| Categorical| Experimental condition
"comprehension_score"| Numeric| Primary outcome
"comprehension_correct"| Binary| Primary outcome
"response_time_ms"| Numeric| Secondary outcome
"trust_score"| Numeric| Secondary outcome
"workload_score"| Numeric| Secondary outcome
"perceived_understanding"| Numeric| Secondary outcome
"task_success"| Binary/Categorical| Performance
"interaction_error"| Binary/Categorical| Performance
"protocol_deviation"| Categorical| Quality control
"technical_issue"| Categorical| Quality control
"qualitative_note"| Text| Exploratory observation

---

6. Condition Coding

Experimental conditions must use consistent coding throughout the dataset.

Code| Explanation
"A"| No explanation
"B"| Minimal explanation
"C"| Contextual explanation

Condition labels must not change between data collection, cleaning, analysis, visualisation, and reporting.

---

7. Initial Dataset Validation

Before analysis, the dataset should undergo structural validation.

Required checks

- participant identifiers are present
- trial identifiers are present
- scenario identifiers are valid
- condition values are restricted to A/B/C
- numerical variables contain valid numerical values
- binary variables use the defined coding scheme
- response times use milliseconds
- workload values use the predefined scale
- trust values use the predefined scale
- duplicate trials are identified
- missing values are explicitly represented
- technical issues are documented
- protocol deviations are documented

---

8. Missing Data Handling

Missing observations must not automatically be treated as zero.

Missingness should be classified where possible.

Recommended categories:

NA
NOT_RECORDED
TECHNICAL_FAILURE
PARTICIPANT_WITHDRAWAL
TRIAL_INTERRUPTED
NOT_APPLICABLE

The final analysis should document:

1. how much data are missing
2. which variables are affected
3. why observations are missing where known
4. whether missing observations are excluded from specific analyses
5. whether the missingness could influence interpretation

---

9. Invalid Trial Handling

A trial may require exclusion from a specific analysis if the recorded observation cannot validly represent the intended experimental measurement.

Potential reasons include:

- technical failure
- incomplete trial
- protocol violation
- participant withdrawal
- corrupted measurement
- invalid response recording

An excluded trial should not simply disappear.

It should remain traceable through a quality-control flag.

Example:

trial_id: T014
technical_issue: TRUE
protocol_deviation: FALSE
analysis_status: EXCLUDED
exclusion_reason: INTERFACE_FAILURE

---

10. Cleaning Rules

Cleaning must be conservative.

Permitted processing

- correcting documented data-entry errors
- standardising categorical labels
- converting units
- identifying duplicates
- flagging invalid trials
- explicitly representing missing observations
- separating invalid observations from valid analysis observations

Prohibited processing

- changing observations to improve statistical results
- removing inconvenient observations without justification
- replacing missing values without a documented method
- altering participant responses
- selectively excluding participants after inspecting results
- changing condition labels
- manually modifying statistical outputs

---

11. Primary Outcome: Comprehension

The primary dependent variable is passenger comprehension.

Two representations are maintained.

11.1 Comprehension Score

A continuous or ordinal score derived from the predefined comprehension assessment.

comprehension_score

11.2 Comprehension Correctness

A binary representation:

1 = Correct
0 = Incorrect

This allows both descriptive score analysis and categorical comprehension analysis.

---

12. Secondary Outcomes

12.1 Response Time

Recorded in milliseconds:

response_time_ms

Response-time distributions should be inspected before selecting statistical procedures.

Potential reporting measures include:

- mean
- median
- standard deviation
- interquartile range
- minimum
- maximum

---

12.2 Trust

Trust is analysed as a distinct construct rather than as a proxy for comprehension.

trust_score

The analysis should examine whether explanation conditions are associated with differences in reported trust.

The objective is not to maximise trust.

The Human Factors objective is appropriately calibrated trust.

---

12.3 Cognitive Workload

Workload is measured using the predefined workload instrument.

workload_score

Where NASA-TLX or an equivalent validated instrument is used, the reporting procedure should follow the selected instrument's scoring conventions.

---

12.4 Perceived Understanding

Participants' subjective understanding is recorded separately:

perceived_understanding

This allows comparison between:

«What participants believe they understood»

and

«What participants demonstrated through objective comprehension.»

---

12.5 Task Success

Task performance is recorded using:

task_success

This provides an additional behavioural outcome beyond questionnaire responses.

---

12.6 Interaction Errors

Interaction errors are recorded as:

interaction_error

Errors should be interpreted in relation to the task and interface state rather than treated as isolated numbers.

---

13. Descriptive Analysis

The first empirical analysis should be descriptive.

For each experimental condition:

Condition A
Condition B
Condition C

report the available observations for:

- comprehension
- comprehension correctness
- response time
- trust
- workload
- perceived understanding
- task success
- interaction errors

Descriptive statistics should be reported before inferential testing.

---

14. Condition-Level Summary

The core results table should follow this structure.

Outcome| Condition A| Condition B| Condition C
Comprehension score| —| —| —
Comprehension accuracy| —| —| —
Response time| —| —| —
Trust| —| —| —
Workload| —| —| —
Perceived understanding| —| —| —
Task success| —| —| —
Interaction errors| —| —| —

The dashes indicate values that must be generated from the actual dataset.

---

15. Distribution Inspection

Before selecting inferential procedures, distributions should be inspected.

Particular attention should be given to:

- comprehension scores
- response times
- trust scores
- workload scores
- perceived understanding

Response time deserves additional inspection because such measurements may be asymmetric.

Possible inspection methods include:

- histograms
- box plots
- density plots
- Q-Q plots where appropriate

The purpose is diagnostic rather than cosmetic.

---

16. Initial Visualisation Framework

The empirical results should use visualisations that directly correspond to research questions.

Recommended figures:

Figure 1 — Comprehension by Explanation Condition

Explanation Condition
        ↓
Comprehension

Figure 2 — Response Time by Condition

Explanation Condition
        ↓
Response Time

Figure 3 — Trust by Condition

Explanation Condition
        ↓
Trust

Figure 4 — Workload by Condition

Explanation Condition
        ↓
Cognitive Workload

Figure 5 — Objective vs Perceived Understanding

Objective Comprehension
          ↕
Perceived Understanding

Figures should display uncertainty where appropriate and should not visually exaggerate differences.

---

17. Objective vs Subjective Understanding

A central Human Factors question is whether subjective understanding corresponds to objectively demonstrated comprehension.

The analysis therefore considers:

comprehension_score
        ↕
perceived_understanding

Possible outcomes include:

- strong correspondence
- weak correspondence
- divergence
- condition-dependent differences

No relationship should be assumed before analysis.

---

18. Trust–Comprehension Relationship

Trust and comprehension are treated as related but distinct constructs.

The analysis may examine:

comprehension_score
        ↕
trust_score

This is important because increased trust does not necessarily imply improved understanding.

Similarly, improved understanding does not automatically imply increased trust.

---

19. Workload–Comprehension Relationship

The project also examines the relationship between information processing demands and understanding.

workload_score
        ↕
comprehension_score

The theoretical expectation is not that lower workload is always better.

A useful explanation may increase understanding while also increasing cognitive demand.

The empirical analysis therefore evaluates both constructs rather than optimising one independently.

---

20. Inferential Analysis

Inferential testing should only be selected after inspection of:

- actual sample size
- measurement scale
- experimental design
- repeated-measures structure
- distribution characteristics
- missingness
- validity of assumptions

Potential methods may include:

- paired comparisons
- repeated-measures procedures
- non-parametric alternatives
- categorical association tests
- correlation or regression approaches

The exact method must be justified from the actual dataset rather than predetermined solely for convenience.

---

21. Effect Sizes

Statistical significance alone is insufficient.

Where inferential testing is appropriate, effect sizes should also be reported.

The reporting framework should consider:

- magnitude
- direction
- uncertainty
- practical relevance
- confidence intervals where appropriate

A statistically detectable difference should not automatically be described as practically important.

---

22. Multiple Comparisons

Because the experiment includes multiple outcomes and potentially multiple condition comparisons, the analysis should document the number and nature of statistical tests.

Where appropriate, procedures for controlling multiplicity should be considered.

The analysis should avoid presenting isolated statistically significant findings as if they were independent confirmation of the research hypothesis.

---

23. Qualitative Observation Processing

Qualitative observations may provide contextual information that quantitative measures cannot capture.

Potential categories include:

- confusion
- delayed interpretation
- explanation-seeking behaviour
- perceived reassurance
- perceived information overload
- uncertainty
- accessibility difficulty
- interaction difficulty
- unexpected interpretation

Qualitative observations should remain clearly distinguished from quantitative findings.

---

24. Protocol Deviations

Any deviation from the planned experimental protocol should be documented.

Examples:

Participant instruction deviation
Scenario timing deviation
Interface malfunction
Measurement failure
Unexpected interruption
Incomplete trial

Deviations should be evaluated for their potential effect on the corresponding observation.

---

25. Analysis Decision Log

Every non-trivial analytical decision should be recorded.

Example:

Decision| Reason| Impact
Exclude technically invalid trial| Measurement unavailable| Trial removed from affected analysis
Retain valid extreme response| No evidence of measurement error| Included
Treat missing workload score as NA| No valid observation recorded| Excluded from workload calculation

This creates an auditable analytical history.

---

26. Empirical Integrity Rules

The following rules remain active throughout the project.

1. No fabricated participant data.
2. No simulated empirical results presented as real findings.
3. No invented statistical significance.
4. No invented effect sizes.
5. No selective reporting.
6. No unexplained participant exclusion.
7. No post-hoc manipulation of conditions.
8. No unsupported causal claims.
9. Null results must be reported honestly.
10. Limitations must remain visible.

---

27. Day 41 Output

Day 41 establishes the empirical-processing foundation required for final analysis.

Completed methodological outputs:

- raw-data structure
- dataset validation framework
- cleaning procedure
- missing-data policy
- invalid-trial policy
- primary outcome processing
- secondary outcome processing
- descriptive-analysis framework
- visualisation framework
- qualitative-analysis framework
- protocol-deviation handling
- analysis decision logging
- empirical integrity safeguards

---

28. Current Research Status

The project is now structurally prepared for empirical results generation.

The project does not claim numerical findings until actual observations have been recorded and processed.

Therefore:

«Methodological readiness ≠ empirical evidence.»

The distinction is intentionally maintained throughout the project.

---

29. Next Step

The next stage is to convert the processed dataset into a formal results section containing:

1. participant/sample description
2. data-quality summary
3. descriptive statistics
4. condition-level comparisons
5. primary outcome analysis
6. secondary outcome analysis
7. effect sizes and uncertainty
8. qualitative findings
9. hypothesis mapping
10. research interpretation

Next milestone: Day 42 — Empirical Results Synthesis and Research Findings Framework
