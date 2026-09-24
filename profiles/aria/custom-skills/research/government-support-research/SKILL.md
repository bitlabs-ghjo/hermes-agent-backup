---
name: government-support-research
description: "Use when researching public grants and support programs."
version: 1.0.1
author: ARIA
license: MIT
metadata:
  hermes:
    tags: [government-support, grants, eligibility, korea, research, citations]
    category: research
---

# Government Support Research

Research public grants, R&D programs, vouchers, financing, accelerators, and
non-cash support for a specific company. Optimize for **actual eligibility and
actionability**, not for the largest headline amount.

## When to Use

Use for current grant searches, public R&D opportunity scans, regional support
matching, eligibility reviews, and next-cycle funding roadmaps. Also use when a
founder's career must be translated into a realistic public-support strategy.

## Inputs to Establish

Before ranking programs, extract or retrieve:

1. Legal entity type, opening/incorporation date, headquarters and workplaces.
2. Employee count, revenue band, industry codes, and SME/startup status.
3. Product ownership: idea, demo, MVP, paid product, IP, certification, or only
   consulting/custom-development experience.
4. Prior government R&D and commercialization awards.
5. Available partners: customer, manufacturer, hospital, university, investor.
6. Cash matching capacity and application-writing capacity.
7. Research cutoff in the program's legal timezone.

Unknowns that can change eligibility must remain explicit. Never infer product
ownership, regulatory approval, revenue, prior R&D, or a partner commitment from
the founder's career alone.

## Research Procedure

1. **Set an exact cutoff timestamp.** Use the program jurisdiction's timezone.
2. **Search official sources first.** Use the portals and agency list in
   `references/korea-portals-and-checklist.md` for Korean programs.
3. **Separate status strictly:**
   - open now;
   - announced but not yet open;
   - rolling / while budget remains;
   - closed, retained only as a next-cycle planning signal.
4. **Open the full notice and attachment.** Portal summaries are discovery
   aids, not sufficient eligibility evidence. Read the PDF/HWP or originating
   agency notice when a condition is load-bearing.
5. **Build an eligibility matrix** containing applicant type, age, location,
   industry, revenue, prior-award condition, consortium, matching funds,
   product/IP/certification, deadline, and exclusion rules.
6. **Apply hard gates before scoring fit.** A strong technical résumé does not
   override a missing consortium, region restriction, required prior R&D,
   relocation obligation, team-size rule, or different-industry incorporation
   requirement.
7. **Rank by realistic actionability:** hard eligibility → deadline feasibility
   → product/partner readiness → strategic fit → support value.
8. **Read capacity against the deadline.** For a solo company, do not recommend
   several simultaneous applications without a primary choice and a stop/go
   gate.
9. **Cite every external claim** using `grounded-citations`; verify the written
   report before delivery.

## Exhaustive Agency / Year Inventories

When the user requests **all** programs for an agency, topic, and year, completeness
within that scope takes precedence over fit-based shortlisting. Keep every relevant
program in the inventory, including closed calls; put the actionable recommendation
in a separate summary. Do not silently discard low-fit programs.

- Inspect both the current support board and legacy/global search. A global search
  may omit a newer JavaScript-backed board. An empty HTML table or missing search
  parameter is not evidence of zero programs: inspect the form and page scripts,
  then retrieve the public read-only endpoint actually used by the page.
- Search topic variants and reconcile the year’s board listings where practical.
  Save each batch with stable notice IDs; paginate to the declared total, dedupe,
  and compare collected counts programmatically. Check prior-year announcements
  that explicitly concern the target year rather than filtering only by posting date.
- Report three distinct counts: parent programs, recruitment notices/rounds, and
  unique support tracks. Never sum repeat-round budgets without evidence that they
  are separate appropriations.
- Build a round-by-track matrix. Compare attached notices for changed eligibility,
  facilities, supported items, deadlines, and cash versus in-kind support. A stale
  form heading does not establish that an omitted track was reopened.
- Read every relevant full notice; verify extraction coverage per page and visually
  inspect merged tables carrying important amounts or area thresholds. Record
  conflicting age/date ranges and specific versus general matching-fund clauses
  without choosing the more favorable interpretation.
- Separate press-release plans, networking events, proposed R&D, and historical
  results from actionable recruitment calls. Clearly state the coverage boundary:
  publicly discoverable topic-specific calls as of the cutoff, not unpublished
  plans, all future annual calls, or every generic grant that might admit the sector.

For the validated Ulsan TP current-board/global-search retrieval pattern, see
`references/agency-board-inventory.md`.

## Identifying Unnamed Programs and Supplier Routes

When the user only recalls a promotional claim (for example, “AI training is
90% reimbursed”), investigate the claim rather than requiring the user to find
the original video. Search the benefit phrase with the beneficiary, subject,
year, and provider-recruitment terms. Treat matching programs as candidates,
not proof of which video the user saw. Ask for a link only if unresolved
ambiguity materially changes the recommendation after research.

For supplier participation, distinguish the purchasing company's eligibility
from the training provider's eligibility and individual course approval. Read
the provider recruitment attachment before recommending certification or a
partner-only route: a specific scheme may explicitly admit uncertified
providers even when other vocational-training schemes require certification.
Check infrastructure evidence, instructor credentials, application documents,
and sole-proprietor treatment separately. An absent exclusion is not confirmed
eligibility, and eligibility is not selection.

Explain who receives the reimbursement, its calculation base (actual paid fee
versus a reference rate), limits, and conditional regional uplifts. Do not
transfer generic reimbursement rules to a named scheme. Separate provider
application deadlines from learner enrollment dates; ongoing classes do not
prove supplier recruitment is open. If primary evidence changes an earlier
recommendation, explicitly correct it.

For a worked official-source example and retrieval approach, see
`references/korean-training-provider-research.md`.

## Small Manufacturing Projects: Demand, Funding, and Delivery

For bitlabs, rank a narrow, evidence-backed field problem before optimizing for
subsidy size. Keep **commercial validation priority** separate from **fit to a
currently open program**; they may be different items. Ease of implementation
is not proof of repeated pain or willingness to pay. A historical RFP supports
only the problem it actually states: for example, fragmented alarm handling
does not itself prove duplicate alarms. Label the proposed smaller feature as
a product hypothesis.

Before recommending a supplier route, trace the money and continuing duties:
who applies, spends first, receives reimbursement, and may invoice whom;
allowed expense categories; VAT and excluded costs; supplier registration;
new-company substitutes for missing historical financial statements; sole-owner
participation evidence; pre-award work exclusions; source-code/model/data
submission or publication; and multi-year logging or maintenance obligations.
Do not equate a consortium's support ceiling with the supplier's revenue.
A broad phrase such as “source-code implementation” does not settle whether
supplier development fees are eligible when the expense table lists only
materials and infrastructure.

Search additional, second-round, amended, and reopened notices before declaring
a program closed. Reconcile the same program across workers using notice IDs,
publication dates, attachments, and jurisdiction-local time. Preserve conflicting
clauses inside an official notice—such as a fixed deadline alongside an
undated early-closure warning, or email versus online submission—and request
operator confirmation rather than silently choosing one.

For a solo firm, favor one team, one document type or line, exported/read-only
inputs, and human confirmation. Compare existing tools and deterministic rules
before adding AI. Set performance thresholds after measuring the customer's
baseline and error costs; do not invent uniform accuracy or time-saving targets.
When a consortium deadline is close and no qualified partner is already ready,
recommend deferral rather than hastily assembling a partnership. AI staff do
not satisfy human headcount requirements.

See `references/manufacturing-microproject-due-diligence.md` for a worked
source-reading example and the validated official-portal retrieval pattern.

## Next-Cycle Portfolio Planning

When asked to maximize next year's support, optimize net business benefit and
credible delivery capacity, not application count or headline ceilings.

- Maintain separate ledgers for grants/R&D, vouchers/in-kind benefits, supplier
  revenue, and loans/guarantees. Never sum them into a promised funding total.
- For a solo firm, choose one primary commercialization application and one
  fallback. Treat local complementary support, education revenue, and technical
  R&D as distinct routes with explicit readiness gates—not an automatically
  compatible bundle.
- Search next-year notices already published this year. Distinguish operator,
  consortium organizer, supplier-pool, course-provider, and beneficiary calls;
  an operator call does not open company applications. Label projected dates
  and budgets separately from announced terms.
- Audit video-based advice against exact program identities. Similar names such
  as a scale-up “Jump-up” program and technology-readiness “TRL Jump-up” do not
  share budgets or eligibility. Follow the budget's reform/renaming language.
- Look for next-cycle technical-demand surveys already open this year; do not
  wait for the month predicted in a video. Read the original poster and form:
  an unmatched-technology option may allow a survey submission without meeting
  the later grant's technology-transfer gate. Survey participation is neither
  RFP adoption nor award selection. Separate prior-cohort phase 2 from the next
  cohort's phase 1, and keep schedule diagrams labeled as provisional.
- Record each matching percentage's denominator: total project cost, grant
  amount, or applicant contribution. Copy the official example and calculate
  with tools. If wording and example disagree, preserve the conflict and defer
  the budget decision to written operator clarification.
- Test duplicate funding at application, selection, commitment letter,
  agreement, and expenditure stages. One program's local-government exception
  does not override the other program's restrictions or permit double charging.
- Downgrade supplier routes to exploration when only purchaser notices were
  verified. Do not transfer a legal-entity, staffing, or registration rule from
  a similarly named scheme.
- Build a month-by-month preparation plan around owned-product evidence,
  demand validation, rights, common application documents, cash flow, and
  actual human workload. Label interview/MVP targets as internal proposals,
  not official requirements or completed achievements.
- Count unique programs separately from rounds, demand/supply routes, exclusions,
  and non-cash institutions. A large research appendix is not a count of
  eligible applications. Keep the decision summary selective.

See `references/next-cycle-portfolio-review.md` for financial-denominator,
parallel-review, and evidence-quality checks with dated research examples.

## Program Fit Categories

Use these labels consistently:

- **Apply now:** all hard gates appear satisfied and required evidence/partner
  can be assembled before the deadline.
- **Apply after one check:** one retrievable fact or partner confirmation remains.
- **Partner only:** company cannot lead but can join an eligible consortium.
- **Capability-building:** consultation, testing, certification, export booth,
  or training rather than cash.
- **Next-cycle pipeline:** closed this year; useful for concrete preparation.
- **Exclude:** a hard gate conflicts with known facts.

## Item-First Commercialization and R&D Proposals

When the request is for **business ideas for grants or R&D**, lead with product
opportunities, not a grant catalogue. Deliver at least the requested number of
distinct items and verify the count. Reusing the same document engine across
workflows is not by itself evidence of distinct customer demand.

For each item state the paying customer, exact costly task, source-backed problem,
proposed narrow MVP and exclusions, existing non-AI/commercial alternative,
technical uncertainty, data rights and ground-truth owner, evaluation design,
revenue model, and stop/go condition. Label proposed durations and sample sizes
as planning assumptions conditional on data readiness, not validated estimates.

Rank **commercial validation** and **R&D suitability** separately. A useful
rules/OCR/RAG integration can be a viable product without being a defensible R&D
project. Research framing needs a specific unresolved technical problem, a
baseline, independent test data, and a measurable improvement hypothesis. Do not
inflate scope merely to fit funding. For a solo firm, name one lead product and
one conditional alternative rather than recommending simultaneous development.

Historical RFPs establish the stated historical problem; later implementation
reports strengthen evidence of feasibility, not proof of present unmet demand.
Separate current purchasing intent from both. Mark adjacent ideas with no direct
problem evidence as exploratory rather than ranking them highly for ease of build.
Keep expected effects, RFP targets, and measured outcomes distinct.

See `references/item-first-rd-proposals.md` for a worked evidence bank and
technical evaluation patterns. Re-fetch dated sources before using them for
current eligibility or market claims.

## Required Output

For item-first requests, use the structure above, followed by a short conditional
funding-route map and next-cycle preparation plan. Do not force an immediate-open
opportunity or deadline into an ideation request.

For program-search requests, lead with a decision, then provide:

1. Top 1–3 immediate opportunities with deadline and days remaining.
2. Exact support form: grant, voucher, R&D reimbursement, loan/interest subsidy,
   in-kind service, competition prize, or export support.
3. Hard eligibility and unresolved checks.
4. Why the company's **owned product and evidence** fit—not merely why the
   founder's résumé sounds related.
5. A recommended project framing.
6. Excluded attractive-looking programs and the disqualifying reason.
7. A 3–6 month and next-cycle preparation pipeline.
8. Official source links and a verified report artifact when the task is broad.

## Citation and Parallel-Research Discipline

- Create a task-specific citation ledger. Do not let concurrent workers reset or
  mutate the default ledger.
- Give each subagent a unique ledger, or have subagents return URLs without
  numbering and register the deduplicated URLs in one parent-owned final ledger.
- Never merge prose that carries child-local citation numbers.
- Render the final Sources block mechanically and run strict verification.

## Common Pitfalls

- Ranking a large grant above a small program despite a hidden hard-gate failure.
- Treating `while budget remains` as proof that funds remain; verify with the
  operator before application.
- Calling a loan, guarantee, booth, consultation, or in-kind service a grant.
- Assuming an existing founder can use a program that requires a new business or
  a different industry code.
- Assuming one-person status is allowed merely because the summary omits a
  minimum headcount; state that the full notice showed no exclusion and confirm
  when material.
- Recommending healthcare support based only on consulting history when the
  notice requires a company-owned product, device registration, clinical site,
  or hospital consortium.
- Recommending a consortium program without naming the missing partner and the
  deadline for securing it.
- Reusing annual program dates or amounts as future facts. Mark next-year terms
  unannounced and use the prior notice only as a preparation reference.
- Dumping all discovered programs into a recommendation-only answer. Shortlist
  by fit when that is the request; for an explicit **all-programs inventory**, keep
  every in-scope item and separate the selective recommendation from the full list.

## Verification Checklist

- [ ] Cutoff timestamp and timezone stated.
- [ ] Every recommended program is open/announced as labeled.
- [ ] Full notice or attachment checked for hard gates.
- [ ] Support type is named accurately.
- [ ] Known facts, inferred fit, and unresolved checks are separated.
- [ ] Deadline arithmetic is tool-computed.
- [ ] Solo-company workload has a primary recommendation and fallback.
- [ ] Closed programs are clearly separated from current opportunities.
- [ ] Citation ledger is isolated from parallel workers.
- [ ] Sources block and citation coverage verify successfully.
