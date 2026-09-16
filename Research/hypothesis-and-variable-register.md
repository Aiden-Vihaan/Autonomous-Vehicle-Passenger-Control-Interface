Hypothesis and Variable Register

Autonomous Vehicle Passenger Control Interface

---

1. Purpose

This register provides the controlled reference for all hypotheses and research variables used in the project.

It prevents ambiguity between:

- theoretical constructs;
- experimental variables;
- measured outcomes;
- contextual factors;
- exploratory variables.

---

2. Hypothesis Register

ID| Hypothesis| Status| Primary Variables
H1| Explanation presentation will be associated with differences in passenger comprehension compared with no explanation.| Testable| Condition, comprehension
H2| Explanation specificity will be associated with differences in comprehension and trust-related responses.| Testable| Condition, comprehension, trust
H3| Explanation specificity will be associated with differences in perceived cognitive workload.| Testable| Condition, workload
H4| Objective comprehension and perceived understanding will not necessarily be equivalent.| Testable| Comprehension, perceived understanding
H5| Trust-related responses and comprehension will represent related but distinct passenger outcomes.| Testable| Trust, comprehension
H6| Contextual factors may moderate the usefulness of passenger-facing explanations.| Exploratory / future| Timing, event, activity, modality

---

3. Independent Variable Register

IV-01 — Explanation Condition

Variable name: "condition"

Type: Categorical

Levels:

- A — No explanation
- B — Minimal explanation
- C — Contextual explanation

Role: Primary experimental manipulation.

---

4. Primary Dependent Variable Register

DV-01 — Comprehension Score

Variable name: "comprehension_score"

Type: Numeric score

Role: Primary dependent variable.

Construct: Passenger comprehension.

Purpose: Determine how accurately participants understand unexpected autonomous-vehicle behaviour.

---

DV-02 — Comprehension Correctness

Variable name: "comprehension_correct"

Type: Binary

Coding:

- "1" = correct
- "0" = incorrect
- "NA" = missing/invalid

Role: Secondary representation of the primary comprehension outcome.

---

5. Secondary Dependent Variables

DV-03 — Response Time

Variable name: "response_time_ms"

Type: Continuous

Unit: milliseconds

Construct: Processing/response efficiency.

---

DV-04 — Trust

Variable name: "trust_score"

Type: Scale score

Construct: Trust in automation.

Interpretation: Trust is examined in relation to understanding and calibration rather than as an isolated positive outcome.

---

DV-05 — Workload

Variable name: "workload_score"

Type: Scale score

Construct: Cognitive workload.

Planned instrument: NASA-TLX.

---

DV-06 — Perceived Understanding

Variable name: "perceived_understanding"

Type: Self-report

Construct: Subjective understanding.

---

DV-07 — Task Success

Variable name: "task_success"

Type: Binary

Coding:

- "1" = successful
- "0" = unsuccessful
- "NA" = invalid/interrupted

---

DV-08 — Interaction Error

Variable name: "interaction_error"

Type: Binary/categorical coding

Construct: Interaction reliability.

---

6. Exploratory Variables

EV-01 — Qualitative Note

Variable name: "qualitative_note"

Possible content:

- participant comments;
- confusion;
- preferences;
- interpretation difficulties;
- accessibility observations;
- unexpected interaction behaviour.

---

EV-02 — Protocol Deviation

Variable name: "protocol_deviation"

Records deviations from the predefined experimental procedure.

---

EV-03 — Technical Issue

Variable name: "technical_issue"

Records technical problems affecting a trial or participant session.

---

7. Contextual Variables

Potential contextual variables include:

- "scenario_id"
- event type;
- event urgency;
- explanation timing;
- passenger activity;
- modality;
- accessibility requirement.

These variables should only be included in formal inferential analysis if they are actually manipulated or systematically recorded.

---

8. Variable Classification

Variable| Classification
"condition"| Independent variable
"comprehension_score"| Primary dependent variable
"comprehension_correct"| Primary outcome representation
"response_time_ms"| Secondary dependent variable
"trust_score"| Secondary dependent variable
"workload_score"| Secondary dependent variable
"perceived_understanding"| Secondary dependent variable
"task_success"| Secondary dependent variable
"interaction_error"| Secondary dependent variable
"qualitative_note"| Exploratory variable
"protocol_deviation"| Quality-control variable
"technical_issue"| Quality-control variable

---

9. Data Integrity Rules

Rule 1

Variable names must remain consistent between data collection, cleaning, analysis, and reporting.

Rule 2

Missing values must not be silently converted into zero.

Rule 3

Invalid trials must be flagged rather than deleted without documentation.

Rule 4

Technical issues must be recorded separately from participant errors.

Rule 5

Protocol deviations must remain traceable.

Rule 6

Raw data must remain immutable.

Rule 7

No value may be manually changed to improve an apparent result.

---

10. Analysis Priority

Primary

1. Comprehension

Secondary

2. Response time
3. Trust
4. Workload
5. Perceived understanding
6. Task success
7. Interaction errors

Exploratory

8. Qualitative observations
9. Contextual effects

This hierarchy should be preserved during final analysis and paper writing.

---

11. Interpretation Priority

The project should interpret results in this order:

Comprehension
     ↓
Trust + Workload
     ↓
Task Performance
     ↓
Subjective Experience
     ↓
Qualitative Explanation
     ↓
Design Implications

This prevents subjective satisfaction or trust from replacing the project's primary Human Factors outcome.

---

12. Final Variable Model

                    CONDITION
                     A / B / C
                         │
                         ↓
               ┌─────────────────┐
               │   PRIMARY DV    │
               │  COMPREHENSION  │
               └─────────────────┘
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       RESPONSE         TRUST        WORKLOAD
         TIME                           │
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                  TASK OUTCOMES
                         │
                         ↓
                DESIGN IMPLICATIONS

---

13. Final Research Integrity Statement

The hypothesis register defines questions to be tested.

It does not constitute evidence that any hypothesis is true.

The final paper must distinguish clearly between:

- hypothesised relationships;
- observed data;
- statistical results;
- interpretation;
- design implications.

No hypothesis may be reported as supported or rejected until the actual dataset has been analysed using the predefined methodology.
