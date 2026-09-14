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

## Manager-assisted generation and specialist return

A working recovery pattern is to separate source generation from specialist composition:

1. Check the manager's live tool inventory when the specialist reports a capability blocker. A profile-local blocker does not establish a system-wide limitation. Use only an already authorized alternative; do not bypass denied approval or transport confidential material to a new provider without permission.
2. For a new fictional teammate, pass an approved existing portrait or a team contact sheet as an actual reference-image input. Explicitly request one portrait, matching rendering style, a distinct silhouette and background, safe hair margins, and no copied grid, captions or extra people. Existing teammates retain their original identities.
3. Open the returned image and inspect it. Decode actual pixel dimensions instead of trusting the requested-size label: a successful generator can return dimensions different from its request metadata. Normalize the export with aspect-preserving resampling.
4. Give the real specialist an absolute source path, generation provenance, the manager's visual findings, and correction criteria in a file-backed revision packet. The specialist completes composition and packaging; the manager then reopens and checks the results. Attribute each operation to whoever actually performed it.
5. When producing both name-band and plain avatars, enumerate every person × variant, decode each PNG, verify dimensions, and test archive integrity. A contact sheet alone does not prove individual exports exist.

## Segmentation fallback and release gate

- Graphic-rich light backgrounds are poor candidates for simple neutral-color flood fill. Watch for white hair halos, fragmented diagrams, and color intrusion into pens, clothing, or magnifying glasses. Restoring original pixels can remove destructive masking, but does not satisfy a full-background recoloring requirement.
- An original image panel plus colored frame is a reversible alternative, not an equivalent substitute for a dominant colored background. Circular masks further reduce frame visibility. Keep this as a candidate requiring a decision if it departs from the approved brief.
- Judge identity at 32/48/64px by face, hair silhouette and color together. Do not promise reliable 32px name reading. Offer a plain derivative without silently dropping a requested named version.
- Reconcile review labels in the HTML, preview captions, manifest and ZIP before reporting. Distinguish technical checks passed, design reviewed with exceptions, executive approval pending, and Slack not applied. Regenerate the archive after any included file changes and rerun integrity checks.
- A set with a material unmet design criterion remains a candidate even when every PNG decodes. Report the exception and the decision required; do not close the underlying approval-dependent work as fully accepted.

## Acceptance checklist
- Correct number of individually named PNGs, square and within platform limits.
- Approved identities preserved; no unrequested replacement characters.
- Distinct backgrounds, consistent composition and requested names.
- Full-resolution and small-size visual review completed or limitations disclosed.
- Original assets retained and output manifest saved.
