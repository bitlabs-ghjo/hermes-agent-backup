# Self-contained HTML Media Packaging

Use this pattern when an HTML deliverable contains generated portraits, diagrams, icons, or other local media and the HTML itself will be attached or moved independently.

## Why

Relative paths such as `src="portrait.jpg"` work only while the companion files remain beside the HTML. A standalone attachment must either embed its media or be delivered as an explicitly requested package.

## Default

- For a single HTML deliverable, embed local images as `data:` URIs.
- Keep CSS and JavaScript inline unless a remote dependency is necessary and documented.
- If embedded media makes the file impractically large, offer a ZIP package or a hosted asset only with the appropriate delivery approval.
- Do not claim “self-contained” while any required local relative asset remains.

## Deterministic embedding pattern

```python
from pathlib import Path
import base64, mimetypes

html_path = Path("artifact.html")
html = html_path.read_text(encoding="utf-8")
for asset in [Path("portrait.jpg"), Path("diagram.png")]:
    mime = mimetypes.guess_type(asset.name)[0] or "application/octet-stream"
    uri = f"data:{mime};base64," + base64.b64encode(asset.read_bytes()).decode("ascii")
    html = html.replace(f'src="{asset.name}"', f'src="{uri}"')
html_path.write_text(html, encoding="utf-8")
```

## Verification

Programmatically confirm all of the following:

1. Expected embedded-image count is present.
2. No required `src="local-file.ext"` references remain.
3. Every Base64 payload decodes with validation enabled.
4. Decoded byte counts are non-zero and match the source assets when source files remain available.
5. No unintended remote `script[src]` or `link[href]` dependencies remain.
6. HTML structure, JavaScript syntax, responsive layout, and print CSS are still checked separately.

A contact sheet can efficiently validate visual consistency across a generated character set, but it does not replace inspection of the final HTML layout. If browser rendering is unavailable, report static verification and character-image inspection separately.
