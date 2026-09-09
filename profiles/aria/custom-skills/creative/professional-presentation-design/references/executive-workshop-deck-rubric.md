# Executive Workshop Deck Review Rubric

Use this reference when a deck is intended for executives, a conference room, or a facilitated workshop. It supplements the general procedure in `SKILL.md`.

## Scoring

Score each dimension from 0 to 3.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Message | No clear point | Topic only | Claim is visible | One memorable, decision-relevant claim |
| Room legibility | Key text under 20 pt | Much body under 24 pt | Most delivery text 24–26 pt | Korean delivery text 28–32 pt with clear hierarchy |
| Composition | Document dump | Repeated cards/panels | Purposeful layout with minor repetition | Layout expresses the slide’s specific job |
| Imagery | None or cliché | Decorative | Relevant but secondary | Image provides context, evidence, or emotional anchor |
| Diagram semantics | Decorative shapes | Sequence unclear | Relationship mostly clear | Inputs, sequence, ownership, output, or decision explicit |
| Evidence | Unsupported or cluttered | Data without takeaway | Data and source present | Visual evidence directly supports the claim |
| Workshop action | No participant action | Generic activity footer | Action is clear | Action is integrated into the main visual and produces an artifact |
| Deck rhythm | Every slide similar | Limited variation | Clear section changes | Intentional rhythm across hero, explanation, practice, and decision |
| Safety and accuracy | Risk hidden | Fine-print caveat | Visible safeguards | Safeguard is part of workflow and decision design |
| Verification | Not rendered | Structure only | Representative renders inspected | Every slide and contact sheet inspected in target environment |

A client-ready deck should score at least 24/30 with no zero in message, legibility, composition, or verification.

## Back-of-Room Test

At a 1920×1080 render:

1. Downscale to 960×540.
2. The title and all information the audience must act on should remain readable without zooming.
3. If secondary explanation disappears, either enlarge it, remove it, or move it to speaker notes.
4. Do not count the presenter’s ability to read from a laptop as audience legibility.

## Contact-Sheet Test

Render all slides and inspect a contact sheet at 5–6 thumbnails per row.

Flag:

- three or more consecutive slides with the same composition;
- repeated footer banners or `ACTIVITY` cards;
- long runs with no human, place, process, evidence, or participant action;
- dark slides used randomly rather than as section punctuation;
- inconsistent title positions or margins;
- image crops that cut faces, hands, machinery, or the object of attention;
- dense appendix material left in the live sequence.

## Worked Redesign Patterns

### Roadmap

**Weak:** a thin line and small labels placed inside a large white rounded panel.

**Strong:** use the full content width for 3–5 stages. Give each stage a 28–32 pt title and a 22–26 pt output. Show the final artifact at the end of the flow. Integrate the participant prompt below the relevant stage instead of adding a detached activity box.

### Before → After

**Weak:** two generic cards with small bullet lists and no transformation axis.

**Strong:** align the same three dimensions on both sides. Use a visible transition arrow or bridge. Keep each phrase under one line. End with a 28–32 pt assertion, not a separate callout component.

### Evidence or KPI

**Weak:** five equal cards containing metric names.

**Strong:** display the decision rule first, then one chart or baseline-to-test graphic. Use large numerals only when they carry real meaning. State the comparison conditions and the decision the audience will make.

### Image-Led Case

**Weak:** decorative icon plus four text boxes.

**Strong:** devote 35–55% of the slide to a credible work-context image. Use the remaining space for input → AI task → human review → output. Add one high-contrast safety rule and one integrated participant action.

### Safety Gate

**Weak:** multiple pastel cards with warning icons.

**Strong:** use a decisive three-question gate or red/yellow/green decision structure. Make the consequence explicit: proceed, narrow/de-identify, or stop.

## Korean Type Guidance

- Avoid relying on automatic `fit: shrink` for primary content.
- Test actual Korean glyph width; Korean lines wrap earlier than equivalent English text.
- Use one Korean family with regular and bold or semibold weights.
- Do not use thin font weights on projectors.
- Prefer 28–32 pt body text for mixed-age executive audiences.
- When a sentence cannot fit at 28 pt, edit the sentence before editing the font size.

## Image Guidance

Use supplied or commissioned imagery first. Generated imagery is acceptable when it is clearly illustrative, contains no real personal information, and avoids fabricated readable data.

Reject:

- robots shaking hands;
- glowing brains, circuitry faces, holograms, and neon control rooms;
- laptops with fake dashboards as the only subject;
- generic smiling office teams with no task context;
- abstract vector art used only to fill whitespace.

Prefer:

- hands reviewing a checklist or source document;
- a manager and operator discussing a real process;
- a small-business owner handling a repeated operational task;
- a before/after view of a workflow artifact;
- objects whose relationship to the slide’s claim is immediately clear.

## Verification Report Template

```text
Structural
- slides / core / appendix:
- timing total:
- notes present:
- package health:

Visual
- renderer and resolution:
- full-slide inspection count:
- contact-sheet inspection:
- font substitution or glyph issues:
- clipping/overlap fixes:
- image crop and contrast fixes:

Status
- prototype / structurally verified draft / visually verified final
- limitations:
```
