---
name: enterprise-case-study-research
description: "Use when researching enterprise adoption case studies."
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Research, Enterprise, Case Studies, YouTube, Evidence, Reports]
    related_skills: [youtube-content, grounded-citations]
---

# Enterprise Case Study Research

Produce decision-ready research on how named organizations apply a technology in real work. This skill is for reusable case-study classes—not product tutorials or one-video summaries. It composes `youtube-content` for transcript evidence and `grounded-citations` for claim-to-source integrity.

## When to Use

Use for requests to investigate how companies apply AI, automation, cloud, developer tools, or another technology in actual operations—especially when the evidence includes YouTube talks, conference videos, customer stories, and claimed business outcomes. Do not use it for a single-video summary, a generic product tutorial, or academic literature review.

## Required Output

Unless the user specifies otherwise, deliver:

1. Executive conclusion and recommended action.
2. A case table with organization, workflow, implementation, disclosed result, evidence status, and transferability.
3. Cross-case patterns and failure risks.
4. A phased adoption recommendation with measurable KPIs.
5. A source list containing the exact video and corroborating official pages.

## Procedure

1. **Define selection criteria before searching.** Balance recency, industries, business functions, organization sizes, and quantified versus qualitative outcomes. Prefer first-party presentations by the adopting company or a platform channel carrying a named customer speaker.
2. **Collect candidates, then shortlist.** Reject generic demos, hypothetical use cases, anonymous marketing clips, and videos that do not identify the operational workflow.
3. **Capture video metadata mechanically.** Record video ID, exact title, channel, upload date, and duration. Use compact metadata output rather than full extractor JSON; full JSON can be extremely large and is unnecessary for a research ledger.
4. **Fetch timestamped transcripts.** Validate that transcript text is non-empty and in the expected language. When automatic selection returns no transcript, retry with explicit likely source-language codes before concluding captions are unavailable.
5. **Extract evidence windows.** For every case, save the smallest timestamp range that supports the workflow and any quantitative result. Do not cite a whole keynote as if every claim were verified.
6. **Cross-check quantitative claims.** Look for the adopter's newsroom, investor material, official customer story, or product-provider case page. Mark the origin of every metric: adopter-reported, vendor-reported, third-party reported, or independently verified.
7. **Separate fact from interpretation.** Facts describe what the source states. Interpretation explains why it may transfer. Recommendations state what the client should test. Do not merge these layers.
8. **Build the citation ledger before drafting.** Register sources as retrieved, cite sentence-by-sentence, render the source block mechanically, and verify before delivery.
9. **Draft for decision use.** Rank cases by relevance to the user's operating model, not by brand size or headline metric.
10. **Verify the artifact.** Check named case count, unique sources, timestamp links, citation targets, table completeness, declared caveats, and requested file format.

## Evidence Labels

Use one of these labels in working notes or the final table:

- **A — Corroborated:** video/transcript plus a separate official adopter or provider source.
- **B — First-party single source:** named company speaker or official company publication, not independently corroborated.
- **C — Vendor claim:** result appears only in the vendor's marketing material.
- **D — Illustrative:** qualitative workflow with no published measured outcome.

Never present C or D as audited ROI. If a number is an estimate, retain words such as “estimated,” “projected,” or “equivalent workload.”

## KPI Translation

Translate cases into measurable pilot hypotheses:

- Search and summarization: time to locate the correct source, citation accuracy, stale-document errors.
- Drafting: time to approved final, human edit ratio, rework rate—not generation time alone.
- Customer support: containment rate, resolution time, repeat inquiry rate, escalation quality.
- Development: cycle time, review defects, test pass rate, rollback frequency—not lines of code.
- Sales: preparation time, follow-up latency, qualified conversion, attributable revenue.

## Pitfalls

- **Headline-number copying:** Large savings often come from self-reported or extrapolated calculations. Preserve attribution and methodology caveats.
- **Timestamp-free citations:** A video URL alone makes verification expensive. Include the supporting segment.
- **One keynote, many cases:** A compilation may mention many brands but give evidence for only a few. Count only cases with a concrete workflow.
- **Tool adoption mistaken for transformation:** Licenses and active-user counts are inputs. Process redesign and approved-output KPIs are outcomes.
- **Ignoring negative evidence:** Cost, weak usage visibility, security gaps, and failed pilots are often more transferable than success claims.
- **Over-generalizing enterprise scale:** State explicitly which practices fit small teams and which require enterprise data, governance, or integration budgets.
- **Large transcript capture:** Do not depend on a tool's displayed stdout for long transcripts. Persist the complete transcript first, then parse or chunk the saved file.
- **Misreading citation coverage:** Markdown-table rows may be excluded from prose coverage statistics even when their claims are cited. Inspect the tool's counting rules, verify source IDs and rendered links separately, and do not weaken citation quality merely to raise a misleading percentage. Also remove or cite ledger entries before strict verification so unused-source warnings do not mask real failures.

## Supporting Reference

See `references/youtube-evidence-workflow.md` for compact commands, transcript fallback order, evidence-window extraction, and verification checks.

## Completion Gate

Before reporting completion, verify:

- Every promised case is present and counted programmatically.
- Every quantitative claim has an evidence label and source.
- Vendor-reported values are not described as independent facts.
- Each video case includes title, channel, upload date, URL, and useful timestamp where available.
- Recommendations contain owner/action/KPI/timebox or clearly state that these remain for user decision.
- The final artifact opens, has no broken internal citation links, and matches the user's requested format.
