Reproducible Results Framework

Autonomous Vehicle Passenger Control Interface

Empirical Analysis and Results Reproducibility Framework

---

1. Purpose

This document defines the reproducible workflow used to transform collected experimental observations into validated statistical results, figures, tables, and research-paper findings.

The framework ensures that every empirical claim can be traced back to the original recorded data.

---

2. Reproducibility Chain

The project follows:

Participant Observation
        ↓
Raw Dataset
        ↓
Data Validation
        ↓
Cleaning
        ↓
Analysis Dataset
        ↓
Statistical Analysis
        ↓
Tables / Figures
        ↓
Interpretation
        ↓
Research Paper

Each stage must preserve traceability to the preceding stage.

---

3. Source of Truth

The raw dataset is the primary empirical source.

Raw data must be:

- preserved;
- never overwritten;
- stored separately from cleaned data;
- backed up where appropriate;
- accompanied by a data dictionary;
- protected from accidental modification.

Recommended structure:

data/
├── README.md
├── raw/
├── cleaned/
└── codebook/

---

4. Raw Dataset Policy

Files inside:

data/raw/

represent the original recorded observations.

Raw files should not be manually edited for analysis.

Corrections should instead be implemented through a documented cleaning process that produces a separate cleaned dataset.

---

5. Cleaned Dataset

The cleaned dataset is generated from the raw dataset.

Cleaning may include:

- standardising variable names;
- validating condition codes;
- converting measurement formats;
- identifying missing values;
- flagging invalid trials;
- identifying protocol deviations;
- checking impossible values;
- preparing analysis-ready variables.

Every transformation must be documented.

---

6. Required Variables

The minimum analytical dataset should contain:

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

Additional variables may be retained where they are defined in the final protocol.

---

7. Condition Coding

The experimental condition variable is:

A = No Explanation
B = Minimal Explanation
C = Contextual Explanation

Condition labels must remain consistent across:

- raw data;
- cleaned data;
- analysis scripts;
- figures;
- tables;
- paper;
- presentation.

---

8. Validation Checks

Before analysis, the dataset should be checked for:

Structural validity

- required columns present;
- unique participant/trial identifiers;
- valid condition codes;
- valid scenario identifiers.

Measurement validity

- comprehension values within permitted range;
- response times in valid units;
- trust scores within instrument range;
- workload scores within instrument range.

Logical validity

Examples:

Invalid trial → not treated as valid completion
Technical issue → recorded explicitly
Missing response → NA
Protocol deviation → flagged

---

9. Data Quality Flags

The following flags may be used:

TECHNICAL_ISSUE
PROTOCOL_DEVIATION
MISSING_RESPONSE
TRIAL_INTERRUPTED
PARTICIPANT_WITHDRAWAL
INVALID_TRIAL

Flags should remain attached to the relevant observation during analysis.

---

10. Analysis Dataset

The analysis dataset is derived from the cleaned dataset.

It should contain:

- validated variables;
- documented transformations;
- analysis-relevant exclusions;
- condition labels;
- measurement variables;
- metadata required for reproducibility.

The analysis dataset must never contain unexplained manual modifications.

---

11. Descriptive Results Pipeline

For every major outcome:

Outcome
→ Condition-level summary
→ Distribution inspection
→ Missing-data inspection
→ Validity check
→ Appropriate inferential analysis
→ Effect size
→ Uncertainty
→ Interpretation

---

12. Primary Results Pipeline

The primary result is:

"comprehension_score"

The pipeline is:

comprehension_score
        ↓
Condition A summary
Condition B summary
Condition C summary
        ↓
Distribution / design assessment
        ↓
Appropriate statistical comparison
        ↓
Effect size
        ↓
Confidence interval where appropriate
        ↓
Interpretation

No numerical result is entered manually into the research paper.

---

13. Secondary Results Pipeline

Each secondary outcome follows the same procedure.

Response Time

response_time_ms
→ descriptive analysis
→ distribution assessment
→ condition comparison
→ effect size
→ interpretation

Trust

trust_score
→ descriptive analysis
→ condition comparison
→ effect size
→ interpretation

Workload

workload_score
→ descriptive analysis
→ condition comparison
→ effect size
→ interpretation

Perceived Understanding

perceived_understanding
→ descriptive analysis
→ condition comparison
→ relationship with objective comprehension

Task Performance

task_success
interaction_error
→ frequency / proportion
→ condition comparison where justified
→ interpretation

---

14. Figure Generation

Figures should be generated directly from the analysis dataset.

Potential figures include:

1. comprehension by explanation condition;
2. response time by condition;
3. trust by condition;
4. workload by condition;
5. perceived understanding by condition;
6. objective comprehension versus perceived understanding;
7. trust versus comprehension;
8. workload versus comprehension.

Only figures supported by the actual dataset should appear in the final paper.

---

15. Table Generation

Potential research tables include:

Table 1 — Dataset Description

Participant/trial information actually collected.

Table 2 — Condition-Level Descriptive Statistics

Condition A/B/C summaries.

Table 3 — Primary Outcome Analysis

Comprehension comparison.

Table 4 — Secondary Outcomes

Trust, workload, response time, perceived understanding, and task performance.

Table 5 — Effect Sizes

Relevant effect-size estimates and uncertainty.

Table 6 — Hypothesis Summary

Observed evidence for H1–H6.

---

16. Hypothesis Reporting

Each hypothesis should ultimately be reported using:

Hypothesis
→ Variables
→ Analysis
→ Observed result
→ Effect / uncertainty
→ Interpretation
→ Evidence status

Possible evidence-status labels:

- Supported by observed data;
- Not supported by observed data;
- Inconclusive;
- Exploratory;
- Not testable with available data.

These labels must reflect the actual analysis.

---

17. Statistical Output Integrity

Statistical output must not be copied selectively.

If an analysis produces:

- significant results;
- non-significant results;
- unexpected results;
- null results;

all relevant outcomes must be retained in the project analysis record.

Unexpected results are not evidence of a failed project.

---

18. Sensitivity Analysis

Where methodologically justified, sensitivity analyses may examine whether conclusions change under reasonable analytical alternatives.

Examples:

- inclusion versus exclusion of predefined invalid trials;
- parametric versus non-parametric analysis;
- alternative treatment of a documented data-quality issue.

Sensitivity analyses must be clearly labelled.

They must not be used to search for a preferred result.

---

19. Qualitative Integration

Quantitative results may be interpreted alongside qualitative observations.

The integration framework is:

Quantitative Pattern
        +
Observed Participant Comment / Behaviour
        ↓
Human Factors Interpretation

Qualitative observations must originate from actual participant records.

No participant quote or observation may be invented.

---

20. Evidence-to-Design Pipeline

The final project connects empirical evidence to design through:

Observed Data
        ↓
Human Factors Interpretation
        ↓
Design Implication
        ↓
Interface Decision
        ↓
Prototype Revision

A design decision should identify the evidence supporting it.

---

21. Research Paper Traceability

Each empirical statement in the final paper should be traceable to one or more of:

- raw dataset;
- cleaned dataset;
- statistical output;
- figure;
- table;
- qualitative record;
- methodological documentation.

---

22. Presentation Traceability

The final presentation should use the same validated results as the research paper.

No separate or manually altered statistics should be introduced into the presentation.

The presentation should not simplify findings in a way that changes their meaning.

---

23. Version Control

Recommended analysis versions:

analysis/
├── analysis-plan.md
├── statistical-analysis-specification.md
├── data-quality-assurance.md
├── analysis-readiness-report.md
├── reproducible-results-framework.md
├── data-dictionary.md
├── data/
├── notebooks/
└── figures/

Each major analytical change should be recorded in Git.

---

24. Recommended Commit Structure

Example:

Day 40: Complete statistical analysis specification and reproducible results framework

Future analysis commits may use:

Generate descriptive statistics
Validate primary outcome analysis
Generate condition comparison figures
Complete secondary outcome analysis
Complete hypothesis evaluation
Finalize empirical results

---

25. Reproducibility Checklist

Before results are included in the final paper:

- [ ] Raw dataset preserved
- [ ] Data dictionary complete
- [ ] Cleaning rules documented
- [ ] Invalid trials identified
- [ ] Missing data documented
- [ ] Protocol deviations documented
- [ ] Analysis dataset generated
- [ ] Primary outcome analysed
- [ ] Secondary outcomes analysed
- [ ] Appropriate statistical tests selected
- [ ] Effect sizes reported where appropriate
- [ ] Uncertainty reported where appropriate
- [ ] Figures generated from data
- [ ] Tables generated from data
- [ ] Hypotheses mapped to actual results
- [ ] Null results retained
- [ ] Qualitative findings verified
- [ ] Paper results match analysis output
- [ ] Presentation results match paper
- [ ] No fabricated values
- [ ] No unsupported claims

---

26. Final Integrity Rule

The project follows a strict principle:

«The analysis must follow the data; the data must never be made to follow the desired conclusion.»

The purpose of reproducibility is not merely technical correctness. It establishes a defensible chain between participant observations, statistical analysis, Human Factors interpretation, and interface design decisions.
