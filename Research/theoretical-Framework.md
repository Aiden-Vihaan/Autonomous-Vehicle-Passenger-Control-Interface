Theoretical Framework

Designing Passenger-Facing Explanations for Autonomous Vehicle Behaviour

This project investigates how passenger-facing explanations of unexpected autonomous-vehicle behaviour may influence passenger understanding, trust, and cognitive workload.

The theoretical framework integrates four primary Human Factors and HCI perspectives:

1. Trust in Automation
2. Situation Awareness
3. Cognitive Workload
4. Explainable AI and Human-Automation Interaction

Additional concepts from multimodal interaction, visual attention, accessibility, and safety-oriented interface design are used to contextualise the framework.

The framework does not assume that more explanation is inherently better. Instead, it treats explanation design as a Human Factors problem involving the relationship between information content, timing, passenger interpretation, trust, workload, and context.

---

1. Trust in Automation

Trust is a central construct in autonomous-vehicle passenger interaction because passengers must rely on an automated system while having limited direct control over vehicle operation.

In this project, trust is treated as a relationship between the passenger and the automated driving system rather than simply as a positive attitude toward the interface.

A key Human Factors objective is therefore calibrated trust.

Calibrated Trust

Calibrated trust refers to an appropriate correspondence between a person's trust in an automated system and the system's actual capabilities and behaviour.

Two undesirable outcomes are possible:

- Overtrust: the passenger places more trust in the system than its demonstrated capability warrants.
- Undertrust: the passenger places less trust in the system than its demonstrated capability warrants.

Therefore:

«The design objective is not maximum trust, but appropriately calibrated trust.»

Passenger-facing explanations may contribute to trust by helping users understand why an autonomous vehicle is behaving in an unexpected way.

However, explanations may also create additional cognitive demands or produce unwarranted confidence if they communicate information unclearly.

This project therefore evaluates trust alongside comprehension and workload rather than treating increased trust alone as a successful outcome.

---

2. Situation Awareness

Situation Awareness (SA) provides a framework for understanding how passengers perceive and interpret changes in the autonomous vehicle's behaviour.

The classical three-level model describes:

Level 1 — Perception

The passenger becomes aware of relevant environmental or system information.

Examples:

- A pedestrian enters the crossing.
- The vehicle begins slowing.
- The route changes.
- A system warning appears.

Level 2 — Comprehension

The passenger understands what the observed information means.

Example:

«The vehicle is slowing because a pedestrian has entered the vehicle's path.»

Level 3 — Projection

The passenger can anticipate what is likely to happen next.

Example:

«The vehicle will continue slowing until the pedestrian has cleared the crossing.»

The explanation architecture in this project is intended primarily to support comprehension, while potentially contributing to projection.

The conceptual relationship is:

Environmental Event
        ↓
Vehicle Behaviour
        ↓
Passenger Perception
        ↓
Explanation
        ↓
Passenger Comprehension
        ↓
Expectation of Next Action

The project therefore treats explanation as an interaction mechanism that can help transform observable vehicle behaviour into interpretable information.

---

3. Cognitive Workload

Cognitive workload describes the mental demand experienced while performing or interpreting a task.

For autonomous-vehicle passengers, workload may arise from:

- interpreting unexpected vehicle behaviour;
- monitoring the environment;
- reading explanations;
- interacting with the interface;
- listening to spoken information;
- simultaneously performing another activity;
- responding to safety-related information.

An explanation may reduce uncertainty while simultaneously increasing information-processing requirements.

This creates an important Human Factors trade-off:

More Information
      ↓
Potentially greater understanding
      +
Potentially greater cognitive demand

Therefore, explanation design should not be evaluated only according to information completeness.

It should also consider:

- information density;
- readability;
- timing;
- relevance;
- modality;
- passenger activity;
- urgency.

NASA-TLX is identified as the principal subjective workload framework for the planned evaluation.

---

4. Explainable AI and Human-Automation Interaction

Explainable AI provides a framework for understanding how an intelligent system can communicate information about its behaviour to people.

Within this project, explainability is treated as an interaction-design problem rather than only as a technical property of the autonomous-driving model.

The passenger does not necessarily need access to the underlying machine-learning model.

Instead, the interface should communicate information that is useful for the passenger's immediate situation.

The proposed explanation structure is:

WHAT HAPPENED
      ↓
WHAT THE VEHICLE IS DOING
      ↓
WHAT IT MEANS FOR THE PASSENGER
      ↓
OPTIONAL ADDITIONAL DETAIL

Example

Minimal explanation

«Slowing for pedestrian.»

Contextual explanation

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

The distinction between these conditions is important because the project investigates explanation specificity, rather than treating explanations as simply present or absent.

---

5. Explanation Specificity as the Primary Experimental Construct

The primary independent variable is:

«Passenger-facing explanation condition»

Three levels are defined:

Condition| Description
A| No explanation
B| Minimal explanation
C| Contextual explanation

Condition A — No Explanation

The vehicle displays or performs the relevant behaviour without providing a passenger-facing causal explanation.

Condition B — Minimal Explanation

The system provides a concise description of the immediate reason for the behaviour.

Example:

«Slowing for pedestrian.»

Condition C — Contextual Explanation

The system provides the relevant event, vehicle response, and immediate implication.

Example:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

The conditions are intended to differ primarily in explanatory information while maintaining consistency in visual presentation and interaction structure.

---

6. Explanation Timing

Timing is treated as an important contextual factor.

An explanation may occur:

- before the vehicle action;
- during the vehicle action;
- immediately after the vehicle action.

The conceptual distinction is:

Pre-action
Passenger receives information
        ↓
Vehicle behaviour
        ↓
Passenger interpretation

versus

Vehicle behaviour
        ↓
Passenger receives explanation
        ↓
Passenger interpretation

The project does not assume that one timing strategy is universally superior.

Instead, timing is treated as a factor that may influence comprehension, trust, and workload.

---

7. Multimodal Interaction

Autonomous-vehicle passenger interfaces may communicate information through:

- visual text;
- speech;
- auditory signals;
- haptic feedback;
- combinations of modalities.

However, additional modalities may not always improve interaction.

Their usefulness may depend on:

- passenger activity;
- environmental conditions;
- urgency;
- information complexity;
- accessibility requirements;
- individual preference.

Therefore, multimodal interaction is treated as a contextual design dimension rather than as a universal optimisation strategy.

---

8. Accessibility

Accessibility is integrated into the theoretical framework rather than treated as a final-stage compliance activity.

The passenger population may include people with different:

- visual abilities;
- hearing abilities;
- motor abilities;
- cognitive processing requirements;
- language preferences;
- interaction capabilities.

Consequently, important information should not depend exclusively on a single sensory modality.

The theoretical framework therefore supports:

Visual Information
        +
Auditory Information
        +
Haptic Information where appropriate
        ↓
Accessible Passenger Understanding

Accessibility must remain compatible with the cognitive workload and safety requirements of the interaction.

---

9. Safety-Oriented Interface Hierarchy

The interface operates in a safety-relevant environment.

This creates a distinction between:

Informational interaction

Examples:

- route explanations;
- vehicle-state explanations;
- contextual information;
- diagnostics.

Safety-critical interaction

Examples:

- emergency controls;
- urgent warnings;
- passenger assistance;
- actions required during abnormal conditions.

Explanatory content should not compete visually or cognitively with safety-critical controls.

The design principle is therefore:

«Explanations should improve understanding without obscuring, delaying, or weakening access to safety-relevant functions.»

This project does not claim production safety validation, functional-safety certification, or compliance with a particular automotive safety standard.

---

10. Integrated Theoretical Model

The four primary theoretical perspectives can be combined into one conceptual model.

                AUTONOMOUS VEHICLE EVENT
                         │
                         ↓
              UNEXPECTED VEHICLE BEHAVIOUR
                         │
                         ↓
             ┌─────────────────────────┐
             │ Passenger Explanation  │
             │       Condition         │
             └─────────────────────────┘
                  /       |       \
                 /        |        \
                ↓         ↓         ↓
             None      Minimal   Contextual
                         │
                         ↓
              Passenger Information
                  Interpretation
                         │
              ┌──────────┼──────────┐
              ↓          ↓          ↓
        Comprehension   Trust    Workload
              │          │          │
              ↓          ↓          ↓
       Situation       Trust      Cognitive
       Awareness    Calibration    Demand
              │          │          │
              └──────────┼──────────┘
                         ↓
               Passenger Response
                         │
                         ↓
              Continued Journey

---

11. Construct Relationships

The proposed relationships are:

Explanation Condition → Comprehension

Different levels of explanation specificity may influence how accurately passengers understand unexpected vehicle behaviour.

Explanation Condition → Trust

Different explanation presentations may influence passenger trust-related responses.

However, the project does not assume that more explanation necessarily produces higher or better trust.

Explanation Condition → Workload

Additional information may increase cognitive demand even when it improves understanding.

Comprehension ↔️ Trust

Understanding and trust may be related but are not treated as interchangeable constructs.

A passenger can report high trust without demonstrating accurate comprehension.

Conversely, a passenger may understand the vehicle's behaviour without reporting high trust.

Comprehension ↔️ Workload

An explanation may improve understanding while simultaneously imposing additional cognitive demands.

This relationship is therefore evaluated empirically rather than assumed.

---

12. Human Factors Design Principle

The integrated framework produces the following design principle:

«Passenger explanations should provide sufficient information to support accurate interpretation of autonomous-vehicle behaviour while minimising unnecessary cognitive demand and preserving appropriately calibrated trust.»

This principle can be operationalised through five design requirements:

1. Relevance — communicate information related to the immediate event.
2. Specificity — provide enough causal context to support understanding.
3. Timing — present information at a useful point relative to the vehicle action.
4. Accessibility — provide information through appropriate interaction modalities.
5. Safety hierarchy — ensure explanations do not compete with safety-critical controls.

---

13. Conceptual Model Summary

The conceptual model positions explanation condition as the principal manipulated factor and passenger outcomes as measurable responses.

Independent Variable

Explanation condition

- A: No explanation
- B: Minimal explanation
- C: Contextual explanation

Primary Dependent Variable

Comprehension

Operationalised through comprehension accuracy and related task performance.

Secondary Dependent Variables

- response time;
- trust;
- workload;
- perceived understanding;
- task success;
- interaction errors.

Contextual Variables

Potential contextual influences include:

- scenario type;
- event type;
- explanation timing;
- passenger activity;
- urgency;
- information modality;
- accessibility requirements.

---

14. Theoretical Boundaries

The framework deliberately avoids several unsupported assumptions.

It does not assume that:

- explanations always increase trust;
- more information is always better;
- contextual explanations are universally superior;
- visual information is universally superior to auditory information;
- multimodal interaction is always optimal;
- increased trust necessarily represents successful interaction;
- perceived understanding is equivalent to objective comprehension;
- prototype results demonstrate real-world autonomous-vehicle safety.

These questions require empirical evidence.

---

15. Framework Contribution

The contribution of this framework is the integration of:

Explainability + Trust + Situation Awareness + Cognitive Workload + Accessibility + Safety-Oriented Interaction

within a passenger-facing autonomous-vehicle HMI context.

Rather than evaluating explanation quality as an isolated UX attribute, the framework treats explanations as part of a broader Human Factors system.

The resulting research model is:

EXPLANATION DESIGN
       ↓
PASSENGER INTERPRETATION
       ↓
COMPREHENSION
       ↕
TRUST CALIBRATION
       ↕
COGNITIVE WORKLOAD
       ↓
PASSENGER INTERACTION
       ↓
DESIGN IMPLICATIONS

This model provides the theoretical foundation for the methodology, experimental design, analysis, and final design recommendations developed in subsequent stages of the project.
