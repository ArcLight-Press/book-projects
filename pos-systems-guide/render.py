"""
Render The Complete POS Systems Guide 2026 — ArcLight Press
Exhaustive business reference guide, US Letter report format via WeasyPrint.
"""
import importlib, sys, os

# Build HTML from parts
from parts.styles import CSS
from parts.cover import COVER
from parts.front_matter import FRONT_MATTER
from parts.ch01_introduction import CH01
from parts.ch02_anatomy import CH02
from parts.ch03_pos_types import CH03
from parts.ch04_clover import CH04
from parts.ch05_toast import CH05
from parts.ch06_square import CH06
from parts.ch07_shift4 import CH07
from parts.ch08_lightspeed import CH08
from parts.ch09_shopify import CH09
from parts.ch10_revel import CH10
from parts.ch11_touchbistro import CH11
from parts.ch12_spoton import CH12
from parts.ch13_fees import CH13
from parts.ch14_cash_discount import CH14
from parts.ch15_hardware import CH15
from parts.ch16_security import CH16
from parts.ch17_integrations import CH17
from parts.ch18_industry import CH18
from parts.ch19_negotiating import CH19
from parts.ch20_implementation import CH20
from parts.ch21_legal import CH21
from parts.ch22_future import CH22
from parts.ch23_comparison import CH23
from parts.ch24_decision import CH24
from parts.ch25_glossary import CH25
from parts.back_matter import BACK_MATTER

HTML = f"""<!DOCTYPE html>
<html lang="en" class="report">
<head><meta charset="utf-8"><title>The Complete POS Systems Guide — 2026 Edition</title>
<style>{CSS}</style>
</head>
<body class="report">
{COVER}
{FRONT_MATTER}
{CH01}{CH02}{CH03}
{CH04}{CH05}{CH06}{CH07}{CH08}{CH09}{CH10}{CH11}{CH12}
{CH13}{CH14}{CH15}{CH16}{CH17}{CH18}
{CH19}{CH20}{CH21}{CH22}
{CH23}{CH24}{CH25}
{BACK_MATTER}
</body></html>
"""

from weasyprint import HTML as WHTML, default_url_fetcher
def fetcher(url, t=15):
    try: return default_url_fetcher(url, timeout=t)
    except Exception: return {'string': b'', 'mime_type': 'image/jpeg'}

out = "/work/pos_guide/The_Complete_POS_Systems_Guide_2026_ArcLight_Press.pdf"
WHTML(string=HTML, url_fetcher=fetcher).write_pdf(out)
print(f"✅ Rendered to {out}")

# Verify
import fitz
doc = fitz.open(out)
print(f"📄 {len(doc)} pages")
for i, page in enumerate(doc):
    for x0, y0, x1, y1, text, *_ in page.get_text("blocks"):
        if not text.strip(): continue
doc.close()
