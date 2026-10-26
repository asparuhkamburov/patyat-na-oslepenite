from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://krasenkamburov.github.io/'
SLUGS = ['vodopadat', 'patyat-na-oslepenite', 'osiyanie-dnes', 'zavetat-na-medeya', 'kamakat-ot-vaterlo', 'zhivotat-na-geroya', 'dati', 'poltargayst', 'velikden', 'saborna-kniga', 'satirikonite-na-abarbareya', 'izkusheniya-v-zdracha', 'vrazka-goticheski-klyuchove', 'sedem-piesi', 'chetvartiyat-eshelon']

def redirect(path):
    target = BASE + path
    return f'''<!doctype html>
<html lang="bg"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Красен Камбуров — нов адрес</title><link rel="canonical" href="{html.escape(target)}">
<script>location.replace({json.dumps(target)} + location.search + location.hash);</script>
<noscript><meta http-equiv="refresh" content="0;url={html.escape(target)}"></noscript>
<style>body{{max-width:46rem;margin:12vh auto;padding:1.5rem;font:1.2rem/1.6 Georgia,serif;background:#faf8f0;color:#222}}a{{color:#445330}}</style></head>
<body><h1>Сайтът на Красен Камбуров е с нов адрес</h1><p><a href="{html.escape(target)}">Продължете към krasenkamburov.github.io</a></p></body></html>'''

if __name__ == '__main__':
    paths = ['', *['books/' + slug + '/' for slug in SLUGS]]
    for path in paths:
        destination = ROOT / path / 'index.html'
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(redirect(path), encoding='utf-8')
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + BASE + 'sitemap.xml\n', encoding='utf-8')
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + BASE + '</loc></url></urlset>\n', encoding='utf-8')
