# Stage 1: Product Ideation

**The question:** is there something worth pursuing? Two phases answer it. Phase 1 is built by the **discovery agent** and ends at **Checkpoint 1**. Phase 2 is built by the **strategy agent** and ends at **Gate 1**, with the initial business case as the decision pack.

!!! info "How to read the tables"
    **Mode** is auto, assist or human (see [How each output is built](how-built.md)). **Builds on** lists the earlier deliverables each one used, which is exactly its `depends_on` header. **Words** is the length of the body. **Sources** is the number of dated sources listed in its header.

## Phase 1: Assess market and customers

| ID | Deliverable | What it is | Mode | Builds on | Words | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Problem and opportunity statement | The problem and the opportunity in plain words, with what is known, what is assumed and what is still open. | auto | PM input only | 647 | 1 |
| 1.2 | Market definition | The market: its size and growth, trends, segments, and the alternatives and competitors. | auto | 1.1 | 2,670 | 30 |
| 1.3 | Customer definition | Who the customers are, who benefits most, and who buys versus who uses. | auto | 1.1 | 2,961 | 14 |
| 1.4 | Existing research summary | What research already exists: the PM's own material plus published evidence, and where the evidence is thin. | assist | PM input only | 2,536 | 19 |


Phase 1 starts from nothing but your idea. Deliverable 1.1 is built from a short conversation. The tool asks up to four questions at a time and says why it is asking. 1.2 and 1.3 run **in parallel**, because both depend only on 1.1. 1.4 is `assist` because the PM supplies existing research, and the tool records what it was given and where the evidence is thin.

??? note "Go deeper: what is inside each phase 1 deliverable"
    - **1.1 Problem and opportunity statement:** The problem · The opportunity · What we know · What we are assuming · Open questions · Why now
    - **1.2 Market definition:** Market in one paragraph · Size and growth · Trends · Segments · Alternatives and competitors · What we are assuming · Open questions
    - **1.3 Customer definition:** Customer groups · Who benefits most, and why · Buyers and users · What we are assuming · Open questions
    - **1.4 Existing research summary:** Status of PM-supplied research · The PM's idea · Research inventory · What the evidence says · Where the evidence is thin · What is known, assumed and open · PM research that would strengthen…

    Most deliverables in the run (24 of 30) end with the same sections: **What we are assuming**, **Open questions** and **What the PM should check first**. The phase 1 files, 2.7 and 4.1 keep the first two and give the check-first list in chat instead. That is by design: a reviewer can tell at a glance what is fact and what is not.

??? note "Go deeper: a real excerpt from 1.1, the problem and the opportunity"
    > **The problem.** Families planning holidays, solo leisure travellers and people on multi-city or long-haul trips have to put a trip together themselves, across many disconnected places. They research destinations online across many tabs, then book flights in one place, hotels in another, and car hire and tours somewhere else. This takes hours, and because nothing connects the pieces, the traveller carries the whole plan in their head.
    >
    > **The opportunity.** If one assistant understood what the traveller wants from the trip and stayed with them from first idea through booking, travel and after they get home, travellers could plan and complete a trip that fits them, in a single connected flow.

    Note how it is written for a decision-maker: short, plain, and followed by the list of what it assumes and how each assumption could be checked.

## Checkpoint 1

After phase 1, a new reviewer agent checked the approved files, and the PM reported the decision in chat. It is recorded as `gates/checkpoint-1.md`: approved by the PM and senior management on 2026-10-15, with the feedback "Only leisure travel". That feedback narrowed the scope for everything after it. See [Decisions and reviews](decisions.md).

## Phase 2: Define vision and strategy

| ID | Deliverable | What it is | Mode | Builds on | Words | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| 2.1 | Use cases | The situations the product serves, in priority order, with how strong the evidence is for each. | auto | 1.1, 1.3 | 2,874 | 20 |
| 2.2 | Outcome-oriented scope | Which outcomes are in scope, what is out, and which scope decisions depend on undecided choices. | auto | 1.1, 2.1 | 1,837 | 12 |
| 2.3 | Experience strategy fit | How the product fits the company's own experience principles, use case by use case. | assist | 2.1 | 2,328 | 18 |
| 2.4 | Partnership consideration | Which partners the product would need, with phased partnership paths shown as options. | assist | 1.2, 2.1 | 3,036 | 16 |
| 2.5 | Services consideration | Which services the product offers, the ways to run each, and how each could be paid for. | assist | 2.1 | 3,517 | 15 |
| 2.6 | Team skills gaps | The skills the team has and lacks against the plan, with a checklist only the PM can complete. | assist | 2.2 | 1,903 | 7 |
| 2.7 | Pricing and billing model check | How the product could charge: the options compared, and the evidence on who pays. | assist | 1.2, 1.3 | 2,934 | 14 |
| 2.8 | Business model canvas | The business model canvas: how the product creates, delivers and captures value. | auto | 1.1, 1.2, 1.3, 2.1 | 1,854 | 24 |
| 2.9 | Vision statement | A short vision statement, what the product is not, and alternative wordings. | auto | 1.1, 2.1 | 773 | 3 |
| 2.10 | Initial business case | The initial business case for Gate 1, with a draft recommendation for the decision-makers. | assist | 1.2, 2.2, 2.7, 2.8, 2.9 | 5,028 | 26 |


Phase 2 shows the dependency order well. 2.1 Use cases needs only 1.1 and 1.3. Then 2.2, 2.3, 2.4, 2.5, 2.8 and 2.9 can run side by side. 2.7 pricing needs the market and customer work. **2.10 Initial business case needs five earlier deliverables** (1.2, 2.2, 2.7, 2.8 and 2.9), so it is the last one drafted and the one that goes to Gate 1.

??? note "Go deeper: what is inside each phase 2 deliverable"
    - **2.1 Use cases:** Priority view · What we are assuming · Open questions · What the PM should check first
    - **2.2 Outcome-oriented scope:** Outcomes in scope · Where scope depends on undecided c… · Out of scope · Scope decisions already made · What we are assuming · Open questions · What the PM should check first
    - **2.3 Experience strategy fit:** Company principles supplied · Fit by use case · What we are assuming · Open questions · What the PM should check first
    - **2.4 Partnership consideration:** Inputs from the PM · Why partners matter for this product · Partner table · Web scraping as a starting approach · Phased partnership paths · Dependencies on undecided choices · What we are assuming · Open questions
    - **2.5 Services consideration:** PM input · Services · Ways to run each service · Essential or optional · How the cost could be paid for · Dependencies on undecided choices · Known, assumed, open · What we are assuming
    - **2.6 Team skills gaps:** What the PM has told us · What AI-DLC covers and what it doe… · Skills table · Tension with the 4-month timeline · What we are assuming · Open questions · Checklist for the PM to complete · What the PM should check first
    - **2.7 Pricing and billing model check:** Inputs from the PM · What the evidence says about who p… · Options compared · Billing considerations · What the PM needs to decide · What we are assuming · Open questions
    - **2.8 Business model canvas:** Competitive context · What we are assuming · Open questions · What the PM should check first
    - **2.9 Vision statement:** Vision · What this product is not · Alternative wording · Notes for the PM · What we are assuming · Open questions · What the PM should check first
    - **2.10 Initial business case:** Recommendation for the gate · Problem and opportunity · Market and competition · Customers and who goes first · Scope and outcomes · How it earns money · Costs and investment · Benefits

??? note "Go deeper: the business case opens with a recommendation, and says whose decision it is"
    > DRAFT for the PM and senior management, who make this decision. The draft recommendation is a conditional approve: move into the next phase with a narrow UK families MVP, but release build money only once four things are in place: a budget estimate, interviews with UK families confirming the pain, a chosen supply and payment path, and a first legal view on ATOL and package travel.

    The business case is built to be read by the people who fund the work. It carries the recommendation first, then the problem, market, customers, scope, how it earns money, costs, benefits, risks and open questions, each section drawn from the deliverable that owns it.

## Gate 1

2.10 is the pack for Gate 1. Senior management approved on 2026-10-15. The record lists the evidence behind the decision, ten open risks and nine open questions carried forward. See [Decisions and reviews](decisions.md).

**Next:** [Stage 2: Planning](planning.md)
