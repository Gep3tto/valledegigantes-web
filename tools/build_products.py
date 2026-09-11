# -*- coding: utf-8 -*-
"""Build the four product pages from one template so their chrome never drifts.

    python tools/build_products.py

Edit PRODUCTS below to change copy or data. Values marked "Por confirmar" are owner
inputs listed in SPEC.md §15.
"""
import json, os, html
from urllib.parse import quote
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.afergreens.com"
WA = "526141690797"
CERT = {
    "campo": ("373629", "https://secure.azzule.com/PGFSDocuments/PGFS_Certificate_SCS-PGFS-1546_373629_0_SP.pdf"),
    "cuadrilla": ("373630", "https://secure.azzule.com/PGFSDocuments/PGFS_Certificate_SCS-PGFS-1546_373630_0_SP.pdf"),
    "empaque": ("373631", "https://secure.azzule.com/PGFSDocuments/PGFS_Certificate_SCS-PGFS-1562_373631_0_SP.pdf"),
}
MONTHS = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
PENDING = '<span class="pending">Por confirmar</span>'

ORDER = ["melon", "chiltepin", "jalapeno", "chipotle"]

PRODUCTS = {
    "melon": {
        "name": "Melón dulce del desierto",
        "short": "Melón",
        "title": "Melón dulce del desierto — Cantaloupe de Chihuahua a granel | AFER Greens",
        "description": "Melón cantaloupe de pulpa naranja, firme y dulce, cultivado en el Valle de Gigantes, Chihuahua. 2–3 kg por pieza, calibres 9's y 9j's, venta a granel. Primus GFS. Mayoreo y exportación.",
        "eyebrow": "La fruta del valle",
        "h1": "Melón dulce del <em>desierto</em>",
        "sub": "Cantaloupe de pulpa naranja, firme y dulce, cultivado en suelo mineral y clima semidesértico del <strong>Valle de Gigantes</strong>, Saucillo, Chihuahua. Fruto de 2 a 3 kg en calibres 9's y 9j's. Cosecha concentrada, cadena de frío desde el campo y certificación Primus GFS.",
        "meta": [("2–3 kg", "Peso por pieza"), ("9's · 9j's", "Calibres"), ],
        "image": "melon", "image_alt": "Melón cantaloupe recién cosechado en el Valle de Gigantes, Chihuahua",
        "portrait": True,
        "specs": [
            ("Tipo", "Melón cantaloupe (Western Shipper), pulpa naranja"),
            ("Variedad", "Gran Torino F1 (HM.Clause / Harris Moran)"),
            ("Dulzura (°Brix)", PENDING + " — rango por lote"),
            ("Calibre", "2 a 3 kg por pieza. 6 a 9 frutos por caja en tamaños 9's y 9j's"),
            ("Forma y piel", "Fruto esférico, piel reticulada uniforme de patrón fino y denso"),
            ("Pulpa", "Naranja, firme, cavidad de semilla pequeña"),
            ("Resistencias", "Fusarium oxysporum f.sp. melonis razas 0,2 (HR) · Podosphaera xanthii razas US 1,2 (IR)"),
            ("Vida de anaquel", "Extendida con cadena de frío desde cosecha"),
        ],
        "logistics": [
            ("Temporada", PENDING + " — cultivo de temporada, ver calendario"),
            ("Pedido mínimo", PENDING),
            ("Empaque", "Granel sobre tarima o macrobin de madera · cajas por tarima " + PENDING),
            ("Incoterms", PENDING),
            ("Tiempo de entrega", PENDING),
            ("Fracción arancelaria", PENDING),
        ],
        "season": [],
        "pres_title": "Formato a <em>granel</em>.",
        "pres_intro": "Venta a granel sobre tarima o macrobin de madera, para distribución mayorista, retail y exportación al mercado fresco.",
        "presentations": [("Mayoreo / retail / exportación", "Granel", "melon-granel", "Tarima o macrobin de madera con cadena de frío desde el campo hasta destino.", "Macrobin de madera con melón a granel sobre tarima")],
        "states": [("Cadena de frío", "Manejo controlado desde cosecha hasta destino"), ("Cosecha concentrada", "Calidad uniforme de fruto por lote")],
        "uses_title": "Usos en mercado <em>fresco</em>.",
        "uses_intro": "Fruta para canal de mayoreo, retail, food service y exportación al mercado fresco norteamericano.",
        "uses": ["Retail y supermercado", "Food service y hospitalidad", "Centrales de abasto", "Exportación a EE. UU. y Canadá", "Cortes y procesado en fresco", "Jugos y postres"],
        "cta": "Indique volumen, calibre y destino. Respondemos con mínimo, empaque por tarima, Incoterms y fechas de la temporada.",
        "wa_msg": "Hola, me interesa cotizar melón dulce del desierto (volumen y destino: ).",
        "category": "Melón / Frutas frescas",
        "schema_props": [("Variedad", "Gran Torino F1 (HM.Clause / Harris Moran)"), ("Tipología", "Western Shipper"), ("Color de pulpa", "Naranja"), ("Calibre por pieza", "2-3 kg"), ("Piezas por caja", "6-9 (9's y 9j's)"), ("Resistencia HR", "Fusarium oxysporum f.sp. melonis razas 0,2"), ("Resistencia IR", "Podosphaera xanthii razas US 1,2"), ("Origen", "Valle de Gigantes, Saucillo, Chihuahua, MX")],
        "offers": [("AFER-MEL-GRANEL", "Melón dulce del desierto — Granel")],
        "sku": "AFER-MEL",
    },
    "chiltepin": {
        "name": "Chile chiltepín",
        "short": "Chiltepín",
        "title": "Chile Chiltepín de Chihuahua — 100 g, 1 kg y 10 kg | AFER Greens",
        "description": "Chile chiltepín seco y fresco del Valle de Gigantes, Chihuahua. Picor 50,000–100,000 SHU, diámetro 5–8 mm. Presentaciones de 100 g, 1 kg y 10 kg. Primus GFS. Mayoreo y exportación.",
        "eyebrow": "El chile del norte",
        "h1": "Chile <em>chiltepín</em>",
        "sub": "Chile de 5 a 8 mm, picor intenso y final limpio. Cosecha manual y selectiva en el <strong>Valle de Gigantes</strong>, Saucillo, Chihuahua, en cultivo controlado bajo certificación Primus GFS. Disponible seco y fresco.",
        "meta": [("50–100k", "SHU"), ("5–8 mm", "Diámetro")],
        "image": "chiltepin", "image_alt": "Chiltepín rojo en la mano sobre la cama de secado, Valle de Gigantes",
        "portrait": True,
        "specs": [
            ("Picor", "50,000 a 100,000 SHU. Intenso, directo, de final limpio"),
            ("Diámetro", "5 a 8 mm, calibre compacto y uniforme"),
            ("Color", "Rojo intenso al madurar; verde oscuro en fruto fresco"),
            ("Forma", "Redonda u ovoide. Superficie lisa en fresco, arrugada al secarse"),
            ("Vida de anaquel (seco)", "12 a 18 meses en lugar fresco, seco y sin sol directo"),
            ("Vida de anaquel (fresco)", "7 a 12 días refrigerado"),
            ("Cosecha", "Manual y selectiva, cultivo controlado"),
        ],
        "logistics": [
            ("Disponibilidad", "Seco: todo el año sujeto a inventario · Fresco: " + PENDING),
            ("Pedido mínimo", PENDING + " por presentación"),
            ("Empaque", "Bolsa 100 g · bolsa 1 kg · saco 10 kg · unidades por tarima " + PENDING),
            ("Incoterms", PENDING),
            ("Tiempo de entrega", PENDING),
            ("Fracción arancelaria", PENDING),
        ],
        "season": list(range(12)),
        "pres_title": "Tres <em>presentaciones</em>.",
        "pres_intro": "Chiltepín seco y fresco en tres formatos de empaque: canal especializado, cocina profesional y formulación industrial.",
        "presentations": [
            ("Retail gourmet", "100 g", "chiltepin-100g", "Bolsa con ventana para canal especializado y tiendas gourmet.", "Bolsa de 100 g de chiltepín Valle de Gigantes"),
            ("HoReCa / restaurante", "1 kg", "chiltepin-1kg", "Bolsa kraft para cocinas de alto volumen y salsas de autor.", "Bolsa de 1 kg de chiltepín Valle de Gigantes"),
            ("Industrial / procesadora", "10 kg", "chiltepin-10kg", "Saco para formulación de salsas, adobos y marinados.", "Saco de 10 kg de chiltepín Valle de Gigantes sobre tarima"),
        ],
        "states": [("Seco", "Vida útil 12 a 18 meses en lugar fresco, seco y sin sol directo"), ("Fresco", "Vida útil 7 a 12 días refrigerado")],
        "uses_title": "Usos en <em>cocina</em> e industria.",
        "uses_intro": "Ingrediente de cocina tradicional mexicana, gastronomía contemporánea y formulación industrial.",
        "uses": ["Salsas tradicionales", "Adobos y escabeches", "Condimento entero", "Preparaciones gourmet", "Formulación industrial"],
        "cta": "Indique volumen, presentación (100 g, 1 kg o 10 kg) y destino. Respondemos con mínimo, empaque por tarima e Incoterms.",
        "wa_msg": "Hola, me interesa cotizar chiltepín (presentación y volumen: ).",
        "category": "Chile seco / Especias",
        "schema_props": [("Picor (SHU)", "50,000–100,000"), ("Diámetro", "5-8 mm"), ("Vida útil (seco)", "12-18 meses"), ("Vida útil (fresco)", "7-12 días refrigerado"), ("Origen", "Valle de Gigantes, Saucillo, Chihuahua, MX")],
        "offers": [("AFER-CHIL-100G", "Chiltepín 100 g"), ("AFER-CHIL-1KG", "Chiltepín 1 kg"), ("AFER-CHIL-10KG", "Chiltepín 10 kg")],
        "sku": "AFER-CHIL",
    },
    "jalapeno": {
        "name": "Jalapeño fresco",
        "short": "Jalapeño",
        "title": "Jalapeño Fresco de Chihuahua — Caja 17 kg y Arpilla 30 kg | AFER Greens",
        "description": "Jalapeño fresco del Valle de Gigantes, Chihuahua. Pared gruesa, calibre uniforme, picor 2,500–8,000 SHU. Caja 17 kg (1 1/9 bushel) y arpilla 30 kg. Primus GFS. Mayoreo y exportación.",
        "eyebrow": "La hortaliza del valle",
        "h1": "Jalapeño <em>fresco</em>",
        "sub": "Fruto firme de pared gruesa y calibre uniforme, verde oscuro brillante, picor medio de perfil vegetal. Cosecha manual y clasificación en campo en el <strong>Valle de Gigantes</strong>, Saucillo, Chihuahua, con cadena de frío y certificación Primus GFS.",
        "meta": [("2.5–8k", "SHU"), ("5–9 cm", "Longitud")],
        "image": "jalapeno", "image_alt": "Cuadrilla vaciando jalapeño fresco en bin de campo, Valle de Gigantes",
        "portrait": True,
        "specs": [
            ("Picor", "2,500 a 8,000 SHU. Pungencia media, sabor vegetal limpio"),
            ("Calibre", "Longitud 5 a 9 cm, diámetro 2.5 a 3.5 cm. Selección uniforme"),
            ("Color", "Verde oscuro brillante"),
            ("Forma", "Cónica alargada con ápice redondeado. Pared gruesa y carnosa"),
            ("Vida de anaquel", "10 a 21 días refrigerado entre 0 y 4 °C, HR 85–95 %"),
            ("Cosecha", "Manual y selectiva; clasificación por calibre y madurez en campo"),
        ],
        "logistics": [
            ("Temporada", PENDING + " — cultivo de temporada, ver calendario"),
            ("Pedido mínimo", PENDING + " por presentación"),
            ("Empaque", "Caja 17 kg (1 1/9 bushel) · arpilla 30 kg · cajas por tarima " + PENDING),
            ("Incoterms", PENDING),
            ("Tiempo de entrega", PENDING),
            ("Fracción arancelaria", PENDING),
        ],
        "season": [],
        "pres_title": "Dos <em>formatos</em> de empaque.",
        "pres_intro": "Caja estándar de exportación y arpilla industrial, según canal y destino.",
        "presentations": [
            ("Exportación / retail", "17 kg", "jalapeno-17kg", "Caja 1 1/9 bushel, el formato logístico estándar para mayoreo, retail y exportación en fresco.", "Caja de 17 kg de jalapeño Valle de Gigantes"),
            ("Industrial / procesadora", "30 kg", "jalapeno-30kg", "Arpilla de malla para encurtidoras, salseras y transformación industrial.", "Arpilla de 30 kg de jalapeño Valle de Gigantes"),
        ],
        "states": [("Fresco", "Vida útil 10 a 21 días refrigerado entre 0 y 4 °C"), ("Cadena de frío", "Manejo controlado desde cosecha hasta destino")],
        "uses_title": "Usos en fresco e <em>industria</em>.",
        "uses_intro": "Hortaliza para mercado en fresco, formulación industrial y cocina tradicional mexicana.",
        "uses": ["Encurtidos y escabeches", "Salsas industriales", "Rellenos y toreados", "Cocina mexicana tradicional", "Mercado fresco y retail", "Materia prima para chipotle"],
        "cta": "Indique volumen, presentación (caja 17 kg o arpilla 30 kg) y destino. Respondemos con mínimo, cajas por tarima, Incoterms y fechas de la temporada.",
        "wa_msg": "Hola, me interesa cotizar jalapeño fresco (presentación y volumen: ).",
        "category": "Chile fresco / Hortalizas",
        "schema_props": [("Picor (SHU)", "2,500–8,000"), ("Longitud", "5-9 cm"), ("Diámetro", "2.5-3.5 cm"), ("Vida útil (fresco)", "10-21 días refrigerado 0-4°C"), ("Origen", "Valle de Gigantes, Saucillo, Chihuahua, MX")],
        "offers": [("AFER-JAL-17KG", "Jalapeño caja 17 kg (1 1/9 bushel)"), ("AFER-JAL-30KG", "Jalapeño arpilla 30 kg")],
        "sku": "AFER-JAL",
    },
    "chipotle": {
        "name": "Chipotle ahumado con mezquite",
        "short": "Chipotle",
        "title": "Chipotle Ahumado con Mezquite — Arpilla 30 kg | AFER Greens",
        "description": "Chipotle ahumado lento con leña de mezquite en el Valle de Gigantes, Chihuahua. Color caoba, picor 8,000–25,000 SHU. Arpilla 30 kg para salsas, charcutería y exportación. Primus GFS.",
        "eyebrow": "El chile ahumado",
        "h1": "Chipotle ahumado con <em>mezquite</em>",
        "sub": "Jalapeño rojo maduro de nuestra propia cosecha, ahumado lentamente con leña de mezquite hasta su deshidratación completa. Color caoba, aroma profundo, humo limpio con notas terrosas. Producido en el <strong>Valle de Gigantes</strong>, Saucillo, Chihuahua, con trazabilidad de origen y certificación Primus GFS.",
        "meta": [("8–25k", "SHU"), ("Mezquite", "Ahumado lento")],
        "image": "chipotle", "image_alt": "Chipotle ahumado con mezquite sobre bandeja de secado, Valle de Gigantes",
        "portrait": True,
        "specs": [
            ("Picor", "8,000 a 25,000 SHU. Pungencia concentrada, perfil ahumado dulce"),
            ("Proceso", "Ahumado lento con leña de mezquite hasta deshidratación completa. Lote artesanal"),
            ("Materia prima", "Jalapeño rojo maduro de cosecha propia"),
            ("Color", "Caoba ahumada, rojo profundo con tonos cobrizos"),
            ("Calibre", "Longitud 4 a 7 cm tras deshidratación. Pieza entera, sin fragmentos"),
            ("Forma", "Cónica deshidratada, superficie arrugada con relieve longitudinal y tallo seco"),
            ("Vida de anaquel", "12 a 24 meses en lugar fresco y seco. No requiere refrigeración"),
        ],
        "logistics": [
            ("Disponibilidad", "Todo el año sujeto a inventario"),
            ("Pedido mínimo", PENDING),
            ("Empaque", "Arpilla 30 kg · arpillas por tarima " + PENDING),
            ("Incoterms", PENDING),
            ("Tiempo de entrega", PENDING),
            ("Fracción arancelaria", PENDING),
        ],
        "season": list(range(12)),
        "pres_title": "Arpilla <em>industrial</em>.",
        "pres_intro": "Formato a granel para procesadoras de salsas, charcutería ahumada, retail gourmet y exportación.",
        "presentations": [("Industrial / gourmet / exportación", "30 kg", "chipotle-30kg", "Arpilla de polipropileno blanco, cosida, para almacenamiento sin refrigeración.", "Arpilla de 30 kg de chipotle Valle de Gigantes sobre tarima")],
        "states": [("Producto seco", "Vida útil 12 a 24 meses en lugar fresco y seco"), ("Sin cadena de frío", "No requiere refrigeración para almacenamiento ni transporte")],
        "uses_title": "Usos en cocina e <em>industria</em>.",
        "uses_intro": "Chile ahumado para cocina mexicana tradicional, gastronomía gourmet y formulación industrial.",
        "uses": ["Adobos y marinadas", "Salsas BBQ y morita", "Salsas industriales", "Charcutería ahumada", "Cocina gourmet y de autor", "Conservas y encurtidos", "Polvo y molienda"],
        "cta": "Indique volumen y destino. Respondemos con mínimo, arpillas por tarima, Incoterms y tiempo de entrega.",
        "wa_msg": "Hola, me interesa cotizar chipotle ahumado con mezquite (volumen y destino: ).",
        "category": "Chile ahumado / Especias",
        "schema_props": [("Picor (SHU)", "8,000–25,000"), ("Longitud", "4-7 cm (deshidratado)"), ("Color", "Caoba ahumada / rojo profundo"), ("Proceso", "Ahumado lento con leña de mezquite hasta deshidratación"), ("Vida útil", "12-24 meses en lugar fresco y seco, sin refrigeración"), ("Origen", "Valle de Gigantes, Saucillo, Chihuahua, MX")],
        "offers": [("AFER-CHI-30KG", "Chipotle ahumado con mezquite, arpilla 30 kg")],
        "sku": "AFER-CHI",
    },
}

ICONS = """    <svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
        <symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 12h16M4 6h16M4 18h16"/></symbol>
        <symbol id="i-x" viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></symbol>
        <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></symbol>
        <symbol id="i-ext" viewBox="0 0 24 24"><path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/></symbol>
        <symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol>
        <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" stroke="none" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></symbol>
    </svg>"""

HEADER = """    <header id="site-header">
        <div class="nav-container">
            <div class="logo">
                <a href="/" aria-label="AFER Greens — inicio"><picture>
                    <source srcset="/logo.webp" type="image/webp">
                    <img src="/logo.png?v=3" alt="AFER Greens — Valle de Gigantes" width="1107" height="487" fetchpriority="high" decoding="async">
                </picture></a>
            </div>
            <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-main" aria-label="Abrir menú">
                <svg class="ic ic-menu" aria-hidden="true"><use href="#i-menu"/></svg>
                <svg class="ic ic-x" aria-hidden="true"><use href="#i-x"/></svg>
            </button>
            <nav class="nav-main" id="nav-main" aria-label="Principal">
                <ul>
                    <li><a href="/#productos">Productos</a></li>
                    <li><a href="/#certificaciones">Certificaciones</a></li>
                    <li><a href="/#nosotros">Nosotros</a></li>
                    <li><a href="/#contacto" class="nav-cta in-menu">Cotizar</a></li>
                </ul>
                <a href="/#contacto" class="nav-cta in-bar">Cotizar</a>
            </nav>
        </div>
    </header>"""

FOOTER = """    <footer>
        <div class="footer-inner">
            <div class="footer-grid">
                <div class="footer-brand">
                    <div class="footer-logo"><a href="/" aria-label="AFER Greens — inicio"><picture>
                        <source srcset="/logo.webp" type="image/webp">
                        <img src="/logo.png?v=3" alt="AFER Greens — Valle de Gigantes" width="1107" height="487" loading="lazy" decoding="async">
                    </picture></a></div>
                    <p>Melón y chile del Valle de Gigantes, Chihuahua. Certificación Primus GFS de campo a empaque.</p>
                </div>
                <div class="footer-col">
                    <h2>Productos</h2>
                    <ul>
                        <li><a href="/melon/">Melón dulce del desierto</a></li>
                        <li><a href="/chiltepin/">Chile chiltepín</a></li>
                        <li><a href="/jalapeno/">Jalapeño fresco</a></li>
                        <li><a href="/chipotle/">Chipotle ahumado con mezquite</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h2>Empresa</h2>
                    <ul>
                        <li><a href="/#certificaciones">Certificaciones</a></li>
                        <li><a href="/#nosotros">Nosotros</a></li>
                        <li><a href="/#faq">Preguntas frecuentes</a></li>
                        <li><a href="/#contacto">Cotizar</a></li>
                        <li><a href="/aviso-de-privacidad.html">Aviso de privacidad</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h2>Contacto</h2>
                    <ul>
                        <li><a href="tel:+526141690797">+52 (614) 169-0797</a></li>
                        <li><a href="mailto:jacobo@afergreens.com">jacobo@afergreens.com</a></li>
                        <li><address>Rancho Valle de Gigantes<br>La Cruz, Municipio de Saucillo<br>Chihuahua, CP 33676, México</address></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2026 <strong>AFER Greens S. de R.L. de C.V.</strong></span>
                <span>Valle de Gigantes · Chihuahua, México</span>
            </div>
        </div>
    </footer>"""


def wa_link(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"


def picture(name, alt, sizes, widths, eager=False, cls=""):
    webp = ", ".join(f"/img/{name}-{w}.webp {w}w" for w in widths)
    jpg = ", ".join(f"/img/{name}-{w}.jpg {w}w" for w in widths)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    src = f"/img/{name}-{widths[-1]}.jpg"
    w, h = Image.open(os.path.join(ROOT, "img", f"{name}-{widths[-1]}.jpg")).size
    return (f'<picture><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
            f'<img src="{src}" srcset="{jpg}" sizes="{sizes}" alt="{html.escape(alt)}" {load} decoding="async" width="{w}" height="{h}"></picture>')


def dl(rows):
    out = []
    for k, v in rows:
        out.append(f'<div class="row"><dt>{k}</dt><dd>{v}</dd></div>')
    return "\n".join(out)


def season_strip(months):
    cells = "".join(f'<span class="{"on" if i in months else ""}"></span>' for i in range(12))
    labels = "".join(f"<span>{m}</span>" for m in MONTHS)
    if not months:
        text = "Temporada por confirmar."
    elif len(months) == 12:
        text = "Disponible todo el año."
    else:
        text = "Disponible: " + ", ".join(MONTHS[i] for i in months) + "."
    return (f'<div class="season" role="img" aria-label="{text}">'
            f'<div class="season-months" aria-hidden="true">{cells}</div>'
            f'<div class="season-labels" aria-hidden="true">{labels}</div></div>')


def schema(slug, p):
    props = [{"@type": "PropertyValue", "name": k, "value": v} for k, v in p["schema_props"]]
    offers = [{"@type": "Offer", "sku": sku, "name": name, "availability": "https://schema.org/InStock",
               "businessFunction": "http://purl.org/goodrelations/v1#Sell",
               "seller": {"@id": f"{SITE}/#organization"}} for sku, name in p["offers"]]
    images = [f"{SITE}/{p['image']}.jpg"] + [f"{SITE}/{pr[2]}.jpg" for pr in p["presentations"]]
    g = {"@context": "https://schema.org", "@graph": [
        {"@type": "Product", "@id": f"{SITE}/{slug}/#product", "name": p["name"], "description": p["description"],
         "url": f"{SITE}/{slug}/", "image": images, "sku": p["sku"], "category": p["category"], "inLanguage": "es-MX",
         "brand": {"@type": "Organization", "name": "AFER Greens", "@id": f"{SITE}/#organization"},
         "manufacturer": {"@type": "Organization", "name": "Valle de Gigantes", "@id": f"{SITE}/#farm"},
         "countryOfOrigin": "MX", "additionalProperty": props, "offers": offers},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Productos", "item": f"{SITE}/#productos"},
            {"@type": "ListItem", "position": 3, "name": p["short"], "item": f"{SITE}/{slug}/"}]}]}
    return json.dumps(g, ensure_ascii=False, indent=2)


def build(slug):
    p = PRODUCTS[slug]
    others = [s for s in ORDER if s != slug]
    meta_html = "".join(f"<div><strong>{v}</strong><span>{l}</span></div>" for v, l in p["meta"])
    meta_html += (f'<a href="{CERT["campo"][1]}" target="_blank" rel="noopener">'
                  f'<strong>Primus GFS</strong><span>Certificado<span class="visually-hidden"> de campo, PDF, abre en ventana nueva</span></span></a>')
    specs_html = dl(p["specs"] + [("Certificación", " · ".join(
        f'<a href="{u}" target="_blank" rel="noopener">Primus GFS {k} #{n}<span class="visually-hidden"> (PDF, abre en ventana nueva)</span></a>' for k, (n, u) in CERT.items()))])
    log_rows = list(p["logistics"])
    log_html = dl(log_rows) + f'<div class="row"><dt>Calendario</dt><dd>{season_strip(p["season"])}</dd></div>'
    pres_html = ""
    for tag, size, img, text, alt in p["presentations"]:
        pres_html += f"""
                <div class="pres-card reveal reveal-d2">
                    <div class="pres-img">{picture(img, alt, "(min-width: 769px) 33vw, 100vw", [480, 960])}</div>
                    <div class="pres-body">
                        <span class="pres-tag">{tag}</span>
                        <div class="pres-size">{size}</div>
                        <p>{text}</p>
                    </div>
                </div>"""
    states_html = "".join(f'<div class="ps-item"><svg class="ic" aria-hidden="true"><use href="#i-check"/></svg><div><strong>{a}</strong> · {b}</div></div>' for a, b in p["states"])
    uses_html = "".join(f"<li>{u}</li>" for u in p["uses"])
    others_html = ""
    for o in others:
        q = PRODUCTS[o]
        others_html += f"""
                <a class="other-card reveal" href="/{o}/">
                    <div class="thumb"><picture><source type="image/webp" srcset="/img/{q['image']}-112.webp 112w, /img/{q['image']}-224.webp 224w" sizes="88px"><img src="/img/{q['image']}-224.jpg" alt="" width="224" height="224" loading="lazy" decoding="async"></picture></div>
                    <div><h3>{q['name']}</h3><p>{q['meta'][0][0]} {q['meta'][0][1]}</p></div>
                </a>"""
    iw, ih = Image.open(os.path.join(ROOT, p["image"] + ".jpg")).size
    hero_widths = [w for w in (480, 960, 1440) if w < iw]
    hero_webp = ", ".join(f"/img/{p['image']}-{w}.webp {w}w" for w in hero_widths) + f", /{p['image']}.webp {iw}w"
    hero_jpg = ", ".join(f"/img/{p['image']}-{w}.jpg {w}w" for w in hero_widths) + f", /{p['image']}.jpg {iw}w"
    hero_pic = (f'<picture><source type="image/webp" srcset="{hero_webp}" sizes="(min-width: 1025px) 45vw, 100vw">'
                f'<img src="/{p["image"]}.jpg" srcset="{hero_jpg}" sizes="(min-width: 1025px) 45vw, 100vw" alt="{html.escape(p["image_alt"])}" fetchpriority="high" decoding="async" width="{iw}" height="{ih}"></picture>')
    wa = wa_link(p["wa_msg"])

    return f"""<!DOCTYPE html>
<html lang="es-MX">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="author" content="AFER Greens S. de R.L. de C.V.">
    <meta name="description" content="{html.escape(p['description'])}">
    <link rel="canonical" href="{SITE}/{slug}/">
    <link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
    <link rel="icon" type="image/png" sizes="64x64" href="/favicon-64.png">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <meta name="theme-color" content="#042E28">

    <title>{html.escape(p['title'])}</title>

    <meta property="og:type" content="product">
    <meta property="og:site_name" content="AFER Greens">
    <meta property="og:title" content="{html.escape(p['title'])}">
    <meta property="og:description" content="{html.escape(p['description'])}">
    <meta property="og:url" content="{SITE}/{slug}/">
    <meta property="og:locale" content="es_MX">
    <meta property="og:image" content="{SITE}/img/og-{slug}.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="{html.escape(p['image_alt'])}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html.escape(p['title'])}">
    <meta name="twitter:description" content="{html.escape(p['description'])}">
    <meta name="twitter:image" content="{SITE}/img/og-{slug}.jpg">

    <link rel="preload" href="/assets/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/assets/fonts/outfit-300.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="/assets/site.css">

    <script type="application/ld+json">
{schema(slug, p)}
    </script>
</head>
<body>
    <a class="skip-link" href="#contenido">Saltar al contenido</a>
{ICONS}
    <div id="cursor" aria-hidden="true"></div>
    <div id="cursor-ring" aria-hidden="true"></div>

{HEADER}

    <main id="contenido">

    <nav class="breadcrumb" aria-label="Ruta de navegación">
        <div class="bc-inner">
            <a href="/">Inicio</a><span class="sep" aria-hidden="true">&rsaquo;</span>
            <a href="/#productos">Productos</a><span class="sep" aria-hidden="true">&rsaquo;</span>
            <span aria-current="page">{p['short']}</span>
        </div>
    </nav>

    <section class="product-hero">
        <div class="ph-inner">
            <div class="ph-content">
                <span class="section-label">{p['eyebrow']}</span>
                <h1>{p['h1']}</h1>
                <p class="ph-sub">{p['sub']}</p>
                <div class="ph-meta">{meta_html}</div>
                <div class="ph-actions">
                    <a href="/?producto={quote(p['name'])}#contacto" class="btn-primary">Solicitar cotización</a>
                    <a class="hero-wa" href="{wa}" target="_blank" rel="noopener"><svg class="ic" aria-hidden="true"><use href="#i-wa"/></svg>WhatsApp<span class="visually-hidden"> (abre en ventana nueva)</span></a>
                </div>
            </div>
            <div class="ph-visual">{hero_pic}</div>
        </div>
    </section>

    <section class="section-pad specs" id="ficha">
        <div class="specs-inner">
            <span class="section-label reveal">Ficha técnica</span>
            <h2 class="section-title reveal reveal-d1">Datos del <em>producto</em>.</h2>
            <div class="spec-grid">
                <div class="spec-list reveal reveal-d2">
                    <h3>Características</h3>
                    <dl>
{specs_html}
                    </dl>
                </div>
                <div class="spec-list reveal reveal-d3">
                    <h3>Logística y disponibilidad</h3>
                    <dl>
{log_html}
                    </dl>
                </div>
            </div>
            <p class="spec-note reveal reveal-d3">Los datos marcados <span class="pending">por confirmar</span> se completan con el productor y se confirman en cada cotización. Esta página se puede imprimir como ficha técnica.</p>
        </div>
    </section>

    <section class="section-pad presentations light" id="presentaciones">
        <div class="pres-inner">
            <span class="section-label reveal">Presentaciones</span>
            <h2 class="section-title reveal reveal-d1">{p['pres_title']}</h2>
            <p class="section-intro reveal reveal-d2">{p['pres_intro']}</p>
            <div class="pres-grid">{pres_html}
            </div>
            <div class="pres-states reveal">{states_html}</div>
        </div>
    </section>

    <section class="section-pad uses" id="usos">
        <div class="uses-inner">
            <span class="section-label reveal">Aplicaciones</span>
            <h2 class="section-title reveal reveal-d1">{p['uses_title']}</h2>
            <p class="section-intro reveal reveal-d2">{p['uses_intro']}</p>
            <ul class="uses-tags reveal reveal-d2">{uses_html}</ul>
        </div>
    </section>

    <section class="section-pad others">
        <div class="others-inner">
            <span class="section-label reveal">Otros productos</span>
            <h2 class="section-title reveal reveal-d1">Del mismo <em>valle</em>.</h2>
            <div class="others-grid">{others_html}
            </div>
        </div>
    </section>

    <section class="section-pad cta-band">
        <div class="cta-inner">
            <h2 class="section-title reveal">¿Listo para <em>cotizar</em>?</h2>
            <p class="reveal reveal-d1">{p['cta']}</p>
            <div class="actions reveal reveal-d2">
                <a href="/?producto={quote(p['name'])}#contacto" class="btn-primary">Solicitar cotización</a>
                <a class="btn-ghost" href="{wa}" target="_blank" rel="noopener">WhatsApp<span class="visually-hidden"> (abre en ventana nueva)</span></a>
            </div>
        </div>
    </section>

    </main>

{FOOTER}

    <a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp (abre en ventana nueva)">
        <svg class="ic" aria-hidden="true"><use href="#i-wa"/></svg>
    </a>

    <script src="/assets/site.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    for slug in ORDER:
        path = os.path.join(ROOT, slug, "index.html")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(build(slug))
        print("wrote", path, sum(1 for _ in open(path, encoding="utf-8")), "lines")
