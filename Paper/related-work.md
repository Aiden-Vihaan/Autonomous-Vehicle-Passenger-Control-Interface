Related Work

2. Related Work

The design of passenger-facing interfaces for autonomous vehicles lies at the intersection of Human-Computer Interaction, Human Factors, explainable artificial intelligence, trust in automation, situation awareness, and cognitive workload. As vehicle automation increases, passengers become less directly involved in vehicle control and more dependent on the interface for interpreting system behaviour.

This section reviews research relevant to the central problem of this project: how explanations of unexpected autonomous-vehicle behaviour can support passenger understanding while considering trust, workload, timing, and accessibility.

The literature is organized into six themes:

1. Trust in Automation
2. Explanation and Explainable AI
3. Situation Awareness
4. Cognitive Workload
5. Explanation Timing and Multimodal Interaction
6. Passenger Context and Accessibility

The review is used not only to summarize previous research but also to identify the specific design and research space addressed by the present project.

---

2.1 Trust in Automation

Trust is a central construct in human interaction with automated systems because users must decide whether and when to rely on system behaviour.

In autonomous vehicles, this relationship becomes particularly important because passengers have limited direct control over the vehicle. A passenger may therefore use interface information to interpret whether an unexpected action represents appropriate system adaptation, an environmental response, or a situation requiring attention.

Research on autonomous-vehicle explanations indicates that the way system behaviour is explained can influence trust-related responses.

Ha et al. investigated different explanation types in autonomous-driving scenarios and found that explanation type influenced trust, while perceived risk moderated aspects of the relationship between explanation and trust. Their findings indicate that explanation design cannot necessarily be separated from the perceived risk of the situation.

This is important for the present project because an explanation should not be treated as a universally beneficial interface element. Its effectiveness may depend on the situation in which it is presented.

The relevant Human Factors objective is therefore not simply:

«Increase trust.»

Instead, the more appropriate objective is:

«Support appropriately calibrated trust through understandable communication of system behaviour.»

This distinction is important because high trust without corresponding understanding may encourage inappropriate reliance, while low trust despite appropriate system behaviour may create unnecessary uncertainty.

---

2.2 Explanation and Explainable AI

Explainable AI concerns methods for making the behaviour or outputs of intelligent systems more interpretable to humans.

Within autonomous vehicles, explainability can be considered at several levels.

At a technical level, an explanation may describe system variables, perception outputs, or decision-making processes.

At a passenger-interface level, however, the relevant information is usually much more immediate:

«Why did the vehicle do that?»

The present project therefore treats explainability primarily as an interaction-design problem.

An explanation is useful only if it communicates information that the intended user can interpret and use.

The original Autonomous Vehicle Passenger Control Interface PRD identifies explanation as a first-class interaction mechanism and proposes explanation cards that communicate why the vehicle changed behaviour.

This supports a layered approach to explanation:

WHAT HAPPENED
      ↓
WHAT THE VEHICLE IS DOING
      ↓
WHAT IT MEANS FOR THE PASSENGER
      ↓
OPTIONAL DETAIL

The distinction between explanation availability and explanation usability is particularly important. A system can technically provide an explanation while still failing to provide meaningful passenger understanding.

---

2.3 Explanation Specificity

Explanation specificity represents another important dimension.

A minimal explanation may communicate the immediate reason for an action:

«"Slowing for pedestrian."»

A more contextual explanation may provide additional information:

«"Pedestrian entering the crossing ahead. Slowing to maintain a safe distance."»

These two explanations provide different amounts of contextual information even though they communicate the same underlying event.

Previous autonomous-vehicle research has examined multiple explanation forms rather than treating explanation as a single binary feature. Ha et al. compared explanation types across different risk situations, while Du et al. examined explanation timing and presentation conditions in a driving-simulator study.

This provides a basis for investigating explanation presentation as a multidimensional design variable.

The present project therefore distinguishes:

- explanation presence;
- explanation specificity;
- explanation timing;
- information density;
- interaction context.

This distinction forms part of the research gap addressed by the project.

---

2.4 Situation Awareness

Situation Awareness (SA) provides a useful theoretical framework for understanding how passengers interpret autonomous-system behaviour.

Endsley's framework describes situation awareness through three stages:

1. perception of relevant information;
2. comprehension of its meaning;
3. projection of future states.

Applied to an autonomous vehicle, a passenger may first notice that the vehicle has slowed down, then understand that a pedestrian has entered a crossing, and finally anticipate that the vehicle will continue once the situation changes.

The interface can therefore contribute to passenger situation awareness by communicating information that connects vehicle behaviour with its environmental context.

The explanation framework developed in this project reflects this structure:

Vehicle Behaviour
      ↓
Environmental Reason
      ↓
Passenger Understanding
      ↓
Expectation of Next State

However, situation awareness should not be assumed simply because information is displayed.

The passenger must be able to perceive, understand, and use the information.

This creates a direct connection between explanation design and comprehension.

---

2.5 Cognitive Workload

Information presentation also introduces a potential trade-off.

Additional information may improve understanding while simultaneously increasing cognitive demand.

This is particularly relevant in autonomous vehicles because passengers may not always be actively monitoring the road or interface. They may be:

- reading;
- watching media;
- communicating;
- working;
- interacting with other passengers;
- resting.

A detailed explanation that is appropriate during a low-demand situation may not be appropriate during a high-demand or urgent event.

NASA-TLX provides an established framework for assessing perceived workload across multiple dimensions.

The present project therefore treats workload as a secondary outcome rather than assuming that increased information is automatically beneficial.

The relevant design question becomes:

«Does additional explanation provide enough comprehension benefit to justify its additional cognitive demand?»

This question is especially important when comparing minimal and contextual explanations.

---

2.6 Explanation Timing

The timing of an explanation may be as important as its content.

Du et al. examined explanation timing in autonomous-driving scenarios and reported differences associated with when explanations were presented. Their work provides evidence that explanation timing should be treated as an interaction variable rather than merely a visual-detail decision.

For a passenger, there is a meaningful difference between:

Vehicle slows
     ↓
Explanation

and:

Explanation
     ↓
Vehicle slows

A pre-action explanation can establish expectations before the behaviour occurs.

A post-action explanation can help the passenger interpret behaviour that has already occurred.

The present project therefore considers explanation timing as an important extension of the basic explanation-condition comparison.

---

2.7 Multimodal Explanations

Autonomous-vehicle interfaces can communicate through multiple channels, including:

- visual display;
- speech;
- audio alerts;
- haptic feedback;
- physical controls.

Research examining multimodal explanations indicates that combining modalities does not necessarily produce universally better outcomes.

Hong et al. investigated visual and speech explanations in autonomous-driving contexts and examined their relationship with situation awareness, trust, and passenger activity. Their findings suggest that interaction context can influence the usefulness of different modalities.

This is important for passenger HMI design because passengers may be engaged in another activity when an unexpected vehicle event occurs.

A visual explanation may be appropriate when the passenger is looking at the display.

An auditory explanation may be useful when visual attention is elsewhere.

However, multimodal presentation can also increase information density and interruption.

The design implication is therefore not:

«"Use every available modality."»

Instead:

«Select communication modalities according to information importance, passenger context, accessibility, and cognitive demand.»

---

2.8 Passenger Activity and Context

Passenger activity introduces an additional Human Factors variable that is less central in traditional driver-facing interfaces.

A driver is expected to monitor the driving environment.

A passenger may not be.

Consequently, passenger attention can be intermittent.

The passenger may encounter an unexpected vehicle event while:

- watching a video;
- reading;
- using a personal device;
- talking;
- working;
- resting.

This changes the requirements for notification and explanation design.

An explanation that depends on continuous visual attention may fail when the passenger is looking elsewhere.

Conversely, constant auditory notifications may unnecessarily interrupt passengers.

The present project therefore identifies passenger activity as an important moderator for future multimodal research.

---

2.9 Accessibility and Inclusive Interaction

Accessibility is a fundamental component of Human Factors design.

The original project requirements explicitly address:

- visual accessibility;
- auditory accessibility;
- motor accessibility;
- cognitive accessibility;
- language accessibility;
- wheelchair accessibility.

Critical information is intended to have multimodal equivalents, and critical actions should remain accessible through appropriate interaction mechanisms.

This has direct implications for explanation design.

A visual explanation cannot be considered fully effective if a passenger cannot perceive the relevant visual information.

Similarly, an auditory explanation cannot be considered sufficient if the passenger cannot reliably hear it.

Accessibility therefore affects not only interface usability but also the passenger's ability to construct an accurate understanding of autonomous-system behaviour.

---

2.10 Safety-Relevant Communication

Autonomous-vehicle passenger interfaces operate in a safety-relevant context.

The interface therefore needs to distinguish between:

- informational content;
- explanatory content;
- journey controls;
- safety-critical controls.

The PRD establishes a hierarchy in which emergency and safety-related functions remain accessible and should not be obscured by ordinary interface content.

This distinction is important for explanation design.

An explanation should help the passenger understand system behaviour without competing with a control that may require immediate attention.

The present project consequently treats explanation as part of the information architecture while keeping safety-critical interaction structurally separate.

---

2.11 Synthesis of the Literature

The reviewed literature suggests that autonomous-vehicle explanation design is influenced by multiple interacting factors.

Factor| Human Factors relevance
Explanation presence| May affect understanding and trust
Explanation type| Different forms may produce different responses
Explanation specificity| Changes information depth
Explanation timing| Influences expectation and interpretation
Risk context| May moderate trust and explanation effects
Passenger activity| Influences attention and modality usefulness
Modality| Determines how information reaches the passenger
Workload| Determines whether additional information remains manageable
Accessibility| Determines whether information can be perceived and used
Safety hierarchy| Prevents explanation from competing with critical controls

The literature therefore supports treating explanation design as a multidimensional Human Factors problem rather than a simple transparency feature.

---

2.12 Literature-to-Research-Gap Transition

The reviewed literature establishes several important findings:

1. Explanation presentation can influence trust-related responses.
2. Explanation timing can influence user responses.
3. Risk and situational context can affect explanation outcomes.
4. Visual and auditory explanations may have different effects depending on passenger activity.
5. Explainability is connected to perceived understanding and acceptance.
6. Additional information may create cognitive workload.
7. Accessibility affects whether explanations can be effectively perceived.

However, these findings do not eliminate the need for a structured passenger-HMI investigation.

The present project therefore focuses on the interaction between:

Explanation Specificity
        +
Explanation Timing
        +
Passenger Context
        ↓
Passenger Understanding
        ↓
Trust + Workload
        ↓
Design Implications

The next section defines the specific research gap addressed by this project.
