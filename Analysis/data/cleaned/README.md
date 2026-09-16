Cleaned Data

Cleaned data are derived from the raw dataset using documented validation and transformation rules.

Pipeline

RAW
 ↓
Schema validation
 ↓
Missing-data checks
 ↓
Range checks
 ↓
Logical consistency checks
 ↓
Quality-flag review
 ↓
Condition verification
 ↓
Analysis-ready dataset

Cleaning Principles

Cleaning must never change an observed response merely because it produces a more desirable result.

Every transformation must be reproducible.

Excluded observations must retain their exclusion reason.

Required Quality Flags

TECHNICAL_ISSUE
PROTOCOL_DEVIATION
MISSING_RESPONSE
TRIAL_INTERRUPTED
PARTICIPANT_WITHDRAWAL
INVALID_TRIAL

Output

The final analysis dataset should contain only observations that satisfy the predefined inclusion criteria.

A separate exclusion log should document every removed trial or participant.
