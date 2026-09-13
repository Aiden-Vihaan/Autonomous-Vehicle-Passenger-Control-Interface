Scenario Scripts

1. Purpose

This document defines the standardized scenarios that will be used in the experimental prototype for the Autonomous Vehicle Passenger Control Interface.

The purpose of the scenario scripts is to ensure that the underlying autonomous-vehicle behaviour remains consistent across experimental conditions while the explanation presented to the passenger is systematically manipulated.

The scenarios are designed for a passenger-facing Level 4/Level 5 autonomous vehicle interface and focus on unexpected but safety-relevant changes in vehicle behaviour.

The scenarios are not intended to represent real-world autonomous-driving validation. They are controlled interaction scenarios for evaluating passenger understanding, trust, workload, and interaction performance.

---

2. Experimental Principle

For each scenario, the following elements should remain constant across conditions:

- Vehicle route
- Passenger role
- Environmental context
- Triggering event
- Autonomous vehicle response
- Approximate event timing
- Visual environment
- Primary passenger task
- Question structure
- Response mechanism

The manipulated element is the explanation condition.

Explanation Conditions

Condition| Description
A — No Explanation| The vehicle changes its behaviour without providing an explicit explanation.
B — Minimal Explanation| The interface provides a short description of the immediate reason for the behaviour.
C — Contextual Explanation| The interface provides the immediate reason plus relevant contextual information about what the vehicle is doing.

The exact wording should remain standardized during the experiment.

---

3. Scenario SCN-01 — Pedestrian Crossing

Scenario Objective

Evaluate passenger understanding and trust when the autonomous vehicle unexpectedly reduces speed because a pedestrian is entering a crossing area.

Initial State

- Vehicle is operating normally.
- Passenger is seated in the rear passenger area.
- Vehicle is travelling along a familiar urban route.
- No immediate safety concern is visible to the passenger.
- Vehicle maintains a normal cruising speed.

Trigger Event

A pedestrian begins entering a marked pedestrian crossing ahead of the vehicle.

Autonomous Vehicle Response

The vehicle:

1. Detects the pedestrian.
2. Reduces speed.
3. Maintains a safe stopping distance.
4. Allows the pedestrian to cross.
5. Resumes normal travel after the crossing is clear.

Passenger-Visible Behaviour

The passenger experiences an unexpected reduction in vehicle speed.

The event should be noticeable but should not be presented as an emergency.

---

Condition A — No Explanation

The vehicle slows down.

No explicit explanation is presented to the passenger.

The interface should continue displaying the relevant journey information without an explanatory message.

Expected Passenger Interpretation

The participant must infer why the vehicle slowed down.

---

Condition B — Minimal Explanation

The interface displays:

«Slowing for pedestrian.»

The vehicle performs the same manoeuvre as Condition A.

No additional contextual information is provided.

---

Condition C — Contextual Explanation

The interface displays:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

The vehicle performs the same manoeuvre as Conditions A and B.

---

Primary Evaluation Focus

- Understanding of vehicle behaviour
- Perceived transparency
- Trust in the autonomous system
- Cognitive workload
- Response time

---

4. Scenario SCN-02 — Vehicle Merging

Scenario Objective

Evaluate passenger understanding when the autonomous vehicle changes following behaviour because another vehicle is merging into the lane.

Initial State

- Vehicle is travelling normally.
- Traffic is moderate.
- Passenger is engaged in the standard passenger task.
- No immediate hazard is apparent.

Trigger Event

Another road vehicle begins merging into the autonomous vehicle's lane.

Autonomous Vehicle Response

The vehicle:

1. Detects the merging vehicle.
2. Reduces speed.
3. Increases following distance.
4. Maintains lane position.
5. Returns toward normal speed after the situation stabilizes.

---

Condition A — No Explanation

The vehicle slows and increases following distance.

No explanation is provided.

---

Condition B — Minimal Explanation

The interface displays:

«Adjusting for merging vehicle.»

---

Condition C — Contextual Explanation

The interface displays:

«Vehicle merging ahead. Increasing following distance to maintain a safe gap.»

---

Primary Evaluation Focus

- Recognition of the reason for speed adjustment
- Understanding of autonomous vehicle intent
- Trust calibration
- Workload
- Perceived transparency

---

5. Scenario SCN-03 — Obstacle Ahead

Scenario Objective

Evaluate passenger understanding when the autonomous vehicle responds to an unexpected obstacle in its path.

Initial State

- Vehicle is travelling normally.
- Passenger is engaged in the standard passenger task.
- Road conditions are otherwise stable.

Trigger Event

An unexpected object is detected in the vehicle's current path.

Autonomous Vehicle Response

The vehicle:

1. Detects the obstacle.
2. Reduces speed.
3. Adjusts its trajectory as required.
4. Passes the obstacle safely.
5. Returns to the normal route.

---

Condition A — No Explanation

The vehicle slows and changes its trajectory.

No explicit explanation is provided.

---

Condition B — Minimal Explanation

The interface displays:

«Adjusting path around obstacle.»

---

Condition C — Contextual Explanation

The interface displays:

«Obstacle detected ahead. Adjusting the path to maintain a safe clearance.»

---

Primary Evaluation Focus

- Understanding of vehicle intent
- Situation awareness
- Trust
- Workload
- Interaction performance

---

6. Scenario SCN-04 — Road Construction

Scenario Objective

Evaluate passenger understanding when temporary road conditions cause the autonomous vehicle to modify its speed and position.

Initial State

- Vehicle is travelling normally.
- Passenger is engaged in the standard passenger task.
- The road appears suitable for normal travel.

Trigger Event

The vehicle approaches a temporary road-construction area with a lane restriction.

Autonomous Vehicle Response

The vehicle:

1. Detects the changed road configuration.
2. Reduces speed.
3. Adjusts its position within the available lane.
4. Continues through the restricted area.
5. Resumes normal travel when appropriate.

---

Condition A — No Explanation

The vehicle slows and changes its road position.

No explanation is provided.

---

Condition B — Minimal Explanation

The interface displays:

«Adjusting for road construction.»

---

Condition C — Contextual Explanation

The interface displays:

«Lane restriction ahead due to road construction. Adjusting speed and position to continue safely.»

---

Primary Evaluation Focus

- Understanding of environmental context
- Perceived transparency
- Trust calibration
- Workload
- Response accuracy

---

7. Scenario Selection

The initial candidate set contains four scenarios.

ID| Scenario| Primary Vehicle Behaviour| Expected Complexity
SCN-01| Pedestrian Crossing| Speed reduction| Low–Moderate
SCN-02| Vehicle Merging| Speed/following-distance adjustment| Moderate
SCN-03| Obstacle Ahead| Speed + trajectory adjustment| Moderate–High
SCN-04| Road Construction| Speed + position adjustment| Moderate

The final experimental set should be determined after prototype validation and pilot testing.

Scenario selection should consider:

- clarity of the triggering event
- consistency of autonomous response
- ability to communicate the event through the prototype
- comparable difficulty across scenarios
- absence of unnecessary visual complexity
- ability to produce meaningful comprehension questions

---

8. Scenario Standardization Rules

The following rules apply to every experimental scenario.

Rule 1 — Same Event

The underlying event must be identical across explanation conditions.

Rule 2 — Same Vehicle Behaviour

The autonomous vehicle must perform the same action regardless of explanation condition.

Rule 3 — Explanation Is the Manipulation

No explanation condition should make the vehicle appear safer, more capable, or more successful than another condition.

Rule 4 — No Outcome Bias

The explanation should describe the vehicle's behaviour rather than explicitly stating that the outcome was successful.

Rule 5 — Standardized Timing

The event and explanation should occur at predefined points in the scenario.

Rule 6 — Standardized Wording

Once wording is finalized, it should remain unchanged during the main experiment.

Rule 7 — No Unintended Cues

Visual differences unrelated to the explanation manipulation should be minimized.

---

9. Scenario Development Status

Scenario| Draft| Prototype| Pilot| Main Study
SCN-01| Complete| Pending| Pending| Pending
SCN-02| Complete| Pending| Pending| Pending
SCN-03| Complete| Pending| Pending| Pending
SCN-04| Complete| Pending| Pending| Pending

---

10. Integrity Note

These scenarios are controlled experimental representations of autonomous-vehicle passenger interactions.

They do not constitute:

- real-world autonomous-driving validation
- vehicle safety certification
- ISO 26262 compliance evidence
- production-system validation
- evidence of actual Waymo system behaviour

The scenarios are intended solely to support controlled Human Factors/HCI research using the project prototype.
