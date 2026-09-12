# App-icon derivatives from approved character art

## Trigger
A user wants existing employee badges or character portraits adapted for an app icon, or reports square-image upload validation errors.

## Procedure
1. Recover previous artifact locations with session search, then inspect actual files. Prefer the original portrait over a rendered badge containing labels and borders.
2. Preserve the approved character identity; do not regenerate a face just to change aspect ratio. For bitlabs, the user approved reuse of the ARIA, MIRA, LEO, and EDEN badge characters with face/upper-body framing and no badge text.
3. Confirm the target's current upload constraints. In the observed Slack validation message, icons must be square with each side between 512 and 2000 pixels; 1024×1024 PNG satisfies that message. Do not treat these limits as immutable across platforms.
4. Inspect source dimensions and pixels. Choose a square crop around the head and upper body; avoid stretching the entire portrait. Preserve hair and chin. Top-aligned cropping worked for the source portraits in this session, but is not a universal default—inspect each source.
5. Use Pillow: convert to RGB/RGBA, crop `(left, top, left+side, top+side)`, resize to `(1024,1024)` with `Image.Resampling.LANCZOS`, save as PNG. Keep originals unchanged and use clearly named derivative files.
6. Build a manifest with expected names, source/output paths, crop rectangles, and dimensions. Read outputs back, verify format and square dimensions against limits, and reconcile the count against all requested characters.
7. Build and visually inspect a contact sheet. Check facial framing, unwanted text, distortion, and recognizability at small size. File integrity alone is not visual verification.
8. Deliver individual upload-ready files through the authorized channel. Distinguish file production from installing icons in Slack; do not claim the app configuration changed unless explicitly authorized and verified.

## Source-location reference
The approved bitlabs portrait set was located under `/opt/data/profiles/aria/artifacts/bitlabs_employee_ids/`, with originals `aria.jpg`, `mira.jpg`, `leo.jpg`, and `eden.jpg`. This is a lookup hint, not a guarantee of continued existence. Locate and inspect before reuse.

## Verification checklist
- All requested characters represented exactly once.
- Output PNGs decode successfully and meet target dimensions.
- Existing character designs preserved, not regenerated.
- No squashed aspect ratios or badge labels in avatars.
- Faces and hairstyles remain intact in each crop.
- No claim of external installation based solely on local file creation.
