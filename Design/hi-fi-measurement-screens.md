High-Fidelity Measurement Screens

1. Purpose

This document defines the high-fidelity design and interaction requirements for the experimental measurement screens that follow the autonomous-vehicle event and explanation sequence.

The measurement layer consists of:

- "EXP-06" — Comprehension
- "EXP-07" — Trust / Experience
- "EXP-08" — Cognitive Workload
- "EXP-09" — Trial Complete

These screens are designed to collect structured participant responses without unnecessarily increasing cognitive demand or introducing visual inconsistency between experimental conditions.

The measurement screens are part of the experimental prototype and are not intended to represent a production passenger interface.

---

2. Measurement Design Principles

The measurement layer follows these principles:

1. Measure without contaminating the preceding interaction
2. Use consistent presentation across experimental conditions
3. Keep questions concise and unambiguous
4. Avoid leading participants toward positive or negative responses
5. Separate comprehension from subjective experience
6. Minimize unnecessary visual complexity
7. Preserve accessibility
8. Prevent accidental data loss
9. Maintain consistent interaction patterns
10. Do not imply that one explanation condition is expected to be better

---

3. EXP-06 — Comprehension Screen

3.1 Purpose

The comprehension screen measures whether the participant understood the autonomous vehicle's behaviour during the preceding scenario.

The screen should assess understanding of the event and the vehicle's response rather than asking participants whether they liked the interface.

---

3.2 Information Hierarchy

The hierarchy should be:

1. Screen title
2. Short instruction
3. Scenario comprehension question
4. Response options
5. Continue action

Example structure:

What happened during the previous situation?

Select the answer that best describes what the vehicle responded to.

[ Option A ]

[ Option B ]

[ Option C ]

[ Option D ]

[ Continue ]

The exact wording of the question should be scenario-specific and finalized before participant testing.

---

3.3 Interaction Requirements

- Participant must select one response before continuing.
- Only one response should be selectable when the question requires a single correct answer.
- Selected state must be visually distinguishable.
- The Continue button remains disabled until a valid response is selected.
- The interface must not reveal whether the selected response is correct.
- No correctness feedback should be provided during the experiment unless explicitly defined by the protocol.

---

3.4 Comprehension Measurement

The prototype should record:

- Participant identifier
- Scenario identifier
- Explanation condition
- Selected response
- Correct/incorrect score
- Response time
- Trial identifier

Example data representation:

participant_id
trial_id
scenario_id
condition
comprehension_response
comprehension_correct
comprehension_response_time

---

3.5 Visual Design

The comprehension screen should reuse:

- Global application shell
- Typography system
- Spacing tokens
- Surface components
- Button components
- Semantic interaction states

The screen should visually resemble the main prototype rather than appearing as an unrelated questionnaire.

---

4. EXP-07 — Trust / Experience Screen

4.1 Purpose

This screen captures the participant's subjective evaluation following the scenario.

The measurement should focus on the participant's experience with the autonomous vehicle behaviour and explanation rather than asking directly whether the system is "good" or "safe."

---

4.2 Measurement Structure

The screen should support a standardized response scale.

Example:

How confident were you in the vehicle's response?

Not at all confident

[ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ]

Very confident

The exact question wording and scale anchors must remain consistent across all trials.

---

4.3 Trust Measurement Principle

Trust should be treated as a construct requiring calibrated interpretation.

The design must therefore avoid wording such as:

«"Did the explanation make you trust the vehicle?"»

unless that exact question is part of the finalized research instrument.

Instead, the measurement interface should capture the participant's reported confidence or trust-related judgment using the selected validated or pre-defined instrument.

---

4.4 Interaction Requirements

- One response must be selected before proceeding.
- Scale values must have equal visual weight.
- Scale endpoints must be clearly labelled.
- Selected state must remain visible.
- Participant should be able to change the response before continuing.
- No response should be visually emphasized as desirable.
- Continue should activate only after a valid response.

---

4.5 Data Capture

Potential fields:

participant_id
trial_id
scenario_id
condition
trust_response
trust_response_time

Additional subjective measures may be captured if included in the finalized experimental protocol.

---

5. EXP-08 — Cognitive Workload Screen

5.1 Purpose

The workload screen captures the participant's perceived mental demand associated with the trial.

The screen should use the finalized workload instrument defined in the research protocol.

NASA-TLX may be used if retained as the selected workload measure.

---

5.2 Measurement Integrity

The visual design should not alter the conceptual structure of the selected measurement instrument.

If a validated instrument is used, its required instructions, scales, dimensions, anchors, and scoring procedure should be preserved according to the finalized protocol.

The interface should not simplify or modify a validated instrument merely for aesthetic consistency.

---

5.3 Screen Structure

The general structure may be:

How mentally demanding was the previous task?

[ Workload scale / instrument ]

[ Continue ]

The final implementation must follow the actual measurement protocol rather than this placeholder structure.

---

5.4 Interaction Requirements

- All required workload responses must be completed.
- Scale interactions must be easy to operate.
- Selected values must remain visible.
- No response should be visually preferred.
- The participant must be able to review selections before submission where appropriate.
- Continue remains unavailable until required inputs are complete.

---

5.5 Data Capture

Potential fields:

participant_id
trial_id
scenario_id
condition
workload_measure
workload_response_time

If NASA-TLX is implemented using its constituent dimensions, the dataset should preserve the individual dimension responses rather than storing only a final aggregate.

---

6. EXP-09 — Trial Complete Screen

6.1 Purpose

The trial completion screen provides a clear transition from one experimental trial to the next.

It confirms completion without providing performance feedback.

---

6.2 Information Hierarchy

Trial complete

The previous trial has been recorded.

[ Continue ]

The wording should remain neutral.

---

6.3 Requirements

The completion screen must:

- confirm that the trial has ended;
- prevent accidental duplicate submission;
- provide a clear transition to the next trial;
- avoid displaying comprehension correctness;
- avoid displaying trust scores;
- avoid comparing explanation conditions;
- avoid evaluative feedback.

---

7. Measurement Flow

The complete post-event measurement sequence is:

Autonomous Response
        ↓
Explanation
        ↓
Passenger Observation
        ↓
Comprehension
        ↓
Trust / Experience
        ↓
Cognitive Workload
        ↓
Trial Complete

The sequence must remain identical across explanation conditions.

---

8. Condition Independence

The measurement screens must not reveal the participant's experimental condition.

For example:

No Explanation
      ↓
Comprehension
      ↓
Trust
      ↓
Workload
      ↓
Complete

Minimal Explanation
      ↓
Comprehension
      ↓
Trust
      ↓
Workload
      ↓
Complete

Contextual Explanation
      ↓
Comprehension
      ↓
Trust
      ↓
Workload
      ↓
Complete

Only the explanation presentation changes.

---

9. Accessibility

The measurement screens must support:

- sufficient text size;
- clear contrast;
- large interactive targets;
- visible focus/selection states;
- non-colour-only state communication;
- readable scale labels;
- consistent navigation;
- simple language;
- predictable interaction behaviour.

Accessibility decisions should remain consistent with the broader project design system.

---

10. Experimental Integrity

The measurement interface must not:

- reveal the hypothesis;
- identify the "correct" explanation condition;
- praise or criticize participant responses;
- provide correctness feedback during trials;
- change question wording between conditions;
- change scale structure between conditions;
- introduce condition-specific visual styling.

The goal is to ensure that differences in measured outcomes can be more plausibly attributed to the experimental manipulation rather than unrelated interface differences.

---

11. Figma Implementation

Recommended Figma frames:

EXP-06 Comprehension
EXP-07 Trust
EXP-08 Workload
EXP-09 Trial Complete

Recommended reusable components:

MeasurementHeader
QuestionBlock
SingleChoiceOption
LikertScale
ScaleLabel
ContinueButton
TrialCompletionCard

---

12. Definition of Done

Day 24 measurement screens are complete when:

- [ ] EXP-06 is implemented in high fidelity.
- [ ] EXP-07 is implemented in high fidelity.
- [ ] EXP-08 is implemented in high fidelity.
- [ ] EXP-09 is implemented in high fidelity.
- [ ] All screens use the established design system.
- [ ] Measurement wording matches the finalized protocol.
- [ ] No condition-specific measurement styling exists.
- [ ] Required validation states are implemented.
- [ ] Accessibility checks are performed.
- [ ] Measurement data fields are mapped to the data schema.
- [ ] The screens can be connected to the main experimental flow.
