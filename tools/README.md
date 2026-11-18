# Archived profile visuals

`gen-banner.py` builds `assets/header-dark.svg` and `assets/header-light.svg`,
the banners from the previous profile README. The visual generation workflow
is available for manual runs.

```bash
python tools/gen-banner.py
```

Edit the colours in `T` or the text in `build()`, rerun, commit the SVGs.

## Fonts

JetBrains Mono is embedded in the SVG as a base64 data URI — an SVG rendered
through `<img>` (which is how GitHub serves it) cannot fetch external fonts, so
a Google Fonts link would silently fall back to the system monospace.

The `.woff2` files here are subset to only the ~30 glyphs the banner uses,
which is why they're 2KB instead of 200KB. To change the banner text to use new
characters, re-subset first:

```bash
pyftsubset JetBrainsMono-Regular.ttf --text="<every char used>" \
  --flavor=woff2 --output-file=jb-Regular.woff2 --layout-features='' --no-hinting
```

then re-embed the base64 into `gen-banner.py`.
