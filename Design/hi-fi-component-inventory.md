High-Fidelity Component Inventory

Purpose

This document defines the initial reusable component inventory for the high-fidelity autonomous-vehicle passenger interface.

The component system is intended to reduce inconsistency, accelerate iteration, and preserve experimental control.

---

1. Component Architecture

Design System
│
├── Foundations
│   ├── Typography
│   ├── Spacing
│   ├── Colour
│   ├── Iconography
│   └── Elevation
│
├── Navigation
│   ├── Journey Status
│   ├── Destination
│   └── System Status
│
├── Vehicle State
│   ├── Autonomy Status
│   ├── Current Action
│   └── Safety State
│
├── Explanation
│   ├── None
│   ├── Minimal
│   └── Contextual
│
├── Controls
│   ├── Primary
│   ├── Secondary
│   ├── Emergency
│   └── Confirmation
│
└── Measurement
    ├── Comprehension
    ├── Trust
    ├── Workload
    └── Completion

---

2. Foundation Components

Typography

Required categories:

- Display;
- Heading;
- Section Heading;
- Body;
- Secondary;
- Caption;
- Control Label;
- Status.

Spacing

Use a consistent spacing scale across all components.

Colour

Use semantic tokens rather than screen-specific colour choices.

---

3. Navigation Components

Journey Status

Purpose:

Communicate current journey state and orientation.

Possible information:

- destination;
- journey progress;
- estimated arrival;
- current journey state.

---

System Status

Purpose:

Communicate the current autonomous-system state.

Examples:

- Autonomous;
- Attention;
- Degraded;
- Emergency.

---

4. Vehicle-State Components

Current Action

Communicates what the vehicle is currently doing.

Examples:

- Slowing;
- Maintaining distance;
- Changing position;
- Adjusting route.

---

Autonomy Status

Communicates whether autonomous operation is active.

The status should not require the passenger to infer autonomy from the map alone.

---

Safety State

Communicates the current safety-relevant state when required.

---

5. Explanation Components

Explanation / None

No explanatory message is displayed.

The surrounding interface remains structurally comparable to the other conditions.

Explanation / Minimal

Provides a concise immediate reason.

Explanation / Contextual

Provides additional contextual information.

The three variants must remain visually comparable.

---

6. Control Components

Primary Button

Used for the main available passenger action.

Secondary Button

Used for supporting actions.

Emergency Control

Provides access to the appropriate emergency interaction.

Confirmation

Used when an action requires explicit confirmation.

Controls should clearly communicate:

- action;
- current state;
- availability;
- consequence where necessary.

---

7. Measurement Components

Comprehension Response

Used after the explanation/observation stage to assess passenger understanding.

Trust Response

Used to collect the participant's trust-related response.

Workload Response

Used to collect cognitive-workload information according to the selected measurement protocol.

Trial Completion

Confirms that the current trial has ended.

---

8. Component Variant Rules

Variants should be created only when the underlying component remains conceptually the same.

Example:

Explanation
├── None
├── Minimal
└── Contextual

Not:

Red Explanation
Blue Explanation
Large Explanation
Decorative Explanation
Experimental Explanation

unless these represent legitimate documented component states.

---

9. Component Documentation

Each reusable component should document:

- purpose;
- anatomy;
- variants;
- properties;
- states;
- interaction;
- accessibility considerations;
- experimental relevance.

---

10. Experimental Components

The following components require additional review because they directly affect experimental conditions:

- explanation;
- event notification;
- autonomous-response communication;
- comprehension interface;
- trust measurement;
- workload measurement.

These components should not be modified casually after experimental freeze.

---

11. Definition of Done

- [ ] Core foundation components identified.
- [ ] Navigation components identified.
- [ ] Vehicle-state components identified.
- [ ] Explanation variants identified.
- [ ] Control components identified.
- [ ] Measurement components identified.
- [ ] Experimental components flagged.
- [ ] Naming convention applied.
- [ ] Component documentation structure established.

---

Next Step

Implement the foundation and first reusable components in Figma before constructing the complete high-fidelity screens.
