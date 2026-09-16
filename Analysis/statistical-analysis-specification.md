Statistical Analysis Specification

Project

Autonomous Vehicle Passenger Control Interface

Research Focus

Designing Passenger-Facing Explanations for Autonomous Vehicle Behaviour: A Human Factors Approach to Understanding, Trust, and Cognitive Workload

---

1. Purpose

This document defines the statistical analysis strategy for the experimental evaluation of passenger-facing explanations of unexpected autonomous-vehicle behaviour.

The purpose is to ensure that:

- the analysis is specified before interpreting empirical results;
- primary and secondary outcomes are clearly separated;
- statistical tests are selected according to the actual experimental design and data characteristics;
- effect sizes and uncertainty are considered alongside statistical significance;
- missing data, protocol deviations, and invalid trials are handled transparently;
- null or non-significant findings are treated as legitimate results;
- no unsupported conclusions are introduced.

No numerical findings are reported in this document.

---

2. Experimental Structure

The frozen experimental version is:

EV-1.0

The principal independent variable is:

Variable| Role| Levels
"condition"| Independent variable| A, B, C

Explanation Conditions

Condition A — No Explanation

No passenger-facing explanation is presented.

Condition B — Minimal Explanation

A concise explanation communicates the immediate reason for the vehicle behaviour.

Example:

«“Slowing for pedestrian.”»

Condition C — Contextual Explanation

A concise explanation communicates the observed event, vehicle response, and passenger-relevant implication.

Example:

«“Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.”»

These examples represent the experimental structure and should not be treated as empirical findings.

---

3. Primary Research Question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

The primary statistical focus is passenger understanding, operationalised through comprehension.

---

4. Primary Outcome

4.1 Comprehension Score

Variable:

"comprehension_score"

The comprehension measure represents the participant's ability to correctly understand the reason for the autonomous vehicle's unexpected behaviour.

The exact scoring procedure must follow the finalized participant instrument and protocol.

If multiple comprehension items are used, the scoring rule must be defined before outcome analysis.

Possible representation:

- total correct responses;
- proportion correct;
- percentage correct.

The selected representation must remain consistent across participants.

---

4.2 Binary Comprehension

Variable:

"comprehension_correct"

Coding:

Code| Meaning
1| Correct
0| Incorrect
NA| Missing/invalid

Binary comprehension will be used for item-level or trial-level analysis where appropriate.

---

5. Secondary Outcomes

The following variables are secondary outcomes:

Variable| Construct
"response_time_ms"| Response efficiency
"trust_score"| Trust in automation
"workload_score"| Cognitive workload
"perceived_understanding"| Subjective understanding
"task_success"| Task performance
"interaction_error"| Interaction accuracy

Secondary outcomes should not replace the primary comprehension analysis.

---

6. Exploratory Variables

The following variables may support exploratory interpretation:

- "qualitative_note"
- "protocol_deviation"
- "technical_issue"
- "scenario_id"
- event type
- urgency/risk category
- passenger activity
- explanation timing
- modality
- accessibility-related observations

These variables should not automatically be treated as confirmatory predictors unless the experimental design explicitly supports such analysis.

---

7. Analysis Sequence

The analysis will follow this order:

Raw Data
    ↓
Data Integrity Check
    ↓
Data Cleaning
    ↓
Descriptive Statistics
    ↓
Distribution / Assumption Assessment
    ↓
Primary Outcome Analysis
    ↓
Secondary Outcome Analysis
    ↓
Effect Size Estimation
    ↓
Confidence Intervals / Uncertainty
    ↓
Exploratory Analysis
    ↓
Qualitative Analysis
    ↓
Integrated Interpretation

---

8. Descriptive Analysis

Before inferential analysis, descriptive statistics will be calculated for each experimental condition.

For continuous or approximately continuous variables:

- mean;
- standard deviation;
- median;
- interquartile range;
- minimum;
- maximum.

For categorical variables:

- frequency;
- percentage.

Descriptive analysis will be reported separately for Conditions A, B, and C.

No condition will be described as superior solely because its descriptive mean is larger or smaller.

---

9. Primary Analysis

9.1 Main Comparison

The primary analysis will evaluate whether comprehension differs across explanation conditions.

The final statistical test will depend on the actual experimental structure and distribution of the collected data.

If the experiment is within-subject

Potential approaches include:

- repeated-measures ANOVA for appropriate continuous approximately normal scores;
- Friedman test for non-parametric repeated-measures comparisons;
- paired post-hoc comparisons where justified.

If the experiment is between-subject

Potential approaches include:

- one-way ANOVA for appropriate continuous approximately normal outcomes;
- Kruskal–Wallis test where parametric assumptions are not appropriate;
- appropriate post-hoc comparisons where justified.

The final test must correspond to the actual protocol and collected dataset.

---

10. Binary Comprehension Analysis

For "comprehension_correct", analysis may use:

- condition-level proportions;
- paired categorical analysis for repeated observations where appropriate;
- contingency-table methods for independent observations;
- logistic modelling where sample size and experimental structure support it.

The selected method will be documented in the final analysis notebook.

---

11. Secondary Outcome Analysis

11.1 Response Time

Variable:

"response_time_ms"

Analysis considerations:

- distribution inspection;
- central tendency;
- variability;
- possible skew;
- condition-level comparison;
- effect size.

Response-time exclusions must be defined according to protocol and documented rather than selected after observing which values produce a preferred result.

---

11.2 Trust

Variable:

"trust_score"

Trust will be interpreted as a distinct construct from comprehension.

The analysis will examine whether trust scores differ between explanation conditions.

The interpretation will focus on the observed pattern rather than assuming that higher trust is inherently preferable.

The Human Factors objective is calibrated trust, not maximum trust.

---

11.3 Cognitive Workload

Variable:

"workload_score"

Workload will be analysed as a secondary outcome.

The analysis will examine whether explanation presentation is associated with differences in reported workload.

Higher or lower workload will not automatically be interpreted as better or worse without considering comprehension and task demands.

---

11.4 Perceived Understanding

Variable:

"perceived_understanding"

Perceived understanding will be analysed separately from objective comprehension.

This distinction is important because a participant may report high understanding while performing poorly on an objective comprehension measure, or vice versa.

---

11.5 Task Success and Interaction Errors

Variables:

- "task_success"
- "interaction_error"

These measures will be used to determine whether explanation presentation is associated with observable differences in task performance.

---

12. Objective vs Subjective Understanding

A dedicated comparison will be made between:

Objective Comprehension
        ↕
Perceived Understanding

Possible analyses include:

- descriptive comparison;
- correlation where appropriate;
- cross-tabulation for categorical measures;
- qualitative interpretation.

The purpose is to determine whether perceived understanding and demonstrated understanding behave as equivalent or distinct measures.

No assumption of equivalence will be made.

---

13. Trust–Comprehension Relationship

Trust and comprehension will be analysed as conceptually distinct constructs.

Where the dataset supports it, the analysis may examine their association.

Possible approaches include:

- Pearson correlation for appropriate continuous variables;
- Spearman correlation for ordinal/non-normal variables;
- descriptive comparison where assumptions are not satisfied.

Correlation will not be interpreted as evidence of causation.

---

14. Workload–Comprehension Relationship

Where sample size and measurement characteristics permit, the relationship between workload and comprehension may be explored.

The objective is to examine whether greater cognitive demand is associated with differences in understanding.

This is exploratory unless explicitly specified as a confirmatory hypothesis in the finalized protocol.

---

15. Effect Sizes

Statistical significance alone will not determine interpretation.

Where applicable, effect sizes will be reported, such as:

- Cohen's d;
- η² or partial η²;
- rank-based effect sizes;
- odds ratios;
- correlation coefficients.

The selected effect-size measure must match the statistical test.

Effect sizes will help distinguish:

Statistical Detectability
        ≠
Practical Importance

---

16. Uncertainty

Where appropriate, confidence intervals will be reported.

Confidence intervals will help communicate uncertainty around estimated differences and associations.

The analysis will avoid presenting point estimates as if they were exact population values.

---

17. Multiple Comparisons

If multiple pairwise comparisons are performed across Conditions A, B, and C, an appropriate correction procedure may be applied.

Potential approaches include:

- Holm correction;
- Bonferroni correction;
- another justified multiple-comparison procedure.

The selected procedure will be documented in the final analysis notebook.

---

18. Assumption Checking

Before applying parametric tests, relevant assumptions will be considered.

These may include:

- independence where applicable;
- approximate normality;
- homogeneity of variance;
- measurement scale;
- repeated-measures structure;
- presence of influential observations.

Visual inspection and appropriate diagnostic procedures will be preferred over relying on a single automated test.

If assumptions are not adequately satisfied, an alternative analysis will be selected and documented.

---

19. Missing Data

Missing observations will be coded as:

"NA"

Missingness will be classified where possible as:

- participant non-response;
- technical issue;
- protocol deviation;
- trial interruption;
- participant withdrawal;
- invalid trial.

Missing values will not be silently converted into zero.

Any exclusion or handling of missing observations will be documented.

---

20. Invalid Trials

Trials may be excluded from inferential analysis when predefined criteria indicate that the observation is invalid.

Potential reasons include:

- technical failure;
- incomplete trial;
- major protocol deviation;
- participant withdrawal;
- unusable response.

Every exclusion must be traceable to a documented reason.

---

21. Outlier Policy

Potential outliers will be identified using predefined statistical and contextual criteria.

An unusual observation will not be removed merely because it changes the result.

Each exclusion must have a methodological justification.

Where appropriate, analyses may be conducted both:

1. with the observation;
2. without the observation.

If such sensitivity analysis is performed, both analyses will be documented.

---

22. Scenario Effects

If multiple scenarios are used, scenario identity may contribute to variation in participant responses.

Therefore:

"scenario_id"

will be retained throughout the analysis pipeline.

Scenario-level patterns may be examined descriptively.

Scenario should not automatically be treated as an independent statistical predictor unless the experimental design and sample size support such analysis.

---

23. Risk and Urgency

Risk/urgency is a contextual variable rather than the primary independent variable in EV-1.0 unless explicitly manipulated.

If multiple risk levels are present, exploratory comparisons may be conducted.

The interpretation must distinguish:

«planned experimental manipulation»

from

«observed contextual variation.»

---

24. Explanation Timing

Explanation timing is an important theoretical factor in the research framework.

However, timing should only be analysed as an independent variable if it was deliberately manipulated and controlled within the experimental protocol.

If timing was held constant in EV-1.0, it will remain a design control rather than an inferential factor.

---

25. Passenger Activity

Passenger activity is similarly treated as a contextual variable unless deliberately manipulated.

Potential activities include:

- attentive/passenger monitoring;
- secondary digital activity;
- other controlled passenger tasks.

No conclusion about activity effects will be made unless supported by collected data.

---

26. Statistical Significance

A conventional significance threshold such as:

"α = 0.05"

may be used where appropriate and specified before inferential testing.

However:

«Statistical significance will not be treated as the sole criterion for determining whether an interaction design is meaningful.»

Interpretation will consider:

- effect size;
- uncertainty;
- direction;
- consistency;
- practical relevance;
- measurement quality;
- experimental limitations.

---

27. Null Results

A non-significant result will not be described as proof that no effect exists.

Appropriate interpretation may include:

«“The analysis did not provide sufficient evidence for a detectable difference under the conditions tested.”»

The final wording will depend on the actual result and uncertainty.

---

28. Hypothesis Mapping

Hypothesis| Primary variables| Analysis focus
H1| "condition", "comprehension_score"| Comprehension differences
H2| "condition", "comprehension_score", "trust_score"| Specificity-related differences
H3| "condition", "workload_score"| Workload differences
H4| "comprehension_score", "perceived_understanding"| Objective–subjective relationship
H5| "trust_score", "comprehension_score"| Trust–understanding relationship
H6| contextual variables| Exploratory moderation/context

---

29. Analysis Priority

The analysis hierarchy is:

Primary

Comprehension

Secondary

- response time;
- trust;
- workload;
- perceived understanding;
- task success;
- interaction errors.

Exploratory

- qualitative observations;
- scenario effects;
- contextual variables;
- relationships among constructs;
- protocol-related patterns.

This hierarchy prevents secondary outcomes from becoming post-hoc substitutes for the primary research question.

---

30. Interpretation Rules

The final interpretation must:

1. report the observed result;
2. report uncertainty where appropriate;
3. report effect magnitude where appropriate;
4. distinguish statistical significance from practical relevance;
5. distinguish association from causation;
6. acknowledge missing data and exclusions;
7. acknowledge protocol deviations;
8. report null findings;
9. avoid unsupported generalisation;
10. avoid production-level safety claims.

---

31. Reproducibility Requirement

Every reported numerical result in the final paper must be traceable to:

Raw Dataset
→ Cleaned Dataset
→ Analysis Script/Notebook
→ Statistical Output
→ Figure/Table
→ Written Interpretation

No manually invented numerical value may enter the final report.

---

32. Integrity Statement

This project does not permit:

- fabricated participant data;
- fabricated statistical significance;
- fabricated effect sizes;
- selective deletion of inconvenient observations;
- invented participant counts;
- invented confidence intervals;
- invented qualitative findings;
- unsupported causal claims.

All empirical findings must originate from the actual dataset collected under the defined protocol.

---

33. Final Analysis Principle

The objective of the analysis is not to demonstrate that one explanation condition is universally superior.

The objective is to determine what the collected evidence indicates about the relationship between explanation presentation and:

- passenger comprehension;
- trust;
- cognitive workload;
- perceived understanding;
- task performance.

The resulting evidence will then inform Human Factors and interface-design implications within the defined experimental scope.
