---
name: presentation-visual-design
description: Use when designing or upgrading presentation visuals.
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [presentation, powerpoint, pptx, visual-design, slides, svg]
    related_skills: [powerpoint, popular-web-designs, brand-identity-development]
---

# Presentation Visual Design

Design presentation decks as visual narratives, not documents placed on slides. Use this skill alongside the technical `powerpoint` skill: this skill governs art direction, slide archetypes, information hierarchy, and visual QA; `powerpoint` governs package creation and editing.

## When to Use

Use when asked to:

- create or redesign a PowerPoint, keynote-style deck, workshop deck, or training material;
- improve a deck criticized as plain, repetitive, generic, document-like, or visually weak;
- turn dense notes into a persuasive or teachable visual sequence;
- create a presentation-ready deck while preserving selected editability;
- compare visual directions before committing to a full deck.

## Core Principle

A clean grid is not enough. Repeated rounded cards, uniform shadows, and large unused whitespace can look orderly while still failing as presentation design. Each slide should have a clear focal point, one dominant message, and a visual structure that explains the relationship among ideas.

## Procedure

### 1. Diagnose before redesigning

Inspect representative slides or renders and evaluate:

- **information hierarchy:** what is seen first, second, and third;
- **space utilization:** whether whitespace creates focus or merely emptiness;
- **visual relationship:** sequence, contrast, causality, comparison, hierarchy, or decision;
- **typography:** title/body scale, line length, weight, and density;
- **shape language:** whether cards, radius, borders, and shadows are intentional or generic;
- **narrative rhythm:** whether section transitions and scene changes are visible;
- **teaching behavior:** whether the audience knows what to notice or do;
- **brand fit:** whether the visual posture matches the audience and subject.

Do not respond to “make it more designed” by adding more decoration to the same layout.

### 2. Offer three meaningfully different directions

Show a comparison board using the same content in three visual systems. Vary structure and posture, not only color.

Default directions:

1. **Enterprise/industrial editorial:** strict grid, flat surfaces, engineered diagrams, restrained blue accent.
2. **Cinematic minimal:** large type and numbers, dark/light scene rhythm, one visual event per slide.
3. **Participatory workshop:** canvases, sticky-note groupings, warm accent surfaces, visible activity cues.

Recommend one direction and explain the tradeoff. For executive AI/AX workshops, prefer enterprise/industrial editorial as the base, cinematic treatment for openings/transitions, and participatory treatment only for exercises.

### 3. Establish a deck-level design system

Define before building:

- 16:9 canvas and safe margins;
- 8-point spacing grid;
- display, title, body, caption, and data typography;
- one primary accent plus semantic warning/success colors;
- light and dark scene backgrounds;
- line, corner, shadow, and icon rules;
- chart and diagram style;
- footer, section label, slide number, source, and activity treatment.

Use installed fonts that contain all required glyphs. Verify the actual font file, not only the declared family name.

### 4. Build a slide-archetype map

Avoid using one card template for every slide. Map content to its semantic visual form:

- promise/hero → large statement or image-led scene;
- agenda/journey → path or staged process;
- definition → before/after or contrast;
- roles → split comparison;
- criteria → scorecard, radar, or ranked ladder;
- case → input → AI role → human review → output pipeline;
- safety → gate, stop sign, or traffic-light model;
- measurement → baseline chart and experimental sequence;
- action plan → timeline;
- decision → branching tree;
- activity → worksheet/canvas with a visible instruction;
- evidence → chart with source and interpretation caveat.

A deck should normally contain several archetypes and deliberate section transitions.

### 5. Reduce and stage content

- Keep one dominant message per slide.
- Convert lists into relationships where the content implies sequence, comparison, hierarchy, or decision.
- Put detail in speaker notes or a handout rather than shrinking text.
- Use progressive disclosure across slides rather than one dense dashboard.
- Make the audience action explicit but visually subordinate to the learning point.

### 6. Choose the production model explicitly

Offer three production modes:

- **Fully editable:** all text and graphics as native PowerPoint shapes; best for frequent editing, lower visual fidelity.
- **Visual-first:** full-slide rendered artwork; highest fidelity, low editability.
- **Hybrid:** titles, body text, numbers, and activity instructions remain editable; complex diagrams, icon systems, and decorative backgrounds are embedded vector graphics. This is the default recommendation for professional training decks.

For a tested hybrid SVG workflow, see `references/hybrid-pptx-svg-workflow.md`.

### 7. Use visual assets with meaning

Icons, photos, charts, and diagrams must explain the message, not fill space.

- Prefer vector diagrams for processes and controls.
- Use photographs only when they establish industry context or emotion.
- Use abstract visuals for section transitions, not factual evidence.
- Never present decorative example data as measured business results.
- Use no more than one strong visual event per slide.

### 8. Verify in two layers

**Structural verification**

- PPTX opens as a valid package;
- slide count, notes count, and timing match;
- fonts, editable text, media, sources, and required phrases are present;
- all XML and relationships parse;
- SVG assets include compatibility fallbacks when the generator supports them.

**Visual verification**

- render every slide through PowerPoint, LibreOffice, or another real presentation renderer;
- inspect thumbnails for rhythm and repeated layouts;
- inspect full-size slides for clipping, line breaks, contrast, alignment, and non-Latin glyphs;
- correct every issue and re-render.

If no real renderer is available, label the result “structurally verified, visual rendering pending.” A layout-box check is not a visual verification.

## User Preference for bitlabs Decks

For bitlabs training decks, do not default to a sequence of rounded cards on white backgrounds. Favor:

- stronger slide-to-slide visual narrative;
- multiple semantic layouts;
- diagrams, charts, timelines, and industry-relevant imagery;
- clear dark/light section rhythm;
- presentation-scale typography and focal points;
- restrained enterprise styling rather than generic web-dashboard styling.

## Common Pitfalls

- **Cards as a universal answer:** four text boxes do not explain a sequence or causal relationship.
- **Empty rather than intentional whitespace:** space must create focus around a dominant object.
- **UI chrome in a presentation:** labels, pills, shadows, and footers can overwhelm the teaching message.
- **Decorative icons:** repeating icons without semantic value adds noise.
- **Every slide looks the same:** consistency is not sameness; vary archetype while preserving tokens.
- **Overusing rounded corners and shadows:** use flat layers, lines, scale, and contrast first.
- **Tiny activity boxes:** participant instructions should be clear but integrated with the content flow.
- **Claiming visual QA from XML checks:** structural inspection cannot prove appearance.
- **Rebuilding the whole deck before direction approval:** create representative title, concept, case, data, and activity samples first.

## Deliverable Checklist

- [ ] Three visual directions were compared when no design direction existed.
- [ ] One direction was recommended and approved.
- [ ] Design tokens and slide archetypes were defined before production.
- [ ] One idea dominates each slide.
- [ ] Lists were converted into meaningful visual relationships.
- [ ] Section transitions create narrative rhythm.
- [ ] Complex visuals and editable content use the chosen production model.
- [ ] Speaker notes carry detail that does not belong on-screen.
- [ ] Structural checks passed.
- [ ] Every slide was rendered and visually inspected, or the limitation was stated precisely.
