#!/usr/bin/env python3
"""Generate individual A4 and A3 promo flyers for each product."""

import os

PRODUCTS = [
    {
        "id": "dindy_poulet_ail",
        "name": "Saucisson Poulet à l'Ail",
        "brand": "DINDY",
        "type": "Poulet",
        "old_price": "485",
        "new_price": "242",
        "color_accent": "#E2001A",
    },
    {
        "id": "daara_poulet_piquant",
        "name": "Saucisson Poulet Piquant",
        "brand": "DAARA",
        "type": "Poulet",
        "old_price": "355",
        "new_price": "177",
        "color_accent": "#E2001A",
    },
    {
        "id": "daara_boeuf_piquant",
        "name": "Saucisson Bœuf Piquant",
        "brand": "DAARA",
        "type": "Bœuf",
        "old_price": "335",
        "new_price": "167",
        "color_accent": "#E2001A",
    },
    {
        "id": "daara_poulet_nature",
        "name": "Saucisson Poulet Nature",
        "brand": "DAARA",
        "type": "Poulet",
        "old_price": "318",
        "new_price": "159",
        "color_accent": "#E2001A",
    },
    {
        "id": "daara_boeuf_nature",
        "name": "Saucisson Bœuf Nature",
        "brand": "DAARA",
        "type": "Bœuf",
        "old_price": "299",
        "new_price": "150",
        "color_accent": "#E2001A",
    },
    {
        "id": "nafy_boeuf_piquant",
        "name": "Saucisson Bœuf Piquant",
        "brand": "NAFY",
        "type": "Bœuf",
        "old_price": "299",
        "new_price": "150",
        "color_accent": "#E2001A",
    },
]

ICON = {"Poulet": "🍗", "Bœuf": "🥩"}

CSS_A4 = """
    @page { size: A4 portrait; margin: 0; }
    body { width: 210mm; height: 297mm; font-family: Arial, sans-serif; margin: 0; overflow: hidden; background: #fff; }
    .page { width: 210mm; height: 297mm; display: flex; flex-direction: column; overflow: hidden; }
"""

CSS_A3 = """
    @page { size: A3 portrait; margin: 0; }
    body { width: 297mm; height: 420mm; font-family: Arial, sans-serif; margin: 0; overflow: hidden; background: #fff; }
    .page { width: 297mm; height: 420mm; display: flex; flex-direction: column; overflow: hidden; }
"""

def make_flyer(p, fmt):
    is_a3 = fmt == "A3"
    # Scale factors vs A4
    s = 1.45 if is_a3 else 1.0

    def px(v): return f"{v * s:.1f}pt"

    icon = ICON.get(p["type"], "🥩")

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Flyer {fmt} – {p['brand']} {p['name']} – Auchan Kaolack</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    {"" if is_a3 else ""}
    {CSS_A3 if is_a3 else CSS_A4}

    /* HEADER */
    .header {{
      background: #E2001A;
      color: white;
      padding: {px(7)} {px(12)} {px(6)};
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .logo {{
      font-size: {px(28)};
      font-weight: 900;
    }}
    .logo span {{
      background: white;
      color: #E2001A;
      padding: 2px {px(8)};
      border-radius: 4px;
    }}
    .header-right {{
      text-align: right;
      font-size: {px(8)};
      line-height: 1.5;
      opacity: 0.92;
    }}
    .header-right strong {{
      font-size: {px(10)};
      display: block;
    }}

    /* BANNER -50% */
    .banner {{
      background: #FF6B00;
      color: white;
      text-align: center;
      padding: {px(8)} {px(12)};
    }}
    .banner-inner {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: {px(10)};
    }}
    .circle-50 {{
      background: white;
      color: #E2001A;
      font-size: {px(36)};
      font-weight: 900;
      width: {px(52)};
      height: {px(52)};
      border-radius: 50%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      line-height: 1;
      flex-shrink: 0;
    }}
    .circle-50 .pct {{ font-size: {px(13)}; font-weight: 900; }}
    .banner h1 {{
      font-size: {px(26)};
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 2px;
      line-height: 1.1;
    }}
    .banner p {{ font-size: {px(9)}; opacity: 0.95; margin-top: {px(2)}; }}

    /* BLACK STRIP */
    .strip {{
      background: #1a1a1a;
      color: #FFD700;
      text-align: center;
      padding: {px(4)} {px(12)};
      font-size: {px(9)};
      font-weight: 900;
      letter-spacing: 1px;
      text-transform: uppercase;
    }}

    /* PRODUCT HERO */
    .hero {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: #f5f5f5;
      padding: {px(10)} {px(16)};
      gap: {px(8)};
    }}

    .product-icon {{
      font-size: {px(72)};
      line-height: 1;
    }}

    .brand-chip {{
      background: #1a1a1a;
      color: white;
      font-size: {px(12)};
      font-weight: 900;
      letter-spacing: 3px;
      padding: {px(3)} {px(12)};
      border-radius: {px(20)};
      text-transform: uppercase;
    }}

    .product-name-hero {{
      font-size: {px(28)};
      font-weight: 900;
      color: #1a1a1a;
      text-align: center;
      line-height: 1.1;
    }}

    .type-badge {{
      background: {'#FF6B00' if p['type'] == 'Poulet' else '#8B4513'};
      color: white;
      font-size: {px(10)};
      font-weight: 900;
      padding: {px(2)} {px(10)};
      border-radius: {px(4)};
      text-transform: uppercase;
      letter-spacing: 1px;
    }}

    /* PRICE BOX */
    .price-box {{
      background: white;
      border: 3px solid #E2001A;
      border-radius: {px(10)};
      padding: {px(10)} {px(20)};
      text-align: center;
      width: 100%;
      max-width: {px(180)};
      box-shadow: 0 4px 16px rgba(226,0,26,0.15);
    }}

    .price-label {{
      font-size: {px(8)};
      color: #888;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: {px(3)};
    }}

    .price-old-row {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: {px(8)};
      margin-bottom: {px(4)};
    }}

    .price-old {{
      font-size: {px(16)};
      color: #bbb;
      text-decoration: line-through;
    }}

    .price-was {{
      font-size: {px(8)};
      color: #aaa;
    }}

    .price-new-row {{
      display: flex;
      align-items: baseline;
      justify-content: center;
      gap: {px(4)};
    }}

    .price-new {{
      font-size: {px(58)};
      font-weight: 900;
      color: #E2001A;
      line-height: 1;
    }}

    .price-unit {{
      font-size: {px(12)};
      color: #666;
      font-weight: normal;
    }}

    .price-economy {{
      margin-top: {px(5)};
      font-size: {px(9)};
      color: #555;
    }}
    .price-economy strong {{
      color: #E2001A;
      font-size: {px(11)};
    }}

    .per-kg-note {{
      font-size: {px(9)};
      color: #888;
      margin-top: {px(4)};
      font-style: italic;
    }}

    /* BOTTOM BADGES */
    .badges {{
      display: flex;
      justify-content: center;
      gap: {px(6)};
      padding: 0 {px(12)};
    }}

    .badge {{
      background: white;
      border: 1.5px solid #ddd;
      border-radius: {px(6)};
      padding: {px(4)} {px(6)};
      text-align: center;
      flex: 1;
      max-width: {px(50)};
    }}

    .badge .bicon {{ font-size: {px(14)}; display: block; margin-bottom: {px(2)}; }}
    .badge .blabel {{ font-size: {px(6.5)}; color: #555; font-weight: bold; text-transform: uppercase; line-height: 1.2; }}

    /* FOOTER */
    .footer {{
      background: #E2001A;
      color: white;
      padding: {px(5)} {px(12)};
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .footer-left {{
      font-size: {px(8)};
      line-height: 1.6;
    }}
    .footer-left strong {{ font-size: {px(10)}; display: block; }}
    .validity {{
      background: white;
      color: #E2001A;
      font-size: {px(7)};
      padding: {px(1)} {px(3)};
      border-radius: {px(3)};
      font-weight: 900;
      margin-top: {px(1)};
      display: inline-block;
      text-transform: uppercase;
    }}
    .footer-right {{
      text-align: right;
      font-size: {px(7)};
      opacity: 0.85;
      line-height: 1.5;
    }}

    @media print {{
      body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    }}
  </style>
</head>
<body>
<div class="page">

  <div class="header">
    <div class="logo"><span>auchan</span></div>
    <div class="header-right">
      <strong>Auchan Kaolack (SN1041)</strong>
      Département Frais · Rayon 44 – Charcuterie Traditionnelle
    </div>
  </div>

  <div class="banner">
    <div class="banner-inner">
      <div class="circle-50"><div>-50</div><div class="pct">%</div></div>
      <div>
        <h1>GRAND DÉSTOCKAGE<br>CHARCUTERIE</h1>
        <p>50% de réduction · Offre valable jusqu'à épuisement des stocks</p>
      </div>
      <div class="circle-50"><div>-50</div><div class="pct">%</div></div>
    </div>
  </div>

  <div class="strip">⚡ OFFRES LIMITÉES — JUSQU'À ÉPUISEMENT DES STOCKS — NE RATEZ PAS CES PRIX ! ⚡</div>

  <div class="hero">
    <div class="product-icon">{icon}</div>
    <div class="brand-chip">{p['brand']}</div>
    <div class="product-name-hero">{p['name']}</div>
    <div class="type-badge">100% {p['type']} · Halal</div>

    <div class="price-box">
      <div class="price-label">Prix promotionnel</div>
      <div class="price-old-row">
        <span class="price-was">Ancien prix :</span>
        <span class="price-old">{p['old_price']} F / 100g</span>
      </div>
      <div class="price-new-row">
        <span class="price-new">{p['new_price']}</span>
        <span class="price-unit">F / 100g</span>
      </div>
      <div class="price-economy">Vous économisez <strong>{int(p['old_price']) - int(p['new_price'])} F</strong> par 100g</div>
      <div class="per-kg-note">Vendu au poids · Prix calculé à la découpe</div>
    </div>
  </div>

  <div class="badges">
    <div class="badge"><span class="bicon">{icon}</span><span class="blabel">100% {p['type']} Halal</span></div>
    <div class="badge"><span class="bicon">❄️</span><span class="blabel">Chaîne du Froid Respectée</span></div>
    <div class="badge"><span class="bicon">✅</span><span class="blabel">Qualité Contrôlée</span></div>
    <div class="badge"><span class="bicon">📅</span><span class="blabel">DLC Vérifiée Chaque Jour</span></div>
  </div>

  <div class="footer">
    <div class="footer-left">
      <strong>Auchan Kaolack · Rayon 44</strong>
      Charcuterie Traditionnelle
      <span class="validity">OFFRE LIMITÉE – JUSQU'À ÉPUISEMENT DU STOCK</span>
    </div>
    <div class="footer-right">
      Prix au 100g · Vendu au poids.<br>
      Offre sous réserve de disponibilité.<br>
      Voir conditions en magasin.
    </div>
  </div>

</div>
</body>
</html>"""
    return html


output_dir = os.path.dirname(os.path.abspath(__file__))
count = 0

for p in PRODUCTS:
    for fmt in ["A4", "A3"]:
        filename = f"flyer_{fmt}_{p['id']}.html"
        path = os.path.join(output_dir, filename)
        html = make_flyer(p, fmt)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: {filename}")
        count += 1

print(f"\nDone — {count} flyers generated.")
