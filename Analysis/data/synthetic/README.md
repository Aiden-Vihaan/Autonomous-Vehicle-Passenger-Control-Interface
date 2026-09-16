Synthetic Demonstration Dataset

This directory contains a programmatically generated dataset used to demonstrate the EV-1.0 analysis pipeline.

The observations do not represent real participants.

No claim about human behaviour, statistical significance, trust, comprehension, workload, or design effectiveness should be based on this dataset.

---

Why It Exists

The synthetic dataset allows the repository to demonstrate the complete analytical workflow without misrepresenting invented observations as genuine research.

It supports:

- pipeline testing
- code testing
- figure generation
- statistical-method demonstration
- reproducibility testing
- portfolio demonstration

---

Generation

The dataset is generated using:

generate_synthetic_data.py

A fixed random seed is used so that the demonstration dataset can be regenerated.

---

Interpretation

Synthetic patterns are intentionally plausible but are not evidence.

Any values shown in:

analysis/
paper/
presentation/

must be identified as synthetic whenever they originate from this dataset.

---

Replacement With Real Data

If genuine participant data are subsequently collected, they should replace the synthetic demonstration dataset only in the empirical analysis workflow.

The synthetic dataset should remain archived as a demonstration artifact.
