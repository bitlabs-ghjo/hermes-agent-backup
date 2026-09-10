---
name: government-program-research
description: "Use when evaluating government grants and support programs."
version: 1.0.0
author: MIRA
license: MIT
metadata:
  hermes:
    tags: [government-support, grants, eligibility, startup, business-planning, research]
    category: research
---

# Government Program Research

## Purpose

Turn a government-support request into a decision-ready recommendation: whether the organization can apply, which item or project to submit, what could disqualify it, and what must happen before the deadline.

## When to Use

Use for national or regional grants, startup-support programs, R&D calls, commercialization funding, vouchers, competitions, and requests to choose an application item. It is especially important when the applicant is already operating a business, because eligibility may depend on business age, five-digit KSIC classification, duplicate funding, or a required new entity.

## Source Order

1. Official announcement page.
2. Official notice and attachments (PDF/HWPX/XLSX); attachments govern when summaries conflict.
3. Official administering-agency FAQ, management rules, evaluation criteria, and schedule.
4. Official regional implementing body.
5. Independent reporting only for competition signals, market context, or operational experience.

Never conclude from a search-result snippet when the underlying notice is available. If a PDF download endpoint fails, locate an official mirror or CDN copy, extract the full text, and retain the official announcement URL for traceability.

## Procedure

### 1. Establish urgency and decision question

- Check the current local time and calculate time remaining to the exact closing time.
- State urgent deadlines and disqualifying conditions at the top.
- Define the decision as `apply / do not apply / apply only if conditions are met`.

### 2. Build an eligibility gate before ideation

Extract and cite:

- Applicant type and required legal entity.
- Business age window and the date used to calculate it.
- Headquarters, regional, industry, and company-size requirements.
- Excluded industries, tax/default restrictions, sanctions, and account requirements.
- Simultaneous-performance and duplicate-funding exclusions.
- Stage-specific obligations such as incorporation, new registration, insurance, bank accounts, or matching funds.

For existing founders, compare the applicant's current business activities with the notice's exact new-business rule. When the notice uses the Korean Standard Industrial Classification, compare **five-digit KSIC codes**, not broad labels such as “AI,” “education,” or “consulting.” Treat an item as conditionally eligible until the implementing agency confirms ambiguous classification or 창업기업 recognition.

### 3. Separate eligibility from attractiveness

A strong business idea can still be ineligible. Report two judgments independently:

- `Eligibility`: confirmed / conditional / ineligible.
- `Program fit`: high / medium / low.

Do not recommend an item until both are acceptable.

### 4. Generate and screen application items

Generate 3–5 candidates connected to the applicant's capabilities and customer access. Score them with explicit weights such as:

- Eligibility and classification distance: 25.
- Severity and frequency of customer problem: 25.
- Differentiation from direct competitors and substitutes: 20.
- MVP feasibility within program schedule and budget: 15.
- Applicant capability and evidence access: 15.

Scores are analysis, not external facts; label them as such. Reject generic “AI platform” framing when the field is crowded. Prefer a narrow user, moment of pain, measurable result, and evidence that can be collected before submission.

### 5. Perform a competitor disconfirmation check

Search for direct products, public substitutes, and manual workarounds. If a competitor already offers the proposed headline functionality, do not hide it. Reframe around a distinct job-to-be-done, workflow boundary, buyer, or proof mechanism. State the conditions under which the item would merely be a weak copy.

### 6. Design the minimum credible evidence package

Before submission, seek:

- 2–5 customer interviews.
- One anonymized sample workflow or document.
- A five-screen prototype or a 30–60 second demo when allowed.
- One quantified baseline and target metric.
- Evidence of the founder's readiness, access, and execution history.

For programs using AI-generation or plagiarism screening, keep the applicant's own observations, interview findings, and decisions prominent. AI may structure and edit; it must not fabricate field evidence or imitate a generic winning proposal.

### 7. Produce the decision report

Use this order:

1. Urgent alert and bottom-line recommendation.
2. One-page executive summary.
3. Program facts and exact eligibility.
4. Recommended item: customer, problem, value proposition, MVP, exclusions, pricing hypothesis, launch plan.
5. Candidate comparison and scoring method.
6. Competitors and substitutes.
7. Implications, risks, and mitigations.
8. Go/no-go gates, documents, estimated preparation time, and reverse schedule.
9. Cited source list with issuer and publication or verification date.

Label every material statement as fact, interpretation, hypothesis, or recommendation where ambiguity could matter.

## Verification Checklist

- [ ] Exact deadline and timezone verified.
- [ ] Official notice and all relevant attachments read.
- [ ] Applicant's incorporation/opening date checked against the notice.
- [ ] Current and proposed five-digit KSIC codes compared when applicable.
- [ ] Duplicate-funding and simultaneous-performance exclusions checked.
- [ ] Stage-specific registration/incorporation obligations captured.
- [ ] Funding amount, self-payment, payment method, and tax treatment verified.
- [ ] Regional quota or preference distinguished from guaranteed advantage.
- [ ] Direct competitors and free/public substitutes checked.
- [ ] Market-size math labels assumptions and avoids presenting an upper bound as obtainable revenue.
- [ ] Submission itself has not been made without explicit approval.
- [ ] Final report routed to the required internal destination and delivery receipt recorded.

## Pitfalls

- Treating “anyone may apply” as proof that an existing company is eligible.
- Confusing a different product name with a legally distinct industry.
- Assuming that adding an 업태/종목 to an existing registration satisfies an 이종창업 requirement.
- Recommending a crowded AI idea without searching for direct functional competitors.
- Presenting a seat-count multiplication as a validated market size.
- Focusing on the maximum prize while ignoring early-round support and later-stage obligations.
- Claiming a report was posted without a platform receipt or verifiable message identifier.

## Reference Notes

- See `references/modoo-startup-2026.md` for a worked example of eligibility-first item selection for an existing Korean founder.
