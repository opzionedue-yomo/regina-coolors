# RILIEVO PARETE — campata tipo (colonne + fascia gialla)

Rilievo ricavato da **una sola foto** scattata al volo dalla balconata di fronte
(`foto/00-originale.jpg`). Qui dentro ci sono le misure, le maschere, gli schemi e le deduzioni.

---

## L'area (come concordata)

Una **campata**, per esempio la n. 8 (quella con la macchia blu):

- **ai lati:** dal bordo esterno della colonna di sinistra al bordo esterno della colonna di destra,
  **colonne comprese**;
- **in alto:** la **cima delle colonne**, poco sotto la trave nera, dove appoggiano i faretti.
  I faretti erano solo un riferimento per capirci;
- **in basso:** il **fondo della fascia gialla**, compresa tutta la parte gialla tra le due colonne.
  Sotto ogni colonna la fascia scende con un **dente** a trapezio.

Le campate con la macchia blu si alternano a quelle con la luce bianca: 9 bianca, 8 blu, 7 bianca, 6 blu.

---

## Cosa c'è nella cartella

```
rilievo-parete/
├── LEGGIMI.md              questo file: deduzioni, misure, dubbi
├── misure.json             tutte le misure, grezze (pixel) e ricavate (unità)
├── foto/
│   ├── 00-originale.jpg                 la foto di partenza
│   ├── 01-area-prima-bozza.jpg          primo tentativo (limite alto ai faretti, fascia esclusa)
│   ├── 02-area-confermata.jpg           area confermata, sulla foto storta
│   ├── 03-parete-raddrizzata.jpg        la foto raddrizzata come se fosse frontale
│   └── 04-verifica-livelli-su-foto.jpg  maschera divisa per piani, sovrapposta alla foto raddrizzata
├── maschere/
│   ├── maschera.svg                     sagoma unica, bianco su nero (vettoriale)
│   ├── maschera-livelli.svg             stessa sagoma divisa in livelli (Inkscape/Illustrator li vedono come layer)
│   ├── maschera-completa.png            sagoma unica, bianco su nero
│   ├── livello-1-parete-arretrata.png   ┐
│   ├── livello-2-colonne.png            ├ un PNG per piano, stessa tela: si sovrappongono al pixel
│   ├── livello-3-fascia-gialla.png      ┘
│   ├── livello-0-apertura-telo-APPROSSIMATA.png
│   └── settore/                         settore per l'impianto contiguo (vedi sotto)
├── schemi/
│   ├── schema-proporzioni.png           prospetto frontale quotato
│   ├── schema-profondita.png            pianta + sezione: i tre piani
│   └── indizi-rilievo.jpg               dove si vede, nella foto, che la parete non è piana
└── script/
    └── ricostruisci.py                  rifà tutto da capo partendo dalla foto originale
```

Per rigenerare:

```bash
pip install numpy opencv-python-headless pillow
python3 rilievo-parete/script/ricostruisci.py
```

---

## 1. Come ho raddrizzato la foto

La foto era storta in due modi:

- **Parete girata di circa 4,6°** rispetto alla fotocamera, con il lato destro più lontano. Per questo
  le campate a destra sembravano più strette e più basse: il passo delle colonne passava da 362 a 337 px.
- **Rotazione del telefono di circa 0,2°**. L'inclinazione in alto o in basso è trascurabile: la
  fotocamera era più o meno all'altezza del pannello, sulla balconata di fronte.

Ho calcolato i **punti di fuga** delle linee orizzontali della parete (cima delle colonne, fascia
gialla) e delle verticali (bordi delle colonne). Poi ho ruotato la fotocamera "virtualmente" fino a
metterla di fronte alla parete.

**Controlli dopo la correzione:**

- la cima delle colonne e la fascia gialla vengono orizzontali e parallele, con uno scarto di 1–2 px;
- le colonne hanno lo stesso passo, **355 e 357 px** (prima la differenza era circa il 7%).

La focale del telefono non si conosce, perché la foto non ha dati EXIF: l'ho stimata in 1150 px.
Anche cambiandola del ±15%, il rapporto altezza/larghezza della campata cambia **meno dello 0,3%**.

---

## 2. Proporzioni della campata (vista frontale)

Unità: **larghezza del modulo = 100** (bordo esterno colonna → bordo esterno colonna).

| parte | valore |
|---|---|
| larghezza modulo | **100** |
| colonna (ciascuna) | **16,6** |
| luce tra le colonne | **66,8** |
| dalla cima delle colonne all'inizio della fascia gialla | **87,6** |
| spessore fascia gialla | **8,7** |
| altezza al fondo della fascia | **96,3** |
| altezza in asse colonna (con il dente) | **100,5** |
| dente sotto la colonna: larghezza / parte piatta / profondità | **30 / 7 / 4,2** |
| apertura col telo (approssimata) | x da 17,9 a 82,1 · y da 5,5 a 36,5 |

In pratica la maschera è **quasi quadrata**. Precisione stimata: **1–2%**.

---

## 3. La campata NON è piana — cosa si vede nella foto

Ci sono **tre piani** a profondità diverse, più un quarto in fondo all'apertura:

| livello | cosa | dove sta |
|---|---|---|
| 0 | telo dentro l'apertura | ancora più indietro della parete (profondità non misurabile) |
| 1 | **parete arretrata** tra le colonne (pannello col numero e la macchia blu, architrave sopra il telo) | il piano più lontano (riferimento = 0) |
| 2 | **colonne** | sporgono dalla parete |
| 3 | **fascia gialla** (bordo del ripiano) | sporge ancora di più, davanti alle colonne |

**Gli indizi** (vedi `schemi/indizi-rilievo.jpg`):

1. **Fianchi delle colonne.** Di ogni colonna si vede un fianco sottile, e sempre e solo **dal lato
   rivolto verso la fotocamera**. La fotocamera guardava più o meno il centro-sinistra della campata 8:
   - la colonna 9|8 mostra il fianco destro (circa 6 px);
   - le colonne 8|7 e 7|6 mostrano il fianco sinistro (circa 5 e 12 px);
   - sul lato opposto non si vede mai nessun fianco;
   - la colonna 7|6, la più lontana dall'asse della fotocamera, ha il fianco più largo, come deve essere.

   Questo succede solo se le colonne sporgono dalla parete.
2. **Ringhiera e tubo rosso.** Corrono dritti e **senza interruzioni davanti alle colonne**. Quindi il
   bordo del ripiano, cioè la fascia gialla, sta più avanti del fronte delle colonne. Sul ripiano,
   ai piedi della parete arretrata, appoggiano le barre luminose che fanno la macchia blu.
3. **Passi diversi per piani diversi.** Nella foto un piano più vicino appare più grande, quindi con un
   passo più lungo. La struttura invece si ripete uguale (stessa campata). Misurando il passo su ogni piano:
   - numeri dipinti sulla parete arretrata: **≈ 348 px** (il più corto: il piano più lontano);
   - colonne: **356 px**;
   - denti della fascia gialla: **≈ 361 px** (il più lungo: il piano più vicino).

   Stesso ordine degli indizi 1 e 2: parete → colonne → fascia.

**Stima delle sporgenze** davanti alla parete arretrata (unità: modulo = 100):

| | stima | intervallo plausibile |
|---|---|---|
| colonne | **≈ 6,5** | 5 – 9 |
| fascia gialla (fronte) | **≈ 11** | 8 – 14 |

La fotocamera era a circa **2,75 larghezze di modulo** dalla parete.

Queste stime vengono dai rapporti di scala del punto 3 (+2,2% e +3,7%) e dalla larghezza dei fianchi
(punto 1), che danno valori coerenti. Dipendono però dalla focale stimata e da differenze di pochi
pixel: sono **ordini di grandezza**, non misure da cantiere.

**Scala reale (molto grezza).** Prendendo come riferimento la persona in piedi e le panche, il modulo
dovrebbe essere largo circa **4,3–4,9 m**. Con questa scala le colonne sporgerebbero circa 25–40 cm e
la fascia circa 40–60 cm. **Da confermare con una misura sul posto.**

### Cosa cambia per la maschera

- **Guardata esattamente di fronte, la sagoma non cambia:** il contorno resta quello disegnato.
- **Guardata o proiettata di lato**, i piani **scivolano uno rispetto all'altro** (parallasse):
  - si vedono, e vengono colpiti dalla luce, i **fianchi delle colonne**, la **cima delle colonne** e
    il **ripiano** sopra la fascia;
  - una maschera unica e piatta combacia solo su un piano alla volta.
- Per questo la maschera è divisa in **livelli**, uno per piano (`maschera-livelli.svg` e i PNG
  `livello-*`), così ogni piano si può adattare per conto suo.
- Nella foto, le parti più vicine appaiono più grandi del 2–4%. Le larghezze le ho misurate sul piano
  delle colonne e la fascia sul suo piano, quindi l'effetto sulla sagoma resta **sotto l'1%**.

---

## 3b. Settore per l'impianto contiguo (campate 1–9)

Con le campate una accanto all'altra, la maschera con le **due colonne intere** si sovrapporrebbe
alla vicina sulla colonna in comune. Per l'impianto il **settore** va **dal centro di una colonna al
centro della successiva**: la campata più mezza colonna per lato. I 9 settori si affiancano senza
buchi e senza sovrapposizioni.

In `maschere/settore/`:

| file | cosa |
|---|---|
| `settore-maschera.png` | bianco = proietta, nero = no · 1668 × 2010 px, senza margini (il riquadro è il settore) |
| `settore-maschera-alfa.png` | stessa sagoma, bianca su fondo trasparente |
| `settore-livello-1/2/3-*.png` | parete arretrata, mezze colonne, fascia gialla: stessa tela, si sovrappongono al pixel |
| `settore.svg` | la sagoma in vettoriale |
| `settore-verifica-su-foto.jpg` | il settore sulla campata 8 della foto raddrizzata |

Proporzioni del settore (unità come sopra, modulo = 100): larghezza **83,4** (= passo delle colonne),
mezza colonna **8,3** per lato, altezza **100,5** in asse colonna, **96,3** al fondo della fascia.

Restano fuori dai 9 settori le due mezze colonne alle estremità, a sinistra della 9 e a destra della 1.

---

## 4. Semplificazioni e dubbi aperti

- **Denti sotto la fascia:** li ho disegnati uguali e centrati sotto ogni colonna. In foto quelli a
  destra sembrano spostati di pochi pixel: è in buona parte l'effetto della fascia che sta più avanti
  (vedi punto 3).
- **Colonne:** conta solo il fronte. I fianchi sono esclusi dalla sagoma frontale.
- **Apertura col telo:** i teli delle campate 8 e 7 non sono appesi alla stessa altezza (differenza di
  circa 7 px). Il riquadro è una media: indicativo.
- **Campata 8, riga orizzontale sul pannello:** sotto il numero, a circa 47 unità dalla cima, c'è una
  linea orizzontale che nella 7 non si vede. Potrebbe essere un pannello diverso o un tamponamento.
  Da verificare sul posto.
- **Colonna 9|8:** a sinistra confina con la finestra della campata 9, quindi il suo bordo sinistro è
  meno netto degli altri.

### Cosa servirebbe per chiudere il rilievo

1. **Una misura reale**, per esempio la larghezza di una colonna o il passo tra due colonne: tutto passa
   in centimetri.
2. **Di quanto sporgono**, misurate sul posto, le colonne e la fascia rispetto alla parete arretrata.
3. **Quali campate** vanno coperte: solo quelle con la macchia blu (8, 6, …) o tutte.
