Day 35 — Discussion, Contribution and Limitations

Project: Autonomous Vehicle Passenger Control Interface
Research Theme: Explainable Autonomous-Vehicle Behaviour
Research Question: How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?

Experimental Version: EV-1.0
Project Stage: Discussion and Research Contribution
Status: Complete

---

1. Discussion

1.1 Overview

This project investigated the Human Factors problem of communicating unexpected autonomous-vehicle behaviour to passengers.

The original product requirement was transformed into a research-oriented investigation of explanation presentation, with particular attention to passenger understanding, trust, cognitive workload, and interaction performance.

Rather than treating explainability as a purely visual design problem, the project conceptualised the explanation interface as a Human-AI interaction mechanism.

The resulting framework connects:

Autonomous-System Behaviour
          ↓
Explanation Presentation
          ↓
Passenger Interpretation
          ↓
Understanding
          ↓
Trust + Workload
          ↓
Passenger Response

This provides a structured basis for evaluating passenger-facing explainability in autonomous vehicles.

---

2. Interpretation of the Research Question

The primary research question was:

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

The experimental framework operationalises explanation presentation through three conditions:

- Condition A: No explanation
- Condition B: Minimal explanation
- Condition C: Contextual explanation

This design makes explanation specificity an explicit experimental factor rather than treating explainability as a binary property.

The project therefore moves beyond the question:

«“Should autonomous vehicles explain themselves?”»

towards the more useful Human Factors question:

«“What information should be communicated, at what level of specificity, and under what interaction conditions?”»

---

3. Theoretical Contribution

The project integrates several Human Factors perspectives into one passenger-interface framework.

3.1 Trust in Automation

Trust is treated as an important but non-independent outcome.

The design does not attempt to maximise passenger trust regardless of system behaviour.

Instead, the intended outcome is calibrated trust, where passenger confidence is appropriately related to the system's observable behaviour and communicated limitations.

This distinction is particularly important for autonomous systems because excessive trust can be problematic just as insufficient trust can be.

---

3.2 Situation Awareness

Unexpected autonomous behaviour can create uncertainty when the passenger cannot determine:

- what the vehicle detected;
- why the vehicle responded;
- what the vehicle intends to do next;
- and whether the behaviour affects the journey.

Explanation cards provide an external representation of relevant system state.

The conceptual relationship is:

System State
     ↓
Externalised Information
     ↓
Passenger Interpretation
     ↓
Situation Awareness

The design therefore treats explanations as a mechanism for supporting passenger understanding of system behaviour.

---

3.3 Cognitive Workload

The project does not assume that additional information is inherently beneficial.

Additional information can potentially improve understanding while simultaneously increasing cognitive demand.

This creates an important Human Factors trade-off:

More Information
      ↓
Potentially Greater Understanding
      +
Potentially Greater Workload

The design therefore adopts concise explanations and progressive disclosure rather than continuously presenting technical information.

---

3.4 Explainable AI

The project interprets XAI from the perspective of the passenger rather than the system developer.

A technically accurate explanation is not automatically a useful passenger explanation.

The relevant question becomes:

«Can the passenger understand the explanation sufficiently to interpret the system's behaviour?»

This distinction places human interpretability at the centre of the interface.

---

4. Primary Design Contribution

The project's primary design contribution is a structured explanation architecture:

WHAT HAPPENED
      ↓
WHAT THE VEHICLE IS DOING
      ↓
WHAT IT MEANS FOR THE PASSENGER
      ↓
OPTIONAL ADDITIONAL CONTEXT

Example:

«Pedestrian entering crossing ahead.
Slowing to maintain a safe distance.
Arrival unaffected.»

This architecture deliberately avoids exposing unnecessary technical system information.

---

5. Explanation Specificity

The project treats explanation specificity as a design variable.

No explanation

The passenger receives no direct explanation.

Minimal explanation

The passenger receives the immediate cause.

«Slowing for pedestrian.»

Contextual explanation

The passenger receives cause plus system response.

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

This structure allows future empirical evaluation of whether additional contextual information produces measurable benefits or costs.

---

6. Timing as Part of Explainability

An explanation is not only defined by its content.

Its timing is also important.

An explanation presented too early may be difficult to associate with the resulting vehicle behaviour.

An explanation presented too late may fail to resolve the passenger's uncertainty.

The project therefore treats explanation timing as part of the interaction model:

Unexpected Event
      ↓
Vehicle Response
      ↓
Explanation
      ↓
Passenger Interpretation

The explanation should appear close enough to the relevant behaviour to maintain a meaningful relationship between event and explanation.

---

7. Trust and Explanation

The project deliberately avoids the simplistic assumption:

«More explanation = more trust.»

Instead, the conceptual relationship is:

Explanation
    ↓
Understanding
    ↓
Interpretation of System Behaviour
    ↓
Appropriate Confidence

The effect of an explanation on trust may depend on:

- the quality of the explanation;
- the actual system behaviour;
- the perceived risk of the situation;
- passenger expectations;
- the timing of the explanation;
- and the amount of information presented.

Therefore, trust should be interpreted alongside comprehension and workload rather than independently.

---

8. Understanding Versus Perceived Understanding

A particularly important methodological distinction is:

objective comprehension ≠ subjective confidence in understanding

A passenger may report that an explanation was clear while still misunderstanding the underlying event.

For this reason, the project includes both:

- comprehension accuracy;
- perceived understanding.

This enables a future analysis of whether subjective transparency corresponds to actual understanding.

---

9. Cognitive Workload and Information Density

The project establishes an information-density principle:

«Passenger-facing transparency should maximise useful understanding rather than information volume.»

The interface therefore uses:

- concise primary messages;
- stable hierarchy;
- progressive disclosure;
- consistent placement;
- limited simultaneous alerts;
- human-readable language.

This approach attempts to reduce unnecessary cognitive demand while preserving relevant information.

---

10. Accessibility Contribution

Explainability is treated as an accessibility concern.

An explanation that can only be perceived through one sensory channel is not universally accessible.

The project therefore incorporates:

- visual explanations;
- auditory equivalents;
- captions;
- screen-reader support;
- large text;
- high contrast;
- simplified cognitive presentation;
- voice interaction.

The underlying principle is:

«The semantic information should remain accessible even when the preferred interaction modality changes.»

---

11. Safety and Explainability

The project distinguishes between:

explanation

and

safety control.

An explanation can support understanding, but it should never become a substitute for a safety pathway.

The interface therefore preserves a protected safety control independent of the explanation system.

This produces the following hierarchy:

Safety Action
     ↓
Critical System Information
     ↓
Explanation
     ↓
Journey Information
     ↓
Secondary Information

This distinction is important because a transparent interface is not necessarily a safe interface unless critical actions remain immediately accessible.

---

12. Research Contribution

The project contributes a structured research framework for passenger-facing autonomous-vehicle explainability.

Its contribution can be represented as:

PRODUCT PROBLEM
      +
HUMAN FACTORS THEORY
      +
XAI
      +
EXPERIMENTAL DESIGN
      +
ACCESSIBILITY
      ↓
PASSENGER EXPLANATION FRAMEWORK

Rather than treating the HMI as a static visual artefact, the project defines it as an interaction system whose behaviour can be experimentally evaluated.

---

13. UX Contribution

The project also contributes to practical UX design by demonstrating how research constructs can be translated into interface requirements.

For example:

Research construct| UX translation
Understanding| Clear causal explanation
Trust calibration| Factual, non-reassuring language
Workload| Concise information hierarchy
Situation awareness| Timely system-state communication
Accessibility| Multimodal semantic equivalence
Safety| Persistent protected controls

This creates direct traceability between research and design.

---

14. Methodological Contribution

The methodology establishes a reproducible structure:

Scenario
  ↓
Vehicle Event
  ↓
Explanation Condition
  ↓
Passenger Interaction
  ↓
Measurement
  ↓
Data Quality Check
  ↓
Statistical / Descriptive Analysis
  ↓
Interpretation

This structure allows the same interface concept to be evaluated systematically rather than relying only on subjective portfolio critique.

---

15. Limitations

15.1 Empirical Dataset Availability

The current project record does not establish a verified participant-level dataset sufficient for claiming numerical empirical findings.

Therefore, the project does not report fabricated:

- participant counts;
- means;
- standard deviations;
- p-values;
- confidence intervals;
- effect sizes;
- correlations;
- or significance tests.

The experimental framework remains fully specified, but causal conclusions require actual valid observations.

---

15.2 Prototype-Based Evaluation

The interface is a prototype rather than a production autonomous-vehicle system.

Consequently, interaction with the prototype cannot reproduce every characteristic of a real vehicle, including:

- physical motion;
- acceleration;
- braking forces;
- vibration;
- environmental noise;
- real road complexity;
- real passenger risk perception.

The findings of any future prototype evaluation should therefore be interpreted within the scope of simulated interaction.

---

15.3 Ecological Validity

A controlled experimental scenario necessarily simplifies real-world passenger experience.

Real autonomous vehicles operate within environments containing:

- multiple road users;
- unpredictable events;
- changing weather;
- varying visibility;
- social interaction;
- physical motion;
- and longer periods of autonomous operation.

Future work should evaluate whether the interaction principles remain effective under more realistic conditions.

---

15.4 Explanation Scope

The project focuses specifically on passenger-facing explanations for unexpected autonomous behaviour.

It does not attempt to solve every explainability problem associated with autonomous vehicles.

The project does not evaluate:

- developer-facing diagnostics;
- complete model interpretability;
- source-code-level explanations;
- autonomous-driving algorithm transparency;
- formal safety certification;
- or vehicle-control verification.

---

15.5 Generalisability

Passenger expectations may vary according to:

- previous autonomous-vehicle experience;
- technology familiarity;
- cultural context;
- age;
- accessibility needs;
- risk perception;
- travel purpose;
- and individual trust in automation.

Future studies should therefore recruit broader and more diverse samples.

---

15.6 Multimodal Interaction

Although the project incorporates visual, auditory, and voice interaction concepts, the primary research focus is explanation presentation rather than a complete multimodal optimisation study.

Future research should isolate modality as an independent factor.

---

16. Validity Considerations

The project considers four forms of validity.

Internal validity

Controlled explanation conditions and consistent scenario structure support comparison between experimental conditions.

Construct validity

The project distinguishes comprehension, trust, workload, perceived understanding, and task performance rather than treating them as a single construct.

Ecological validity

The prototype provides controlled interaction but cannot fully reproduce real vehicle motion and environmental complexity.

External validity

Generalisation beyond the tested population and prototype context requires additional studies.

---

17. Future Work

17.1 Complete Empirical Evaluation

The immediate future step is to collect verified participant-level observations using the frozen EV-1.0 protocol.

The analysis should then evaluate:

- comprehension;
- response time;
- trust;
- workload;
- perceived understanding;
- task success;
- interaction errors.

---

17.2 Larger Participant Study

A larger study could examine whether observed effects remain stable across participant groups.

Potential factors include:

- age;
- technology experience;
- autonomous-vehicle familiarity;
- accessibility requirements;
- and passenger activity.

---

17.3 Passenger Activity

Future experiments should examine explanation effectiveness under different passenger activities.

Examples:

- attentive passenger;
- reading;
- conversation;
- entertainment;
- navigation;
- reduced visual attention.

This would help determine when visual, auditory, or multimodal explanations are most appropriate.

---

17.4 Risk and Urgency

Explanation effectiveness may depend on the perceived severity of the event.

Future research could compare:

- routine unexpected behaviour;
- moderate-risk events;
- high-urgency events.

This would allow explanation strategy to be studied as a function of risk context.

---

17.5 Adaptive Explanations

A future system could dynamically adjust explanation detail according to:

Event Severity
+
Passenger Context
+
Attention Availability
+
Accessibility Preference
+
Previous Interaction

The objective would be adaptive transparency rather than static transparency.

---

17.6 Longitudinal Trust

Short experimental sessions cannot fully represent trust development over repeated autonomous journeys.

Future studies should investigate whether explanation strategies influence:

- initial trust;
- trust repair;
- reliance;
- acceptance;
- and long-term mental models.

---

17.7 Real-Vehicle Validation

A later stage of research could evaluate the interface in a controlled autonomous-vehicle environment.

Such research would need appropriate:

- safety procedures;
- ethics approval;
- vehicle instrumentation;
- experimental controls;
- participant protection;
- and operational permissions.

The current project makes no claim of having completed this validation.

---

18. Final Research Contribution Statement

The project demonstrates a research-oriented approach to autonomous-vehicle passenger interface design in which explainability is treated as a measurable Human Factors problem rather than solely a visual design feature.

Its central contribution is the integration of:

explanation specificity + timing + passenger understanding + trust calibration + cognitive workload + accessibility

into a single passenger-facing interaction framework.

The resulting approach can be summarised as:

«Explain meaningful autonomous behaviour clearly, provide the information necessary for interpretation, minimise unnecessary cognitive demand, preserve accessibility, and maintain a clear separation between explanation and safety-critical action.»

---

19. Final Academic Position

The project should be positioned as a:

research-grade Human Factors / HCI project and research-paper-style portfolio artifact.

It should not be presented as:

- a completed academic thesis;
- a production autonomous-driving validation;
- a certified safety system;
- or a statistically validated claim without corresponding participant data.

Its strength lies in the complete chain from:

REAL UX PROBLEM
      ↓
RESEARCH QUESTION
      ↓
THEORY
      ↓
HYPOTHESES
      ↓
EXPERIMENT
      ↓
PROTOTYPE
      ↓
MEASUREMENT
      ↓
ANALYSIS
      ↓
DESIGN IMPLICATIONS

This structure demonstrates the ability to connect Human Factors theory with practical interaction design.

---

20. Discussion Completion Statement

Day 35 is complete.

The project now has a formal discussion layer covering:

- interpretation;
- theoretical contribution;
- design contribution;
- methodological contribution;
- limitations;
- validity;
- future research;
- and final contribution.

The research narrative is now sufficiently mature to transition into the final paper structure.

No unsupported empirical result has been introduced.
