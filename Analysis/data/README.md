Analysis Data

Purpose

This directory contains the data architecture used for the EV-1.0 Human Factors evaluation.

The project separates:

1. Raw participant data
2. Cleaned analysis data
3. Codebook and data definitions
4. Synthetic demonstration data
5. Analysis outputs

The separation is intentional so that data provenance remains visible throughout the research workflow.

---

Experimental Version

EV-1.0

Conditions:

- A — No explanation
- B — Minimal explanation
- C — Contextual explanation

Primary dependent variable:

- "comprehension_correct"

Secondary dependent variables:

- "response_time_ms"
- "trust_score"
- "workload_score"
- "perceived_understanding"
- "task_success"
- "interaction_error"

---

Data Provenance

Real empirical data

If genuine participant data are collected, they belong in:

analysis/data/raw/

Raw data must remain immutable.

Synthetic demonstration data

For demonstrating the analysis pipeline without claiming that participant research was conducted, synthetic data are stored separately:

analysis/data/synthetic/

Synthetic data must never be described as participant observations.

The synthetic dataset included with this project is generated programmatically and is intended only to demonstrate:

- data validation
- descriptive statistics
- condition comparisons
- effect-size calculations
- visualisation
- reporting workflow
- reproducibility

---

Data Integrity Rule

No synthetic observation may be moved into the empirical/raw dataset and represented as a real participant observation.

The analysis pipeline therefore accepts an explicit dataset-status declaration.

DATA_STATUS = SYNTHETIC_DEMONSTRATION

For genuine data collection:

DATA_STATUS = EMPIRICAL

---

Directory Structure

analysis/data/
├── README.md
├── raw/
│   └── README.md
├── cleaned/
│   └── README.md
├── codebook/
│   └── codebook.md
└── synthetic/
    ├── README.md
    ├── generate_synthetic_data.py
    └── ev1_synthetic_trials.csv

---

Reproducibility

The synthetic dataset is generated with a fixed random seed.

This means another researcher can execute the generator and reproduce the same demonstration dataset.

The synthetic dataset is not evidence for the hypotheses.

It is an executable demonstration of how the project would process and analyse a completed empirical dataset.
