# The Complete POS Systems Guide — 2026 Edition

**Publisher:** ArcLight Press  
**Format:** Amazon KDP (6" × 9" trim)  
**Pages:** ~149  

## Build

```bash
pip install weasyprint pymupdf
python render.py
```

## Structure

- `render.py` — Main build script
- `parts/styles.py` — CSS (KDP 6×9 formatting)
- `parts/cover.py` — Cover page
- `parts/front_matter.py` — Copyright, TOC, how-to-use
- `parts/ch01–ch25` — All 25 chapters
- `parts/back_matter.py` — About the publisher
