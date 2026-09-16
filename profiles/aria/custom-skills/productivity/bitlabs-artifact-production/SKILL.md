---
name: bitlabs-artifact-production
description: Use when creating bitlabs deliverables. Default to HTML.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [bitlabs, artifacts, html, documents, delivery]
    related_skills: [claude-design, grounded-citations]
---

# bitlabs Artifact Production

Create polished, verifiable deliverables for bitlabs without wasting time on an unrequested format. This skill governs reports, lecture materials, proposals, briefs, guides, and comparable artifacts; domain-specific skills still govern the content.

## When to Use

Use this skill whenever bitlabs asks to create, package, revise, verify, or deliver a report, lecture handout, proposal, brief, guide, presentation master, or similar file. Load it alongside the relevant content/design skill. Skip it only when the request is conversational and no artifact will be created.

## Format Contract

- Produce a complete **HTML file by default**.
- Create PDF, PPTX, DOCX, HWP, XLSX, or other formats only when the user explicitly requests that format.
- Do not interpret phrases such as “파일로 정리” or “자료로 만들어” as permission to choose an Office format.
- When the user names a format, preserve it exactly. If native production is unavailable, explain the limitation and propose the closest compatible alternative before substituting.
- Markdown is an internal drafting and source-management format, not the default user deliverable.
- App icons and avatars are image deliverables, not documents: when requested, produce upload-ready PNGs rather than an HTML substitute. Reuse approved character art, crop without distortion, remove badge text, and verify dimensions plus facial framing. See `references/app-icon-derivatives.md` for the workflow.

## Procedure

1. **Classify the artifact.** Identify audience, purpose, reading context, and whether the primary surface is Learn, Decide, Compare, Operate, Monitor, Configure, Explore, or Inspect.
2. **Load the domain skill.** Examples: workshop design for courses, grounded citations for researched claims, or presentation design for decks.
3. **Apply Impeccable for design.** Load `impeccable` for bitlabs design production and review. For UI/UX, websites and HTML, follow its applicable playbooks, using critique, audit and polish as appropriate. Preserve approved brand colors, Pretendard, copy and accepted designs; never redesign an approved artifact without permission. For static images and business cards, use applicable hierarchy/typography/spacing principles but keep separate image and print checks. Use profile-local launcher cache (`IMPECCABLE_HOME=/opt/data/profiles/aria/cache/impeccable` for ARIA). The Hermes catalog installer may return only a stub: verify references and launcher exist before claiming full installation.
3a. **Use Taste selectively alongside Impeccable.** For marketing websites, landing pages and portfolios, load `taste-skill` (frontmatter name `design-taste-frontend`) for visual direction and layout; use Impeccable for production and review. Do not default Taste onto dashboards, complex product UI or print artifacts. Approved requirements, brand, accessibility and requested format override conflicting style defaults. Never force React/Next.js, dual themes or motion onto standalone HTML. Keep the installed upstream snapshot; updates require review, not automatic replacement. Check dependency necessity and pin versions before installation.
3b. **Gather the source material.** Prefer supplied links and files first. Separate source claims, reasonable synthesis, and unresolved uncertainty.
4. **Draft the information architecture.** Put the decision, lesson, or action first. Avoid merely translating or dumping the source structure.
5. **Build one self-contained HTML master.** Use semantic HTML, embedded CSS/JS where useful, responsive behavior, print styles, and bitlabs brand conventions when applicable. When the deliverable contains local portraits, diagrams, or icons, embed them as data URIs before attaching the HTML; do not leave required relative assets behind. Follow `references/self-contained-html-media.md` for the packaging and verification pattern.
6. **Include provenance.** Put citations next to externally sourced claims and include a mechanically checked source list when research is involved.
7. **Verify before delivery.** Check file existence, HTML parseability, duplicate IDs, internal anchor targets, JavaScript syntax when present, expected section counts, and key content.
8. **Run a visual check when tooling permits.** Inspect the primary viewport and print layout. If rendering is unavailable, state that limitation rather than claiming visual verification.
9. **Prepare delivery separately.** File creation does not authorize Slack posting, email, sharing, or any external state change. Present recipient, purpose, complete message, attachment, links, and impact; execute only after the required approval.
10. **Report concisely.** State the artifact, verification performed, and delivery location or pending approval. Do not attach an unrequested derivative format.

## Artifact Handoff and Design Feedback

- When the user asks when they can see results, inspect current artifacts and handoff records before answering. Distinguish available preview, corrected/reviewed version, and full package; do not repeat an old incomplete status if newer files exist. Give only a confirmed ETA, explicitly labeling an estimate if used.
- When asked where files are or to show the whole design, provide accessible attachments or verified links in the authorized destination, not just server paths or another status report. Include short opening instructions. Respect delivery approval rules; do not claim an attachment was received based only on composing its media marker.
- For a complete design package, inspect the archive inventory and integrity, confirm expected entry pages and required local assets are included, and identify the starting HTML file. Explain whether course material is a representative excerpt or the complete requested course. A complete archive does not mean content, QA, or release approval is complete.
- When asked for a design opinion, inspect actual rendered screens before evaluating. Lead with an independent recommendation, then concrete strengths and prioritized improvements tied to visible evidence. Do not merely agree with the user's positive reaction.
- Long-page screenshots can shrink text and show fixed-position bars across content. Inspect native-size crops or live viewport/print behavior before asserting a layout defect; report unresolved capture artifacts as hypotheses. Static checks and archive integrity are not visual approval.
- Treat positive aesthetic feedback as design-direction feedback, not authorization to publish or a waiver of factual, contractual, accessibility, or final-review checks.

## HTML Quality Requirements

- Use the bitlabs visual language when no client brand overrides it: deep navy, teal, bright body surface, Pretendard-first typography, practical and trustworthy tone.
- Use a single composition appropriate to the surface instead of generic equal-weight cards.
- Keep the file usable without remote dependencies unless a dependency is necessary and stable.
- Support responsive reading and `@media print` for document-like outputs.
- Use accessible structure: language attribute, title, headings in order, sufficient contrast, keyboard-usable controls, and meaningful link text.
- Add only interactions that improve use: copy buttons, section navigation, progress, filters, or print controls as appropriate.
- Preserve identifiers and source URLs exactly.

## Research-to-Lecture Pattern

When converting a supplied article or post into teaching material:

1. Reconstruct the complete source, including article blocks or embedded content rather than only the social-post preview.
2. Identify unsupported generalizations, product-specific behavior, and internal contradictions.
3. Cross-check important claims against primary or official sources.
4. Transform the material into learning objectives, a timed agenda, concept explanations, worked examples, exercises, facilitator guidance, operational risks, and sources.
5. Label the recommended duration as an assumption when the user did not provide one.
6. Avoid reproducing the entire copyrighted source; teach the ideas in an original structure and cite the source.

## Pitfalls

- **Office-first inertia:** generating DOCX/PPTX because the request says “file.” Default to HTML.
- **Silent substitution:** delivering a compatible format when the user asked for a native format without explaining the difference.
- **Preview-only research:** summarizing an X post that links to a long-form article without retrieving the article body.
- **Source transcription disguised as instruction:** a lecture needs objectives, practice, assessment, and facilitator cues.
- **Product claims presented as universal:** distinguish author framing, official platform behavior, and general design principles.
- **Successful write treated as complete delivery:** verify the artifact, then separately gate external posting or sharing.
- **Broken standalone media:** attaching an HTML file that still depends on neighboring local images. Embed required media or explicitly deliver a package, then decode-check every embedded payload.
- **Invented likeness:** generated portraits made without a reference photo are concept characters, not verified representations of a real person. Label them accordingly and request a reference image before claiming likeness.
- **Unverified visual claims:** static parsing and JavaScript checks do not prove layout quality. Distinguish final-layout rendering from separate inspection of source images or a contact sheet.

## Verification

Use `references/html-delivery-checklist.md` for a compact pre-delivery audit. At minimum confirm:

- the requested content and format are present;
- HTML parses and has no duplicate IDs or broken local anchors;
- embedded JavaScript passes a syntax check when a JS runtime is available;
- external factual claims are cited;
- no confidential data or unnecessary remote dependencies are included;
- no other output format was generated or delivered unless explicitly requested;
- external delivery has the required approval and a verifiable receipt.
