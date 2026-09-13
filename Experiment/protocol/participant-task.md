Participant Task

Project: Autonomous Vehicle Passenger Control Interface
Study Focus: Explanations for unexpected autonomous-vehicle behaviour
Status: Protocol v1
Date: 23 September 2026

---

1. Purpose

This document defines the participant's task during the experimental study.

The participant task is designed to evaluate whether different forms of explanatory information affect passenger understanding, trust, cognitive workload, and interaction performance.

The participant is treated as a passenger rather than as the operator or driver of the autonomous vehicle.

---

2. Participant Role

Participants will be instructed to imagine that they are travelling as passengers in a highly automated/autonomous vehicle.

They are not responsible for controlling the vehicle.

The autonomous system is responsible for driving.

The participant's role is to:

1. observe the journey;
2. interact with the passenger interface when instructed;
3. interpret unexpected vehicle behaviour;
4. answer questions about what occurred;
5. provide subjective ratings.

---

3. General Participant Instructions

Participants should receive instructions similar to the following:

«Imagine that you are travelling as a passenger in an autonomous vehicle.

The vehicle is responsible for navigation and driving.

During the journey, the vehicle may occasionally perform an action that you did not expect.

Pay attention to the vehicle's behaviour and the passenger interface.

After some events, you will be asked questions about what happened.

Answer each question based on what you understood from the journey and interface.

There are no right or wrong opinions. We are interested in your experience and understanding.»

The final participant-facing wording will be reviewed before pilot testing.

---

4. Experimental Trial Structure

Each experimental trial should follow a consistent sequence.

Trial Sequence

1. Scenario begins

↓

2. Participant observes normal journey

↓

3. Unexpected event occurs

↓

4. Autonomous vehicle responds

↓

5. Explanation condition is presented

↓

6. Participant observes the interface

↓

7. Comprehension question

↓

8. Trust-related rating

↓

9. Trial ends

↓

10. Next scenario

The exact timing between these stages will be finalized during prototype implementation and pilot testing.

---

5. Practice Trial

A practice trial should be provided before the experimental trials.

The purpose is to ensure that participants understand:

- how the prototype works;
- how to interact with the interface;
- how to answer comprehension questions;
- how to provide ratings.

Practice data should not automatically be included in the main analysis.

---

6. Experimental Event

During each trial, the participant will encounter an unexpected autonomous-vehicle event.

Example:

A pedestrian enters a crossing ahead.

The autonomous vehicle slows down.

The passenger interface communicates the event according to the assigned explanation condition.

The underlying vehicle response should remain consistent between conditions.

---

7. Explanation Conditions

Condition A — No Explanation

The interface provides no causal explanation.

Example:

«Vehicle slowing.»

The interface should avoid communicating the experimental explanation while still providing sufficient information for the interface to remain coherent.

---

Condition B — Minimal Explanation

The interface communicates the immediate reason.

Example:

«Slowing for pedestrian.»

---

Condition C — Contextual Explanation

The interface communicates both the relevant event and the reason for the resulting vehicle action.

Example:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

---

8. Comprehension Task

After the event, participants will answer a scenario-specific comprehension question.

Example:

«Why did the vehicle slow down?»

The question should be designed so that answering it requires understanding the event rather than simply recognizing a word displayed on the interface.

Potential response formats include:

- multiple choice;
- short answer;
- structured response.

The final format will be selected after pilot testing.

---

9. Trust Measurement

Following the comprehension task, participants will complete a trust-related rating using a validated or appropriately adapted instrument.

The measurement should capture the participant's perception of the autonomous system rather than simply asking whether they "liked" the explanation.

The final trust instrument will be selected before data collection.

---

10. Workload Measurement

Cognitive workload will be assessed using NASA-TLX or another validated workload instrument selected before the main experiment.

The workload assessment should not be unnecessarily repeated after every short trial if doing so would itself create excessive participant burden.

The final measurement schedule will therefore be determined during protocol development and pilot testing.

---

11. Interaction Performance

Where interaction is required, the following may be recorded:

- response time;
- incorrect selections;
- missed interactions;
- task completion;
- interaction errors.

These measures will be treated as secondary outcomes unless the final research design establishes them as primary measures.

---

12. Post-Experiment Questions

After completing all experimental trials, participants may be asked about:

- overall interface experience;
- perceived transparency;
- explanation usefulness;
- confidence in understanding the vehicle;
- perceived clarity;
- preference between explanation types;
- demographic or technology-experience variables relevant to analysis.

Post-experiment questions should be kept separate from trial-level outcome measures.

---

13. Participant Flow

The intended participant flow is:

Consent / study information

↓

Instructions

↓

Practice trial

↓

Experimental trials

↓

Workload/trust/understanding measurements

↓

Post-experiment questionnaire

↓

Debrief

---

14. Debrief

Participants should be informed about the purpose of the study after completing the experiment.

The debrief should explain that the study investigated how different forms of explanation may affect passenger understanding and perceptions of autonomous-vehicle behaviour.

The wording should avoid implying that one explanation condition is necessarily superior before the data are analyzed.

---

15. Data Integrity

Each participant should receive a study identifier rather than having personally identifying information stored with experimental responses.

Personally identifying participant information should not be stored in the public GitHub repository.

If participant data are collected, the public repository should contain only anonymized or appropriately aggregated research data.

---

16. Protocol Status

Status: Preliminary v1

The following remain to be finalized:

- exact trial duration;
- final scenario count;
- explanation display duration;
- question format;
- trust instrument;
- workload measurement schedule;
- participant eligibility;
- sample size;
- randomization;
- statistical analysis.

---

Next Step

Convert the participant task into a complete experimental protocol with exact timing, trial states, measurements, and data fields.
