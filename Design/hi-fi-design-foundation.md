High-Fidelity Design Foundation

Purpose

This document establishes the visual and interaction foundation for the high-fidelity experimental prototype.

The objective is to translate the existing Autonomous Vehicle Passenger Control Interface product direction into a coherent high-fidelity Human Factors interface while preserving the experimental architecture frozen in Day 20.

High-fidelity design begins with the system, not individual screens.

---

1. Design Foundation Principles

The high-fidelity interface will follow these principles:

1.1 Calm by Default

Normal autonomous travel should feel stable, predictable, and visually calm.

The interface should not continuously communicate urgency when no passenger action is required.

1.2 Present in Crisis

When an unexpected or safety-relevant event occurs, the interface should increase the salience of relevant information without creating unnecessary alarm.

1.3 Explain the Why

When the autonomous system performs an unexpected action, the passenger should be able to understand the relevant reason when an explanation is provided.

1.4 One Tap to Safety

Safety-relevant controls should remain discoverable and require minimal interaction when appropriate.

1.5 Information Before Decoration

Visual elements should support comprehension, orientation, or interaction.

Decorative elements must not compete with safety-relevant information.

1.6 Consistency

The same semantic information should be represented consistently across the interface.

---

2. Design Hierarchy

The high-fidelity interface should prioritize information according to passenger relevance:

Level 1 — Immediate safety state
Level 2 — Autonomous vehicle action
Level 3 — Explanation / reason
Level 4 — Journey context
Level 5 — Passenger controls
Level 6 — Secondary information

This hierarchy may change according to system state.

---

3. Core Interface Regions

The primary passenger interface is organized into functional regions.

┌──────────────────────────────────────────────┐
│ SYSTEM / JOURNEY STATUS                      │
├──────────────────────────────────────────────┤
│                                              │
│                                              │
│              JOURNEY VIEW                    │
│                                              │
│                                              │
├──────────────────────────────────────────────┤
│ VEHICLE ACTION / EXPLANATION                 │
├──────────────────────────────────────────────┤
│ PRIMARY PASSENGER CONTROLS                   │
└──────────────────────────────────────────────┘

The exact visual proportions will be refined during Figma implementation.

---

4. Semantic States

The interface must distinguish between:

Normal

The vehicle is operating normally and no unexpected event requires passenger attention.

Attention

A relevant event has occurred or the vehicle has changed behaviour.

Safety-Relevant

The interface must prioritize information required to understand or respond to a safety-relevant situation.

Degraded

The autonomous system is operating under a constrained or degraded condition.

Emergency

The passenger requires access to safety or emergency interaction.

---

5. Typography

Typography should support:

- rapid recognition;
- readability;
- clear hierarchy;
- short-distance viewing;
- accessibility;
- predictable scanning.

The typography system should define:

Display
Heading
Section Heading
Body
Secondary
Caption
Control Label
Status

Exact font sizes should be established as design tokens in Figma rather than independently selected on each screen.

---

6. Spacing

A consistent spacing scale should be used across the interface.

Spacing should support:

- grouping;
- separation;
- hierarchy;
- touch interaction;
- visual scanning.

Components should not use arbitrary spacing values unless there is a documented reason.

---

7. Iconography

Icons should:

- communicate a recognizable concept;
- support text rather than replace necessary text;
- remain visually consistent;
- avoid ambiguous symbolism;
- maintain sufficient size and contrast.

Safety-relevant meaning should not depend exclusively on an icon.

---

8. Colour Semantics

Colour should communicate semantic states rather than decoration.

The system should distinguish concepts such as:

Neutral
Informational
Attention
Warning
Critical
Success / Confirmed
Disabled

Colour must not be the sole mechanism for communicating state.

Each meaningful state should also have another representation, such as:

- text;
- icon;
- position;
- shape;
- status label.

---

9. Component Strategy

The interface should be built from reusable components.

Initial component groups:

Navigation

- journey status;
- destination;
- route status;
- system status.

Vehicle State

- current action;
- speed/status;
- autonomy state;
- safety state.

Explanation

- explanation container;
- explanation title;
- reason;
- contextual detail;
- explanation icon.

Interaction

- primary button;
- secondary button;
- emergency control;
- confirmation control;
- navigation control.

Measurement

- comprehension response;
- trust response;
- workload response;
- completion state.

---

10. Explanation Component Rules

The explanation component is experimentally sensitive.

The component must support:

Variant A — None
Variant B — Minimal
Variant C — Contextual

The visual shell should remain as consistent as possible.

The primary difference between variants should be the amount and specificity of explanatory information.

The component must not introduce unrelated visual changes that could become experimental confounds.

---

11. Unexpected Event Visual Language

Unexpected events should create a clear transition from normal operation.

The passenger should be able to recognize:

Something changed
        ↓
The vehicle responded
        ↓
The system can explain the response
        ↓
Passenger action is / is not required

The design should avoid excessive:

- flashing;
- animation;
- warning sounds;
- colour saturation;
- decorative motion.

---

12. Accessibility Foundation

The high-fidelity system should support:

- readable text;
- sufficient contrast;
- clear focus/selection states;
- adequate touch targets;
- non-colour-only communication;
- consistent component placement;
- concise language;
- predictable interaction.

Accessibility requirements should be validated during implementation rather than deferred to the end.

---

13. Experimental Integrity

High-fidelity visual design must not unintentionally change:

- scenario timing;
- vehicle response;
- explanation condition;
- information level;
- measurement sequence;
- participant task;
- condition assignment.

Any change affecting these elements must be documented and reviewed.

---

14. Figma Foundation

The Figma file should establish the following structure:

00 — Cover / Documentation
01 — Foundations
02 — Components
03 — Vehicle States
04 — Journey
05 — Explanation Conditions
06 — Experimental Screens
07 — Measurement
08 — Prototype
09 — Accessibility
10 — Archive

This structure keeps design-system work separate from experimental screens.

---

15. Naming Convention

Components:

Component / Name / Variant

Examples:

Button / Primary / Default
Button / Primary / Disabled
Explanation / Minimal
Explanation / Contextual
Vehicle State / Slowing

Frames:

EXP-00_Start
EXP-01_Practice
EXP-02_Normal
EXP-03_EventApproach
EXP-04_UnexpectedEvent
EXP-05_Response
EXP-05A_NoExplanation
EXP-05B_Minimal
EXP-05C_Contextual
EXP-06_Comprehension
EXP-07_Trust
EXP-08_Workload
EXP-09_Complete

---

16. Definition of Done

The design foundation is complete when:

- [ ] Visual hierarchy is defined.
- [ ] Semantic states are defined.
- [ ] Typography categories are defined.
- [ ] Spacing strategy is defined.
- [ ] Colour semantics are defined.
- [ ] Iconography rules are defined.
- [ ] Core components are identified.
- [ ] Explanation component strategy is defined.
- [ ] Accessibility principles are incorporated.
- [ ] Experimental integrity constraints are documented.
- [ ] Figma page structure is established.
- [ ] Naming conventions are established.

---

17. Next Step

The next step is to implement the design foundations in Figma and create the first reusable high-fidelity components.

The first visual implementation should focus on the foundation and core journey components rather than completing every screen simultaneously.
