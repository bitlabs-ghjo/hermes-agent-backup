---
name: brand-identity-development
description: "Use when proposing or refining a company brand identity."
version: 1.0.0
author: Hermes Curator
license: MIT
metadata:
  hermes:
    tags: [brand, identity, naming, logo, business-card, positioning]
    related_skills: [claude-design, design-md, grounded-citations]
---

# Brand Identity Development

Develop a credible brand direction that connects business strategy, customer comprehension, verbal identity, visual identity, and practical applications such as business cards. Use this for new companies, rebrands, logo direction studies, naming reviews, and founder-led businesses that need an identity before they have complete brand assets.

This skill governs the **strategy and clearance workflow**. Use `claude-design` to render high-fidelity HTML option boards and `design-md` when a persistent token specification is required.

## When to Use

Use this skill when the user asks to:

- define or refine a company’s vision, mission, positioning, or brand promise;
- propose a name, tagline, logo direction, color posture, or visual identity;
- compare several identity concepts and choose a recommended direction;
- design business cards or other first-touch brand applications;
- assess whether an identity can credibly span several products or services;
- review name, domain, or category-collision risk before launch or printing.

Do not use it for a simple image-generation request with an already approved brand, or for legal trademark clearance. Use qualified counsel and official registries for clearance.

## Core Principle

A logo is not the starting point. First define what the company does, for whom, and what progression or outcome it owns. Then express that strategy through language, symbols, color, typography, and applications.

Do not make an identity look polished before checking whether the name and promise are usable.

## Workflow

### 1. Separate facts, proposals, and unknowns

Create three explicit buckets:

- **Confirmed facts:** legal/company name, founder, date, products, customer groups, geography, current assets.
- **Strategic proposals:** vision, mission, positioning, tagline, goals, visual concepts.
- **Unknowns requiring a decision:** official domain, contact details, trademark status, numeric targets, QR destination, preferred language, print quantity.

Never turn a proposed slogan, revenue target, or market position into a company fact. Use placeholders for unknown phone numbers, emails, websites, social handles, and QR targets.

### 2. Find the business through-line

When a company offers several services, do not merely list them. Find the customer journey or capability progression connecting them.

Useful patterns include:

- discover → design → implement → operate
- learn → diagnose → apply → measure
- service experience → reusable module → product

Express the brand in one plain-language sentence a non-specialist can understand in five seconds. Prefer concrete verbs over words such as “innovation,” “cutting-edge,” “insights,” or “transformation” unless those terms carry specific evidence.

### 3. Run a lightweight name-collision gate

Before recommending a logo or printing materials:

1. Search the exact company name and capitalization variants.
2. Check the primary `.com` and category-relevant domains.
3. Inspect active same-name businesses and compare their industry, audience, geography, and message.
4. Distinguish verified web findings from unverified trademark, legal-name, and social-handle status.
5. Put a material collision warning **before** visual concepts, not in the fine print.

A same-name company in a similar category is a search, domain, referral, and international-expansion risk even if it is based in another country. A web search is not legal clearance; recommend the relevant trademark registry and qualified legal review before official launch.

See `references/company-name-collision-check.md` for the evidence and reporting pattern.

### 4. Draft the verbal identity

Produce a compact hierarchy:

- **Vision:** the future state the company wants to make true.
- **Mission:** what the company repeatedly does to create that future.
- **Brand promise:** the practical expectation customers can hold.
- **Primary message:** the five-second customer-facing explanation.
- **Supporting message:** a more memorable campaign line.

A useful mission names the sequence of work and the result. Do not claim measurable impact unless the company has a measurement method or evidence.

For multi-year goals without a planning baseline, propose stage gates rather than invented numbers, for example:

- validate a repeatable offer and evidence;
- productize repeated demand;
- establish scalable or recurring delivery.

### 5. Gather multiple functional perspectives

For a consequential identity, review it through at least three independent lenses:

- **Strategy:** Does it support the business model and future expansion?
- **Revenue/customer:** Can a target customer understand and act within five seconds?
- **Delivery/education:** Can a non-technical audience understand it, and does it describe the real experience?

When temporary subagents provide these lenses, describe the result as a **role-perspective review**, not as a handoff to an independent employee profile unless that profile actually performed the work.

### 6. Generate three meaningfully different directions

Default to:

1. **Conservative:** clearest, lowest-risk interpretation.
2. **Strong-fit:** best synthesis of strategy and audience.
3. **Divergent:** useful boundary exploration or future product posture.

Each direction must vary in meaning and posture—not only color. For every option state:

- strategic idea;
- symbol rationale;
- personality;
- palette posture;
- strongest use case;
- weakness or confusion risk.

Recommend one option and explain why. Do not leave the user with an undifferentiated menu.

### 7. Show real applications

For business cards, default to a practical front/back information architecture:

**Front**
- logo/wordmark;
- name;
- plain-language role or title;
- phone, email, website.

**Back**
- one memorable message;
- service progression or short descriptor;
- one QR code with a declared destination.

Use actual standard dimensions for the intended market, minimum print-legible type, and a restrained initial print specification. Recommend a small proof run before expensive finishing.

For comparison artifacts, use a **Compare** surface: aligned option structures, one clearly marked recommendation, and toggles or side-by-side views. Include print CSS when presenting business-card concepts in HTML.

### 8. Verify at the right level

Label the asset accurately:

- **Directional prototype:** concept rationale and rough visual treatment; not cleared for official use.
- **Production design:** export-ready vectors, type licensing, color profiles, bleed/safe zones, and printer specifications checked.
- **Cleared identity:** name, trademark, domain, and similarity risks reviewed through the appropriate process.

Minimum artifact verification:

- file exists and parses;
- every option and application is present;
- internal navigation targets are valid;
- placeholders remain where source data is unknown;
- collision and clearance caveats are visible.

Visual claims require a rendered inspection. Static checks may verify structure but do not prove spacing, legibility, color, or print fidelity. Report exactly which level was verified.

For multilingual print assets, verify the **actual glyphs**, not only layout boxes:

1. Render at least the recommended front and back to raster previews at print aspect ratio.
2. Inspect non-Latin names, titles, slogans, and CTA text for tofu/missing glyphs, fallback-font substitution, clipping, and weight mismatch.
3. If the renderer lacks the needed font, load a known licensed font explicitly and render through a path that can address the font file directly; do not treat a successful HTML/SVG parse or `font-family` declaration as proof that glyphs rendered.
4. Keep a portable review artifact (for example, HTML with a stable web-font source) separate from production delivery. Before printer handoff, embed licensed fonts or convert type to outlines, then re-check bleed, safe zone, trim size, and color profile.
5. Preserve placeholders for contact and QR data, but render them as readable labels so visual spacing can still be judged.

A reliable review package can pair an interactive comparison board with raster previews of the recommended card faces. The board supports decision-making; the raster previews provide evidence that the chosen typography and composition actually render.

See `references/multilingual-print-verification.md` for the condensed font, raster-proof, and printer-handoff checklist.

### 9. Review an existing design-system handoff

When reviewing another designer's package, inspect the supplied assets rather than merely endorsing its handoff report. Separate **author-reported QA**, **reviewer-repeated checks**, and **remaining release gates**. A conditional recommendation of a direction is not official CI approval.

- Distinguish known company services from an unknown target customer or project brief; do not repeat an overly broad “business unknown” label.
- Audit governance copy inside templates: content reviewers do not automatically have authority to approve prices, contracts, publication, or deployment.
- Keep company symbols and already-approved staff character avatars as separate asset scopes unless replacement is explicitly approved.
- Prefer one realistic, representative application over adding more empty templates or logo directions. Check actual content density and keep internal editing instructions distinct from customer-facing content.
- Present actionable feedback with priorities, next-version acceptance criteria, and unresolved decisions. Separately gate delivery; message-post success does not establish that the designer read it or began work.

See `references/design-handoff-review.md` for package checks, evidence accounting, and feedback structure.

## Deliverable Structure

1. Conclusion and recommended direction
2. Confirmed facts and assumptions
3. Name/domain/trademark risk
4. Functional-perspective synthesis
5. Vision, mission, promise, and messages
6. Stage goals
7. Three identity directions with tradeoffs
8. Business-card/application proposal
9. Decisions and source data still needed
10. Verification status and next action

## Pitfalls

- Starting with aesthetics before clarifying positioning.
- Treating search-engine checks as trademark clearance.
- Hiding a serious naming collision after the logo options.
- Inventing contact details or numeric goals to make a mockup look complete.
- Showing three color swaps instead of three strategic directions.
- Using opaque English job titles when target customers need immediate clarity.
- Presenting generated marks as production-ready or legally cleared.
- Claiming a specialist employee reviewed the work when only a temporary role-prompted subagent did.
- Saying an HTML artifact was visually verified after only parsing its structure.

## Final Check

- [ ] Facts, proposals, and unknowns are separated.
- [ ] The company has a plain-language five-second explanation.
- [ ] Exact-name and domain collision checks were performed.
- [ ] Trademark/legal status is labeled verified or unverified.
- [ ] Vision, mission, promise, and message are distinct.
- [ ] Three directions differ in strategic meaning.
- [ ] One option is recommended with a reason.
- [ ] Contact and QR placeholders are not fabricated.
- [ ] Applications are appropriate to the audience and medium.
- [ ] Prototype, production, and clearance status are not conflated.
- [ ] Verification claims match what was actually tested.
