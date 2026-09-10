---
name: professional-presentation-design
description: Use when designing or reviewing professional slide decks.
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [presentation, powerpoint, deck, keynote, workshop, visual-design]
    related_skills: [powerpoint, claude-design, popular-web-designs]
---

# Professional Presentation Design

Design and review presentation decks that must look credible in an executive meeting, conference room, classroom, or client workshop. This skill governs composition, type, imagery, narrative rhythm, prototyping, and visual verification. Pair it with `powerpoint` for PPTX mechanics and `claude-design` for HTML prototypes.

## When to Use

Use this skill when the user asks for:

- a professional PPTX, keynote-style deck, conference presentation, consulting deck, or executive workshop;
- a redesign after feedback that slides look generic, amateur, too small, too empty, or insufficiently visual;
- a visual audit of screenshots or exported slides;
- a deck that must remain readable from the back of a room;
- a hybrid deck with editable text and SVG, charts, photography, or other complex visual assets.

Do not use it for a text-only outline, speaker notes without slides, or a simple document export where presentation quality is irrelevant.

## Core Principle

A presentation is a **Decide/Learn surface**, not a document or web dashboard. One idea must land per slide. Empty space is useful only when it creates focus; cards, icons, panels, and large shapes must explain relationships rather than merely occupy space.

Color polish cannot rescue the wrong composition. Storyboard and approve representative compositions before building the full deck.

## Required Inputs

Confirm or infer only low-risk defaults:

- audience, room size, screen/projector, and viewing distance;
- duration, speaking style, and whether slides support lecture, discussion, or hands-on work;
- brand assets, approved fonts, color restrictions, and image rights;
- output format and editability requirement;
- desired slide count and whether appendices are allowed;
- source materials, citations, and confidential-data constraints.

If brand direction or the tradeoff between editability and visual fidelity materially affects the result, ask one focused question and recommend an option.

### New reusable formats: agree on process before production

When the user is creating a reusable proposal, training, consulting, or sales-deck format for the first time, establish and discuss a phase-gated workflow before making the full deck. Confirm the representative offer, buyer, end audience, delivery context, price treatment, and output formats; then approve the content architecture before visual work.

Do **not** design an empty generic template first. Build and validate one real representative proposal, prototype 3–5 pages, complete that proposal only after direction approval, and then extract fixed, variable, optional, appendix, and companion-document components into the reusable template. Treat approval of each gate as limited to that gate, not as blanket approval of later content or visuals.

For the detailed gates, emailed-PDF considerations, short training-proposal pattern, and browser-verified HTML prototype workflow, read `references/reusable-proposal-deck-workflow.md`.

## Procedure

### 1. Audit before redesigning

Review supplied screenshots or rendered slides at their actual 16:9 size. Diagnose separately:

- composition and slide purpose;
- hierarchy and reading order;
- room-distance legibility;
- image relevance and quality;
- diagram semantics;
- repetition across the deck;
- contrast, alignment, clipping, and font substitution.

Run a short anti-slop audit. Flag repeated card grids, accent rails, decorative icons, oversized rounded rectangles, meaningless diagrams, generic tech gradients, and a fixed footer/callout system that appears on every slide.

Do not treat a user complaint about professionalism as a request for more decoration. It usually requires re-storyboarding, larger type, less copy, better imagery, and fewer repeated components.

### 2. Commit to an art direction

Write one sentence naming the posture before choosing tokens, for example:

> Industrial editorial: evidence-led, human-centered, restrained navy and cobalt, with documentary imagery and sharp information graphics.

Use no more than one primary accent and one warm support accent unless the brand requires more. Prefer hierarchy through scale, alignment, and surface contrast over shadows and rounded cards.

### 3. Build the storyboard before the deck

Assign every slide exactly one job:

1. Photo hero
2. Assertion
3. Before → after
4. Process
5. Evidence or chart
6. Case story
7. Decision gate
8. Workshop canvas
9. Safety warning
10. Roadmap or commitment

Do not apply one template to all slides. Use section rhythm: immersive opener, explanatory middle, active exercise, decision close.

For a 120-minute workshop with substantial participant work, default to roughly 22–26 core slides and move supporting detail to an appendix. More slides are acceptable only when rehearsal proves the pacing and type remains large.

### 4. Set a room-readable type system

For a 1920×1080 Korean-language deck, use these defaults unless the room is unusually small:

- cover title: 68–82 pt;
- major assertion: 56–64 pt;
- normal slide title: 44–52 pt;
- subtitle: 26–30 pt;
- body and diagram labels: minimum 26 pt, usually 28–32 pt;
- table text: minimum 24 pt; simplify the table instead of shrinking below this;
- citations, legal text, and page numbers: 15–17 pt only when they are not meant to be read during delivery.

Keep a line to roughly 24–32 Korean characters and a slide to one claim plus at most three supporting points. If text does not fit, split or cut it; do not use automatic shrink-to-fit as the default.

### 5. Use imagery as evidence and context

Use real supplied imagery first. When generation or stock imagery is appropriate, select documentary/editorial scenes that establish audience context: people reviewing work, operating a process, checking evidence, or making a decision.

For visual decks, let one relevant image occupy roughly 35–60% of the slide. Use imagery on enough slides to establish a narrative rhythm, commonly 6–10 images in a 22–26-slide deck, but never impose a quota when the content is better served by diagrams or data.

Avoid robots, glowing AI brains, holograms, neon cyberpunk, meaningless abstract waves, fake dashboards, generic SaaS icons, and decorative SVG scenes. Never place generated readable business data, logos, or personal information inside imagery.

### 6. Make diagrams carry meaning

A process diagram must show sequence, ownership, inputs, outputs, or decisions. A comparison must use aligned structures and a clear transformation axis. A chart must answer a question and state the takeaway.

Do not put a small diagram inside a large white rounded rectangle. Do not place white labels over a white panel. Do not add an icon unless it improves scanning or establishes context.

For activity slides, integrate the instruction into the main composition as the next action. Avoid repeating a separate `ACTIVITY` card or bottom message banner on every slide.

### 7. Prototype before full production

Before rebuilding a significant deck, create and render 3–5 representative slides:

- one hero or section transition;
- one process or roadmap;
- one comparison;
- one data/evidence slide;
- one image-led case or activity slide.

Show the rendered PNGs at 1920×1080. Confirm art direction, type scale, image posture, and density before applying the system to every slide. A structurally valid PPTX is not proof of visual quality.

### 8. Choose the production model deliberately

- **Native/editable:** all text, charts, and shapes editable; best for frequent client edits, but requires careful master layouts and more visual QA.
- **Hybrid:** key text and numbers editable; complex visuals embedded as SVG with PNG fallback. Best default for polished workshop decks.
- **Visual-first:** full-slide raster or vector artwork; highest fidelity but limited editability.

When using SVG, verify that the PPTX package contains the SVG and a compatible fallback when the target environment needs one. Keep the important text editable and outside decorative images.

### 9. Verify the rendered result

Verification is mandatory for professional visual claims:

1. validate the PPTX package and slide count;
2. render every slide to PNG at 1920×1080 or higher;
3. inspect representative slides individually for glyphs, clipping, contrast, and image quality;
4. inspect a contact sheet for pacing, repetition, and visual rhythm;
5. verify core timing and speaker notes separately;
6. open in the target PowerPoint environment when possible to catch font and SVG differences.

If rendering is unavailable, do not call the deck visually final. Deliver a prototype or structurally verified draft and state the limitation precisely.

## User Preference for bitlabs Decks

For decks prepared for 조대표님:

- prefer professional consulting/conference composition over document-style or card-grid layouts;
- use large Korean text readable from the back of a room;
- use photography, meaningful diagrams, and evidence graphics where they clarify the story;
- avoid tiny body copy, repeated cards, fixed bottom callouts, meaningless large shapes, and generic AI imagery;
- prototype representative slides and obtain visual direction approval before rebuilding the full deck.

## Pitfalls

- **Title-only hierarchy:** the title is large but all meaningful information is too small to read in a room.
- **Document on a slide:** paragraphs and tables are copied from a report instead of edited for speech.
- **UI masquerading as presentation:** panels, pills, cards, and status bars repeat without narrative purpose.
- **Decorative SVG:** a vector occupies space but explains no relationship.
- **Whitespace without focus:** the slide feels empty because scale and composition are weak.
- **Footer tyranny:** repeated activity and takeaway boxes make every slide look identical.
- **Image starvation:** an audience-specific deck contains no people, places, or work context.
- **Unrendered confidence:** XML, slide count, and bounding-box checks are reported as design verification.
- **Full-deck-first:** dozens of slides are built before the art direction is approved.

## Deliverables

A professional deck engagement should produce:

1. art-direction sentence and design tokens;
2. storyboard with slide jobs;
3. 3–5 rendered representative slides;
4. full PPTX after direction approval;
5. rendered contact sheet and selected full-size previews;
6. verification report with visual and structural checks separated.

For a detailed review rubric and common redesign patterns, read `references/executive-workshop-deck-rubric.md`.

## Final Check

- [ ] Each slide has one job and one dominant reading path.
- [ ] Korean body text intended for delivery is at least 26 pt.
- [ ] Images are relevant, high-resolution, and licensed or generated appropriately.
- [ ] Diagrams express real sequence, ownership, comparison, or decision.
- [ ] Repeated cards and bottom callouts have been removed unless functionally justified.
- [ ] Core slide count matches the workshop pacing.
- [ ] Representative slides were approved before full production.
- [ ] Every slide was rendered and the contact sheet was inspected.
- [ ] Visual verification claims match what was actually tested.
