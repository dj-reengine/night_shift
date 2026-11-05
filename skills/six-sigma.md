---
name: six-sigma
description: Practitioner-depth Six Sigma and Lean Six Sigma skill for public-sector process improvement (courts, corrections, municipal permitting, environmental regulators, utilities, licensing, benefits and eligibility programs). Use when a problem involves variation, error or defect rates, decision inconsistency across offices or reviewers, unexplained cycle-time spread, data-driven root cause, measurement system questions, statistical process control, DMAIC or DMADV project structure, belt roles and tollgates, or when drafting the Six Sigma or data-analysis portion of a ReEngine proposal methodology section. Draft-only; never fabricate data.
---

# Six Sigma and Lean Six Sigma for Public-Sector Work (ReEngine Consulting)

## 0. When to use this skill

Use this skill when:
- Outcomes vary and nobody can explain why (review times range from 3 to 300 days; one district approves 90% and another 60% of similar applications).
- Errors, returns, deficiencies, or rework are the dominant problem and the agency needs a defensible root cause before investing.
- Decisions must be consistent and auditable (eligibility, enforcement, sentencing support, inspection scoring, grant compliance), so measurement-system and attribute-agreement questions matter.
- An auditor, legislature, or oversight body requires data-based evidence of improvement.
- A Lean redesign is done and the agency needs control: control charts, control plans, response plans.
- A solicitation asks for DMAIC, belt training, statistical analysis, or "data-driven" process improvement.
- You are drafting a project charter, tollgate review, data collection plan, or control plan.

Do not use this skill alone when:
- The obvious problem is flow and waste with no real data question (use lean.md first).
- One step clearly limits throughput (use theory-of-constraints.md first; Six Sigma then reduces variation at and feeding the constraint).
- The change is clear but people are not adopting it (use change-management.md).

Default stance for ReEngine: Six Sigma is used inside GQI as the variation and verification lens, not as a heavy standalone program. Most government processes are transactional, data is messy, and sample sizes are modest; use the simplest statistically valid tool and explain it in plain language.

---

## 1. Source basis and evidence tags

This skill draws on expert knowledge of the Six Sigma body of knowledge (ASQ CSSBB/CSSGB bodies of knowledge, IASSC, Breyfogle's Integrated Enterprise Excellence, Montgomery, Wheeler) and on these read-only ReEngine sources:
- ReEngine BOK, Six Sigma subfolder (listed): Knowles, Six Sigma handbook (general information); Zailani and Ramayah, Six Sigma and organizational knowledge; Hummour (2018), TQM in municipalities in Jordan (empirical); Breyfogle, IEE DMAIC Roadmap, Define phase figure 9.4. These were identified in the folder; this skill's content on them is limited to their titles and general subject, as they were not read in full.
- ReEngine BOK, Lean and Continuous Improvement subfolders (read): Maleyeff (2007), Improving Service Delivery in Government with Lean Six Sigma (IBM Center for The Business of Government); Fryer, Antony, and Douglas (2007), Critical success factors of continuous improvement in the public sector; VA Lean Work Description (sample SOW, which lists LSS tools such as MSA, DOE, SPC, CCPM, and Hoshin and requires belt training); EPA Lean Government Implementation Guide (2017); Example A3 Problem Solving ReEng Format (LMO A3); Rother, Target Conditions (80-95% of variation is common cause, consistent with Deming); DoD Continuous Process Improvement Guidebook (2006).
- ReEngine RAG (read-only): Past Project Performance Reports #001-#044, CORE_METH_Main-Master-Logic, CORE_METH_4-Pillars-Framework, CORE_METH_BRAG-Tool-Logic, CORE_METH_Staff-Certifications.

Evidence tags used in this file:
- [Verified-deck]: a figure confirmed in a client deliverable reviewed by ReEngine.
- [Summary]: a figure from a RAG project summary; verify against the source deliverable before external use.
- [Target]: a goal, projection, or recommendation. Never present as a result.
- Hypothetical example: invented for teaching. Labeled every time.

---

## 2. Core concepts

### 2.1 What Six Sigma is

Six Sigma is a disciplined, data-driven approach to reducing variation and defects in a process so that it reliably meets customer requirements. It has three faces:
1. A metric: a process performing at "six sigma" produces about 3.4 defects per million opportunities (DPMO), assuming the conventional 1.5 sigma long-term shift.
2. A method: DMAIC for improving existing processes; DMADV (DFSS) for designing new ones.
3. A management system: project selection tied to strategy, trained belts, champions, tollgate reviews, and financial or mission benefit validation.

Lean Six Sigma (LSS) combines Lean's flow and waste focus with Six Sigma's variation focus. Maleyeff's government report (BOK) frames LSS for government as a way to improve service delivery when processes are complex, customers are multiple, and goals compete; he emphasizes adapting the manufacturing toolkit to services (intangible outputs, the customer in the process, high labor content, hidden queues in electronic inboxes).

### 2.2 Key ideas, plainly

- Y = f(X): the outcome (Y) is a function of inputs and process factors (Xs). Projects find the vital few Xs.
- Variation is the enemy of reliable service: an average of 30 days with a spread from 5 to 200 means many applicants wait far longer than the average suggests. Averages hide the story; this is the NH VR "Old Dogs" lesson: 83% of cases met the 60-day eligibility window while outliers averaging 840 days in services saturated counselor capacity [Summary].
- Common cause vs special cause (Shewhart, Deming): common-cause variation is built into the system and requires changing the system; special-cause variation is an assignable event that requires investigation of that event. Rother (BOK) notes 80-95% of variation is common cause. Treating common cause as special (blaming the individual for system noise) is tampering and makes things worse.
- Voice of the customer (VOC) becomes critical-to-quality (CTQ) requirements with specification limits; voice of the process (VOP) is what the process actually does (control limits). Capability compares the two.
- Data beats opinion, but data quality must be proven (measurement system analysis) before conclusions are drawn.
- Root cause must be verified (with data, an experiment, or a pilot), not just brainstormed.

### 2.3 Public-sector adaptations

| Manufacturing assumption | Public-sector reality | Adaptation |
|---|---|---|
| One customer who pays | Multiple customers: applicant, public, legislature, funders, oversight, future generations | Build a customer map; define CTQs per customer; use metric tension so one CTQ does not destroy another |
| Defects are obvious | "Defect" can be contested (a denial is not a defect if correct) | Define defects operationally: wrong decision, late decision, incomplete decision, rework, missing documentation |
| Profit is the benefit | Mission value, public trust, statutory compliance | Use quality throughput per operating expense (QT/OE) and cost-of-poor-quality in staff hours, not just dollars |
| Large automated data sets | Case management systems with free-text, inconsistent coding, manual spreadsheets | Plan data collection carefully; manual check sheets for 2-4 weeks are often the best data |
| Production can stop to fix | Due process and statutory clocks continue | Containment actions must protect legal deadlines |
| Management can mandate | Civil service, unions, elected officials, statutes | Involve stakeholders early; route policy changes through proper authority |

Fryer, Antony, and Douglas (BOK) find that public-sector CI depends on leadership commitment, customer focus, training, culture, and appropriate measurement, and that a frequent barrier is unclear identification of the customer. Begin every Define phase by resolving "who is the customer and what do they require."

Do not treat cost as value. The ReEngine/TOC government paper (Mycue and Schragenheim, BOK) uses a civil-rights investigation example: an investigation may cost $4,500, but its value lies in the protection delivered, not in its cost. Benefits in a government Six Sigma project should therefore be expressed as quality units delivered, time saved for the public, risk reduced, and capacity freed, with dollar figures only where real.

---

## 3. Roles and belts

| Role | Responsibility | Typical public-sector holder |
|---|---|---|
| Executive sponsor | Sets priorities, removes barriers, approves resources | Agency head, deputy director, city manager, court administrator |
| Champion | Owns project selection and tollgates in a business area | Division director |
| Process owner | Owns the process day to day and the control plan after closure | Program manager or supervisor |
| Master Black Belt (MBB) | Coaches belts, trains, reviews statistics, governs the portfolio | ReEngine senior consultant (ReEngine staff hold LSS Black Belt and Master Black Belt credentials per CORE_METH_Staff-Certifications) |
| Black Belt (BB) | Leads complex cross-functional projects; full statistical toolkit | Internal CI lead or ReEngine consultant |
| Green Belt (GB) | Leads smaller projects part time; core toolkit | Analyst, supervisor |
| Yellow Belt (YB) | Team member; basic tools | Front-line staff |
| Finance or budget partner | Validates benefits | Budget office |
| Data steward | Provides and validates data extracts | IT or records unit |

ReEngine practice: in government engagements the "belt" structure is often lightweight. A ReEngine partner acts as MBB/BB, agency staff participate as team members, and certification training (for example the GQI Practitioner courses delivered through LBJ School GCMD, Texas SAO workshops, and ND IT train-the-trainer [Summary]) builds internal capability. Confirm with David before citing Texas state-agency training in external materials.

---

## 4. DMAIC in depth

### 4.1 Overview

| Phase | Purpose | Key questions | Typical tools | Tollgate deliverables |
|---|---|---|---|---|
| Define | Agree the problem, customer, scope, goal | What is the problem, for whom, how big, and what is the goal? | Charter, SIPOC, VOC/CTQ tree, stakeholder map, high-level map, project plan | Signed charter; SIPOC; CTQs with operational definitions; stakeholder analysis; schedule |
| Measure | Establish baseline and data integrity | How is the process performing now, and can we trust the data? | Data collection plan, operational definitions, MSA/Gage R&R, attribute agreement, detailed map, baseline charts, capability | Validated baseline; MSA results; current capability; refined problem statement |
| Analyze | Find and verify root causes | Which Xs drive Y, and how do we know? | Fishbone, 5 Whys, Pareto, stratification, scatter, hypothesis tests, regression, VSM waste analysis, interference diagram | Verified root causes with evidence; quantified impact |
| Improve | Develop, test, and implement solutions | What change addresses the root cause, and does it work? | Solution selection matrix, FMEA on the new process, pilot, DOE where feasible, future-state map, implementation plan | Pilot results with before/after statistics; implementation plan; risk analysis |
| Control | Sustain the gain | How do we keep it, and who responds when it drifts? | Control plan, SPC charts, standard work, mistake-proofing, response plan, training, handoff | Control plan signed by process owner; charts in place; benefits validated; lessons learned |

### 4.2 Define, step by step

1. Write the problem statement: what, where, when, how big, compared to what standard. No cause and no solution in the statement.
   - Weak: "Permits are slow because staff are overworked."
   - Strong (hypothetical example): "From January to June [year], 38% of residential building permits exceeded the 30-day review standard set in [ordinance section], with a median of 34 days and 90th percentile of 71 days, generating an estimated [N] customer calls per month."
2. Identify customers and their requirements (VOC): interviews, complaint logs, surveys, call center data, statute and rule, audit findings, legislative testimony.
3. Translate VOC into CTQs using a CTQ tree: need (driver) to measurable requirement with a specification limit.
4. Build a SIPOC with start and stop points.
5. Set a goal (SMART) and a scope (in and out).
6. Identify the team, the sponsor, the champion, and the process owner.
7. Estimate benefits (hours, cycle time, error rate, QT/OE); mark as estimate.
8. Assess stakeholders and risks; plan communications (see change-management.md).
9. Tollgate review with the sponsor.

CTQ tree example (hypothetical example):

| Customer need | Driver | CTQ (measurable) | Spec |
|---|---|---|---|
| "I want my permit fast" | Timeliness | Calendar days from Full-Kit to decision | USL 30 days |
| "Tell me once what's missing" | Completeness of feedback | Percent of deficiency letters listing all deficiencies | LSL 95% |
| "Decisions must be right" | Accuracy | Percent of decisions upheld on QA review | LSL 98% |
| Legislature: "Show us the backlog" | Transparency | Monthly published WIP and age distribution | Published by day 5 |

### 4.3 Measure, step by step

1. Define the operational definitions for every metric: what counts, start and stop clocks, units, inclusion rules (for example "Clock starts at Full-Kit date as recorded in field X; excludes withdrawn applications; business days per the agency calendar").
2. Write a data collection plan (template in Section 13).
3. Validate the measurement system:
   - For continuous data (times, amounts): Gage R&R or, more often in government, a data audit comparing system timestamps to file evidence for a random sample.
   - For attribute data (decisions, pass/fail, error/no error, category coding): attribute agreement analysis (Section 6).
4. Collect baseline data: enough to see the process over time (at least 20-25 subgroups or periods for a control chart where possible).
5. Plot the data over time first (run chart or I-MR chart), then distributions (histogram, box plot), then capability.
6. Stratify: by office, reviewer, type, complexity, channel, month, applicant type.
7. Compute baseline capability and sigma level if specification limits exist.
8. Refine the problem statement and goal with real data.
9. Tollgate review.

Data reality in government: many systems record the date of entry, not the date of receipt; status codes are overloaded; workarounds live in spreadsheets; free-text fields hold the real reason codes. Plan for manual normalization. VEC capacity modeling required reconciling data from multiple legacy systems and a vendor-managed call center platform with significant manual normalization [Summary]. Prairie View's lesson was to gather timeliness data automatically from the ERP rather than manual spreadsheets, which were error-prone and lagged [Summary].

### 4.4 Analyze, step by step

1. Brainstorm potential causes with the team (fishbone using 6Ms or the service version: People, Policy, Procedures, Places, Systems, Measurement, Environment, Inputs).
2. Prioritize potential causes (cause-and-effect matrix, multi-voting).
3. Analyze the process: value stream map, value-added analysis, interference diagram, handoff and loop count (see lean.md).
4. Analyze data:
   - Pareto of defect or deficiency reasons. Prairie View: Pareto showed the majority of late payments were driven by a small number of recurring causes such as missing receiving documents or incorrect invoice addresses [Summary]. Columbus ROW permitting applied the 80/20 rule to permit revisions in a prototype dashboard [Summary].
   - Stratification and comparison across offices, reviewers, or types.
   - Hypothesis tests to confirm differences are real (Section 7).
   - Correlation and regression to quantify relationships.
5. Verify root causes: each verified cause has data or a test showing it drives Y. Use 5 Whys to reach system-level causes, not people.
6. Quantify the impact of each verified cause.
7. Tollgate review.

### 4.5 Improve, step by step

1. Generate solutions for each verified root cause (benchmark peers, Lean principles, Full-Kit, standard work, mistake-proofing, automation after cleanup).
2. Select solutions using a criteria matrix (impact on CTQ, cost, time, legal feasibility, staff acceptance, risk).
3. Run an FMEA on the future-state process.
4. Pilot: small scope, defined duration, defined measures, defined success criteria, before/after comparison.
5. Analyze pilot data statistically (Section 7). Confirm improvement is real, not noise.
6. Plan full implementation (project-management.md) and the change approach (change-management.md).
7. Tollgate review.

### 4.6 Control, step by step

1. Write the control plan (Section 11).
2. Put control charts in place for key Ys and critical Xs, with an owner and a review cadence.
3. Write the response (reaction) plan: what happens when a chart signals.
4. Standardize: SOPs, standard work, checklists, system configuration, training.
5. Mistake-proof the highest-risk failure modes.
6. Validate benefits with finance or the budget partner (mark as validated vs estimated).
7. Hand over to the process owner; sign-off.
8. Lessons learned and replication opportunities.
9. Schedule post-closure reviews (30/60/90 days, quarterly).

### 4.7 Tollgate review checklist

```
Phase: ______  Project: ______  Date: ______
[ ] Deliverables for this phase complete (list)
[ ] Data sources documented; data quality issues disclosed
[ ] Conclusions supported by evidence (no unsupported claims)
[ ] Scope still valid; changes approved
[ ] Risks and issues reviewed
[ ] Stakeholder communication current
[ ] Benefits estimate updated and labeled (estimate vs validated)
[ ] Next phase plan and resources confirmed
Decision: [ ] Proceed  [ ] Proceed with conditions  [ ] Rework  [ ] Stop
Sponsor signature: ______
```

---

## 5. DMADV and Design for Six Sigma

Use DMADV (Define, Measure, Analyze, Design, Verify) when there is no existing process to improve or the current process cannot meet requirements even when optimized: a new grant program, a new statutory mandate, a new agency function, or a system replacement where the agency must design the future process first.

| Phase | Purpose | Tools |
|---|---|---|
| Define | Goals, scope, customers, risk | Charter, multi-generational plan |
| Measure | Customer requirements and CTQs; benchmark | VOC, Kano analysis, QFD (house of quality), benchmarking |
| Analyze | Develop and evaluate design concepts | Functional analysis, Pugh concept selection, TRIZ, high-level design capability estimates |
| Design | Detailed design | Detailed process maps, standard work, system requirements, FMEA, simulation |
| Verify | Pilot and validate; transition | Pilot, capability study, control plan, handoff |

Public-sector examples from the RAG:
- Clean Energy Fund of Texas (EPA Solar for All grant): building an audit-ready grant administration entity from a conceptual phase, designing an equitable application process, and establishing internal controls able to scale with a rapid influx of capital [Summary]. This is effectively a DMADV design problem. Confirm with David before external use.
- WY DEQ multi-division work designed requirements for a new information system (WYIMS) alongside future-state maps [Summary], and Santa Clara Valley Water produced requirements for Cityworks and OnBase [Summary]. "Clean before automating" is the Design phase rule: design the process, then configure the system.
- CalGEM was transitioning operations into a new IT system (WellSTAR) while lacking consistent SOPs across headquarters and three districts [Summary]; the Encyclopedia of SOPs is a design artifact that also reduced district-to-district variability.

Kano model for public services (expert knowledge): basic needs (correct decision, legal compliance) cause dissatisfaction when missing but no delight when present; performance needs (speed, clarity) scale satisfaction; delighters (status notifications, a single checklist up front) exceed expectations. Basic needs must be secured first.

Pugh matrix: list criteria as rows, concepts as columns, a datum concept, and score each as better (+), same (S), or worse (-). Iterate by combining strengths.

---

## 6. Measurement system analysis (MSA)

### 6.1 Why it matters in government

If two reviewers looking at the same file reach different decisions, the "process data" partly measures reviewer differences, not the process. Eligibility, enforcement, inspection, and quality assurance decisions all depend on human judgment. CalGEM's drive to a unified well-permit review standard across three districts addressed exactly this kind of district-to-district variability [Summary]; the SD Attorney General appellate work addressed variability in how briefs were constructed and reviewed [Summary].

### 6.2 Continuous data: Gage R&R

Components:
- Repeatability (equipment variation): same appraiser, same item, repeated measurement.
- Reproducibility (appraiser variation): different appraisers, same items.
- Part-to-part variation: real differences among items.

Typical study: 10 items, 3 appraisers, 2-3 trials, randomized and blind.

Acceptance guidelines (AIAG):
- %GRR (study variation) under 10%: acceptable.
- 10-30%: may be acceptable depending on application and cost.
- Over 30%: unacceptable; fix the measurement system.
- Number of distinct categories (ndc) at least 5.

In transactional settings continuous "gages" are often timestamps. Replace the classic Gage R&R with a timestamp validation audit:
1. Pull a random sample of 30-50 records.
2. For each, compare the system timestamp for the start and stop events with documentary evidence (email receipt, scanned date stamp, signed decision).
3. Compute the difference; report the bias (mean difference) and spread.
4. Decide whether the field is usable as is, usable with correction, or unusable.

### 6.3 Attribute agreement analysis

Use when outcomes are categories: approve/deny, complete/incomplete, error type, risk class, priority bucket.

Procedure:
1. Select 20-50 items (files) with a known "standard" answer set by an expert panel; include a realistic mix including borderline cases.
2. Have each appraiser assess each item twice, blind and in random order, separated in time.
3. Compute:
   - Within-appraiser agreement (does each person agree with themselves?).
   - Between-appraiser agreement (do people agree with each other?).
   - Appraiser vs standard (are people right?).
   - Kappa statistics (Fleiss' kappa for multiple appraisers; Cohen's kappa for two).
4. Interpret kappa: above 0.9 excellent; 0.7-0.9 acceptable for many uses; below 0.7 needs improvement. (Some texts use 0.75 as the acceptability threshold.)
5. Improve: clarify criteria, create decision aids and exemplars, calibrate in group sessions, re-test.

Kappa formula (Cohen): kappa = (Po - Pe) / (1 - Pe), where Po is observed agreement and Pe is agreement expected by chance.

Worked example (hypothetical example): two eligibility reviewers assess 50 files. They agree on 42 (Po = 0.84). Reviewer A says "eligible" on 30 files (0.60), Reviewer B on 28 (0.56). Pe = (0.60 x 0.56) + (0.40 x 0.44) = 0.336 + 0.176 = 0.512. Kappa = (0.84 - 0.512) / (1 - 0.512) = 0.328 / 0.488 = 0.67. Interpretation: agreement beyond chance is marginal; criteria and calibration need work before eligibility error rates can be trusted.

Public-sector uses: QA review scoring, inspection checklists, case classification (Class A/B investigations), triage buckets (Minnesota Lottery procurement buckets [Summary]; Greeley's three-bucket legal work framework [Summary]), and audit sampling.

### 6.4 Calibration session script

"We'll each review the same five files independently, then compare. When we disagree, we'll not argue who is right; we'll find the criterion that was unclear and rewrite it so the next reviewer gets the same answer. Our goal is the same decision on the same facts, regardless of who reviews it or which office it lands in."

---

## 7. Statistics toolkit

### 7.1 Data types and the first question

| Data type | Examples | Summary | Charts |
|---|---|---|---|
| Continuous (variable) | Days, hours, dollars, counts per case where large | Mean, median, standard deviation, percentiles | Histogram, box plot, run chart, I-MR |
| Discrete count | Errors per file, complaints per week | Rate per unit | c or u chart |
| Proportion (binomial) | Percent late, percent complete, percent first-time-go | Proportion | p or np chart |
| Ordinal | Survey ratings, priority levels | Median, distribution | Bar chart |
| Nominal | Reason codes, offices, types | Counts | Pareto |

First question with any data: plot it over time. Many conclusions change once you see trends, shifts, seasonality, or a data-entry change.

### 7.2 Descriptive statistics essentials

- Mean: sum divided by n. Sensitive to outliers.
- Median: middle value. Use for skewed government cycle times (almost always right-skewed).
- Standard deviation (s): sqrt(sum((x - mean)^2) / (n - 1)).
- Percentiles: report the 50th, 85th or 90th, and 95th for service promises. "Most applicants get a decision in 12 days" is less honest than "half get a decision in 12 days, and 9 in 10 within 41 days."
- Range and interquartile range.
- Coefficient of variation: s / mean.

### 7.3 Normality and skew

Cycle times are bounded at zero and skewed right. Do not assume normality. Options: use medians and percentiles; use nonparametric tests; transform (log, Box-Cox) for capability; use a distribution fit (lognormal, Weibull) for capability on non-normal data. Check with a normal probability plot and the Anderson-Darling test.

### 7.4 Sampling

- Random sampling for audits and baselines; stratified random sampling when offices or types differ.
- Systematic sampling (every kth record) is acceptable if no periodicity exists.
- Sample size for estimating a proportion: n = (Z^2 x p x (1 - p)) / E^2. With 95% confidence (Z = 1.96), p = 0.5 (worst case), and margin E = 0.05: n = (3.8416 x 0.25) / 0.0025 = 384. With E = 0.10: n = 96. For small populations, apply the finite population correction: n_adj = n / (1 + (n - 1) / N).
- Worked example (hypothetical example): an agency has N = 600 closed cases last quarter and wants a 95% confidence, plus or minus 10% estimate of the error rate. n = 96; n_adj = 96 / (1 + 95/600) = 96 / 1.158 = 83 files.
- Sample size for estimating a mean: n = (Z x s / E)^2. If s = 20 days and E = 5 days: n = (1.96 x 20 / 5)^2 = 61.5, so 62.
- Data for control charts: rational subgroups (for example cases decided per week) and at least 20-25 subgroups.

### 7.5 Hypothesis testing decision tree

State H0 (no difference) and Ha. Choose alpha (usually 0.05). Check assumptions. Run the test. Report the p-value and the practical significance (effect size). A statistically significant difference may not matter operationally, and a non-significant result with a small sample is not proof of no difference.

| Question | Data | Test | Nonparametric alternative |
|---|---|---|---|
| Is the mean different from a target? | Continuous, one group | One-sample t | One-sample Wilcoxon / sign test |
| Are two groups' means different? | Continuous, two independent groups | Two-sample t (Welch) | Mann-Whitney U |
| Before vs after on the same items | Continuous, paired | Paired t | Wilcoxon signed-rank |
| Are 3 or more groups' means different? | Continuous, k groups | One-way ANOVA | Kruskal-Wallis |
| Are medians different (skewed times)? | Continuous, k groups | Mood's median | (is itself nonparametric) |
| Are variances different? | Continuous | F-test (2 groups), Bartlett's | Levene's |
| Is a proportion different from a target? | Proportion | One-proportion test | Exact binomial |
| Are two proportions different? | Proportion, two groups | Two-proportion z test | Fisher's exact (small counts) |
| Are categorical variables related? | Counts in a table | Chi-square test of independence | Fisher's exact |
| Is Y related to X? | Continuous Y and X | Correlation, regression | Spearman rank correlation |
| Is a binary outcome related to Xs? | Binary Y | Logistic regression | |

Worked example, two proportions (hypothetical example): before a Full-Kit checklist, 66 of 200 applications were first-time-go (33%). During a pilot, 52 of 100 were (52%). Pooled p = 118/300 = 0.393. SE = sqrt(0.393 x 0.607 x (1/200 + 1/100)) = sqrt(0.2386 x 0.015) = sqrt(0.003579) = 0.0598. z = (0.52 - 0.33) / 0.0598 = 3.18; p is about 0.0015. The improvement is statistically significant; confirm it is sustained on a p chart. (The 33% baseline echoes the type of figure seen in the OWBC CEAP summary but this calculation is purely illustrative.)

Worked example, medians (hypothetical example): review times for two offices are skewed. Use Mood's median or Mann-Whitney rather than a t-test, and report medians and 90th percentiles side by side.

Errors to avoid:
- Running many tests and reporting the one significant result (multiple comparisons; adjust with Bonferroni or use ANOVA with post-hoc tests).
- Ignoring the time order of data (autocorrelation).
- Comparing a pilot month with a different season's baseline without considering seasonality.
- Confusing correlation with causation; confirm with a pilot or designed experiment.

### 7.6 Correlation and regression

- Pearson r measures linear association (-1 to +1). r^2 is the share of variance explained.
- Simple linear regression: Y = b0 + b1 X. Check residuals (normal, constant variance, independent).
- Multiple regression: Y = b0 + b1 X1 + b2 X2 + ... Watch multicollinearity (variance inflation factor above 5-10 is a warning).
- Logistic regression for binary outcomes (late or on time, approved or denied); report odds ratios with care when the outcome is a legally sensitive decision.
- Government caution: regression on decisions that affect individuals (eligibility, enforcement, sentencing) can reveal disparate impact. Treat findings involving protected characteristics as sensitive; route to legal review; never draw conclusions about individuals.

Example of a capacity relationship (from the RAG): VEC contact-center analysis looked at the relationship between average handle time and calls transferred to Tier 2, to ensure faster calls were not simply creating downstream rework [Summary]. That is a metric-tension analysis that can be formalized as a correlation or regression with a time lag.

### 7.7 Design of experiments (DOE)

Use when several factors may influence the outcome and you can deliberately set them (for example form version, notification timing, triage rule, reviewer assignment method).
- Full factorial 2^k: every combination of k factors at two levels. 3 factors = 8 runs.
- Fractional factorial 2^(k-p): screening many factors with fewer runs, accepting confounding of higher-order interactions (resolution III, IV, V).
- Randomize run order; replicate; block on nuisance variables (office, week).
- Analyze main effects and interactions; Pareto of effects; confirm with a validation run.

Government practicality: full DOE is rare because processes cannot be "set" freely, legal fairness rules apply, and volumes per week are modest. Practical alternatives:
- A/B tests of letters, forms, or reminder messages (randomize applicants to version A or B where legally and ethically allowed; obtain approval).
- Stepped pilots by office (each office adopts the change at a different time; compare).
- Simulation (Sandbox exercises, capacity models). VEC's cohort capacity model tested a hypothetical 10% capacity improvement at the adjudication constraint to show a measurable backlog reduction [Summary]; that is a model-based experiment rather than a DOE.

---

## 8. Process capability, sigma level, DPMO

### 8.1 Definitions and formulas

- Defect: any failure to meet a CTQ requirement.
- Unit: the item processed (an application, a case, a permit, an invoice).
- Opportunity: a distinct chance for a defect on a unit (define carefully and conservatively; inflating opportunities inflates the sigma level).
- DPU (defects per unit) = total defects / total units.
- DPO = total defects / (units x opportunities per unit).
- DPMO = DPO x 1,000,000.
- Yield: first-pass yield (FPY) = units passing a step without rework / units entering. Rolled throughput yield (RTY) = product of FPY across steps. RTY approximates e^(-DPU) for small defect rates.
- Sigma level (short-term, with the 1.5 shift convention) = NORMSINV(1 - DPO) + 1.5.

| Sigma level | DPMO (with 1.5 shift) | Yield |
|---|---|---|
| 1 | 691,462 | 30.9% |
| 2 | 308,538 | 69.1% |
| 3 | 66,807 | 93.3% |
| 4 | 6,210 | 99.38% |
| 5 | 233 | 99.977% |
| 6 | 3.4 | 99.99966% |

### 8.2 Worked example: first-time-go as a sigma level (hypothetical example)

An intake unit receives 1,000 applications; 330 are complete on first submission. Treat each application as one unit with one opportunity (complete or not). DPO = 670 / 1,000 = 0.67. NORMSINV(0.33) = -0.44. Sigma level = -0.44 + 1.5 = 1.06. A 33% first-time-go rate is roughly a one-sigma process. Raising first-time-go to 80% gives NORMSINV(0.80) + 1.5 = 0.84 + 1.5 = 2.34 sigma. Communicate this honestly: transactional government processes often start between 1 and 3 sigma, and the goal is mission performance, not a sigma label.

### 8.3 Worked example: rolled throughput yield (hypothetical example)

Four steps with first-pass yields of 0.90 (intake), 0.80 (technical review), 0.95 (supervisory review), 0.85 (issuance). RTY = 0.90 x 0.80 x 0.95 x 0.85 = 0.581. Only 58% of permits pass all steps without rework, even though every step individually looks "mostly fine." This is a powerful way to show leadership the hidden factory of rework and deficiency loops.

### 8.4 Capability indices

For continuous data with specification limits:
- Cp = (USL - LSL) / (6 sigma_within). Potential capability if centered.
- Cpk = min[(USL - mean) / (3 sigma_within), (mean - LSL) / (3 sigma_within)]. Actual capability accounting for centering.
- Pp and Ppk use overall (long-term) standard deviation instead of within-subgroup.
- One-sided spec (typical in government: a maximum days limit): Cpk = (USL - mean) / (3 sigma).
- Benchmarks: Cpk at least 1.33 is commonly called capable; 1.0 means the process just fits; below 1.0 means defects are expected.
- Process must be stable (in statistical control) before capability means anything.

Worked example (hypothetical example): permit review days have mean 22 and within-subgroup standard deviation 6; USL = 30 days. Cpk = (30 - 22) / (3 x 6) = 8 / 18 = 0.44. Expected share beyond 30 days if normal: z = 8/6 = 1.33, so about 9% late. If the data is right-skewed, the true late share will be higher; use a lognormal fit or simply count the actual percent beyond 30 days.

Practical advice: for skewed cycle times, report the actual percent beyond the standard and the 90th percentile alongside any Cpk; leaders understand "1 in 11 permits is late" better than "Cpk 0.44."

### 8.5 Cost of poor quality (COPQ) in government

Categories:
- Internal failure: rework, deficiency letters, re-reviews, corrections, duplicate data entry, re-notification (the LMO A3 noted premature landowner notification causing costly re-notification, per the BOK A3).
- External failure: appeals, complaints, legislative inquiries, audit findings, litigation, improper payments, public safety consequences.
- Appraisal: inspections, QA reviews, audits, reconciliations.
- Prevention: training, standard work, Full-Kit checklists, system edits.

Express COPQ in staff hours, calendar days for the public, risk events, and dollars only where defensible. Use QT/OE (see lean.md and theory-of-constraints.md) for the value side: (0.95 x 100) / 9,800 = 0.0097 quality units per dollar, about $103 per quality unit, in the BOK paper's illustration.

---

## 9. Statistical process control (SPC)

### 9.1 Control chart selection

| Data | Subgroup | Chart |
|---|---|---|
| Continuous, individual values (one case at a time, or one value per period) | n = 1 | I-MR (individuals and moving range) |
| Continuous, small subgroups | n = 2-9 | X-bar and R |
| Continuous, larger subgroups | n of 10 or more | X-bar and S |
| Defectives (pass/fail), varying subgroup size | n varies | p chart |
| Defectives, constant subgroup size | n constant | np chart |
| Defects (counts) per unit, constant area of opportunity | constant | c chart |
| Defects per unit, varying area of opportunity | varies | u chart |
| Rare events (time between events) | | t chart or g chart |
| Small shifts matter | | EWMA or CUSUM |

Rule of thumb for transactional government data: the I-MR chart (also called the XmR or process behavior chart, Wheeler) handles most situations: weekly median cycle time, weekly backlog, monthly error rate as a single number.

### 9.2 Formulas

I-MR:
- Center line (CL) = mean of individual values (X-bar).
- MR-bar = mean of moving ranges |Xi - Xi-1|.
- UCL_X = X-bar + 2.66 x MR-bar; LCL_X = X-bar - 2.66 x MR-bar.
- UCL_MR = 3.267 x MR-bar.

p chart:
- p-bar = total defectives / total inspected.
- UCL, LCL = p-bar plus or minus 3 x sqrt(p-bar (1 - p-bar) / n_i).

c chart: CL = c-bar; limits = c-bar plus or minus 3 x sqrt(c-bar).
u chart: CL = u-bar; limits = u-bar plus or minus 3 x sqrt(u-bar / n_i).
X-bar and R (subgroup n): UCL = X-double-bar + A2 R-bar; LCL = X-double-bar - A2 R-bar; R limits D3 R-bar and D4 R-bar. For n = 5: A2 = 0.577, D3 = 0, D4 = 2.114.

Worked example, I-MR (hypothetical example): weekly backlog counts over 10 weeks: 120, 126, 118, 131, 124, 129, 122, 135, 127, 130. Mean = 126.2. Moving ranges: 6, 8, 13, 7, 5, 7, 13, 8, 3; MR-bar = 70 / 9 = 7.78. UCL = 126.2 + 2.66 x 7.78 = 146.9; LCL = 105.5. No point is outside the limits: the backlog is stable at about 126 with routine weekly variation of about plus or minus 21. Reacting to a single week's rise from 122 to 135 would be tampering. To reduce the backlog, the system must change (capacity at the constraint, demand shaping, Full-Kit).

### 9.3 Special-cause rules (Western Electric / Nelson, simplified)

1. One point beyond 3-sigma limits.
2. Two of three consecutive points beyond 2 sigma on the same side.
3. Four of five consecutive points beyond 1 sigma on the same side.
4. Eight (some texts use seven or nine) consecutive points on one side of the center line.
5. Six points in a row steadily increasing or decreasing.
6. Fourteen points alternating up and down.
Use rules 1, 4, and 5 as a minimum in government dashboards; more rules raise false alarms.

### 9.4 Control limits are not specification limits

Control limits are the voice of the process; specification limits (the 30-day ordinance standard) are the voice of the customer. A process can be stable and incapable (predictably late). Never draw a target line and call it a control limit.

### 9.5 Recalculating limits

Recalculate after a verified, intentional process change (use a staged chart: before and after the change). Do not recalculate to make signals disappear.

### 9.6 SPC in public-sector dashboards

- Put control charts behind the dashboard KPIs so leaders see signal vs noise.
- Pair each speed chart with a quality chart (metric tension). Prairie View's prototype dashboard showed metric tension between Net30 timeliness and overall quality [Summary]; Minnesota Lottery's dashboard tracked speed and quality (compliance or correct bucket) to ensure speed did not compromise audit readiness [Summary].
- Annotate charts with events (system go-live, statute change, staffing changes, seasonal surges).
- Report by the period that matches decision cadence (weekly for operations, monthly for leadership).
- Teach leaders two questions: "Is this a signal or noise?" and "If noise, what system change do we need?"

---

## 10. Root cause and risk tools

### 10.1 Fishbone (Ishikawa)

Service categories: People, Policy (statute, rule, guidance), Procedures, Places (offices, channels), Systems (IT), Measurement, Environment (demand, politics, season), Inputs (applications, data from other agencies). Write the effect as a measurable problem statement in the head. Brainstorm; then circle candidates for verification. (See also the fishbone-analysis skill if loaded.)

### 10.2 5 Whys

Ask why until the answer is a system cause the team can act on. Rule: if the answer is a person ("Sam made a mistake"), ask why the system allowed that mistake. Verify each link with evidence. (See the 5why-root-cause skill if loaded.)

Example from the BOK LMO A3 (summarized): variable review times traced to no standardized process, no internal timeline target, and no communication gate, which a 5-Whys chain can reach from "operators complain about delays."

### 10.3 Pareto analysis

Sort categories by frequency or impact; plot bars and the cumulative percent line; focus on the vital few (often about 20% of causes drive about 80% of the effect, but do not force the 80/20 ratio). Weight by impact when frequency and severity differ (a rare deficiency that causes a 60-day delay may outrank a frequent one that costs a day).

### 10.4 Stratification and multi-vari

Split the data by office, reviewer, shift, application type, complexity, channel, and month. Multi-vari charts show whether variation is mostly within units, between units, or over time; this points to where to look for causes.

### 10.5 Cause-and-effect (C&E) matrix

Rows: process inputs (Xs). Columns: CTQs weighted by importance. Score each X's relationship to each CTQ (0, 1, 3, 9). Sum weighted scores; top Xs go into FMEA and data collection.

### 10.6 FMEA

Columns: process step; potential failure mode; potential effect; severity (S, 1-10); potential cause; occurrence (O, 1-10); current controls; detection (D, 1-10); RPN = S x O x D; recommended action; owner; date; revised S, O, D, RPN.

Rules:
- Address high severity first regardless of RPN (severity 9-10 usually means harm to people, legal violation, or loss of rights). AIAG-VDA (2019) replaces RPN with action priority (AP) for this reason.
- Do not game the scores. Calibrate scales with examples relevant to the agency.
- In government, severity anchors should include legal and due-process consequences, public safety, improper payment, and loss of public trust.

Example scale anchors for severity (government service):

| Score | Effect |
|---|---|
| 10 | Harm to a person, or loss of legal rights, without warning |
| 9 | Statutory violation or improper payment discovered externally |
| 7-8 | Wrong decision reaching the customer; appeal likely |
| 5-6 | Significant delay beyond the statutory clock |
| 3-4 | Rework or delay within the statutory clock |
| 1-2 | Minor inconvenience, no customer impact |

Hypothetical FMEA row (court warrant processing): step "enter booking data"; failure mode "booking data missing required fields"; effect "case cannot be docketed; defendant held without timely appearance"; S 9; cause "no data standard at booking"; O 6; controls "clerk calls officer"; D 5; RPN 270; action "data standard with time limit and officer training." Compare the Albany municipal court recommendation of a 2-hour booking procedure, with officers trained before 1 August 2021 per the recommendations report [Verified-deck].

### 10.7 Mistake-proofing in service processes

Prevention (cannot be done wrong): required fields, drop-downs, validation rules, auto-population from authoritative sources (SD BOR onboarding form auto-complete [Summary]), checklists embedded in the form. Detection (caught immediately): system edits on submission, Full-Kit check at the Front Door, automated completeness flags. See lean.md Section 12.

---

## 11. Control plan

Template:

| Process step | CTQ or critical X | Specification or target | Measurement method | Sample size and frequency | Who measures | Where recorded | Control method (chart, checklist, system edit) | Reaction plan (what, who, how fast) |
|---|---|---|---|---|---|---|---|---|
| Intake screening | First-time-go rate | At least [target]% | System report | All applications, weekly | Intake lead | Dashboard | p chart | Signal: review rejected reasons within 2 business days; update checklist or guidance |
| Technical review | Days Full-Kit to decision | USL [N] days | Timestamps | All, weekly median and 90th percentile | Supervisor | Dashboard | I-MR | Signal: check WIP and staffing; escalate to manager at huddle |
| Decision QA | Decision accuracy | At least [target]% | QA sample | [n] files per month (Section 7.4) | QA reviewer | QA log | p chart, calibration | Below target: calibration session within 2 weeks |

Elements:
- Owner signature (process owner, not the belt).
- Training records and SOP links.
- Review cadence (huddles, monthly leadership review).
- Audit of the control plan itself (is it used?).
- Linkage to leader standard work (lean.md Section 8).

Response plan principle: every signal has a named responder, a time limit, and a documented action. A chart with no reaction plan is decoration.

---

## 12. Lean Six Sigma integration

| Issue | Lean answer | Six Sigma answer | Combined LSS approach |
|---|---|---|---|
| Long lead time | Remove waits, batches, handoffs | Reduce variation in steps that cause queues | Map flow, then attack the variation at the constraint |
| High rework | Full-Kit, standard work, poka-yoke | Verify root causes of the top defect categories | Pareto, verify, mistake-proof, control chart |
| Inconsistent decisions | Standard work, visual criteria | Attribute agreement, calibration | Standard + calibration + QA sampling |
| Too many metrics | Measure What Matters | Operational definitions, MSA | A few CTQ metrics with SPC and metric tension |
| Backlog | Pull, WIP limits | Capability of processing times; predict clearance | Capacity model and control charts on WIP |

GQI-aligned LSS roadmap for a government engagement:
1. Define with GQI Charter It and Vision It (Strategic Compass = CTQ framework).
2. Measure with Map It (Value Stream SOP with data), plus data validation.
3. Analyze with Gap It (interference diagram plus Pareto, stratification, tests).
4. Improve with Build It (future state, pilots, FMEA).
5. Control with Launch It and Track It (standard work, dashboards with SPC, BRAG, 30/60/90).

Variation and flow interact (queueing theory): the more variable arrivals and service times are, the longer queues get at a given utilization. Kingman's approximation: average wait is roughly [(ca^2 + cs^2) / 2] x [u / (1 - u)] x average service time, where ca and cs are the coefficients of variation of arrivals and service, and u is utilization. Reducing variation (Six Sigma) shortens queues without adding staff; running a reviewer near 100% utilization makes waits explode, regardless of effort. This is also why the Albany docket work concluded a docket should not be "perfectly" scheduled: over-scheduling protects against statistical fluctuations in defendant attendance; the 133% figure was a recommendation [Target].

Day and Zimmermann (a federal munitions production contractor): ReEngine delivered seminars featuring the Bead Game, a simulation of how statistical fluctuations and dependent events create bottlenecks [Summary]. Use this kind of simulation to teach leaders why variation plus dependency, not effort, creates backlogs.

---

## 13. Templates

### 13.1 Project charter (DMAIC)

```
Project title:
Business case (why now; link to strategic goal or statute):
Problem statement (what, where, when, how big, vs what standard):
Goal statement (metric, from baseline to target, by date):
Primary metric (Y) and operational definition:
Secondary / counter-balancing metrics (metric tension):
Scope: start event, stop event; in scope; out of scope
Customers and CTQs:
Team: sponsor, champion, process owner, belt, members, data steward
Milestones: Define, Measure, Analyze, Improve, Control tollgates (dates)
Estimated benefits (labeled estimate): hours, days, error rate, QT/OE
Risks and constraints (legal, labor, IT, data):
Approvals:
```

### 13.2 Data collection plan

| Metric | Operational definition | Data type | Source (system, field) | Sample plan | Collection period | Collector | Stratification factors | Known data issues | MSA plan |
|---|---|---|---|---|---|---|---|---|---|

### 13.3 Check sheet (manual collection, 2-4 weeks)

| Date | Case ID (or anonymized) | Type | Received complete? (Y/N) | Missing item(s) | Hand-offs count | Notes |
|---|---|---|---|---|---|---|

### 13.4 Root cause verification log

| Potential cause | Source (fishbone, interview, data) | Verification method | Evidence (cited) | Verified? (Y/N/partial) | Impact estimate |
|---|---|---|---|---|---|

### 13.5 Solution selection matrix

| Solution | Root cause addressed | Impact on CTQ (1-5) | Cost (1-5, 5 = low) | Time to implement (1-5) | Legal and policy feasibility (1-5) | Staff acceptance (1-5) | Risk (1-5, 5 = low) | Weighted total |
|---|---|---|---|---|---|---|---|---|

### 13.6 Pilot plan

```
Change being piloted:
Scope (office, type, volume, dates):
Hypothesis: If we [change], then [Y] will move from [baseline] to [target] because [root cause].
Measures (primary, secondary, counter-balancing):
Success criteria and statistical test:
Risks and safeguards (legal clocks protected; fallback):
Communication to affected customers and staff:
Decision at end: adopt / adapt / abandon
```

### 13.7 Benefits validation

| Benefit | Baseline (source, period) | After (source, period) | Method | Validated by | Status (estimate / validated) |
|---|---|---|---|---|---|

### 13.8 Tollgate summary (one page)

```
Phase completed:
Key findings (with evidence references):
Decisions requested:
Risks / issues:
Next steps and dates:
```

---

## 14. Metrics for Six Sigma projects and programs

Project-level:
- Primary Y with baseline, target, and post-improvement values (with statistical test).
- Process capability (percent beyond standard, 90th percentile, Cpk or sigma level where appropriate).
- First-pass yield and rolled throughput yield.
- DPMO or error rate per unit.
- COPQ in hours and, where real, dollars.
- QT/OE change (quality units delivered per operating expense).
- Measurement system adequacy (kappa, %GRR, timestamp bias).

Program-level (portfolio):
- Projects chartered, completed, and sustained at 6 and 12 months.
- Average days per DMAIC phase (tollgate cycle time).
- Benefits validated vs estimated.
- Belts trained and certified; projects per belt.
- Control plans audited and in use.
- Replication: number of other units adopting a proven solution.

Sustainment check (ReEngine BRAG): track recommendations Blue, Green, Amber, Red. The NH VR focus-group BRAG with 46 observations across 6 groups showed 19.6% Red and 26.1% Blue or Green [Summary]; such snapshots show where control is weak. Do not rush items to Blue.

---

## 15. ReEngine past-engagement parallels (Six Sigma lens)

Cite in this form: "Comparable to the <client> engagement (<years>), where <situation>; ReEngine <action> [tag]." Use only these or verified RAG content.

| Situation pattern (variation, data, defects) | Engagement | What ReEngine did | Evidence status |
|---|---|---|---|
| District-to-district variability in a regulatory program | CalGEM (2021-23) | Encyclopedia of SOPs (18+ high-level SOPs); unified well-permit review standard across three districts; "document to delegate" | Standardization across districts [Summary] |
| Averages hide outliers that saturate capacity | NH Vocational Rehabilitation (2021-23) | "Old Dogs" review to interrogate the outliers | 83% of cases met the 60-day eligibility window; outliers averaged 840 days in services; some cases open over 7,300 days [Summary] |
| A few recurring causes drive most late payments | Prairie View A&M (2021) | Pareto in a prototype dashboard; metric tension between Net30 and quality; department-level certified purchasing SMEs | Targets of 3 business days for fully kitted POs and 10 for contracts under $100k [Target]; "Payments Exceeding Net30" chart framework [Summary]. Confirm with David before external use (Texas state university) |
| Top revision reasons drive permit rework | City of Columbus ROW Permitting (2020-21) | 80/20 dashboard of permit revisions; Full-Kit vetting | 51% cycle-time improvement and 46% rework reduction at 3-year follow-up [Summary] |
| Speed metric could hide downstream rework | Virginia Employment Commission (via Accenture) | Correlated average handle time with Tier 2 transfers; WGLL targets per phase (e.g., 1 week intake, 3-5 weeks adjudication); cohort capacity model | Throughput ~2,000 new and ~6,500 continued claims per week analyzed [Summary]; hypothetical 10% constraint capacity test in the model |
| Inconsistent appellate brief construction and review | SD Attorney General (2022) | Standardized brief construction and review | Variability addressed via standard work [Summary] |
| Variable review times, no internal target | WY DEQ LQD, LMO (BOK A3 and RAG) | Standard criteria; O-G-P review targets 5/10/20 working days; 90-day policy review | Outliers over 100 days in current condition (BOK A3); 100% LMO annual report automation path [Summary]; 20% supervisor triage reduction [Target] |
| Low first-time-go baseline | OWBC CEAP (2022-23); MaineHousing HEAP (2019) | Full-kit vs incomplete cycle comparisons; pre-screening | About 57 vs 90 days, 33% first-time-go [Summary]; about 35% first-time-go [Summary]. Confirm with David before external use |
| Speed vs compliance in procurement | Minnesota State Lottery (2023) | Dashboard tracking speed and quality (correct bucket) | PO cycle 3.5 days simplest vs 74 days most complex [Summary] |
| Teaching variation and dependency | Day and Zimmermann (federal munitions production contractor) | Bead Game simulation | Seminars delivered [Summary] |
| Over-reporting without decision value | SD Department of Corrections (2018-19) | Measure What Matters; information requirements | 87 slides to about 13 [Verified-deck] |

Never present a Target as a result. Never merge numbers across engagements. Texas state agency and housing or energy-assistance examples: confirm with David before external use.

---

## 16. Integration with the other four methodologies

- Lean (lean.md): Lean maps flow and removes waste; Six Sigma verifies causes and controls variation. In ReEngine GQI, Map It and Gap It use both. Use Lean first when waste is obvious; use Six Sigma when causes are contested or data must convince oversight bodies.
- Theory of Constraints (theory-of-constraints.md): TOC selects where Six Sigma matters most: reduce variation at the constraint and in the flow feeding it (buffer protection). A Six Sigma project at a non-constraint may improve local quality without improving system throughput; prioritize defects that consume constraint capacity (rework that returns to the scarce reviewer is doubly costly). Buffer management data (penetration into red) is an excellent Y for DMAIC.
- Project management (project-management.md): DMAIC tollgates are phase gates; charter, schedule, risk register, and change control apply. In government contracts, map DMAIC deliverables to contract deliverables and acceptance criteria.
- Change management (change-management.md): Statistical findings do not change behavior by themselves. Plan ADKAR for reviewers whose decisions will be calibrated; prepare people managers to discuss variation without blame; reinforce with recognition for following standard work.

Specialist-synthesizer pattern: the Six Sigma specialist posts at most three findings per run, each anchored to a cited artifact, such as "Review-time data shows bimodal distribution by office (cited: data extract 2026-10-20, tab 3); recommend stratified comparison before attributing to staffing."

---

## 17. Decision guides

### 17.1 Do we need Six Sigma here?

| Signal | Use Six Sigma? |
|---|---|
| Cause is obvious and agreed; fix is simple | No; just do it (kaizen) |
| Cause is contested among managers or offices | Yes; verify with data |
| Outcome varies widely and unpredictably | Yes; SPC and stratification |
| Decisions inconsistent across reviewers | Yes; attribute agreement and calibration |
| Oversight body requires proof | Yes; baseline, test, control chart |
| Data does not exist | Collect with a check sheet first; do not fake rigor |
| Problem is one step limiting throughput | TOC first, then Six Sigma at the constraint |

### 17.2 Which chart?

Continuous one-at-a-time: I-MR. Percent defective: p. Counts of defects: c or u. Small persistent shifts: EWMA. When unsure in transactional work: I-MR of the weekly metric.

### 17.3 Which test?

See Section 7.5. If data is skewed cycle time, default to medians and nonparametric tests. If counts are small (expected cell under 5), use exact tests.

### 17.4 DMAIC or DMADV?

Existing process that can meet requirements once improved: DMAIC. New program, new mandate, or redesign from scratch: DMADV. Unsure: run Define and Measure, then decide.

### 17.5 How much statistics should the report show?

Leaders and elected officials: plain-language conclusion, one chart, one sentence on confidence. Technical appendix: method, test, assumptions, p-values, data caveats. Auditors: full method and data lineage.

---

## 18. Facilitation scripts and questions

Opening data conversation:
"We're not here to grade anyone. Data tells us how the system behaves. If the numbers surprise us, that's useful; it means we've found something to learn."

Operational definitions:
"When we say a case is 'received,' what exactly happens and where is it recorded? If two of us counted the same week, would we get the same number?"

Signal vs noise for leaders:
"This chart shows the backlog has moved between about 105 and 147 for months. Last week's 135 is within that range; it's normal noise. Reacting to it would be like steering a car on every bump. If we want a lower backlog, we need to change the system."

Calibration:
"Let's each score these five files privately. Now reveal. Where we differ, let's find the words in the criteria that let us read it two ways."

When someone challenges the data:
"That's a fair challenge. What would we need to see to be confident? Let's pull 30 records and check them against the files together."

When the group wants to blame one office:
"Office B's times are longer. Before we conclude anything, what's different about what Office B receives: case mix, complexity, staffing, systems?"

Pilot design:
"What would convince you, as a skeptic, that this change worked? Let's write that down now as the success criterion before we see any results."

Questions bank:
- What does the customer consider a defect here?
- What is the standard, and where does it come from (statute, rule, policy, practice)?
- What happens to the case when it fails?
- Where does rework return to? Is that the busiest person?
- What changed in the data system in the last two years?
- Which cases are the outliers, and what do they have in common?
- Who decides, and do they decide the same way?

---

## 19. Common pitfalls

1. Statistics theater: complex analysis on bad data. Validate the measurement system first.
2. Ignoring time order: histograms and averages without run or control charts.
3. Assuming normality on skewed cycle times.
4. Tampering: reacting to common-cause noise with individual blame or new rules.
5. Confusing control limits with targets or specs.
6. Calling a correlation a root cause without verification.
7. Too many projects, too few champions; projects stall between tollgates.
8. Belts trained but no projects or coaching afterward.
9. Benefits overstated or not validated; claiming a Target as a result.
10. Over-counting opportunities to inflate sigma levels.
11. Optimizing local quality at a non-constraint while system throughput is unchanged.
12. Ignoring legal fairness when experimenting on members of the public. A/B tests must be approved and must not deny rights.
13. Analyzing decisions about individuals in ways that create disparate impact or privacy risk; route to legal review.
14. Control plan written but not owned; charts not reviewed.
15. Failing to explain results in plain language; leaders tune out.

---

## 20. Application to ReEngine engagements and proposals

### 20.1 Typical scope items in public-sector solicitations

- LSS training and belt certification (VA Lean SOW in the BOK lists belt training, MSA, DOE, SPC, CCPM, Hoshin and A3 among required capabilities).
- Rapid improvement events and DMAIC projects with tollgate reviews.
- Data analysis and performance dashboards.
- Process capability assessment and baseline studies.
- QA program design (sampling, calibration, error tracking).
- Audit remediation (NH VR addressed all 46 audit observations through process designs [Summary]).

### 20.2 Draft proposal language (David edits; do not add claims)

Approach paragraph (draft):
"ReEngine integrates Six Sigma within its Government Quality Improvement (GQI) method to ensure recommendations rest on verified root causes rather than opinion. During Map It, we will establish operational definitions and validate data sources for key measures such as [cycle time, first-time-go rate, decision accuracy]. During Gap It, we will use Pareto analysis, stratification across [offices, case types], and appropriate statistical tests to verify the causes that drive performance. In Track It, we will install control charts and a control plan so [Agency] leaders can distinguish real change from routine variation and respond quickly when performance drifts."

Data limitations paragraph (draft):
"Where system data are incomplete, ReEngine will use short, structured manual data collection and file sampling (with documented sample sizes and confidence levels) to establish a defensible baseline. All figures in our deliverables will be labeled with their source and period."

QA and consistency paragraph (draft):
"Because [eligibility, enforcement, inspection] decisions depend on professional judgment, ReEngine will conduct an attribute agreement study and calibration sessions to measure and improve decision consistency across reviewers and offices, comparable to ReEngine's work establishing a unified permit review standard across three districts in the CalGEM engagement [verify wording with David]."

Staff qualifications sentence (draft, from CORE_METH_Staff-Certifications): "ReEngine's team includes Lean Six Sigma Black Belt and Master Black Belt practitioners." Verify names and credentials with David for each submission.

### 20.3 Deliverables to propose

Charter; SIPOC and CTQ tree; data collection plan; MSA or attribute agreement report; baseline capability report; root cause verification log; pilot report with statistics; control plan; dashboard with SPC; benefits validation; training materials.

---

## 21. Agent instructions and guardrails

1. Draft only. Do not send, submit, or publish analyses or proposals.
2. Never fabricate data, results, p-values, or charts. If you lack data, design the data collection plan and stop.
3. Show your work: every statistic in a deliverable lists data source, period, n, method, and assumptions.
4. Label hypothetical examples. Label RAG figures with the evidence tag. Never upgrade a Target.
5. Use plain-language summaries for executives, with the technical detail in an appendix.
6. Do not compute results on personally identifiable data outside approved environments. Anonymize case IDs in drafts.
7. Flag legal sensitivity: analyses touching protected classes, enforcement decisions, eligibility denials, or employee performance require human legal or HR review before sharing.
8. Prefer simple valid methods over complex ones. State why a test was chosen.
9. When using code (Python, R) on the box to compute statistics, save the script and the output with the draft so a human can re-run it.
10. When the local model or another agent proposes a statistic, check the formula and the arithmetic before including it.
11. Respect read-only sources (BOK and RAG). Never modify them.
12. Engagement-synopsis Six Sigma specialist prompt: "Report at most three findings on variation, defects, data quality, or measurement. Each: observation; why it matters for the CTQ; cited artifact; suggested analysis or next step; whether it advances the charter objective; one genuinely comparable past engagement from Section 15 if applicable."

---

## 22. Glossary

- Alpha: probability of a Type I error (false positive), usually 0.05.
- ANOVA: analysis of variance; tests differences among three or more means.
- Attribute agreement analysis: measures consistency and accuracy of categorical judgments.
- Beta: probability of a Type II error (false negative); power = 1 - beta.
- Black Belt, Green Belt, Yellow Belt, Master Black Belt: levels of Six Sigma training and role.
- Capability (Cp, Cpk, Pp, Ppk): comparison of process spread and centering to specifications.
- Common cause: variation inherent to the system.
- COPQ: cost of poor quality.
- CTQ: critical-to-quality requirement.
- DMAIC: Define, Measure, Analyze, Improve, Control.
- DMADV: Define, Measure, Analyze, Design, Verify.
- DOE: design of experiments.
- DPMO: defects per million opportunities.
- DPU: defects per unit.
- FMEA: failure mode and effects analysis.
- FPY, RTY: first-pass yield; rolled throughput yield.
- Gage R&R: repeatability and reproducibility study.
- I-MR: individuals and moving range chart.
- Kappa: agreement statistic correcting for chance.
- Kano model: classification of customer needs into basic, performance, and delighters.
- MSA: measurement system analysis.
- Operational definition: precise, measurable definition of a metric.
- p-value: probability of observing data at least as extreme as observed if H0 is true.
- Pareto: ordered bar chart for prioritizing causes.
- Pugh matrix: concept selection against a datum.
- QFD: quality function deployment (house of quality).
- RPN: risk priority number (S x O x D).
- SIPOC: Suppliers, Inputs, Process, Outputs, Customers.
- Special cause: assignable variation from a specific event.
- SPC: statistical process control.
- Tampering: adjusting a stable process in response to common-cause noise.
- Tollgate: phase-end review and decision point.
- VOC, VOP: voice of the customer; voice of the process.
- Y = f(X): outcome as a function of inputs.

---

## 23. References

ReEngine BOK (Shared Drive, read-only): Six Sigma subfolder: Knowles, Six Sigma handbook (general information); Zailani and Ramayah, Six Sigma and Organizational Knowledge; Hummour (2018), TQM in municipalities (Jordan, empirical); Breyfogle, IEE DMAIC Roadmap Define-phase figure 9.4 (titles identified; not read in full). Read: Maleyeff (2007), Improving Service Delivery in Government with Lean Six Sigma, IBM Center for The Business of Government; Fryer, Antony, and Douglas (2007), Critical success factors of continuous improvement in the public sector, The TQM Magazine 19(5); VA Lean Work Description (sample SOW); EPA Lean Government Implementation Guide (2017); Example A3 Problem Solving ReEng Format (LMO A3); Rother, Improvement Kata Handbook, Target Condition; Mycue and Schragenheim, Unique Features of Government (TOCICO BOK paper); DoD Continuous Process Improvement Guidebook (2006).

ReEngine RAG (read-only): Past Project Performance Reports #001-#044; CORE_METH_Main-Master-Logic; CORE_METH_4-Pillars-Framework; CORE_METH_BRAG-Tool-Logic; CORE_METH_Staff-Certifications.

Standard literature (expert knowledge): ASQ Certified Six Sigma Black Belt Body of Knowledge; Pyzdek and Keller, The Six Sigma Handbook; Breyfogle, Implementing Six Sigma and Integrated Enterprise Excellence; Montgomery, Introduction to Statistical Quality Control; Wheeler, Understanding Variation; Deming, Out of the Crisis; Shewhart, Economic Control of Quality of Manufactured Product; George, Lean Six Sigma for Service; AIAG, Measurement Systems Analysis Reference Manual (4th ed.); AIAG-VDA FMEA Handbook (2019); Kano et al. (1984), Attractive quality and must-be quality; Hopp and Spearman, Factory Physics (Kingman's equation).
