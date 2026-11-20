"""Rigenera deploy/index.html (pagina completa per Netlify) da prototipo-checkin.html (versione artifact).

Uso: python3 build-deploy.py
Poi si pubblica la cartella deploy/ sul sito Netlify love-pet-checkin
(site id 5e5633a6-24e5-4a0b-9380-b0f5abc8b42d), dal connettore Netlify: deploy-site.
"""
from pathlib import Path

root = Path(__file__).parent
src = (root / "prototipo-checkin.html").read_text(encoding="utf-8")
cut = src.index("</style>") + len("</style>")
head, body = src[:cut], src[cut:]
head = head.replace('<meta charset="utf-8">\n', "")
page = (
    '<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="robots" content="noindex, nofollow">\n'
    + head
    + "\n<style>html,body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>"
    + body
    + "\n</body>\n</html>\n"
)
out = root / "deploy"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(page, encoding="utf-8")
(out / "_headers").write_text("/*\n  X-Robots-Tag: noindex, nofollow\n")
(out / "netlify.toml").write_text('[build]\n  publish = "."\n')
print("deploy/index.html:", len(page), "caratteri")
