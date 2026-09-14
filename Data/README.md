Experimental Data

Project: Autonomous Vehicle Passenger Control Interface
Dataset: Formal Experimental Study
Version: DATA-1.0
Status: Analysis-ready data structure

---

Purpose

This directory contains the structured data generated during formal evaluation of the autonomous-vehicle passenger interface.

The study investigates the effect of explanation presentation on passenger understanding, trust, perceived workload, and perceived understanding.

---

Data Principle

Only observations actually collected during the formal study are entered into the dataset.

No synthetic participant data are used as empirical evidence.

No invented statistics, participant quotations, or experimental findings are permitted.

---

Directory Structure

data/
├── README.md
├── raw/
├── cleaned/
└── codebook/

"raw/"

Original exported study data.

Raw files are preserved and are not overwritten during analysis.

"cleaned/"

Validated analytical datasets derived from the raw data.

Every transformation must be documented.

"codebook/"

Definitions and coding rules for variables.

---

Data Lifecycle

Participant interaction
        ↓
Raw observation
        ↓
Raw dataset
        ↓
Integrity check
        ↓
Cleaned dataset
        ↓
Analysis
        ↓
Figures / tables
        ↓
Research interpretation

---

Separation of Evidence

The project distinguishes:

Pilot evidence

Used to identify technical and procedural problems.

Formal empirical evidence

Used to answer the research questions.

Design interpretation

Used to translate empirical findings into human-factors and HCI implications.

These categories must not be mixed.

---

Data Quality Rules

Before a dataset is analysed:

- duplicate records are checked;
- identifiers are validated;
- condition labels are validated;
- missing values are reviewed;
- technical failures are identified;
- protocol deviations are identified;
- scoring rules are verified.

---

Privacy

The analytical dataset should use anonymous participant identifiers.

Personally identifying information must not be placed in the public analytical dataset.

If identifying information is required for administrative purposes, it must be stored separately.

---

Reproducibility

Every cleaned dataset should have:

- a version number;
- a source dataset;
- documented transformations;
- an analysis date;
- the corresponding experimental version.

The objective is to make it possible to trace:

Raw observation
      ↓
Cleaned value
      ↓
Analysis
      ↓
Reported result

---

Research Integrity

The absence of data is itself a valid project state.

If a measure was not collected, it remains unreported.

If a participant observation is ambiguous, the ambiguity is documented.

If the evidence does not support a hypothesis, the final report will state that outcome.

The project prioritizes reproducibility and evidential accuracy over producing a predetermined result.

---

Current Milestone

Day 29

Experimental design       COMPLETE
Experimental protocol     COMPLETE
Data dictionary           COMPLETE
Data infrastructure      COMPLETE
Formal data collection    READY
Formal results            NOT YET CLAIMED

---

Next Milestone

Day 30 — Formal data collection, dataset integrity verification, and first controlled empirical dataset build.
