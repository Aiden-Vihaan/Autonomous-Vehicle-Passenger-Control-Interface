Day 41 — Empirical Data Processing and Analysis Workflow

Project: Autonomous Vehicle Passenger Control Interface
Research Domain: Human Factors Engineering / HCI / Explainable Autonomous Vehicles
Experimental Version: EV-1.0
Primary Research Question:

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

---

1. Day 41 Objective

Day 41 establishes the project-specific empirical data-processing workflow required to move from experimental observations to defensible Human Factors findings.

The workflow is derived from the experimental design established in Days 28–40 and remains grounded in the original product requirements.

The original PRD identifies unexpected autonomous-vehicle behaviour—including abrupt slow-downs, lane changes, pauses, and other events—as moments in which passengers may question system behaviour. It specifies contextual explanation cards as a primary interaction for these situations. The explanation architecture is:

«What the vehicle noticed → What the vehicle is doing → Impact on the passenger»

The PRD also specifies that these explanations should appear around the time of the relevant manoeuvre, use calm factual language, and remain distinct from the protected safety-control interface.

Therefore, the empirical analysis does not evaluate a generic chatbot or generic XAI system.

It evaluates a specific passenger-facing explanation mechanism within an autonomous-vehicle HMI.

---

2. Experimental Context

The project evaluates three explanation conditions while holding the surrounding passenger interface and vehicle event constant.

Condition| Explanation treatment| Purpose
A| No explanation| Baseline passenger experience
B| Minimal explanation| Tests concise event-level information
C| Contextual explanation| Tests event + context + intended vehicle response

Condition A — No Explanation

The autonomous vehicle performs the unexpected behaviour without presenting an explanatory card.

Condition B — Minimal Explanation

The interface provides a short description of the immediate reason for the vehicle behaviour.

Example structure:

«“Slowing for pedestrian.”»

Condition C — Contextual Explanation

The interface provides the detected context together with the vehicle's response.

Example structure:

«“Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.”»

The exact experimental stimuli must remain those defined in the frozen EV-1.0 prototype.

---

3. Relationship to the Original Product Requirements

The empirical analysis preserves the original product concept rather than replacing it.

The original PRD defines:

- contextual explanation cards on the Journey Dashboard
- unexpected-event states
- route explanations
- vehicle diagnostics
- emergency controls
- accessibility support
- passenger-facing transparency
- calm and factual communication
- protected safety controls
- multiple input modalities

The research layer asks a narrower Human Factors question:

«How should an unexpected autonomous-vehicle event be explained so that the passenger can understand what is happening without creating unnecessary cognitive demand or inappropriate trust?»

This distinction keeps the internship product intact while giving the project an empirical research layer.

---

4. Empirical Processing Model

The complete processing chain is:

Experimental Scenario
        ↓
Autonomous Vehicle Event
        ↓
Explanation Condition
        ↓
Passenger Interaction
        ↓
Recorded Response
        ↓
Data Validation
        ↓
Data Cleaning
        ↓
Quality Control
        ↓
Analysis Dataset
        ↓
Descriptive Analysis
        ↓
Inferential Analysis
        ↓
Human Factors Interpretation
        ↓
Design Implication

This chain provides traceability from the original product requirement to the final research conclusion.

---

5. Research Variables

5.1 Independent Variable

Explanation Condition

condition

Coding:

A = No explanation
B = Minimal explanation
C = Contextual explanation

The explanation condition is the primary controlled manipulation in EV-1.0.

---

6. Primary Dependent Variable

6.1 Passenger Comprehension

The primary outcome is:

«How accurately the passenger understands the reason for the autonomous vehicle's unexpected behaviour.»

Variable:

comprehension_score

Binary representation:

comprehension_correct

Coding:

1 = Correct
0 = Incorrect

Comprehension is prioritised because the central Human Factors problem is not simply whether passengers feel informed, but whether they can correctly interpret what the vehicle is doing.

---

7. Secondary Dependent Variables

The project maintains several secondary outcomes.

Variable| Human Factors construct| Purpose
"response_time_ms"| Response efficiency| Measures time required to interpret/respond
"trust_score"| Trust in automation| Examines passenger confidence in the system
"workload_score"| Cognitive workload| Examines cognitive demand
"perceived_understanding"| Subjective understanding| Measures how informed passengers believe they are
"task_success"| Task performance| Measures successful completion
"interaction_error"| Interaction performance| Captures interface-level mistakes
"qualitative_note"| Exploratory behaviour| Captures observations not represented numerically

---

8. Theoretical Interpretation of the Variables

The variables are not treated as interchangeable.

Comprehension
     ↓
What the passenger objectively understood

Perceived Understanding
     ↓
What the passenger believes they understood

Trust
     ↓
How appropriately the passenger relies on the system

Workload
     ↓
How cognitively demanding the interaction was

A condition may therefore produce:

- high comprehension + high workload
- high comprehension + moderate trust
- low comprehension + high perceived understanding
- high trust + poor comprehension

Such combinations are theoretically meaningful and should not be collapsed into a single "better UX" score.

---

9. Dataset Schema

The analysis dataset should contain:

Variable| Type| Role
"participant_id"| Identifier| Participant
"trial_id"| Identifier| Trial
"scenario_id"| Categorical| Experimental scenario
"condition"| Categorical| A/B/C manipulation
"comprehension_score"| Numeric| Primary outcome
"comprehension_correct"| Binary| Primary outcome
"response_time_ms"| Numeric| Secondary outcome
"trust_score"| Numeric| Secondary outcome
"workload_score"| Numeric| Secondary outcome
"perceived_understanding"| Numeric| Secondary outcome
"task_success"| Binary/Categorical| Performance
"interaction_error"| Binary/Categorical| Interaction quality
"protocol_deviation"| Categorical| Quality control
"technical_issue"| Categorical| Quality control
"qualitative_note"| Text| Exploratory observation

---

10. Scenario-Level Traceability

Every observation must remain connected to the scenario that generated it.

scenario_id
      ↓
vehicle event
      ↓
explanation condition
      ↓
participant response
      ↓
measured outcome

This is particularly important because the PRD includes multiple unexpected-event contexts, including braking, lane changes, route changes, emergency situations, perception-heavy scenes, weather limitations, and degraded states.

The EV-1.0 experiment must only analyse scenarios actually included in the frozen experimental protocol.

---

11. Raw Data Preservation

Raw observations are immutable.

Recommended structure:

data/
├── README.md
├── raw/
├── cleaned/
└── codebook/

Raw

Contains the original recorded observations.

Cleaned

Contains observations prepared for analysis.

Codebook

Defines variables, coding schemes, missing-value conventions, and quality flags.

No statistical manipulation should modify the raw dataset.

---

12. Data Validation

Before analysis, the following checks must be performed.

Participant-level checks

- participant identifiers exist
- participant identifiers are consistently formatted
- duplicate participant records are identified

Trial-level checks

- trial identifiers exist
- trial identifiers are unique where required
- scenario identifiers are valid
- condition identifiers are valid

Measurement checks

- comprehension values use the predefined scoring system
- binary comprehension uses the correct coding
- response time is recorded in milliseconds
- trust values follow the selected scale
- workload values follow the selected instrument
- perceived-understanding values follow the selected scale

---

13. Condition Integrity

The condition variable must contain only:

A
B
C

Invalid values such as:

Minimal
Contextual
No-XAI
Explanation
Condition 1
Condition 2

must not be introduced into the final analysis dataset unless explicitly defined in the codebook.

This prevents accidental condition fragmentation.

---

14. Missing Data

Missing observations must remain distinguishable from genuine zero values.

Recommended representation:

NA

with an accompanying reason where available:

NOT_RECORDED
TECHNICAL_FAILURE
TRIAL_INTERRUPTED
PARTICIPANT_WITHDRAWAL
NOT_APPLICABLE

Missing observations must not be converted into zero merely to complete the dataset.

---

15. Invalid Trials

A trial may be excluded from a particular analysis when the intended measurement was not validly obtained.

Possible reasons include:

- interface failure
- incomplete scenario
- technical failure
- protocol deviation
- participant withdrawal
- corrupted measurement
- invalid response capture

The original observation must remain documented.

Example:

trial_id: T014
technical_issue: TRUE
protocol_deviation: FALSE
analysis_status: EXCLUDED
exclusion_reason: INTERFACE_FAILURE

---

16. Data Cleaning Rules

Cleaning should be conservative and reproducible.

Permitted

- correcting documented transcription errors
- standardising categorical labels
- converting units
- identifying duplicates
- flagging invalid trials
- representing missing values consistently

Not permitted

- removing observations because they weaken a hypothesis
- changing participant responses
- changing experimental conditions
- selectively removing outliers after viewing results
- replacing missing data without a documented procedure
- modifying raw observations

---

17. Primary Analysis: Explanation Condition → Comprehension

The central analysis evaluates whether comprehension differs across:

A → B → C

The first analysis should be descriptive.

For each condition, calculate the appropriate statistics based on the actual measurement scale and experimental design.

Recommended reporting structure:

Measure| A| B| C
Valid observations| "[ACTUAL]"| "[ACTUAL]"| "[ACTUAL]"
Mean score| "[ACTUAL]"| "[ACTUAL]"| "[ACTUAL]"
Median score| "[ACTUAL]"| "[ACTUAL]"| "[ACTUAL]"
Correct (%)| "[ACTUAL]"| "[ACTUAL]"| "[ACTUAL]"

No values should be entered until generated from actual observations.

---

18. Secondary Analysis: Response Time

Response time is analysed as an indicator of interaction efficiency.

condition
     ↓
response_time_ms

Because response-time distributions can be asymmetric, the analysis should inspect:

- mean
- median
- standard deviation
- interquartile range
- distribution shape
- potential extreme observations

The final statistical method must follow the actual experimental design and observed distribution.

---

19. Secondary Analysis: Trust

Trust is treated as a separate construct.

condition
     ↓
trust_score

The project does not assume:

«higher trust = better outcome.»

Instead, interpretation focuses on whether the explanation condition appears associated with an appropriate relationship between understanding and trust.

This follows the project's calibrated-trust framework.

---

20. Secondary Analysis: Cognitive Workload

The workload analysis follows:

condition
     ↓
workload_score

The key Human Factors question is whether additional explanation information creates cognitive demand that could offset its informational benefit.

Therefore:

«Understanding and workload must be evaluated together.»

A condition should not be interpreted as superior solely because it produces more information or solely because it produces lower workload.

---

21. Objective vs Subjective Understanding

The analysis explicitly compares:

comprehension_score
        ↕
perceived_understanding

This addresses a critical Human Factors distinction:

«Feeling informed is not necessarily equivalent to being correctly informed.»

Possible empirical patterns include:

1. objective and perceived understanding increase together
2. perceived understanding increases without objective comprehension
3. objective comprehension improves without a comparable subjective increase
4. the relationship differs by explanation condition

Only the observed pattern should be reported.

---

22. Trust–Comprehension Analysis

Trust and comprehension are also analysed together:

comprehension_score
        ↕
trust_score

The analysis asks whether passengers who understand the vehicle's behaviour also report different levels of trust.

This does not establish that comprehension causes trust or that trust causes comprehension.

The interpretation must remain consistent with the actual experimental design.

---

23. Workload–Comprehension Analysis

A further relationship is:

workload_score
        ↕
comprehension_score

This allows the project to investigate a central design trade-off:

«How much explanation is useful before additional information becomes cognitively demanding?»

This question is particularly relevant to the PRD's requirement for concise, calm, plain-language explanation cards.

---

24. Explanation Structure as an Analytical Dimension

The contextual explanation condition should be interpreted according to the PRD's intended explanation architecture:

WHAT THE VEHICLE NOTICED
          ↓
WHAT THE VEHICLE IS DOING
          ↓
WHAT IT MEANS FOR THE PASSENGER

Therefore, the analysis should consider whether additional contextual information contributes to comprehension without unnecessarily increasing workload.

This is more informative than simply treating the conditions as:

«"no text vs more text."»

---

25. Timing as a Controlled Context

The original PRD specifies that explanation cards should appear around the time of the relevant vehicle manoeuvre.

Therefore, timing must be documented for each experimental condition.

Relevant variables may include:

event_timestamp
explanation_timestamp
response_timestamp

and, where technically available:

explanation_latency_ms
response_time_ms

If timing is not directly recorded, no numerical timing claim should be made.

Timing remains an important contextual dimension of the research framework.

---

26. Passenger Context

The original product requirements recognise that passengers may be:

- commuting
- working
- travelling
- caring for children
- using accessibility features
- unfamiliar with autonomous vehicles

The core EV-1.0 experiment should only analyse passenger-context effects if those variables were actually manipulated or recorded.

Otherwise, passenger activity remains a contextual design dimension rather than an empirical finding.

---

27. Accessibility Considerations

The PRD explicitly requires:

- large text
- high contrast
- screen-reader support
- captions
- visual equivalents for audio alerts
- voice control
- simplified mode
- no time pressure
- wheelchair-related support
- multilingual interaction

Therefore, accessibility cannot be treated as a cosmetic design layer.

However, an accessibility effect should only be claimed if it was empirically measured.

If accessibility was not experimentally manipulated, the appropriate conclusion is:

«Accessibility requirements informed the interface design and experimental stimulus, while accessibility-specific performance remains outside the current empirical claim set.»

---

28. Safety Hierarchy

The PRD defines the emergency interface as the most important screen and specifies that the safety control remains persistently accessible.

Therefore, explanation-card performance must not be interpreted as equivalent to safety-control performance.

The analysis does not claim:

- improved vehicle safety
- reduced accident probability
- production-level safety validation
- regulatory compliance
- functional-safety certification

The experiment evaluates passenger-facing interaction and Human Factors outcomes, not vehicle-control safety.

---

29. Descriptive Visualisation Plan

The first empirical figures should directly correspond to the research model.

Figure 1 — Comprehension by Explanation Condition

A: No explanation
B: Minimal explanation
C: Contextual explanation

Figure 2 — Response Time by Explanation Condition

Condition → Response Time

Figure 3 — Trust by Explanation Condition

Condition → Trust

Figure 4 — Workload by Explanation Condition

Condition → Workload

Figure 5 — Objective vs Perceived Understanding

Objective comprehension
          ↕
Perceived understanding

Visualisations must represent the actual dataset and should not exaggerate small differences.

---

30. Inferential Analysis

Inferential analysis will be selected only after examining:

- actual sample size
- repeated-measures structure
- measurement scales
- distribution characteristics
- missing data
- protocol deviations
- scenario structure

Possible methods may include:

- paired comparisons
- repeated-measures analyses
- non-parametric alternatives
- categorical analyses
- correlation
- regression

The final method must be justified in "STATISTICAL-ANALYSIS-SPECIFICATION.md".

---

31. Effect Sizes and Uncertainty

Where inferential analysis is appropriate, results should include effect sizes and uncertainty estimates where applicable.

The reporting hierarchy is:

Observed difference
        ↓
Statistical uncertainty
        ↓
Effect magnitude
        ↓
Practical Human Factors meaning

A p-value alone is insufficient to establish practical importance.

---

32. Hypothesis Processing

The Day 39 hypotheses are evaluated against the processed dataset.

Hypothesis| Primary evidence
H1| Explanation condition → comprehension
H2| Explanation specificity → comprehension/trust
H3| Explanation specificity → workload
H4| Objective comprehension ↔️ perceived understanding
H5| Trust ↔️ comprehension
H6| Contextual factors → usefulness

Importantly, H6 and any timing/activity/modality effects must only be tested when the corresponding variables were actually manipulated or recorded.

---

33. Qualitative Analysis

Qualitative observations may be used to explain quantitative patterns.

Potential codes include:

- confusion
- explanation seeking
- reassurance
- uncertainty
- information overload
- delayed interpretation
- accessibility difficulty
- interaction difficulty
- perceived lack of control

Only codes supported by actual observations should enter the final results.

---

34. Data-to-Design Traceability

The ultimate purpose of the empirical analysis is not merely to produce statistics.

The workflow is:

Empirical Result
      ↓
Human Factors Interpretation
      ↓
Design Implication
      ↓
Interface Decision
      ↓
Prototype Revision

Example:

Observed:
[ACTUAL RESULT]

Human Factors interpretation:
[ACTUAL INTERPRETATION]

Design implication:
[ACTUAL IMPLICATION]

Interface decision:
[ACTUAL DECISION]

This maintains traceability between the research study and the original product-design objective.

---

35. Research Integrity Rules

The following rules remain mandatory:

1. Raw data remain immutable.
2. No fabricated participant observations.
3. No fabricated numerical results.
4. No simulated results presented as empirical findings.
5. No invented statistical significance.
6. No invented effect sizes.
7. No selective removal of inconvenient observations.
8. No unsupported causal claims.
9. No unsupported accessibility claims.
10. No vehicle-safety validation claims.
11. No functional-safety certification claim
