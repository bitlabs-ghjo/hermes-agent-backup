# Reusable Proposal-Deck Workflow

Use this workflow when the user wants a reusable sales, training, consulting, or program proposal format rather than a one-off presentation.

## Principle

Do not design an empty generic template first. Build one representative proposal with real content, validate that it persuades and reads correctly, then extract the reusable system. Otherwise the result tends to become a decorative form that users fill with weak, document-like copy.

## Phase Gates

### Gate 1 — Engagement brief

Confirm:

- offer or representative product;
- buyer organization and decision-maker;
- end audience or learner;
- reading context: emailed PDF, live presentation, or both;
- whether price is included, optional, or supplied separately;
- required editability and final formats.

Do not begin visual production before these materially consequential choices are settled.

### Gate 2 — Content architecture

Draft a short content brief containing:

- one-sentence promise;
- buyer questions the proposal must answer;
- observable outcomes and tangible deliverables;
- evidence and trust claims, separated into verified, proposed, and missing;
- page-by-page story with one job per page;
- customer-specific variables and operational prerequisites;
- risks, exclusions, and prohibited claims.

For an emailed proposal, ensure a reviewer can answer fit, result, delivery burden, safety, trust, and next step in roughly 2–3 minutes. Add an early “at a glance” page when useful. The PDF must make sense without a presenter.

### Gate 3 — Representative visual prototype

Create only 3–5 representative pages, normally:

- cover;
- need/problem or buyer context;
- outcome or before/after;
- program/process/curriculum;
- operations, evidence, price, or CTA page depending on the proposal.

Compare meaningfully different visual directions if no direction exists. Render to images and obtain approval for posture, density, and editability before full production.

### Gate 4 — Complete the representative proposal

Build the full real proposal, not the empty template. Verify:

- the promised outcome matches the offer;
- the buyer can understand it without narration;
- price treatment matches the agreed commercial process;
- unverified testimonials, logos, statistics, and performance claims are absent;
- contact and CTA are accurate;
- PowerPoint structure and rendered output both pass QA.

### Gate 5 — Extract the reusable template

Classify every page or field as:

- fixed brand/company content;
- required offer-specific content;
- customer-specific variable;
- optional page;
- appendix;
- external companion document such as quotation or terms.

Deliver both a filled example and a clean template. Add page-level authoring guidance and a pre-send checklist so reuse does not depend on remembering the original project.

## Example: Short Training Proposal

A concise emailed training proposal often works as:

1. cover;
2. course at a glance;
3. institutional need and audience fit;
4. observable outcomes and participant artifacts;
5. timed curriculum;
6. representative exercise;
7. safety and quality controls;
8. delivery requirements and fallback plan;
9. evaluation and result reporting;
10. verified instructor/company evidence;
11. low-friction consultation CTA.

This is a pattern, not a mandatory slide count. Merge or split pages according to complexity while keeping one job per page.

## Review Perspectives

For consequential proposals, reconcile at least three lenses before design:

- buyer/market: selection criteria, operational burden, evidence;
- conversion/revenue: scanning order, customization, CTA, sales pressure;
- delivery/domain: feasibility, outcomes, safety, contingencies.

Record the final decision when reviewers disagree. Do not paste parallel opinions into the deliverable.

## HTML Prototype Production and QA

When HTML is the approval surface before PPTX production:

1. Use a fixed 1920×1080 slide canvas that scales to the viewport.
2. Include keyboard navigation, visible page count, stable slide IDs/titles, and print rules.
3. Keep the prototype to the approved representative pages; do not quietly expand into the full deck.
4. During iteration, prefer linked local images and fonts so targeted patches stay small and reviewable. Inline them as data URIs only for the final portable single-file handoff.
5. Run a static check for page count, missing asset placeholders, navigation hooks, and embedded/linked asset integrity.
6. Render every page through a real browser at 1920×1080 and collect console/page errors.
7. Inspect each render individually, then inspect a contact sheet for rhythm and repeated composition.
8. Re-render after every visual fix. A successful HTML parse is not visual verification.

Korean narrow-column QA needs an explicit pass. Side rails and proportional timelines can wrap short labels one syllable per line even when no element technically overflows. Check the actual raster output for awkward breaks in compact labels, time ranges, and body copy; fix with wider columns, `word-break: keep-all`, deliberate `<br>` placement, smaller local type, or reduced padding rather than global shrink-to-fit.

Before sign-off, report separately:

- structural status: page count, IDs/titles, navigation, asset completeness;
- browser status: console/page errors and actual font family;
- visual status: clipping, Korean line breaks, contrast, image integrity, and contact-sheet rhythm.

## Pitfalls

- Embedding large fonts and images before design stabilizes, causing oversized files and unmanageable diffs.
- Empty-template-first production.
- Treating process approval as approval of all later content and visuals.
- Building the full deck before representative pages are approved.
- Copying a prior deck whose audience and outcome differ.
- Designing an emailed PDF as if a presenter will explain missing context.
- Mixing quotation data into the proposal when the commercial process calls for a separate document.
- Calling every field customizable without defining what remains pedagogically or commercially fixed.
