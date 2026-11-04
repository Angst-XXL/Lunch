#!/usr/bin/env python3
"""Z dnešní stránky obědů (formát pro Artifact, bez <html>/<head>) vyrobí index.html pro GitHub Pages.

Použití: python3 pages-index.py obedy-RRRR-MM-DD.html
"""
import sys

src = sys.argv[1]
body = open(src, encoding="utf-8").read()
cut = body.find("<style>")
head_part, rest = (body[:cut], body[cut:]) if cut > 0 else ("", body)
head = (
    '<!doctype html><html lang="cs"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    "<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);"
    "padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}"
    "[hidden]{display:none!important}</style>\n" + head_part.strip() + "\n</head><body>\n"
)
open("index.html", "w", encoding="utf-8").write(head + rest.rstrip() + "\n</body></html>\n")
print("index.html z", src)
