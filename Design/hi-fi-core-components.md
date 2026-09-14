High-Fidelity Core Components

1. Purpose

This document defines the reusable high-fidelity components required to implement the experimental prototype.

The components are derived from the frozen experimental architecture and the established design foundation.

The goal is to create a consistent component system that can be reused across scenarios and explanation conditions.

---

2. Component Architecture

The component system is divided into five groups:

1. Foundations
2. Journey and vehicle state
3. Explanation
4. Passenger interaction
5. Experimental measurement

Foundations
    ↓
Journey / Vehicle Components
    ↓
Explanation Components
    ↓
Passenger Interaction
    ↓
Measurement Components

---

3. Foundation Components

3.1 Application Shell

Purpose:

Provide the persistent structure surrounding the experimental interface.

Contains:

- primary content region
- status region
- navigation/context region
- interaction region

Properties:

Theme: Light / Dark
State: Normal / Attention / Safety / Degraded / Emergency

---

3.2 Surface

Purpose:

Provide reusable containers for grouped information.

Properties:

Type: Primary / Secondary / Elevated
State: Default / Attention / Safety / Degraded / Emergency

---

3.3 Button

Purpose:

Provide consistent passenger actions.

Variants:

Primary
Secondary
Tertiary
Destructive
Disabled

Properties:

Size
Icon
Label
State

Buttons must have clear action labels.

---

4. Journey Components

4.1 Journey Status

Purpose:

Communicate the current journey state.

Content may include:

- destination
- journey progress
- current operational status
- relevant journey information

States:

Normal
Attention
Safety-Relevant
Degraded
Emergency

---

4.2 Route Progress

Purpose:

Provide a simplified representation of journey progress.

The component should remain secondary to safety-relevant information.

It should not visually compete with explanation or emergency information.

---

4.3 Vehicle Status

Purpose:

Communicate the current autonomous operating state.

Example semantic states:

Driving normally
Adjusting speed
Adjusting trajectory
System degraded
Assistance required

The exact state displayed must correspond to the scenario state.

---

5. Event Components

5.1 Unexpected Event Indicator

Purpose:

Represent the environmental event that triggered an autonomous response.

Structure:

[Event Icon]
Event Description

Examples of event categories:

- pedestrian crossing
- merging vehicle
- obstacle
- road construction

The event description must remain consistent across explanation conditions.

---

5.2 Autonomous Response

Purpose:

Show what the autonomous system is doing.

Structure:

System response
↓
Vehicle action

Example:

Vehicle response
Slowing down

The response must remain identical across the experimental explanation conditions for the same scenario.

---

6. Explanation Components

6.1 Explanation Container

Base component:

Component / Explanation

Variants:

No Explanation
Minimal
Contextual

Properties:

Condition
Scenario
Theme
State

---

7. No-Explanation Variant

Component name:

Explanation / None

Purpose:

Represent the control condition.

The component must not provide an explanatory reason.

It may preserve the surrounding information architecture required to show the autonomous response.

The control condition must not accidentally communicate the manipulated explanatory information through:

- icons
- secondary labels
- helper text
- animations
- route information
- unrelated messages

---

8. Minimal Explanation Variant

Component name:

Explanation / Minimal

Purpose:

Provide a concise explanation of the autonomous response.

Structure:

Why?
[Concise reason]

Example:

Why?
Slowing for pedestrian.

The wording should be concise and directly related to the observed autonomous response.

---

9. Contextual Explanation Variant

Component name:

Explanation / Contextual

Purpose:

Provide a more detailed contextual explanation.

Structure:

Why?
[Environmental context]
[Autonomous response rationale]

Example:

Why?
Pedestrian entering the crossing ahead.
Slowing to maintain a safe distance.

The contextual condition should provide additional information without introducing unrelated content.

---

10. Explanation Component Integrity

The three variants must be controlled carefully.

Property| No Explanation| Minimal| Contextual
Scenario| Same| Same| Same
Vehicle response| Same| Same| Same
Event| Same| Same| Same
Position| Equivalent| Equivalent| Equivalent
Theme| Same| Same| Same
Interaction| Equivalent| Equivalent| Equivalent
Explanation information| None| Concise| Contextual

The explanation condition is the experimental manipulation.

---

11. Safety Components

11.1 Emergency Action

Purpose:

Provide a clearly recognizable safety action.

Requirements:

- high visibility
- clear label
- predictable placement
- sufficient interaction size
- non-colour-dependent recognition

The emergency action must not be confused with normal journey controls.

---

11.2 Assistance Action

Purpose:

Provide a passenger-support pathway where appropriate.

Possible functions include:

- request assistance
- contact support
- access safety information

The exact functionality should follow the existing PRD rather than being invented during experimental implementation.

---

12. Measurement Components

12.1 Comprehension Question

Purpose:

Measure passenger understanding following a trial.

Structure:

Question
[Response option]
[Response option]
[Response option]
[Response option]

Design principles:

- one clear question
- minimal unnecessary text
- consistent response format
- no visual cue that identifies the correct answer

---

12.2 Trust Measure

Purpose:

Capture the participant's evaluation of the autonomous system following the scenario.

The final questionnaire wording should be based on the selected validated measurement approach.

Do not modify validated scales casually.

---

12.3 Workload Measure

Purpose:

Capture perceived workload after the relevant trial or experimental sequence.

The implementation should follow the selected NASA-TLX procedure or other approved workload measurement protocol.

Do not present the workload screen as a design preference survey.

It is a research measurement interface.

---

13. Feedback and Error States

Components should support:

Default
Selected
Incorrect
Incomplete
Disabled

Error feedback must not reveal experimental answers before the relevant measurement is complete.

If correctness feedback is unnecessary for the experimental task, it should not be displayed.

---

14. Accessibility Properties

Reusable components should support:

- sufficient contrast
- readable text
- clear focus states
- non-colour state communication
- predictable interaction
- adequate touch targets
- clear labels
- consistent icon use

Accessibility properties should be implemented at the component level wherever possible.

---

15. Component Properties

The following properties should be exposed as Figma component variables or variants where practical.

Theme
State
Condition
Scenario
Enabled
Selected
Icon
Content density

Avoid creating unnecessary variants.

A variant should exist only when it represents a meaningful reusable state.

---

16. Figma Component Naming

Use:

COMP / Shell
COMP / Surface
COMP / Button
COMP / Journey Status
COMP / Route Progress
COMP / Vehicle Status
COMP / Event
COMP / Autonomous Response
COMP / Explanation
COMP / Emergency Action
COMP / Assistance Action
COMP / Comprehension
COMP / Trust
COMP / Workload

Explanation variants:

COMP / Explanation / None
COMP / Explanation / Minimal
COMP / Explanation / Contextual

---

17. Component Construction Order

Build components in this order:

Phase 1 — Foundations

- Shell
- Surface
- Typography
- Buttons

Phase 2 — Journey

- Journey Status
- Route Progress
- Vehicle Status

Phase 3 — Event

- Event Indicator
- Autonomous Response

Phase 4 — Explanation

- Explanation / None
- Explanation / Minimal
- Explanation / Contextual

Phase 5 — Safety

- Emergency Action
- Assistance Action

Phase 6 — Measurement

- Comprehension
- Trust
- Workload

---

18. Component Validation

Each component should be checked for:

- [ ] correct naming
- [ ] correct variants
- [ ] correct semantic state
- [ ] consistent typography
- [ ] consistent spacing
- [ ] accessibility
- [ ] interaction clarity
- [ ] reusable structure
- [ ] experimental integrity

---

19. Experimental Integrity Check

Before placing a component into the prototype, verify:

«Does this component introduce information that could change the participant's interpretation of the experimental condition?»

If yes, the component must be reviewed before implementation.

Examples of potential unintended manipulation:

- an icon that reveals the reason in the no-explanation condition;
- different colours that make one explanation condition appear more trustworthy;
- different animation intensity between conditions;
- additional contextual information outside the explanation component;
- different response wording between conditions.

---

20. Definition of Done

The component system is complete when:

1. Core components are implemented.
2. Components use the established foundations.
3. Explanation conditions are represented as controlled variants.
4. Journey and vehicle-state components are reusable.
5. Measurement components have consistent structures.
6. Accessibility is considered at component level.
7. Component naming is consistent.
8. Components can be reused across all experimental scenarios.
9. No component introduces uncontrolled experimental information.

The next phase is assembling these components into the high-fidelity experimental screens.
