Figma Component & State System

1. Purpose

This document defines the reusable component, variant, property, and state system for the experimental prototype of the Autonomous Vehicle Passenger Control Interface.

The objective is to establish a consistent Figma architecture before high-fidelity visual design begins.

The component system must support two requirements simultaneously:

1. Preserve the interaction language and product identity established by the original Autonomous Vehicle Passenger Control Interface PRD.
2. Allow controlled manipulation of explanation conditions for the Human Factors experiment.

The experimental prototype should therefore be treated as a structured interface system rather than a collection of independent screens.

---

2. Component Architecture

The prototype is organized into five component layers.

Prototype
│
├── Global Interface
│   ├── Header
│   ├── Navigation
│   ├── Status Indicators
│   └── Primary Actions
│
├── Journey Interface
│   ├── Journey Status
│   ├── Route Information
│   ├── Vehicle Status
│   └── Environmental Event
│
├── Explanation Interface
│   ├── Explanation Container
│   ├── Minimal Explanation
│   ├── Contextual Explanation
│   └── Explanation Iconography
│
├── Measurement Interface
│   ├── Comprehension Question
│   ├── Trust Measure
│   ├── Experience Measure
│   ├── Workload Measure
│   └── Trial Completion
│
└── Experimental Control
    ├── Scenario
    ├── Condition
    ├── Trial State
    └── Prototype Branch

---

3. Naming Convention

All Figma components should use consistent names.

Component naming

AV/
├── Global/
├── Journey/
├── Event/
├── Explanation/
├── Measurement/
├── Navigation/
└── Experimental/

Examples:

AV/Global/Header
AV/Global/StatusIndicator
AV/Journey/JourneyStatus
AV/Event/UnexpectedEvent
AV/Explanation/ExplanationCard
AV/Measurement/ComprehensionQuestion
AV/Measurement/TrustScale
AV/Measurement/WorkloadItem
AV/Experimental/ScenarioSelector

---

4. Component Properties

Components should use Figma component properties wherever practical instead of duplicated components.

Recommended properties include:

Property| Type| Values
"visibility"| Boolean| True / False
"state"| Variant| Default / Active / Completed / Disabled
"severity"| Variant| Informational / Caution / Safety
"explanation"| Variant| None / Minimal / Contextual
"modality"| Variant| Visual / Audio / Multimodal
"interaction"| Variant| Enabled / Disabled
"progress"| Variant| Not Started / Active / Complete

The prototype should avoid creating unnecessary component copies when a variant can represent the difference.

---

5. Explanation Component

The explanation component is the primary experimental manipulation.

It must support three controlled conditions.

5.1 Condition A — No Explanation

Explanation = None

The autonomous vehicle response occurs without an explanatory message.

The surrounding interface should remain otherwise unchanged.

Purpose:

Establish the baseline condition for evaluating passenger understanding, trust, and workload.

---

5.2 Condition B — Minimal Explanation

Explanation = Minimal

Example structure:

Slowing for pedestrian.

The explanation communicates the immediate reason for the vehicle behaviour without additional contextual detail.

The wording must remain concise.

---

5.3 Condition C — Contextual Explanation

Explanation = Contextual

Example structure:

Pedestrian entering the crossing ahead.
Slowing to maintain a safe distance.

The contextual explanation provides both:

1. the relevant environmental event; and
2. the resulting autonomous action.

The contextual condition must not introduce information unavailable in the corresponding scenario.

---

6. Explanation Card Structure

The explanation card should use a consistent internal hierarchy.

┌──────────────────────────────────┐
│  [Status / Event Icon]           │
│                                  │
│  WHY I'M SLOWING                 │
│                                  │
│  Pedestrian entering the         │
│  crossing ahead.                 │
│                                  │
│  Slowing to maintain a safe      │
│  distance.                       │
└──────────────────────────────────┘

The exact visual styling will be defined during the high-fidelity phase.

At low fidelity, the hierarchy is more important than decoration.

---

7. Explanation Rules

The explanation system must follow these rules:

Rule 1 — Same event

The environmental event must remain identical across explanation conditions.

Rule 2 — Same autonomous response

The vehicle behaviour must remain identical across conditions.

Rule 3 — Explanation is the manipulated variable

The primary difference between conditions should be the explanation itself.

Rule 4 — No additional evidence

The explanation must not provide information that is unavailable to the passenger in the corresponding scenario.

Rule 5 — No outcome exaggeration

The interface must not claim that the system is safer, more accurate, or more reliable than the experimental scenario establishes.

Rule 6 — No persuasive language

The explanation should describe system behaviour rather than attempt to persuade the passenger to trust the vehicle.

---

8. Event Component

The Event component represents the environmental event that triggers an autonomous response.

Required properties:

eventType
severity
visibility
duration

Candidate event types:

Pedestrian
Merging Vehicle
Obstacle
Road Construction

Example:

AV/Event/UnexpectedEvent
eventType = Pedestrian
severity = Caution

---

9. Autonomous Response Component

The Autonomous Response component represents the vehicle's observable response.

Examples:

Slowing
Increasing following distance
Changing trajectory
Adjusting position

The response must be standardized for a given scenario.

For experimental validity, changing the explanation condition must not change the underlying autonomous response.

---

10. Journey Status Component

The Journey Status component communicates the current state of the autonomous journey.

Recommended states:

Normal
Approaching Event
Responding
Explanation Active
Awaiting Passenger Observation
Completed

The component should communicate state clearly without introducing unnecessary visual complexity.

---

11. Primary Action Component

Primary actions should use a consistent component.

Examples:

Continue
Submit
Next
Confirm
Finish

Button states:

Default
Pressed
Disabled
Completed

The prototype should prevent accidental submission wherever possible.

---

12. Measurement Components

Measurement components should be visually separated from the vehicle interface.

This distinction is important because measurement screens are part of the research protocol rather than the passenger's normal vehicle interface.

Required components:

AV/Measurement/ComprehensionQuestion
AV/Measurement/TrustScale
AV/Measurement/WorkloadItem
AV/Measurement/TrialComplete

---

13. Comprehension Question Component

Structure:

Question
↓
Response options
↓
Submit

Example:

Why did the vehicle slow down?

○ A pedestrian entered the crossing
○ The destination changed
○ The vehicle encountered a system failure
○ The passenger requested a stop

Questions must correspond directly to the scenario.

Correct answers must be defined in the experiment data dictionary rather than inferred from the interface.

---

14. Trust Measurement Component

The trust measurement interface should use a consistent response scale across trials.

The exact scale and wording will be finalized during experimental validation.

Required states:

Unselected
Selected
Submitted

The interface should not visually indicate which response represents "correct" or "preferred" trust.

The experiment measures trust and trust calibration rather than attempting to maximize trust.

---

15. Workload Component

The workload component should support the selected workload measurement procedure.

For the current methodology, NASA-TLX is the primary candidate.

The interface must not visually bias participants toward a particular response.

Any implementation of NASA-TLX must follow the finalized measurement protocol.

---

16. Accessibility

All reusable components should support:

- sufficient text size;
- clear hierarchy;
- readable contrast;
- non-color-dependent status communication;
- clear focus/selection states;
- sufficiently large interactive targets;
- consistent terminology;
- readable line lengths;
- predictable interaction order.

Accessibility decisions should be documented rather than treated only as visual styling.

---

17. Component Independence

Each reusable component should have one clear responsibility.

For example:

ExplanationCard

should communicate an explanation.

It should not simultaneously contain:

- experiment scoring;
- participant identification;
- trust measurement;
- workload measurement;
- unrelated navigation.

This separation makes the prototype easier to validate and reduces accidental experimental coupling.

---

18. Experimental Isolation

The three explanation conditions must be isolated through component variants.

ExplanationCard
│
├── None
├── Minimal
└── Contextual

The experiment should not require manually rebuilding the interface for every condition.

Changing the condition should be sufficient to change the explanation presentation.

---

19. Version Control

Major component changes should be recorded in:

docs/decisions-log.md

Each decision should include:

Date
Decision
Reason
Alternative considered
Impact on experiment

This creates an auditable design history.

---

20. Completion Criteria

The component system is complete when:

- [ ] global components are defined;
- [ ] journey components are defined;
- [ ] event components are defined;
- [ ] autonomous response components are defined;
- [ ] explanation variants are defined;
- [ ] measurement components are defined;
- [ ] component naming is consistent;
- [ ] variant/property logic is documented;
- [ ] explanation conditions can be changed without rebuilding screens;
- [ ] accessibility requirements are represented;
- [ ] experimental measurement components are separated from vehicle UI;
- [ ] component decisions are documented.

---

21. Design Principle

The Figma file should behave like a system.

The objective is not to create three attractive versions of the same screen.

The objective is to create one controlled interface system capable of producing experimentally distinct conditions while keeping all non-manipulated elements stable.
