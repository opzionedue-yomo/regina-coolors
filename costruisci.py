# -*- coding: utf-8 -*-
"""
Costruisce il sito statico di Regina Coolors dentro la cartella sito/.
Uso:  python3 costruisci.py
"""
import os, re, html, calendar, datetime
import contenuti as C

QUI = os.path.dirname(os.path.abspath(__file__))
V = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # marca anti-cache
OUT = os.path.join(QUI, "sito")
A = C.AZIENDA

# ------------------------------------------------------------------- ICONE SVG
_L = 'fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"'
ICONE = {
 "cuore": f'<path {_L} d="M12 20.5S3.5 15.4 3.5 9.7A4.2 4.2 0 0 1 12 7.6a4.2 4.2 0 0 1 8.5 2.1c0 5.7-8.5 10.8-8.5 10.8Z"/>',
 "gruppo": f'<circle cx="9" cy="8" r="3.2" {_L}/><path {_L} d="M2.8 20c.4-3.3 3-5.4 6.2-5.4S14.8 16.7 15.2 20"/><circle cx="17" cy="9.5" r="2.4" {_L}/><path {_L} d="M16.4 14.8c2.4.3 4.3 2.2 4.6 5.2"/>',
 "stella": f'<path {_L} d="m12 3.6 2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8L3.5 9.8l5.9-.9Z"/>',
 "smile": f'<circle cx="12" cy="12" r="9" {_L}/><path {_L} d="M8.5 14c1 1.3 2.2 2 3.5 2s2.5-.7 3.5-2"/><path {_L} d="M9 9.5h.01M15 9.5h.01"/>',
 "tufting": f'<circle cx="12" cy="12" r="8.6" {_L}/><path {_L} d="M5.2 7.4c3.5 1.9 7.6 1.3 10.8-1.7M3.6 13.4c4.9 1 9.6-1.4 12.2-6M6.2 18.2C11 17.6 15.9 13.7 17.6 8.2M11.2 20.4c3.5-1 6.9-4 8.7-7.6"/>',
 "ricamo": f'<circle cx="10.5" cy="12.5" r="7.3" {_L}/><circle cx="10.5" cy="12.5" r="5.2" {_L}/><path {_L} d="m16.4 7.6 4.5-4.5M19 3.4l1.8 1.8"/>',
 "patch": f'<path {_L} d="M6.4 4.6h11.2c1 0 1.8.8 1.8 1.8v11.2c0 1-.8 1.8-1.8 1.8H6.4c-1 0-1.8-.8-1.8-1.8V6.4c0-1 .8-1.8 1.8-1.8Z" stroke-dasharray="3 2.4"/><path {_L} d="m12 8.4 1.4 2.9 3.2.5-2.3 2.2.6 3.2-2.9-1.5-2.9 1.5.6-3.2-2.3-2.2 3.2-.5Z"/>',
 "fiore": f'<circle cx="12" cy="12" r="2.5" {_L}/><ellipse cx="12" cy="6.4" rx="2.9" ry="3.4" {_L}/><ellipse cx="17.6" cy="12" rx="3.4" ry="2.9" {_L}/><ellipse cx="12" cy="17.6" rx="2.9" ry="3.4" {_L}/><ellipse cx="6.4" cy="12" rx="3.4" ry="2.9" {_L}/>',
 "ago": f'<path {_L} d="M20.5 3.5 9.8 14.2M18.4 3.9a1.9 1.9 0 0 1 1.7 1.7M9.8 14.2l-2.3 4.6-4.6 2.3 2.3-4.6Z"/><circle cx="17.6" cy="6.4" r="1.4" {_L}/>',
 "penna": f'<path {_L} d="M4 20.2c5.5-1.4 9.4-5.6 11.1-9.4M14.2 3.6l6.2 6.2-4.7 4.7-6.2-6.2Z"/><path {_L} d="m8 9.4-3.4 6.9L11.5 13"/>',
 "foto": f'<rect x="3" y="5" width="18" height="14" rx="2.4" {_L}/><path {_L} d="m6 15.5 3.4-3.6 2.6 2.4 3-3.4L18 15"/><circle cx="8.6" cy="9" r="1.3" {_L}/>',
 "biglietto": f'<rect x="3" y="5.5" width="18" height="13" rx="2.2" {_L}/><path {_L} d="m3.6 7 8.4 6 8.4-6"/>',
 "corona": f'<path {_L} d="M3.5 17.5h17M4 7.5l3.6 3.2L12 5l4.4 5.7L20 7.5l-1.4 8H5.4Z"/>',
 "festa": f'<path {_L} d="m3.5 20.5 5.2-12.8 7.6 7.6Z"/><path {_L} d="M14 3.2v2M18.8 4.4l-1.3 1.5M20.6 9.2h-2M16.2 8.6a3.3 3.3 0 0 1 3.2 3.4"/>',
 "palette": f'<path {_L} d="M12 3.2a8.8 8.8 0 0 0 0 17.6c1.3 0 1.9-.9 1.9-1.8 0-1.5-1.2-1.8-1.2-2.9 0-.8.7-1.4 1.6-1.4h1.6a4.9 4.9 0 0 0 4.9-4.9c0-3.6-3.7-6.6-8.8-6.6Z"/><path {_L} d="M7.4 10.4h.01M10 7.2h.01M14.4 7.4h.01M17 10.6h.01"/>',
 "sabato": f'<circle cx="12" cy="12" r="4.2" {_L}/><path {_L} d="M12 2.8v2.2M12 19v2.2M4.5 4.5 6 6M18 18l1.5 1.5M2.8 12H5M19 12h2.2M4.5 19.5 6 18M18 6l1.5-1.5"/>',
 "pausa": f'<path {_L} d="M4 9h12v5.5a4.5 4.5 0 0 1-4.5 4.5h-3A4.5 4.5 0 0 1 4 14.5Z"/><path {_L} d="M16 10.5h1.8a2.4 2.4 0 0 1 0 4.8H16M7.5 5.5c-.6-1 .3-1.7 0-2.6M11.5 5.5c-.6-1 .3-1.7 0-2.6"/>',
 "tappeto": f'<rect x="3.2" y="6" width="17.6" height="12" rx="1.6" {_L}/><path {_L} d="M3.2 10c3.5 2.2 6.5-2.2 9.4 0s5.5-1.4 8.2.4M3.2 14.4c3.5 2.2 6.5-2.2 9.4 0s5.5-1.4 8.2.4M5.4 18v2M9 18v2M15 18v2M18.6 18v2"/>',
 "regalo": f'<rect x="3.2" y="8.4" width="17.6" height="4" rx="1.2" {_L}/><path {_L} d="M4.8 12.4h14.4v7.2a1.2 1.2 0 0 1-1.2 1.2H6a1.2 1.2 0 0 1-1.2-1.2ZM12 8.4v12.4"/><path {_L} d="M12 8.4S10.6 3 8.2 3.6C6.2 4.2 6.6 8.4 12 8.4Zm0 0S13.4 3 15.8 3.6C17.8 4.2 17.4 8.4 12 8.4Z"/>',
 "domanda": f'<circle cx="12" cy="12" r="9" {_L}/><path {_L} d="M9.5 9.4a2.6 2.6 0 0 1 5 .9c0 1.7-2.5 2.2-2.5 3.8M12 17.2h.01"/>',
 "documento": f'<path {_L} d="M6 3h8l4.5 4.5V21H6Z"/><path {_L} d="M14 3v5h4.5M9 12.5h6M9 16h6"/>',
 "telefono": f'<path {_L} d="M6.5 3.5h3l1.6 4-2 1.4a11.5 11.5 0 0 0 5.4 5.4l1.4-2 4 1.6v3a2 2 0 0 1-2.2 2C11.4 18.4 5.6 12.6 4.5 5.7a2 2 0 0 1 2-2.2Z"/>',
 "calendario": f'<rect x="3.2" y="5" width="17.6" height="16" rx="2.4" {_L}/><path {_L} d="M3.2 10h17.6M8 3v4M16 3v4"/><path {_L} d="M7.6 14h.01M12 14h.01M16.4 14h.01M7.6 17.6h.01M12 17.6h.01"/>',
 "workshop": f'<circle cx="6.2" cy="6.4" r="2.6" {_L}/><circle cx="6.2" cy="17.6" r="2.6" {_L}/><path {_L} d="M8.4 7.8 20 18.4M8.4 16.2 20 5.6"/>',
 "mappa": f'<path {_L} d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6" {_L}/>',
 "mail": f'<rect x="3" y="5.5" width="18" height="13" rx="2.2" {_L}/><path {_L} d="m3.6 7 8.4 6 8.4-6"/>',
 "menu": f'<path {_L} d="M4 7h16M4 12h16M4 17h16"/>',
 "chiudi": f'<path {_L} d="M6 6l12 12M18 6 6 18"/>',
 "whatsapp": '<path fill="currentColor" d="M12.04 2C6.6 2 2.2 6.4 2.2 11.84c0 1.74.46 3.44 1.32 4.94L2 22l5.36-1.4a9.8 9.8 0 0 0 4.68 1.2h.01c5.43 0 9.84-4.4 9.84-9.84 0-2.63-1.02-5.1-2.88-6.96A9.78 9.78 0 0 0 12.04 2Zm0 1.8a8 8 0 0 1 5.68 2.36 7.96 7.96 0 0 1 2.36 5.68c0 4.44-3.6 8.04-8.05 8.04a8.1 8.1 0 0 1-4.1-1.12l-.3-.18-3.05.8.82-2.98-.2-.3a8 8 0 0 1-1.24-4.26c0-4.44 3.62-8.04 8.08-8.04Zm-3.3 4.1c-.16 0-.42.06-.64.3-.22.24-.85.83-.85 2.02 0 1.2.87 2.35.99 2.51.12.16 1.7 2.72 4.2 3.7 2.07.82 2.5.66 2.95.62.45-.04 1.44-.59 1.65-1.16.2-.57.2-1.05.14-1.16-.06-.1-.22-.16-.46-.28-.24-.12-1.44-.71-1.66-.79-.22-.08-.38-.12-.55.12-.16.24-.62.79-.76.95-.14.16-.28.18-.52.06-.24-.12-1.03-.38-1.96-1.21-.72-.65-1.21-1.45-1.35-1.69-.14-.24-.02-.37.1-.49.11-.11.24-.28.36-.42.12-.14.16-.24.24-.4.08-.16.04-.3-.02-.42-.06-.12-.54-1.32-.75-1.8-.18-.44-.37-.38-.51-.39h-.44Z"/>',
 "instagram": '<path fill="currentColor" d="M8 2.2h8A5.8 5.8 0 0 1 21.8 8v8A5.8 5.8 0 0 1 16 21.8H8A5.8 5.8 0 0 1 2.2 16V8A5.8 5.8 0 0 1 8 2.2Zm0 1.9A3.9 3.9 0 0 0 4.1 8v8A3.9 3.9 0 0 0 8 19.9h8a3.9 3.9 0 0 0 3.9-3.9V8A3.9 3.9 0 0 0 16 4.1Zm9.1 1.5a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4ZM12 6.9a5.1 5.1 0 1 1 0 10.2 5.1 5.1 0 0 1 0-10.2Zm0 1.9a3.2 3.2 0 1 0 0 6.4 3.2 3.2 0 0 0 0-6.4Z"/>',
 "freccia": f'<path {_L} d="M4 12h15M13 6l6 6-6 6"/>',
}
def icona(nome, cls="", vb=24):
    corpo = ICONE.get(nome, ICONE["stella"])
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 {vb} {vb}" aria-hidden="true" width="24" height="24">{corpo}</svg>'

# ------------------------------------------------------------------ UTILITÀ
WA = f'https://wa.me/{A["telefono_intl"]}'
TEL = 'tel:+' + A["telefono_intl"]
MESI = ["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio",
        "agosto","settembre","ottobre","novembre","dicembre"]
MESI_BREVI = ["GEN","FEB","MAR","APR","MAG","GIU","LUG","AGO","SET","OTT","NOV","DIC"]
GIORNI = ["L","M","M","G","V","S","D"]

def risolvi(href):
    return {"WHATSAPP": WA, "TELEFONO": TEL, "MAPPA": A["mappa"],
            "INSTAGRAM": A["instagram_url"], "EMAIL": "mailto:" + A["email"]}.get(href, href)

def esterno(href):
    return href.startswith("http") or href.startswith("tel:") or href.startswith("mailto:")

def inline(t):
    """**grassetto**, [testo](destinazione) e i segnaposto WHATSAPP/TELEFONO/..."""
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    def _a(m):
        testo, href = m.group(1), risolvi(m.group(2))
        extra = ' target="_blank" rel="noopener"' if esterno(href) else ""
        return f'<a href="{href}"{extra}>{testo}</a>'
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _a, t)

# ------------------------------------------------------------------- IL GUSCIO
def logo(dove=""):
    cls = "logo" + (f" logo--{dove}" if dove else "")
    return (f'<a class="{cls}" href="index.html" aria-label="Regina Coolors, home">'
            f'<img src="assets/img/logo.png?v={{V}}" alt="Regina Coolors" width="560" height="611"></a>')

def testata(attiva):
    voci = []
    for etichetta, href, figli in C.NAV:
        cls = "nav__voce"
        if figli: cls += " ha-figli"
        if href == attiva or any(f[1] == attiva for f in figli): cls += " nav__voce--attiva"
        tend = ""
        if figli:
            righe = "".join(f'<a href="{f[1]}">{f[0]}</a>' for f in figli)
            tend = f'<div class="tendina">{righe}</div>'
        voci.append(f'<div class="{cls}"><a href="{href}">{etichetta}</a>{tend}</div>')
    return f'''<div class="strillo"><span>{(A["strillo"] + " · ") * 4}</span></div>
<header class="testata">
  <div class="contenitore testata__riga">
    {logo()}
    <nav class="nav" aria-label="Menu principale">{"".join(voci)}</nav>
    <div class="azioni">
      <a class="tondo tondo--ig" href="{A["instagram_url"]}" target="_blank" rel="noopener" aria-label="Instagram">{icona("instagram")}</a>
      <a class="tondo tondo--wa" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{icona("whatsapp")}</a>
      <a class="bottone bottone--rosa bottone--mini" href="contatti.html">Prenota</a>
      <button class="apri-menu" aria-expanded="false" aria-controls="menu-mobile" aria-label="Apri il menu">{icona("menu")}</button>
    </div>
  </div>
</header>
{menu_mobile()}'''

def menu_mobile():
    voci = []
    for etichetta, href, figli in C.NAV:
        if figli:
            righe = "".join(f'<a href="{f[1]}">{f[0]}</a>' for f in figli)
            voci.append(f'<details><summary>{etichetta}</summary><div class="menu-mobile__figli">'
                        f'<a href="{href}"><b>Tutto su {etichetta.lower()}</b></a>{righe}</div></details>')
        else:
            voci.append(f'<a class="voce-piatta" href="{href}">{etichetta}</a>')
    return f'''<div class="menu-mobile" id="menu-mobile">
  <div class="contenitore">
    <div class="menu-mobile__testa">{logo("menu")}
      <button class="apri-menu chiudi-menu" aria-label="Chiudi il menu">{icona("chiudi")}</button></div>
    {"".join(voci)}
    <div class="bottoni"><a class="bottone bottone--rosa" href="{WA}" target="_blank" rel="noopener">Scrivimi su WhatsApp</a></div>
    <p style="font-size:.85rem;color:var(--grigio)">{A["indirizzo"]}<br>{A["telefono"]}</p>
  </div>
</div>'''

def pre_piede():
    return f'''<div class="contenitore"><section class="pre-piede appari">
  <h2>Vieni a creare qualcosa di tuo</h2>
  <p>Per prenotare basta scrivermi o telefonarmi: rispondo io. I posti sono pochi per scelta, perché accolgo solo piccoli gruppi.</p>
  <div class="bottoni">
    <a class="bottone" href="{WA}" target="_blank" rel="noopener">{icona("whatsapp")} Scrivimi su WhatsApp</a>
    <a class="bottone bottone--ghost" href="{TEL}">{icona("telefono")} {A["telefono"]}</a>
  </div>
</section></div>'''

def piede():
    def col(titolo, voci):
        righe = "".join(f'<li><a href="{risolvi(h)}"{" target=_blank rel=noopener" if esterno(risolvi(h)) else ""}>{t}</a></li>' for t, h in voci)
        return f'<div><h4>{titolo}</h4><ul>{righe}</ul></div>'
    esperienze = [(e[0], e[1]) for e in C.NAV[0][2][:6]]
    utili = [("Calendario", "calendario.html")] + C.PIE
    return f'''<footer class="piede">
  <div class="contenitore">
    <div class="piede__griglia">
      <div>{logo("piede")}
        <p style="margin-top:16px">{A["indirizzo"]}<br>
        <a href="{TEL}">{A["telefono"]}</a> · <a href="mailto:{A["email"]}">{A["email"]}</a><br>
        <a href="{A["instagram_url"]}" target="_blank" rel="noopener">@{A["instagram"]}</a></p>
      </div>
      {col("Esperienze", esperienze)}
      {col("Informazioni", utili)}
    </div>
    <div class="piede__nota">
      <span>© 2026 {A["nome"]} · P.IVA da inserire · Tutti i diritti riservati</span>
      <span>Bozza di lavoro — sito non ancora pubblicato</span>
    </div>
  </div>
</footer>
<nav class="barra-mobile" aria-label="Azioni rapide">
  <ul>
    <li><a href="calendario.html">{icona("calendario")}Calendario</a></li>
    <li><a href="{WA}" target="_blank" rel="noopener">{icona("whatsapp")}WhatsApp</a></li>
    <li><a href="{TEL}">{icona("telefono")}Chiama</a></li>
    <li><a href="{A["mappa"]}" target="_blank" rel="noopener">{icona("mappa")}Mappa</a></li>
  </ul>
</nav>'''

def guscio(nome_file, titolo, descrizione, contenuto, attiva="", tema="rosa", corpo_extra=""):
    doc = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titolo}</title>
<meta name="description" content="{html.escape(descrizione, quote=True)}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{html.escape(titolo, quote=True)}">
<meta property="og:description" content="{html.escape(descrizione, quote=True)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#FF2E9A">
<link rel="icon" href="assets/img/favicon.png?v={V}" type="image/png">
<link rel="apple-touch-icon" href="assets/img/favicon.png?v={V}">
<link rel="stylesheet" href="assets/stile.css?v={V}">
</head>
<body class="tema-{tema}{corpo_extra}">
<span class="macchia macchia--1"></span><span class="macchia macchia--2"></span><span class="macchia macchia--3"></span>
{testata(attiva)}
<main id="contenuto">
{contenuto}
</main>
{pre_piede()}
{piede()}
<script src="assets/sito.js?v={V}"></script>
</body>
</html>'''
    with open(os.path.join(OUT, nome_file), "w", encoding="utf-8") as f:
        f.write(doc)
    return nome_file

# --------------------------------------------------------------- I BLOCCHI
def bottoni(lista):
    fuori = []
    for etichetta, href, stile in lista:
        h = risolvi(href)
        cls = "bottone bottone--rosa" if stile == "primary" else "bottone bottone--ghost"
        extra = ' target="_blank" rel="noopener"' if esterno(h) else ""
        ic = icona("whatsapp") if href == "WHATSAPP" else (icona("telefono") if href == "TELEFONO" else "")
        fuori.append(f'<a class="{cls}" href="{h}"{extra}>{ic}{etichetta}</a>')
    return f'<div class="bottoni appari">{"".join(fuori)}</div>'

def rendi(blocchi, tema="rosa"):
    out = []
    for tipo, dato in blocchi:
        if tipo == "p":
            out.append(f"<p>{inline(dato)}</p>")
        elif tipo == "h":
            out.append(f"<h2 class='appari'>{inline(dato)}</h2>")
        elif tipo == "ul":
            voci = "".join(f"<li>{inline(v)}</li>" for v in dato)
            out.append(f"<ul class='appari'>{voci}</ul>")
        elif tipo == "info":
            righe = "".join(f"<div class='riga'><dt>{k}</dt><dd>{inline(v)}</dd></div>" for k, v in dato)
            out.append(f"<div class='scheda appari'><dl>{righe}</dl></div>")
        elif tipo == "steps":
            passi = "".join(f"<div class='passo'><h3>{inline(t)}</h3><p>{inline(v)}</p></div>" for t, v in dato)
            out.append(f"<div class='passi appari'>{passi}</div>")
        elif tipo == "cta":
            out.append(bottoni(dato))
        elif tipo == "nota":
            out.append(f"<div class='nota appari'>{inline(dato)}</div>")
        elif tipo == "evidenza":
            out.append(f"<div class='evidenza appari'>{inline(dato)}</div>")
        elif tipo == "box":
            out.append(f"<div class='riquadro appari'><b>{inline(dato[0])}</b><p>{inline(dato[1])}</p></div>")
        elif tipo == "prezzi":
            righe = "".join(f"<div><span>{k}</span><span>{v}</span></div>" for k, v in dato)
            out.append(f"<div class='listino appari'>{righe}</div>")
        elif tipo == "faq":
            dd = "".join(f"<details class='domanda'><summary>{inline(d)}</summary>"
                         f"<div class='domanda__r'>{inline(r)}</div></details>" for d, r in dato)
            out.append(f"<div class='domande appari'>{dd}</div>")
        elif tipo == "cards":
            cc = []
            for t, testo, href in dato:
                cc.append(f"<a class='card card--{tema} appari' href='{href}'>"
                          f"<span class='card__pallino'>{icona('freccia')}</span>"
                          f"<h3>{t}</h3><p>{testo}</p>"
                          f"<span class='card__freccia'>Scopri →</span></a>")
            out.append(f"<div class='griglia'>{''.join(cc)}</div>")
        elif tipo == "elenco_lab":
            lista = C.LABORATORI_BAMBINI if dato == "BAMBINI" else C.LABORATORI_ADULTI
            vv = []
            for t, testo, href in lista:
                link = f" <a href='{href}'>Vai alla scheda →</a>" if href else ""
                vv.append(f"<div class='lab__voce appari'><b>{t}</b><p>{inline(testo)}{link}</p></div>")
            out.append(f"<div class='lab'>{''.join(vv)}</div>")
        elif tipo == "hr":
            out.append("<hr>")
        elif tipo == "calendario":
            out.append(calendario_html())
        elif tipo == "modulo":
            out.append(modulo_html())
        elif tipo == "contatti_griglia":
            out.append(contatti_html())
        elif tipo == "mappa":
            out.append(mappa_html())
    return "\n".join(out)

# ------------------------------------------------------------------ CALENDARIO
def eventi_per_giorno():
    d = {}
    for e in C.EVENTI:
        d.setdefault(e["data"], []).append(e)
    return d

def calendario_html():
    per_giorno = eventi_per_giorno()
    mesi = []
    for anno, mese in C.CALENDARIO_MESI:
        celle = []
        for settimana in calendar.Calendar(firstweekday=0).monthdayscalendar(anno, mese):
            riga = []
            for i, g in enumerate(settimana):
                if g == 0:
                    riga.append('<td><span class="giorno giorno--vuoto">0</span></td>')
                    continue
                iso = f"{anno}-{mese:02d}-{g:02d}"
                if iso in per_giorno:
                    titoli = " · ".join(e["titolo"] for e in per_giorno[iso])
                    riga.append(f'<td><span class="giorno giorno--evento" title="{html.escape(titoli, quote=True)}">{g}</span></td>')
                elif i == 5:
                    riga.append(f'<td><span class="giorno giorno--sabato" title="Sabato creativo">{g}</span></td>')
                else:
                    riga.append(f'<td><span class="giorno">{g}</span></td>')
            celle.append("<tr>" + "".join(riga) + "</tr>")
        intest = "".join(f"<th>{g}</th>" for g in GIORNI)
        mesi.append(f'<div class="mese appari"><h3>{MESI[mese-1]} {anno}</h3>'
                    f'<table><thead><tr>{intest}</tr></thead><tbody>{"".join(celle)}</tbody></table></div>')
    legenda = (f'<div class="legenda"><span><i style="background:var(--rosa)"></i>Workshop in programma</span>'
               f'<span><i style="background:var(--salvia-soft);border:2px solid var(--salvia)"></i>Sabato creativo (bambini)</span></div>')
    righe = []
    for e in sorted(C.EVENTI, key=lambda x: x["data"]):
        a, m, g = e["data"].split("-")
        pil = f'<span class="pillola">{e.get("stato","")}</span>' if e.get("stato") else ""
        righe.append(f'<a class="data-riga appari" href="{e["pagina"]}">'
                     f'<span class="data-riga__g"><b>{int(g)}</b><span>{MESI_BREVI[int(m)-1]}</span></span>'
                     f'<span class="data-riga__t"><b>{e["titolo"]}</b>'
                     f'<span>{e.get("ora") or "orario su richiesta"} · {A["indirizzo"]}</span></span>{pil}</a>')
    s = C.SABATO_RICORRENTE
    righe.append(f'<a class="data-riga appari" href="{s["pagina"]}">'
                 f'<span class="data-riga__g" style="background:var(--salvia-velo);color:var(--salvia-scuro)"><b>SAB</b><span>ogni</span></span>'
                 f'<span class="data-riga__t"><b>{s["titolo"]}</b><span>{s["ora"]} · su prenotazione telefonica</span></span>'
                 f'<span class="pillola" style="background:var(--salvia-soft)">tutte le settimane</span></a>')
    return f'<div class="mesi">{"".join(mesi)}</div>{legenda}<div class="date">{"".join(righe)}</div>'

def prossimi(n=3):
    oggi = datetime.date.today().isoformat()
    fut = [e for e in sorted(C.EVENTI, key=lambda x: x["data"]) if e["data"] >= oggi]
    return fut[:n]

# ----------------------------------------------------------- MODULO E CONTATTI
def modulo_html():
    esperienze = ["Tufting", "Punch needle", "Ricamo creativo", "Calligrafia", "Patch bar",
                  "Ricama la tua foto", "Biglietti d’auguri", "Fluffy flowers", "Coroncine di fiori",
                  "Armocromia", "Sabato creativo", "Pausa creativa", "Festa o evento privato",
                  "Tappeto personalizzato", "Gift card", "Non lo so ancora"]
    opzioni = "".join(f'<option>{e}</option>' for e in esperienze)
    return f'''<form class="modulo appari" id="modulo-contatti" data-wa="{A["telefono_intl"]}" data-mail="{A["email"]}" onsubmit="return false">
  <div class="due">
    <div class="campo"><label for="c-nome">Come ti chiami *</label><input id="c-nome" name="nome" required placeholder="Nome e cognome"></div>
    <div class="campo"><label for="c-tel">Telefono</label><input id="c-tel" name="telefono" type="tel" placeholder="Il tuo numero"></div>
  </div>
  <div class="due">
    <div class="campo"><label for="c-mail">E-mail</label><input id="c-mail" name="email" type="email" placeholder="tua@email.it"></div>
    <div class="campo"><label for="c-exp">Cosa ti interessa</label><select id="c-exp" name="esperienza">{opzioni}</select></div>
  </div>
  <div class="due">
    <div class="campo"><label for="c-pers">Quante persone</label><input id="c-pers" name="persone" placeholder="Es. 4"></div>
    <div class="campo"><label for="c-per">Quando, più o meno</label><input id="c-per" name="periodo" placeholder="Es. un sabato di ottobre"></div>
  </div>
  <div class="campo"><label for="c-msg">Scrivimi pure</label><textarea id="c-msg" name="messaggio" placeholder="Raccontami cosa hai in mente"></textarea></div>
  <div class="bottoni" style="margin:4px 0 0">
    <button type="button" class="bottone bottone--rosa" id="invia-whatsapp">{icona("whatsapp")} Mandalo su WhatsApp</button>
    <button type="button" class="bottone bottone--ghost" id="invia-mail">{icona("mail")} Mandalo per e-mail</button>
  </div>
  <p style="font-size:.78rem;color:var(--grigio);margin:0">I dati non vengono salvati da nessuna parte: il pulsante apre WhatsApp o il programma di posta con il messaggio già scritto.</p>
</form>'''

def contatti_html():
    voci = [
        ("telefono", "Chiamami", A["telefono"], TEL),
        ("whatsapp", "Scrivimi su WhatsApp", A["telefono"], WA),
        ("mail", "Mandami una mail", A["email"], "mailto:" + A["email"]),
        ("instagram", "Seguimi su Instagram", "@" + A["instagram"], A["instagram_url"]),
        ("mappa", "Vieni a trovarmi", A["indirizzo"], A["mappa"]),
        ("calendario", "Guarda le date", "Il calendario dei workshop", "calendario.html"),
    ]
    cc = []
    for ic, eti, val, href in voci:
        extra = ' target="_blank" rel="noopener"' if esterno(href) else ""
        cc.append(f'<a class="contatto appari" href="{href}"{extra}>{icona(ic)}<span><b>{eti}</b><span>{val}</span></span></a>')
    return f'<div class="contatti-griglia">{"".join(cc)}</div>'

def mappa_html():
    bbox = "11.3345,44.4825,11.3465,44.4895"
    src = f"https://www.openstreetmap.org/export/embed.html?bbox={bbox}&layer=mapnik&marker=44.4860,11.3405"
    return (f'<div class="mappa-riquadro appari"><iframe src="{src}" loading="lazy" title="Mappa: {A["indirizzo"]}"></iframe></div>'
            f'<div class="bottoni"><a class="bottone bottone--ghost" href="{A["mappa"]}" target="_blank" rel="noopener">{icona("mappa")} Apri in Google Maps</a></div>')

# ------------------------------------------------------------ PAGINE INTERNE
def genitore(slug_file):
    for etichetta, href, figli in C.NAV:
        for f in figli:
            if f[1] == slug_file:
                return etichetta, href
    return None

def pagina_interna(slug, p):
    file_ = slug + ".html"
    g = genitore(file_)
    briciole = '<a href="index.html">Home</a> › '
    if g: briciole += f'<a href="{g[1]}">{g[0]}</a> › '
    briciole += p["titolo"]
    largo = " corpo--largo" if slug in ("calendario", "contatti") else ""
    classe_corpo = " pagina-larga" if largo else ""
    corpo = f'''<section class="testa-pagina">
  <div class="contenitore">
    <p class="briciole">{briciole}</p>
    <div class="testa-pagina__griglia">
      <div>
        <span class="occhiello">{p["occhiello"]}</span>
        <h1>{p["h1"]}</h1>
        <p class="lead">{inline(p["lead"])}</p>
      </div>
      <div class="simbolo-pagina">{icona(p["icona"])}</div>
    </div>
  </div>
</section>
<div class="contenitore"><div class="corpo{largo}">
{rendi(p["blocchi"], p["colore"])}
</div></div>'''
    return guscio(file_, f'{p["titolo"]} · {A["nome"]}', p["seo"], corpo,
                  attiva=file_, tema=p["colore"], corpo_extra=classe_corpo)

# ------------------------------------------------------------------- LA HOME
def home():
    h = C.HOME
    titolo = "".join(h["titolo_grande"])
    testo = "".join(f"<p>{t}</p>" for t in h["sottotitolo"])

    scorc = "".join(
        f'<a class="scorciatoia scorciatoia--{col} appari" href="{href}">'
        f'<img src="assets/{img}?v={V}" alt="" loading="lazy">'
        f'<span class="scorciatoia__testo"><b>{t}</b><span>{sub}</span></span></a>'
        for t, sub, href, img, col in h["scorciatoie"])

    app = "".join(
        f'<a class="app" href="{e["pagina"]}"><span class="app__data">'
        f'<b>{int(e["data"].split("-")[2])}</b><span>{MESI_BREVI[int(e["data"].split("-")[1])-1]}</span></span>'
        f'<span class="app__nome">{e.get("breve") or e["titolo"]}<em>{e.get("stato","")}</em></span></a>'
        for e in prossimi(3))

    piastr = "".join(
        f'<a class="piastrella piastrella--{col} appari" href="{href}">{icona(ic)}'
        f'<span>Tutti impazziscono per</span><b>{t}</b></a>'
        for t, href, col, ic in h["impazziscono"])

    valori = "".join(
        f'<div class="valore">{icona(ic)}<div><b>{t}</b><span>{s}</span></div></div>'
        for ic, t, s in h["valori"])

    pillole = "".join(
        f'<a class="bottone bottone--ghost bottone--mini" href="{f[1]}">{f[0]}</a>'
        for f in C.NAV[0][2])

    corpo = f'''<section class="hero">
  <div class="contenitore hero__griglia">
    <div>
      <h1>{titolo}</h1>
      <div class="hero__testo">{testo}</div>
      <div class="bottoni">
        <a class="bottone bottone--rosa" href="corsi.html">Scopri i corsi</a>
        <a class="bottone bottone--ghost" href="calendario.html">Vedi il calendario</a>
      </div>
    </div>
    <div class="hero__foto appari">
      <img src="assets/img/lab-concept.jpg?v={V}" alt="Lo spazio Regina Coolors in via San Mamolo a Bologna" width="1305" height="1018">
      <div class="bollo">RALLENTA · IMPARA<br>CONDIVIDI</div>
    </div>
  </div>
</section>

<section class="sezione sezione--stretta">
  <div class="contenitore"><div class="scorciatoie">{scorc}</div></div>
</section>

<section class="sezione--stretta">
  <div class="contenitore"><div class="appuntamenti appari">
    <span class="appuntamenti__eti">{icona("calendario")} Prossimi appuntamenti</span>
    <div class="appuntamenti__lista">{app}</div>
    <a class="bottone bottone--mini" href="calendario.html" style="background:#fff;color:var(--inchiostro);border-color:#fff">Vedi tutti</a>
  </div></div>
</section>

<section class="sezione">
  <div class="contenitore">
    <div class="titolo-sezione"><h2>Le esperienze più amate</h2>
      <a class="bottone bottone--ghost bottone--mini" href="corsi.html">Tutti i corsi e i workshop</a></div>
    <div class="piastrelle">{piastr}</div>
    <div class="bottoni" style="gap:8px">{pillole}</div>
  </div>
</section>

<section class="sezione--stretta">
  <div class="contenitore"><div class="valori appari">{valori}</div></div>
</section>

<section class="sezione">
  <div class="contenitore">
    <div class="griglia">
      <a class="card card--rosa appari" href="chi-sono.html">
        <span class="card__pallino">{icona("cuore")}</span><h3>Chi sono</h3>
        <p>Ciao, sono Regina: una mamma millennial cresciuta a dolcetti e creatività. Ho lasciato la toga per il filo e ho aperto il mio lab in via San Mamolo.</p>
        <span class="card__freccia">La mia storia →</span></a>
      <a class="card card--viola appari" href="eventi-privati.html">
        <span class="card__pallino">{icona("festa")}</span><h3>Feste ed eventi privati</h3>
        <p>60 mq tutti per voi, fino a 12 persone: compleanni, team building, addii al nubilato e feste creative su misura.</p>
        <span class="card__freccia">Organizziamo →</span></a>
      <a class="card card--giallo appari" href="gift-card.html">
        <span class="card__pallino">{icona("regalo")}</span><h3>Gift card</h3>
        <p>Non il solito regalo: regali tempo di qualità e creatività. Cartacea o digitale, valida un anno, non finisce in un cassetto.</p>
        <span class="card__freccia">Regala un’esperienza →</span></a>
    </div>
  </div>
</section>

<section class="sezione--stretta">
  <div class="contenitore">
    <div class="evidenza appari" style="font-size:1.2rem">
      Non serve “essere creativi”, avere manualità o saper già fare qualcosa:
      si viene per provare, staccare, svagarsi e sorprendersi. Qui semplicemente si crea!
    </div>
  </div>
</section>'''
    return guscio("index.html", f'{A["nome"]} · Laboratorio creativo a Bologna',
                  "Regina Coolors, lab creativo in via San Mamolo 39C a Bologna: tufting, ricamo, punch needle, patch bar, armocromia, feste ed eventi privati.",
                  corpo, attiva="index.html", tema="rosa")

# ---------------------------------------------------------------------- MAIN
FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
<rect width="24" height="24" rx="5" fill="#FF2E9A"/>
<path d="M4 17.5h16M4.6 7l3.8 3.4L12 5.2l3.6 5.2L19.4 7l-1.5 8.5H6.1Z" fill="none" stroke="#FFDE3D" stroke-width="1.8" stroke-linejoin="round"/></svg>'''

def main():
    os.makedirs(os.path.join(OUT, "assets", "img"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "img", "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON)
    fatti = [home()]
    for slug, p in C.PAGINE.items():
        fatti.append(pagina_interna(slug, p))
    print(f"✅ {len(fatti)} pagine generate in {OUT}")
    for n in sorted(fatti):
        print("   ·", n)

if __name__ == "__main__":
    main()
