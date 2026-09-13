Experimental Scenario Framework

Project: Autonomous Vehicle Passenger Control Interface
Status: Scenario framework v1
Date: 22 September 2026

---

1. Purpose

The purpose of the scenario framework is to define controlled autonomous-vehicle events that can be used to evaluate passenger-facing explanations.

The scenarios should represent plausible situations in which a passenger may notice an unexpected change in autonomous-vehicle behaviour and seek an explanation.

The scenarios are not intended to simulate every possible autonomous-driving edge case.

They are designed to create controlled experimental events in which:

1. the vehicle behaviour is understandable;
2. the passenger has a reason to seek an explanation;
3. the interface can communicate the reason;
4. the event can be reproduced consistently;
5. the explanation condition can be manipulated independently.

---

2. Scenario Design Principles

Each scenario should satisfy the following principles.

Principle 1 — Consistent Vehicle Behaviour

The autonomous vehicle should perform the same underlying action regardless of explanation condition.

Principle 2 — Clear Causal Relationship

There should be a reasonably understandable relationship between the environmental event and the vehicle response.

Principle 3 — Passenger Relevance

The event should be something a passenger could reasonably notice or consider important.

Principle 4 — Controlled Complexity

The scenario should contain enough environmental information to feel plausible without introducing unnecessary confounds.

Principle 5 — Explanation Compatibility

The event must provide a meaningful basis for generating:

- no explanation;
- minimal explanation;
- contextual explanation.

Principle 6 — Safety-Relevant but Non-Crisis

The initial study should focus on unexpected behaviour without relying exclusively on catastrophic emergency events.

---

3. Candidate Scenario Categories

Scenario A — Pedestrian Crossing

Environmental event: Pedestrian enters or approaches a crossing.

Vehicle response: Vehicle reduces speed.

Passenger-facing explanation:

Minimal:

«Slowing for pedestrian.»

Contextual:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

Primary construct: Understanding of vehicle intent.

---

Scenario B — Vehicle Merging

Environmental event: Another vehicle merges into the autonomous vehicle's path.

Vehicle response: Vehicle reduces speed and increases following distance.

Minimal explanation:

«Slowing for merging vehicle.»

Contextual explanation:

«Vehicle merging ahead. Slowing to maintain a safe following distance.»

Primary construct: Understanding of reactive behaviour.

---

Scenario C — Obstacle Ahead

Environmental event: Temporary obstacle is detected in the vehicle's planned path.

Vehicle response: Vehicle slows or changes its trajectory.

Minimal explanation:

«Slowing for obstacle ahead.»

Contextual explanation:

«Obstacle detected in the planned path. Slowing while selecting a safe path around it.»

Primary construct: Understanding of system decision-making.

---

Scenario D — Road Condition / Construction

Environmental event: Temporary road construction or restricted lane.

Vehicle response: Vehicle reduces speed or changes lane.

Minimal explanation:

«Adjusting for road construction.»

Contextual explanation:

«Road construction is restricting the current lane. Adjusting speed and position to continue safely.»

Primary construct: Understanding of planned adaptation.

---

4. Scenario Selection Criteria

The final scenarios should be selected using the following criteria:

Criterion| Requirement
Reproducibility| High
Causal clarity| High
Passenger relevance| High
Explanation suitability| High
Interface compatibility| High
Environmental complexity| Controlled
Safety sensitivity| Moderate
Potential learning effect| Low
Technical implementation complexity| Manageable

---

5. Scenario Variables

Each scenario should document:

- Scenario ID
- Environment
- Initial vehicle state
- Passenger activity
- Trigger event
- Vehicle response
- Event onset
- Explanation onset
- Explanation condition
- Expected passenger interpretation
- Comprehension question
- Expected correct response
- Potential confounds

---

6. Example Scenario Specification

Scenario ID

"SCN-01"

Title

Pedestrian Crossing

Initial State

The autonomous vehicle is travelling normally through an urban environment.

Trigger Event

A pedestrian begins entering a marked crossing ahead.

Autonomous Response

The vehicle reduces speed to maintain an appropriate distance.

Explanation Condition A

No explanatory information.

Explanation Condition B

«Slowing for pedestrian.»

Explanation Condition C

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

Passenger Question

«Why did the vehicle slow down?»

Expected Answer

The vehicle slowed because a pedestrian was entering the crossing ahead.

Primary Construct

Passenger understanding.

Secondary Constructs

- Trust
- Workload
- Perceived transparency

---

7. Scenario Equivalence

When multiple scenarios are used, the scenarios should be comparable in terms of:

- event visibility;
- explanation length;
- information complexity;
- response magnitude;
- question difficulty;
- interaction requirements.

Perfect equivalence may not be possible.

Therefore, scenario-specific differences should be documented and considered during analysis.

---

8. Scenario Development Process

The scenario-development process will be:

Literature → Scenario concept → Prototype implementation → Internal review → Pilot → Revision → Main experiment

Scenarios should not be finalized solely because they appear visually convincing.

They must also be suitable for controlled measurement.

---

9. Scenario Exclusion Criteria

A scenario should be reconsidered or removed if:

- the vehicle response is ambiguous;
- multiple explanations are equally plausible;
- the explanation contains information unavailable to the passenger;
- the scenario requires unsupported claims about autonomous-system perception;
- the event is too difficult to reproduce consistently;
- the explanation is substantially longer than the equivalent explanations;
- the event introduces unnecessary emotional distress;
- participants could answer the comprehension question without processing the explanation.

---

10. Initial Scenario Set

The initial candidate set is:

1. Pedestrian crossing
2. Vehicle merging
3. Obstacle ahead
4. Road construction / lane restriction

The final number of scenarios will be determined after pilot testing and power/sample-size considerations.

---

11. Research Integrity

The scenario descriptions represent experimental abstractions.

They should not be interpreted as claims about how a production autonomous vehicle necessarily detects, predicts, or responds to the specified events.

The experiment concerns the passenger interface and explanatory communication.

---

Status

Scenario framework: v1
Candidate scenarios: 4
Final scenarios: Not yet locked
Next step: Develop scenario scripts, timing diagrams, and participant tasks
