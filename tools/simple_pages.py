# -*- coding: utf-8 -*-
"""Build 404.html, gracias.html and aviso-de-privacidad.html with the shared chrome.

    python tools/simple_pages.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_products import ROOT, SITE, ICONS, HEADER, FOOTER  # noqa: E402

PAGES = {
    "404.html": {
        "title": "Página no encontrada | AFER Greens",
        "robots": "noindex",
        "body": """
        <span class="section-label">Error 404</span>
        <h1>Esta página no <em>existe</em>.</h1>
        <p>El enlace puede estar incompleto o haber cambiado. Los productos y la cotización siguen aquí:</p>
        <ul>
            <li><a href="/melon/">Melón dulce del desierto</a></li>
            <li><a href="/chiltepin/">Chile chiltepín</a></li>
            <li><a href="/jalapeno/">Jalapeño fresco</a></li>
            <li><a href="/chipotle/">Chipotle ahumado con mezquite</a></li>
        </ul>
        <div class="actions">
            <a href="/#contacto" class="btn-primary">Solicitar cotización</a>
            <a href="/" class="btn-ghost">Ir al inicio</a>
        </div>""",
    },
    "gracias.html": {
        "title": "Solicitud enviada | AFER Greens",
        "robots": "noindex",
        "body": """
        <span class="section-label">Cotización</span>
        <h1>Solicitud <em>enviada</em>.</h1>
        <p>Gracias. Respondemos en un día hábil con mínimo, empaque por tarima y condiciones para su destino.</p>
        <p>Si prefiere, escríbanos directo por <a href="https://wa.me/526141690797" target="_blank" rel="noopener">WhatsApp</a> o a <a href="mailto:jacobo@afergreens.com">jacobo@afergreens.com</a>.</p>
        <div class="actions">
            <a href="/" class="btn-ghost">Volver al inicio</a>
        </div>""",
    },
    "aviso-de-privacidad.html": {
        "title": "Aviso de privacidad | AFER Greens",
        "robots": "index, follow",
        "body": """
        <span class="section-label">Legal</span>
        <h1>Aviso de <em>privacidad</em>.</h1>
        <p><strong>AFER Greens S. de R.L. de C.V.</strong>, con domicilio en Rancho Valle de Gigantes, La Cruz, Municipio de Saucillo, Chihuahua, CP 33676, México, es responsable del tratamiento de los datos personales que usted proporciona a través del formulario de cotización y los canales de contacto de este sitio, conforme a la Ley Federal de Protección de Datos Personales en Posesión de los Particulares.</p>
        <h2>Datos que recabamos</h2>
        <p>Nombre de la empresa, correo electrónico y, de manera opcional, teléfono, volumen estimado y el mensaje que usted redacte.</p>
        <h2>Finalidad</h2>
        <p>Responder a su solicitud de cotización, dar seguimiento comercial a esa solicitud y, en su caso, formalizar una relación de compraventa. No usamos sus datos para fines distintos ni los transferimos a terceros, salvo obligación legal.</p>
        <h2>Conservación y seguridad</h2>
        <p>Los datos se conservan mientras exista una relación comercial o una solicitud activa. Se almacenan en el correo electrónico de ventas de la empresa con acceso restringido.</p>
        <h2>Derechos ARCO</h2>
        <p>Usted puede solicitar el acceso, rectificación, cancelación u oposición al tratamiento de sus datos escribiendo a <a href="mailto:jacobo@afergreens.com">jacobo@afergreens.com</a>. Responderemos en un plazo máximo de 20 días hábiles.</p>
        <h2>Cambios a este aviso</h2>
        <p>Cualquier modificación se publicará en esta misma página. Última actualización: 11 de septiembre de 2026.</p>""",
    },
}

TEMPLATE = """<!DOCTYPE html>
<html lang="es-MX">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="{robots}">
    <title>{title}</title>
    <link rel="canonical" href="{SITE}/{file}">
    <link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
    <link rel="icon" type="image/png" sizes="64x64" href="/favicon-64.png">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <meta name="theme-color" content="#042E28">
    <link rel="stylesheet" href="/assets/site.css">
</head>
<body>
    <a class="skip-link" href="#contenido">Saltar al contenido</a>
{ICONS}
    <div id="cursor" aria-hidden="true"></div>
    <div id="cursor-ring" aria-hidden="true"></div>

{HEADER}

    <main id="contenido" class="page-simple">{body}
    </main>

{FOOTER}

    <script src="/assets/site.js" defer></script>
</body>
</html>
"""

if __name__ == "__main__":
    for file, p in PAGES.items():
        out = TEMPLATE.format(SITE=SITE, file=file, ICONS=ICONS, HEADER=HEADER, FOOTER=FOOTER, **p)
        with open(os.path.join(ROOT, file), "w", encoding="utf-8", newline="\n") as f:
            f.write(out)
        print("wrote", file)
