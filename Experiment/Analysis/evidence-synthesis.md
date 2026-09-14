Day 34 — Evidence Synthesis and Design Implications

Project: Autonomous Vehicle Passenger Control Interface
Research Focus: Explanations for unexpected autonomous-vehicle behaviour
Research Question: How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?

Experimental Version: EV-1.0
Analysis Stage: Evidence synthesis and design implications
Status: Complete at the level supported by the available project evidence

---

1. Purpose

Day 34 consolidates the research, theoretical, methodological, and design work completed during the project into a coherent evidence synthesis.

The objective is not to manufacture empirical outcomes where participant-level observations are unavailable. Instead, this stage establishes:

1. what the project was designed to investigate;
2. what the existing literature and project evidence support;
3. what design principles follow from that evidence;
4. which claims require empirical validation;
5. how the experimental framework connects directly to the final interface;
6. what conclusions can responsibly be carried into the final report.

This distinction preserves research integrity while allowing the project to function as a complete research-grade Human Factors/HCI artifact.

---

2. Evidence Boundary

The project contains three distinct evidence layers.

Evidence layer| Status| Interpretation
Product/UX requirements| Established| Derived from the original PRD
Literature and theoretical foundation| Established| Used to construct the research framework
Experimental methodology| Established| EV-1.0, protocol, variables, measures and analysis plan are defined
Participant-level empirical outcomes| Not established in the available project record| No numerical findings are claimed
Final causal conclusions| Not established| Require valid participant-level observations

The absence of verified participant-level results does not invalidate the research design. It means that empirical conclusions must remain explicitly bounded.

---

3. Research Problem

Autonomous vehicles create a distinctive Human Factors problem: passengers are expected to accept and interpret actions performed by a system that they cannot directly control.

The original PRD identifies opacity of intent as a central passenger problem. A vehicle may brake, hesitate, or reroute without the passenger knowing whether the action reflects an appropriate response to the environment or an unexpected system behaviour. The PRD therefore positions explanation as a first-class interaction rather than an engineering afterthought.

The research project operationalises this broader product problem into a narrower Human Factors question:

«How should an autonomous vehicle explain unexpected behaviour so that passengers can understand the system without creating unnecessary cognitive demand?»

This reframing turns a general UX problem into an experimentally testable interaction problem.

---

4. Evidence-Based Design Proposition

The central design proposition developed through the project is:

«Passenger-facing explanations should communicate the relevant cause and intended action in concise, human-readable language, with the amount and timing of information matched to the passenger's immediate context.»

This proposition follows directly from the project's theoretical framing and the PRD's emphasis on calibrated trust.

The PRD explicitly rejects both extremes:

- insufficient transparency can produce uncertainty;
- excessive raw system information can create overload.

The design target is therefore not maximum transparency, but appropriate transparency.

---

5. Explanation Model

The project defines three explanation conditions.

Condition A — No Explanation

The vehicle performs the unexpected action without presenting an explanatory message.

Purpose: Establishes the baseline passenger experience.

---

Condition B — Minimal Explanation

The interface communicates the immediate reason for the behaviour.

Example:

«Slowing for pedestrian.»

This condition provides a concise causal cue without additional contextual information.

---

Condition C — Contextual Explanation

The interface communicates both the relevant environmental event and the vehicle's intended response.

Example:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

This condition provides greater contextual information while remaining intentionally concise.

---

6. Why These Conditions Matter

The three conditions represent a controlled progression in explanatory information:

No explanation

→ absence of transparency

Minimal explanation

→ immediate causal information

Contextual explanation

→ causal information + situational context + intended action

This structure allows the study to examine explanation specificity rather than simply comparing “explanation” versus “no explanation.”

That distinction is important because a longer explanation is not automatically a better explanation.

---

7. Primary Human Factors Construct

Passenger Understanding

Understanding is treated as the primary outcome because an explanation only fulfils its Human Factors purpose if the passenger can correctly interpret what the vehicle detected and why it acted.

The primary measure is:

Comprehension accuracy

Operationally, the passenger should be able to correctly identify the relevant explanation associated with the vehicle's behaviour.

The original PRD also identifies explanation comprehension as a formal success metric, with the target that riders correctly interpret explanation cards during testing.

---

8. Secondary Constructs

The project evaluates understanding alongside several secondary constructs.

Trust

Trust represents the passenger's confidence in the automated system.

The objective is not to maximise trust independently of system behaviour.

The Human Factors objective is calibrated trust:

«Passenger confidence should correspond appropriately to the perceived competence and behaviour of the automated system.»

---

Cognitive Workload

An explanation that improves understanding but introduces excessive cognitive demand would not necessarily represent an improvement.

Workload is therefore treated as an important secondary outcome.

---

Response Time

Response time provides an objective behavioural indicator of how quickly a passenger can process the interaction and complete the associated response.

---

Perceived Understanding

This captures the passenger's subjective assessment of whether they understood what the vehicle was doing.

Comparing perceived understanding with comprehension accuracy is particularly valuable because people may feel informed without actually interpreting the system correctly.

---

Task Success and Interaction Errors

These measures determine whether the explanatory interaction interferes with or supports successful completion of the passenger task.

---

9. Human Factors Relationship Model

The project's conceptual model can be represented as:

AUTONOMOUS VEHICLE EVENT
          │
          ▼
   EVENT CLASSIFICATION
          │
          ▼
 EXPLANATION PRESENTATION
   ┌──────┼──────┐
   │      │      │
   A      B      C
 None   Minimal Contextual
   │      │      │
   └──────┼──────┘
          ▼
 PASSENGER INTERPRETATION
          │
     ┌────┼────┐
     ▼    ▼    ▼
Understanding Trust Workload
     │    │    │
     └────┼────┘
          ▼
 Passenger Response
          │
          ▼
     Journey Continues

This model establishes the connection between the autonomous-system event, interface explanation, passenger cognition, and observable interaction outcomes.

---

10. Timing as a Human Factors Variable

The original PRD specifies that explanation cards should appear around the time of the vehicle manoeuvre and should be concise, calm, and factual.

The project therefore treats timing as part of the interaction design rather than a cosmetic animation decision.

The explanation should answer the passenger's implicit question:

«“Why did the vehicle just do that?”»

before uncertainty becomes unnecessary cognitive work.

The interface consequently follows the sequence:

Vehicle detects relevant event
        ↓
Vehicle initiates behaviour
        ↓
Explanation becomes available
        ↓
Passenger can interpret the event
        ↓
Explanation resolves/dismisses

---

11. Information Density Principle

The project establishes a practical Human Factors rule:

«Every explanation should provide enough information to establish causal understanding, but not enough information to require the passenger to interpret raw system telemetry.»

The explanation hierarchy is therefore:

Level 1 — What happened?

Example:

«Slowing for pedestrian.»

Level 2 — Why did it happen?

Example:

«Pedestrian entering the crossing ahead.»

Level 3 — What is the vehicle doing about it?

Example:

«Slowing to maintain a safe distance.»

The passenger-facing interface prioritises these human-relevant layers rather than exposing low-level perception or control data.

---

12. Connection to the Original Product

This research layer does not replace the original internship assignment.

The original product remains:

«Autonomous Vehicle Passenger Control Interface»

The Human Factors research layer strengthens the existing product by investigating one of its defining interactions: explainable autonomous behaviour.

The original PRD describes contextual explanation cards as part of the Journey Dashboard and defines the explanation card as the signature XAI component of the interface.

Therefore, the research question is directly connected to the product rather than being an unrelated academic addition.

---

13. Design Implications

The completed research framework produces the following design implications.

13.1 Explain meaningful deviations

Explanations should be prioritised when the vehicle performs behaviour that a passenger could reasonably perceive as unexpected.

Examples include:

- abrupt slowing;
- waiting at an apparently clear intersection;
- rerouting;
- yielding to another road user;
- responding to unusual road conditions.

The goal is not to narrate every autonomous decision.

---

13.2 Explain causes, not internal telemetry

Passengers generally need a human interpretation of system behaviour rather than raw sensor output.

Therefore:

Preferred

«Emergency vehicle approaching — moving aside.»

Avoid

«Object classification: emergency_vehicle
Confidence: 0.94
Lateral trajectory: −1.28 m»

The second representation may be technically informative but is not automatically passenger-relevant.

---

13.3 Make the intended action explicit

An explanation should ideally communicate not only what was detected but what the vehicle is doing.

Recommended structure:

WHAT WAS DETECTED
        +
WHAT THE VEHICLE IS DOING
        +
OPTIONAL PASSENGER IMPACT

Example:

«Construction ahead. Taking an alternate route. Arrival may be 3 minutes later.»

---

13.4 Preserve calmness

The original PRD specifies a factual and calm explanation tone.

The interface should therefore avoid language that unnecessarily increases emotional arousal.

The explanation should communicate competence without pretending certainty beyond what the system can support.

---

13.5 Avoid explanation overload

Not every autonomous action requires an explanation.

A passenger interface that explains everything can become another source of distraction.

The system should therefore prioritise:

Unexpectedness
      +
Passenger relevance
      +
Safety significance
      +
Interpretive value

rather than simply maximising the number of explanations shown.

---

14. Accessibility Implications

Explanation design must remain accessible across sensory and cognitive differences.

The original PRD specifies:

- captions for audio;
- visual equivalents for sound alerts;
- large-text support;
- screen-reader support;
- high-contrast modes;
- simplified cognitive-accessibility modes;
- voice interaction.

Accordingly, an explanation should not depend exclusively on:

- colour;
- sound;
- small text;
- animation;
- rapid visual changes.

The same semantic information should remain available through appropriate modalities.

---

15. Multimodal Design Implication

The project treats multimodality as a context-dependent design decision rather than an automatic improvement.

For a passenger who is actively looking at the display, a concise visual explanation may be sufficient.

During an attentionally demanding context, an auditory cue may provide useful redundancy.

For accessibility needs, visual and auditory channels should have equivalent semantic meaning where appropriate.

The design principle is therefore:

«Use multiple modalities to increase accessibility and situational availability, not simply to increase information volume.»

---

16. Trust Calibration

The project does not define success as “the passenger trusts the vehicle more.”

That would be an incomplete Human Factors objective.

A better outcome is:

Understanding
      ↓
Appropriate interpretation
      ↓
Appropriate confidence
      ↓
Calibrated trust

An explanation should therefore help the passenger understand why the vehicle behaved as it did without encouraging blind confidence.

This is particularly important for safety-relevant autonomous systems.

---

17. Relationship Between Understanding, Trust and Workload

The project treats the three constructs as related but non-identical.

Understanding without trust

A passenger may understand an action but remain uncomfortable with the system.

Trust without understanding

A passenger may report confidence despite having little understanding of the system.

Understanding with excessive workload

A passenger may technically understand the explanation but need too much effort to process it.

The desired interface therefore occupies the intersection:

             UNDERSTANDING
                  ▲
                  │
                  │
          ┌───────┼───────┐
          │       │       │
          │   DESIRED    │
          │    ZONE      │
          │       │       │
          └───────┼───────┘
                  │
        TRUST ◄───┼───► WORKLOAD

The ideal design supports strong understanding and appropriately calibrated trust while keeping unnecessary workload low.

---

18. What the Project Can Claim

Based on the available project evidence, the following claims are justified:

- The project identifies passenger understanding of autonomous behaviour as a meaningful Human Factors problem.
- The original PRD establishes explainability as a central interaction principle.
- The project converts that product principle into an explicit research question.
- The project defines controlled explanation conditions.
- The project defines measurable dependent variables.
- The project establishes an experimental protocol and analysis framework.
- The project connects explanation design with trust, workload, comprehension, and task performance.
- The project establishes accessibility requirements for explanation delivery.
- The project provides a research-grounded basis for evaluating the interface.

---

19. What the Project Does Not Claim

The project does not claim:

- that one explanation condition was empirically superior without verified participant data;
- that explanation design increases trust by a specific percentage;
- that workload was reduced by a specific amount;
- that the interface has been validated in a real autonomous vehicle;
- that the interface satisfies production safety certification requirements;
- that the design is compliant with ISO 26262;
- that the design has been validated under real-world operational conditions;
- that participant behaviour, gaze, physiology, or other measurements occurred unless actually recorded.

This boundary is an intentional part of the research methodology.

---

20. Final Evidence Position

The strongest conclusion supported at this stage is methodological rather than causal:

«The project establishes a controlled and theoretically grounded framework for investigating how explanation presence and specificity influence passenger understanding, trust, workload, and interaction performance during unexpected autonomous-vehicle behaviour.»

The interface therefore functions simultaneously as:

1. a UX product concept;
2. a Human Factors research instrument;
3. an XAI interaction framework;
4. an accessibility-aware passenger HMI;
5. a reproducible experimental artifact.

---

21. Transition to Final Project Report

The evidence synthesis establishes the structure of the final report:

PROBLEM
   ↓
LITERATURE
   ↓
RESEARCH GAP
   ↓
RESEARCH QUESTIONS
   ↓
THEORETICAL FRAMEWORK
   ↓
HYPOTHESES
   ↓
EXPERIMENTAL DESIGN
   ↓
PROTOTYPE
   ↓
EVALUATION
   ↓
EVIDENCE SYNTHESIS
   ↓
DESIGN IMPLICATIONS
   ↓
LIMITATIONS
   ↓
FUTURE WORK

The project has therefore progressed beyond a conventional UX case study.

Its central contribution is the connection between:

autonomous-system behaviour → passenger explanation → human interpretation → measurable Human Factors outcomes → interface design.

---

22. Day 34 Completion Statement

Day 34 is complete.

The project now has a consolidated evidence position, an explicit boundary between established evidence and unverified empirical claims, and a direct translation from Human Factors constructs into interface design decisions.

No unsupported numerical results have been introduced.

The research framework is ready to be incorporated into the final research-paper-style report and presentation.
