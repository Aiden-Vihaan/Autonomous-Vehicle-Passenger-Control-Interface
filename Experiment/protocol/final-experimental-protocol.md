Final Experimental Protocol

Project: Autonomous Vehicle Passenger Control Interface
Study Version: EV-1.0
Protocol Version: FEP-1.0
Milestone: Day 28
Status: Final protocol for formal evaluation

---

1. Study Objective

This study evaluates how different passenger-facing explanations of unexpected autonomous-vehicle behaviour influence:

1. understanding;
2. trust;
3. perceived cognitive workload;
4. perceived understanding;
5. response performance.

The study uses a controlled interactive prototype rather than a real autonomous vehicle.

---

2. Research Question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

---

3. Study Design

The experiment uses controlled explanation conditions applied to equivalent autonomous-vehicle events.

Explanation conditions

Condition| Description
A| No explanation
B| Minimal explanation
C| Contextual explanation

The purpose of this structure is to isolate the contribution of explanation information while keeping the represented vehicle event constant.

---

4. Participant Role

Participants assume the role of a passenger travelling in a driverless vehicle.

They are not asked to drive the vehicle or supervise its operation.

The participant's task is to experience the journey and interact with the passenger interface when instructed.

This reflects the underlying product concept in which the passenger does not drive and instead uses the interface to understand, trust, and interact with a vehicle operating autonomously.

---

5. Standardized Participant Introduction

The following introduction is used consistently:

«You will interact with a simulated passenger interface for an autonomous vehicle.

Imagine that you are travelling as a passenger. You are not responsible for driving the vehicle.

During the journey, the vehicle may perform actions such as slowing down or changing its behaviour. Please interact with the interface as you naturally would as a passenger.

There are no right or wrong ways to feel about the vehicle. We are evaluating the interface, not you.

Please pay attention to what happens during the journey because you will answer questions about selected events afterward.»

The explanation hypothesis is not disclosed.

---

6. Experimental Sequence

Each experimental interaction follows the same general sequence.

Participant briefing
        ↓
Practice interaction
        ↓
Experimental journey
        ↓
Unexpected autonomous event
        ↓
Explanation condition
        ↓
Participant continues journey
        ↓
Comprehension measurement
        ↓
Trust measurement
        ↓
Workload measurement
        ↓
Next trial
        ↓
Final debrief

---

7. Practice Phase

A practice interaction is provided before experimental trials.

The practice phase introduces:

- the passenger role;
- interface navigation;
- interaction conventions;
- response mechanism;
- general journey structure.

The practice event does not form part of the primary analysis.

Its purpose is to reduce learning effects caused by unfamiliarity with the prototype.

---

8. Experimental Event

The core event is an unexpected autonomous-vehicle behaviour.

A representative event is:

«A pedestrian enters a crossing ahead of the vehicle, resulting in the vehicle slowing to maintain an appropriate distance.»

The same underlying event is represented across explanation conditions.

---

9. Condition A — No Explanation

The vehicle changes behaviour.

The passenger interface does not provide an explanation card.

The participant therefore receives the vehicle action without an explicit causal explanation through the experimental explanation component.

---

10. Condition B — Minimal Explanation

The interface presents:

«Slowing for pedestrian.»

The explanation identifies the immediate cause while minimizing contextual detail.

---

11. Condition C — Contextual Explanation

The interface presents:

«Pedestrian entering the crossing ahead.
Slowing to maintain a safe distance.»

This condition communicates the detected event and the vehicle response in a compact passenger-facing explanation.

The original product requirements describe explanation cards as concise, plain-language communication of what the vehicle noticed, what it is doing, and the resulting passenger impact.

---

12. Comprehension Measurement

Following selected scenarios, the participant answers questions about the event.

The questions assess whether the participant understood:

Cause

What caused the vehicle to change its behaviour?

Action

What did the vehicle do?

Purpose

Why did the vehicle perform that action?

A response is coded as correct only when it corresponds to the information represented in the scenario.

---

13. Response-Time Measurement

Where the implementation supports automatic timing:

Question displayed
        ↓
Timer starts
        ↓
Participant responds
        ↓
Response submitted
        ↓
Timer stops

The measured variable is:

Response time = submission timestamp − question presentation timestamp

If timing cannot be captured reliably, the missing measurement will be documented rather than reconstructed or estimated.

---

14. Trust Measurement

Participants provide a subjective assessment of trust following the relevant interaction.

Trust is treated as a perception of the presented automated system.

The measurement does not imply that the participant has objectively verified the safety or reliability of the simulated vehicle.

---

15. Workload Measurement

Perceived workload is measured using the selected NASA-TLX implementation.

The measurement is intended to capture the participant's perceived mental and task demands associated with the interaction.

Workload is interpreted as a human-factors outcome rather than as a direct measurement of neurological or physiological load.

---

16. Perceived Understanding

Participants provide a subjective assessment of how well they understood the reason for the vehicle's behaviour.

This measure is deliberately separated from objective comprehension.

The study therefore distinguishes:

OBJECTIVE UNDERSTANDING
        ≠
PERCEIVED UNDERSTANDING

This distinction allows the analysis to identify potential discrepancies between feeling informed and actually understanding the event.

---

17. Experimental Data Structure

Each observation is conceptually represented as:

Field| Description
participant_id| Anonymous study identifier
trial_id| Trial identifier
scenario_id| Scenario identifier
explanation_condition| A, B, or C
comprehension| Correct/incorrect or predefined score
response_time| Recorded response time where available
trust| Participant trust response
workload| Workload response
perceived_understanding| Subjective understanding
task_success| Whether the required task was completed
interaction_error| Defined interaction error if present
qualitative_note| Relevant participant comment/observation
protocol_deviation| Whether a deviation occurred

No personally identifying information is required for the core analysis dataset.

---

18. Experimental Controls

The following remain constant wherever possible:

- scenario;
- autonomous event;
- passenger role;
- interface structure;
- display dimensions;
- typography;
- visual hierarchy;
- interaction mechanism;
- measurement questions;
- general task instructions.

The explanation condition is the primary experimental manipulation.

---

19. Counterbalancing Principle

Where participants experience multiple explanation conditions, condition order should be counterbalanced or randomized according to the implemented study design.

The purpose is to reduce systematic order effects such as:

- learning;
- fatigue;
- increasing familiarity;
- expectation effects;
- adaptation to the interface.

The exact allocation used during data collection must be recorded in the dataset.

---

20. Protocol Deviations

A protocol deviation is any occurrence that causes the actual procedure to differ materially from the frozen protocol.

Examples include:

- wrong explanation condition displayed;
- incorrect scenario;
- missing questionnaire item;
- prototype failure;
- accidental experimenter prompting;
- participant receiving information not specified in the protocol.

Each deviation must be recorded.

A deviation does not automatically invalidate a participant's data. Its impact is evaluated during analysis.

---

21. Technical Failure Procedure

If the prototype fails:

1. stop the affected trial;
2. record the failure;
3. do not invent or reconstruct missing measurements;
4. restart the trial only if doing so is methodologically justified;
5. record whether the trial was repeated;
6. retain the original failure record.

Technical reliability is treated separately from participant performance.

---

22. Accessibility Procedure

The interface is designed around the original product requirement that critical alerts and controls should support multiple modalities and that accessibility should be treated as a core product requirement.

During evaluation, accessibility-related problems are recorded as usability/protocol observations.

They are not silently corrected during a trial because doing so could introduce uncontrolled variation.

---

23. Experimenter Conduct

The experimenter must:

- follow the standardized introduction;
- avoid revealing the research hypothesis;
- avoid suggesting preferred answers;
- avoid explaining the autonomous event unless the protocol explicitly requires it;
- use consistent instructions;
- document deviations;
- distinguish observations from interpretations.

The experimenter must not tell participants that one explanation is expected to be better.

---

24. Debrief

At the end of the session, the participant is informed that the study examined different ways of communicating autonomous-vehicle behaviour.

The participant may then provide qualitative feedback concerning:

- clarity;
- trust;
- information amount;
- perceived helpfulness;
- distraction;
- preferred explanation style;
- concerns about autonomous behaviour.

Qualitative comments are treated as supplementary evidence unless a formal qualitative coding procedure is applied.

---

25. Data Integrity Rules

The following rules apply to all collected data:

- Missing data remain missing.
- No responses are fabricated.
- No response time is estimated from memory.
- No participant is removed solely because their response contradicts the design expectation.
- Outliers are not removed without a documented rule.
- Qualitative comments are preserved where ethically appropriate.
- Pilot observations are not mixed with formal participant data.
- Protocol deviations are retained in the study record.

---

26. Completion Standard

The protocol is considered final when the experimenter can execute the study from this document without requiring undocumented decisions about:

- what the participant is told;
- what the participant does;
- what condition is shown;
- what is measured;
- how failures are handled;
- how observations are recorded.

Status: FINAL.

---

27. Research Integrity Statement

The protocol defines how empirical evidence will be collected.

It does not itself establish that explanations improve trust, comprehension, or workload.

Those conclusions require actual participant observations and analysis.

---

28. Version

Protocol: FEP-1.0
Experimental build: EV-1.0
Freeze milestone: Day 28
Next stage: Formal data collection and analysis
