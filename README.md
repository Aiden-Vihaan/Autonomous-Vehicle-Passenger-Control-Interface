# Autonomous-Vehicle-Passenger-Control-Interface
The Autonomous Vehicle Passenger Control Interface is a human-centered UX/UI project exploring how passengers can interact with and understand highly automated vehicles in everyday and unexpected situations. It focuses on the in-cabin experience of Level 4 and Level 5 autonomous vehicles, using a robotaxi service such as Waymo One as the reference.

---

Overview

The Autonomous Vehicle Passenger Control Interface is a human-centered UX/UI project focused on the in-cabin experience of passengers travelling in highly automated vehicles.

The project explores how an autonomous vehicle can communicate its intentions, system state, environmental understanding, and safety-related information in a way that passengers can understand and act upon without unnecessary cognitive burden.

The work uses a Level 4/Level 5 autonomous robotaxi context, with Waymo One serving as the reference service for the product context. The project is structured around the design of a passenger-facing control interface for a primary in-cabin display, supported by complementary mobile and voice interactions.

The project combines UX/UI design, Human Factors, HCI, explainable AI, accessibility, interaction design, and empirical evaluation into a single end-to-end workflow.

---

Problem

Highly automated vehicles remove many of the conventional controls passengers associate with driving. While this reduces the need for direct vehicle operation, it creates new challenges around:

- Understanding what the vehicle is doing
- Understanding why the vehicle is behaving in a particular way
- Maintaining appropriate trust in automation
- Recognising unexpected or safety-relevant situations
- Knowing when and how passengers can intervene
- Managing uncertainty without creating unnecessary anxiety
- Supporting passengers with different accessibility needs

The project therefore investigates how passenger interfaces can communicate complex autonomous-system behaviour through clear, contextual, and actionable information.

---

Project Objectives

Product Objectives

- Design a clear passenger control experience for an autonomous vehicle.
- Provide understandable information about vehicle behaviour and system state.
- Support passenger interaction during normal and unexpected situations.
- Create clear safety and emergency pathways.
- Develop an accessible and consistent interface.
- Establish a reusable design system and interaction framework.

Human Factors Objectives

- Explore how interface explanations affect passenger understanding.
- Investigate the relationship between explainability and trust in automation.
- Consider cognitive workload and information requirements during unexpected events.
- Apply Human Factors principles to safety-relevant interaction design.
- Evaluate interaction performance using measurable user outcomes.

---

Research Direction

The research component focuses on explainable AI in autonomous vehicle passenger interfaces.

Primary Research Question

«How does explainable AI feedback influence passenger understanding, trust, perceived workload, and interaction performance during unexpected events in a highly automated vehicle?»

Supporting Questions

- Does contextual explanation improve passenger understanding compared with minimal explanation?
- Can explanations improve trust calibration without increasing unnecessary cognitive workload?
- How does explanation timing influence interpretation of autonomous vehicle behaviour?
- How can safety-relevant information remain understandable and actionable under uncertainty?

The research design, hypotheses, methodology, experimental protocol, and results are documented separately within the ""research/"" (research/) and ""experiment/"" (experiment/) directories.

---

Design Principles

The interface is guided by the following principles:

1. Trust through transparency
   Communicate relevant system behaviour without overwhelming passengers.

2. Show the why
   Explain important autonomous decisions in concise, contextual language.

3. Calm by default
   Normal operation should feel predictable and unobtrusive.

4. Present in crisis
   Safety-relevant information should become clear, prominent, and actionable when required.

5. One tap to safety
   Critical passenger actions should be easy to locate and perform.

6. Accessible by design
   Information should not depend exclusively on colour, vision, hearing, or complex interaction.

---

Project Scope

The project covers:

- Product requirements
- User flows
- Information architecture
- Passenger control interactions
- Autonomous vehicle state modelling
- Explainable AI interaction patterns
- Safety and emergency states
- Degraded-system experiences
- Accessibility considerations
- Design tokens and components
- Light and dark interface themes
- High-fidelity interface design
- Interactive prototyping
- Human Factors analysis
- Experimental evaluation
- Data analysis
- Research documentation

The project does not claim production deployment, vehicle certification, regulatory approval, or compliance with functional-safety standards unless explicitly documented and verified.

---

Project Structure

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
│   └── figures/
│
├── paper/
│   └── research-paper.pdf
│
├── presentation/
│   └── final-presentation.pptx
│
└── docs/
    ├── weekly-progress.md
    ├── decisions-log.md
    └── changelog.md

---

Methodology

The project follows an iterative human-centered design process:

Problem Definition → Literature Review → Human Factors Analysis → Requirements → Interaction Design → Prototyping → Evaluation → Analysis → Refinement → Documentation

Design decisions are documented throughout the process rather than being reconstructed retrospectively.

The research methodology and evaluation procedures are maintained separately so that the project remains transparent and reproducible.

---

Evaluation

The evaluation component is intended to examine measurable aspects of passenger interaction, including where appropriate:

- Comprehension accuracy
- Response time
- Interaction success
- Interaction errors
- Trust and trust calibration
- Perceived transparency
- Perceived usability
- Cognitive workload

Specific measures, experimental conditions, participant procedures, and statistical analyses will be documented in the relevant research and experiment files.

No participant data or personally identifiable information will be published in this repository.

---

Design & Prototype

The interface is developed around a primary in-cabin passenger display, with consideration for complementary mobile and voice interactions.

The prototype explores:

- Normal autonomous operation
- Vehicle intent communication
- Environmental perception information
- Contextual AI explanations
- Unexpected events
- System uncertainty
- Degraded operation
- Emergency interaction
- Passenger assistance
- Accessibility
- Light and dark themes

The final prototype and supporting design documentation will be available in the ""prototype/"" (prototype/) and ""design/"" (design/) directories.

---

Documentation

This repository is designed to preserve the complete development process.

Directory| Purpose
"PRD/"| Product requirements and source documentation
"research/"| Research questions, literature, theory, and methodology
"design/"| UX/UI decisions, flows, systems, and frameworks
"prototype/"| Prototype materials and exports
"experiment/"| Evaluation scenarios, protocols, and participant materials
"analysis/"| Data analysis and visualisations
"paper/"| Final research-oriented documentation
"presentation/"| Final presentation materials
"docs/"| Progress, decisions, and project history

---

Research Integrity

This project distinguishes between:

- Designed concepts
- Prototype behaviour
- Observed user behaviour
- Research findings
- Interpretations and recommendations

Claims about user behaviour or research outcomes will only be made after appropriate evaluation.

The project does not present conceptual designs as production-ready autonomous-vehicle technology and does not claim regulatory or functional-safety certification.

---

Project Status

This repository is maintained throughout the project lifecycle.

For current progress and historical development, see:

- ""docs/weekly-progress.md"" (docs/weekly-progress.md)
- ""docs/decisions-log.md"" (docs/decisions-log.md)
- ""docs/changelog.md"" (docs/changelog.md)

The README intentionally provides a stable overview of the project and is not intended to function as a daily progress log.

---

Final Deliverables

The completed project is intended to produce:

- Product requirements documentation
- Human Factors and HCI research documentation
- High-fidelity interface prototype
- Design system
- Experimental prototype
- Evaluation methodology
- Analysis and findings
- Research-paper-style report
- Final presentation
- Portfolio case study
- Complete GitHub development record

---

Author

Aiden Vihaan

Human-Computer Interaction · UX/UI Design · Human Factors · Cognitive Science

---

Disclaimer

This is an academic, portfolio, and internship-oriented design and research project. Autonomous vehicle behaviour, safety mechanisms, and system capabilities represented in the prototype are conceptual unless explicitly identified as existing capabilities of the referenced service.

The project should not be interpreted as a production autonomous-driving system, safety certification, or engineering validation of an actual vehicle.
