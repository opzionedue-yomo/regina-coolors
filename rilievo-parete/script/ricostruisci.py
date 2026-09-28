"""Rilievo della campata tipo: raddrizza la foto e genera maschere, schemi e misure.

Uso:  python3 rilievo-parete/script/ricostruisci.py
Serve: numpy, opencv-python-headless, pillow

Tutti i numeri "misurati" qui sotto vengono dalla foto raddrizzata (pixel della
vista frontale); il modello pulito è espresso in unità con larghezza modulo = 1000
(nei documenti si usa 100: basta dividere per 10).
"""
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent.parent
FOTO = BASE / 'foto'
MASC = BASE / 'maschere'
SCHEMI = BASE / 'schemi'
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

# ---------------------------------------------------------------------------
# 1. Raddrizzamento (rotazione della camera verso la normale alla parete)
# ---------------------------------------------------------------------------
F_PX = 1150.0                  # focale stimata (telefono ~24-26 mm equiv. su 1200x1600)
VP_ORIZ = (15000.0, 843.0)     # punto di fuga delle orizzontali della parete (foto originale)
DIR_VERT = (-0.0025, 1.0)      # direzione delle verticali (punto di fuga all'infinito)


def omografia(w, h):
    K = np.array([[F_PX, 0, w / 2], [0, F_PX, h / 2], [0, 0, 1]])
    Ki = np.linalg.inv(K)
    d1 = Ki @ np.array([*VP_ORIZ, 1.0]); d1 /= np.linalg.norm(d1)
    d2 = Ki @ np.array([*DIR_VERT, 0.0]); d2 /= np.linalg.norm(d2)
    d2 -= d1 * (d1 @ d2); d2 /= np.linalg.norm(d2)
    d3 = np.cross(d1, d2)
    R = np.column_stack([d1, d2, d3])
    Hr = K @ R.T @ Ki
    ang = np.array([[0, 480], [w, 480], [w, 1000], [0, 1000]], float)
    p = np.c_[ang, np.ones(4)] @ Hr.T; p = p[:, :2] / p[:, 2:]
    xmin, ymin = p.min(0); xmax, ymax = p.max(0)
    T = np.array([[1, 0, -xmin + 10], [0, 1, -ymin + 10], [0, 0, 1]])
    H = T @ Hr
    pp = H @ (K @ d3); pp = pp[:2] / pp[2]          # punto principale della vista frontale
    info = dict(imbardata_gradi=float(np.degrees(np.arcsin(-d1[2]))),
                rollio_gradi=float(np.degrees(np.arctan2(d1[1], d1[0]))),
                punto_principale_raddrizzata=[round(float(v), 1) for v in pp])
    return H, (int(xmax - xmin + 20), int(ymax - ymin + 20)), info


src = cv2.imread(str(FOTO / '00-originale.jpg'))
H, size, info_camera = omografia(src.shape[1], src.shape[0])
radd = cv2.warpPerspective(src, H, size, flags=cv2.INTER_CUBIC)
cv2.imwrite(str(FOTO / '03-parete-raddrizzata.jpg'), radd, [cv2.IMWRITE_JPEG_QUALITY, 92])

# ---------------------------------------------------------------------------
# 2. Misure sulla foto raddrizzata (pixel) e modello pulito (unità, modulo = 1000)
# ---------------------------------------------------------------------------
X8, Y0, PASSO_COL, PX = 293, 79, 356, 427 / 1000   # origine campata 8, px per unità

W, C = 1000, 166                  # modulo, colonna
YT, YB, YH = 876, 963, 1005       # alto fascia, fondo fascia, fondo dente
HT, HF = 150, 35                  # mezza larghezza dente in alto / parte piatta
AP = (179, 55, 821, 365)          # apertura col telo (approssimata): x0, y0, x1, y1

# profondità stimate davanti alla parete arretrata (unità, modulo = 1000)
PROF = dict(parete=0, colonne=65, fascia=110)
PROF_RANGE = dict(colonne=(50, 90), fascia=(80, 140))


def dente_y(x, xc):
    d = abs(x - xc)
    if d <= HF: return YH
    if d >= HT: return YB
    return YH - (YH - YB) * (d - HF) / (HT - HF)


c1, c2 = C / 2, W - C / 2
SAGOMA = [(0, 0), (W, 0), (W, dente_y(W, c2)), (c2 + HF, YH), (c2 - HF, YH), (c2 - HT, YB),
          (c1 + HT, YB), (c1 + HF, YH), (c1 - HF, YH), (0, dente_y(0, c1))]
FASCIA = [(0, YT), (W, YT)] + SAGOMA[2:]
COL_SX = [(0, 0), (C, 0), (C, YT), (0, YT)]
COL_DX = [(W - C, 0), (W, 0), (W, YT), (W - C, YT)]
PARETE = [(C, 0), (W - C, 0), (W - C, YT), (C, YT)]
APERTURA = [(AP[0], AP[1]), (AP[2], AP[1]), (AP[2], AP[3]), (AP[0], AP[3])]
LIVELLI = [('1-parete-arretrata', PARETE), ('2-colonne', None), ('3-fascia-gialla', FASCIA)]


def u2r(poly, x0=X8):            # unità -> pixel della foto raddrizzata
    return [(x0 + u * PX, Y0 + v * PX) for u, v in poly]


# ---------------------------------------------------------------------------
# 3. Maschere PNG (bianco su nero, stessa tela: si sovrappongono al pixel)
# ---------------------------------------------------------------------------
S, M = 2, 60
tela = (W * S + 2 * M, YH * S + 2 * M)
T = lambda poly: [(M + u * S, M + v * S) for u, v in poly]


def maschera(polys, nome):
    im = Image.new('L', tela, 0); d = ImageDraw.Draw(im)
    for p in polys: d.polygon(T(p), fill=255)
    im.save(MASC / nome)


maschera([SAGOMA], 'maschera-completa.png')
maschera([PARETE], 'livello-1-parete-arretrata.png')
maschera([COL_SX, COL_DX], 'livello-2-colonne.png')
maschera([FASCIA], 'livello-3-fascia-gialla.png')
maschera([APERTURA], 'livello-0-apertura-telo-APPROSSIMATA.png')

# ---------------------------------------------------------------------------
# 4. SVG: sagoma unica + versione a livelli (Inkscape/Illustrator vedono i layer)
# ---------------------------------------------------------------------------
pts = lambda poly: ' '.join(f'{u:g},{v:.1f}' for u, v in poly)
(MASC / 'maschera.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 -20 {W+40} {YH+40}" width="{W+40}" height="{YH+40}">
  <!-- Sagoma della campata tipo, vista frontale. Unità: larghezza modulo = 1000. -->
  <rect x="-20" y="-20" width="{W+40}" height="{YH+40}" fill="#000"/>
  <polygon id="sagoma" points="{pts(SAGOMA)}" fill="#fff"/>
</svg>
''')
L = 'inkscape:groupmode="layer"'
(MASC / 'maschera-livelli.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" viewBox="-20 -20 {W+40} {YH+40}" width="{W+40}" height="{YH+40}">
  <!-- Campata tipo divisa per piani di profondità. Unità: larghezza modulo = 1000.
       data-sporgenza = sporgenza stimata davanti alla parete arretrata, stesse unità (vedi LEGGIMI.md). -->
  <g id="sfondo" {L} inkscape:label="sfondo"><rect x="-20" y="-20" width="{W+40}" height="{YH+40}" fill="#000"/></g>
  <g id="apertura-telo" {L} inkscape:label="0 apertura telo (approssimata, piu arretrata)" data-sporgenza="negativa, non misurabile">
    <polygon points="{pts(APERTURA)}" fill="none" stroke="#6cf" stroke-width="3" stroke-dasharray="12 8"/></g>
  <g id="parete-arretrata" {L} inkscape:label="1 parete arretrata" data-sporgenza="0">
    <polygon points="{pts(PARETE)}" fill="#ff4fc8"/></g>
  <g id="colonne" {L} inkscape:label="2 colonne" data-sporgenza="{PROF['colonne']} (da {PROF_RANGE['colonne'][0]} a {PROF_RANGE['colonne'][1]})">
    <polygon id="colonna-sx" points="{pts(COL_SX)}" fill="#35d08a"/>
    <polygon id="colonna-dx" points="{pts(COL_DX)}" fill="#35d08a"/></g>
  <g id="fascia-gialla" {L} inkscape:label="3 fascia gialla" data-sporgenza="{PROF['fascia']} (da {PROF_RANGE['fascia'][0]} a {PROF_RANGE['fascia'][1]})">
    <polygon points="{pts(FASCIA)}" fill="#f5be28"/></g>
</svg>
''')

# ---------------------------------------------------------------------------
# 5. Verifica: livelli sovrapposti alla foto raddrizzata (campate 8 e 6)
# ---------------------------------------------------------------------------
foto = Image.fromarray(cv2.cvtColor(radd, cv2.COLOR_BGR2RGB)).convert('RGBA')
ov = Image.new('RGBA', foto.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
for x0 in (X8, X8 + 2 * PASSO_COL):
    d.polygon(u2r(PARETE, x0), fill=(255, 0, 200, 55))
    for p in (COL_SX, COL_DX): d.polygon(u2r(p, x0), fill=(0, 220, 120, 60))
    d.polygon(u2r(FASCIA, x0), fill=(255, 120, 0, 70))
    s = u2r(SAGOMA, x0); d.line(s + [s[0]], fill=(255, 0, 200, 255), width=3)
    for p in (COL_SX, COL_DX):
        q = u2r(p, x0); d.line(q + [q[0]], fill=(0, 200, 100, 255), width=2)
    q = u2r(APERTURA, x0); d.line(q + [q[0]], fill=(90, 200, 255, 255), width=2)
Image.alpha_composite(foto, ov).convert('RGB').save(FOTO / '04-verifica-livelli-su-foto.jpg', quality=92)

# ---------------------------------------------------------------------------
# 6. Indizi del rilievo (dove si vede che la parete non è piana)
# ---------------------------------------------------------------------------
K2 = 1.6
base = Image.fromarray(cv2.cvtColor(radd, cv2.COLOR_BGR2RGB))
base = base.resize((int(base.width * K2), int(base.height * K2)), Image.LANCZOS)
Wb, Hb = base.size
zoom_h = 360
tav = Image.new('RGB', (Wb, Hb + zoom_h + 40), 'white'); tav.paste(base, (0, 0))
d = ImageDraw.Draw(tav)
f = ImageFont.truetype(FB, 20); fs = ImageFont.truetype(FR, 16)
k = lambda x, y: (x * K2, y * K2)
kw = dict(font=f, stroke_width=3, stroke_fill='white')
# fianchi visibili solo dal lato rivolto alla camera
for (x0, x1, lab) in [(364, 372, 'A'), (993, 1006, 'B')]:
    d.rectangle([k(x0, 290), k(x1, 390)], outline=(255, 0, 0), width=3)
    d.text(k(x0 - 4, 395), lab, fill=(255, 0, 0), **kw)
for x in (293, 718, 1077):
    d.line([k(x, 290), k(x, 390)], fill=(40, 120, 255), width=3)
# ringhiera e tubo che passano davanti alle colonne
d.rectangle([k(286, 424), k(372, 452)], outline=(255, 140, 0), width=3)
d.rectangle([k(645, 424), k(724, 452)], outline=(255, 140, 0), width=3)
d.text(k(300, 456), 'C', fill=(255, 140, 0), **kw)
# passi: numeri (parete), colonne, denti (fascia)
num = [155.3, 511.8, 856.8, 1206.5]; col = [329, 684, 1041]; den = [328.5, 691.5, 1051.5]
for x in num: d.line([k(x, 228), k(x, 244)], fill=(40, 120, 255), width=4)
for x in col: d.line([k(x, 60), k(x, 84)], fill=(0, 170, 90), width=4)
for x in den: d.line([k(x, 512), k(x, 530)], fill=(230, 110, 0), width=4)
d.text(k(560, 205), 'passo numeri ≈ 348', fill=(40, 120, 255), **kw)
d.text(k(750, 40), 'passo colonne = 356', fill=(0, 150, 80), **kw)
d.text(k(760, 525), 'passo denti fascia ≈ 361', fill=(210, 90, 0), **kw)
# riquadri ingranditi (ognuno nel suo spazio, didascalia su due righe)
zooms = [((348, 330, 392, 420), 'A — colonna 9|8:', 'fianco destro visibile'),
         ((978, 335, 1022, 425), 'B — colonna 7|6:', 'fianco sinistro visibile'),
         ((698, 330, 742, 420), 'colonna 8|7:', 'nessun fianco a destra'),
         ((270, 405, 400, 470), 'C — ringhiera e tubo rosso', 'passano davanti alla colonna')]
x = 10
for (a, b, c_, e), r1, r2 in zooms:
    cr = Image.fromarray(cv2.cvtColor(radd[b:e, a:c_], cv2.COLOR_BGR2RGB))
    s = min((zoom_h - 50) / cr.height, 520 / cr.width)
    cr = cr.resize((int(cr.width * s), int(cr.height * s)), Image.LANCZOS)
    d.text((x, Hb + 8), r1, font=fs, fill='black'); d.text((x, Hb + 28), r2, font=fs, fill='black')
    tav.paste(cr, (x, Hb + 55))
    x += max(cr.width, int(d.textlength(r2, font=fs)), int(d.textlength(r1, font=fs))) + 40
d.text((x, Hb + 70), 'rosso = fianco della colonna visibile', font=fs, fill=(220, 0, 0))
d.text((x, Hb + 95), 'blu = lato opposto: nessun fianco', font=fs, fill=(40, 120, 255))
d.text((x, Hb + 120), 'arancio = ringhiera e tubo davanti alle colonne', font=fs, fill=(230, 110, 0))
d.text((x, Hb + 145), 'tacche = passi di numeri, colonne, denti', font=fs, fill='black')
tav.save(SCHEMI / 'indizi-rilievo.jpg', quality=90)

# ---------------------------------------------------------------------------
# 7. Schema proporzioni (prospetto frontale quotato)
# ---------------------------------------------------------------------------
Sd = 0.9; ML, MT, MR, MB = 360, 160, 500, 200
im = Image.new('RGB', (int(W * Sd + ML + MR), int(YH * Sd + MT + MB)), 'white'); d = ImageDraw.Draw(im)
f = ImageFont.truetype(FB, 22); fs = ImageFont.truetype(FR, 18); ft = ImageFont.truetype(FB, 26)
P = lambda u, v: (ML + u * Sd, MT + v * Sd)
d.polygon([P(u, v) for u, v in SAGOMA], fill=(255, 225, 245))
d.polygon([P(u, v) for u, v in FASCIA], fill=(245, 190, 40))
for p in (COL_SX, COL_DX): d.polygon([P(u, v) for u, v in p], fill=(215, 240, 225), outline=(0, 150, 80))
d.rectangle([P(AP[0], AP[1]), P(AP[2], AP[3])], outline=(60, 150, 230), width=2)
d.polygon([P(u, v) for u, v in SAGOMA], outline=(220, 0, 160), width=5)
fmt = lambda v: f'{v / 10:.1f}'.replace('.', ',')


def hdim(x1, x2, y, txt, up=True):
    a, b = P(x1, y), P(x2, y); d.line([a, b], fill='black', width=2)
    for p in (a, b): d.line([(p[0], p[1] - 10), (p[0], p[1] + 10)], fill='black', width=2)
    tw = d.textlength(txt, font=f); d.text(((a[0] + b[0] - tw) / 2, a[1] - (32 if up else -8)), txt, font=f, fill='black')


def vdim(x, y1, y2, txt, right=True):
    a, b = P(x, y1), P(x, y2); d.line([a, b], fill='black', width=2)
    for p in (a, b): d.line([(p[0] - 10, p[1]), (p[0] + 10, p[1])], fill='black', width=2)
    d.text((a[0] + (14 if right else -14 - d.textlength(txt, font=f)), (a[1] + b[1]) / 2 - 12), txt, font=f, fill='black')


hdim(0, W, -60, '100  (bordo esterno colonna → bordo esterno colonna)')
hdim(0, C, -8, fmt(C)); hdim(W - C, W, -8, fmt(C)); hdim(C, W - C, -8, fmt(W - 2 * C) + '  luce tra le colonne')
vdim(W + 60, 0, YT, fmt(YT)); vdim(W + 60, YT, YB, fmt(YB - YT) + ' fascia')
vdim(W + 190, 0, YB, fmt(YB) + ' al fondo fascia')
vdim(-60, 0, YH, fmt(YH) + ' in asse colonna', right=False)
hdim(c1 - HT, c1 + HT, YH + 60, 'dente ' + fmt(2 * HT) + ' (piano ' + fmt(2 * HF) + ')', up=False)
d.text((P(AP[0] + 10, AP[1] + 10)), 'apertura col telo (approssimata)', font=fs, fill=(40, 110, 200))
d.text((ML, im.height - 70), 'Unità: larghezza del modulo = 100.  Profondità del dente sotto la fascia: ' + fmt(YH - YB) + '.', font=fs, fill=(60, 60, 60))
d.text((ML, im.height - 45), 'Rosa = parete arretrata · verde = colonne · giallo = fascia · azzurro = apertura col telo. Vista frontale.', font=fs, fill=(60, 60, 60))
d.text((ML, 30), 'Campata tipo (es. n. 8) — prospetto frontale', font=ft, fill='black')
im.save(SCHEMI / 'schema-proporzioni.png')

# ---------------------------------------------------------------------------
# 8. Schema profondità: pianta (vista dall'alto) + sezione verticale
# ---------------------------------------------------------------------------
Z = 0.75
im = Image.new('RGB', (1700, 1320), 'white'); d = ImageDraw.Draw(im)
ft = ImageFont.truetype(FB, 26); f = ImageFont.truetype(FB, 19); fs = ImageFont.truetype(FR, 17)
d.text((40, 25), 'La campata non è piana: tre piani a profondità diverse (stime)', font=ft, fill='black')
# --- pianta
ox, oy = 110, 270                      # oy = filo parete arretrata
d.text((40, 90), 'PIANTA (vista dall\'alto, a metà altezza)', font=f, fill='black')
Pp = lambda u, z: (ox + u * Z, oy + z * Z * 2.2)  # profondità esagerata x2,2 per leggibilità
d.line([Pp(-60, 0), Pp(W + 60, 0)], fill=(200, 0, 150), width=4)
d.text(Pp(W + 70, -8), 'parete arretrata (0)', font=fs, fill=(200, 0, 150))
d.line([Pp(C, -40), Pp(W - C, -40)], fill=(60, 150, 230), width=3)
d.text(Pp(C + 10, -75), 'telo dentro l\'apertura: più indietro, profondità non misurabile', font=fs, fill=(40, 110, 200))
for x0 in (0, W - C):
    d.rectangle([Pp(x0, 0), Pp(x0 + C, PROF['colonne'])], fill=(215, 240, 225), outline=(0, 150, 80), width=3)
d.line([Pp(-60, PROF['fascia']), Pp(W + 60, PROF['fascia'])], fill=(230, 160, 0), width=4)
d.text(Pp(W + 70, PROF['fascia'] - 8), 'filo fascia gialla (sotto) ≈ ' + fmt(PROF['fascia']), font=fs, fill=(190, 120, 0))
d.text(Pp(W + 70, PROF['colonne'] - 8), 'filo colonne ≈ ' + fmt(PROF['colonne']), font=fs, fill=(0, 130, 70))
d.text(Pp(W / 2 - 120, PROF['fascia'] + 30), '↓ verso chi guarda / la camera', font=fs, fill=(90, 90, 90))
# --- sezione
sx, sy = 160, 700
d.text((40, 620), 'SEZIONE VERTICALE (nel mezzo della campata; colonna vista dietro)', font=f, fill='black')
Ps = lambda z, v: (sx + z * 0.52 * 2.2 + 400, sy + v * 0.52)
# colonna (in vista, dietro il piano di taglio)
d.rectangle([Ps(0, 0), Ps(PROF['colonne'], YT)], fill=(215, 240, 225), outline=(0, 150, 80), width=2)
# parete arretrata con apertura
d.line([Ps(0, 0), Ps(0, AP[1])], fill=(200, 0, 150), width=4)
d.line([Ps(-40, AP[1]), Ps(-40, AP[3])], fill=(60, 150, 230), width=3)
d.line([Ps(0, AP[1]), Ps(-40, AP[1])], fill=(200, 0, 150), width=2); d.line([Ps(0, AP[3]), Ps(-40, AP[3])], fill=(200, 0, 150), width=2)
d.line([Ps(0, AP[3]), Ps(0, YT)], fill=(200, 0, 150), width=4)
# ripiano e fascia
d.line([Ps(0, YT), Ps(PROF['fascia'], YT)], fill=(120, 120, 120), width=3)
d.rectangle([Ps(PROF['fascia'] - 12, YT), Ps(PROF['fascia'], YB)], fill=(245, 190, 40), outline=(190, 120, 0), width=2)
d.text(Ps(PROF['fascia'] + 15, YT + 5), 'fascia gialla', font=fs, fill=(190, 120, 0))
d.text(Ps(PROF['fascia'] + 15, YT - 45), 'ripiano (barre luminose, ringhiera, tubo rosso)', font=fs, fill=(90, 90, 90))
d.text(Ps(PROF['colonne'] + 15, 300), 'colonna (in vista)', font=fs, fill=(0, 130, 70))
d.text(Ps(-40, AP[1] + 120), 'telo ?  ', font=fs, fill=(40, 110, 200), anchor='ra')
d.text(Ps(-8, AP[3] + 200), 'parete arretrata', font=fs, fill=(200, 0, 150), anchor='ra')
d.text(Ps(PROF['colonne'] + 15, -12), '◂ cima colonna', font=fs, fill=(90, 90, 90))
d.text((40, im.height - 95), 'Unità: larghezza modulo = 100. In pianta e in sezione le profondità sono esagerate ×2,2 per leggerle.', font=fs, fill=(60, 60, 60))
d.text((40, im.height - 68), f'Sporgenza stimata: colonne ≈ {fmt(PROF["colonne"])} (da {fmt(PROF_RANGE["colonne"][0])} a {fmt(PROF_RANGE["colonne"][1])}), '
       f'fascia ≈ {fmt(PROF["fascia"])} (da {fmt(PROF_RANGE["fascia"][0])} a {fmt(PROF_RANGE["fascia"][1])}) davanti alla parete arretrata.', font=fs, fill=(60, 60, 60))
d.text((40, im.height - 41), 'Sono stime da una sola foto: servono per capire l\'ordine dei piani, non per costruire. Una misura sul posto le fissa.', font=fs, fill=(60, 60, 60))
im.save(SCHEMI / 'schema-profondita.png')

# ---------------------------------------------------------------------------
# 9. Misure in JSON
# ---------------------------------------------------------------------------
misure = {
    'nota': 'px_raddrizzata = pixel della foto 03-parete-raddrizzata.jpg; unita = modulo largo 1000 (nei documenti 100).',
    'camera': dict(focale_px_stimata=F_PX, fuga_orizzontali_foto_originale=VP_ORIZ,
                   direzione_verticali=DIR_VERT, **info_camera),
    'misurato_px_raddrizzata': {
        'cima_colonne_y': 79, 'fondo_trave_y': 72,
        'fascia_alto_y': 453, 'fascia_fondo_y': 490,
        'colonne_fronte_x': {'9|8': [293, 365], '8|7': [650, 718], '7|6': [1005, 1077]},
        'fianchi_visibili': {'9|8 lato destro': [365, 371], '8|7 lato sinistro': [645, 650],
                             '7|6 lato sinistro': [993, 1005], 'lati opposti': 'nessuno'},
        'denti_fascia': {'9|8': {'da': 262, 'a': 395, 'piano': [310, 345], 'fondo_y': 510},
                         '8|7': {'da': 628, 'a': 755, 'piano': [680, 705], 'fondo_y': 506.5},
                         '7|6': {'da': 988, 'a': 1115, 'piano': [1035, 1065], 'fondo_y': 508}},
        'numeri_centro_x': {'9': 155.3, '8': 511.8, '7': 856.8, '6': 1206.5},
        'aperture_telo': {'8': {'x': [369, 643], 'y': [105, 238]}, '7': {'x': [726, 997], 'y': [100, 231]}},
        'passi': {'numeri_parete': [356.5, 345.0, 349.7], 'colonne': [355, 357], 'denti_fascia': [363, 360]},
    },
    'modello_unita': dict(larghezza_modulo=W, colonna=C, luce_tra_colonne=W - 2 * C,
                          fascia_alto=YT, fascia_fondo=YB, fondo_dente=YH,
                          dente_larghezza=2 * HT, dente_piano=2 * HF,
                          apertura_telo_approssimata=dict(x=[AP[0], AP[2]], y=[AP[1], AP[3]]),
                          sagoma=SAGOMA),
    'profondita_stimate_unita': dict(valori=PROF, intervalli=PROF_RANGE,
                                     rapporti_di_scala=dict(colonne_su_parete=1.022, fascia_su_parete=1.037, fascia_su_colonne=1.015),
                                     distanza_camera_parete=' ≈ 2,75 × larghezza modulo'),
    'scala_reale_grezza': 'modulo largo circa 4,3-4,9 m (stimato da persona e panche, ±20%): da confermare con una misura',
}
(BASE / 'misure.json').write_text(json.dumps(misure, ensure_ascii=False, indent=2))
print('fatto:', info_camera)
