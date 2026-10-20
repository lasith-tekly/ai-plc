# Stage 2: Product Planning

**The question:** what exactly will we build first, and can it work? Phase 3 is built by the **solution agent** and ends at **Checkpoint 2**. Phase 4 is built by the **viability agent** and ends at **Gate 2**, with the final business case as the decision pack.

## Phase 3: Converge on solution

| ID | Deliverable | What it is | Mode | Builds on | Words | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| 3.1 | Prioritised capabilities | The capabilities the product must have, ranked against stated criteria. | auto | 2.1, 2.2 | 4,120 | 30 |
| 3.2 | Solution research | How the solution could look and feel: approaches seen elsewhere, the proposed experience, content needed, design questions to test. | assist | 3.1 | 5,127 | 14 |
| 3.3 | Usability tests (v2) | A usability test kit: plan, screener, consent and data handling, tasks and a capture template. People run the sessions. | human | 3.2 | 9,837 | 14 |
| 3.4 | Early positioning and messaging | Positioning and messages by customer group, with the proof we have and the proof we still need. | auto | 1.2, 2.9 | 3,455 | 9 |
| 3.5 | Pilot plan | A pilot plan: questions to answer, who, where, how long, what runs, measures, success and stop signals. | assist | 3.2, 3.3 | 5,856 | 14 |
| 3.6 | MVP scope | The MVP scope: what is in, what is not and when it might be, and what must be true before build. | auto | 3.1, 3.3 | 5,637 | 18 |


Phase 3 is where the work stops being only desk research. **3.3 Usability tests** is a `human` deliverable: the tool writes the test plan, the screener, the consent notes and the capture templates, and people run the sessions. In this dummy run the PM asked for invented results to complete the cycle, and the file says so in its first lines:

> **SYNTHETIC RESULTS (dummy run, not evidence).** The PM asked for fake data to complete this AI-PLC dummy run. No sessions took place. Every result, quote, count and finding in "Results", "What the results say" and "How results feed 3.5 and 3.6" is invented and labelled SYNTHETIC.

The label then follows the data downstream: 3.5, 3.6 and everything built on them carry it too, and the reviewer checks that no SYNTHETIC finding is ever quoted as fact.

??? note "Go deeper: what is inside each phase 3 deliverable"
    - **3.1 Prioritised capabilities:** Ranking criteria · Capabilities · Variants that depend on open decis… · Feasibility dependencies · Known, assumed and open · What we are assuming · Open questions · What the PM should check first
    - **3.2 Solution research:** Approaches seen elsewhere · Proposed experience · Content needed · Design questions to test · Known, assumed and open · What we are assuming · Open questions · What the PM should check first
    - **3.3 Usability tests:** What we want to learn · Who to test with · What to test with · Consent and data handling · Tasks to give them · Capture template · Results · What the results say
    - **3.4 Early positioning and messaging:** Positioning statement · Differences from alternatives · Messages by customer group · Proof we have, proof we need · What we are assuming · Open questions · What the PM should check first
    - **3.5 Pilot plan:** Goal and questions the pilot answers · Who, where and how long · What runs in the pilot · Measures · Success and stop signals · What it needs · Risks · What would change the plan
    - **3.6 MVP scope:** In short · The six open choices · In the MVP · Not in the MVP · What must be true before build · How it fits 4 months and 4 engineers · What is untested · Risks

## Checkpoint 2

The reviewer found 18 issues before the decision (3 high, 6 medium, 9 low), including a conflict between a scope choice and a legal duty that the PM then had to resolve. See [Decisions and reviews](decisions.md).

## Phase 4: Evaluate viability

| ID | Deliverable | What it is | Mode | Builds on | Words | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| 4.1 | Legal | A legal, regulatory and security assessment template, with questions for reviewers and conditions for Gate 2. People supply the findings. | human | 3.6 | 5,035 | 33 |
| 4.2 | Risk assessment | A risk register with a rating scale, owners, stop signals and a summary by rating. | assist | 3.6 | 5,322 | 19 |
| 4.3 | Implementability | How it could be built: team and skills, architecture, integration complexity, effort against capacity, a month-by-month plan. | assist | 3.2, 3.6 | 5,364 | 15 |
| 4.4 | Product viability | Unit economics, build and run costs, break-even and cumulative cash over three years, and sensitivities. | assist | 2.10, 3.6 | 3,612 | 14 |
| 4.5 | Market viability (v2) | Market viability: market size (TAM, SAM, SOM), pilot volumes, competition, barriers to entry and timing. | auto | 1.2 | 5,077 | 19 |
| 4.6 | Measurement plan | The measurement plan: outcome measures, guardrail metrics, AI quality, cost, accessibility and privacy-respecting analytics. | assist | 2.2, 3.6 | 4,147 | 15 |
| 4.7 | Value assessment | The value to families and to the business, against cost and against the market, split into evidenced, assumed and unknown. | assist | 4.4, 4.5 | 3,733 | 12 |
| 4.8 | Pricing strategy | The pricing strategy: evidence for the fee, structure options, commission, refunds and how the price is shown. | assist | 2.7, 4.4 | 3,679 | 14 |
| 4.9 | Services review | Which services the MVP needs, the cost and effort per booked trip, and options for running them. | assist | 2.5, 3.6 | 3,921 | 15 |
| 4.10 | Final business case | The final business case for Gate 2: a draft recommendation, the case in one table, what changed since Gate 1, and each viability area in summary. | assist | 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9 | 6,001 | 19 |


**4.10 Final business case needs nine earlier deliverables**, 4.1 to 4.9, so it can only be drafted last. Notice the two ways the phase handles things the tool cannot do. **4.1** is a `human` deliverable: the tool writes the questions and the template, and the findings are supplied by reviewers (here, invented and attributed to fictional reviewer roles). The **budget estimate worksheet** is a working input, not a deliverable. It holds every assumed cost line in one place, so 4.4, 4.8 and 4.10 take their figures from one source instead of each making up its own.

??? note "Go deeper: what is inside each phase 4 deliverable"
    - **4.1 Legal:** The plan being reviewed · Questions for review · Reviewer template · Findings · What the findings mean for the plan · Conditions for Gate 2 · What we are assuming · Open questions
    - **4.2 Risk assessment:** In short · Rating scale · Risk appetite · Stop signals referred to · Owners · Risk register · Summary by rating · Inputs needed from the PM
    - **4.3 Implementability:** In short · Team and skills · Proposed high-level architecture · Integration complexity per partner · Capabilities, effort and dependenc… · Capacity against effort · What AI-DLC can and cannot speed up · Month-by-month delivery plan
    - **4.4 Product viability:** Summary for the PM · Unit economics per booked trip · Cost to build and run · Revenue: 4.5 v2 SOM scenarios reco… · Break-even and cumulative cash ove… · Sensitivity: the biggest drivers · What must be true for viability · Does the product make sense as a b…
    - **4.5 Market viability:** Changes in v2 · Summary for the PM · Size and growth · Market sizing: TAM, SAM, SOM · Pilot volumes for the MVP and firs… · Competition in the UK, for families · Barriers to entry · Timing
    - **4.6 Measurement plan:** Scope of measurement · Staged pilot: what can be measured… · Outcome measures · Guardrail metrics · AI quality metrics · Cost metrics · Accessibility metrics · Privacy-respecting analytics
    - **4.7 Value assessment:** Summary for the PM · Outcomes the MVP actually delivers · Value to UK families · Value to the business · Value against cost · Value against the market opportunity · Evidenced, assumed, unknown · Draft reading for the PM
    - **4.8 Pricing strategy:** Fixed by the PM · Summary for the PM · Evidence for setting the fee · Fee structure options · Commission by category · Fee refund and cancellations · How the price is shown · Pilot pricing
    - **4.9 Services review:** In short · What changed since 2.5 · The ten services against the MVP · Open legal point: AI-only help and… · Cost and effort per booked trip · Options for running services · Inputs the PM should supply to rep… · What we are assuming
    - **4.10 Final business case:** Recommendation for the gate · The case in one table · What changed since Gate 1 · Problem, market and customers · Solution and MVP · Evidence from testing · Viability: product, market, implem… · Legal, regulatory and security

??? note "Go deeper: what 'our arithmetic' looks like"
    Whenever the tool calculates, it says so, and the reviewer recomputes it. These lines are from the summaries of 4.3, 4.4 and 4.8. Every input is assumed, which is why each line is labelled.

    > On the SYNTHETIC numbers, variant d as scoped in 3.6 does not fit 4 months. Likely effort is 82.5 engineer-weeks against about 52.3 available: 158%, or about 6.3 months (our arithmetic, below). *(4.3 Implementability)*

    > Revenue per booked trip falls to £31 / £106 / £238 (low / mid / high), from £70 / £205 / £400 in 4.5 v2, once flights and packages are taken out (our arithmetic, assumed inputs). Each booked trip contributes £3 / £47 / £134 after card fees, disputes and AI use (our arithmetic). *(4.4 Product viability)*

    > At mid assumptions the fee cannot carry break-even on its own. To break even at mid year-3 volume (4,748 trips), the fee would need to be about £58 at 6% commission before contingency, or about £88 with 20% contingency. (Our arithmetic.) *(4.8 Pricing strategy)*

    The risk register (4.2) opens the same way: "37 risks across 12 areas. 6 are rated critical (high likelihood and high impact, our judgement)."

??? note "Go deeper: the final business case recommends, shows the alternatives fairly, and leaves the decision to people"
    > DRAFT for the decision-makers (senior management, as reported for Gate 1 and Checkpoint 2). The PM and senior management decide.
    >
    > **Draft recommendation: rework.** Do not approve the full MVP build and 12-month run yet. Main reason: the case does not yet show the product can earn back what it costs, and its only revenue source cannot yet switch on.

    It then gives the evidence (money, booking, evidence quality), what "rework" would come back with, and two other readings the gate may prefer, **approve a limited step** and **stop**, each with what speaks for and against it. What actually happened at the gate is in [Decisions and reviews](decisions.md).

## Gate 2

4.10 is the pack for Gate 2. After it, the Outcome Definition step is allowed to run, and not before.

**Next:** [Decisions and reviews](decisions.md)
