Empirical Results — EV-1.0

1. Study Status

This document defines the final reporting structure for empirical evaluation of EV-1.0.

The analysis distinguishes:

1. observed empirical results,
2. descriptive summaries,
3. statistical inference,
4. qualitative observations,
5. design interpretation,
6. product targets from the original PRD.

PRD targets are not treated as empirical findings.

«Integrity rule: No participant value, statistical result, effect size, confidence interval, significance test, or qualitative finding may be populated unless supported by actual collected data.»

---

2. Experimental Conditions

Condition| Description| Example
A| No explanation| Vehicle slows without explanatory card
B| Minimal explanation| “Slowing for pedestrian.”
C| Contextual explanation| “Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.”

The primary comparison is between explanation conditions rather than between different autonomous-driving behaviours.

---

3. Primary Outcome

Objective Comprehension

Operational variable: "comprehension_correct"

Binary scoring:

- "1" = participant correctly interpreted the relevant vehicle behaviour/cause.
- "0" = incorrect interpretation.

Where appropriate:

"comprehension_score = correct comprehension responses / valid comprehension trials"

---

4. Secondary Outcomes

Response Time

"response_time_ms"

Time from task presentation to valid response.

Trust

"trust_score"

Post-condition trust measure using the predefined study instrument.

Trust is interpreted as calibration, not maximisation.

Workload

"workload_score"

Perceived cognitive workload measured using the predefined instrument.

Perceived Understanding

"perceived_understanding"

Participant's subjective assessment of how well they understood the vehicle's behaviour.

Task Success

"task_success"

Whether the participant completed the required interaction without assistance or invalid interaction.

Interaction Error

"interaction_error"

Recorded interaction failures, including incorrect controls, missed controls, or unintended actions.

---

5. Dataset Overview

Complete only from the actual dataset.

Participants:
Valid participants:
Excluded participants:
Valid trials:
Excluded trials:
Condition A trials:
Condition B trials:
Condition C trials:

---

6. Exclusion Summary

Exclusion category| Count| Reason
Technical issue| [actual]| [documented reason]
Protocol deviation| [actual]| [documented reason]
Missing response| [actual]| [documented reason]
Trial interruption| [actual]| [documented reason]
Participant withdrawal| [actual]| [documented reason]
Invalid trial| [actual]| [documented reason]

---

7. Primary Comprehension Result

Condition A:
Condition B:
Condition C:

Observed pattern:
Statistical result:
Effect estimate:
Confidence interval:
Interpretation:

---

8. Secondary Results

Response Time

Condition A:
Condition B:
Condition C:
Statistical test:
Effect:
Interpretation:

Trust

Condition A:
Condition B:
Condition C:
Statistical test:
Effect:
Interpretation:

Workload

Condition A:
Condition B:
Condition C:
Statistical test:
Effect:
Interpretation:

Perceived Understanding

Condition A:
Condition B:
Condition C:
Statistical test:
Effect:
Interpretation:

Task Success

Condition A:
Condition B:
Condition C:
Observed completion:
Error rate:
Interpretation:

---

9. Interpretation Rule

If contextual explanations improve comprehension:

«The evidence supports the interpretation that additional contextual information can improve passenger interpretation under the tested conditions.»

If minimal explanations perform similarly:

«The evidence does not establish that additional contextual detail provides a measurable comprehension advantage under the tested conditions.»

If no-explanation performs similarly:

«The observed data do not establish a measurable comprehension benefit from the tested explanation presentation.»

No conclusion should exceed the design and dataset.

---

10. Trust Interpretation

Trust is treated as a calibration construct.

The analysis therefore asks:

«Did participants understand the vehicle sufficiently to form an appropriate level of trust?»

rather than:

«Which interface produced the highest trust?»

A high trust score accompanied by poor comprehension should not automatically be interpreted as a positive outcome.

---

11. Workload Interpretation

Comprehension| Workload| Interpretation
High| Low| Efficient explanation
High| High| Informative but cognitively expensive
Low| Low| Insufficient information
Low| High| Poor information design

---

12. Objective vs Subjective Understanding

Two constructs remain separate.

Objective understanding

What the participant actually inferred.

Perceived understanding

What the participant believes they understood.

A divergence between the two is itself a Human Factors finding.

---

13. Evidence Boundary

The original PRD contains product-level success targets.

Those targets are not converted into observed results unless empirical data support them.

---

14. Final Status

Methodology: COMPLETE
Experimental specification: COMPLETE
Analysis framework: COMPLETE
Design interpretation: READY
