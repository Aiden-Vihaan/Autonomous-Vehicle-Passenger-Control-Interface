Paper Analysis

Purpose

Day 9 moves the literature review from citation collection to methodological analysis.

Instead of asking only:

«What did previous researchers find?»

the project asks:

«How did previous researchers investigate the problem, what variables did they manipulate, how did they measure outcomes, and which elements can be appropriately adapted to this project?»

The objective is to ensure that the experimental design is informed by empirical Human Factors research rather than by assumptions derived from interface design alone.

---

Paper 1

Du et al. (2019)

Full Citation

Du, N., Haspiel, J., Zhang, Q., Tilbury, D., Pradhan, A. K., Yang, X. J., & Robert, L. P. Jr. (2019).

"Look Who's Talking Now: Implications of AV's Explanations on Driver's Trust, AV Preference, Anxiety and Mental Workload."

Transportation Research Part C: Emerging Technologies, 104, 428–442.

DOI:

10.1016/j.trc.2019.05.025

---

Research Objective

The study investigated whether explanations provided by an autonomous vehicle influence:

- Trust
- AV preference
- Anxiety
- Mental workload

It specifically examined the timing and interaction structure of explanations.

---

Participants

The experiment involved:

32 participants.

---

Experimental Method

A within-subject driving-simulator experiment was conducted.

Four conditions were examined:

1. No explanation.
2. Explanation before the AV acted.
3. Explanation after the AV acted.
4. Explanation followed by an opportunity to approve/disapprove the AV action.

The source record confirms that the study used four experimental conditions and a driving simulator.

---

Important Variables

Independent Variable

Explanation condition.

Important Manipulation

Explanation timing:

- Before action
- After action

Dependent Variables

- Trust
- AV preference
- Anxiety
- Mental workload

---

Main Finding Relevant to Our Project

The study provides evidence that when an explanation is delivered can matter, rather than explanation presence being the only important factor.

This supports our decision to investigate explanation timing.

---

What We Can Borrow

We can adapt the general experimental logic:

Same autonomous event
        ↓
Different explanation timing
        ↓
Measure passenger response

This provides a cleaner causal comparison than changing the entire interface between conditions.

---

What We Should NOT Borrow Directly

The participants were interacting in a driving context.

Our project concerns passengers in a highly automated vehicle.

Therefore:

«Driver findings must not automatically be treated as passenger findings.»

This distinction will remain important throughout the literature review.

---

Paper 2

Ha et al. (2020)

Full Citation

Ha, T., Kim, S., Seo, D., & Lee, S. (2020).

"Effects of explanation types and perceived risk on trust in autonomous vehicles."

Transportation Research Part F: Traffic Psychology and Behaviour, 73, 271–280.

DOI:

10.1016/j.trf.2020.06.021

---

Research Objective

The study investigated how:

- Explanation type
- Perceived risk

affect trust in autonomous vehicles.

---

Experimental Structure

The researchers examined:

Explanation

Three levels:

1. No explanation
2. Simple explanation
3. Attributional explanation

Driving Situation

Four situations with different levels of perceived risk.

This resulted in:

12 experimental conditions.

The study used a simulator-based experiment.

---

Key Finding

Explanation type significantly affected trust.

More importantly:

«Perceived risk moderated the effect of explanation type on trust.»

The relationship was therefore not constant across situations.

---

Critical Implication

This challenges a simple model:

Explanation
     ↓
Higher Trust

A more realistic model is:

Explanation
     +
Situation Risk
     ↓
Trust

---

What We Can Borrow

The project should consider whether unexpected events should be classified according to:

- Low urgency
- Moderate urgency
- High urgency

However, this should only become an experimental variable if it can be manipulated without introducing unnecessary complexity.

---

What We Should NOT Borrow Directly

The exact explanation categories used by Ha et al. should not automatically become our interface categories.

Our explanation taxonomy should be derived from:

- Literature
- Existing PRD requirements
- Human Factors principles
- Pilot testing

---

Paper 3

Strauch et al. (2019)

Full Citation

Strauch, C., Mühl, K., Patro, K., Grabmaier, C., Reithinger, S., Baumann, M., & Huckauf, A. (2019).

"Real autonomous driving from a passenger's perspective: Two experimental investigations using gaze behaviour and trust ratings in field and simulator."

Transportation Research Part F: Traffic Psychology and Behaviour, 66, 15–28.

DOI:

10.1016/j.trf.2019.08.013

---

Research Objective

The researchers investigated:

- Passenger gaze behaviour
- Safety-relevant visual attention
- Trust

during autonomous and manual driving.

---

Experimental Context

The research included:

- Real traffic
- Simulator conditions

The researchers examined passenger eye movements and trust ratings.

---

Key Finding

Passengers showed more fixations toward safety-relevant regions during safety-critical driving situations than during regular driving.

The study also found differences in trust depending on driving mode and context.

---

Important Limitation

The authors specifically note that gaze toward safety-relevant regions may not be a sufficiently exhaustive alternative to passenger trust ratings.

This is important.

Therefore:

Gaze ≠ Trust

and:

Gaze ≠ Situation Awareness

without additional evidence.

---

Implication for Our Project

Eye tracking can potentially provide useful behavioural evidence.

However, if eye tracking becomes part of our study, it should be treated as:

«An additional behavioural measure.»

It should not replace:

- Comprehension measures
- Trust measures
- Workload measures
- Situation-awareness measures

---

Paper 4

Hong et al. (2025)

Full Citation

Hong, J., Kim, S., & Lee, S. (2025).

"Enhancing passenger-vehicle interaction through multimodal explanation for unexpected behaviors of fully autonomous driving in non-driving-related tasks."

Transportation Research Part F: Traffic Psychology and Behaviour, 109, 1350–1364.

---

Research Objective

The study examined multimodal XAI for passengers experiencing unexpected autonomous-vehicle behaviour while performing non-driving-related tasks.

This is particularly relevant because the current project is passenger-oriented rather than driver-oriented.

---

Main Factors

The research considered:

- Explanation modality
- Passenger engagement in non-driving-related tasks
- Unexpected vehicle behaviour

---

Main Finding

Speech explanations increased situation awareness and trust when passengers were not engaged in non-driving-related tasks.

Visual explanations improved pragmatic UX when passengers were engaged in non-driving-related tasks.

Multimodal explanations were not universally superior and could reduce hedonic UX for passengers engaged in non-driving tasks.

---

Critical Design Lesson

The assumption:

«Visual + audio = automatically better»

is not supported.

Instead:

Explanation Modality
        +
Passenger Activity
        ↓
Interaction Outcome

---

Implication

Our prototype should support multimodal interaction architecturally.

However, our experiment should only test modality if it can be done rigorously within the project scope.

We should not add extra experimental conditions simply to make the study appear more sophisticated.

---

Paper 5

Lee et al. (2024)

Full Citation

Lee et al. (2024).

"Critical roles of explainability in shaping perception, trust, and acceptance of autonomous vehicles."

International Journal of Industrial Ergonomics, 100, 103568.

DOI:

10.1016/j.ergon.2024.103568

---

Research Objective

The study investigated the role of perceived explainability in:

- Trust
- Perception
- Acceptance

of autonomous vehicles.

---

Participants

The study analyzed responses from:

399 participants.

---

Experimental/Research Structure

Participants were exposed to different AV introductions, including:

- Basic introduction
- Video introduction
- Introduction including how + why explanations

Structural equation modelling was used to investigate relationships among constructs.

---

Main Finding

Perceived explainability had a strong influence on trust and acceptance.

The study also found that perceived explainability affected perceptions such as:

- Ease of use
- Usefulness
- Safety
- Intelligence

which subsequently contributed to trust and acceptance.

---

Important Limitation for Our Project

This research primarily addresses perceptions and acceptance.

Our project is interested in:

- Real-time interaction
- Unexpected events
- Passenger understanding
- Explanation timing
- Workload
- Interaction performance

Therefore, this paper supports the importance of explainability but does not directly establish the effectiveness of our proposed real-time interface.

---

Cross-Paper Comparison

Paper| Context| Main Manipulation| Main Outcomes| Most Relevant Lesson
Du et al. 2019| Driver / simulator| Explanation timing| Trust, workload, anxiety, preference| Timing matters
Ha et al. 2020| AV / simulator| Explanation type × risk| Trust| Context changes explanation effects
Strauch et al. 2019| Passenger / field + simulator| Driving mode/context| Gaze, trust| Passenger ≠ driver
Hong et al. 2025| Passenger / FAV| Modality × passenger activity| SA, trust, UX| Multimodal ≠ automatically better
Lee et al. 2024| AV perception| Explainability| Trust, acceptance| Explainability is important for trust

---

Cross-Paper Conclusion

The literature supports a conditional model of explanation effectiveness.

The project should therefore investigate:

Explanation Design
       +
Interaction Context
       +
Passenger Context
       ↓
Understanding / SA
       ↓
     Trust
       +
   Workload
       ↓
Interaction Quality

This model is more defensible than assuming that increasing explanation quantity automatically improves the passenger experience.
