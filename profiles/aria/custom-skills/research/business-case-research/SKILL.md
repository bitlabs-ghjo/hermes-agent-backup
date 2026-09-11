---
name: business-case-research
description: "Use when researching real company use cases and ROI."
version: 1.0.0
author: ARIA / bitlabs
license: MIT
metadata:
  hermes:
    tags: [research, case-studies, youtube, roi, reports]
    related_skills: [grounded-citations, youtube-content]
---

# Business Case Research

Produce decision-ready reports on how named or comparable organizations use a technology in real work. Separate observed workflows from vendor claims, cross-check quantitative outcomes, and turn the findings into a practical recommendation.

## When to Use

Use for requests such as:

- “Find examples of companies using AI in their work.”
- “Research real-world cases on YouTube.”
- “Compare adoption patterns and ROI.”
- “Write a management report from customer stories.”

Load `youtube-content` when videos are in scope and `grounded-citations` for the source ledger. This skill adds business-case selection, evidence grading, synthesis, artifact QA, and approved delivery. For regional SME audiences that know AI matters but cannot identify a first use case, also read `references/regional-sme-ai-adoption-reports.md` and frame the report around business loss, data readiness, a measurable pilot, and human approval.

## Workflow

1. **Define the decision.** Infer the default scope when harmless; ask only when industry, geography, confidentiality, cost, or external distribution materially changes the work.
2. **Build a balanced candidate set.** Cover several functions such as sales, customer support, knowledge work, development, operations, and regulated work. Prefer implemented workflows over demos and future plans.
3. **Collect source material progressively.** Save each video transcript and metadata result to disk as it is retrieved so long or interrupted runs do not lose progress. For exact commands and fallbacks, read `references/youtube-evidence-and-delivery.md`.
4. **Cross-check every selected case.** Pair the video with a first-party company page, press release, technical blog, or credible independent report when available.
5. **Grade the evidence.** Label each important result as one of:
   - independently verified;
   - company self-report;
   - vendor-produced customer story;
   - limited pilot;
   - rollout plan / no measured ROI.
6. **Extract a standard case record.** Capture company, industry, job-to-be-done, AI/tool, workflow before/after, metric, measurement caveat, video title/channel/date/URL, timestamps, official corroboration, and transferable lesson.
7. **Synthesize across cases.** Identify repeated success conditions, failure modes, and the smallest useful pilot. Do not merely list examples.
8. **Draft for executives.** Lead with the conclusion and recommended action. Put detailed cases in a compact table, then add common patterns, risks, and a 30/60/90-day plan with measurable gates.
9. **Verify citations and artifact structure.** Run the citation ledger verifier. For table-heavy reports, also audit table rows explicitly because prose-coverage statistics exclude Markdown table rows.
10. **Deliver safely.** External or cross-channel posting requires the exact approved recipient, body, attachments, and links. After sending, read back the destination and verify both text and attachments before reporting success.

## Selection Rules

Prefer cases that disclose at least one of:

- adoption scale or active-user rate;
- elapsed time before/after;
- cost, revenue, or throughput impact;
- error, repeat-contact, or quality change;
- controls such as source citations, permissions, audit logs, evaluations, or human approval.

Exclude or clearly downgrade:

- product demos presented as customer outcomes;
- planned deployments described as completed rollouts;
- metrics without a denominator, baseline, period, or definition;
- the same vendor claim repeated by secondary sites without independent evidence.

## Reporting Pattern

Use this order unless the user requests another format:

1. Decision summary
2. Recommended action
3. Case comparison table
4. Cross-case patterns
5. Risks and evidence limits
6. 30/60/90-day implementation plan
7. Source list

Each case row should answer: **What changed in the workflow, what measurable result was reported, how strong is the evidence, and what should the reader copy?**

## Pitfalls

- Do not treat transcript auto-captions as exact quotes without checking timestamps and context.
- Do not call vendor-reported numbers “proven ROI.” Preserve the source’s own qualifiers such as estimate, pilot, or user-reported.
- Do not use a search snippet to support a claim that requires the full page or transcript.
- Do not let a citation coverage percentage hide uncited table claims; tables need a separate row-level citation check.
- Do not register sources after drafting from memory. Add URLs to the citation ledger as they are retrieved.
- Do not announce delivery from a successful send command alone. Verify the exact channel, message text, and attachment name by reading the target back.

## Verification Checklist

- [ ] Requested scope and case count are met.
- [ ] Every case has a working video URL and identifying metadata.
- [ ] Quantitative claims carry an evidence label and citation.
- [ ] Rollout plans are not described as measured outcomes.
- [ ] Table rows with external facts include citations.
- [ ] Executive recommendations follow from the observed patterns.
- [ ] Generated HTML/PDF has the intended headings, tables, links, source anchors, and footer.
- [ ] Any approved external delivery was read back from the exact target.
