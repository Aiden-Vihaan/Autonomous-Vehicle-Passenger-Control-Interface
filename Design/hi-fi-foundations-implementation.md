High-Fidelity Foundations Implementation

1. Purpose

This document defines how the high-fidelity design foundation will be implemented in Figma for the Autonomous Vehicle Passenger Control Interface.

The purpose is to translate the previously established visual and interaction principles into a reusable design system while preserving the experimental architecture established during the low-fidelity phase.

The high-fidelity implementation must improve:

- visual hierarchy
- readability
- consistency
- accessibility
- interaction clarity
- perceived system transparency
- component reusability

It must not change the experimental variables, scenario sequence, explanation conditions, measurement sequence, or state transitions defined in the experimental architecture freeze.

---

2. Implementation Principles

The high-fidelity implementation follows six primary principles.

2.1 Calm by Default

Normal journey states should avoid unnecessary visual emphasis.

The interface should communicate that the autonomous system is operating normally without continuously demanding passenger attention.

2.2 Present in Crisis

Safety-relevant events should receive sufficient visual emphasis to support rapid passenger comprehension.

Emphasis should come from hierarchy, positioning, concise language, and semantic state representation rather than visual overload.

2.3 Explain the Why

When the autonomous vehicle changes its behaviour, the passenger should be able to understand the reason for the action.

The explanation component must remain visually distinguishable from decorative or secondary information.

2.4 Information Before Decoration

Visual elements must support comprehension, navigation, status recognition, or interaction.

Decorative elements should not compete with safety-relevant or experimental information.

2.5 Consistency

Equivalent information must use equivalent visual structures throughout the prototype.

Examples include:

- vehicle status
- journey progress
- explanation cards
- action buttons
- comprehension questions
- trust questions
- workload questions

2.6 Experimental Integrity

Visual refinement must not unintentionally modify the independent variable.

For example:

- the contextual explanation must not receive substantially greater visual prominence merely because it contains more information;
- the no-explanation condition must not contain substitute explanatory information;
- the autonomous response must remain identical across explanation conditions.

---

3. Figma Foundations

Create a dedicated Figma page:

"01 — Foundations"

The page should contain the following sections:

1. Colour
2. Typography
3. Spacing
4. Layout
5. Radius
6. Borders
7. Elevation
8. Iconography
9. Semantic states
10. Accessibility references

---

4. Colour Foundation

The existing PRD establishes a semantic token approach.

The high-fidelity implementation should therefore use semantic roles rather than assigning colours directly to individual components.

4.1 Semantic Colour Roles

Token Role| Purpose
Background / Primary| Main application surface
Background / Secondary| Secondary surface or supporting region
Surface / Primary| Primary card or component surface
Surface / Secondary| Supporting surface
Text / Primary| Main readable content
Text / Secondary| Supporting information
Text / Disabled| Disabled or unavailable content
Border / Default| Standard component boundaries
Border / Focus| Keyboard or interaction focus
State / Normal| Normal operational state
State / Attention| Non-critical attention state
State / Safety| Safety-relevant state
State / Degraded| Reduced-system-capability state
State / Emergency| Emergency state

Exact colour values should be taken from the approved PRD/design-system source rather than invented during implementation.

---

5. Light and Dark Themes

The interface supports both light and dark themes.

Create two theme sections:

- "Theme / Light"
- "Theme / Dark"

The semantic meaning of a token must remain consistent between themes.

For example:

"State / Safety"

must continue to represent the same semantic condition regardless of whether the interface is displayed in light or dark mode.

Do not use colour alone to communicate a state.

Each important state should have supporting:

- text
- iconography
- position
- component structure
- or other redundant representation.

---

6. Typography Foundation

Typography should prioritize legibility and rapid information recognition.

Create a reusable type scale rather than assigning arbitrary font sizes to individual screens.

Recommended semantic roles:

Style| Usage
Display| Large journey or primary contextual information
Heading 1| Major screen section
Heading 2| Component or content section
Heading 3| Supporting subsection
Body Large| Primary explanatory content
Body| Standard interface content
Body Small| Supporting information
Label| Component labels
Caption| Secondary metadata

Typography must remain consistent across:

- journey information
- system status
- explanation cards
- safety states
- measurement screens
- buttons
- error messages

---

7. Spacing Foundation

Use a consistent spacing scale throughout the interface.

Spacing should be defined as reusable design tokens rather than manually selected values for each component.

Primary spacing applications include:

- screen margins
- card padding
- component gaps
- text-to-icon spacing
- section separation
- button spacing
- measurement-question spacing

Spacing should support grouping and hierarchy.

Related information should appear closer together than unrelated information.

---

8. Layout Foundation

The primary interface uses the established landscape in-cabin display concept.

The layout should provide:

1. persistent orientation
2. clear primary content
3. secondary supporting information
4. predictable interaction areas
5. sufficient visual separation between system information and passenger actions

The layout should remain stable across journey states where possible.

Safety-relevant events may increase the prominence of the relevant information without causing unnecessary restructuring of the entire interface.

---

9. Border and Radius Foundation

Use a consistent radius system for:

- cards
- buttons
- status indicators
- input controls
- modal surfaces
- explanation components

Borders should be used primarily to establish grouping and boundaries.

Do not use excessive borders as a substitute for hierarchy.

---

10. Elevation Foundation

Elevation should communicate layering and grouping.

Use elevation selectively for:

- primary cards
- floating controls
- overlays
- important transient information

Do not use elevation merely as decoration.

Safety-relevant information should remain understandable even if elevation or shadow effects are unavailable.

---

11. Iconography

Icons should support recognition rather than replace essential textual information.

Important states should use icons consistently.

Examples:

- normal journey state
- attention state
- safety-relevant state
- degraded state
- emergency state
- explanation
- information
- accessibility
- passenger assistance

Icons must be:

- visually consistent
- recognizable
- sufficiently large
- paired with text when ambiguity is possible

---

12. Semantic State Foundation

The system uses the following primary semantic states.

Normal

The autonomous system is operating within expected parameters.

Visual treatment:

- low visual emphasis
- stable hierarchy
- minimal interruption

Attention

The passenger may benefit from awareness of a developing situation.

Visual treatment:

- moderate emphasis
- concise supporting information
- no unnecessary alarm

Safety-Relevant

The system has encountered a situation requiring meaningful passenger awareness.

Visual treatment:

- strong hierarchy
- clear event description
- clear autonomous response
- clear explanation

Degraded

The autonomous system's capability is reduced or operating under a constrained condition.

Visual treatment:

- explicit system status
- concise explanation
- clear passenger options where applicable

Emergency

Immediate passenger attention or action may be required.

Visual treatment:

- highest appropriate hierarchy
- clear action
- minimal ambiguity
- accessible emergency control

---

13. Explanation Foundation

The explanation component is a central experimental component.

It must support three conditions:

Condition A — No Explanation

The interface does not provide an explanatory reason for the autonomous response.

The vehicle response itself remains visible.

Condition B — Minimal Explanation

The interface provides a concise reason.

Example structure:

«Slowing for pedestrian.»

Condition C — Contextual Explanation

The interface provides additional contextual information.

Example structure:

«Pedestrian entering the crossing ahead. Slowing to maintain a safe distance.»

These example sentences are illustrative interface content, not experimental results.

---

14. Explanation Component Rules

All three conditions must preserve:

- identical placement where practical
- equivalent visual quality
- equivalent interaction expectations
- identical vehicle response
- identical scenario timing

The manipulated factor should be the explanatory information rather than unrelated visual treatment.

The contextual condition may contain more text, but additional content should not be accompanied by unnecessary decorative emphasis.

---

15. Accessibility Foundation

The high-fidelity implementation must preserve the accessibility requirements established in the original product specification.

Consider:

- readable typography
- sufficient contrast
- non-colour-dependent state communication
- clear touch targets
- consistent interaction patterns
- understandable language
- predictable navigation
- support for different sensory modalities where included in the design
- reduced cognitive complexity during safety-relevant states

Accessibility should be treated as part of the interaction design rather than a final visual check.

---

16. Figma Naming Convention

Use predictable names.

Examples:

Color / Background / Primary
Color / Text / Primary
Color / State / Safety
Type / Heading 1
Type / Body
Spacing / 16
Radius / Medium
Component / Explanation
Component / Vehicle Status
Component / Primary Button
Component / Emergency Action

Frames should use:

EXP-00 / Start
EXP-01 / Practice
EXP-02 / Normal Journey
EXP-03 / Event Approach
EXP-04 / Unexpected Event
EXP-05 / Autonomous Response
EXP-05A / No Explanation
EXP-05B / Minimal Explanation
EXP-05C / Contextual Explanation
EXP-06 / Comprehension
EXP-07 / Trust
EXP-08 / Workload
EXP-09 / Complete

---

17. Implementation Order

Build the system in the following order:

1. colour tokens
2. typography
3. spacing
4. layout grid
5. semantic states
6. icons
7. buttons
8. cards
9. vehicle status
10. explanation component
11. emergency control
12. measurement components
13. complete screen compositions

This order minimizes inconsistent component construction.

---

18. Validation Checklist

Before using the foundations in the experimental prototype, verify:

- [ ] Semantic tokens are defined.
- [ ] Light and dark themes are consistent.
- [ ] Typography hierarchy is consistent.
- [ ] Spacing follows a reusable system.
- [ ] Semantic states are distinguishable.
- [ ] Important states are not communicated through colour alone.
- [ ] Explanation variants remain experimentally comparable.
- [ ] Components use consistent naming.
- [ ] Touch targets are sufficiently clear.
- [ ] Accessibility considerations are represented.
- [ ] No experimental variable has been changed.
- [ ] Existing prototype architecture remains intact.

---

19. Definition of Done

The high-fidelity foundation is complete when:

1. The visual token system is implemented in Figma.
2. Light and dark themes are established.
3. Typography and spacing systems are reusable.
4. Semantic states are consistently represented.
5. Core visual foundations are documented.
6. Explanation variants are defined without changing their experimental meaning.
7. Accessibility principles are incorporated.
8. The foundation can be applied consistently to the experimental screen set.
9. The architecture freeze remains unchanged.

The next phase is implementation of the reusable high-fidelity components.
