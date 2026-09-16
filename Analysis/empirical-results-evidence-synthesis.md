Empirical Results, Findings, and Evidence Synthesis

Project

Autonomous Vehicle Passenger Control Interface

Research Focus

Passenger-facing explanations for unexpected autonomous-vehicle behaviour.

Primary Research Question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

---

Day 41 — Empirical Results Template

1. Purpose

This document defines the final empirical-results structure for EV-1.0.

The purpose is not to produce attractive numbers. It is to provide a reproducible structure through which observations can be transformed into defensible Human Factors findings.

The experimental intervention consists of three explanation conditions:

Condition| Description
A| No explanation
B| Minimal explanation
C| Contextual explanation

The experimental conditions are derived from the product's explanation-card concept, where the interface communicates what the vehicle noticed, what it is doing, and the consequence for the passenger.

---

2. Dataset Status

Current empirical status: "[UPDATE ONLY AFTER ACTUAL DATA COLLECTION]"

Possible statuses:

- "ANALYSIS_READY — NO PARTICIPANT DATA"
- "DATA_COLLECTION_IN_PROGRESS"
- "DATA_COLLECTION_COMPLETE"
- "ANALYSIS_COMPLETE"

No numerical result may be entered unless it can be traced to the underlying dataset.

---

3. Dataset Overview

Report:

- number of participants
- number of trials
- number of scenarios
- number of observations per condition
- completed trials
- excluded trials
- missing responses
- protocol deviations
- technical interruptions

Reporting table

Measure| Value
Participants| "[N]"
Total trials| "[N]"
Valid trials| "[N]"
Excluded trials| "[N]"
Condition A| "[N]"
Condition B| "[N]"
Condition C| "[N]"

---

4. Data Quality

Before interpreting outcomes, verify:

Participant-level integrity

- unique participant identifiers
- no duplicate participant records
- complete condition assignment
- valid consent status
- withdrawal status recorded where applicable

Trial-level integrity

- valid scenario ID
- valid explanation condition
- valid response
- response-time integrity
- task completion status
- technical issue status
- protocol-deviation status

Missingness

Missing observations must be classified rather than silently deleted.

Recommended categories:

- "MISSING_RESPONSE"
- "TRIAL_INTERRUPTED"
- "TECHNICAL_ISSUE"
- "PROTOCOL_DEVIATION"
- "PARTICIPANT_WITHDRAWAL"
- "INVALID_TRIAL"

---

5. Primary Outcome — Comprehension

Operational definition

Comprehension represents whether the participant correctly understands the reason for the autonomous vehicle's unexpected behaviour.

Variables

"comprehension_score"

and/or

"comprehension_correct"

The primary analysis should use the prespecified scoring method documented in the experimental protocol.

Results structure

Condition| Valid observations| Correct| Incorrect| Accuracy
A — No explanation| "[N]"| "[N]"| "[N]"| "[x%]"
B — Minimal| "[N]"| "[N]"| "[N]"| "[x%]"
C — Contextual| "[N]"| "[N]"| "[N]"| "[x%]"

Interpretation

Do not equate perceived understanding with objective comprehension.

The central question is:

«Did participants actually identify what caused the vehicle behaviour and what the vehicle was doing?»

---

6. Response Time

Measure:

"response_time_ms"

Report:

- mean and SD where appropriate
- median and IQR when distributions are skewed
- condition-level distributions
- exclusions and their rationale

Response time should not be interpreted independently from comprehension.

A faster response with poorer comprehension does not necessarily represent improved usability.

---

7. Trust

Trust is a secondary outcome.

The objective is calibrated trust, rather than maximizing trust.

Report:

- condition-level trust
- distribution
- uncertainty
- relationship with comprehension
- relationship with workload

Interpretation should avoid statements such as:

«"More trust is always better."»

Instead:

«The relevant Human Factors question is whether passenger confidence appropriately reflects their understanding of the automated system's behaviour.»

---

8. Cognitive Workload

Measure:

"workload_score"

Where NASA-TLX or another prespecified workload instrument is used, retain the documented scoring procedure.

Report:

- overall workload
- condition-level comparison
- relevant subdimensions if justified
- relationship with comprehension

A contextual explanation should not automatically be interpreted as superior if it improves comprehension while substantially increasing workload.

---

9. Perceived Understanding

Measure:

"perceived_understanding"

This construct is deliberately separated from objective comprehension.

Four possible patterns are particularly important:

Objective comprehension| Perceived understanding| Interpretation
High| High| aligned understanding
High| Low| under-confidence
Low| High| possible over-confidence
Low| Low| limited understanding

The third pattern is particularly important for trust calibration.

---

10. Task Performance

Where applicable, report:

- task success
- task completion
- interaction error
- unnecessary interaction
- abandonment

Task success should remain subordinate to safety-critical constraints.

The explanation mechanism must not obstruct persistent safety controls.

---

11. Statistical Analysis

The statistical procedure follows the analysis specification established previously.

For each outcome:

1. inspect distribution and measurement characteristics
2. verify missingness
3. verify condition coding
4. select the prespecified test
5. report effect size
6. report uncertainty
7. interpret magnitude rather than statistical significance alone

No post-hoc test should be selected merely because it produces a preferred result.

---

12. Hypothesis Evaluation

H1 — Explanation presence and comprehension

«Participants receiving an explanation will demonstrate different comprehension performance from participants receiving no explanation.»

Status:

"[SUPPORTED / NOT SUPPORTED / INCONCLUSIVE / NOT TESTABLE]"

Evidence:

"[RESULT]"

---

H2 — Explanation specificity

«Contextual explanations will produce different comprehension outcomes from minimal explanations.»

Status:

"[STATUS]"

Evidence:

"[RESULT]"

---

H3 — Explanation and trust

«Explanation condition will be associated with differences in passenger trust.»

Status:

"[STATUS]"

Evidence:

"[RESULT]"

---

H4 — Explanation and workload

«Explanation condition will be associated with differences in cognitive workload.»

Status:

"[STATUS]"

Evidence:

"[RESULT]"

---

H5 — Comprehension and trust calibration

«Objective comprehension and trust will show a meaningful relationship.»

Status:

"[STATUS]"

Evidence:

"[RESULT]"

---

H6 — Comprehension and workload

«Higher workload will be associated with differences in comprehension performance.»

Status:

"[STATUS]"

Evidence:

"[RESULT]"

---

13. Qualitative Findings

Qualitative observations should be coded rather than presented as anecdotes.

Suggested coding framework:

Explanation interpretation

- understood cause
- misunderstood cause
- understood action
- misunderstood action
- understood passenger impact

Trust

- reassurance
- uncertainty
- suspicion
- confidence
- perceived transparency

Workload

- information overload
- insufficient information
- visual search
- reading burden
- distraction
- cognitive effort

Language

- clear
- ambiguous
- technical
- reassuring
- unnecessarily verbose

---

14. Evidence-to-Design Matrix

Finding| Evidence| Design implication| Confidence
"[Finding]"| "[Measure]"| "[Decision]"| "[High/Moderate/Low]"
"[Finding]"| "[Measure]"| "[Decision]"| "[High/Moderate/Low]"

Design decisions must be traceable to evidence.

---

Day 42 — Findings Synthesis

The purpose of this stage is to move from isolated outcome variables to Human Factors interpretation.

The analysis should answer five questions:

1. What did passengers understand?
2. What did they believe they understood?
3. How much cognitive effort did understanding require?
4. How did explanation presentation relate to trust?
5. What does this imply for passenger-facing XAI?

---

Day 43 — Research Question Mapping

Research question| Evidence| Outcome| Interpretation
RQ1: Does explanation presence affect understanding?| Comprehension| "[RESULT]"| "[INTERPRETATION]"
RQ2: Does specificity matter?| A/B/C comparison| "[RESULT]"| "[INTERPRETATION]"
RQ3: What is the relationship with trust?| Trust + comprehension| "[RESULT]"| "[INTERPRETATION]"
RQ4: What is the workload implication?| Workload| "[RESULT]"| "[INTERPRETATION]"

Contextual factors such as timing, urgency, modality and passenger activity remain secondary/future dimensions unless they were actually manipulated and measured.

---

Day 44 — Human Factors Interpretation

The central analytical model is:

Unexpected vehicle event
        ↓
Passenger uncertainty
        ↓
Explanation condition
        ↓
Passenger interpretation
        ↓
┌──────────────┬───────────────┬───────────────┐
│ Comprehension│ Trust         │ Workload      │
└──────────────┴───────────────┴───────────────┘
        ↓
Passenger response

The interface should therefore be evaluated as a human-automation interaction system rather than merely as a visual design.

A successful explanation is not simply one that contains more information.

It is one that provides enough information for the passenger to construct an accurate interpretation of the automated behaviour without creating unnecessary cognitive demand.

---

Day 45 — Evidence Synthesis

Final evidence hierarchy

Level 1 — Direct empirical evidence

Results derived from actual participant observations.

Level 2 — Design-system evidence

Prototype behaviour, interaction specifications, accessibility checks and interface-state validation.

Level 3 — Literature evidence

Previously reviewed Human Factors, XAI, trust, situation-awareness and workload literature.

Level 4 — Design inference

Reasoned implications derived from the combination of empirical and theoretical evidence.

The final report must clearly distinguish these levels.

---

Evidence language

Use:

- "The data indicate..."
- "Participants demonstrated..."
- "The observed pattern suggests..."
- "This result is consistent with..."
- "The finding provides preliminary evidence..."
- "The result should be interpreted cautiously..."

Avoid:

- "This proves..."
- "This guarantees..."
- "This is objectively the best..."
- "Passengers will always..."
- "The interface is safer..."

---

Project-Level Finding Structure

Each final finding should follow:

Observation → Evidence → Interpretation → Design implication → Limitation

Example structure:

«Participants showed "[observed pattern]" under "[condition]". This was reflected in "[measure]". The pattern suggests "[Human Factors interpretation]". For the interface, this supports "[design implication]". However, "[limitation]" constrains the generalisability of this interpretation.»

---

Endpoint of the empirical-analysis phase

At the end of this phase, the repository contains:

- reproducible data-processing rules
- defined statistical procedures
- a formal results structure
- RQ-to-evidence mapping
- hypothesis evaluation structure
- qualitative coding framework
- evidence-to-design traceability
- explicit claim boundaries

No fabricated empirical result is introduced.
