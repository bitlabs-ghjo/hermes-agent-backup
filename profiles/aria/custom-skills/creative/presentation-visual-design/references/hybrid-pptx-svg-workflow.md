# Hybrid PPTX + SVG Workflow

Use this when a deck needs presentation-grade visuals while keeping titles, body copy, numbers, and participant instructions editable.

## Architecture

- **Editable PowerPoint layer:** titles, subtitles, labels, numbers, sources, activity instructions, and speaker notes.
- **Vector visual layer:** charts, process lines, icons, abstract backgrounds, and complex diagrams as SVG.
- **Compatibility layer:** PNG fallback paired with each SVG when the generation engine supports it.

## Recommended Engine

PptxGenJS can embed an SVG data URI and writes both an SVG image and a PNG fallback into the PPTX package. This is useful when `python-pptx` cannot ingest SVG directly.

```js
const pptxgen = require('pptxgenjs');
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450">
  <rect width="800" height="450" fill="#102A43"/>
  <circle cx="400" cy="225" r="120" fill="#0F62FE"/>
</svg>`;
const data = 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64');

const slide = pptx.addSlide();
slide.addImage({ data, x: 6, y: 1, w: 6, h: 3.4 });
slide.addText('Editable headline', {
  x: 0.8, y: 0.8, w: 5, h: 0.7,
  fontFace: 'Noto Sans KR', fontSize: 30, bold: true
});
slide.addNotes('[진행 시간] 3분\n[강사 멘트] ...');

pptx.writeFile({ fileName: 'deck.pptx' });
```

## SVG Design Rules

- Keep text outside SVG unless it is permanently decorative; editable labels belong in PowerPoint text boxes.
- Use a stable `viewBox` and explicit aspect ratio.
- Prefer flat fills and paths over filters, masks, embedded fonts, or browser-specific CSS.
- Use stroke widths that remain visible after downscaling.
- Keep SVG colors tied to the deck token system.
- Avoid fake charts that could be mistaken for measured evidence.

## Compatibility Check

Inspect the PPTX package as a ZIP and confirm:

- all slide XML and relationship XML files parse;
- expected slide and notes counts are present;
- `[Content_Types].xml` includes `image/svg+xml` and `image/png`;
- SVG and PNG fallback counts match for generated vector assets;
- editable text appears as `<a:t>` runs in slide XML;
- core slide timings sum to the requested duration.

Do not rely solely on readers built on Pillow or `python-pptx`: they may fail while inspecting valid SVG media because Pillow does not decode SVG. Use ZIP/XML inspection for structural validation and a real presentation renderer for visual validation.

## Visual QA Loop

1. Render all slides through PowerPoint, LibreOffice, or an equivalent real renderer.
2. Build a contact sheet and inspect narrative rhythm, repeated archetypes, and inconsistent density.
3. Inspect each full-size slide for clipping, fallback fonts, broken SVG, and weak contrast.
4. Fix and render again.
5. If the renderer is unavailable, deliver only as “structurally verified, visual rendering pending.”

## Design-Direction Gate

Before building a long deck, create representative samples for:

- title/hero;
- concept/definition;
- process;
- industry case;
- data/measurement;
- participant activity.

Compare at least three directions when the visual posture is unknown. Obtain direction approval before full production to avoid polishing the wrong system.
