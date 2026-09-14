Day 31 — Data Quality Assurance Protocol

Project: Autonomous Vehicle Passenger Control Interface
Research Phase: Formal Empirical Data Collection
Experimental Version: EV-1.0
Primary Research Question:

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

---

1. Purpose

Day 31 establishes the formal data-quality assurance (DQA) procedure for the empirical dataset.

The objective is to ensure that observations collected under EV-1.0 remain:

- internally consistent;
- traceable to their source trial;
- compatible with the predefined data dictionary;
- distinguishable from technical or procedural failures;
- suitable for reproducible analysis.

The quality-assurance process does not alter participant responses to produce a preferred result.

---

2. Data Pipeline

The project uses the following controlled pipeline:

Formal Observation
        ↓
Raw Dataset
        ↓
Structural Validation
        ↓
Data-Quality Review
        ↓
Cleaning Log
        ↓
Clean Dataset
        ↓
Analysis Dataset
        ↓
Statistical / Qualitative Analysis

The raw dataset remains immutable.

Any transformation is performed on a derivative dataset and documented.

---

3. Raw Dataset Protection

The raw dataset is treated as the primary record of formal observations.

The following rules apply:

1. Raw observations are not overwritten.
2. Original values are retained even when an error is discovered.
3. Corrections are applied only to derivative datasets.
4. Every substantive transformation is documented.
5. Participant identifiers contain no directly identifying personal information.
6. Dataset versions are distinguishable through filenames and Git history.

Recommended structure:

data/
├── README.md
├── raw/
│   └── formal-data-raw.csv
├── cleaned/
│   └── formal-data-cleaned.csv
└── codebook/
    └── data-dictionary.md

---

4. Structural Validation

Each dataset is checked for the following:

Participant Identifier

"participant_id"

Requirements:

- non-empty for valid formal observations;
- consistent across trials;
- no duplicate participant identifier representing different participants.

Trial Identifier

"trial_id"

Requirements:

- unique within the dataset;
- associated with exactly one participant;
- associated with a valid scenario.

Scenario Identifier

"scenario_id"

Requirements:

- must correspond to a predefined experimental scenario;
- must not contain an unapproved scenario variant.

Explanation Condition

"condition"

Only the following values are valid:

A = No explanation
B = Minimal explanation
C = Contextual explanation

Any other value is flagged for review.

---

5. Measurement Validation

Comprehension

The recorded value must correspond to the predefined comprehension scoring procedure.

The researcher does not reinterpret an incorrect response as correct because it appears conceptually close.

Response Time

Response time is represented in:

milliseconds (ms)

Values are checked for:

- missing units;
- impossible negative values;
- accidental text entry;
- obvious recording errors.

A suspicious value is flagged rather than automatically deleted.

Trust

Trust responses must follow the predefined measurement scale.

Workload

Workload responses must follow the predefined workload measurement procedure.

Perceived Understanding

Responses must remain consistent with the predefined scale.

---

6. Logical Consistency Checks

The following relationships are reviewed.

Trial Identity

Every observation must map to:

participant → trial → scenario → condition

Condition Integrity

The recorded condition must correspond to the experimental version used for that trial.

Technical Issues

A technical issue is not treated as a participant interaction error.

Protocol Deviations

A protocol deviation is recorded separately from participant performance.

Missing Data

Missing values are represented as:

NA

Missing observations are not converted to zero.

---

7. Quality Flags

The following flags are available:

Flag| Meaning
"TECHNICAL_ISSUE"| Interface or recording problem
"PROTOCOL_DEVIATION"| Procedure differed from protocol
"MISSING_RESPONSE"| Expected response unavailable
"TRIAL_INTERRUPTED"| Trial did not complete normally
"PARTICIPANT_WITHDRAWAL"| Participant discontinued participation
"INVALID_TRIAL"| Trial cannot be interpreted according to protocol

A flag does not automatically imply exclusion.

The analysis plan determines whether a flagged observation is retained, excluded, or analyzed separately.

---

8. Duplicate Detection

Duplicate observations are identified using the combination of:

participant_id
+
trial_id

If a duplicate exists, the original records are preserved and the duplication is documented.

No record is silently deleted.

---

9. Missing-Data Policy

Missingness is categorized where possible.

Type 1 — Participant Missingness

The participant did not provide the required response.

Type 2 — Technical Missingness

The measurement could not be captured because of a technical problem.

Type 3 — Protocol Missingness

A protocol deviation prevented valid measurement.

Type 4 — Administrative Missingness

The value was not recorded correctly during session administration.

The reason for missingness is retained whenever known.

---

10. Outlier Policy

Potentially unusual values are not automatically removed.

An observation is reviewed against:

1. the original record;
2. the session record;
3. the protocol;
4. the measurement definition;
5. the data-entry history.

An unusual value may represent a legitimate participant response.

Therefore:

«Statistical unusualness alone is not sufficient justification for deleting an observation.»

---

11. Cleaning Rules

Permitted cleaning operations include:

- correcting documented formatting inconsistencies;
- standardizing condition labels;
- standardizing missing-value representation;
- correcting demonstrable transcription errors;
- removing accidental duplicate rows when the duplication is confirmed;
- standardizing response-time units where the original unit is known.

Not permitted:

- changing participant answers;
- replacing missing values with expected values;
- removing inconvenient observations;
- changing condition assignments to improve balance;
- changing scores to fit hypotheses;
- deleting unexpected results without documented justification.

---

12. Cleaning Log

Every substantive correction follows this format:

Field| Description
Dataset version| Dataset being modified
Variable| Variable affected
Original value| Recorded value
Revised value| Corrected value
Reason| Evidence-based reason
Evidence| Source record/session
Decision| Retain/correct/exclude
Reviewer| Person performing review

---

13. Analysis Readiness Criteria

A dataset is considered ready for analysis only when:

- [ ] participant identifiers are consistent;
- [ ] trial identifiers are unique;
- [ ] scenario identifiers are valid;
- [ ] explanation conditions are valid;
- [ ] measurement scales are correct;
- [ ] response-time units are consistent;
- [ ] missing values are explicitly coded;
- [ ] technical issues are documented;
- [ ] protocol deviations are documented;
- [ ] duplicate records are reviewed;
- [ ] cleaning decisions are documented;
- [ ] raw data remain preserved;
- [ ] dataset version is recorded;
- [ ] analysis dataset can be traced to the raw dataset.

---

14. Relationship to the Analysis Plan

The DQA procedure does not replace the predefined analysis plan.

The analysis plan determines:

- descriptive statistics;
- condition comparisons;
- effect-size reporting;
- inferential testing where justified;
- qualitative analysis;
- treatment of protocol deviations;
- treatment of missing observations;
- limitations.

Data quality assurance occurs before interpretation.

---

15. Empirical Integrity Statement

No statistical result is considered valid unless it can be traced to:

Recorded observation
        ↓
Raw dataset
        ↓
Documented transformation
        ↓
Analysis dataset
        ↓
Reproducible calculation

No empirical result is inferred from the research hypothesis alone.

---

16. Day 31 Outcome

Day 31 establishes a reproducible quality-assurance layer between formal data collection and empirical analysis.

The project now has a controlled pathway for transforming recorded observations into an analysis-ready dataset without compromising the original evidence.

Status: Data-quality framework complete.

---

Git Commit

Day 31: Establish data quality assurance and reproducible analysis pipeline
