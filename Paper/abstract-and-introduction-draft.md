Abstract and Introduction Draft

Designing Passenger-Facing Explanations for Autonomous Vehicle Behaviour: A Human Factors Approach to Understanding, Trust, and Cognitive Workload

Abstract

Autonomous vehicles change the traditional relationship between humans and transportation by removing the need for a human driver while simultaneously reducing passengers' direct visibility into vehicle decision-making. Although passengers may understand that an automated system is responsible for driving, unexpected behaviours such as slowing, stopping, rerouting, or yielding can create uncertainty when the reason for the behaviour is unclear. This project investigates how passenger-facing explanations of unexpected autonomous-vehicle behaviour can support understanding while maintaining appropriate trust and manageable cognitive workload.

The study develops a Human Factors framework for designing and evaluating explanations within an autonomous-vehicle passenger interface. Three explanation conditions are considered: no explanation, minimal explanation, and contextual explanation. The experimental framework focuses primarily on passenger comprehension, with response time, trust, workload, perceived understanding, task success, interaction errors, and qualitative observations considered as secondary measures. The design is informed by concepts from Trust in Automation, Situation Awareness, Cognitive Workload, Explainable AI, and Human-Automation Interaction.

The interface architecture treats unexpected autonomous-vehicle behaviour as an explicit interaction event. Instead of presenting raw system information, explanations are structured around what the vehicle detected, what it is doing, and what the behaviour means for the passenger. The framework also considers explanation timing, information density, accessibility, multimodal communication, and the separation of safety-critical controls from explanatory content.

The project contributes a reproducible research-to-design workflow connecting autonomous-vehicle scenarios, explanation conditions, passenger interaction, measurement, data-quality procedures, analysis, and design decisions. Its intended contribution is not to establish a universally optimal explanation format, but to provide a structured Human Factors approach for experimentally investigating how explanation design affects passenger understanding and trust-related outcomes in autonomous mobility.

Keywords: Autonomous Vehicles; Human Factors; Human-Computer Interaction; Explainable AI; Trust in Automation; Situation Awareness; Cognitive Workload; Passenger HMI; Transparency; Intelligent Transportation Systems

---

1. Introduction

1.1 Background

The introduction of highly automated vehicles changes the role of the human inside a vehicle. In a conventional automobile, the driver directly observes the environment, interprets road events, makes decisions, and controls vehicle behaviour. In a highly automated vehicle, these responsibilities can shift substantially toward the automated driving system. The passenger therefore experiences transportation through a fundamentally different human-machine relationship.

The passenger does not necessarily need to understand the technical architecture of the autonomous-driving system. However, the passenger does need enough information to interpret what the vehicle is doing, understand relevant changes in the journey, determine whether an unexpected event requires action, and maintain an appropriately calibrated level of confidence in the system.

This creates a Human Factors problem at the interface between automated system behaviour and human interpretation.

The original product requirements for the Autonomous Vehicle Passenger Control Interface identify passenger concerns including loss of agency, opacity of vehicle intent, uncertainty during edge cases, unclear escalation paths, and exclusion of passengers whose sensory or physical capabilities do not match conventional interface assumptions. The PRD therefore places trust, explanation, safety, and accessibility at the centre of the passenger experience.

The product concept is consequently broader than a conventional infotainment interface. The passenger-facing system is intended to help passengers understand, interact with, and respond appropriately to a vehicle that is operating without a human driver. The interface includes journey information, route information, vehicle diagnostics, emergency controls, accessibility features, and explanation mechanisms.

---

1.2 The Human Factors Problem

One of the most important moments in an autonomous-vehicle journey occurs when the vehicle behaves differently from what the passenger expected.

Examples include:

- slowing unexpectedly;
- stopping at an apparently clear intersection;
- yielding to another road user;
- changing lanes;
- rerouting;
- responding to an emergency vehicle;
- adapting to environmental conditions.

From the passenger's perspective, the visible action may be clear while the underlying reason is not.

A vehicle slowing down is observable.

The reason for slowing down may not be.

This distinction is important because human interpretation is based not only on the observation of an action but also on understanding its meaning and implications.

The original PRD explicitly identifies this opacity of intent as a passenger problem: a passenger may see the vehicle brake, hesitate, or reroute without knowing whether the system detected a hazard or whether another explanation applies.

A passenger-facing explanation can therefore function as a bridge between automated system behaviour and human interpretation.

However, explanation itself introduces a design challenge.

Too little information may leave the passenger uncertain.

Too much information may create unnecessary cognitive demand.

An explanation that appears too late may fail to resolve the initial uncertainty.

An explanation that is technically accurate but difficult to understand may provide transparency without producing meaningful understanding.

The central problem is therefore not simply whether the system should explain itself.

The deeper question is:

«What should be explained, how specifically, when, and in what form should the explanation be presented to the passenger?»

---

1.3 Trust as a Human-Automation Interaction Problem

Trust is particularly important in autonomous mobility because passengers cannot continuously verify the vehicle's decisions through direct control.

The interface must therefore support a relationship in which passenger confidence is appropriately related to the system's observed behaviour.

The design objective is not maximum trust.

A passenger who trusts an automated system regardless of its behaviour may rely on it inappropriately. Conversely, a passenger who distrusts the system despite appropriate performance may experience unnecessary anxiety and reduced acceptance.

This project therefore uses the concept of calibrated trust.

Within the interface, explanations are treated as one mechanism that can help passengers interpret unexpected behaviour. The original product requirements similarly describe explanation as a central mechanism for communicating why an automated vehicle has changed its behaviour.

The Human Factors challenge is to determine whether different explanation presentations support better understanding without introducing unnecessary cognitive demand or inappropriate confidence.

---

1.4 Explainability as an Interaction Design Problem

Explainable AI is frequently discussed as a property of intelligent systems. From a passenger-interface perspective, however, explainability also becomes an interaction design problem.

A technically available explanation is not necessarily a usable explanation.

For a passenger, the relevant question may be much simpler:

«"Why did the car do that?"»

A useful passenger-facing explanation should therefore translate system behaviour into information that is relevant to the passenger's immediate situation.

The interface framework developed in this project organizes explanations around four layers:

WHAT HAPPENED
      ↓
WHAT THE VEHICLE IS DOING
      ↓
WHAT IT MEANS FOR THE PASSENGER
      ↓
OPTIONAL DETAIL

This approach reflects the product requirement that explanations should communicate automated decisions in plain language and appear as first-class interface events rather than hidden engineering information.

---

1.5 Accessibility as a Core Human Factors Requirement

Explanation design cannot assume that all passengers perceive or interact with information in the same way.

The original project requirements explicitly include visual, auditory, motor, cognitive, language, and wheelchair-accessibility considerations. Critical alerts are intended to have multimodal equivalents, while critical actions should remain accessible through appropriate interaction methods.

This makes accessibility directly relevant to explainability.

For example, an explanation that is understandable to a passenger reading a visual display may not be equally accessible to a passenger who relies on auditory or non-visual interaction.

Consequently, this project treats accessibility as part of the explanation architecture rather than as a separate layer added after the primary interface has been designed.

---

1.6 Research Objective

The objective of this project is to develop and evaluate a Human Factors framework for passenger-facing explanations of unexpected autonomous-vehicle behaviour.

The study focuses specifically on the relationship between explanation presentation and passenger interpretation.

The primary outcome is comprehension.

Secondary outcomes include:

- response time;
- trust;
- cognitive workload;
- perceived understanding;
- task success;
- interaction errors;
- qualitative observations.

---

1.7 Research Questions

Primary Research Question

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

Secondary Research Questions

1. Does explanation presence improve passenger understanding?
2. Does explanation specificity affect understanding and trust-related outcomes?
3. Does explanation timing influence passenger interpretation of autonomous behaviour?
4. Does event risk or urgency moderate the usefulness of explanations?
5. How does passenger activity affect the usefulness of visual, auditory, or multimodal explanations?

---

1.8 Research Approach

The project evaluates three explanation conditions:

Condition A — No Explanation

The vehicle performs the unexpected action without a passenger-facing explanation.

Condition B — Minimal Explanation

The interface provides a concise reason.

«"Slowing for pedestrian."»

Condition C — Contextual Explanation

The interface provides the reason together with relevant contextual information.

«"Pedestrian entering the crossing ahead. Slowing to maintain a safe distance."»

The three conditions allow the project to investigate explanation presentation as a spectrum rather than reducing explainability to a binary variable.

---

1.9 Contribution

The central contribution of the project is a Human Factors framework that connects:

Autonomous Vehicle Event
        ↓
Explanation Design
        ↓
Passenger Understanding
        ↓
Trust + Workload
        ↓
Interaction Outcome
        ↓
Evidence-Based Design Decision

The project therefore connects product design with empirical Human Factors evaluation.

Its contribution is not a claim that one explanation format is universally superior.

Instead, it provides a structured method for investigating how explanation specificity, timing, information density, accessibility, and interaction context affect passenger experience.

---

1.10 Scope of the Study

The project focuses on the passenger-facing human-machine interface.

The following are within scope:

- passenger explanations;
- unexpected vehicle behaviour;
- comprehension;
- trust-related responses;
- cognitive workload;
- interaction;
- accessibility;
- explanation timing;
- interface design.

The following are outside the scope:

- autonomous-driving stack development;
- vehicle perception algorithms;
- fleet operations;
- production vehicle certification;
- functional-safety certification;
- real-world vehicle control;
- claims of ISO 26262 compliance;
- autonomous-driving performance validation.

The interface is therefore evaluated as a Human Factors prototype and research artifact rather than as a production autonomous-driving system.

---

1.11 Structure of the Paper

The remainder of the paper is organized as follows.

Section 2 reviews related work in Trust in Automation, Situation Awareness, Cognitive Workload, Explainable AI, Human-Automation Interaction, multimodal interaction, and accessibility.

Section 3 establishes the research gap, theoretical framework, research questions, hypotheses, and conceptual model.

Section 4 presents the methodology, variables, scenarios, experimental conditions, procedure, and measurement framework.

Section 5 describes the passenger interface architecture and explanation design.

Section 6 presents the experimental data and analysis.

Section 7 discusses the findings in relation to the theoretical framework.

Section 8 presents evidence-based design implications.

Section 9 discusses limitations and validity considerations.

Section 10 presents future research directions.

Section 11 concludes the study and summarizes its contribution.

---

1.12 Research Integrity Statement

This project follows a strict evidence boundary.

No participant result, numerical statistic, qualitative observation, or empirical conclusion will be presented unless it is supported by recorded study data.

Where empirical evidence is unavailable or incomplete, the paper will explicitly identify the relevant section as methodological, conceptual, proposed, or limited.

This distinction is essential because the value of a Human Factors project depends not only on the sophistication of its interface but also on the validity and transparency of its evidence.
