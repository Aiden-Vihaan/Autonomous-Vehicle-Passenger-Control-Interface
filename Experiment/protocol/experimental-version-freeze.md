Experimental Version Freeze

Project: Autonomous Vehicle Passenger Control Interface
Research Focus: Explanations for unexpected autonomous-vehicle behaviour
Milestone: Day 28
Status: Experimental design frozen
Version: EVF-1.0

---

1. Purpose

This document establishes the controlled experimental version of the Autonomous Vehicle Passenger Control Interface.

The project began as a product and UX design assignment for a passenger-facing interface for Level 4 autonomous vehicles. The original product brief identifies passenger trust, transparency, safety communication, accessibility, and understandable explanations of autonomous decisions as central design objectives.

The research layer narrows this broader product problem into one experimentally testable question:

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

The purpose of this freeze is to ensure that the experimental interface, independent variable, dependent variables, scenarios, participant instructions, and measurement procedure remain stable during formal data collection.

---

2. Experimental Scope

The experiment evaluates passenger-facing explanations accompanying unexpected autonomous-vehicle behaviour.

The study does not evaluate:

- autonomous-driving performance;
- vehicle perception accuracy;
- the underlying autonomy stack;
- actual vehicle safety;
- production-level autonomous-vehicle certification;
- ISO 26262 compliance;
- SAE certification;
- real-world driving performance;
- the correctness of an actual autonomous vehicle's decisions.

The vehicle behaviour represented in the prototype is a controlled experimental simulation.

The experiment therefore evaluates the human-facing interface and explanation design, rather than the autonomous-driving system itself.

---

3. Primary Research Question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

---

4. Secondary Research Questions

RQ1 — Explanation presence

Does providing an explanation improve passenger understanding of an unexpected autonomous-vehicle action compared with providing no explanation?

RQ2 — Explanation specificity

Does a contextual explanation provide greater understanding and more appropriate trust than a minimal explanation?

RQ3 — Timing

Does presenting an explanation close to the autonomous action help passengers interpret the event more effectively?

RQ4 — Cognitive demand

How does explanation presentation affect perceived cognitive workload?

RQ5 — Trust calibration

Does explanation quality influence whether passenger trust appropriately reflects the presented system behaviour?

---

5. Experimental Independent Variable

The primary manipulated variable is:

Explanation condition

Three controlled interface conditions are defined.

Condition A — No Explanation

The vehicle performs the represented action without presenting a textual explanation.

Example:

«Vehicle slows.»

No reason is presented through the experimental explanation component.

---

Condition B — Minimal Explanation

The interface presents a short explanation identifying the immediate reason for the action.

Example:

«Slowing for pedestrian.»

The message is intentionally concise and provides limited contextual information.

---

Condition C — Contextual Explanation

The interface presents a structured explanation containing:

1. what the vehicle detected;
2. what the vehicle is doing;
3. the immediate passenger-relevant implication.

Example:

«Pedestrian entering the crossing ahead.
Slowing to maintain a safe distance.»

The wording follows the product requirement that explanations communicate the reason for an autonomous decision in plain language.

---

6. Dependent Variables

6.1 Comprehension

Primary measure of passenger understanding.

Participants are asked questions concerning the autonomous event after selected scenarios.

Example constructs:

- What caused the vehicle to slow?
- What action did the vehicle take?
- What was the likely purpose of the action?

The comprehension score represents the proportion of correctly answered questions.

---

6.2 Response Time

Response time measures the time required to provide the comprehension response.

Where technically possible, timing begins at presentation of the comprehension prompt and ends when the participant submits the response.

Response time will be analysed alongside accuracy rather than interpreted independently.

---

6.3 Trust

Trust is measured as the participant's reported confidence in the autonomous system following the represented event.

Trust will be treated as a subjective construct rather than interpreted as evidence of actual vehicle reliability.

---

6.4 Cognitive Workload

Perceived workload will be measured using the NASA Task Load Index framework where the selected implementation permits it.

The project uses workload as an evaluation construct because an explanation can potentially improve understanding while simultaneously increasing information-processing demands.

---

6.5 Perceived Understanding

Participants report how well they believe they understood the reason for the vehicle's behaviour.

This measure is distinct from objective comprehension.

A participant may believe they understand an event without answering comprehension questions correctly.

---

7. Secondary Observational Variables

The following may be recorded where the prototype or study setup supports them:

- task completion;
- interaction errors;
- hesitation;
- navigation errors;
- explanation dismissal behaviour;
- requests for clarification;
- qualitative comments;
- visible confusion;
- accessibility-related interaction problems.

These observations are supplementary.

They will not be represented as quantitative findings unless they are systematically recorded.

---

8. Variables Not Included in the Experimental Claim

The project does not claim to measure:

- eye-tracking metrics unless dedicated eye-tracking equipment is actually used;
- physiological arousal;
- heart-rate variability;
- galvanic skin response;
- EEG;
- biometric stress;
- actual passenger safety;
- real-world trust behaviour;
- autonomous-driving reliability.

The interface may be designed with future multimodal measurement in mind, but unavailable instrumentation will not be presented as collected evidence.

---

9. Controlled Elements

The following elements are frozen across experimental conditions unless the manipulation explicitly requires otherwise:

- vehicle scenario;
- event type;
- route context;
- passenger role;
- primary display format;
- typography;
- component hierarchy;
- interaction structure;
- comprehension question;
- measurement procedure;
- participant instructions;
- experimental terminology;
- safety framing;
- visual design system;
- general interaction timing.

The explanation condition is the principal manipulated interface factor.

---

10. Explanation Design Principle

All explanation conditions are derived from the same conceptual event.

The difference between conditions is therefore information presentation, not a different underlying scenario.

The conceptual mapping is:

AUTONOMOUS EVENT
       ↓
WHAT WAS DETECTED?
       ↓
WHAT IS THE VEHICLE DOING?
       ↓
WHAT DOES THIS MEAN FOR THE PASSENGER?

This preserves comparability between explanation conditions.

---

11. Scenario Model

The experimental prototype represents unexpected but understandable autonomous-vehicle events.

The scenario architecture follows:

NORMAL JOURNEY
      ↓
UNEXPECTED EVENT
      ↓
EVENT CLASSIFICATION
      ↓
EXPLANATION CONDITION
      ↓
PASSENGER INTERPRETATION
      ↓
COMPREHENSION / TRUST / WORKLOAD
      ↓
JOURNEY CONTINUES

The underlying product concept treats unexpected autonomous behaviour as an important explanation moment because riders may otherwise be uncertain about why the vehicle slowed, stopped, hesitated, or changed its behaviour.

---

12. Experimental Integrity Rules

The following rules are permanently frozen:

1. No participant data will be invented.
2. No pilot observation will be represented as participant evidence unless actually observed.
3. Pilot observations will remain separate from formal experimental findings.
4. Experimental conditions will not be changed after formal data collection begins without documentation.
5. Changes affecting the independent variable require a new experimental version.
6. Changes affecting the measurement procedure require protocol documentation.
7. Prototype bugs will be distinguished from participant interaction errors.
8. Qualitative comments will not be converted into numerical findings without a defined coding procedure.
9. Small samples will not be presented as population-level evidence.
10. The study will not claim validation of a real autonomous-driving system.

---

13. Version-Control Decision

Experimental version: EV-1.0

The following are considered frozen for formal experimentation:

- research question;
- explanation conditions;
- primary constructs;
- scenario logic;
- participant instructions;
- experimental flow;
- measurement framework;
- data schema;
- analysis strategy.

Further modifications are permitted only when they correct:

- a technical failure;
- an ambiguity that threatens experimental validity;
- an accessibility barrier;
- an unintended confound;
- a safety/procedural problem.

Any such change must be documented in the research log.

---

14. Completion Criteria

The experimental version is considered ready when:

- the three explanation conditions can be reliably distinguished;
- every experimental scenario has a defined state sequence;
- participant instructions are standardized;
- comprehension questions are fixed;
- trust and workload measures are defined;
- data fields are predefined;
- the experimenter procedure is documented;
- technical failure handling is documented;
- version control is active;
- no unresolved issue threatens the primary research question.

---

15. Day 28 Decision

Decision: EXPERIMENTAL DESIGN FROZEN.

The project is now transitioning from interface development toward controlled empirical evaluation.

The next stage is formal participant data collection using the frozen experimental version.

---

16. Git Commit

Day 28: Freeze experimental design and analysis plan

---

17. Research Integrity Statement

This document defines the intended experimental configuration. It does not constitute evidence that a particular explanation condition has already produced superior comprehension, trust, or workload outcomes.

Empirical conclusions will be based only on observations and measurements actually collected during the formal study.
