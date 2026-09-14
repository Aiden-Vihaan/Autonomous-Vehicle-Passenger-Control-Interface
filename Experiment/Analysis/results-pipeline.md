Day 32 — First Results Pipeline

Project: Autonomous Vehicle Passenger Control Interface
Experimental Version: EV-1.0
Analysis Stage: First Results Pipeline
Status: Reproducible analysis framework completed

---

1. Objective

The first results pipeline converts the frozen experimental design into a reproducible sequence for producing empirical results.

The pipeline preserves the distinction between:

- raw observations;
- cleaned observations;
- valid analysis observations;
- descriptive statistics;
- inferential statistics;
- qualitative findings;
- interpretation.

No analytical result is considered valid unless its source observation can be traced back to the recorded dataset.

---

2. Analysis Pipeline

data/raw/
    │
    ├── Structural validation
    │
    ├── Identifier validation
    │
    ├── Condition validation
    │
    ├── Missing-data inspection
    │
    └── Quality-flag inspection
            │
            ↓
data/cleaned/
            │
            ├── Descriptive statistics
            │
            ├── Condition comparisons
            │
            ├── Visualisation
            │
            ├── Effect estimation
            │
            └── Inferential testing where justified
                    │
                    ↓
analysis/results/

---

3. Analysis Dataset

The cleaned analysis dataset must retain:

participant_id
trial_id
scenario_id
condition
comprehension_score
comprehension_correct
response_time_ms
trust_score
workload_score
perceived_understanding
task_success
interaction_error
protocol_deviation
technical_issue
qualitative_note

The raw dataset remains unchanged.

---

4. Primary Analysis

Research question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

Primary outcome

Comprehension

Primary comparison

No Explanation
        vs.
Minimal Explanation
        vs.
Contextual Explanation

The primary analysis first examines descriptive differences.

Inferential testing is performed only if the resulting sample size, design, distribution, and repeated-measures structure support it.

---

5. Secondary Analyses

5.1 Response Time

Question:

«Does explanation condition correspond to differences in the time required to interpret and respond to the vehicle event?»

---

5.2 Trust

Question:

«Does explanation condition correspond to differences in reported trust?»

Trust is interpreted as a measure of passenger-system relationship, not as proof that the vehicle itself is objectively safe.

---

5.3 Workload

Question:

«Does explanation presentation appear to alter perceived cognitive workload?»

Particular attention is paid to whether additional information appears beneficial or potentially burdensome.

---

5.4 Perceived Understanding

Question:

«Do passengers report greater understanding when explanations are provided?»

This measure is analysed separately from objective comprehension.

---

5.5 Task Success

Question:

«Does explanation condition affect successful completion of the defined passenger task?»

---

5.6 Interaction Error

Question:

«Are interaction errors distributed differently across explanation conditions?»

---

6. Participant-Level Accounting

The analysis must report:

Total recruited participants
Total participants completing protocol
Total recorded trials
Valid trials
Excluded trials
Interrupted trials
Trials affected by technical issues
Protocol deviations

No participant or trial count is invented in advance.

---

7. Trial-Level Accounting

Each trial receives an analysis status:

Status| Meaning
"VALID"| Meets the analysis criteria
"MISSING"| Required response unavailable
"INTERRUPTED"| Trial did not complete
"TECHNICAL_ISSUE"| Measurement affected by technical failure
"PROTOCOL_DEVIATION"| Trial departed from protocol
"INVALID"| Trial cannot support the intended analysis

A single participant may therefore contribute valid and invalid trials.

---

8. Descriptive Reporting Standard

For continuous variables, report:

n
mean
median
standard deviation
minimum
maximum

For categorical/binary variables, report:

n
percentage

Where distributions are strongly skewed, median and interquartile range should receive greater interpretive emphasis than the mean.

---

9. Condition-Level Results Table

The final empirical results table will follow this structure:

Measure| A: No Explanation| B: Minimal| C: Contextual
Valid trials| —| —| —
Comprehension| —| —| —
Correct comprehension| —| —| —
Response time| —| —| —
Trust| —| —| —
Workload| —| —| —
Perceived understanding| —| —| —
Task success| —| —| —
Interaction errors| —| —| —

The em-dash represents not yet populated from an actual dataset, rather than zero.

---

10. Relationship Between Objective and Subjective Measures

A particularly important analytical comparison is:

Objective comprehension
        ↕
Perceived understanding

Possible patterns include:

Pattern A — Agreement

High perceived understanding accompanies high comprehension.

Pattern B — Overconfidence

Perceived understanding is high while comprehension is comparatively weak.

Pattern C — Underconfidence

Comprehension is strong while perceived understanding is comparatively low.

Pattern D — No clear relationship

The two measures do not show an interpretable descriptive relationship.

These patterns should be reported rather than assuming that confidence equals understanding.

---

11. Trust–Comprehension Relationship

The analysis also examines whether participants who demonstrate greater comprehension report different levels of trust.

This is exploratory unless the final sample and analysis design justify a formal association test.

The interpretation should avoid the assumption:

«explanation → understanding → trust»

unless the empirical data actually support such a pattern.

---

12. Workload–Explanation Relationship

The analysis specifically tests the conceptual possibility that more information is not automatically better.

The contextual explanation condition may theoretically:

- improve understanding;
- impose additional processing;
- reduce uncertainty;
- increase visual attention;
- or produce little measurable difference.

The analysis therefore remains open to both positive and negative outcomes.

---

13. Qualitative Analysis

Qualitative notes are analysed after quantitative inspection.

Initial coding categories include:

- clarity;
- ambiguity;
- reassurance;
- information overload;
- timing;
- relevance;
- perceived control;
- trust;
- confusion;
- unexpected interpretation;
- accessibility-related observation;
- interaction difficulty.

These are analysis categories, not findings.

Actual themes will be added only when supported by recorded observations.

---

14. Visualisation Principles

Every figure must include:

- meaningful title;
- clearly labelled axes;
- units where applicable;
- explanation-condition labels;
- sample size where useful;
- appropriate uncertainty representation where applicable.

Figures should not imply precision beyond what the sample supports.

---

15. Reproducibility Rules

The analysis pipeline follows five principles:

Rule 1 — Raw data are immutable

The original dataset is never overwritten.

Rule 2 — Cleaning is documented

Every exclusion or transformation has a reason.

Rule 3 — Results are traceable

Every reported statistic can be traced to a defined dataset version.

Rule 4 — Null results remain results

Failure to observe a difference is not converted into a positive narrative.

Rule 5 — Interpretation follows evidence

The research question guides interpretation but does not determine the result.

---

16. Current Analytical Status

Completed:

- analysis architecture;
- dataset inspection framework;
- primary-outcome pipeline;
- secondary-outcome pipeline;
- quality-control integration;
- descriptive-analysis specification;
- visualisation specification;
- qualitative-analysis framework;
- reproducibility rules.

Not claimed without recorded observations:

- participant count;
- condition means;
- statistical significance;
- effect sizes;
- correlations;
- confidence intervals;
- comprehension improvement;
- trust improvement;
- workload reduction.

This preserves the empirical integrity of the project.

---

17. Day 32 Output

Day 32 establishes the bridge between the experimental protocol and the final empirical results.

The project can now move from:

«“What will be analysed?”»

to:

«“What does the recorded evidence show?”»

without changing the frozen experimental design.

---

18. Next Stage

Day 33 — Empirical Results Generation

The next analysis stage will produce the actual:

1. dataset summary;
2. participant/trial accounting;
3. condition-level descriptive statistics;
4. first figures;
5. preliminary empirical observations;
6. deviation and exclusion summary;
7. results narrative.

All numerical results will be generated from the recorded dataset rather than predetermined expectations.
