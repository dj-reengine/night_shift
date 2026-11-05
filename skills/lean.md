---
name: lean
description: Use when an agent is planning, facilitating, analyzing, documenting, or proposing Lean work for a public-sector client (courts, corrections, municipal permitting and public works, environmental regulators, utilities, state agencies, higher-education systems, public authorities). Covers TPS roots, the five Lean principles, the 8 wastes (DOWNTIME) translated for government offices, value stream mapping (current, future, and ideal state), flow, pull, takt, kaizen events, 5S (physical and digital), standard work, A3, gemba, visual management, heijunka, SMED, poka-yoke, Lean metrics (lead time, PCE, %C&A, first-time-go), facilitation agendas and scripts, templates, pitfalls, ReEngine GQI alignment, proposal methodology language, and integration with Six Sigma, TOC, project management, and change management. Practitioner depth; draft-only guardrails.
---

# Lean for Public-Sector Process Improvement (Practitioner Skill)

Owner context: ReEngine Consulting LLC (Leander, TX), a small public-sector process-improvement consultancy. The principal is certified in Lean, Six Sigma (Black Belt level and above), Theory of Constraints (Jonah), PMI PMP, and Prosci change management. This skill is written at practitioner depth for AI agents that support ReEngine proposals and client engagements. It assumes the reader already knows what Lean is; it exists to make the agent apply Lean the way an experienced government Lean practitioner would, and to keep the agent from fabricating data, results, or quotes.

All work produced under this skill is a DRAFT for David's review. Nothing is sent, submitted, posted, or presented to a client by an agent.

---

## 0. When to use this skill (and when not to)

Use this skill when any of the following is true:

- A solicitation (RFP, RFQ, RFO, SOQ request) asks for process improvement, Lean, Lean Six Sigma, kaizen, rapid improvement events, value stream mapping, business process reengineering, operational assessment, efficiency study, or SOP development.
- An active engagement needs a kaizen agenda, a current-state or future-state value stream map, a waste analysis, standard work, an A3, a 5S plan, a visual-management design (Journey Board, takt board, huddle board), or a 30/60/90-day implementation follow-up.
- A transcript, email, or work product from an engagement mentions backlogs, rework, handoffs, missing information at intake, long waits, "detective work," duplicate data entry, approvals that pile up, or staff saying "we have always done it this way."
- A client asks how to "do more with the same staff," "reduce turnaround times," "get ahead of the backlog," or "prepare our process before the new system goes live."
- The specialist-synthesizer engagement-synopsis worker needs the Lean lens to produce a short finding anchored to a cited artifact.

Do not use this skill alone when:

- The core problem is variation in an outcome that must be measured and modeled statistically (use six-sigma.md alongside).
- The core problem is a single resource or policy limiting the whole system, a chronic conflict, or a backlog that will not drain no matter how much local waste is removed (use theory-of-constraints.md first; Lean is then used to exploit and subordinate).
- The ask is primarily schedule, scope, budget, deliverable acceptance, or contract compliance (use project-management.md).
- The ask is primarily about adoption, resistance, sponsorship, or communications (use change-management.md).

In practice ReEngine engagements combine all five. Section 17 explains the integration.

---

## 1. Source basis for this skill

ReEngine body-of-knowledge (BOK) documents on the ReEngine Shared Drive that were read for this skill (read-only):

- LEAN BOK / Lean at the EPA - Resources: "Lean Govt Implement Guide - EPA 2017.pdf" (EPA Lean Government Initiative, Lean Government Implementation Guide, September 2017). Drawn on for the PDCA eight-step problem-solving framework, the three components of a rapid improvement event, the 30/60/90-day report-out structure, the backsliding curve, and the implementation step sequence (Set up for success; Develop an implementation plan; Complete and track actions; Measure and evaluate results; Standardize and socialize; Celebrate and share; Manage change and avoid pitfalls). The folder also contains "EPA's Lean Handbook.pdf" and "Logic Models (Yvonne Watson).pptx".
- LEAN BOK / A3 1-Pagers - Format & Examples: "Example A3 Problem Solving ReEng Format.pptx" (ReEngine A3 format, worked on a Limited Mining Operations review process). Drawn on for the ReEngine A3 template in Section 9.
- LEAN BOK / Gemba-walks & discussions: "Gemba_Walks.pdf" (A Guide to Successful Gemba Walks). Drawn on for the gemba-versus-MBWA distinction, question set, and keys to a successful walk.
- LEAN BOK / Target Conditions - Rother et al: "Target Conditions Presentation by Rother.pdf" (Improvement Kata Handbook excerpt). Drawn on for target-condition definitions in Section 13.
- LEAN BOK / Lean RFPs - typical: "VA Lean Work Description020-03-03-27.docx" (a federal Lean Six Sigma sensei statement of work). Drawn on for what public buyers typically specify.
- LEAN BOK: "Cont-Impr_in_public_sector_Anthony021-02-21.pdf" (Fryer, Antony, Douglas 2007, Critical success factors of continuous improvement in the public sector). Drawn on for public-sector differences (multiple domains, unclear customers).
- LEAN BOK: "improving-service-delivery-in-in-government-with-lean-six-sigma.pdf" (Maleyeff 2007, IBM Center for The Business of Government). Drawn on for service-environment adaptations (cross-functional flow, task variability, handoffs, hidden costs, terminology).
- LEAN BOK / Lean Books, Articles & Other Resources: "Night of Long Knives-Pub_Servants & Change & Lean.pdf" (Ratner 2012) and "Elegant Solutions" (Matthew May) excerpt. Drawn on for pitfalls about Lean dividing workforces.
- LEAN BOK / SIPOC tools & aids: "SIPOC Template.pptx"; LEAN BOK / PDCA: "PDCA image".
- Continuous Improvement BOK: "DoD Continuous Process Improvement CPI Guidebook May 2006.pdf", "Lexicon Development021-01-07.pptx" (listed; used for vocabulary discipline).
- TOC Body of Knowledge: "06-bok_paper_on_government_uniq.pdf" (Mycue and Schragenheim, Unique Features of Government and How Governance Could be Assisted by TOC). Drawn on for QT/OE and government characteristics that shape Lean.

ReEngine RAG (past-project vault, read-only) material drawn on:

- 03_ReEngineIP/Methodology_CI: CORE_METH_Main-Master-Logic.md (GQI 7-phase method: Charter It, Vision It, Map It, Gap It, Build It, Launch It, Track It; Improvement Week Kaizen and Solution Session formats), CORE_METH_4-Pillars-Framework.md (Strategic Compass, Journey Board, Value-Stream SOPs, Dashboards and Scoring; binding elements Purpose, Focus, Value), CORE_METH_Strategic-Path-Logic.md, CORE_METH_BRAG-Tool-Logic.md.
- ReEngine Past Project Performance Reports (aggregated past-performance summaries #001 to #044) and 05_ProjectSummaries.
- Box extracts: story_bank_from_RAG_2026-11-04.md and albany_detail_from_RAG.md, which flag which figures were verified against final decks and which are summary-only.

Evidence discipline used throughout this file: a past-engagement figure is cited only if it appears in the RAG. Figures are tagged as follows.

- [Verified-deck]: the RAG extract states the figure was checked against the final client deck or report.
- [Summary]: the figure appears in the RAG past-performance summary but was not confirmed against the final deliverable. Verify before external use.
- [Target]: the figure was a goal or projection, not an achieved result. Never present it as achieved.

---

## 2. Core concepts at practitioner depth

### 2.1 Roots: Toyota Production System and what transfers to government

The Toyota Production System (TPS) rests on two pillars, Just-in-Time (make only what is needed, when needed, in the amount needed) and Jidoka (build quality in; stop and fix abnormalities at the source), on a foundation of standardized work, heijunka (leveled production), and kaizen (continuous improvement), all held together by respect for people. Taiichi Ohno's core move was to look at the timeline from order to cash and shrink it by removing non-value-adding time. Lean Thinking (Womack and Jones) generalized TPS into five principles.

What transfers well to government:

- The timeline view. A permit, claim, case, license, inspection, grant application, or public records request has a start (receipt) and an end (decision, issuance, closure). Most of the elapsed time is waiting. The Lean move is the same.
- Jidoka as "quality at the source." In government this is the "Front Door" or "Full-Kit" principle: do not let an incomplete application, case file, or request enter the value stream. ReEngine has applied this in almost every engagement (see Section 16).
- Standard work. Public organizations are rules-based but often lack documented standard work; the rules exist, the way to apply them does not.
- Respect for people. Public servants are mission-driven. ReEngine's 4-Pillars document frames the binding element "Purpose": staff who see management validate their sense of purpose begin to improve on their own.

What transfers poorly and must be adapted:

- "Customer pull." Government cannot refuse demand and often cannot control it (Mycue and Schragenheim, fourth characteristic: government cannot control demand). Pull must be redesigned as WIP control inside the agency, not as refusing work.
- "Value is what the customer will pay for." Government has multiple customers with competing definitions of value (the applicant, the public at large, the legislature or council, the funding source, the courts, the auditor). See 2.3.
- Inventory as visible material. Office inventory is invisible: emails, queues in case-management systems, folders on shared drives, voicemails. Making it visible is the first job.
- Speed as the dominant metric. In regulation, enforcement, and justice, speed can never come at the cost of due process, chain of custody, environmental protection, or legal defensibility. ReEngine's WY DEQ Coal lesson: "Don't sacrifice quality for timeliness... the focus must be on flow, not speed-at-any-cost." Pittsburgh Police lesson: "Subordinate to the Chain of Custody."

### 2.2 The five Lean principles, government-translated

| Principle | Classic definition | Public-sector translation | Practitioner check question |
|---|---|---|---|
| 1. Specify value | Define value from the customer's perspective | Define the quality unit of public value (a "goal unit" or quality throughput, QT) and what makes it "quality" (on time, complete, correct, legally defensible, equitable) | "What exactly does this process produce, and what makes one unit good?" |
| 2. Identify the value stream | Map all steps, VA and NVA, from request to delivery | Map the full cross-agency stream, including other departments, other governments (county, state, federal), vendors, and the applicant's own steps | "Where does the clock really start for the applicant, versus where we start counting?" |
| 3. Make value flow | Eliminate interruptions, batching, rework | Eliminate deficiency loops, queues for signature, batching for weekly meetings, sequential reviews that could run concurrently | "What would it take for a complete file to move from step to step without waiting?" |
| 4. Establish pull | Produce only on downstream signal | Release work into a constrained review stage only when it has capacity; hold incomplete work at the front door; limit WIP per reviewer | "Who decides when work starts, and is it started because someone is ready or because it arrived?" |
| 5. Pursue perfection | Continuous improvement, never done | Daily management, standard work that is revised, 30/60/90-day reviews, Track It dashboards, kata | "Who owns the process after we leave, and what routine makes them look at it weekly?" |

### 2.3 Value in government: multiple customers and quality throughput

Fryer, Antony, and Douglas (BOK) note that public organizations suffer a "lack of clarity about who their customers are" and operate across policy, managerial, and professional domains with different values. A Lean practitioner resolves this before mapping, not during.

Customer classes to list in every SIPOC and charter:

1. Direct recipient: applicant, permittee, defendant, claimant, inmate, student, resident.
2. Statutory customer: the law, rule, or court order that the output must satisfy.
3. Funding source: federal grantor, legislature, council, ratepayers.
4. Oversight: auditors, inspectors general, courts, elected officials, the media.
5. Internal downstream: the next unit that receives the output (Records, Legal, Finance).
6. The public at large: the "commons" protected by regulation.

ReEngine's Strategic Compass (Vision It phase) is the tool that resolves this. It identifies the primary value produced, the major stages of the process, the core bottleneck, and the definition of What Good Looks Like (WGLL). The Compass is the "north star" that the Lean tools serve.

QT/OE (Quality Throughput over Operating Expense) is ReEngine's value metric and is grounded in the TOC BOK paper by Mycue and Schragenheim. Q is a quality percentage (on time, first-time-go, error-free), T is the count of goal units, OE is all operating expense for the period. The inverse is cost per quality unit. Worked example from the BOK paper: 100 case determinations at 95 percent quality with OE of 9,800 dollars gives QT/OE = (0.95 x 100) / 9,800 = 0.0097, so cost per quality unit is about 103 dollars. The paper warns against equating cost with value: knowing a civil-rights investigation costs about 4,500 dollars on average does not mean it is worth 4,500 dollars. Use QT/OE for comparison over time and across options, never as a statement of public worth.

### 2.4 Muda, mura, muri

- Muda (waste): activity that consumes resources without adding value.
- Mura (unevenness): fluctuation in demand or workload, for example a permit surge before construction season, a benefits surge after a layoff event, a legislative-session spike in information requests, a snow event.
- Muri (overburden): pushing people or systems beyond capacity, for example a 200 percent workload on a three-person traffic review team (Columbus Traffic Impact Studies [Summary]).

Practitioner point: government offices often attack muda while mura and muri are the root cause. Leveling (heijunka) and WIP control often produce more benefit than removing individual waste steps. TOC thinking reinforces this.

### 2.5 The 8 wastes (DOWNTIME), translated for government offices

| Waste | Definition | Public-sector examples | Typical countermeasures |
|---|---|---|---|
| D - Defects | Errors, rework, deficiency loops | Incomplete applications returned to applicant; denial for missing documentation then appeal; brief returned for formatting; permit issued for an impassable route; reopened tickets | Full-Kit intake checklist; pre-screening; required fields; poka-yoke on forms; standard review criteria; MOU on study parameters |
| O - Overproduction | Doing more, or earlier, than needed | 87-slide monthly metrics decks nobody acts on; full review of simple cases; reports produced "in case"; mid-event status reports during storms | Measure what matters; tiered review by complexity; eliminate reports without an owner and a decision |
| W - Waiting | Idle time between steps | Signature queues; waiting for another department's comments; waiting for a weekly meeting; files waiting for a records clerk; judge waiting for a case file | Concurrent review; delegated authority; batch standing orders; daily stand-ups; parallel bonding and review |
| N - Non-utilized talent | Not using people's skills and ideas | Engineers doing administrative coordination; attorneys triaging simple questions; senior leaders assigning every request; frontline staff never asked | Role specialization (coordinator roles); triage by paralegals; delegation; idea systems; kaizen participation |
| T - Transportation | Moving work, files, or people unnecessarily | Paper files carried between buildings; evidence transported by mail cars; wet-ink routing; emailing attachments through five inboxes | Digital routing; single source of truth; reassign transport to the point of origin; e-signature |
| I - Inventory | Work in queues, backlogs, aged cases | Court backlog of several thousand cases; aged rehabilitation cases at 7,000+ days; unread inbox queues; paper permits awaiting digitization | Visual WIP; WIP limits; aged-case reviews ("Old Dogs"); cumulative flow diagrams |
| M - Motion | Unnecessary movement of people or clicks | Searching multiple systems for booking data; toggling between five applications; walking to printers for wet signatures; hunting on shared drives | 5S of digital workspace; integration; knowledge cards; templates |
| E - Extra processing | More work than the customer or rule requires | 100 percent certification review for simple cases; verifying documents the statute does not require; duplicate data entry into two systems; re-keying from PDFs | Line-by-line review of requirements against statute and rule; self-attestation with back-end audit; risk-based review; "clean before automating" |

ReEngine terms that map onto the wastes (use them in ReEngine work products because clients have learned them):

- Red Steps: non-value-adding steps flagged red on a Value Stream SOP. Example: SD Legislative Research Council motion-sheet redesign targeted elimination of 9 Red Steps, and the future-state flow had 0 Red Steps and a 55 percent automation rate [Summary].
- Full-Kit: everything a reviewer needs to complete work without stopping. Originates in TOC (Goldratt's full-kit concept); ReEngine applies it as Lean jidoka at intake.
- First Time Go: percent of submissions complete and correct on first submission (a first-pass-yield measure). MaineHousing HEAP baseline was estimated at 35 percent [Summary]; OWBC CEAP baseline 33 percent [Summary].
- Deficiency loop: a backward flow to fix incomplete or incorrect work.
- Bad Circle Back: a case or item that returns to a decision-maker's queue unnecessarily.
- Detective work: staff time spent finding missing information.
- WWADI: "We've always done it (this way)," the cultural form of waste.
- Late-hit comments: review comments arriving after a design or decision is supposedly settled (Columbus 3P, Santa Clara Valley Water).
- Front Door: intake, the point where most quality is won or lost.

### 2.6 Value-added classification in a regulated environment

Classify each step as:

- VA (customer value-added): transforms the item toward the output, the customer would want it, done right the first time. In government, "customer" includes the statutory customer.
- RNVA or BVA (required non-value-added, business value-added): required by statute, rule, court order, grant condition, or audit standard, but not valued by the direct recipient. Examples: public notice periods, statutory comment windows, conflict-of-interest checks, debarment checks, chain-of-custody logging.
- NVA (non-value-added, Red Step): neither.

Practitioner rules:

1. RNVA is not untouchable. Ask "required by what, exactly?" and get the citation. MaineHousing: a line-by-line review of every required document against federal and state regulation found items that could move to self-attestation or third-party verification [Summary]. Many "requirements" are local policy or habit.
2. If the requirement is real, minimize its time and effort: run it in parallel, automate it, template it, move it earlier.
3. Never classify a due-process step as NVA in a client-facing document without the client's legal counsel reviewing the classification. Use RNVA and propose minimization instead.

---

## 3. Lean metrics and the math behind them

### 3.1 Definitions

| Metric | Definition | Notes for government |
|---|---|---|
| Lead time (LT) | Elapsed time from request received to output delivered | Distinguish the customer clock (applicant's first contact) from the agency clock (official receipt) and the statutory clock (which may stop during deficiency periods). Report all three when they differ. |
| Process time (PT), also touch time | Time someone actually works on the item | Collect by sampling or time studies; staff estimates are biased. ReEngine uses O-G-P (Optimistic, Goal, Pessimistic) time boxes in workshops. |
| Wait time | LT minus PT | Usually the large majority of lead time in office processes. |
| Process cycle efficiency (PCE) | PT / LT | Office processes commonly show single-digit PCE. Do not promise a target PCE; use it diagnostically. |
| Percent complete and accurate (%C&A) | Percent of times the downstream step receives the input usable as-is | Collect from the receiving step. |
| Rolled %C&A | Product of %C&A across steps | Shows how small defect rates compound. Five steps at 90 percent gives about 59 percent. |
| Throughput (TH) | Completed units per period | Use quality throughput (QT): count only units meeting the quality definition. |
| WIP | Units started but not finished | Includes items "pending applicant." Make it visible. |
| Takt time | Available work time / customer demand in the same period | Meaningful only when demand is reasonably stable or leveled. |
| Cycle time (CT) | Time between completions at a step (or average time per unit at a step) | Compare CT to takt. Define it in the charter because the term is used loosely. |
| First Time Go (FTG) | Percent of submissions complete on first submission | ReEngine's core intake metric. |
| Reopen or rework rate | Percent of closed items reopened or reworked | Pair with closures to create metric tension. |
| Aging | Distribution of open items by age | Interrogate the outliers. |
| QT/OE | Quality throughput per dollar of operating expense | See 2.3. |

### 3.2 Little's Law

Average lead time = Average WIP / Average throughput (for a stable system over the same period).

Worked example (hypothetical, label as an example in any draft): a permitting unit has 450 open applications and issues 90 per week. Average lead time is 450 / 90 = 5 weeks. If the unit holds throughput at 90 per week and reduces active WIP to 270 by holding incomplete applications at the Front Door in a "pending completion" status outside the active queue, average active lead time drops to 3 weeks. The applicant's total time does not necessarily drop unless the deficiency is fixed faster; report both.

Implications:

- To reduce lead time you must reduce WIP or increase throughput. Most office improvements reduce WIP.
- Starting everything immediately raises WIP and lengthens lead time, the "bad multitasking" ReEngine documented at SD BIT.
- Little's Law also lets you estimate lead time when timestamps are poor: count WIP on a given day and count completions over a period.

### 3.3 Takt time in an office

Takt = net available work time per period / demand per period.

Worked example (hypothetical): 4 reviewers, each 6.5 productive hours per day after meetings and breaks, 5 days per week, gives 130 reviewer-hours per week. Demand is 260 reviews per week. Takt is 130 hours / 260 = 0.5 hours, or 30 minutes per review. If average review effort is 42 minutes, capacity is short by about 40 percent and no amount of encouragement will hold the line. Options: reduce effort per review (standard work, full-kit, templates), reduce demand on reviewers (screen out incomplete files, delegate simple types), add capacity, or level the demand.

ReEngine's Journey Board breaks annual targets into weekly per-person rates, which is takt expressed for managers. From the 4-Pillars document: an annual target of 1,200 permits becomes 100 per month; with two teams, 50 per team per month or about 12.5 per week; with four people per team, about 3 to 4 per person per week. Leaders can see in February whether the year is on track.

Takt variants used in government:

- Seasonal takt: compute separately for peak and off-peak (snow season, energy assistance season, legislative session, construction season).
- Takt by work type: when complexity varies, compute takt per bucket (Greeley's three-bucket legal work framework; Minnesota Lottery's six procurement buckets).
- Docket takt: courts schedule by session capacity. Albany's capacity model compared current docket closures per court day against a target and computed annual capacity versus demand and backlog (model documented in the final deck; the figures are projections and contain internal inconsistencies noted in the RAG extract, so cite the model, not the numbers).

### 3.4 Clock definitions that must be in every charter

- Start event: what starts the clock (first contact, receipt, complete-application date, assignment)?
- Stop event: decision, issuance, mailing, closure in the system?
- Pause rules: does the clock stop when waiting on the applicant?
- Business days or calendar days?
- Exclusions: withdrawn, transferred, or consolidated items.

Minnesota childcare licensing illustrates the "Official Starting Line": the licensing clock should start only when a full-kit application is submitted, preventing staff time on unvetted concepts [Summary]. WY DEQ LQD-URP established 60-day completeness and 150-day technical review milestones [Summary].

---

## 4. Value stream mapping (VSM) in the public sector

ReEngine calls its swim-lane map a "Value Stream SOP": it maps the current state, assesses each step's value contribution, and becomes the backbone of the future-state SOP, tying together procedures, checklists, templates, and examples (4-Pillars, Pillar 3).

### 4.1 Scoping the value stream

1. Name the product family: a group of items that follow mostly the same steps (for example "residential right-of-way permits, utility type"). Do not map "all permits" in one event.
2. Define start and stop events using Section 3.4.
3. Identify the process owner (one person accountable end to end) and the sponsor.
4. Build a SIPOC first (template in Section 15).
5. Decide the level: Level 1 (5 to 9 boxes, the Strategic Compass view), Level 2 (swim-lane by role, 25 to 60 steps), Level 3 (work instructions, only where standard work is needed).
6. Check the political scope: does any step belong to another elected official's office (clerk of court, county attorney, sheriff)? If so, get that office's agreement to participate or mark the step as an external interface.

### 4.2 Data to collect per step (the data box)

| Field | Meaning | Collection method |
|---|---|---|
| Step name (verb-noun) | "Review site plan," not "Engineering" | Workshop |
| Role or lane | Who does it | Workshop |
| System | Which application or medium | Workshop or system walk |
| Process time (O-G-P) | Optimistic, Goal (typical), Pessimistic hands-on time | Workshop estimates, then sample timing |
| Wait before step | Queue time | System timestamps if available; otherwise WIP count and Little's Law |
| %C&A of input | Percent usable as received | Ask the receiving role; sample files |
| Volume | Items per period through this step | System reports |
| Staff and availability | FTE and percent of time on this process | Manager interview |
| Batch size and frequency | For example "weekly review meeting" | Workshop |
| Value class | VA, RNVA (with citation), NVA (Red Step) | Team classification |
| Decision point | Yes or no | Workshop |
| Pain points | Interference items | Interference diagram |

### 4.3 Current-state mapping procedure (workshop)

1. Walk the process (gemba or virtual gemba, Section 10) before the workshop where possible.
2. Post the SIPOC and Strategic Compass draft.
3. Map the happy path left to right with sticky notes (or digital whiteboard), one note per step, verb-noun.
4. Add lanes by role (applicant, intake, technical reviewer, supervisor, legal, other department).
5. Add the loops: deficiency letters, resubmittals, appeals, escalations. Use a different color for backward flows.
6. Add data boxes. Mark unknowns with a question mark and assign follow-up data collection; never invent.
7. Draw the timeline ladder: process time on the bottom rung, wait time on the top rung. Sum lead time and process time; compute PCE.
8. Mark Red Steps.
9. Mark the constraint: where does work pile up? (Section 17 and theory-of-constraints.md.)
10. Run the interference diagram (ReEngine Gap It tool): with the people who do the work, list every obstacle to reaching the goal, then group and rank.
11. Validate: read the map back to participants step by step and ask "Is this what really happens, or what the manual says happens?"

### 4.4 Future-state design questions (adapted from Rother and Shook for offices)

1. What is the quality unit of throughput, and what is the takt by work type?
2. Where can work flow continuously from step to step without a queue? Where must there be a queue (FIFO lane, supermarket, pending-completion holding)?
3. What is the single scheduling point (the pacemaker)? In offices it is often intake triage or assignment. Albany's design gave the Court Administrator that role ("chute and ready bench"), with a morning standup setting the order of cases (design documented in the final deck and recommendations report).
4. How will work be leveled across reviewers, days, and types?
5. What is the Full-Kit definition at the Front Door and who verifies it?
6. Which reviews can run concurrently instead of sequentially? (WY DEQ: decouple hydrology from linear review; LMO: run bonding in parallel with LQD review.)
7. Which approvals can be delegated or converted to post-decision audit? (NYSDOT ODO 7-day objection window; Greeley legal-question bucket.)
8. What process improvements are needed before automation? ("Clean before automating": SD Attorney General SOR, WY DEQ Solid Waste.)
9. What standard work, visual management, and metrics will hold the future state?

### 4.5 Ideal state

Optionally map an ideal state with no constraints (MDOT TPU "Ideal State" walkthroughs harvested requirements for the routing system replacement [Summary]). Use it to generate IT requirements and long-term vision, then step back to a future state achievable in 3 to 12 months.

### 4.6 Public-sector VSM conventions

- Show statutory clocks as a separate band beneath the timeline with the citation.
- Show the applicant's own steps as a lane. Applicants cause a large share of delay through incomplete submissions; the fix is usually in agency guidance and forms.
- Show other governments (county, state, federal) as external lanes with dashed boundaries.
- Show systems as icons or a separate lane. Note duplicate entry explicitly.
- Show "pending applicant" as an inventory triangle with its own count.
- For enforcement processes, show the evidence chain and the appeal path (Columbus ROW Enforcement designed every step "with the Appeals Hearing in mind" [Summary]).

### 4.7 VSM pitfalls

- Mapping the manual, not the reality.
- Mapping at the wrong altitude (200 sticky notes for a Level 1 question).
- No data, only opinions. Use O-G-P in the room, then verify with samples.
- Leaving the map on a wall. Convert it to a Value Stream SOP.
- Treating the future state as the deliverable. The implementation plan and the 30/60/90 follow-up are the deliverable.

---

## 5. Flow, pull, takt, and leveling in office and regulatory work

### 5.1 Flow patterns

| Pattern | When to use | Government example |
|---|---|---|
| Single-piece flow | Steps can be done by one person or a cell in sequence | Simple permit types handled start-to-finish by one technician |
| Cell or pod | Several roles must touch each item | Interdepartmental project teams assigned at inception (Columbus 3P) |
| FIFO lane with WIP cap | Queues are unavoidable but should be ordered and capped | Engineering review queue capped at N files per reviewer |
| Triage lanes by complexity | Work types differ greatly in effort | Greeley three buckets: Legal Questions (under 4 hours), Legal Reviews (4 hours to 2 days), Projects Enabled |
| Express lane | A large share of items are simple | Expedited review for simple energy-assistance cases; Minnesota Lottery Bucket 1 (state contract) vs Bucket 4 |
| Concurrent review | Multiple reviewers needed and independent | Parallel department comments with a single due date and an appellate path for conflicts |

### 5.2 Pull in government

Pull means work enters a stage when that stage signals capacity. In government:

- Release work to technical reviewers only when they are below their WIP cap ("Choke and Release" at SD BIT; "Qualified Screening" at Santa Clara Valley Water).
- Hold incomplete items in a pending-completion status at intake rather than starting them (OWBC CEAP "Pending Completion" pivot [Summary]).
- Schedule dockets or inspections to capacity, including expected no-shows (Albany's recommendations proposed scheduling to about 133 percent of capacity to account for failure-to-appear rates of 25 to 40 percent of the docket; the deck recommends it and implementation is not documented, so describe it as a recommendation).

### 5.3 Heijunka (leveling)

Leveling smooths volume and mix. Office techniques:

- Daily intake distribution by type (heijunka box equivalent): a board or system queue allocating a mix of simple and complex items to each reviewer each day.
- Fixed review slots: reserve reviewer hours for a given work type (Santa Clara Valley Water: dedicate engineer hours for CPRU reviews [Summary]).
- Pre-application meetings scheduled on a cadence.
- Surge playbooks: a pre-agreed mode for peaks (WY DEQ target: a 30 percent increase in demand should produce less than a 10 percent increase in delays [Target]).
- Seasonal staffing plans and cross-training matrices.

### 5.4 Batching and its costs

Office batching is common: weekly sign-off meetings, monthly board approvals, end-of-week mailing. Each batch step adds, on average, roughly half the batch interval to lead time. Some batches are good: Albany's "batch standing orders" at end of day consolidated signatures to reduce interruptions to the judge, a constraint resource (recommendation in the deck). Rule: batch at non-constraints to protect the constraint's focus; never batch in front of the constraint in a way that starves it.

### 5.5 Supermarkets and kanban in offices

Kanban in an office is a visual WIP-limited board (see project-management.md for the Kanban method). A supermarket is a small buffer of ready work in front of a constrained reviewer so they are never idle (TOC calls this the constraint buffer). Albany's "chute and ready bench" is a supermarket for the bench: the next case is ready, and the following four are in the chute.

---

## 6. Kaizen events (rapid improvement events) in government

### 6.1 Event types used by ReEngine

| Format | Duration | Covers | Use when |
|---|---|---|---|
| Improvement Week Kaizen (GQI) | 3 to 5 days | All 7 GQI phases | One well-bounded value stream, sponsor committed, data available |
| Solution Session (GQI) | 1 to 2 days | Charter It, Map It, Gap It, plus solution ideas | Discovery, assessment, or when staff time is scarce |
| Series workshops | Several 1.5-day sessions over weeks | Mapping and redesign in stages | Staff cannot leave operations for a week (OWBC CEAP used five 1.5-day sessions [Summary]) |
| Mini-Launch sessions | Half day per program | Localized buy-in and launch | Multi-program agency (WY DEQ multi-division) |
| Tiger Teams | Weeks | Prototype a countermeasure | Specific solution needs build-out (Albany virtual court; MDOT TPU and Bridge; OWBC HR) |
| Sandbox simulation | 1 day | Stress-test a future state with role play and injected curveballs | High-stakes or infrequent operations (Columbus ROW Enforcement; Columbus Snow and Ice) |
| Daily kaizen | Ongoing | Small improvements at huddles | Sustaining culture |

### 6.2 Three phases (EPA Lean Government Implementation Guide)

1. Plan and prepare (2 to 6 weeks before): scope, charter, team, logistics, baseline data, background research, leadership briefing.
2. Event (2 to 5 days): map current state, design future state, implement what can be done in the room, build the implementation plan.
3. Follow-up (90 days or more): implement, verify, and evaluate at 30-, 60-, and 90-day report-outs; standardize, sustain, and share.

The EPA guide's central warning: without follow-up, a Lean effort produces only plans, changes backslide, and further opportunities are missed. The guide's PDCA framework has eight steps: (1) clarify the problem, (2) describe current conditions, (3) set improvement targets, (4) determine root cause, (5) develop countermeasures, (6) enact countermeasures, (7) measure and evaluate results, (8) standardize, sustain, and share success. Build the follow-up into the contract and the schedule.

### 6.3 Event scoping checklist

- [ ] Product family and start and stop events defined.
- [ ] Problem statement with baseline data (or a plan to get it).
- [ ] Measurable target (for example lead time, FTG, backlog) with a date.
- [ ] Sponsor named and available for kickoff and report-out.
- [ ] Process owner named.
- [ ] Out-of-scope items listed (especially statute changes, IT procurement, and HR classification decisions).
- [ ] Team of 6 to 10: people who do the work, one upstream, one downstream, one fresh eye, one IT or data person, process owner. Avoid packing with managers.
- [ ] Union, civil service, or employee-association notification if required (see change-management.md).
- [ ] Open-meetings or public-records implications reviewed (some boards and commissions trigger notice requirements if a quorum attends).
- [ ] Room, wall space, or digital whiteboard; system access for live data pulls.
- [ ] Coverage plan for participants' regular work.
- [ ] Decision rights agreed: what can the team implement without further approval?

### 6.4 Five-day Improvement Week agenda (template)

Day 1 - Charter It and Vision It, then Map It
- 08:30 Sponsor kickoff (why this matters, what is in scope, decision rights, redeployment commitment if the client has made one).
- 09:00 Introductions, norms, parking lot.
- 09:30 Lean and GQI primer, short (45 minutes): value, waste, flow, full-kit, constraint.
- 10:30 Review charter, problem statement, baseline data.
- 11:00 SIPOC and Strategic Compass draft (goal unit, WGLL, major stages).
- 13:00 Gemba or system walk-through.
- 14:30 Current-state mapping begins.
- 16:30 Daily debrief: plus/delta, parking lot review.

Day 2 - Map It and Gap It
- Complete current-state map with loops and data boxes.
- Timeline, PCE, Red Steps.
- Interference diagram; group and rank obstacles.
- Five Whys or fishbone on the top three (see 5why-root-cause and fishbone-analysis skills).
- Constraint identification.
- Sponsor check-in (30 minutes, late afternoon).

Day 3 - Build It
- Future-state design questions (Section 4.4).
- Full-Kit definition and intake checklist.
- Draft standard work for the top changes.
- Visual management design (Journey Board).
- Quick experiments: try the new intake checklist on real files in the room.

Day 4 - Build It and Launch It preparation
- Implementation plan with owners and dates.
- Metrics and dashboard design (Track It).
- Risk review: what could break due process, audit, or legal defensibility? Legal or compliance review of changes.
- Change impact assessment (see change-management.md).
- Draft launch presentation.

Day 5 - Launch It
- Rehearse the report-out.
- Report-out to sponsor and leadership (60 minutes): problem, current state, future state, quick wins done, implementation plan, metrics, asks.
- Sponsor decisions recorded.
- Recognize participants (letters of recognition are cheap and powerful; the Columbus Snow and Ice "What Can We Do Today" roadmap included letters of recognition for auxiliary staff [Summary]).

### 6.5 Two-day Solution Session agenda (template)

Day 1: kickoff, SIPOC, Strategic Compass, current-state map, timeline.
Day 2: interference diagram, root cause on top items, solution ideation, prioritization (impact vs effort, or ReEngine's ROI and risk ranking from Gap It), next steps and decision brief.

### 6.6 Series-workshop agenda (five 1.5-day sessions, template)

| Session | Content | Between sessions |
|---|---|---|
| 1 | Charter, SIPOC, Compass, data plan | Data pull; sample of closed files |
| 2 | Current-state map, timeline, data review | Validate map with absent staff |
| 3 | Interference diagram, root cause, Pareto of deficiency reasons | Test hypotheses on file sample |
| 4 | Future state, Full-Kit, standard work drafts | Pilot checklist on live intake |
| 5 | Implementation plan, metrics, launch deck | Sponsor review |

### 6.7 30/60/90-day follow-up

| Report-out | Focus | Audience | Questions |
|---|---|---|---|
| 30 days | Actions completed vs plan; early metrics; obstacles | Sponsor, process owner, team | Which actions slipped and why? What did we learn from the first month of data? |
| 60 days | Metrics vs baseline; standard work adherence; adjustments | Sponsor, team | Is the new process actually being followed? Where is it being bypassed? |
| 90 days | Results vs target; sustainment plan; next improvement | Leadership | Is the gain holding? Who owns it? What is the next target condition? |

ReEngine's LMO A3 included a "process and policy change review" session 90 days after implementation to confirm the change was taking across all regions and offices. The BRAG tool (Blue, Red, Amber, Green) tracks "improvement velocity" across many action items: Blue complete, Green progressing on track, Amber progressing with difficulty, Red stuck or not started. The BRAG logic warns against rushing to Blue; training-type actions, for example, should complete at least one delivery-and-feedback cycle before being declared complete.

---

## 7. 5S for physical and digital workplaces

5S: Sort, Set in order, Shine, Standardize, Sustain. Many public agencies add Safety as a sixth S.

### 7.1 Physical 5S in government

Applies to evidence rooms, records rooms, fleet garages, maintenance shops, warehouse and supply rooms, field-inspection kits, and court clerk counters. Pittsburgh Police's evidence and property-room work and College Station's fleet and solid-waste work are relevant parallels (the latter used acetated knowledge cards in truck cabs so drivers had immediate access to billing and routing standards [Summary]).

### 7.2 Digital 5S (often more valuable in offices)

| S | Digital practice |
|---|---|
| Sort | Identify duplicate, obsolete, and personal files on shared drives; identify unused system fields and forms; apply the records retention schedule (never delete outside the retention schedule; coordinate with the records officer) |
| Set in order | Standard folder taxonomy by value stream and case number; naming convention (YYYY-MM-DD_case_doc-type_version); one location per document type; links instead of attachments |
| Shine | Remove broken links; fix templates; archive closed matters per retention schedule |
| Standardize | Publish the taxonomy and naming standard; template library; locked templates for letters and notices |
| Sustain | Quarterly digital 5S audit; ownership per folder; onboarding includes the standard |

Parallel: WY DEQ LQD faced interference from legacy paper records and a fragmented document system ("the F-Drive") during an ePermit conversion [Summary]. CalGEM's "Encyclopedia of SOPs" created a structured, hierarchical menu of procedures [Summary].

Guardrail: records management in government is legally controlled. 5S Sort never authorizes destruction. Always route disposition through the records officer and the approved retention schedule.

### 7.3 5S audit checklist (score 0 to 4 each)

- [ ] Only items needed for current work are present (physical or folder).
- [ ] Every item has a labeled home; anyone can find a document in under 30 seconds.
- [ ] Templates are current and locked; no "final_v7_REAL" files.
- [ ] Visual status of work is evident at a glance.
- [ ] Standard is posted and referenced in onboarding.
- [ ] Audit is scheduled and results are posted with trend.

---

## 8. Standard work

### 8.1 Elements

Classic standard work has three elements: takt time, work sequence, and standard WIP. Office standard work adds: inputs required (Full-Kit), decision criteria, templates and systems, quality checks, and escalation rules.

### 8.2 Standard work vs SOP vs work instruction

| Artifact | Purpose | Level |
|---|---|---|
| Policy | What and why, authority | Executive |
| SOP (procedure) | Who does what, when, in what sequence, with controls | Process owner |
| Standard work | The current best method for a task with time and quality expectations; the baseline for improvement | Team |
| Work instruction or job aid | Step-by-step for a single task, often with screenshots | Individual |
| Desk guide, flip book, knowledge card | Quick reference at point of use | Individual |

ReEngine's Value Stream SOP unifies these: the future-state swim-lane is the spine, and procedures, checklists, templates, and examples hang from each step.

Parallels:
- Charlottesville Redevelopment and Housing Authority: 70+ SOPs covering public housing, housing choice voucher, finance, procurement, maintenance, and capital funds; 100 percent documentation coverage of high-risk regulatory workflows [Summary]. Lesson recorded: standard work is risk mitigation; an inconsistent process is a legal liability. Agent note: confirm with David before citing housing and energy-assistance engagements (Charlottesville, MaineHousing, OWBC) in external materials.
- SD Legislative Research Council: Fiscal Training Workbook codified WGLL for bill writing and fiscal notes, reducing reliance on unstructured shadowing [Summary].
- CalGEM: Encyclopedia of SOPs and a how-to framework for staff to maintain it; "Document to Delegate" lesson [Summary].
- SD Department of Education: desk guides and flip books for secretaries and fiscal staff [Summary].

### 8.3 Standard work drafting procedure

1. Start from the future-state map step.
2. Observe the best performer(s) doing it; record steps, key points (what makes it safe, correct, or easy), and reasons.
3. Write steps as verb-object with key points (TWI Job Instruction format).
4. Attach the Full-Kit checklist for inputs and the quality check for outputs.
5. Note the expected time (O-G-P).
6. Pilot with two people who did not write it.
7. Revise, approve by process owner, publish with version and date.
8. Train with TWI JI: prepare, present, try out, follow up.
9. Audit adherence through leader standard work.
10. Improve: standard work is the baseline for the next kaizen, not a monument.

### 8.4 Leader standard work

A recurring routine for supervisors and managers: daily huddle, board review, a gemba visit, a standard-work audit, escalation follow-up, weekly metric review. Without leader standard work, Lean systems decay within months.

| Cadence | Activity | Time | Output |
|---|---|---|---|
| Daily | Tier 1 huddle at the Journey Board | 10-15 min | Blockers escalated, today's priorities |
| Daily | Check aged items over threshold | 10 min | Action on outliers |
| Weekly | Gemba visit to one step | 30-45 min | One observation, one coaching conversation |
| Weekly | Standard work audit (one procedure, one person) | 20 min | Adherence noted, standard updated if needed |
| Weekly | Metrics review with team | 30 min | Trend, one improvement experiment |
| Monthly | Report to sponsor | 30 min | Dashboard, decisions needed |

---

## 9. A3 problem solving (ReEngine format)

The A3 is a single page that tells the story of a problem and its PDCA solution. ReEngine's A3 format (BOK example on a Limited Mining Operations notification review) uses these blocks:

1. Title: the problem stated plainly.
2. Background: why it matters, process purpose, pain points.
3. Current Condition: facts and data (variability, outliers, sequencing, risks).
4. Goal / Target Conditions: measurable, dated; ReEngine uses O-G-P targets (for example Good = 10 working days).
5. Root Cause Analysis: the causal chain with evidence.
6. Improvement Opportunities: what the analysis reveals.
7. Countermeasures (Experiments): written as hypotheses to test.
8. Implementation Plan: who, what, when, including SOP drafting, leadership decisions, training and launch, and a 90-day review.
9. Follow-up (Actions): metrics, monitoring, PDCA cadence.

Example drawn from the BOK A3 (summarized from the document, not invented): the LMO process required operators to notify the agency 30 days before mining, but lacked a standardized internal review and communication gates. The current condition showed highly variable review times with some outliers over 100 days, ambiguous criteria for temporary file numbers, sequential bonding and review, and premature landowner notification causing costly re-notification. Root cause: no standardized process, no internal timeline target, no communication gate. Countermeasures: standardize preliminary and pending TFN criteria; send an immediate receipt confirmation (Mine Notification Memorandum); set O-G-P review targets of 5/10/20 working days; visualize the parallel bond and review path; pilot with two or three frequent operators; move landowner notification after the initial review. Follow-up: track average time from package receipt to cure letter or acknowledgement against the 10-day Good target; 90-day review; quarterly PDCA.

### 9.1 A3 coaching questions

- What is the problem, in one sentence, without a solution embedded in it?
- How do you know? Show the data.
- What is the target condition and by when?
- What is the root cause, and how did you verify it rather than assume it?
- Why do you believe this countermeasure addresses that cause?
- What do you expect to happen, and how will you know?
- Who has to agree, and have they seen this A3?
- What will you do if the experiment does not work?

### 9.2 A3 template

```
TITLE:
Owner:                Sponsor:                Date / Version:
1. Background (why this matters; link to Strategic Compass goal)
2. Current Condition (facts, data, map excerpt; mark unknowns)
3. Goal / Target Condition (metric, O-G-P target, date)
4. Root Cause Analysis (5 Whys / fishbone / interference diagram; evidence)
5. Improvement Opportunities
6. Countermeasures (as experiments: "If we ___, we expect ___ measured by ___")
7. Implementation Plan (action | owner | due | status BRAG)
8. Follow-up (metric cadence; 30/60/90 review; standardization)
```

---

## 10. Gemba

### 10.1 What a gemba walk is (and is not)

From the BOK guide: gemba means "the real place." A gemba walk is structured observation and collaboration where the work is done, focused on a specific process, with open-ended questions, leading to reflection before action. It differs from management by walking around (MBWA), which is unstructured. Deming, as quoted in the guide: management by walking around "is hardly ever effective," because the walker does not know what to ask and does not stay long enough. Leaders committed to CI often spend 45 to 60 minutes or more per week on formal gemba walks.

Keys (BOK): focus on the process, not blame; observe and learn; mix up times and days; test assumptions (a sloppy-looking practice may be a workaround for missing equipment); walk with a cross-functional team; follow up.

### 10.2 Gemba question set (government adaptation)

- What are you working on right now, and what triggered it?
- How do you know what to do next? Where is the standard?
- What do you need that you do not have right now?
- Where do you get stuck? How often?
- What do you do when information is missing? How long does that take?
- How do you know you did it right?
- Who receives your work, and what do they do with it?
- If you could change one thing, what would it be?
- What rule or requirement drives this step? Where is it written?

### 10.3 Virtual gemba (remote and hybrid work)

Many public offices are hybrid. Virtual gemba options: screen-share walk-through of a real case in the system from receipt to current step (with privacy controls), system timestamp extraction, shadowing a staff member on a video call, and reviewing a sample of closed files end to end ("file walk"). Albany's recommendations report recorded a single observed court day on which only one court-held case closed and only one hour of the first session was used; observing a real day exposed the gap between scheduled and used capacity (documented in the recommendations report).

### 10.4 Gemba ethics in government

- Inform supervisors and, where applicable, union stewards in advance.
- Never record staff without consent; follow public-records rules for notes.
- Do not observe confidential proceedings (juvenile matters, sealed records, medical information, investigations) without explicit authorization and confidentiality agreements.
- Report system problems, never individual performance.

---

## 11. Visual management

### 11.1 ReEngine Journey Board

From the 4-Pillars document: the Journey Board visualizes the flow of work (projects, investigations, permits, applications) through major phases where the work gains value, shows WGLL from beginning to satisfied customer, and breaks annual targets into weekly targets per team and person. It can be a tracking tool or a "simulate and calculate" capacity model.

Design elements:

- Columns: major value-adding phases from the Strategic Compass (not every step).
- Cards: one per unit of work, with ID, type or bucket, date entered, date due (O-G-P), owner.
- WIP limits per column, especially at the constraint.
- Aging indicators: color or dot per week in phase.
- Blocked flag with reason and escalation owner.
- Target rate per week vs actual completions.
- Cumulative flow diagram (submitted vs issued). MDOT TPU used a cumulative flow diagram to track permits submitted vs issued [Summary].

Stand-up questions used at Columbus 3P Journey Board sessions [Summary]: (1) Did we make expected progress? (2) What is the intent for the next two weeks? (3) What help is needed to clear obstacles?

Parallels: SD BIT takt board (physical and digital) [Summary]; SD Board of Regents system-wide Journey Board for VPs and Regents, described as the "Aha" moment for executives because it made the invisible burden of policy development visible [Summary]; SD LRC digital Journey Board in Microsoft Teams for legislative information requests with a complexity matrix scored 4 to 20 [Summary]; Minnesota Lottery Teams Journey Board shifting conversations from "What is the status?" to "How do we resolve the bottleneck?" [Summary]; WY DEQ LQD-URP unified board tracking a license and permit as a synchronized pair [Summary].

### 11.2 Tiered huddles

| Tier | Who | Length | Content |
|---|---|---|---|
| 1 | Front-line team | 10-15 min daily | Yesterday's results, today's plan, blockers, safety or quality issues |
| 2 | Supervisors | 15 min daily or 3x weekly | Escalated blockers, cross-team load balancing |
| 3 | Managers or division | Weekly | Trends, resource decisions, policy issues |
| 4 | Executive | Bi-weekly or monthly | Strategic Compass metrics, decisions on bottlenecked policy workstreams |

Albany's design included an 8:40 AM standup with the Court Administrator, clerks, Solicitor, and Public Defender to set the day's case order (design in the final deck). Day and Zimmermann, a federal munitions production contractor, used 10-minute daily huddles in production bays [Summary].

### 11.3 Dashboards and metric tension

Pillar 4 (Dashboards and Scoring): leadership regularly reviews KPIs for accountability and transparency. ReEngine principle "Metric Tension": pair a speed or volume measure with a quality measure so one cannot be gamed at the expense of the other. Examples from the RAG: tickets closed vs tickets reopened (College Station [Summary]); average handle time vs calls transferred to Tier 2 (Virginia Employment Commission [Summary]); interviews vs successful hires (OWBC HR [Summary]); net-30 timeliness vs quality (Prairie View A&M [Summary]).

SD DOC "Measure What Matters": the monthly reporting deck went from 87 slides to about 13, with metric ownership moved to divisions and institutions [Verified-deck]. Use this as the anchor example for over-reporting waste.

### 11.4 Andon equivalents

A visible, immediate signal that something is wrong: a red card on the board, a Teams channel flag with a response-time standard, a system alert when an item ages past threshold. The rule that matters is the response protocol: who responds, how fast, and what they do.

---

## 12. Error-proofing, changeover reduction, and related tools

### 12.1 Poka-yoke (mistake-proofing) in government

Hierarchy: eliminate the possibility of the error, then make the error obvious, then make it easy to detect and correct.

| Error | Poka-yoke |
|---|---|
| Missing documents | Online form that will not submit without required attachments; pre-screening tree; checklist on the application |
| Wrong form or wrong path | Bucket logic that asks questions and routes to the right form (Minnesota Lottery Bucket Automation Logic Map [Summary]) |
| Missing contact information | Required phone and email fields on citations (Albany design) |
| Missing appearance date | Officer enters first-appearance date on citation (Albany design) |
| Data entry errors | Drop-downs, validation, auto-population from authoritative IDs (SD Board of Regents onboarding form auto-completes from ERP IDs [Summary]) |
| Lost evidence chain | Barcoding at intake; geotagged photos (Columbus ROW Enforcement lat/long capture [Summary]) |
| Late booking data | Time standard: affidavits and booking notes in the jail management system within 2 hours of arrest (Albany; the recommendations report states officers were trained on the procedure before 1 August 2021 and the system was functioning) |

### 12.2 SMED (single-minute exchange of dies) for office changeovers

Changeover in an office is the time lost switching between tasks, sessions, or setups. Examples: court session setup and docket preparation, inspector preparation before a site visit, a reviewer reorienting to a file after an interruption, meeting setup, switching between systems.

SMED steps: (1) observe the changeover; (2) separate internal (must stop work) from external (can be done in advance) activities; (3) convert internal to external (prepare files before the session; pre-load case packets); (4) streamline both (templates, checklists, standard kit); (5) standardize.

Multitasking is a changeover cost. SD BIT's lesson: staff working at a "break-neck pace" but completing few projects because they jumped between tasks [Summary]. Reducing WIP per person reduces changeovers.

### 12.3 Jidoka in offices

Stop and fix at the source. Intake quality gates, a supervisor review of the first five items after a change, and "stop the line" authority for staff who find a systemic error.

### 12.4 TPM-lite for fleets and equipment

For public works and utilities: operator daily checks, planned maintenance, and right-sizing. College Station's "Ghost Fleet" analysis identified underutilized vehicles as a cost lever and proposed charging departments actuals for ghost fleet usage [Summary]. Columbus Snow and Ice set a path toward a 70 percent standardized fleet to reduce maintenance lead times [Target].

---

## 13. Kata, target conditions, and policy deployment

### 13.1 Improvement Kata (Rother, BOK)

Pattern: understand the direction or challenge; grasp the current condition; establish the next target condition; iterate toward it with PDCA. A target condition is an interim goal described in more detail than the challenge; it describes where you want to be next, not how to get there; it lies beyond current knowledge; and it has an achieve-by date usually between 1 week and 3 months. The BOK presentation notes that an estimated 80 to 95 percent of variation in a work process is common-cause; troubleshooting individual failures is the wrong approach, and the system itself must change.

Coaching Kata five questions (use in leader standard work):
1. What is the target condition?
2. What is the actual condition now?
3. What obstacles do you think are preventing you from reaching the target condition? Which one are you addressing now?
4. What is your next step (next experiment)? What do you expect?
5. How quickly can we go and see what we have learned from taking that step?

### 13.2 Hoshin kanri (policy deployment) in government

Cascade the agency's strategic goals into a few breakthrough objectives, then into annual improvement priorities, then into team targets, with "catchball" negotiation at each level. ReEngine's Strategic Compass and Strategic Path serve this purpose in a lighter form. In government, align with the strategic plan, the budget or appropriations cycle, and performance measures required by statute.

---

## 14. Lean government specifics

### 14.1 The government environment (Mycue and Schragenheim, TOC BOK)

1. A clear, agreed goal is elusive due to shifting political priorities. Lean needs a goal; build the Strategic Compass with the sponsor and confirm with elected or appointed leadership.
2. Many restrictions from regulations cannot be challenged at the agency level. Work within them; separate "agency can change" from "requires rule or statute change."
3. Funding and authorization are generally stable, which makes Lean, Six Sigma, and TOC well suited.
4. Government cannot control demand. Design WIP control and surge plans, not demand refusal.
5. Government operates in Moore's Strategic Triangle: legitimacy and support, public value, operational capacity. Change risks legitimacy, so the environment is risk-averse.
6. Money must be paired with authority; expiring funds and appropriation categories complicate implementation.
7. Government has a unique duty in disasters.

### 14.2 Practitioner adaptations

- Statute and rule mapping: for every RNVA step, record the citation. Categorize recommendations: "agency can do now," "director approval," "requires rule change," "requires statute or ordinance change," "requires funding." Columbus Snow and Ice grouped 77 recommendations into Feasible Now, Director Approval, and Third Party or Funding [Summary].
- Due process and equity: every change to intake, eligibility, enforcement, or adjudication gets a legal and equity review. MaineHousing shifted from "Verify Everything" to "Assist Customers to Get to Yes," using an evaporating cloud to show that self-attestation with back-end audits could satisfy both fraud prevention and accessibility [Summary].
- Separation of powers: courts are not executive departments. In a court engagement, the judge controls the bench; the clerk may be a separately elected official; police are another department. Albany's interagency handshake with the police department is the model.
- Collective bargaining and civil service: changes to duties, schedules, or classifications may require meet-and-confer or bargaining. See change-management.md.
- Headcount fear: staff often believe efficiency means layoffs. Get a sponsor statement on redeployment of capacity before the event. ReEngine's framing: capacity is used to clear backlogs, improve service, and absorb growth (WY DEQ Coal: the assessment concluded the program did not need additional FTEs but system optimization [Summary]; Columbus 3P: absorb a large workload increase without additional FTEs [Target]).
- Clean before automating: most public agencies are mid-way through a system replacement (Accela, Cityworks, OnBase, Yardi, MIDAS, WellSTAR, B2Gnow, RMS). Lean the process first, then harvest requirements. "Automating a broken process only results in faster garbage" (SD Attorney General SOR lesson [Summary]). The "digital paper" trap: scanning is not automation (Minnesota Lottery [Summary]).
- Public records: workshop outputs may be public records. Write sticky notes and maps accordingly; avoid personnel commentary.
- Elected-official and legislative cycles: time launches to avoid budget hearings, legislative sessions, and elections when possible (SD LRC: changes had to be stable before the January session [Summary]).
- Creativity before mapping: ND Parks and Recreation found that jumping straight into process mapping can feel like another administrative burden; starting with "Thinking Unconstrained" earned buy-in, and a tangible first VSM (boat and pontoon rentals) made the method relatable [Summary].

### 14.3 GQI 7 phases mapped to Lean tools

| GQI phase | Purpose (from CORE_METH_Main-Master-Logic) | Primary Lean tools |
|---|---|---|
| Charter It | Set parameters, get leadership buy-in, analyze funding sources and stakeholders, gather existing data, benchmark | Charter, SIPOC, stakeholder and demand analysis, baseline data plan |
| Vision It | Common understanding of goals, WGLL, how to measure | Strategic Compass, QT/OE, target conditions |
| Map It | Comprehensive current-state understanding | Value Stream SOP (swim-lane VSM), gemba, data boxes, O-G-P |
| Gap It | Difference between WGLL and current state; feedback from audits, complaints, legislative inquiries, self-assessment | Interference diagram, waste analysis, 5 Whys, fishbone, ROI and risk ranking |
| Build It | Design the to-be process; full-kit intake; capacity model | Future-state VSM, standard work, Journey Board, Strategic Path, capacity model |
| Launch It | Deploy with change management; 1-hour launch presentation to executives; cascade briefings | Launch deck, training, SOP release |
| Track It | Metrics and dashboards to make change stick (Baldrige-informed) | Dashboard, balanced scorecard, huddles, 30/60/90 reviews, PDCA |

Gap It practice from the methodology document: the team collects available feedback on performance (audits, funding-source assessments, customer complaints, legislative inquiries, directors' concerns, honest self-assessment), divides the documents among members, re-reads them, and reports takeaways. Deliverables through Gap It include high-level process maps with inputs, outputs, dependencies, O-G-P timeframes, and deficiencies, plus a deficiency list ranked by ROI and impact, resembling a risk assessment.

---

## 15. Templates

### 15.1 Lean project charter (one to two pages)

```
Project name:
Sponsor:                 Process owner:              ReEngine lead:
Value stream / product family:
Start event:             Stop event:                 Clock rules:
Problem statement (fact-based, no solution embedded):
Baseline data (source, period; mark UNKNOWN where not yet collected):
Goal / target condition (metric, O-G-P, date):
In scope:                Out of scope:
Constraints (statute, rule, CBA, funding, systems):
Customers (direct, statutory, funding, oversight, internal, public):
Team (name, role, % time):
Decision rights of the team:
Deliverables:
Schedule (event dates; 30/60/90 report-outs):
Risks and mitigations:
Communication plan headline:
Approval: sponsor signature and date
```

### 15.2 SIPOC

| Suppliers | Inputs | Process (5-7 high-level steps) | Outputs | Customers |
|---|---|---|---|---|
| Applicant; other department; state system | Application; plans; fee; data feed | 1. Receive 2. Screen for Full-Kit 3. Assign 4. Technical review 5. Decision 6. Issue 7. Close | Permit; deficiency letter; denial; notice | Applicant; public; inspectors; auditors |

Add a row for "requirements" under inputs and outputs (CTQs; see six-sigma.md). BHAT's strategic retreat used SIPOC to identify the broad range of customers served, from state and federal government to schools and law enforcement, clarifying the public value providers create [Summary]; the same move works for any public program.

### 15.3 Waste walk sheet

| # | Step observed | Waste type (DOWNTIME) | Description (fact) | Frequency or volume | Estimated time impact | Idea |
|---|---|---|---|---|---|---|

### 15.4 Interference diagram (ReEngine Gap It)

Center: the goal (from the Strategic Compass). Around it: every interference (obstacle) staff name, one per note. Group by theme (intake, systems, policy, staffing, communication). Rank by impact. Major interferences feed root cause and the Strategic Path. ReEngine's Strategic Path logic then asks, for each element from top to bottom, "Is completing this step sufficient to achieve the next step?" and if not, "What else do we need?" This sufficiency logic produces a one-page plan the experts agree cannot help but achieve the goal.

### 15.5 Implementation plan

| # | Action | Linked map step | Owner | Due | Status (BRAG) | Approval needed | Metric affected | Notes |
|---|---|---|---|---|---|---|---|---|

### 15.6 Kaizen newspaper (open action list during the event)

| Problem | Countermeasure | Who | When | Done |
|---|---|---|---|---|

### 15.7 30/60/90 report template

```
Process:              Report-out: 30 / 60 / 90 days      Date:
1. Actions planned vs complete (BRAG summary)
2. Metrics vs baseline vs target (chart; data source; caveats)
3. Standard work adherence (audit results)
4. What we learned; adjustments made
5. Risks and asks for the sponsor
6. Next target condition
```

### 15.8 Standard work sheet

| Step # | Major step (what) | Key points (how: safety, quality, ease) | Reasons (why) | Time (O-G-P) | Inputs / Full-Kit | Quality check |
|---|---|---|---|---|---|---|

### 15.9 Full-Kit checklist (generic)

```
Work type:                         Version:
Required before work starts (item | source | verification method | if missing):
- Application form complete (all required fields)
- Required attachments (list each with citation)
- Fee paid / waiver documented
- Prior approvals or clearances
- Contact information verified
- Parameters agreed (e.g., study MOU)
Decision: [ ] Full-Kit -> release to queue  [ ] Not Full-Kit -> pending completion; notice sent date
```

### 15.10 Huddle board layout

```
| Safety/Quality issues | Yesterday: target vs actual | Today: priorities | Blockers (owner, escalate by) | Ideas (just-do-it / kaizen) | Recognition |
```

### 15.11 Strategic Compass (one page)

```
Goal statement (the quality unit of public value and why it matters):
Goal unit (QT) definition and quality criteria:
Major stages (5-7) from request to satisfied customer:
Constraint (the stage that governs throughput) and its control-point metric:
WGLL for each stage (O-G-P time, Full-Kit, first-time-go):
Key measures (throughput, quality, timeliness, cost per quality unit):
```

Clean Energy Fund of Texas developed a mission-aligned application goal statement of this kind as part of its program infrastructure [Summary]; WY DEQ Coal and SD DOC each used a Strategic Compass to align work and metrics to the goal [Summary].

### 15.12 Sandbox simulation plan

```
Future-state process being tested:
Roles played (and by whom):
Scenarios (normal, edge case, failure case):
Curveballs to inject (equipment failure, missing data, conflicting orders):
Observers and what they record (where the chain breaks, decisions escalated):
Debrief questions: What broke? What was unclear? What must change in the SOP?
```

---

## 16. ReEngine past-engagement parallels (use to draw comparisons)

When drafting a finding, synopsis, or proposal, cite a parallel in this form: "Comparable to the situation in the <client> engagement (<years>), where <situation>; ReEngine <action> [evidence tag]." Use only what is below or what you verify in the RAG.

| Situation pattern | Engagement (RAG) | What ReEngine did | Evidence status |
|---|---|---|---|
| Incomplete submissions drive rework at intake | City of Columbus ROW Permitting (2020-21) | Rigid Full-Kit vetting before routing to eight reviewers; 80/20 focus on top revision reasons; customer-perspective website mock-up | 51% cycle-time improvement and 46% rework reduction in a 3-year follow-up [Summary]; an external partner quote appears in the summary [Summary; do not quote externally without verification] |
| Low first-time-go at application intake | MaineHousing HEAP (2019) | Kaizen week; current-state VSM with 21 interference points; pre-screening tree; self-attestation for high-friction documents | Baseline about 35% first-time-go [Summary]; improvement targeted [Target] |
| Incomplete applications slow eligibility | Opportunities for Williamson and Burnet Counties CEAP (2022-23) | Analyzed 1,430 applications; full-kit vs incomplete processing comparison; Pending Completion status instead of denial; volunteer application navigators | Full-kit about 57 days vs incomplete about 90 days; 33% first-time-go baseline [Summary]; at least 33 days reduction potential [Target] |
| Court backlog, limited bench capacity | City of Albany GA Municipal Court (2021) | Capacity model; 8:40 standup; chute and ready bench; batch standing orders; 2-hour booking data standard; virtual court SOP; 35+ recommendations | Booking-data standard implemented with officer training (recommendations report); projected fine increase is a projection [Target]; the 47% case-resolution gain in the summary is summary-only and must not be used as fact |
| Over-reporting, metrics without owners | South Dakota Department of Corrections (2018-19) | Measure What Matters kaizen; Strategic Compass; ownership to divisions | 87 slides to about 13 [Verified-deck] |
| Intake bottleneck in corrections admissions | SD DOC Admissions and Orientation (2018-19) | Full-Kit for records and medical before the intake clock starts; future-state intake flow | Intake reduction targeted [Target] |
| Legal office leadership saturated by triage | City of Greeley City Attorney's Office (2024-25) | Three-bucket legal work framework; evaporating cloud on tracking; confirmation briefs and back-briefs; VSMs | First style guide and brief-back standard [Summary]; triage reduction targeted [Target] |
| Regulatory permitting with technical reviewer bottleneck | Wyoming DEQ Land Quality Division, Coal (2018) | Constraint within the constraint (hydrology and CHIA); decouple from linear review; Journey Board; early technical review results | No additional FTEs needed, optimization instead [Summary] |
| Multi-program regulatory redesign | Wyoming DEQ Solid and Hazardous Waste and Water Quality (2024-26) | Mini-launch per program; VSMs; WYIMS requirements; surge resilience target | 162-page report [Summary]; under 18 months full-kit tank remediation goal [Target] |
| Large-volume permit unit and route data silos | Michigan DOT Transport Permits Unit (2019-21) | Journey Board and cumulative flow; Tiger Teams with Bridge and Maintenance; ideal-state requirements; presumptive denial for non-responsive customers | About 180,000 permits per year; 48-page report with 26 recommendations [Summary] |
| Public works service requests from many channels | City of College Station Public Works (2019) | Kaizen per division; WMS standard; ghost fleet; knowledge cards; metric tension | Future-state VSMs for five divisions [Summary] |
| Utility development review | Santa Clara Valley Water District CPRU (2021-22) | 29 subprocesses; qualified screening before engineers; dedicated engineer hours; requirements for Cityworks and OnBase | Engineer capacity increase projected [Target] |
| Police administrative processes | Pittsburgh Bureau of Police (2021-22) | Secondary employment deduplication; PFA SOP and daily status report; evidence transport redesign | 400-500 manual entries targeted for removal; 100% weapon relinquishment accountability goal [Target] |
| Higher-ed system processes across campuses | South Dakota Board of Regents (2019-24) | Six sub-projects; vetting matrix; onboarding form auto-complete; system Journey Board | First single data source for workload reporting [Summary] |
| SOP codification for regulated programs | Charlottesville RHA (2024-25); CalGEM (2021-23) | 70+ SOPs; Encyclopedia of SOPs; one well-permit review standard across three districts | Coverage as stated [Summary]; confirm before external use for housing examples |
| Procurement intake chaos | Minnesota State Lottery (2023) | Six buckets; bucket automation logic; Teams Journey Board | PO cycle baselines (3.5 days simplest vs 74 days most complex) [Summary] |
| Seasonal operations, conflicting data | City of Columbus Snow and Ice (2025) | Sandbox simulation; shift-change agenda; eliminated mid-event reports; Time to Regain Friction dashboard vs 15-hour goal | 77 recommendations; mid-event reporting requirement eliminated [Summary] |
| Legislative support workload | SD Legislative Research Council (2021) | Motion-sheet redesign; RFI complexity matrix; Teams Journey Board; training workbook | Red Steps 9 to 0 and 55% automation in future-state flow [Summary] |
| Aged caseload and audit remediation | New Hampshire Vocational Rehabilitation (2021-23) | "Old Dogs" aged-case review; end-to-end VR map with 21 interference points; Full-Kit intake checklists | 168 non-advancing eligibility cases; 108-day eligibility baseline [Summary]; 45% reduction [Target] |
| Enterprise CI training and sustainment | North Dakota IT (2019-22); SD BIT (2016-17) | Train-the-trainer; Journey Board workshops; takt board; Full-Kit requirements checklist | 818 trained including 10 certified trainers [Summary]; SD BIT 83% velocity is summary-only and must not be used as fact |

Agent notes on use:
- Texas state-agency engagements (for example the State Auditor's Office training, Office of the Governor federal grants, HHSC practitioner training, the LBJ School GCMD course): confirm with David before using in external materials.
- Housing and energy-assistance engagements (MaineHousing, OWBC, Charlottesville): confirm with David before external use.
- Never combine figures from different engagements into a composite claim.
- The phrase "routinely resulted in 25% or more improvement" appears in ReEngine methodology boilerplate, and the RAG story bank flags "no project under 25% improvement" and "100% customer satisfaction" as marketing-only claims. Do not use them in a proposal without David's approval and supporting evidence.

---

## 17. Integration with the other four methodologies

| Combine Lean with | How | Example |
|---|---|---|
| Six Sigma | Lean removes waste and creates flow; Six Sigma reduces variation and verifies root cause statistically. Use DMAIC when the problem is a variable outcome (error rates, eligibility accuracy, cycle-time variability). Lean tools live inside DMAIC Analyze and Improve. | NH VR: 83% of cases met the 60-day eligibility window while outliers averaged 840 days in services [Summary]; averages hid the story, so an individuals chart and outlier review ("Old Dogs") show whether new standard work holds |
| Theory of Constraints | TOC says where to apply Lean: exploit and subordinate to the constraint. Lean kaizen at a non-constraint may not improve system throughput. Full-Kit and Front Door are TOC subordination implemented with Lean jidoka. | Santa Clara Valley Water: engineer review is the constraint; Lean screening protects it |
| Project management | A kaizen is a project with a charter, schedule, deliverables, and risks. Implementation plans are project schedules. Government contracts need deliverable acceptance and status reporting. | WY DEQ PMP boilerplate: in-progress summaries and reports; decision briefs; deliverable sign-off |
| Change management | Every future state changes jobs. Launch It is a change-management event. ADKAR barrier points show up at gemba and in huddles. | Pittsburgh Police: shifting evidence transport duties was a significant cultural change for frontline officers [Summary] |

The specialist-synthesizer pattern: the Lean specialist posts one short finding (for example "Intake accepts incomplete files; deficiency loops visible in the review queue, cited in the 2026-10-14 transcript at the reviewer's comment"), and the synthesizer merges it with the TOC, Six Sigma, PM, and CM findings into one advisor voice.

---

## 18. Decision guides

### 18.1 Which Lean intervention?

| Symptom | First tool | Then |
|---|---|---|
| "Nobody knows how it really works" | Gemba, SIPOC, current-state VSM | Interference diagram |
| Backlog growing | Count WIP and throughput (Little's Law); find the constraint (TOC) | Full-Kit, WIP limits, aged-case review |
| Lots of returns and resubmittals | Pareto of deficiency reasons; Full-Kit checklist | Poka-yoke on forms; applicant guidance |
| Long waits for approval | Map approvals; delegation matrix | Post-decision audit, batching rules |
| Staff overwhelmed, constant interruptions | WIP per person; triage by type | Coordinator role; leveling; protected focus time |
| Inconsistent decisions across offices | Standard work; decision criteria | Calibration sessions; QA sampling (Six Sigma attribute agreement) |
| New system coming | Clean before automating; future-state VSM | Requirements harvest from future state |
| Gains did not stick last time | Leader standard work; Track It dashboard | 30/60/90 reviews; change-management reinforcement |
| Too many reports | Measure What Matters (information requirements) | Dashboard with metric tension |
| Infrequent high-stakes operation | Sandbox simulation | Standard work, shift-change checklist |

### 18.2 Event, project, or daily kaizen?

- Event: bounded value stream, cross-functional, need for a fast reset, sponsor available.
- Project (DMAIC or multi-month): root cause unknown, data analysis needed, or system changes needed.
- Daily kaizen: small, local, within team authority.

### 18.3 Is it a Lean problem at all?

If removing waste at a step will not change the end-to-end outcome because another step limits the system, it is a TOC problem first. If the outcome varies for unknown reasons, it is a Six Sigma problem first. If people know what to do but are not doing it, it is a change-management problem first. If the scope, schedule, or acceptance criteria are unclear, it is a PM problem first.

---

## 19. Facilitation scripts and questions

Kickoff (sponsor):
"We are here because [problem in one sentence]. This week the people who do this work every day will design how it should work. You have authority to [decision rights]. Nobody will lose their job because of what we find; capacity we free up goes to [backlog, service, growth]. I will be back on Friday to hear your recommendations, and I will decide on the spot where I can." (Use the redeployment sentence only if the sponsor has actually committed to it.)

Opening the current-state map:
"We are mapping what actually happens, not what the manual says. If you do it differently from your colleague, we want both versions. There are no wrong answers, only unknowns we will go find."

When the room blames individuals:
"Let's assume everyone is doing their best with the system they have. What about the system makes this outcome likely?"

When someone says "the law requires it":
"Good, let's capture the citation so we can design around it. Which statute or rule, and which section? If we are not sure, let's put a question mark and assign someone to check."

When the group jumps to solutions during mapping:
"Write the idea on a yellow note and put it in the parking lot. We will come back to every one of them on Day 3."

When a manager dominates:
"Thank you. I'd like to hear from someone who touches this step every day. [Name], what happens when this lands on your desk?"

Future state prompt:
"Imagine a complete file arrives Monday morning. What is the fewest number of touches, handoffs, and waits it could take to reach a decision while meeting every legal requirement?"

Interference diagram prompt:
"Our goal is [Compass goal]. What gets in the way of achieving it? One obstacle per note, as specific as you can."

Professional-culture framing (attorneys, engineers, scientists): "These tools protect your deep-work time from administrative interruptions; they do not tell you how to exercise professional judgment." (Greeley lesson: attorneys resist "efficiency" metrics; framing around protecting deep work helped [Summary].)

Closing the event:
"What did we decide, who owns each action, and when do we meet again to check? Let's read the implementation plan aloud."

Report-out structure (60 minutes): problem and goal (5); current state and key data (10); root causes (10); future state (15); quick wins already done (5); implementation plan and metrics (10); decisions requested (5).

---

## 20. Common pitfalls

1. Event without follow-up. The EPA guide identifies lack of follow-through as a key reason Lean projects fail. Contract and schedule the 30/60/90 reviews.
2. Lean seen as a cost-cutting or headcount program. Get a redeployment commitment.
3. Lean dividing the workforce into "entrepreneurial" and "traditional" groups. Ratner (BOK) documents how Lean in a public department became a source of group conflict, and later a rallying point against a restructuring. Involve skeptics, rotate participation, avoid favoritism, and watch for collisions with other change initiatives.
4. Mapping without data, then claiming results without data.
5. Optimizing a non-constraint.
6. Automating waste.
7. Ignoring the applicant's steps and the statutory customer.
8. Treating RNVA steps as untouchable or, conversely, labeling due-process steps as waste.
9. Too many metrics; no owners (SD DOC lesson).
10. Speed metrics without quality (missing metric tension).
11. Standard work written by managers alone.
12. Sponsor absent at kickoff and report-out.
13. Underestimating union, civil service, and elected-official dynamics.
14. Rolling out without training or a launch moment (GQI Launch It exists for this reason).
15. Declaring victory at Blue on a BRAG board before a full cycle is observed.
16. Ignoring organizational change underway (reorganizations, mergers). Minnesota childcare licensing: a planned hub was not implemented as designed because of a 2024 transfer of functions into a newly created department, although the mapping still supported legislative funding decisions [Summary].

---

## 21. Proposal methodology language (draft building blocks)

Use these as drafts that David edits. Replace bracketed items. Do not add results or claims not supported by the RAG.

Lean approach paragraph (draft):
"ReEngine will apply its Government Quality Improvement (GQI) method, which blends Lean, Six Sigma, and the Theory of Constraints for public-sector environments, through seven phases: Charter It, Vision It, Map It, Gap It, Build It, Launch It, and Track It. Working side by side with [Agency] staff, we will map the [process] value stream from [start event] to [stop event] as a Value Stream SOP, quantify lead time, touch time, rework, and first-time-go rates, identify the constraint that governs overall throughput, and design a future state that meets every statutory and regulatory requirement while removing non-value-added steps. Future-state designs typically strengthen the 'front door' so reviewers receive complete files ('Full-Kit'), make work visible on a Journey Board, and establish standard work and dashboards so improvements are sustained."

Kaizen paragraph (draft):
"Each improvement event follows a plan, event, and follow-up structure consistent with the EPA Lean Government Implementation Guide, including 30-, 60-, and 90-day report-outs that verify results against baseline, standardize changes, and address backsliding."

Staff engagement paragraph (draft, grounded in CORE_METH_Expectations-Logic):
"ReEngine's approach captures experiences from multiple perspectives, including timings, handoffs, pinch points, and customer feedback, and workshops early recommendations with staff so that the people who do the work see their contributions reflected in recommendations to leadership."

Relevant experience paragraph (draft; choose parallels from Section 16 that match the solicitation and cite with correct status):
"ReEngine has applied this approach in comparable settings, including [engagement], where [situation] and ReEngine [action]. [Only include a result if tagged Verified-deck, or Summary with David's approval.]"

Compliance matrix tip: map each Lean deliverable to the solicitation requirement number (see project-management.md and the gov-proposal-pmp skill).

What public buyers typically ask for (from the VA Lean SOW in the BOK): executive-level and mid-level coaching, rapid process improvement events, value stream analysis, a deployment roadmap, belt training and certification, A3s and standard work uploaded to the client's repository, monthly status meetings with minutes within a stated number of days, and a transition-out plan. Check every solicitation for these and address each explicitly.

---

## 22. Agent instructions and guardrails

1. Draft only. Never send, submit, post, or present. Save drafts where instructed (for example a local WIP folder) and report the path.
2. Never fabricate data. If baseline data is missing, write "UNKNOWN - to be collected via [method]" and add it to the data collection plan. Hypothetical examples must be labeled "Hypothetical example."
3. Cite artifacts. Every finding in an engagement synopsis must cite a specific artifact (transcript date and speaker, email subject and date, document name and page). No generic Lean advice without an anchor.
4. Use the evidence tags in Section 16. Never upgrade a Target to a result or a Summary figure to a verified one.
5. Do not invent quotes from clients or staff.
6. Respect read-only sources. The ReEngine BOK on the Shared Drive and the RAG vault are read-only. Never create, edit, move, rename, share, or delete files there.
7. Confidentiality: client documents, staff names, and case details stay within the engagement. Do not paste personally identifiable or sensitive case information into external tools.
8. Public-sector sensitivity: flag any recommendation touching due process, eligibility, enforcement, personnel actions, collective bargaining, or records retention for human legal or HR review.
9. Pursue-or-pass decisions on solicitations belong to David. An agent may summarize fit and flag confidence; it does not decide.
10. Prefer ReEngine vocabulary (Full-Kit, First Time Go, Red Steps, Strategic Compass, Journey Board, WGLL, O-G-P) in ReEngine documents, but define each term once for a new client.
11. When local models extract requirements from solicitations, extract Lean-relevant requirements verbatim with section numbers; do not paraphrase requirements into the compliance matrix.
12. When uncertain which methodology applies, run the decision guide in Section 18 and say which lens you used and why.
13. Write plainly, no emojis, no hype.

Engagement-synopsis Lean specialist prompt (internal pattern):
"Read the new material since the last run. Report at most three Lean findings. Each finding: (a) observation, (b) waste type or flow issue, (c) cited artifact, (d) suggested next step, (e) whether it moves the project toward the charter objective or drifts, (f) a comparable past engagement from Section 16 if one genuinely fits."

---

## 23. Glossary

- A3: one-page PDCA problem-solving report.
- Andon: visible signal of an abnormality with a response protocol.
- Bad Circle Back: an item returning unnecessarily to a decision-maker's queue (ReEngine term).
- BRAG: Blue, Red, Amber, Green status tool measuring improvement velocity (ReEngine).
- Cumulative flow diagram: chart of cumulative arrivals and completions over time; the vertical gap is WIP and the horizontal gap approximates lead time.
- Deficiency loop: backward flow to correct incomplete or incorrect work.
- DOWNTIME: Defects, Overproduction, Waiting, Non-utilized talent, Transportation, Inventory, Motion, Extra processing.
- First Time Go: percent of submissions complete on first submission (ReEngine).
- Full-Kit: all inputs needed to complete work without interruption (TOC origin; ReEngine usage).
- Gemba: the real place where work is done.
- GQI: Government Quality Improvement, ReEngine's blended method.
- Heijunka: leveling of volume and mix.
- Interference diagram: TOC-derived tool listing obstacles to a goal (ReEngine Gap It).
- Jidoka: built-in quality; stop and fix at the source.
- Journey Board: ReEngine visual management of work through value-adding phases with weekly targets.
- Kaizen: continuous improvement; also a focused improvement event.
- Kata: practiced routine for scientific improvement (Rother).
- Lead time: elapsed time from request to delivery.
- Little's Law: WIP = throughput x lead time.
- Muda, mura, muri: waste, unevenness, overburden.
- O-G-P: Optimistic, Goal, Pessimistic time estimates (ReEngine).
- PCE: process cycle efficiency, process time over lead time.
- Poka-yoke: mistake-proofing.
- QT/OE: quality throughput over operating expense.
- Red Steps: non-value-adding steps (ReEngine).
- RNVA or BVA: required or business non-value-added.
- Sandbox: high-fidelity role-play simulation of a future state (ReEngine).
- SIPOC: Suppliers, Inputs, Process, Outputs, Customers.
- SMED: single-minute exchange of dies; changeover reduction.
- Strategic Compass: ReEngine one-page logic map of goal unit, stages, constraint, and WGLL.
- Strategic Path: ReEngine sufficiency-logic roadmap from interferences to goal.
- Takt time: available time divided by demand.
- Target condition: next interim goal, dated, beyond current knowledge (Rother).
- Tiger Team: small team chartered to prototype a specific countermeasure.
- Value Stream SOP: ReEngine swim-lane VSM that anchors the SOP.
- WGLL: What Good Looks Like.
- WIP: work in process.
- WWADI: We've Always Done It.

---

## 24. References

BOK (ReEngine Shared Drive, read-only): EPA Lean Government Implementation Guide (2017); EPA Lean Handbook; Example A3 Problem Solving ReEng Format; A Guide to Successful Gemba Walks; Rother, Improvement Kata Handbook, Target Condition section; VA Lean Work Description (sample SOW); Fryer, Antony, and Douglas (2007), Critical success factors of continuous improvement in the public sector, The TQM Magazine 19(5); Maleyeff (2007), Improving Service Delivery in Government with Lean Six Sigma, IBM Center for The Business of Government; Ratner (2012), "It was the night of the long knives," Public Management Review 14(1); May, Elegant Solutions (excerpt); DoD Continuous Process Improvement Guidebook (2006); Mycue and Schragenheim, Unique Features of Government and How Governance Could be Assisted by the Theory of Constraints (TOCICO BOK); SIPOC Template; PDCA image.

ReEngine RAG (read-only): CORE_METH_Main-Master-Logic; CORE_METH_4-Pillars-Framework; CORE_METH_Strategic-Path-Logic; CORE_METH_BRAG-Tool-Logic; CORE_METH_Expectations-Logic; ReEngine Past Project Performance Reports #001-#044; box extracts story_bank_from_RAG_2026-11-04 and albany_detail_from_RAG.

Standard literature (expert knowledge): Ohno, Toyota Production System; Womack and Jones, Lean Thinking; Rother and Shook, Learning to See; Martin and Osterling, Value Stream Mapping; Liker, The Toyota Way; Shook, Managing to Learn; Rother, Toyota Kata; Shingo, A Revolution in Manufacturing: The SMED System; Hirano, 5 Pillars of the Visual Workplace; Mann, Creating a Lean Culture; Graban, Lean Hospitals; Miller, Creating a Kaizen Culture; Moore, Creating Public Value; Hopp and Spearman, Factory Physics.
