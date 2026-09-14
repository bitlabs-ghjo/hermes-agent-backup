---
name: business-research-reporting
description: "Use when creating or routing business research reports."
version: 1.0.1
author: MIRA
license: MIT
created_by: agent
metadata:
  hermes:
    tags: [research, reporting, html, executive, scheduled-reports, delivery]
---

# Business Research Reporting

Use this skill for market, opportunity, competitor, trend, and internal decision-support reports. It governs the **report artifact and delivery workflow**; pair it with domain skills such as `grounded-citations` or `government-program-research` for evidence collection.

## When to Use

Load this skill when a task includes any of the following:

- a market, opportunity, competitor, trend, or executive research report;
- an HTML or downloadable report artifact;
- delivery to a named decision owner or designated report channel;
- changing the output format or routing of a recurring report;
- verifying whether a report is prepared, posted, scheduled, or actively running.

## Outcomes

Produce a report that:

1. lets an executive decide from the first screen;
2. distinguishes fact, interpretation, hypothesis, and recommendation;
3. makes every material claim traceable to an original source;
4. is delivered in the requested format and route;
5. is verified rather than merely described as sent or scheduled.

## Workflow

### 1. Establish the decision contract

Extract or infer:

- intended decision and decision owner;
- deadline and urgency;
- scope, geography, industry, and exclusions;
- required artifact format;
- delivery target and whether the target is a person, channel, or system;
- confidentiality constraints.

If the request is sufficiently specific, proceed without a redundant clarification.

### 2. Build the report executive-first

Default order:

1. urgent or decision-blocking issue;
2. one-page executive summary;
3. major findings;
4. evidence and data;
5. business impact;
6. opportunities and risks;
7. recommendation and next actions;
8. source list.

Put the requested decision, deadline, owner, and approval need before background detail. Do not bury a stopped scheduler, missed deadline, disqualifying condition, or material evidence gap at the end.

### 3. Separate epistemic labels

Use explicit labels where ambiguity matters:

- **Fact:** directly supported by a source or verified system state.
- **Interpretation:** reasoned meaning derived from facts.
- **Hypothesis:** testable but not yet verified.
- **Recommendation:** proposed action, including owner and timing.

Do not present scores, estimates, or market-size assumptions as measured facts.

### 4. Produce HTML when requested

When the user asks for HTML reporting, produce a standalone HTML5 document rather than Markdown wrapped in a code block.

Minimum contract:

- UTF-8 and Korean-language metadata when applicable;
- responsive layout;
- printable CSS (`@media print`);
- semantic headings, tables, lists, and links;
- visible source numbers linked to a source list;
- no external scripts, trackers, or remote fonts unless explicitly approved;
- no confidential identifiers beyond the approved audience and purpose;
- a concise decision panel near the top.

If file tools are available, save as `.html` and validate that the file exists and contains the expected title and closing HTML structure. Otherwise return the complete HTML document directly.

See `references/html-report-delivery.md` for the detailed artifact and routing checklist.

### 5. Route reports accurately

Distinguish these claims:

- **Prepared:** artifact exists locally.
- **Posted:** delivered to a channel and read back or otherwise verified.
- **Sent to a person:** delivered to an exact verified recipient handle or address.
- **Scheduled:** job definition exists.
- **Active:** scheduler/gateway is running and the next execution is expected to fire.

Never equate posting in a shared channel with notifying a named person unless the person’s verified mention or direct destination was used. If only a display name is known, address the person in prose and state the routing limitation instead of inventing an identifier.

For reports routed through an internal report channel, post the full artifact once in the designated report channel. In the originating channel, leave only a short status and pointer unless the request explicitly requires duplication.

### 6. Update recurring reports safely

When changing a scheduled report’s output format or audience:

1. list the job and identify it by exact job ID;
2. retrieve the full existing prompt from an authoritative store;
3. preserve all research requirements and append or edit only the format/routing contract;
4. update the job;
5. read back the exact job definition to confirm the new clauses;
6. separately check scheduler activity and surface inactivity as a blocker.

Do not replace a long job prompt with a short addendum. A successful update call proves persistence, not that future runs are active.

### 7. Final verification

Before reporting completion, verify:

- every requested section is present;
- titles, dates, totals, scores, and links are internally consistent;
- critical source links point to original material where available;
- the artifact format matches the request;
- the delivery target is exact and authorized;
- any external write has been read back;
- scheduled and active states are reported separately.

## Pitfalls

- Saying “reported to ARIA” when only a channel post was made and no verified ARIA destination was used.
- Claiming a recurring report will run because its job is saved while its scheduler is stopped.
- Updating only the visible prompt preview instead of preserving the full prompt.
- Returning Markdown when the request was for a downloadable HTML artifact.
- Repeating the full report in both the work channel and the report channel.
- Hiding evidence gaps or operational blockers below the source appendix.

## Pairing

- Use `grounded-citations` for source quality and claim-to-source mapping.
- Use `government-program-research` for grants and public support programs.
- Use document or browser skills when HTML must be rendered, visually checked, or converted to PDF.