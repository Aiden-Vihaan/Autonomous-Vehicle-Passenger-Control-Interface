Autonomous Vehicle Passenger Control Interface

Human Factors Research & HCI Design Project

«Designing Passenger-Facing Explanations for Autonomous Vehicle Behaviour»

---

Overview

This project investigates how passenger-facing explanations can help people understand unexpected autonomous-vehicle behaviour without introducing unnecessary cognitive demand.

The project began as an industry-style Product Requirements Document for an in-cabin passenger interface and was subsequently developed into a Human Factors and HCI research project.

The central design problem is simple:

«When a driverless vehicle unexpectedly slows, pauses, changes lanes or modifies its route, how should the interface communicate what is happening?»

The project focuses on the relationship between:

- passenger comprehension
- calibrated trust
- cognitive workload
- perceived understanding
- interaction performance
- accessibility
- safety hierarchy

---

Research Question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

Secondary questions

1. Does explanation presence affect objective comprehension?
2. Does explanation specificity affect comprehension and trust?
3. How does explanation presentation relate to cognitive workload?
4. How closely does perceived understanding correspond with objective comprehension?
5. What Human Factors principles can guide passenger-facing XAI design?

---

Experimental Conditions

Condition| Explanation
A| No explanation
B| Minimal explanation
C| Contextual explanation

Example

A — No explanation

«Vehicle slows.»

B — Minimal

«Slowing for pedestrian.»

C — Contextual

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

The examples illustrate the experimental manipulation and are not empirical findings.

---

Primary Outcome

Objective comprehension

The primary outcome evaluates whether passengers correctly understand the reason for the vehicle's unexpected behaviour.

---

Secondary Outcomes

- response time
- trust
- cognitive workload
- perceived understanding
- task success
- interaction errors

---

Theoretical Foundation

The project integrates:

Trust in Automation

Understanding the relationship between passenger confidence and perceived system behaviour.

Situation Awareness

Understanding how passengers perceive, comprehend and anticipate automated behaviour.

Cognitive Workload

Evaluating the cognitive cost of explanation processing.

Explainable AI

Designing understandable representations of automated system behaviour.

Human-Automation Interaction

Treating the interface as a communication layer between passenger and autonomous system.

---

Product Foundation

The underlying product is an in-cabin passenger interface for autonomous vehicles.

The original PRD specifies:

- Journey Dashboard
- route visualization
- vehicle diagnostics
- emergency controls
- accessibility
- entertainment/work surfaces
- passenger profiles
- contextual explanation cards
- degraded and offline states

The Journey Dashboard is the central ride surface, with contextual explanations appearing when unusual vehicle behaviour occurs.

The original product architecture also maintains a persistent safety control independent of ordinary interface navigation.

---

Explanation Architecture

The original product requirement defines an explanation as:

What the vehicle noticed
          ↓
What the vehicle is doing
          ↓
Impact on the passenger

The research framework extends this into:

EVENT
  ↓
CAUSE
  ↓
ACTION
  ↓
PASSENGER IMPACT
  ↓
OPTIONAL DEEPER INFORMATION

This creates a structured explanation architecture that can be evaluated experimentally.

---

Research-to-Design Traceability

Product requirement| Human Factors question| Design response| Evaluation
Explain unexpected behaviour| What does the passenger need to understand?| Explanation card| Comprehension
Maintain trust| Does explanation influence confidence?| Contextual rationale| Trust
Avoid overload| Does additional detail increase demand?| Controlled information density| Workload
Safety always accessible| Does explanation compete with critical controls?| Persistent safety hierarchy| Interaction/error analysis
Accessibility| Can different passengers access the same explanation?| Multimodal/accessibility architecture| Accessibility evaluation
Calm communication| Does wording support interpretation?| Factual, concise language| Qualitative analysis

---

Repository Architecture

Autonomous-Vehicle-Passenger-Control-Interface/
│
├── README.md
│
├── PRD/
│   ├── original-prd.docx
│   └── refined-prd.docx
│
├── research/
│   ├── PROJECT_CHARTER.md
│   ├── literature-review.md
│   ├── research-questions.md
│   ├── hypotheses.md
│   ├── theoretical-framework.md
│   ├── methodology.md
│   ├── ethics.md
│   └── research-log.md
│
├── design/
│   ├── requirements.md
│   ├── user-flows.md
│   ├── information-architecture.md
│   ├── design-system.md
│   ├── accessibility.md
│   └── xai-framework.md
│
├── prototype/
│   ├── README.md
│   ├── screenshots/
│   └── source/
│
├── experiment/
│   ├── scenarios/
│   ├── protocol/
│   ├── participant-materials/
│   └── questionnaires/
│
├── analysis/
│   ├── data/
│   ├── analysis-notebook/
│   ├── figures/
│   ├── DAY-41-EMPIRICAL-DATA-PROCESSING.md
│   ├── DAY-41-EMPIRICAL-RESULTS-TEMPLATE.md
│   ├── findings-synthesis.md
│   ├── rq-hypothesis-mapping.md
│   └── evidence-to-design.md
│
├── paper/
│   ├── research-paper.pdf
│   └── manuscript.md
│
└── docs/
    ├── decisions-log.md
    ├── changelog.md
    ├── research-traceability.md
    └── reproducibility.md

---

Research Pipeline

PRODUCT REQUIREMENT
        ↓
PROBLEM DEFINITION
        ↓
LITERATURE REVIEW
        ↓
THEORETICAL FRAMEWORK
        ↓
RESEARCH QUESTIONS
        ↓
HYPOTHESES
        ↓
OPERATIONALISATION
        ↓
EXPERIMENTAL DESIGN
        ↓
PROTOTYPE
        ↓
PILOT / VALIDATION
        ↓
DATA COLLECTION
        ↓
DATA QUALITY
        ↓
STATISTICAL ANALYSIS
        ↓
HUMAN FACTORS INTERPRETATION
        ↓
DESIGN IMPLICATIONS
        ↓
RESEARCH CONTRIBUTION
        ↓
FINAL PAPER
        ↓
PORTFOLIO PRESENTATION

---

Evidence Integrity

This repository follows five rules.

1. No fabricated observations

Participant observations must originate from actual data.

2. No invented statistical results

Means, p-values, effect sizes, confidence intervals and correlations must be generated from the underlying dataset.

3. No retrospective hypothesis manipulation

The prespecified research questions and hypotheses remain identifiable even if results do not support them.

4. No unsupported safety claims

The project does not claim that the interface makes an autonomous vehicle safer or guarantees passenger safety.

5. No conflation of design targets and empirical findings

Product KPIs from the original PRD are treated as product targets, not as achieved study outcomes. The PRD itself specifies these as targets to validate through usability testing.

---

Reproducibility

The analytical chain is:

Raw observations
      ↓
Data validation
      ↓
Cleaning
      ↓
Analysis dataset
      ↓
Statistical analysis
      ↓
Figures / tables
      ↓
Interpretation
      ↓
Research paper

Raw observations should remain immutable.

Any transformation must be documented.

Every reported empirical value must be traceable to an analysis output.

---

Accessibility Philosophy

Accessibility is integrated into the system architecture rather than treated as a visual-design checklist.

The product requirements include:

- large text
- high contrast
- screen-reader support
- captions
- visual equivalents for audio alerts
- voice interaction
- cognitive-accessibility mode
- wheelchair-related boarding and securement support.

The research extension therefore treats explanation as a multimodal communication problem.

---

Safety Philosophy

The explanation layer is subordinate to safety-critical interaction.

The interface must preserve:

- persistent emergency access
- clear emergency states
- short incident communication
- non-time-limited safety interaction
- separation between entertainment and vehicle-control functions

The PRD specifies that safety controls must remain reachable from every screen and that emergency interaction must not depend on time-limited or gesture-only mechanisms.

---

Final Design Framework

Passenger Explanation Framework

01 — Recognise

Identify the unexpected vehicle event.

02 — Explain

Provide the relevant reason.

03 — Act

Communicate what the vehicle is doing.

04 — Relate

Explain what the passenger should expect.

05 — Expand

Allow optional deeper information.

Recognise
   ↓
Explain
   ↓
Act
   ↓
Relate
   ↓
Expand

The framework is intentionally designed around progressive disclosure.

The passenger receives the minimum information required for immediate orientation first, with additional detail available when needed.

---

Final Project Deliverables

Product

- complete information architecture
- user flows
- design system
- accessibility specification
- Journey Dashboard
- explanation-card system
- route experience
- diagnostics
- emergency experience
- relevant edge states
- hi-fi prototype

Research

- literature review
- theoretical framework
- research questions
- hypotheses
- operationalisation
- methodology
- experimental protocol
- ethics framework
- data dictionary
- analysis plan
- results framework
- findings synthesis
- discussion
- contribution statement

Communication

- research paper
- final presentation
- GitHub documentation
- portfolio case study

---

Final Project Status

Product design

Complete

Human Factors framework

Complete

Experimental architecture

Complete

Prototype specification

Complete

Data infrastructure

Complete

Analysis framework

Complete

Research manuscript architecture

Complete

Empirical findings

Populate from actual participant data

Final statistical claims

Populate from verified dataset

---

What This Project Demonstrates

This project demonstrates the ability to move between:

Product thinking

→ defining a complex passenger-facing system

UX/HCI

→ information architecture, interaction design and accessibility

Human Factors

→ comprehension, workload, situation awareness and trust

Research

→ operationalisation, hypotheses and experimental design

Data analysis

→ reproducible measurement and statistical reasoning

XAI

→ translating automated system behaviour into human-understandable explanations

Safety-critical UX

→ maintaining safety hierarchy under dynamic interface conditions

Research communication

→ converting design and empirical evidence into a structured academic argument

---

Final Project Statement

«Autonomous vehicles remove the driver from the interaction loop, but they do not remove the passenger's need to understand what the vehicle is doing.

This project investigates how passenger-facing explanations can bridge that gap—providing enough information to support understanding and appropriately calibrated trust while respecting cognitive workload, accessibility and safety constraints.»

---

Project Endpoint

The completed project is not defined by the number of screens produced.

It is defined by the traceability of the reasoning:

Requirement
   ↓
Research question
   ↓
Hypothesis
   ↓
Design decision
   ↓
Experimental manipulation
   ↓
Measurement
   ↓
Evidence
   ↓
Interpretation
   ↓
Design implication

Every major design decision should be explainable through this chain.

That is the final standard of the project.

---

Version

Research/Design Release: 1.0

Status: Research-grade HCI project

Primary domain: Human Factors / HCI / Explainable AI / Autonomous Vehicles

Research focus: Passenger understanding, calibrated trust and cognitive workload

Experimental framework: EV-1.0

Primary outcome: Objective comprehension

Secondary outcomes: Trust, workload, response time, perceived understanding, task success and interaction error

---

Final Integrity Note

This repository distinguishes between:

- what was specified,
- what was designed,
- what was tested,
- what was observed,
- and what can legitimately be concluded.

Where empirical data are available, findings should be reported directly from the verified dataset.

Where empirical data are unavailable, the repository retains the completed methodology and analysis infrastructure without manufacturing results.

That distinction is part of the research quality of the project itself.
