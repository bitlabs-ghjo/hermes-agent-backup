# Multilingual Print Verification

Use this when a business card, stationery item, brochure, or other print asset contains Korean or another non-Latin script.

## Why it matters

A source file can parse correctly while the rendered output silently substitutes a font or displays missing-glyph boxes. HTML/SVG structure checks do not prove typography.

## Review sequence

1. **Source check**
   - Confirm trim size, bleed, and safe zone.
   - Confirm every required face/variant exists.
   - Keep unknown contact and QR data as explicit placeholders.
2. **Font check**
   - Identify the exact font family and weights used.
   - Confirm the chosen files contain the required script glyphs and that licensing permits embedding or outlining.
3. **Rendered proof**
   - Rasterize the recommended front and back at high resolution and the correct aspect ratio.
   - If a generic SVG renderer produces tofu, use a renderer that accepts an explicit font file rather than trusting font discovery.
4. **Visual inspection**
   - Check names, titles, slogans, arrows, punctuation, and mixed Latin/non-Latin baselines.
   - Check clipping, line breaks, contrast, balance, and distance from trim.
5. **Production handoff**
   - Embed licensed fonts or outline final type.
   - Recheck CMYK/spot-color expectations with the printer.
   - Export a small proof before a large or expensive run.

## Evidence package

Keep both:

- an interactive or side-by-side comparison artifact for selecting a direction;
- raster previews of the recommended front and back showing the exact rendered typography.

Label the work as a directional prototype until final contact data, QR destination, font handling, printer specifications, and clearance checks are complete.
