# Design-system handoff review

Use for an existing ZIP or folder containing a brand guide, logo variants, tokens, templates, and QA evidence. Review the actual supplied version; local author paths in the handoff may point to a different version.

## Package and evidence checks

1. Inventory the archive before extracting. Reject path traversal and extract into the reviewer's workspace, preserving the author's original package.
2. Check archive integrity. If a manifest exists, independently compare recorded file sizes and hashes. This proves consistency with that manifest, not authorship, safety, or design quality.
3. Parse HTML and SVG; check duplicate IDs, local resource paths, and fragment targets. Define the counting scope: HTML href/src references, CSS URLs, and required-file assertions are different populations. Different counts are not automatically defects; reconcile scopes before comparing totals.
4. Read the handoff, guide, license information, template copy, and QA report. Record author claims separately from tests actually repeated by the reviewer.
5. Inspect comparison boards, recommended marks at actual small sizes, and representative desktop/mobile applications. Crop long screenshots into readable native-scale regions; a heavily downscaled full-page image does not establish text legibility.
6. Supplied screenshots support review of those captured images, not proof that the extracted HTML currently renders identically. State whether screenshots were supplied or freshly rendered and whether dynamic tests were rerun.

## Design and governance review

- Compare alternatives by customer comprehension, small-size recognition, use across documents/products, and confusion risk—not color preference alone.
- Keep design rationale distinct from official company messaging. A metaphor such as modules may explain the symbol without explaining what the business sells.
- Separate confirmed service lines from unconfirmed customer segments and proposed positioning. Use established context with provenance; do not treat conversation memory as an official company record.
- Inspect approval labels embedded in examples. Sales/content review is not authority over commercial commitments or external distribution.
- Distinguish a company logo/avatar from individual staff app icons. Do not silently replace approved character identities.
- Check footers, contact conventions, real links, and document hierarchy. Repeated editing warnings can overwhelm content; separate editorial instructions while preserving pre-approval restrictions.
- Request a realistic example using an approved topic, with clear placeholders for unapproved commercial facts. Validate text density, a meaningful diagram or screen example, and the next action before expanding the component library.

## Release gates

Keep internal direction selection, external publication, trademark clearance, physical production, and product deployment as separate decisions. Name-search results are leads, not legal findings; label search-only evidence explicitly. Schedule print/CMYK checks before actual print production, rather than treating them as a prerequisite for every internal HTML revision.

## Feedback structure

1. Conditional verdict and recommended direction.
2. Strengths to preserve.
3. Priority corrections with problem, impact, and requested change.
4. Representative next-version deliverables and acceptance criteria.
5. Evidence actually checked, author-reported results, and untested areas.
6. Decisions and delivery approval still required.

For approved delivery, preserve the exact approved audience, body, and attachment scope. Distinguish transport success, target-message readback, recipient acknowledgment, and work acceptance. Never interpret posting to a channel as proof that another agent has been activated or started the revision.
