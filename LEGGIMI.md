# REGINA COOLORS — sito, primo colpo

Sito completo, statico, che gira **solo in locale** su questo Mac.
Costruito a partire da `TESTI.docx`, `HOMEPAGE.docx` e dai due concept grafici (quello mandato in chat
e quello dentro HOMEPAGE.docx, che è diverso e contiene il logo neon).

---

## Come si accende

```bash
cd /Users/andreacuomo/Developer/REGINA-COOLORS && ./avvia.sh
```

Poi si apre **http://localhost:8910** — porta 8910, libera, non tocca nessuno degli altri banchi.
Per spegnerlo: `Ctrl+C` nella finestra del terminale.

## Come si cambia un testo

1. si apre `contenuti.py` (è tutto lì dentro: testi, prezzi, date, menu, contatti);
2. si salva;
3. si rilancia `python3 costruisci.py`;
4. si ricarica la pagina nel browser.

Le pagine dentro `sito/` sono **generate**: se le modifichi a mano, la prossima costruzione le riscrive.

---

## Cosa c'è dentro

```
REGINA-COOLORS/
├── contenuti.py       tutti i testi, i prezzi, le date, il menu
├── costruisci.py      il generatore (icone, impaginazione, calendario, modulo)
├── avvia.sh           accende il server locale sulla porta 8910
└── sito/              il sito vero e proprio (27 pagine)
    ├── index.html … + 26 pagine
    └── assets/  stile.css · sito.js · font/ (Poppins e Caveat, in locale) · img/
```

**27 pagine**: home · corsi (+ 9 schede workshop) · calendario · feste ed eventi privati (+ 5 schede) ·
armocromia · sabato creativo · pausa creativa · tappeto personalizzato · gift card · chi sono ·
contatti · domande frequenti · rimborsi e cancellazioni.

Tutto è locale: niente Google Fonts, niente librerie, niente tracciamenti, niente cookie.
L'unica cosa che esce su internet è il riquadro della mappa in fondo ai contatti (OpenStreetMap).

---

## Le scelte che ho preso da solo (e che vanno confermate da Regina)

1. **Calligrafia (A4)** — nei documenti non c'è nessun testo: la pagina esiste ma dice
   «scheda in preparazione» con il bottone per scrivere. **Serve il testo.**
2. **Punch needle** — l'introduzione diceva «in sole 3 ore», la scheda sotto diceva «2 ore»:
   ho messo **2 ore** dappertutto. Da confermare quale delle due è giusta.
3. **Coroncine di fiori** — il prezzo nel documento era vuoto (« € a persona»): ho scritto **«su richiesta»**.
4. **Biglietti d'auguri e coroncine** — non c'erano date: ho scritto «date in definizione».
5. **Team building, addio al nubilato, eventi aziendali (C3, C4, C5)** — nel documento esiste un solo
   testo (quello dei party per adulti). Ho fatto **tre pagine separate** come chiede il menu, con un
   attacco scritto su misura per ciascuna e il corpo in comune. Se vuoi testi diversi, si sostituiscono.
6. **«Pomeriggi creativi» / «Pausa creativa»** — nei due file compaiono tutti e due i nomi:
   ho tenuto **Pausa creativa**, come nel menu della homepage.
7. **Sabato creativo** — «ad ½ workshop semplici» l'ho letto come **«a uno o due workshop semplici»**.
8. **Listino patch bar** — «BERRETTO LANA 30 MISTO 50» l'ho spezzato in due voci:
   berretto in lana 30 €, berretto misto 50 €.
9. **Gift card** — nel testo l'indirizzo era «via San Mamolo 39», altrove «39C»: ho uniformato a **39C**.
10. **Refusi corretti** senza cambiare il senso: quì→qui, ispiarazioni→ispirazione, pentierai→pentirai,
    traformiamo→trasformiamo, schopping→shopping, pohino→pochino, talaio→telaio, unoggetto→un oggetto,
    più qualche virgola e qualche accordo.

## Cosa manca prima di poter pubblicare

- **Le foto vere.** Quelle che vedi (l'ambiente in home e le 4 card) sono **ritagli del concept fatto
  con l'AI**: servono come segnaposto, non sono foto del laboratorio. Vanno sostituite in `sito/assets/img/`.
  Attenzione: in due di quelle immagini si vede una **insegna al neon diversa dal logo vero**, perché
  l'AI se l'era inventata. Motivo in più per sostituirle.
- **Il logo in vettoriale.** Quello sul sito adesso è **il logo vero** (il tondo con la sagoma incoronata e
  REGINA_COOLORS), ma ricavato dal JPEG arrivato su WhatsApp: quel file aveva la **scacchiera della
  trasparenza stampata dentro**, così l'ho scontornato e ho ridipinto l'alone al neon perché tenesse anche
  sul fondo scuro. Sorgente e versione grande sono in `logo-sorgente-whatsapp.jpeg` e
  `sito/assets/img/logo-originale-scontornato.png`. Per le stampe e per gli schermi grandi serve
  comunque **il file vettoriale** (AI, EPS o SVG) da chi ha disegnato il logo.
- **P.IVA e ragione sociale** nel piè di pagina (adesso c'è scritto «P.IVA da inserire»).
- **Il puntino della mappa è approssimativo** (via San Mamolo, altezza civico 39): da verificare.
- **Privacy policy e cookie policy** (oggi il sito non usa cookie, ma la mappa è di OpenStreetMap).
- Tutte le pagine hanno **`noindex`** addosso: finché è una bozza, Google non la deve vedere.
  Si toglie da `costruisci.py`, riga del `<meta name="robots">`.

## Come funziona la prenotazione, oggi

Non c'è un server, quindi non c'è un modulo che «invia». Il modulo dei contatti **prepara il messaggio
già scritto** e apre WhatsApp (o il programma di posta) con dentro nome, esperienza, numero di persone
e periodo. Funziona bene ed è a costo zero. Se un domani si vuole la prenotazione con pagamento,
è un capitolo a parte.
