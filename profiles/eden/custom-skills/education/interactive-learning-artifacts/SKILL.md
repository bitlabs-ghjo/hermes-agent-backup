---
name: interactive-learning-artifacts
description: "Use when building researched interactive HTML lessons."
version: 1.0.0
author: EDEN Curator
license: MIT
metadata:
  hermes:
    tags: [education, html, microlearning, instructional-design, interaction, verification]
    category: education
---

# Interactive Learning Artifacts

Build self-contained HTML learning materials that turn researched concepts into observable learner actions. Use this skill for interactive explainers, microlearning pages, workshop handouts, browser-based worksheets, and facilitator-ready HTML reports.

## When to Use

Use when the requested deliverable is both instructional and browser-based, especially when it needs research, citations, learner interactions, an embedded worksheet, responsive rendering, or a facilitator appendix. For a non-interactive lesson plan use `instructional-design`; for a general landing page or product prototype use `claude-design`.

This skill complements rather than replaces:

- `instructional-design` for outcomes, practice, assessment, and facilitation logic.
- `grounded-citations` for source ledgers and claim verification.
- `claude-design` for composition, visual quality, accessibility, and responsive behavior.

## Core Standard

A finished artifact must be more than a styled article. It must let the intended learner explain, decide, classify, write, test, or revise something, and it must be exercised in a real browser before delivery.

## Procedure

1. **Frame the learning brief.** Identify audience, prior knowledge, duration, environment, required action, output, and distribution scope. If details are missing, choose a safe default and state it visibly in the artifact.
2. **Define observable outcomes.** Limit a short microlearning artifact to two or three behaviors. Pair every outcome with an interaction, worksheet field, quiz item, or performance check.
3. **Research before designing.** Prefer official product documentation for behavior, limits, versions, pricing, and security. Add independent reporting when vendor claims need context.
4. **Create a cited research memo first.** Populate the citation ledger at retrieval time, write a short claim-and-caveat memo, render its Sources block mechanically, and pass citation verification before converting the content into HTML.
5. **Separate fact, interpretation, and illustration.** Mark vendor claims as claims, educational analogies as analogies, and simulated outputs as illustrative—not live model results. Never let polished UI make a fictional result look measured.
6. **Choose one learning surface.** Default to a `Decide / Learn` composition: one core idea per section, progressive disclosure, and a clear path from explanation to guided practice to independent transfer. Avoid dashboard or generic feature-grid framing.
7. **Build a learning progression.** Use this order when appropriate: hook → outcomes → simple analogy → process → guided demo → limitation or error case → knowledge check → workplace transfer → facilitator appendix → sources.
8. **Design interaction for the concept.** Use controls that expose the underlying decision, not decorative animation. Good examples include threshold sliders, compare/reveal states, sortable evidence, branching scenarios, and instant-answer feedback.
9. **Teach uncertainty and human review.** Show when the system may act, when it should verify, and when it must escalate. Risk level and error cost belong beside confidence; confidence alone is never an automatic deployment rule.
10. **Include a low-dependency fallback.** Make the page useful without logins, network access, or external APIs. When a live service is optional, include synthetic input and an explicitly labeled simulated result.
11. **Add the facilitator layer.** For instructor-led use, include an exact timed run sheet, concise script cues, pre/post checks, completion criteria, satisfaction items, security reminders, and failure-path alternatives. Put these in collapsible sections when learner-facing density would otherwise suffer.
12. **Build a portable artifact.** Prefer one HTML file with embedded CSS and JavaScript, semantic sections, visible focus states, print styling, responsive layouts, and no remote dependency unless justified.
13. **Verify mechanically and visually.** Run the checks below. Fix failures before distribution or reporting completion.

## Educational Anatomy

A practical general-audience page usually needs:

- A plain-language title framed around a familiar problem.
- Two or three observable outcomes.
- One analogy that preserves the important distinction without pretending to be exact.
- A process diagram of three to five steps.
- A comparison table for easily confused concepts.
- One guided example with an explicit provenance label.
- One error case or limitation.
- A short quiz with corrective feedback.
- A workplace-transfer worksheet.
- Human review, privacy, and deployment boundaries.
- A source list with check date.

Remove any section that does not support an outcome or the transfer artifact.

## Research and Claim Discipline

- Cite every changing product fact in the HTML and in the research memo.
- Distinguish type/schema validity from decision correctness.
- Treat vendor benchmarks as vendor evidence unless independently reproduced.
- Do not convert phrases such as “zero hallucinations,” “reliable,” or “faster” into unconditional facts.
- State version and review date for model limitations.
- Use original examples and visuals; do not reproduce social posts, screenshots, or vendor diagrams without permission.

## Interaction Rules

- Every button must change a visible learning state.
- Feedback must explain why, not only say “correct” or “wrong.”
- Slider or threshold demonstrations must expose the policy assumption and warn that real thresholds require validation data.
- Simulations must say `교육용 가상 출력`, `illustrative`, or an equivalent label next to the result.
- Preserve touch targets of at least 44 px and keyboard focus visibility.
- Respect `prefers-reduced-motion`; do not require motion to understand content.

## Verification Pipeline

Use a layered gate so a visually polished page cannot hide technical or instructional failure.

1. **Source gate**
   - Citation ledger populated from retrieved URLs.
   - Research memo passes citation verification.
   - Every numbered citation in HTML maps to the same ledger URL.
2. **Structure gate**
   - Parse HTML successfully.
   - Detect duplicate IDs and broken internal anchors.
   - Confirm required sections, quiz count, source count, and exact duration total.
3. **Script gate**
   - Extract embedded JavaScript and run a syntax check.
4. **Browser gate**
   - Open the file in a real Chromium session.
   - Capture full-page desktop and mobile screenshots.
   - Check console and page errors.
   - Assert no horizontal overflow at both viewports.
5. **Interaction gate**
   - Exercise every concept-critical control.
   - Verify slider or branch state changes.
   - Complete the quiz and verify score/feedback.
   - Verify print or download affordances where required.
6. **Visual gate**
   - Inspect screenshots for clipping, overlap, tiny text, broken tables, awkward whitespace, and mobile stacking.
   - Run the design slop audit; compositional failures must be fixed before cosmetic polish.
7. **Instructional gate**
   - Outcomes are observable and assessed.
   - Activities fit the least-experienced learner.
   - Time allocations sum exactly.
   - Failure paths, privacy, and human review are visible.

If browser installation needs a custom cache location, set a writable `PLAYWRIGHT_BROWSERS_PATH` for both installation and test execution. Treat this as an execution detail, not a reason to skip the browser gate.

## Common Pitfalls

- **Article disguised as training:** Add learner decisions, feedback, and a transfer artifact.
- **Live-looking fake output:** Put the simulation label next to the result, not only in a footer.
- **Confidence as truth:** Teach group calibration and individual uncertainty.
- **Vendor benchmark laundering:** Attribute the evaluation owner and disclose whether it was independently verified.
- **Feature overload:** Keep only concepts needed for the target behavior.
- **Desktop-only verification:** Mobile overflow and touch size failures are common even when desktop looks clean.
- **Static screenshot-only review:** Exercise JavaScript interactions and inspect console errors.
- **Unverified delivery claim:** Confirm the artifact file, browser checks, and delivery result before reporting completion.

## Deliverable Report

Report briefly:

- Artifact path or delivery destination.
- Audience, duration, and primary learner action.
- Included practice and facilitator components.
- Source scope and check date.
- Actual verification results and any remaining limitation.

## References

- `references/jev-rlcd-general-audience.md` — researched Jev/RLCD teaching notes, caveats, and a validated 30-minute structure from the 2026-09-21 artifact.
