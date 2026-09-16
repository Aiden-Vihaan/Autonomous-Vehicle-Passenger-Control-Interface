Reproducibility Protocol

Objective

The project is structured so that another researcher can understand how a research claim would be generated from:

Research question
→ hypothesis
→ variable
→ instrument
→ dataset
→ analysis
→ result
→ interpretation
→ design decision

---

Repository Reproducibility

The repository separates:

- source PRD
- research documentation
- design documentation
- experimental protocol
- data
- analysis
- manuscript
- presentation

This separation allows each stage to be inspected independently.

---

Dataset Reproducibility

Synthetic demonstration data are generated using:

analysis/data/synthetic/generate_synthetic_data.py

The generator uses a fixed random seed.

Therefore:

same code + same seed
=
same synthetic dataset

---

Empirical Data Reproducibility

For genuine participant data:

1. preserve the original export;
2. anonymise participant identifiers;
3. document exclusions;
4. apply predefined cleaning rules;
5. run the analysis pipeline;
6. preserve generated outputs;
7. record the analysis version.

---

Claim Reproducibility

Every empirical claim should identify:

- dataset
- variable
- analysis
- relevant comparison
- uncertainty
- evidence status

Synthetic results must be labelled separately.

---

Reproducibility Status

Component| Status
Research questions| Complete
Experimental design| Complete
Data schema| Complete
Synthetic demonstration dataset| Complete
Analysis architecture| Complete
Empirical dataset| Not claimed
Statistical empirical conclusions| Not claimed
Design interpretation framework| Complete
Manuscript| Complete
Traceability| Complete

---

Integrity Principle

A reproducible project is not one that hides uncertainty.

A reproducible project makes uncertainty visible.
