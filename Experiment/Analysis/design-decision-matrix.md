Day 34 — Evidence-to-Design Decision Matrix

Project: Autonomous Vehicle Passenger Control Interface
Research Theme: Explainable autonomous behaviour
Version: EV-1.0
Purpose: Translate Human Factors evidence into concrete interface decisions

---

1. Overview

This document establishes the traceability between the research problem, Human Factors constructs, experimental variables, and interface decisions.

The purpose is to ensure that the final design is not presented as a collection of aesthetic choices.

Every major interaction should be traceable to a passenger need, Human Factors consideration, or research variable.

---

2. Traceability Matrix

Human Factors problem| Research construct| Design response| Interface component
Passenger does not know why the vehicle slowed| Understanding| Explain relevant cause| Explanation card
Passenger cannot distinguish appropriate behaviour from unexpected behaviour| Transparency| Communicate system intent| Explanation card
Excessive information may increase cognitive demand| Workload| Limit explanation to relevant information| Progressive explanation
Passenger may distrust unexplained behaviour| Trust| Provide timely causal information| Contextual explanation
Passenger may over-trust a system| Trust calibration| Avoid exaggerated reassurance| Factual explanation tone
Passenger may miss visual information| Accessibility| Provide equivalent modalities| Visual + voice/caption support
Passenger may be occupied with another task| Attention| Use glanceable hierarchy| Short headline + optional detail
Passenger needs help during abnormal conditions| Safety / usability| Provide obvious escalation path| Protected safety control
Passenger may experience unexpected route changes| Situation awareness| Explain route change and impact| Route explanation
Passenger may want deeper information| Transparency| Allow progressive disclosure| Diagnostics / explanation detail

---

3. Explanation Card Decision Logic

An explanation card should appear when all of the following are satisfied:

EVENT DETECTED
     │
     ▼
Could the behaviour reasonably surprise the passenger?
     │
   YES
     │
     ▼
Is the event relevant to passenger understanding,
comfort, safety, or journey expectations?
     │
   YES
     │
     ▼
Can the system provide a meaningful explanation?
     │
   YES
     │
     ▼
SHOW CONCISE EXPLANATION

The system should not expose an explanation merely because an internal system state changed.

The passenger-facing trigger should be based on interaction relevance.

---

4. Explanation Content Hierarchy

Every explanation should be constructed using the following priority order.

Priority 1 — Event

What happened?

«Pedestrian entering the crossing ahead.»

Priority 2 — Vehicle response

What is the vehicle doing?

«Slowing to maintain a safe distance.»

Priority 3 — Passenger impact

Does the event affect the passenger's journey?

«Arrival unaffected.»

Priority 4 — Additional context

Only when useful:

«Crossing is temporarily occupied.»

This creates a progressive information hierarchy.

---

5. Explanation Template

[EVENT]
[VEHICLE RESPONSE]
[PASSENGER IMPACT — IF RELEVANT]

Example:

«Emergency vehicle approaching
Pulling to the right.
Arrival unaffected.»

This structure follows the original PRD's explanation model of:

what the car noticed → what it is doing → impact on the passenger.

---

6. Trust Design Rules

Rule 1

Never use explanation language that implies certainty beyond the system's actual knowledge.

Rule 2

Do not use reassurance as a substitute for information.

Weak:

«Don't worry — everything is fine.»

Stronger:

«Construction ahead. Slowing and moving to the adjacent lane.»

Rule 3

Do not equate trust with compliance.

The passenger should remain informed and able to request support.

Rule 4

Explain changes that affect passenger expectations.

Examples:

- ETA change;
- route change;
- prolonged stop;
- degraded capability;
- unexpected manoeuvre.

---

7. Cognitive Workload Rules

The interface follows five workload-reduction principles.

7.1 One primary message

The explanation card should have one dominant message.

7.2 Short headline

The headline should communicate the core event immediately.

7.3 Progressive disclosure

Additional information should be available without appearing automatically.

7.4 Stable visual hierarchy

Explanation cards should maintain consistent placement and structure.

7.5 Avoid simultaneous competing alerts

The passenger should not be forced to choose between multiple equally prominent messages unless the situation genuinely requires it.

---

8. Attention Management

The original product is designed around the principle of a calm dashboard that keeps important information visible while placing secondary information one tap away.

The explanation system follows the same principle:

IMPORTANT NOW
     ↓
VISIBLE
     ↓
RELEVANT
     ↓
BRIEF
     ↓
OPTIONAL DETAIL

This prevents the HMI from becoming a continuously active information display.

---

9. Accessibility Decision Matrix

Requirement| Design response
Low vision| Large text + high contrast
Hearing limitation| Visual equivalent for audio alerts
Screen-reader use| Semantic labels and logical focus
Cognitive accessibility| Simplified language and reduced information density
Motor limitation| Large touch targets + voice alternatives
Temporary distraction| Audio/visual redundancy where appropriate
Multilingual use| Language-switchable UI and voice
Glare/vibration| Large type and generous spacing

The original PRD specifies a minimum in-cabin touch target of 64 × 64 px and supports scalable typography up to 200%.

---

10. Safety Interface Relationship

The explanation system must never compete with the primary safety pathway.

The original PRD explicitly defines a persistent, protected safety button and states that the emergency interface should be reachable from anywhere.

Therefore:

SAFETY CONTROL
      >
EXPLANATION
      >
SECONDARY INFORMATION

An explanation can inform the passenger, but it must never obscure a safety-critical action.

---

11. Degraded-State Behaviour

When system capabilities degrade, the interface should communicate the limitation honestly.

The PRD defines offline behaviour in which safety controls and explanation cards remain available locally while cloud-dependent features may become degraded or unavailable.

The design implication is:

«Do not silently remove functionality. Explain capability changes when they affect the passenger.»

Example:

«Connection limited
Safety controls remain available. Live support is reconnecting.»

This communicates both limitation and retained capability.

---

12. Final Design Principles

The project consolidates its Human Factors design principles into ten rules.

1. Explain meaningful surprises.
2. Lead with the passenger-relevant cause.
3. State the vehicle's intended response.
4. Add passenger impact only when useful.
5. Prefer human-readable explanations over raw telemetry.
6. Use progressive disclosure for deeper information.
7. Design for calibrated trust rather than maximum trust.
8. Minimise unnecessary cognitive workload.
9. Provide equivalent accessible modalities.
10. Never allow explanatory UI to interfere with safety controls.

---

13. Research-to-Design Traceability

The final design can therefore be summarised as:

RESEARCH QUESTION
       ↓
EXPLANATION PRESENTATION
       ↓
PASSENGER UNDERSTANDING
       ↓
TRUST + WORKLOAD
       ↓
DESIGN REQUIREMENTS
       ↓
EXPLANATION CARD
       ↓
PROTOTYPE BEHAVIOUR

This traceability is a central strength of the project.

The interface is not merely “designed around trust.”

It operationalises trust and understanding as explicit Human Factors constructs.

---

14. Final Decision

The project adopts contextual, concise, event-driven explanation cards as the primary passenger-facing XAI mechanism.

The preferred explanation architecture is:

«What happened → What the vehicle is doing → What it means for the passenger»

with progressive disclosure for deeper information.

This decision is consistent with the original product requirements and the project's Human Factors research framework.

---

15. Completion Statement

The evidence-to-design traceability layer is complete.

All major explanation-related design decisions can now be traced to:

- the original PRD;
- the research question;
- Human Factors constructs;
- measurable outcomes;
- accessibility requirements;
- safety hierarchy;
- and the experimental architecture.

No unsupported empirical superiority claim is made.
