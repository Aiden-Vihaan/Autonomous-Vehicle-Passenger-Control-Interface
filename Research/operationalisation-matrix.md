Operationalisation Matrix

Autonomous Vehicle Passenger Control Interface

Research Topic

Passenger-facing explanations for unexpected autonomous-vehicle behaviour

---

1. Purpose

This document operationalises the theoretical and conceptual framework developed in the previous stages of the project.

It establishes a traceable relationship between:

Research Question
      ↓
 Hypothesis
      ↓
 Construct
      ↓
  Variable
      ↓
   Measure
      ↓
Experimental Condition
      ↓
   Analysis
      ↓
Interpretation

The purpose is to ensure that every research question can be connected to a measurable outcome and that every planned analysis has a clearly defined theoretical basis.

---

2. Primary Research Question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

The experimental manipulation is the explanation condition.

The primary outcome is passenger comprehension.

Trust and cognitive workload are treated as secondary outcomes.

---

3. Research Questions and Operationalisation

Research Question| Primary Construct| Variable| Measure| Analysis
RQ1. Does explanation presence affect passenger comprehension?| Comprehension| Comprehension score| Accuracy / score| Descriptive comparison; inferential analysis if justified
RQ2. Does explanation specificity affect comprehension and trust-related responses?| Comprehension; Trust| Condition; comprehension; trust| Score; trust scale| Condition-level comparison
RQ3. Does explanation timing influence passenger understanding?| Situation Awareness / Comprehension| Timing| Experimental timing condition, if tested| Timing comparison
RQ4. Does event risk or urgency influence explanation usefulness?| Risk interpretation| Scenario/event characteristic| Scenario coding| Stratified/exploratory analysis
RQ5. Does passenger activity influence explanation usefulness across modalities?| Multimodal interaction| Passenger activity/modality| Scenario and condition coding| Exploratory analysis

Scope Note

The core controlled experiment defined in EV-1.0 focuses on explanation conditions A/B/C.

Timing, risk/urgency, passenger activity, and multimodal interaction remain contextual or future experimental dimensions unless they are explicitly included in the final executed study.

---

4. Explanation Conditions

Condition A — No Explanation

The autonomous vehicle performs the relevant behaviour without a passenger-facing causal explanation.

Vehicle event
     ↓
Vehicle action
     ↓
No explanatory message

---

Condition B — Minimal Explanation

The interface communicates the immediate reason for the vehicle behaviour.

Example:

«Slowing for pedestrian.»

Vehicle event
     ↓
Vehicle action
     ↓
Short explanation

---

Condition C — Contextual Explanation

The interface communicates the relevant event and vehicle response with additional context.

Example:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

Vehicle event
     ↓
Vehicle action
     ↓
Contextual explanation

---

5. Independent Variable

Explanation Condition

Variable name: "condition"

Code| Condition
A| No explanation
B| Minimal explanation
C| Contextual explanation

Variable Type

Categorical independent variable with three experimental levels.

---

6. Primary Dependent Variable

Comprehension

Variable name: "comprehension_score"

Comprehension represents the participant's ability to correctly understand the cause and meaning of the autonomous vehicle's unexpected behaviour.

Possible components include:

1. Identification of the triggering event.
2. Identification of the vehicle response.
3. Interpretation of the immediate implication.

The precise scoring method must remain consistent across conditions.

---

7. Binary Comprehension Variable

Variable name: "comprehension_correct"

This variable provides a simplified representation of whether the participant achieved the predefined comprehension criterion.

Value| Meaning
1| Correct
0| Incorrect
NA| Missing / invalid trial

The binary representation can be used for descriptive reporting and, where sample size and design assumptions permit, appropriate inferential analysis.

---

8. Secondary Dependent Variables

8.1 Response Time

Variable: "response_time_ms"

Represents the elapsed time between the predefined trial start point and the participant's recorded response.

Unit:

milliseconds

Response-time measurements must use the same start and end definitions across experimental conditions.

---

8.2 Trust

Variable: "trust_score"

Trust represents the participant's reported trust in the autonomous-driving system following the interaction.

Trust is interpreted as a Human Factors construct rather than as a simple UX satisfaction measure.

The analytical objective is not to maximise trust.

The relevant concept is:

«Calibrated trust.»

---

8.3 Cognitive Workload

Variable: "workload_score"

Workload represents the participant's perceived cognitive demand during the experimental task.

The planned principal subjective workload instrument is:

NASA-TLX

The same administration procedure should be used across conditions.

---

8.4 Perceived Understanding

Variable: "perceived_understanding"

This captures how well participants believe they understood the autonomous vehicle's behaviour.

It is intentionally separated from objective comprehension.

Objective comprehension
        ≠
Perceived understanding

This distinction allows potential discrepancies between confidence and actual understanding to be examined.

---

8.5 Task Success

Variable: "task_success"

Records whether the participant successfully completed the predefined experimental task.

Value| Meaning
1| Successful
0| Unsuccessful
NA| Invalid / interrupted trial

---

8.6 Interaction Error

Variable: "interaction_error"

Records whether an interaction error occurred.

Examples include:

- selecting an incorrect control;
- failing to locate required information;
- misunderstanding an interface state;
- performing an incorrect interaction.

---

9. Exploratory Qualitative Data

Variable: "qualitative_note"

Qualitative observations may include:

- participant comments;
- explanation preferences;
- confusion;
- perceived ambiguity;
- comments about information density;
- accessibility observations;
- unexpected interaction behaviour.

Qualitative observations should be recorded without interpreting them as empirical conclusions before analysis.

---

10. Control Variables

The following elements should remain consistent across experimental conditions wherever practical:

Control| Requirement
Scenario| Same underlying event
Vehicle behaviour| Equivalent across conditions
Passenger role| Same
Interface structure| Same
Typography| Same
Visual hierarchy| Same
Interaction mechanism| Same
Task instructions| Same
Measurement procedure| Same
Experimental environment| Controlled as far as practical

The principal intended difference between conditions should be the explanation presentation.

---

11. Construct-to-Measure Mapping

Theoretical Construct| Operational Variable| Measurement
Explainability| Condition| A/B/C
Comprehension| "comprehension_score"| Accuracy / score
Objective understanding| "comprehension_correct"| Correct / incorrect
Processing efficiency| "response_time_ms"| Milliseconds
Trust| "trust_score"| Trust scale
Cognitive workload| "workload_score"| NASA-TLX
Perceived understanding| "perceived_understanding"| Self-report
Task performance| "task_success"| Success / failure
Interaction reliability| "interaction_error"| Error coding
Participant interpretation| "qualitative_note"| Qualitative coding

---

12. Measurement Hierarchy

The project deliberately uses multiple measurement levels.

Objective Measures

- comprehension accuracy;
- response time;
- task success;
- interaction errors.

Subjective Measures

- trust;
- workload;
- perceived understanding.

Qualitative Measures

- participant comments;
- observed confusion;
- explanation preferences;
- unexpected interaction behaviour.

This allows the study to distinguish:

What participants actually did
          ↓
What participants reported
          ↓
What participants described

---

13. Primary Analysis Logic

The primary analysis asks whether comprehension differs across:

A — No explanation
B — Minimal explanation
C — Contextual explanation

The primary outcome is:

Comprehension

The analysis should report:

- descriptive statistics;
- condition-level distributions;
- effect estimates where justified;
- uncertainty estimates where appropriate;
- missing data;
- protocol deviations;
- invalid trials.

No statistical test should be selected solely to produce a significant result.

The final method must depend on:

- sample size;
- data distribution;
- measurement scale;
- repeated-measures structure;
- missingness;
- assumptions of the statistical procedure.

---

14. Secondary Analysis Logic

Secondary outcomes will be examined in relation to explanation condition:

Explanation Condition
        ↓
├── Response Time
├── Trust
├── Workload
├── Perceived Understanding
├── Task Success
└── Interaction Errors

These analyses should remain secondary to the comprehension outcome.

---

15. Relationship Between Objective and Subjective Measures

A major analytical opportunity is to compare:

Comprehension

What the participant actually understood.

Perceived Understanding

How well the participant believed they understood the event.

Trust

How much confidence the participant placed in the autonomous system.

Workload

How mentally demanding the interaction felt.

These constructs should not be collapsed into a single UX score.

---

16. Potential Analytical Patterns

The analysis framework allows several possible outcomes.

Pattern 1

Comprehension ↑
Workload stable
Trust appropriately calibrated

This may indicate a potentially useful explanation pattern.

Pattern 2

Comprehension ↑
Workload ↑ substantially

This may indicate an understanding–workload trade-off.

Pattern 3

Trust ↑
Comprehension unchanged

This would demonstrate that trust and understanding should not be treated as equivalent.

Pattern 4

No meaningful difference

A null result is a valid empirical outcome and should be reported transparently.

---

17. Interpretation Rules

The following interpretation rules are established before final results analysis.

Rule 1

A higher mean score does not automatically establish a practically meaningful effect.

Rule 2

Statistical significance, if tested, does not by itself establish practical importance.

Rule 3

Effect size should accompany inferential results where appropriate.

Rule 4

Null findings must be reported.

Rule 5

Missing data and protocol deviations must be documented.

Rule 6

No causal conclusion should be made beyond what the experimental design supports.

Rule 7

Trust increases must not automatically be interpreted as positive outcomes.

Rule 8

Prototype findings must not be presented as real-world autonomous-vehicle safety validation.

---

18. Hypothesis Operationalisation

The project's hypotheses are directional research propositions rather than predetermined results.

H1 — Explanation and Comprehension

«Participants exposed to passenger-facing explanations will demonstrate different comprehension outcomes compared with participants receiving no explanation.»

H2 — Explanation Specificity

«Different levels of explanation specificity will produce different comprehension and trust-related responses.»

H3 — Explanation and Workload

«Differences in explanation specificity will be associated with differences in perceived cognitive workload.»

H4 — Objective and Subjective Understanding

«Objective comprehension and perceived understanding will not necessarily be equivalent.»

H5 — Trust and Understanding

«Trust-related responses and comprehension outcomes will represent related but distinct aspects of passenger interaction.»

H6 — Contextual Influence

«The usefulness of an explanation may vary according to contextual factors such as event characteristics, timing, passenger activity, and modality.»

H6 is primarily relevant to contextual or future experimental extensions unless these variables are explicitly manipulated in the executed experiment.

---

19. Traceability Matrix

RQ| Hypothesis| IV| Primary/Secondary DV| Measurement| Analysis
RQ1| H1| Condition| Comprehension| Score / accuracy| Condition comparison
RQ2| H2| Condition| Comprehension + Trust| Score + trust scale| Condition comparison
RQ3| H6| Timing| Understanding| Comprehension| Timing analysis if tested
RQ4| H6| Event characteristics| Comprehension / trust| Scenario coding| Exploratory analysis
RQ5| H6| Activity / modality| Comprehension / workload| Condition coding| Exploratory analysis

---

20. Final Operational Model

                EXPLANATION CONDITION
                 A / B / C
                     │
                     ↓
             Passenger Interpretation
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
   Comprehension    Trust     Workload
          │          │          │
          ↓          ↓          ↓
   Task Performance / Passenger Response
                     │
                     ↓
             Design Implications

---

21. Methodological Boundary

This operationalisation defines the measurement framework.

It does not imply that all variables will necessarily produce statistically meaningful relationships.

The final empirical interpretation must be based exclusively on the dataset actually collected under the defined protocol.

No simulated, estimated, or invented participant results are permitted.

---

22. Summary

The project now has a complete operational chain:

«Research Question → Hypothesis → Construct → Variable → Measure → Condition → Analysis → Interpretation»

This establishes methodological traceability between the theoretical framework and empirical evaluation.

The operationalisation will serve as the reference document for final data analysis and research-paper results reporting.
