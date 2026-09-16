DAY 41 — EMPIRICAL RESULTS TEMPLATE

File: "analysis/DAY-41-EMPIRICAL-RESULTS-TEMPLATE.md"

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

Exclusion Summary

Exclusion category| Count| Reason
Technical issue| [actual]| [documented reason]
Protocol deviation| [actual]| [documented reason]
Missing response| [actual]| [documented reason]
Trial interruption| [actual]| [documented reason]
Participant withdrawal| [actual]| [documented reason]
Invalid trial| [actual]| [documented reason]

---

DAY 42 — FINDINGS SYNTHESIS

File: "analysis/DAY-42-FINDINGS-SYNTHESIS.md"

Findings Synthesis

1. Purpose

The purpose of this analysis is to determine whether the observed data provide evidence concerning the effect of passenger-facing explanations on:

- objective understanding,
- response efficiency,
- trust,
- cognitive workload,
- perceived understanding,
- task performance.

The analysis does not assume that more explanation is inherently better.

---

2. Evidence Hierarchy

Interpret findings in this order:

1. Data quality
2. Primary comprehension outcome
3. Secondary outcomes
4. Statistical evidence
5. Effect magnitude
6. Qualitative observations
7. Cross-measure interpretation
8. Design implications

A design recommendation should not be based solely on subjective preference when objective comprehension provides contradictory evidence.

---

3. Primary Finding

Research question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

Primary outcome

"comprehension_correct"

Report

Condition A:
Condition B:
Condition C:

Observed pattern:
Statistical result:
Effect estimate:
Confidence interval:
Interpretation:

Interpretation rule

If contextual explanations improve comprehension:

«The evidence supports the interpretation that additional contextual information can improve passenger interpretation under the tested conditions.»

If minimal explanations perform similarly:

«The evidence does not establish that additional contextual detail provides a measurable comprehension advantage under the tested conditions.»

If no-explanation performs similarly:

«The observed data do not establish a measurable comprehension benefit from the tested explanation presentation.»

No conclusion should exceed the design and dataset.

---

4. Trust Interpretation

Trust is treated as a calibration construct.

The analysis therefore asks:

«Did participants understand the vehicle sufficiently to form an appropriate level of trust?»

Rather than:

«Which interface produced the highest trust?»

A high trust score accompanied by poor comprehension should not automatically be interpreted as a positive outcome.

A lower trust score accompanied by improved understanding may represent improved calibration rather than design failure.

---

5. Workload Interpretation

Explanation effectiveness must be evaluated against cognitive cost.

A useful interpretation matrix is:

Comprehension| Workload| Interpretation
High| Low| Efficient explanation
High| High| Informative but cognitively expensive
Low| Low| Insufficient information
Low| High| Poor information design

---

6. Objective vs Subjective Understanding

Two constructs remain separate:

Objective understanding

What the participant actually inferred.

Perceived understanding

What the participant believes they understood.

These measures must not be collapsed.

A divergence between the two is a Human Factors finding in itself.

---

DAY 43 — RQ AND HYPOTHESIS MAPPING

File: "analysis/DAY-43-RQ-HYPOTHESIS-MAPPING.md"

Research Question and Hypothesis Mapping

RQ1

«How does explanation presentation affect passenger understanding?»

Primary measure: comprehension.

Evidence: objective comprehension performance.

---

RQ2

«Does explanation presence improve understanding compared with no explanation?»

Comparison: A vs B/C.

Interpretation: Based exclusively on observed comprehension data.

---

RQ3

«Does explanation specificity affect comprehension and trust?»

Comparison: B vs C.

The purpose is to determine whether additional contextual information produces measurable benefit without assuming that greater information density is preferable.

---

RQ4

«How does explanation presentation relate to cognitive workload?»

Measures:

- workload score,
- response time,
- interaction errors.

---

RQ5

«Is increased trust accompanied by increased understanding?»

This examines the relationship between trust and comprehension.

The project explicitly avoids treating trust as an isolated success metric.

---

Hypothesis Register

Hypothesis| Prediction| Evidence| Status
H1| Explanations improve comprehension| comprehension| [supported/not supported/inconclusive]
H2| Explanations improve perceived understanding| perceived understanding| [status]
H3| Contextual explanations improve comprehension over minimal explanations| A/B/C comparison| [status]
H4| Explanation presentation affects trust| trust score| [status]
H5| Explanation presentation affects workload| workload| [status]
H6| Better understanding is associated with better calibrated trust| comprehension + trust| [status]

Decision language

Use:

- Supported
- Not supported
- Inconclusive
- Not tested
- Exploratory

Avoid:

- proved
- guaranteed
- definitively established
- universally better

---

DAY 44 — EVIDENCE TO DESIGN

File: "analysis/DAY-44-EVIDENCE-TO-DESIGN.md"

Evidence-to-Design Synthesis

1. Core Design Question

The central design problem is not:

«“How can the system explain everything?”»

It is:

«“How can the system provide enough information for passengers to understand unexpected behaviour without creating unnecessary cognitive demand?”»

---

2. Explanation Integrity Framework

Every explanation should satisfy five requirements.

1. Factuality

The explanation must correspond to the system's actual decision context.

2. Relevance

Only information relevant to the passenger's current situation should be foregrounded.

3. Temporal Coupling

The explanation should appear close enough to the triggering event to preserve the connection between behaviour and explanation.

The original PRD specifies approximately one-second surfacing for decision/explanation events.

4. Passenger Impact

The explanation should communicate what the event means for the passenger.

5. Progressive Disclosure

The primary card should remain concise, with deeper information available on demand.

---

3. Passenger Explanation Framework

The final framework is:

EVENT
  ↓
CAUSE
  ↓
ACTION
  ↓
PASSENGER IMPACT
  ↓
OPTIONAL DEEPER INFORMATION

Example

Event

Unexpected slowing.

Cause

Pedestrian entering crossing.

Action

Vehicle slows to maintain distance.

Passenger impact

Arrival remains approximately unchanged.

Optional deeper information

Expanded route/perception explanation.

---

4. Design Decision Matrix

Evidence question| Design response
Is understanding improved?| Preserve explanation mechanism
Does additional detail increase workload?| Reduce foreground density
Does minimal text adequately explain behaviour?| Prefer concise default
Does contextual information add useful understanding?| Offer progressive detail
Does trust diverge from comprehension?| Reconsider trust-oriented copy
Are safety interactions affected by explanation density?| Preserve safety hierarchy
Do accessibility modes change comprehension?| Preserve semantic equivalence

---

5. Safety Invariant

Explanation content must never compete with safety-critical controls.

The original PRD requires the safety control to remain persistently accessible and prevents critical interactions from depending on time-limited or gesture-only interaction.

Therefore:

SAFETY
  >
ACTIVE VEHICLE STATE
  >
EXPLANATION
  >
SECONDARY INFORMATION
  >
ENTERTAINMENT

---

DAY 45 — HUMAN FACTORS INTERPRETATION

File: "analysis/DAY-45-HUMAN-FACTORS-INTERPRETATION.md"

Human Factors Interpretation

1. Situation Awareness

Unexpected vehicle behaviour creates an information gap:

Vehicle behaviour
      ↓
Passenger notices deviation
      ↓
Passenger asks "Why?"
      ↓
Interpretation
      ↓
Trust / concern / action

The explanation card intervenes between unexpected behaviour and passenger interpretation.

---

2. Mental Model Support

The interface is not intended to expose the complete autonomous-driving stack.

Instead, it provides a passenger-appropriate mental model:

What happened?
Why?
What is the vehicle doing?
What does this mean for me?

This avoids overwhelming passengers with raw perception or engineering data.

The PRD similarly specifies abstracted sensor outputs rather than exposing raw LiDAR, camera, or radar feeds.

---

3. Cognitive Compatibility

The information architecture follows the passenger's natural questions rather than the internal architecture of the vehicle.

Bad structure:

Sensor → classifier → planner → controller

Passenger-oriented structure:

Situation → reason → action → consequence

---

4. Calibrated Trust

The project adopts:

«Understanding before reassurance.»

The system should not use explanation primarily as persuasive language.

The purpose is to give passengers sufficient information to form an appropriately calibrated mental model of the vehicle.

---

5. Accessibility

Accessibility is treated as an interaction architecture rather than a visual afterthought.

The PRD requires:

- screen-reader operation,
- logical focus order,
- wheelchair-related boarding information,
- captions and visual equivalents,
- voice operation,
- large text,
- high contrast,
- simplified cognitive mode.

The final principle is:

«Semantic equivalence across modalities, not identical presentation across modalities.»

A visual explanation may become a spoken explanation, but the underlying information hierarchy must remain equivalent.

---

6. Final Human Factors Principle

The final design principle is:

«Explain enough to support understanding, but not so much that the explanation itself becomes the new source of cognitive load.»

This principle connects comprehension, workload, trust, accessibility, and safety into one design framework.
