Designing Passenger-Facing Explanations for Autonomous Vehicle Behaviour: A Human Factors Approach to Understanding, Trust, and Cognitive Workload

Abstract

Autonomous vehicles introduce a distinctive human–automation interaction problem: passengers may experience vehicle behaviours that appear unexpected even when those behaviours are appropriate to the driving context. A passenger-facing interface therefore needs to communicate not only what is happening, but enough context for the passenger to construct an understandable mental model of the vehicle's behaviour without creating unnecessary cognitive demand.

This project investigates how the presentation of explanations for unexpected autonomous-vehicle behaviour may influence passenger understanding, trust, and cognitive workload. The research framework compares three explanation conditions: no explanation, minimal explanation, and contextual explanation.

The study is grounded in Human Factors principles including situation awareness, trust in automation, cognitive workload, explainable artificial intelligence, accessibility, and cognitive compatibility. Objective comprehension is treated separately from perceived understanding, while trust is interpreted in terms of calibration rather than maximisation.

The project develops an experimental protocol, passenger-facing interface architecture, explanation framework, data schema, analysis pipeline, and design implications for autonomous-vehicle passenger interfaces.

A synthetic dataset is included solely to demonstrate the analysis pipeline. It is explicitly labelled synthetic and does not constitute empirical evidence.

Keywords: autonomous vehicles, Human Factors, HCI, explainable AI, trust in automation, situation awareness, cognitive workload, passenger interface

---

1. Introduction

Autonomous vehicles change the role of the human from active driver to passenger. This transition creates a different interaction problem: the passenger may observe a vehicle slowing, stopping, changing lanes, or taking another action without understanding why the action occurred.

In conventional driving, a driver can inspect the environment and directly connect an action to a perceived cause. An autonomous passenger does not necessarily have access to the same perceptual information or decision process.

This creates a need for passenger-facing explanations that are concise, timely, understandable, and appropriately calibrated to the situation.

The underlying design problem is therefore not simply whether an autonomous vehicle should explain itself. The more important question is how explanations should be presented so that passengers can understand vehicle behaviour without being overloaded by information.

---

2. Research Question

Primary Research Question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

Secondary Questions

1. Does explanation presence improve passenger understanding?
2. Does explanation specificity affect understanding and trust calibration?
3. Does explanation timing influence passenger interpretation?
4. Does event urgency moderate explanation usefulness?
5. How should explanation design account for passenger activity and modality?

The latter questions are treated as contextual or future research dimensions unless directly manipulated by the experimental design.

---

3. Theoretical Foundation

The project combines four primary theoretical perspectives.

3.1 Trust in Automation

Trust is treated as a calibration problem rather than a quantity that should simply be increased.

An interface that produces very high trust despite poor system reliability could be undesirable. The design objective is therefore appropriate confidence in system behaviour.

3.2 Situation Awareness

Explanation design can contribute to passenger situation awareness by helping the passenger understand:

1. what is happening,
2. why it is happening,
3. what will happen next.

The interface therefore prioritises relevant information rather than exposing raw autonomous-driving telemetry.

3.3 Cognitive Workload

Passengers may simultaneously be:

- communicating,
- reading,
- watching media,
- navigating,
- interacting with the vehicle,
- preparing to exit.

Explanation design must therefore account for limited attention and avoid unnecessary information density.

3.4 Explainable AI

The project treats explanation as a human-facing communication layer rather than a requirement to expose the complete internal reasoning of the autonomous system.

The explanation should communicate actionable, passenger-relevant information without claiming that the passenger has been given the complete internal reasoning process.

---

4. Experimental Conditions

The EV-1.0 design contains three conditions.

Condition A — No Explanation

The autonomous vehicle performs the behaviour without providing a contextual explanation.

Condition B — Minimal Explanation

Example:

«Slowing for pedestrian.»

Condition C — Contextual Explanation

Example:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

The three conditions provide increasing levels of passenger-facing contextual information.

---

5. Explanation Framework

The project uses the structure:

WHAT THE CAR NOTICED
        ↓
WHAT IT IS DOING
        ↓
IMPACT ON THE PASSENGER

For example:

«Emergency vehicle approaching — pulling to the right — arrival unaffected.»

The interface aims to communicate relevant information before the passenger needs to infer the reason independently.

The intended tone is:

- factual
- calm
- concise
- non-alarming
- non-apologetic

---

6. Methodology

The project defines a controlled Human Factors evaluation of passenger-facing explanations.

The primary dependent variable is objective comprehension.

Secondary variables include:

- response time
- trust
- cognitive workload
- perceived understanding
- task success
- interaction error

Contextual variables include:

- event type
- urgency
- explanation timing
- modality
- passenger activity

Quality-control variables include:

- technical issue
- protocol deviation
- missing response
- trial interruption
- participant withdrawal
- invalid trial

---

7. Data Integrity

The empirical analysis framework distinguishes genuine participant data from synthetic demonstration data.

No synthetic observations are interpreted as empirical findings.

The included synthetic dataset exists only to demonstrate:

- analysis code
- data validation
- descriptive statistics
- visualisation
- reproducibility
- reporting structure

Therefore, quantitative claims derived from the synthetic dataset must not be presented as results from human participants.

---

8. Analysis Framework

The primary analysis compares comprehension across the three explanation conditions.

Secondary analyses examine:

- response time
- trust
- workload
- perceived understanding
- task success
- interaction error

The interpretation framework considers both statistical and Human Factors significance.

A statistically detectable difference would not automatically establish that one interface is universally superior.

The interpretation must consider:

- effect magnitude
- uncertainty
- practical relevance
- cognitive workload
- trust calibration
- accessibility
- scenario characteristics

---

9. Evidence-to-Design Framework

The project uses the following chain:

Research evidence
       ↓
Human Factors interpretation
       ↓
Design requirement
       ↓
Interface behaviour
       ↓
Evaluation measure
       ↓
Evidence review

This prevents design decisions from being disconnected from research questions.

---

10. Design Implications

The project establishes ten design principles:

1. Explain unexpected behaviour rather than every routine action.
2. Communicate before or during the relevant event when feasible.
3. Use concise, passenger-relevant language.
4. Separate observation, action, and passenger impact.
5. Preserve calm and factual communication.
6. Avoid unnecessary technical terminology.
7. Support progressive disclosure for passengers who want more information.
8. Maintain semantic equivalence across accessible modalities.
9. Keep safety-critical controls visually and interactionally distinct.
10. Design for calibrated trust rather than maximum trust.

---

11. Accessibility

Accessibility is treated as a system property rather than a final visual adjustment.

The interface supports requirements including:

- screen-reader operation
- logical focus order
- large text
- high contrast
- captions
- visual alerts
- voice operation
- multilingual support
- wheelchair-related interaction states
- simplified cognitive mode
- non-time-pressured interaction

The same underlying information should remain available through different modalities even when its presentation differs.

---

12. Limitations

The project does not evaluate the underlying autonomous-driving system itself.

The research evaluates passenger-facing communication.

Important limitations include:

- prototype-based evaluation
- simulated or controlled scenarios
- limited scenario coverage
- potential sample limitations
- self-report measurement
- accessibility requiring additional dedicated validation
- limited ecological validity
- possible mismatch between simulator/interface behaviour and real-world autonomous vehicles

The synthetic demonstration dataset cannot establish empirical effectiveness.

---

13. Future Work

Future research should progressively investigate:

Phase 1

Controlled laboratory evaluation.

Phase 2

Multimodal explanation evaluation.

Phase 3

Passenger activity and divided-attention effects.

Phase 4

Accessibility-specific evaluations.

Phase 5

Higher-fidelity autonomous-vehicle simulation.

Phase 6

Naturalistic passenger studies.

Future studies should also investigate explanation timing, event severity, uncertainty communication, adaptive modality selection, and longitudinal trust calibration.

---

14. Contribution

The primary contribution is a Human Factors framework for designing and experimentally evaluating passenger-facing explanations of unexpected autonomous-vehicle behaviour.

The framework integrates:

Understanding
Trust calibration
Cognitive workload
Situation awareness
Accessibility
Safety hierarchy
Explainable AI

The project therefore treats explanation design as a Human–Automation Interaction problem rather than simply a visual UI problem.

---

15. Conclusion

Passenger-facing autonomous-vehicle interfaces must bridge a gap between machine behaviour and human interpretation.

The EV-1.0 framework addresses this gap by treating explanation as a structured communication mechanism:

What happened?
Why is the vehicle responding?
What does this mean for me?

The resulting design framework emphasises concise contextual communication, calibrated trust, cognitive compatibility, accessibility, and safety.

The project provides a reproducible foundation for future empirical evaluation rather than claiming that synthetic demonstration data constitute evidence.

---

Data Statement

The repository includes a synthetic demonstration dataset for analysis-pipeline reproducibility.

The synthetic dataset is not empirical participant data.
