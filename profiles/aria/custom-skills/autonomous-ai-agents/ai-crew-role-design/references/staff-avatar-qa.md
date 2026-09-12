# Staff avatar preparation and QA

## Why this matters
An employee badge and a messaging avatar have different reading conditions. The bitlabs review exposed three requirements: square exports, visible name labels, and distinct full-background colors so workers can be recognized in small Slack messages. Do not wait for successive user corrections to test these conditions.

## Workflow
1. Recover approved original portraits rather than generating replacement characters or stretching a tall badge. Inspect the actual pixels and dimensions before deciding crop coordinates.
2. Confirm the platform's current upload constraint. The observed Slack requirement was square images between 512 and 2000 pixels per side; 1024×1024 PNG was the chosen export.
3. Crop face and upper body without cutting hair or important facial features. Use consistent apparent head size across the set.
4. Apply a different dominant background per worker. Approved bitlabs mapping in this review: ARIA teal, MIRA purple, LEO orange, EDEN blue. A future worker needs its own distinguishable treatment rather than silently reusing a teammate's color.
5. Preserve name labels when requested. Use a high-contrast, generously sized bottom band, but keep the portrait recognizable if the name becomes unreadable at small sizes. Do not cover the face.
6. Save derivatives under new filenames; preserve source portraits. Write a manifest with worker name, color, source/output path, dimensions and format. Programmatically verify the expected count and decode each output PNG.
7. Inspect the full-size set and a contact sheet rendered at representative 32, 48 and 64 pixel sizes. Check head clipping, readable silhouettes, background distinction, label contrast and circular-mask cropping. A 256px preview alone does not establish small-message legibility.
8. Deliver files separately from app configuration. Image creation is not proof that Slack uploaded or refreshed the icons.

## Background replacement cautions
For genuinely light, plain backgrounds, edge-connected flood fill can isolate the background without recoloring disconnected white clothing. Grow the mask only through eligible near-neutral light pixels from the image edges, then feather minimally before compositing the color. This is a heuristic, not a general portrait segmentation method: pale hair, skin, white clothing connected to the edge, shadows and compression artifacts can confuse it. Inspect every output for halos and lost detail; use an appropriate segmentation/editor workflow when the heuristic fails. Never claim flawless cutouts merely because the image script completed.

## Acceptance checklist
- Correct number of individually named PNGs, square and within platform limits.
- Approved identities preserved; no unrequested replacement characters.
- Distinct backgrounds, consistent composition and requested names.
- Full-resolution and small-size visual review completed or limitations disclosed.
- Original assets retained and output manifest saved.
