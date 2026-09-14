Day 33 — Empirical Results Generation

Project: Autonomous Vehicle Passenger Control Interface
Experimental Version: EV-1.0
Day: 33
Phase: Empirical Analysis
Status: Results-generation workflow completed

---

1. Objective

Day 33 converts the analysis-ready experimental structure established during Days 28–32 into a formal empirical-results generation workflow.

The objective is to produce an evidence trace from:

«Recorded observation → validated trial → condition-level dataset → descriptive result → statistical analysis → interpretation»

The analysis remains centred on the primary research question:

«How does the presentation of explanations for unexpected autonomous-vehicle behaviour affect passenger understanding, trust, and cognitive workload?»

---

2. Experimental Conditions

The experiment compares three explanation conditions.

Code| Condition| Explanation Strategy
A| No Explanation| Vehicle behaviour changes without an explanatory message.
B| Minimal Explanation| Concise plain-language explanation of the immediate reason for the behaviour.
C| Contextual Explanation| Specific explanation describing the relevant situation and intended vehicle response.

The independent variable is therefore:

«Explanation condition»

The primary dependent variable is:

«Passenger comprehension»

Secondary dependent variables are:

- response time;
- trust;
- workload;
- perceived understanding;
- task success;
- interaction errors;
- qualitative observations.

---

3. Analysis Population

The analysis population is determined from the recorded dataset rather than predetermined for presentation purposes.

The following quantities are calculated:

N recruited
N completed
N contributing valid trials
Total recorded trials
Valid trials
Excluded trials
Interrupted trials
Trials with technical issues
Trials with protocol deviations

No participant or trial is excluded solely because its result does not support the research hypothesis.

---

4. Trial Validity

A trial is considered valid for a specific analysis when:

1. the participant identifier is available;
2. the trial identifier is valid;
3. the scenario is identifiable;
4. the explanation condition is correctly coded;
5. the relevant dependent measure is available;
6. no quality flag invalidates that particular measurement.

A trial may therefore be valid for one analysis while being unavailable for another.

For example:

«A trial with a valid comprehension response but a missing trust rating may contribute to comprehension analysis but not trust analysis.»

---

5. Primary Result

5.1 Comprehension

The primary comparison evaluates comprehension across:

A — No Explanation
B — Minimal Explanation
C — Contextual Explanation

The following descriptive quantities are generated:

- valid observations per condition;
- mean comprehension score;
- median comprehension score;
- standard deviation;
- minimum;
- maximum;
- proportion of correct responses.

The primary result is reported only after the recorded dataset has been inspected.

---

6. Primary Analysis Logic

The analytical sequence is:

Comprehension
      ↓
Distribution inspection
      ↓
Condition-level descriptive statistics
      ↓
Within-participant structure assessment
      ↓
Inferential test selection
      ↓
Effect estimation
      ↓
Interpretation

The statistical method is not selected solely because it produces a desirable result.

It is selected according to:

- experimental design;
- measurement scale;
- sample size;
- distribution;
- repeated-measures structure;
- independence assumptions;
- missingness;
- and the actual recorded dataset.

---

7. Secondary Result 1 — Response Time

Response time is examined to determine whether explanation condition is associated with differences in the time required to interpret and respond to the event.

Because response-time distributions can be asymmetric, both:

- mean response time;
- median response time

are retained.

Extreme values are investigated rather than automatically removed.

Potential causes include:

- interruption;
- technical delay;
- participant hesitation;
- misunderstanding;
- accidental interaction;
- or genuine behavioural variation.

---

8. Secondary Result 2 — Trust

Trust scores are compared across the three explanation conditions.

The analysis asks:

«Does the presence and specificity of an explanation correspond to a measurable difference in reported trust?»

The interpretation remains limited to the experimental context.

A higher trust score does not demonstrate that the autonomous system is objectively safer.

It indicates a difference in the participant's reported relationship with the system under the tested interaction condition.

---

9. Secondary Result 3 — Workload

Workload is analysed to test whether explanation presentation changes perceived cognitive demand.

Three possibilities remain empirically open:

Lower workload

An explanation may reduce uncertainty and therefore reduce cognitive demand.

Higher workload

Additional information may require additional processing.

No meaningful difference

The explanation may change understanding without producing a measurable workload difference.

The analysis does not assume which outcome will occur.

---

10. Secondary Result 4 — Perceived Understanding

Perceived understanding is compared across conditions.

This variable is deliberately separated from objective comprehension.

The analysis therefore distinguishes:

«“I feel that I understand the vehicle.”»

from:

«“I can correctly explain what the vehicle is doing.”»

This distinction is important for evaluating calibrated passenger understanding.

---

11. Secondary Result 5 — Task Success

Task success is reported as:

Successful trials
Total valid trials
Success proportion

The condition-level comparison examines whether explanation presentation corresponds to differences in successful completion of the defined passenger task.

---

12. Secondary Result 6 — Interaction Errors

Interaction errors are analysed separately from task failure.

This distinction allows the study to differentiate:

- unsuccessful task completion;
- incorrect interface action;
- hesitation;
- accidental interaction;
- and other observable interaction problems.

---

13. Objective–Subjective Understanding Analysis

A key analysis compares:

Comprehension
      ↕
Perceived Understanding

The analysis considers whether subjective understanding corresponds with demonstrated understanding.

Potential empirical patterns are:

Pattern| Interpretation
High comprehension + high perceived understanding| Alignment
Low comprehension + high perceived understanding| Possible overconfidence
High comprehension + low perceived understanding| Possible underconfidence
Low comprehension + low perceived understanding| Consistent difficulty

These are analytical categories, not predetermined findings.

---

14. Trust–Understanding Analysis

The study also examines the relationship between:

Comprehension
      ↕
Trust

The purpose is not to assume that greater trust is desirable under every circumstance.

The Human Factors objective is calibration:

«passenger confidence should be appropriately related to their understanding of the system's behaviour.»

Accordingly, an increase in trust without a corresponding improvement in understanding should not automatically be interpreted as a successful design outcome.

---

15. Workload–Understanding Analysis

The analysis also considers the joint relationship between:

Comprehension
      ↕
Workload

An explanation that improves comprehension while substantially increasing workload may represent a design trade-off rather than an unqualified improvement.

Conversely, an explanation that reduces workload while failing to improve comprehension may not achieve the intended transparency objective.

---

16. Condition-Level Results Table

The final empirical table follows this structure:

Outcome| A: No Explanation| B: Minimal| C: Contextual
Valid observations| Dataset-derived| Dataset-derived| Dataset-derived
Mean comprehension| Dataset-derived| Dataset-derived| Dataset-derived
Correct comprehension| Dataset-derived| Dataset-derived| Dataset-derived
Median response time| Dataset-derived| Dataset-derived| Dataset-derived
Mean trust| Dataset-derived| Dataset-derived| Dataset-derived
Mean workload| Dataset-derived| Dataset-derived| Dataset-derived
Perceived understanding| Dataset-derived| Dataset-derived| Dataset-derived
Task success| Dataset-derived| Dataset-derived| Dataset-derived
Interaction errors| Dataset-derived| Dataset-derived| Dataset-derived

No placeholder numerical values are inserted.

---

17. Statistical Reporting Standard

Where inferential analysis is justified, the final report should include:

- statistical test;
- test statistic;
- degrees of freedom where applicable;
- p-value;
- effect size;
- confidence interval where appropriate;
- sample size;
- analysis population;
- assumptions or limitations.

Statistical significance is not treated as the sole indicator of practical importance.

---

18. Effect Size

Where an appropriate effect-size measure can be calculated, it is reported alongside statistical significance.

The purpose is to answer:

«How large is the observed difference?»

rather than only:

«Is the observed difference statistically detectable?»

This is particularly important for Human Factors research where a statistically detectable difference may have limited practical relevance.

---

19. Qualitative Results

Qualitative observations are analysed using structured thematic coding.

Initial coding categories are:

- clarity;
- ambiguity;
- reassurance;
- information overload;
- explanation timing;
- explanation relevance;
- perceived control;
- trust;
- confusion;
- unexpected interpretation;
- accessibility;
- interaction difficulty.

A category becomes an empirical theme only when supported by actual observations.

---

20. Negative and Null Findings

The results section explicitly preserves:

- null effects;
- contradictory observations;
- unexpected outcomes;
- negative user reactions;
- condition-specific failures;
- and measurement limitations.

The analysis does not selectively report only outcomes favourable to the proposed design.

---

21. Empirical Results Integrity Statement

This project follows a strict evidence rule:

«No empirical number is considered a project result unless it originates from the recorded participant dataset.»

Therefore, the following are not generated in advance:

- participant count;
- mean scores;
- percentages;
- p-values;
- effect sizes;
- confidence intervals;
- correlations;
- statistical significance claims.

This prevents fabricated evidence from entering the research record.

---

22. Current Day 33 Result Status

Methodological outputs completed

- [x] Empirical-results generation workflow
- [x] Primary-outcome analysis logic
- [x] Secondary-outcome analysis logic
- [x] Participant/trial accounting framework
- [x] Trial-validity rules
- [x] Condition-level comparison framework
- [x] Objective–subjective understanding analysis
- [x] Trust–understanding analysis
- [x] Workload–understanding analysis
- [x] Qualitative-analysis framework
- [x] Statistical reporting standard
- [x] Effect-size reporting requirement
- [x] Null-result policy
- [x] Empirical-integrity controls

Empirical outputs

Actual numerical results remain dependent on the recorded dataset.

No simulated results are presented as experimental findings.

---

23. Interpretation Boundary

The experiment evaluates a passenger-interface concept under controlled research conditions.

It does not establish:

- autonomous-driving safety certification;
- production-system safety;
- regulatory compliance;
- ISO 26262 compliance;
- real-world crash-risk reduction;
- or operational performance of a deployed autonomous vehicle.

The appropriate claim is limited to the tested passenger-interface interaction.

---

24. Day 33 Conclusion

Day 33 completes the transition from an analysis-ready methodology to a formal empirical-results pipeline.

The project now has a complete evidence chain:

Research Question
      ↓
Hypotheses
      ↓
Experimental Conditions
      ↓
Participant Tasks
      ↓
Recorded Observations
      ↓
Quality-Controlled Dataset
      ↓
Descriptive Analysis
      ↓
Inferential Analysis Where Justified
      ↓
Human Factors Interpretation
      ↓
Design Implications

The next stage is therefore not additional methodological planning.

It is the conversion of actual observations into the project's first evidence-based results and design implications.
