Experimental Data Schema

Project: Autonomous Vehicle Passenger Control Interface
Status: Data schema v1
Date: 23 September 2026

---

1. Purpose

This document defines the structure of the experimental dataset before data collection begins.

Predefining the data structure reduces ambiguity during collection and analysis.

---

2. Participant-Level Fields

Variable| Type| Description
participant_id| String| Anonymous participant identifier
age_group| Categorical| Predefined age category if collected
technical_experience| Categorical| Self-reported technology experience
autonomous_vehicle_experience| Categorical| Previous exposure to autonomous vehicles
accessibility_requirements| Categorical| Relevant self-reported requirements if ethically appropriate
session_date| Date| Date of experimental session
completion_status| Categorical| Complete / incomplete

Only variables justified by the research questions should be collected.

---

3. Trial-Level Fields

Variable| Type| Description
participant_id| String| Anonymous participant identifier
trial_id| String| Unique trial
scenario_id| String| Experimental scenario
explanation_condition| Categorical| None / Minimal / Contextual
scenario_order| Integer| Trial position
condition_order| Integer| Condition position
comprehension_response| Text/Categorical| Participant response
comprehension_score| Numeric| Predefined scoring
trust_score| Numeric| Selected trust measure
workload_score| Numeric| Selected workload measure
response_time| Numeric| If collected
interaction_error| Boolean/Numeric| If applicable
task_completion| Boolean| Completed / not completed
protocol_deviation| Boolean| Whether deviation occurred
deviation_notes| Text| Description if applicable

---

4. Scoring Principles

Scoring rules should be defined before analyzing the main dataset.

For comprehension, the scoring rubric should specify:

- correct response;
- partially correct response;
- incorrect response.

For subjective scales, the original instrument's scoring procedure should be followed.

No scoring rule should be changed after observing the results merely to obtain a preferred outcome.

---

5. Missing Data

Missing responses should be explicitly represented.

A missing value should not automatically be converted into:

- zero;
- incorrect;
- average score.

The treatment of missing data will be specified in the final analysis plan.

---

6. Exclusion Rules

Potential exclusion criteria may include:

- incomplete participation;
- technical failure that prevents meaningful exposure to the condition;
- failure to complete the required experimental procedure;
- predefined data-quality criteria.

The final exclusion criteria must be specified before the main analysis.

---

7. Public Repository

Raw participant data should not be uploaded to a public GitHub repository if they contain identifying or potentially re-identifying information.

The repository may instead contain:

- synthetic example data;
- anonymized aggregate results;
- analysis scripts;
- variable definitions;
- codebooks;
- figures;
- appropriately anonymized datasets where ethically and legally suitable.

---

8. Data Dictionary

A formal data dictionary should be created before the main experiment.

Each variable should have:

- variable name;
- definition;
- data type;
- possible values;
- measurement level;
- scoring procedure;
- missing-value convention.

---

9. Reproducibility

The final analysis should be reproducible from:

Raw/anonymized data → Cleaning → Derived variables → Statistical analysis → Figures/tables

The exact analysis workflow will be documented in the "analysis/" directory.

---

Status

Data schema: v1
Final variables: Pending questionnaire and experimental-protocol decisions
Next step: Create scenario scripts and finalize participant-facing instructions.
