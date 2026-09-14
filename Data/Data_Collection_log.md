Formal Data Collection Log

Project: Autonomous Vehicle Passenger Control Interface
Experimental Version: EV-1.0
Research Phase: Formal Data Collection
Primary Outcome: Comprehension

---

1. Purpose

This document provides the controlled record for formal empirical data collection.

It is intentionally separated from the analysis results so that the collection process can be documented independently from subsequent interpretation.

---

2. Collection Rules

All formal observations must follow the frozen experimental protocol.

The following remain fixed:

- scenario structure;
- explanation-condition definitions;
- participant role;
- interface configuration;
- participant instructions;
- measurement procedure;
- data coding;
- analysis definitions.

Any deviation is recorded rather than silently corrected.

---

3. Trial Coding

Explanation Conditions

A = No explanation
B = Minimal explanation
C = Contextual explanation

Missing Data

NA = Not available / missing

Boolean Variables

Where applicable:

1 = Yes / Correct / Present
0 = No / Incorrect / Absent

---

4. Data Collection Sequence

For each formal participant:

Participant briefing
        ↓
Practice
        ↓
Formal trial
        ↓
Unexpected autonomous-vehicle event
        ↓
Explanation condition
        ↓
Passenger interpretation
        ↓
Comprehension
        ↓
Trust
        ↓
Workload
        ↓
Perceived understanding
        ↓
Trial completion
        ↓
Next trial
        ↓
Session completion

---

5. Dataset Integrity

The raw dataset must never be overwritten.

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

6. Data Validation Rules

Before analysis:

Participant IDs

- Must be unique at the participant level.
- Must not contain directly identifying personal information.

Trial IDs

- Must uniquely identify observations.
- Must map to a valid participant and scenario.

Condition

Only the following values are valid:

A
B
C

Comprehension

Must follow the predefined scoring system.

Response Time

Must be recorded consistently in milliseconds.

Trust

Must use the predefined response scale.

Workload

Must use the predefined workload measure.

Perceived Understanding

Must use the predefined measurement scale.

Errors

Interaction errors must be distinguished from protocol deviations and technical failures.

---

7. Quality Flags

The following flags should be documented when applicable:

TECHNICAL_ISSUE
PROTOCOL_DEVIATION
MISSING_RESPONSE
TRIAL_INTERRUPTED
PARTICIPANT_WITHDRAWAL
INVALID_TRIAL

A quality flag does not automatically mean that an observation must be removed.

Inclusion or exclusion decisions are made according to the analysis plan and are documented transparently.

---

8. Researcher Conduct

During collection, the researcher should:

- provide standardized instructions;
- avoid leading participants;
- avoid revealing the hypothesis;
- avoid explaining the intended meaning of an experimental condition;
- avoid correcting participant responses;
- document observable procedural issues;
- separate observations from interpretation;
- preserve unexpected outcomes.

---

9. Formal Collection Record

The following information is retained for each collection session:

Session ID:
Participant ID:
Experimental Version:
Scenario Version:
Date:
Start Time:
End Time:
Protocol Followed:
Technical Issues:
Protocol Deviations:
Participant Withdrawal:
Data Completeness:
Researcher Notes:

No identifying personal information is stored in the analytical dataset.

---

10. Data-Lifecycle Record

Collection
    ↓
Raw dataset
    ↓
Integrity check
    ↓
Cleaning
    ↓
Clean dataset
    ↓
Analysis dataset
    ↓
Statistical / qualitative analysis
    ↓
Figures and tables
    ↓
Research interpretation

Each stage must remain traceable to the preceding stage.

---

11. Evidence Discipline

This project follows a strict evidence hierarchy:

Level 1 — Recorded Data

Direct participant responses and measured observations.

Level 2 — Derived Results

Values calculated from the recorded dataset.

Level 3 — Interpretation

Researcher's explanation of patterns supported by the data.

Level 4 — Discussion

Comparison of observed findings with the literature and theoretical framework.

No higher-level claim should be presented without evidence from the preceding level.

---

12. Current Status

Formal collection infrastructure: Established
Experimental version: EV-1.0
Dataset schema: Established
Raw-data preservation: Defined
Cleaning workflow: Defined
Analysis linkage: Defined
Empirical findings: Not yet claimed

---

13. Integrity Statement

«No participant-level data, statistical result, effect size, significance value, or empirical conclusion is entered into this repository unless it originates from an actual recorded observation or a reproducible transformation of recorded observations.»

This rule applies throughout the remainder of the project.
