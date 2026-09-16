Raw Data

Status

No fabricated participant observations are stored in this directory.

If genuine empirical data are collected, the original exported dataset should be placed here without modifying the original observations.

---

Raw Data Rules

Raw files must be:

- immutable
- anonymised
- versioned
- timestamped
- accompanied by a provenance note
- separated from cleaned analysis data

Never overwrite a raw dataset after collection.

---

Expected File

ev1_trials.csv

The expected schema is documented in:

analysis/data/codebook/codebook.md

---

Data Quality

Trials containing:

- technical failures
- protocol deviations
- missing required responses
- interruptions
- invalid trial states

must be flagged rather than silently deleted.

Exclusion decisions must be documented before inferential analysis.

---

Important Integrity Rule

Synthetic demonstration data belong in:

analysis/data/synthetic/

They must not be copied into this directory and presented as empirical observations.
