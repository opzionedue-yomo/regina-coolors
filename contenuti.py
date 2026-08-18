# -*- coding: utf-8 -*-
"""
Tutti i testi del sito Regina Coolors.
Fonte: TESTI.docx + HOMEPAGE.docx (Regina, agosto 2026).
Si modifica QUESTO file, poi si rilancia:  python3 costruisci.py
"""

# ---------------------------------------------------------------- dati di base
AZIENDA = {
    "nome": "Regina Coolors",
    "claim": "Esperienze creative",
    "indirizzo": "Via San Mamolo 39C, Bologna",
    "telefono": "366 4318918",
    "telefono_intl": "393664318918",
    "email": "regina.lolli@hotmail.it",
    "instagram": "regina_coolors",
    "instagram_url": "https://www.instagram.com/regina_coolors/",
    "mappa": "https://maps.google.com/?q=Via+San+Mamolo+39C+Bologna",
    "strillo": "LABORATORI CREATIVI · TUFTING · WORKSHOP · EVENTI PRIVATI · BOLOGNA",
}

# ------------------------------------------------------------------- home page
HOME = {
    "titolo_grande": [
        '<span class="r">TEMPO DI QUALITÀ</span>',
        '<span>PER SÉ, DOVE</span>',
        '<span><em class="v">SVAGO</em> E</span>',
        '<span class="v">APPRENDIMENTO</span>',
        '<span>SI INCONTRANO.</span>',
    ],
    "sottotitolo": [
        "Non semplici attività creative ma momenti di <b>benessere</b>, <b>condivisione</b>, "
        "<b>socialità</b> e <b>scoperta</b>, in un ambiente rilassato, piacevole e sicuro, "
        "dove ogni dettaglio è curato e personalizzabile.",
        "Un’occasione per rallentare, imparare e ritrovare il piacere di creare con le proprie mani "
        "non solo un oggetto ma <b>un ricordo autentico e duraturo</b>.",
    ],
    "valori": [
        ("cuore", "BENESSERE", "Rallenta e prenditi cura di te"),
        ("gruppo", "CONDIVISIONE", "Vivi esperienze e crea legami"),
        ("stella", "CREATIVITÀ", "Impara nuove tecniche e sperimenta"),
        ("smile", "AMBIENTE SICURO", "Accogliente, inclusivo e personalizzabile"),
    ],
    "scorciatoie": [
        ("CORSI E WORKSHOP", "Tante attività creative da scoprire", "corsi.html", "img/c-tufting.jpg", "rosa"),
        ("FESTE ED EVENTI PRIVATI", "Compleanni, team building, addii", "eventi-privati.html", "img/c-eventi.jpg", "viola"),
        ("CREA IL TUO TAPPETO", "Tufting: il più amato di Bologna", "tufting.html", "img/c-workshop.jpg", "salvia"),
        ("GIFT CARD", "Regala tempo di qualità e creatività", "gift-card.html", "img/c-giftcard.jpg", "giallo"),
    ],
    "impazziscono": [
        ("TUFTING", "tufting.html", "rosa", "tufting"),
        ("RICAMO CREATIVO", "ricamo-creativo.html", "viola", "ricamo"),
        ("PATCH BAR", "patch-bar.html", "salvia", "patch"),
        ("FLUFFY FLOWERS", "fluffy-flowers.html", "giallo", "fiore"),
    ],
}

# ------------------------------------------------- calendario / prossime date
# Le date sono quelle indicate nei testi. Aggiungere qui i nuovi appuntamenti.
EVENTI = [
    {"data": "2026-09-27", "ora": "",              "titolo": "Ricama la tua foto",
     "pagina": "ricamo-su-foto.html", "stato": "posti disponibili", "colore": "viola"},
    {"data": "2026-10-06", "ora": "",              "titolo": "Corso di ricamo creativo · adulti (1° dei 6 incontri)", "breve": "Ricamo creativo · adulti",
     "pagina": "ricamo-creativo.html", "stato": "posti limitatissimi", "colore": "rosa"},
    {"data": "2026-10-07", "ora": "",              "titolo": "Corso di ricamo creativo · bambini (1° dei 5 incontri)", "breve": "Ricamo creativo · bambini",
     "pagina": "ricamo-creativo.html", "stato": "posti limitatissimi", "colore": "rosa"},
    {"data": "2026-10-12", "ora": "",              "titolo": "Fluffy flowers",
     "pagina": "fluffy-flowers.html", "stato": "posti disponibili", "colore": "giallo"},
    {"data": "2026-10-15", "ora": "",              "titolo": "Ricama la tua foto",
     "pagina": "ricamo-su-foto.html", "stato": "posti disponibili", "colore": "viola"},
]
SABATO_RICORRENTE = {
    "titolo": "Sabato creativo (bambini)",
    "ora": "9:00–11:00 · 11:00–13:00",
    "pagina": "sabato-creativo.html",
    "colore": "salvia",
}
CALENDARIO_MESI = [(2026, 9), (2026, 10), (2026, 11)]
CALENDARIO_NOTA = (
    "Ogni mese si aggiungono nuove date di <b>tufting</b> e <b>punch needle</b>, sia serali "
    "infrasettimanali sia nel weekend: la disponibilità è limitatissima perché accolgo solo piccoli gruppi. "
    "Scrivimi su WhatsApp per assicurarti il posto o seguimi su Instagram, dove pubblico le date in continuo aggiornamento."
)

# ------------------------------------------------------- blocchi riutilizzabili
LABORATORI_BAMBINI = [
    ("TUFTING", "Realizza un piccolo tappeto o quadro con le tue mani con il tufting gun, con la forma e i colori che vuoi tu, sparando la lana nella tela. Esperienza amatissima e ad alto grado di soddisfazione ma non adatta ai bambini piccoli: è ok dai 10 anni in su, amatissima dai ragazzi delle medie e delle superiori e dagli adulti di ogni sesso. Il numero massimo è di 6 partecipanti: se desideri organizzarla per più ospiti sentiamoci! Per i bambini di età inferiore sarà obbligatoria la permanenza e l’assistenza del genitore durante l’attività.", "tufting.html"),
    ("PATCH BAR", "Crea la tua borsa, il tuo cappellino, il tuo zaino, il tuo berretto, il tuo portachiavi, la tua t-shirt, la tua felpa, la tua trousse, il tuo astuccio: partendo da una base neutra del colore che desideri dai vita a un oggetto a tua scelta, personalizzandolo secondo il tuo gusto e stile con le tantissime decorazioni, strass e patch disponibili anche a tema! Consigliato dai 5 anni in su, ma queste esperienze non hanno età e piacciono a tutti, grandi e piccoli, maschi e femmine.", "patch-bar.html"),
    ("RICAMA LA TUA FOTO", "Uno scatto a cui tieni molto può essere valorizzato e reso ancor più speciale decorandolo e ricamandoci sopra a mano fili colorati. Ti stupirai del bellissimo risultato! Adatto dagli 8 anni in su ma amatissimo anche dalle ragazzine e dalle mamme.", "ricamo-su-foto.html"),
    ("LABORATORIO DEI CERCHIETTI", "Esperienza creativa per realizzare un cerchietto con la tecnica degli elastici e imparare a decorarlo con piccoli charms, ognuno secondo il proprio stile. Consigliato tra i 6 e gli 8 anni.", None),
    ("FLUFFY FLOWERS", "Impara la tecnica per creare differenti tipologie di fiori modellando a mano soffici bastoncini di velluto e crea un piccolo bouquet colorato. Consigliato dagli 8 anni in su e amatissimo anche dalle ragazzine delle medie e pure dalle mamme.", "fluffy-flowers.html"),
    ("LABORATORIO DEGLI ORSETTI", "Fai uscire lo stilista che è in te! Realizza a mano un vestitino per il tuo orsetto partendo dal cartamodello e dalla stoffa e decoralo con fiocchi e charms: ti porterai a casa un orsetto portachiavi. Consigliato dai 5 anni in su, lo adorano sia i maschi sia le femmine.", None),
    ("LABORATORIO DEGLI SPECCHI E DEI FERMAGLI", "Impara a decorare con la colla magica colorata un piccolo specchio, un fermaglio o una spazzola per capelli e adornali con decorazioni e charms secondo il tuo stile. Consigliato dagli 8 anni in su e amatissimo dalle ragazzine più grandi. Si creano in tutto 2 oggetti.", None),
    ("LABORATORIO DELLE CORNICI", "Crea un ricordo speciale decorando con la colla magica colorata una cornice dove inseriremo la foto ricordo della festa e personalizzala con charms e decorazioni secondo il tuo stile. Consigliato dagli 8 anni in su ma perfetto anche per gli adulti.", None),
    ("LABORATORIO DEI GIOIELLI", "Braccialetti e collanine sono un must: lasciati contagiare dal mondo delle perline e dei ciondoli e crea la tua parure unica con inserti in stoffa. Consigliato dagli 8 anni ma amatissimo anche da ragazzine e adulti.", None),
    ("CORONCINE DI FIORI", "Con l’aiuto di una esperta fiorista apprenderemo come si intreccia e realizza una coroncina di fiori da conservare come decorazione o indossare. Perfetto per condividere un momento mamma e figlia.", "coroncine-di-fiori.html"),
    ("BIGLIETTI D’AUGURI RICAMATI A MANO", "Trasformiamo assieme cartoncini colorati in biglietti d’auguri unici e personalizzati, traforandoli e ricamandoli a mano. Super rilassante e dal risultato wow! Ideale dagli 8 anni in su ma amatissimo dai grandi.", "biglietti-auguri.html"),
    ("LABORATORIO DEI PUPAZZI", "Con piccoli telai circolari daremo vita insieme a dei veri pupazzini cicciosi e colorati realizzati con un filato morbido e li personalizzeremo ciascuno in base al proprio stile. Età: dagli 8 anni. Solo per questa esperienza il numero massimo di partecipanti è di 4 persone.", None),
    ("PUNCH NEEDLE", "Se pensi che ricamare sia difficile, con questo workshop cambierai idea subito: ricama sul telaio con l’ago magico e dai vita al tuo portachiavi! Consigliato dai 10 anni in su e perfetto anche per un’esperienza in relax tra adulti.", "punch-needle.html"),
    ("PIXEL ART", "Piccole perline colorate si fondono per dare vita a un portachiavi o a una calamita fatta a mano: questo workshop lo amano tutti, maschi e femmine, grandi e piccoli, ma lo consiglio tra gli 8 e i 15 anni.", None),
]

LABORATORI_ADULTI = [
    ("TUFTING", "Realizza un piccolo tappeto o quadro con le tue mani con il tufting gun, con la forma e i colori che vuoi tu, sparando la lana nella tela. Massimo 6 partecipanti. Non c’è molto da aggiungere: questa esperienza è la più amata e richiesta da tutti e ti permette di portare a casa un tappetino di 40 cm che lascerà tutti a bocca aperta, te compreso!", "tufting.html"),
    ("ARMOCROMIA", "Esperienza individuale o di gruppo (max 6 persone) durante la quale scopriremo insieme, confrontandoci e divertendoci, quelli che sono i colori in grado di valorizzare ciascuno dei partecipanti, per poter poi conoscere la propria palette personale e imparare a scegliere i vestiti giusti da indossare e il make up ideale. Molto amata dalle ragazze, adorata per gli addii al nubilato e perfetta anche come idea regalo!", "armocromia.html"),
    ("PATCH BAR", "Crea la tua borsa, il tuo cappellino, il tuo zaino, il tuo berretto, il tuo portachiavi, la tua t-shirt, la tua felpa, la tua trousse, il tuo astuccio: partendo da una base neutra del colore e del modello che desideri dai vita a un oggetto a tua scelta, personalizzandolo secondo il tuo gusto e stile con le tantissime decorazioni, strass e patch disponibili anche a tema.", "patch-bar.html"),
    ("RICAMA LA TUA FOTO", "Uno scatto a cui tieni molto può essere valorizzato e reso ancor più speciale decorandolo con dettagli brillanti e ricamandoci sopra a mano fili colorati. Ti stupirai del bellissimo risultato!", "ricamo-su-foto.html"),
    ("BIGLIETTI D’AUGURI RICAMATI A MANO", "Trasformiamo assieme cartoncini colorati in biglietti d’auguri unici e personalizzati, traforandoli e ricamandoli a mano. Super rilassante e dal risultato wow!", "biglietti-auguri.html"),
    ("FLUFFY FLOWERS", "Impara la tecnica per creare differenti tipologie di fiori modellando a mano soffici bastoncini di velluto e crea un piccolo bouquet colorato. Questa tecnica crea dipendenza!", "fluffy-flowers.html"),
    ("LABORATORIO DELLE CORNICI", "Crea una cornice speciale decorandola con la colla magica colorata e personalizzandola con charms e decorazioni secondo il tuo stile: al termine inserirai la foto che vuoi o inseriremo insieme uno scatto ricordo fatto sul momento.", None),
    ("LABORATORIO DEI GIOIELLI", "Braccialetti e collanine sono un must: lasciati contagiare dal mondo delle perline e dei ciondoli e crea la tua parure unica, anche con inserti in stoffa.", None),
    ("LABORATORIO DEI PUPAZZI", "Con piccoli telai circolari daremo vita insieme a dei veri pupazzini cicciosi e colorati realizzati con un filato morbido e li personalizzeremo ciascuno in base al proprio stile (max 4 partecipanti).", None),
    ("PUNCH NEEDLE", "Se pensi che ricamare sia difficile, con questo workshop cambierai idea subito: ricama sul telaio con l’ago magico e dai vita al tuo portachiavi o a un piccolo quadretto da appendere.", "punch-needle.html"),
    ("CORONCINE DI FIORI", "Con l’aiuto di una esperta fiorista apprenderemo come si intreccia e realizza una coroncina di fiori da conservare come decorazione o indossare.", "coroncine-di-fiori.html"),
    ("PIXEL ART", "Piccole perline colorate creano un disegno bidimensionale fatto di pixel e si fondono per dare vita a un portachiavi o a una calamita fatta a mano.", None),
]

NB_VERSATILI = ("Queste esperienze sono molto versatili: possono svolgersi in maniera guidata, in gruppo, "
                "per un evento privato riservando lo spazio in via esclusiva (min 4 partecipanti); "
                "oppure, se non hai un’occasione particolare ma ti piacerebbe partecipare, "
                "[guarda tutte le esperienze già in calendario](calendario.html) e unisciti a un gruppo "
                "dove, oltre a creare un oggetto speciale, conoscerai nuovi amici.")

# ------------------------------------------------------------------- le pagine
PAGINE = {}

PAGINE["corsi"] = {
    "titolo": "Corsi e workshop", "occhiello": "A · Le esperienze",
    "h1": "CORSI E WORKSHOP CREATIVI", "colore": "rosa", "icona": "workshop",
    "seo": "Corsi e workshop creativi a Bologna: tufting, punch needle, ricamo, patch bar, fluffy flowers e molto altro.",
    "lead": "In un mondo sempre più digitale, sapersi concedere del tempo per staccare e rallentare è un valore prezioso a qualsiasi età.",
    "blocchi": [
        ("p", "Concediti il lusso di ritagliarti qualche ora per rilassarti, riscoprire le tue capacità e il piacere di utilizzare le mani, attraverso attività guidate dove idee e colori si trasformano in qualcosa di concreto."),
        ("h", "A quali esperienze puoi partecipare nel mio spazio creativo?"),
        ("p", "Tantissime! Qui le proposte più amate e già a calendario, ma ce ne sono molte altre: tieni d’occhio la [pagina Instagram](INSTAGRAM) per scoprire le date in continuo aggiornamento, oppure [scoprile tutte nel calendario](calendario.html)."),
        ("cards", [
            ("TUFTING", "Crea il tuo tappeto filo dopo filo con la tufting gun. 3 ore, max 6 persone.", "tufting.html"),
            ("PUNCH NEEDLE", "Il ricamo con l’ago magico: in 2 ore un portachiavi o un quadretto.", "punch-needle.html"),
            ("RICAMO CREATIVO", "Un corso in più incontri per adulti e bambini: disegnare con il filo.", "ricamo-creativo.html"),
            ("CALLIGRAFIA", "Il piacere del gesto e della bella scrittura a mano.", "calligrafia.html"),
            ("PATCH BAR", "Personalizza ogni cosa: felpe, cappellini, borse, zaini con patch e strass.", "patch-bar.html"),
            ("RICAMA LA TUA FOTO", "Uno scatto a cui tieni, reso speciale con fili colorati.", "ricamo-su-foto.html"),
            ("BIGLIETTI D’AUGURI", "Cartoncini traforati e ricamati a mano: risultato wow.", "biglietti-auguri.html"),
            ("FLUFFY FLOWERS", "Soffici fiori di velluto modellati a mano: crea dipendenza!", "fluffy-flowers.html"),
            ("CORONCINE DI FIORI", "Con una esperta fiorista, una coroncina da indossare o conservare.", "coroncine-di-fiori.html"),
        ]),
        ("cta", [("GUARDA IL CALENDARIO", "calendario.html", "primary"), ("SCRIVIMI SU WHATSAPP", "WHATSAPP", "ghost")]),
    ],
}

PAGINE["tufting"] = {
    "titolo": "Tufting", "occhiello": "A1 · Corsi e workshop",
    "h1": "TUFTING", "colore": "rosa", "icona": "tufting",
    "seo": "Workshop di tufting a Bologna: crea il tuo tappeto con la tufting gun. 3 ore, piccoli gruppi, tutti i materiali inclusi.",
    "lead": "A Bologna tutti letteralmente impazziscono per il tufting: se ti manca questa esperienza devi assolutamente provarla! Vieni a creare il tuo tappeto, filo dopo filo.",
    "blocchi": [
        ("h", "Di che si tratta?"),
        ("p", "Workshop creativo che permette di realizzare tappeti e quadri tessili personalizzati utilizzando una speciale pistola, la <b>tufting gun</b>."),
        ("p", "Durante l’esperienza potrai partire da un disegno semplice e trasformarlo, colore dopo colore, in una creazione unica realizzata interamente con le tue mani, sparando la lana nella tela."),
        ("h", "Non hai mai usato una tufting gun? Nessun problema!"),
        ("p", "Il workshop è pensato anche per chi parte completamente da zero: accolgo soltanto piccoli gruppi, in maniera da poter seguire ciascuno al meglio. Ti guiderò passo dopo passo, dalla scelta del disegno e dei colori fino alla realizzazione del tuo tappeto: ti stupirai di cosa riuscirai a portarti a casa!"),
        ("p", "Il tufting è un’attività creativa divertente, rilassante e incredibilmente soddisfacente: per qualche ora si stacca dalla routine, ci si concentra sul gesto e si vede il proprio progetto prendere forma sotto le proprie mani."),
        ("p", "Puoi partecipare da solo, unendoti a un gruppo dove potrai conoscere gente, oppure in compagnia, scegliendo tra le varie date disponibili nel calendario ogni mese (piccoli sconti se venite in 3 amici); oppure ancora puoi prenotare un [workshop di tufting privato](eventi-privati.html) per il tuo piccolo gruppo, da svolgersi quando preferite. È anche un’idea originale per festeggiare compleanni, addii al nubilato, team building, eventi privati e occasioni speciali, o per fare un regalo a Bologna."),
        ("evidenza", "Alla fine? Avrai creato un tappeto unico con le tue mani, avrai trascorso 3 ore in totale relax e sicuramente avrai conosciuto nuove persone interessanti che condividono con te la curiosità di provare attività creative."),
        ("p", "Scegli il tuo disegno, scegli i tuoi colori e vieni a trasformarli in un piccolo tappeto speciale!"),
        ("info", [
            ("Prossime date", "Ogni mese sono disponibili diverse date, sia serali infrasettimanali sia nel weekend: scrivimi per assicurarti il tuo posto, la disponibilità è limitatissima perché accolgo solo piccoli gruppi. [Ecco i prossimi appuntamenti](calendario.html)"),
            ("Durata", "3 ore, in un’unica giornata. Il tempo è sufficiente per portare a termine l’opera ma non ne garantisce il completamento: rasatura e rifinitura verranno svolte eventualmente da me e potrai ritirare il tuo tappeto dopo circa 1 settimana."),
            ("A chi è rivolto", "Ragazzi e adulti"),
            ("Dove", "Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "6 (attivazione con almeno 3 partecipanti)"),
            ("Prezzo", "80 € a persona — tutti i materiali sono compresi. Sconto 10% se siete un gruppo di minimo 3 amici."),
        ]),
        ("cta", [("SCOPRI LE PROSSIME DATE E PRENOTA", "calendario.html", "primary"),
                 ("ORGANIZZA UN’ESPERIENZA PRIVATA", "eventi-privati.html", "ghost"),
                 ("REGALA IL TUFTING", "gift-card.html", "ghost")]),
        ("box", ("Non hai voglia di partecipare ma vorresti un tappeto personalizzato?",
                 "Scrivimi per acquistare il tuo pezzo unico: lo realizzerò io per te secondo le tue indicazioni, della dimensione che vuoi tu. [Vai alla pagina dedicata](tappeto-personalizzato.html)")),
        ("hr", None),
        ("h", "WORKSHOP BASE"),
        ("p", "Il workshop di tufting base è quello che propongo abitualmente e che trovi a calendario: un’esperienza in piccolo gruppo (max 6 partecipanti) che dura 3 ore, durante le quali imparerai a utilizzare la tufting gun e realizzerai il tuo tappeto di circa <b>40x40 cm</b>. Sembra incredibile, lo so, ma succede davvero!"),
        ("steps", [
            ("Step 1 · Prima di venire: scegli il disegno che vuoi realizzare",
             "Inviamelo su WhatsApp qualche giorno prima del workshop, in maniera che io possa trasferirlo sulla tela e organizzare i materiali. Qui sotto trovi la guida alla scelta del disegno."),
            ("Step 2 · Impara a utilizzare la tufting gun",
             "Durante la prima mezz’ora del workshop ti insegnerò la tecnica e i trucchi per maneggiare e utilizzare la pistola da tufting con cui realizzerai il tappeto; le indicazioni sono poche e semplici, non preoccuparti 😊"),
            ("Step 3 · Divertiti a sparare la lana nella tela",
             "Avrai due ore di tempo, tra risate e chiacchiere, per creare con calma un oggetto unico fatto con le tue mani, colore dopo colore: io sarò accanto a te a incoraggiarti e a prestarti assistenza, sempre!"),
            ("Step 4 · Applica la colla e rifinisci il tuo tappeto",
             "Terminata la tua opera ti mostrerò e ti farò sperimentare brevemente le fasi finali di incollaggio e rasatura base, che completerò eventualmente io: potrai ritirare il tappeto dopo circa 1 settimana."),
        ]),
        ("h", "Guida alla scelta del disegno per il tuo primo tappeto"),
        ("p", "Scegliere il disegno giusto per la tua prima esperienza di tufting può fare la differenza tra un’esperienza creativa appagante e una frustrante, e naturalmente anche nel risultato!"),
        ("ul", [
            "L’immagine deve essere frontale, in qualsiasi formato.",
            "Scegli grafiche semplici, con pochi grandi blocchi di colore.",
            "Le linee rette sono più agevoli da realizzare rispetto alle linee curve.",
            "Composizioni di forme geometriche sono piacevoli e semplici.",
            "I disegni o i paesaggi astratti sono ideali.",
            "Gli animali sono ok solo se stilizzati (non è possibile trasformare fedelmente in un tappeto la foto del proprio peloso, ma se ci tieni puoi provare a trasformare il tuo cucciolo in una grafica semplificata).",
            "No a disegni sfumati, strisce, puntini, elementi e dettagli piccoli.",
            "Si sconsigliano i personaggi dei cartoni animati, a meno che non siano davvero molto semplici.",
            "Le scritte sono fattibili, ma è probabile che te ne pentirai: riprodurre un font con precisione è molto impegnativo, sconsigliabile alla prima esperienza, e il risultato spesso non è fedele.",
        ]),
        ("p", "Ti piacerebbe provare il tufting ma non hai idea di cosa realizzare? Puoi trovare ispirazione sui social, oppure puoi partire da una grafica qualunque, anche realizzata con le tue mani o creata con l’AI."),
        ("p", "Se sei indeciso, sentiti libero di inviarmi le tue idee su WhatsApp: ti aiuterò volentieri nella scelta, a rielaborare l’immagine per semplificarla, oppure ti invierò alcune idee da cui prendere spunto."),
        ("cta", [("SCRIVIMI", "WHATSAPP", "primary")]),
        ("hr", None),
        ("h", "CORSO AVANZATO"),
        ("p", "Questo workshop lo attivo soltanto su richiesta. Ti intriga il mondo del tufting e vorresti scoprire proprio tutti i suoi segreti, oppure hai già esperienza e vorresti portare la tua conoscenza a un livello superiore?"),
        ("p", "Il workshop di tufting avanzato è un corso individuale o di coppia che si sviluppa in due giornate, per un totale di 8 ore dedicate ad approfondire la tecnica e a perfezionare ogni fase della realizzazione del tappeto, che avrà dimensione <b>50x50 cm</b>."),
        ("p", "Condividerò con te il mio metodo, consigli e strategie pratiche, e approfondiremo tutti quegli accorgimenti che fanno la differenza per ottenere un’opera di qualità."),
        ("info", [
            ("Prossime date", "Contattami e fissiamo insieme le due giornate a tuo comodo!"),
            ("Durata", "Circa 8 ore, distribuite su 2 giornate"),
            ("Dove", "Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "1 o 2 (puoi venire da solo, con un amico, oppure trovo io una persona con cui farti condividere l’esperienza!)"),
            ("Prezzo", "280 € a persona — tutti i materiali sono inclusi"),
        ]),
        ("steps", [
            ("Step 1 · Prima di venire: scegli il disegno che vuoi realizzare",
             "Inviamelo qualche giorno prima del workshop, in maniera che io possa trasferirlo sulla tela e organizzare i materiali."),
            ("Step 2 · Conosci gli strumenti e i materiali (giorno 1)",
             "Inizieremo dando uno sguardo più da vicino a tutti gli strumenti necessari, tra cui telaio e tela, con particolare attenzione alla scelta dei filati e dei materiali più adatti per ottenere un risultato di qualità."),
            ("Step 3 · Divertiti a sparare la lana nella tela (giorno 1)",
             "Con la tufting gun sperimenterai la tecnica sparando la lana nella tela per dar vita al tuo tappeto e ti insegnerò i trucchi per ottenere una superficie compatta e uniforme. Concluderemo la prima giornata dedicandoci alla fase di incollaggio, fondamentale per fissare il filato alla tela e preparare il tappeto alle successive lavorazioni."),
            ("Step 4 · Impara come si rifinisce un tappeto (giorno 2)",
             "La seconda giornata sarà dedicata alle rifiniture, fondamentali per dare al tappeto un aspetto preciso e professionale. Partiremo dall’estrazione del tappeto dal telaio e proseguiremo con la lavorazione del retro, per poi passare all’utilizzo di forbici e rasoio: imparerai a definire forme e contorni, a valorizzare le diverse texture, a creare le differenze di rilievo e a rendere la superficie più pulita e uniforme."),
        ]),
        ("p", "Al termine del corso avrai acquisito tecniche, accorgimenti e competenze pratiche per realizzare in autonomia tappeti ben rifiniti e curati in ogni particolare: con un pochino di pratica sarai in grado di dar vita a tappeti professionali."),
        ("cta", [("MAGGIORI INFO E PRENOTAZIONI", "contatti.html", "primary")]),
    ],
}

PAGINE["punch-needle"] = {
    "titolo": "Punch needle", "occhiello": "A2 · Corsi e workshop",
    "h1": "PUNCH NEEDLE", "colore": "viola", "icona": "ago",
    "seo": "Workshop di punch needle a Bologna: in 2 ore realizzi un portachiavi o un quadretto ricamato con l’ago magico.",
    "lead": "Una tecnica di ricamo speciale dove, in sole 2 ore, con il supporto di un piccolo telaio e di un ago magico, realizzerai un oggetto di 15 cm circa, con la forma e i colori che vuoi tu, che potrà diventare un portachiavi o un quadretto da appendere.",
    "blocchi": [
        ("info", [
            ("Durata", "2 ore, in un’unica giornata"),
            ("Dove", "Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "10 (attivazione con almeno 4 partecipanti)"),
            ("Prezzo", "40 € a persona — tutti i materiali sono compresi. Sconto 10% se siete un gruppo di minimo 3 amici."),
        ]),
        ("cta", [("QUI LE DATE IN PROGRAMMA", "calendario.html", "primary"), ("SCRIVIMI SU WHATSAPP", "WHATSAPP", "ghost")]),
    ],
}

PAGINE["ricamo-creativo"] = {
    "titolo": "Ricamo creativo", "occhiello": "A3 · Corsi e workshop",
    "h1": "CORSO DI RICAMO CREATIVO", "colore": "rosa", "icona": "ricamo",
    "seo": "Corso di ricamo creativo a Bologna per adulti e bambini: più incontri per imparare a disegnare con il filo.",
    "lead": "Ti piacerebbe imparare un nuovo hobby rilassante, che ti permetta di disegnare con il filo sulla stoffa e personalizzare i tuoi outfit? Il ricamo creativo diventerà la tua nuova ossessione: dopo questo corso non indosserai più le solite t-shirt tinta unita.",
    "blocchi": [
        ("info", [
            ("Durata", "5 o 6 incontri da 2 ore ciascuno"),
            ("Quando", "Il corso adulti inizia il <b>6 ottobre</b>, per 6 incontri, ogni martedì. Il corso bambini inizia il <b>7 ottobre</b>, per 5 incontri, ogni mercoledì."),
            ("Dove", "Regina Coolors, Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "6"),
            ("Prezzo", "Adulti: 230 € a persona per 6 incontri · Bambini (dagli 8 anni): 190 € a persona per 5 incontri"),
        ]),
        ("h", "Programma corso ricamo adulti"),
        ("p", "Partiremo dalla conoscenza di materiali, filati e tessuti, per capire come scegliere e abbinare quelli più adatti a ogni progetto."),
        ("p", "Attraverso prove ed esercizi pratici imparerai i punti base e decorativi del ricamo, sperimentandoli su tessuti e superfici differenti."),
        ("p", "Scopriremo poi come nasce un progetto di ricamo: dall’idea alla composizione, dalla creazione del disegno fino al trasferimento sul tessuto."),
        ("p", "Infine metteremo insieme tutto ciò che abbiamo imparato progettando e realizzando un berretto personalizzato e ricamato interamente a mano."),
        ("evidenza", "Non imparerai soltanto una tecnica: acquisirai un metodo creativo che potrai utilizzare anche dopo il corso per personalizzare capi, accessori e oggetti, trasformandoli in pezzi unici che parlano di te."),
        ("cta", [("POSTI LIMITATISSIMI · ISCRIVITI QUI", "contatti.html", "primary")]),
        ("h", "Programma corso ricamo bambini"),
        ("p", "Partiremo dalle basi del ricamo, imparando a infilare l’ago, a conoscere gli strumenti e a scoprire la differenza tra materiali e tessuti."),
        ("p", "Passo dopo passo sperimenteremo i punti base e i punti decorativi, imparando a usarli per disegnare, creare contorni, lettere, colorare e riempire forme e piccoli soggetti."),
        ("p", "Durante ogni incontro raccoglieremo prove ed esercizi pratici in uno speciale <b>diario del ricamo</b>: un piccolo vademecum personale in cui conservare punti, campioni e progressi, da portare a casa e utilizzare anche dopo il corso. Inoltre intraprenderemo un progetto che arriverà a compimento al termine del percorso: una pochette ricamata a mano."),
        ("p", "Impareremo anche come trasferire un disegno sul tessuto e trasformarlo attraverso ago e filo, aggiungendo decorazioni, dettagli e rifiniture brillanti per renderlo ancora più personale."),
        ("p", "Un percorso creativo e graduale in cui i bambini potranno apprendere una nuova abilità, allenare manualità fine e precisione e, soprattutto, scoprire quante cose possono nascere dalla propria fantasia. Il corso è adatto a bambini e bambine a partire dagli 8 anni in su."),
        ("cta", [("POSTI LIMITATISSIMI · ISCRIVITI QUI", "contatti.html", "primary")]),
    ],
}

PAGINE["calligrafia"] = {
    "titolo": "Calligrafia", "occhiello": "A4 · Corsi e workshop",
    "h1": "CALLIGRAFIA", "colore": "salvia", "icona": "penna",
    "seo": "Workshop di calligrafia a Bologna da Regina Coolors.",
    "lead": "Il piacere del gesto lento e della bella scrittura a mano: un’esperienza per rallentare, staccare dagli schermi e riscoprire carta, inchiostro e pennino.",
    "blocchi": [
        ("box", ("Scheda in preparazione",
                 "Sto mettendo a punto il programma, le date e i costi di questo workshop. Nel frattempo, se ti interessa, scrivimi: ti avviso appena apro le iscrizioni.")),
        ("cta", [("SCRIVIMI SU WHATSAPP", "WHATSAPP", "primary"), ("GUARDA GLI ALTRI WORKSHOP", "corsi.html", "ghost")]),
    ],
}

PAGINE["patch-bar"] = {
    "titolo": "Patch bar", "occhiello": "A5 · Corsi e workshop",
    "h1": "PATCH BAR: PERSONALIZZA OGNI COSA!", "colore": "viola", "icona": "patch",
    "seo": "Patch bar a Bologna: personalizza felpe, t-shirt, cappellini, borse e zaini con patch, strass e decorazioni.",
    "lead": "Desideri un look personalizzato e adori indossare capi esclusivi?",
    "blocchi": [
        ("p", "Partendo da una base neutra, del colore e del modello che desideri, dai vita a un oggetto a tua scelta tra cappellino, felpa, t-shirt, berretto, zainetto, borsa e pochette che ti metterò a disposizione. Potrai personalizzarlo secondo il tuo gusto e il tuo stile con le tantissime decorazioni, strass e patch!"),
        ("p", "Consigliato dai 5 anni in su, ma queste esperienze non hanno età e piacciono a tutti: grandi e piccoli, maschi e femmine."),
        ("info", [
            ("Durata", "Variabile"),
            ("Quando", "Questa esperienza è molto versatile: può svolgersi in maniera guidata con un piccolo gruppo riservando lo spazio in via esclusiva (min 4 partecipanti), oppure puoi venire anche da solo quando vuoi, su appuntamento, per personalizzare il tuo pezzo."),
            ("Dove", "Regina Coolors, Via San Mamolo 39C, Bologna"),
            ("A chi è rivolta", "Bambini e adulti"),
            ("Posti disponibili", "10"),
            ("Prezzo", "Variabile, a partire da 30 € fino a 80 € a persona a seconda dell’oggetto creato"),
        ]),
        ("h", "Il listino degli oggetti"),
        ("prezzi", [
            ("Zaino", "40 €"), ("Borsa sfrangiata", "40 €"), ("Tote bag", "30 €"),
            ("Pochette piatta", "25 €"), ("Trousse", "30 €"), ("Cappellino", "30 €"),
            ("Felpa", "45 €"), ("T-shirt", "35 €"), ("Astuccio", "25 €"),
            ("Berretto in lana", "30 €"), ("Berretto misto", "50 €"), ("Guanti", "30 €"),
        ]),
        ("box", ("Non hai voglia di partecipare ma vorresti un capo personalizzato?",
                 "Come una t-shirt, un berretto o una borsa? Scrivimi per acquistare il tuo pezzo unico: lo realizzerò io per te, a mano, secondo le tue indicazioni.")),
        ("cta", [("PRENOTA O SCRIVIMI PER INFO", "WHATSAPP", "primary"), ("GUARDA IL CALENDARIO", "calendario.html", "ghost")]),
    ],
}

PAGINE["ricamo-su-foto"] = {
    "titolo": "Ricama la tua foto", "occhiello": "A6 · Corsi e workshop",
    "h1": "RICAMA LA TUA FOTO", "colore": "viola", "icona": "foto",
    "seo": "Workshop a Bologna per ricamare a mano sopra le tue fotografie con fili colorati.",
    "lead": "Uno scatto a cui tieni molto può essere valorizzato e reso ancor più speciale decorandolo e ricamandoci sopra a mano fili colorati. Ti stupirai del bellissimo risultato! Adatto agli adulti e ai bambini dagli 8 anni.",
    "blocchi": [
        ("info", [
            ("Durata", "2 ore"),
            ("Quando", "27 settembre 2026 e 15 ottobre 2026"),
            ("Dove", "Regina Coolors, Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "10"),
            ("Prezzo", "35 € a persona"),
        ]),
        ("cta", [("PRENOTA", "WHATSAPP", "primary"), ("GUARDA IL CALENDARIO", "calendario.html", "ghost")]),
    ],
}

PAGINE["biglietti-auguri"] = {
    "titolo": "Biglietti d’auguri", "occhiello": "A7 · Corsi e workshop",
    "h1": "BIGLIETTI D’AUGURI RICAMATI A MANO", "colore": "salvia", "icona": "biglietto",
    "seo": "Workshop a Bologna: biglietti d’auguri traforati e ricamati a mano.",
    "lead": "Trasformiamo assieme cartoncini colorati in biglietti d’auguri unici e personalizzati, traforandoli e ricamandoli a mano. Super rilassante e dal risultato wow! Adatto agli adulti e ai bambini dai 10 anni.",
    "blocchi": [
        ("info", [
            ("Durata", "2 ore"),
            ("Quando", "Date in definizione: scrivimi per essere avvisato appena escono"),
            ("Dove", "Regina Coolors, Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "10"),
            ("Prezzo", "35 € a persona"),
        ]),
        ("cta", [("SCRIVIMI PER LE DATE", "WHATSAPP", "primary")]),
    ],
}

PAGINE["fluffy-flowers"] = {
    "titolo": "Fluffy flowers", "occhiello": "A8 · Corsi e workshop",
    "h1": "FLUFFY FLOWERS", "colore": "giallo", "icona": "fiore",
    "seo": "Workshop fluffy flowers a Bologna: fiori di velluto modellati a mano.",
    "lead": "Impara la tecnica per creare differenti tipologie di fiori modellando a mano soffici bastoncini di velluto e crea un piccolo bouquet colorato. Questa tecnica crea dipendenza! Adatto agli adulti e ai bambini dagli 8 anni.",
    "blocchi": [
        ("info", [
            ("Durata", "2 ore"),
            ("Quando", "12 ottobre 2026"),
            ("Dove", "Regina Coolors, Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "10"),
            ("Prezzo", "35 € a persona"),
        ]),
        ("cta", [("PRENOTA", "WHATSAPP", "primary"), ("GUARDA IL CALENDARIO", "calendario.html", "ghost")]),
    ],
}

PAGINE["coroncine-di-fiori"] = {
    "titolo": "Coroncine di fiori", "occhiello": "A9 · Corsi e workshop",
    "h1": "CORONCINE DI FIORI", "colore": "salvia", "icona": "corona",
    "seo": "Workshop a Bologna per realizzare coroncine di fiori con una esperta fiorista.",
    "lead": "Con l’aiuto di una esperta fiorista apprenderemo come si intreccia e si realizza una coroncina di fiori, da conservare come decorazione o da indossare: un’esperienza meravigliosa, adatta agli adulti o ai bambini accompagnati.",
    "blocchi": [
        ("info", [
            ("Durata", "2 ore"),
            ("Quando", "Date in definizione: scrivimi per essere avvisato appena escono"),
            ("Dove", "Regina Coolors, Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "10"),
            ("Prezzo", "Su richiesta"),
        ]),
        ("cta", [("SCRIVIMI PER INFO E DATE", "WHATSAPP", "primary")]),
    ],
}

# --------------------------------------------------------------- eventi privati
PAGINE["eventi-privati"] = {
    "titolo": "Feste ed eventi privati", "occhiello": "C · Eventi privati",
    "h1": "FESTE ED EVENTI PRIVATI", "colore": "viola", "icona": "festa",
    "seo": "Feste ed eventi privati a Bologna: compleanni creativi, party per adulti, team building, addii al nubilato ed eventi aziendali.",
    "lead": "Il mio spazio di 60 mq si presta ad accogliere gruppi fino a 12 persone, adulti e bambini, per vivere esperienze esclusive in cui poter festeggiare, creare e stare insieme in maniera speciale e diversa dal solito.",
    "blocchi": [
        ("p", "Feste creative, team building, party, compleanni, addii al nubilato o al celibato sono soltanto alcuni degli eventi che posso organizzare, personalizzando ogni proposta in base alle esigenze e alla fascia d’età e plasmando allestimenti e temi di ciascun gruppo in base a gusto e interessi."),
        ("p", "Mettetevi alla prova con un’attività creativa appagante in un ambiente rilassato e realizzate insieme, ognuno secondo il proprio stile, un’opera unica."),
        ("cards", [
            ("COMPLEANNI CREATIVI", "Per bambini e ragazzi/e: la festa che non hanno mai fatto.", "compleanni-creativi.html"),
            ("PARTY CREATIVI ADULTI", "Una serata diversa, informale, unica ed esclusiva.", "party-adulti.html"),
            ("TEAM BUILDING", "Metti alla prova il tuo team creando qualcosa insieme.", "team-building.html"),
            ("ADDIO AL NUBILATO", "L’idea originale che stavate cercando.", "addio-al-nubilato.html"),
            ("EVENTI AZIENDALI", "Anche presso il vostro spazio privato o aziendale.", "eventi-aziendali.html"),
        ]),
        ("cta", [("PARLIAMONE SU WHATSAPP", "WHATSAPP", "primary"), ("CHIAMAMI", "TELEFONO", "ghost")]),
    ],
}

PAGINE["compleanni-creativi"] = {
    "titolo": "Compleanni creativi", "occhiello": "C1 · Eventi privati",
    "h1": "COMPLEANNI CREATIVI PER BAMBINI E RAGAZZI/E", "colore": "rosa", "icona": "festa",
    "seo": "Compleanni creativi per bambini e ragazzi a Bologna: feste personalizzate in piccoli gruppi con laboratorio creativo.",
    "lead": "Vorresti organizzare un compleanno speciale per tuo figlio o tua figlia a Bologna, ma non vuoi replicare le solite feste, o hai già sperimentato tutte le opzioni? Vorresti lasciare i bambini e i ragazzi in un ambiente tranquillo, sicuro ed esclusivo, ma non te la senti di ospitarli tutti a casa?",
    "blocchi": [
        ("p", "Se organizzare la festa di tuo figlio si sta rivelando uno stress, da ora non lo sarà più: lo spazio Regina Coolors è pensato anche per togliersi questi pensieri! Si organizzano feste creative personalizzate con piccoli gruppi, dove i bambini e i ragazzi potranno condividere momenti spensierati con i propri amici e realizzare, sotto la mia guida, piccole creazioni con le proprie mani, tra chiacchiere, musica e relax, in un ambiente piacevole."),
        ("p", "I partecipanti porteranno a casa non solo un gadget speciale fatto a mano da sé stessi, ma anche la soddisfazione di averlo realizzato con le proprie mani e una nuova competenza."),
        ("evidenza", "Non devi pensare a niente, tranne che a festeggiare: i materiali dei workshop sono compresi, le feste sono sempre diverse e personalizzabili nel tema e nel livello di difficoltà e, al termine dell’attività, l’oggetto creato rimarrà come ricordo a ciascuno da portare a casa."),
        ("p", "Il numero minimo di partecipanti è di 6 persone e il massimo di 10, ma se hai numeri differenti o preferisci realizzare l’evento in una location differente, sentiamoci: possiamo trovare una soluzione ad hoc."),
        ("h", "Scegli l’esperienza che preferisci per il party creativo"),
        ("elenco_lab", "BAMBINI"),
        ("nota", NB_VERSATILI),
        ("cta", [("ORGANIZZIAMO LA FESTA", "WHATSAPP", "primary"), ("CHIAMAMI", "TELEFONO", "ghost")]),
    ],
}

_EVENTI_ADULTI_BLOCCHI = [
    ("p", "Nello spazio Regina Coolors si organizzano attività creative personalizzate con piccoli gruppi di adulti, dove poter rilassarsi e staccare la spina tra chiacchiere e risate mentre si realizza, con la mia guida, una creazione fatta a mano da portare a casa."),
    ("evidenza", "Non devi pensare a niente: i materiali sono sempre compresi, le attività sono sempre diverse e personalizzabili nel tema e nel livello di difficoltà e, al termine dell’esperienza, gli oggetti creati saranno tutti diversi e rimarranno come ricordo a ciascuno da portare a casa."),
    ("p", "Il numero minimo di partecipanti è di 6 persone e il massimo di 10, ma se hai esigenze diverse scrivimi per trovare una soluzione ad hoc, o per organizzare la tua esperienza presso il tuo spazio privato o aziendale."),
    ("h", "Scegli l’esperienza che preferisci"),
    ("elenco_lab", "ADULTI"),
    ("nota", NB_VERSATILI),
    ("cta", [("ORGANIZZIAMO L’EVENTO", "WHATSAPP", "primary"), ("CHIAMAMI", "TELEFONO", "ghost")]),
]

PAGINE["party-adulti"] = {
    "titolo": "Party creativi adulti", "occhiello": "C2 · Eventi privati",
    "h1": "PARTY CREATIVI PER ADULTI", "colore": "viola", "icona": "festa",
    "seo": "Party creativi per adulti a Bologna: una serata diversa in un ambiente informale ed esclusivo.",
    "lead": "Vorresti organizzare un evento per un’occasione speciale ma non trovi nulla di originale? Cerchi un’idea per festeggiare, o semplicemente vuoi trascorrere una serata diversa in un ambiente informale, piacevole, unico ed esclusivo?",
    "blocchi": _EVENTI_ADULTI_BLOCCHI,
}
PAGINE["team-building"] = {
    "titolo": "Team building", "occhiello": "C3 · Eventi privati",
    "h1": "TEAM BUILDING CREATIVO", "colore": "salvia", "icona": "gruppo",
    "seo": "Team building creativo a Bologna: attività manuali per squadre, anche presso la vostra sede.",
    "lead": "Vuoi mettere alla prova il tuo team fuori dalla solita sala riunioni? Un’attività creativa fatta insieme, con le mani, scioglie il ghiaccio meglio di qualunque presentazione: si lavora fianco a fianco, si ride e ognuno porta a casa qualcosa che ha fatto da sé.",
    "blocchi": _EVENTI_ADULTI_BLOCCHI,
}
PAGINE["addio-al-nubilato"] = {
    "titolo": "Addio al nubilato", "occhiello": "C4 · Eventi privati",
    "h1": "ADDIO AL NUBILATO (E AL CELIBATO)", "colore": "rosa", "icona": "festa",
    "seo": "Addio al nubilato creativo a Bologna: tufting, armocromia e laboratori per festeggiare in modo originale.",
    "lead": "Cerchi un’idea originale per l’addio al nubilato, che non sia la solita? Qui si festeggia creando: spazio riservato in via esclusiva, un’attività scelta da voi e un ricordo fatto a mano da portare a casa per ognuna delle partecipanti. Le più richieste sono il tufting e l’armocromia.",
    "blocchi": _EVENTI_ADULTI_BLOCCHI,
}
PAGINE["eventi-aziendali"] = {
    "titolo": "Eventi aziendali", "occhiello": "C5 · Eventi privati",
    "h1": "EVENTI AZIENDALI", "colore": "viola", "icona": "gruppo",
    "seo": "Eventi aziendali creativi a Bologna: laboratori su misura per aziende, anche in sede.",
    "lead": "Un regalo di Natale diverso, un momento di incontro tra colleghi, la presentazione di un progetto o semplicemente una serata da ricordare: le attività si personalizzano nel tema e nel livello di difficoltà e possono svolgersi anche presso il vostro spazio privato o aziendale.",
    "blocchi": _EVENTI_ADULTI_BLOCCHI,
}

# ------------------------------------------------------------- pagine singole
PAGINE["armocromia"] = {
    "titolo": "Armocromia", "occhiello": "D · Consulenza",
    "h1": "ARMOCROMIA", "colore": "viola", "icona": "palette",
    "seo": "Consulenza di armocromia a Bologna: scopri i colori che ti valorizzano, make up compreso.",
    "lead": "Questa esperienza è una vera e propria consulenza, che si svolge una sola volta nella vita e ti svolterà il look, make up compreso!",
    "blocchi": [
        ("p", "Scopriamo insieme, grazie al supporto dei drappi di stoffa colorata e sulla base delle teorie dell’armocromia, quali sono i colori in grado di valorizzarti e da prediligere quando fai shopping e scegli cosa indossare."),
        ("info", [
            ("Durata", "1 ora"),
            ("Quando", "Decidi tu! Le consulenze di armocromia si svolgono su appuntamento."),
            ("Dove", "Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "Si tratta di un’esperienza individuale o di coppia, ma posso accogliere anche un piccolo gruppo; è possibile partecipare con massimo 2 accompagnatori."),
            ("Prezzo", "120 € a persona, sconti a partire da 3 persone"),
        ]),
        ("box", ("Perché “Coolors”?",
                 "Il nome nasce proprio da qui: io sono un <b>inverno Cool</b> e ho una passione per i colori. [Leggi la mia storia](chi-sono.html)")),
        ("cta", [("PRENOTA LA CONSULENZA", "WHATSAPP", "primary"), ("REGALALA CON UNA GIFT CARD", "gift-card.html", "ghost")]),
    ],
}

PAGINE["sabato-creativo"] = {
    "titolo": "Sabato creativo", "occhiello": "E · Per i bambini",
    "h1": "SABATO CREATIVO", "colore": "salvia", "icona": "sabato",
    "seo": "Sabato creativo a Bologna: 2 ore di laboratorio creativo per bambini dai 5 ai 13 anni, ogni sabato mattina.",
    "lead": "Che sogno sarebbe avere 2 ore tutte per te il sabato mattina, per sbrigare commissioni, fare una colazione tra amiche, una piega dal parrucchiere o un giro per negozi? Ora puoi!",
    "blocchi": [
        ("p", "Se vuoi ritagliarti del tempo libero facendo felice anche tuo figlio, prenota il sabato mattina da Regina Coolors: ogni settimana un nuovo workshop creativo, su un tema sempre diverso, dove lasciarlo a divertirsi 2 ore in totale relax in compagnia di altri bimbi. I workshop a rotazione sono tantissimi, dalla pixel art al punch needle: scoprili di settimana in settimana!"),
        ("nota", "Questi laboratori sono versatili e adatti a essere svolti da diverse fasce d’età, ciascuno secondo le proprie competenze. Si attivano solo su prenotazione telefonica e solo alla presenza minima di 4 bambini, fino a un massimo di 10. Età 5-13 anni."),
        ("info", [
            ("Durata", "2 ore per slot"),
            ("Quando", "Tutti i sabati, 2 slot a scelta: dalle 9 alle 11 oppure dalle 11 alle 13"),
            ("Dove", "Regina Coolors, Via San Mamolo 39C, Bologna"),
            ("Posti disponibili", "Minimo 4, massimo 10 bambini in tutto per slot"),
            ("Prezzo", "30 € a bambino per ogni slot di 2 ore di laboratorio. Si può rimanere anche per due laboratori consecutivi, per un totale di 4 ore: in questo caso il prezzo sarà di 60 €. Sono previsti sconti per fratelli e sorelle e pacchetti per chi vuole venire più volte."),
        ]),
        ("nota", "Non si tratta di uno spazio di gioco libero né di un servizio di babysitting, ma di una mattinata creativa dove i bambini, seduti attorno a un tavolo, parteciperanno seguendo le mie indicazioni a uno o due workshop semplici, adatti a ogni sesso ed età."),
        ("cta", [("PRENOTA PER TELEFONO", "TELEFONO", "primary"), ("SCRIVIMI SU WHATSAPP", "WHATSAPP", "ghost")]),
    ],
}

PAGINE["pausa-creativa"] = {
    "titolo": "Pausa creativa", "occhiello": "F · Relax, creatività, nuove amicizie",
    "h1": "PAUSA CREATIVA", "colore": "giallo", "icona": "pausa",
    "seo": "Pausa creativa a Bologna: un’ora per personalizzare un capo o un accessorio, su appuntamento.",
    "lead": "Se hai voglia di ritagliarti un momento diverso, in un ambiente tranquillo e pieno di colori, prenota la pausa creativa che ti rimette al mondo!",
    "blocchi": [
        ("p", "Un’ora da vivere da sola o in compagnia, dove partendo da un oggetto basico darai vita a un pezzo unico ed esclusivo. Scegli tra cappellino, felpa, t-shirt, berretto, zainetto, borsa e pochette che ti metterò a disposizione e personalizzalo secondo il tuo gusto e stile con le tantissime decorazioni, strass e patch che applicheremo insieme! Alla fine ti porterai a casa una creazione mai vista prima."),
        ("p", "L’esperienza piace a tutti, adulti e bambini (questi ultimi dovranno partecipare con un accompagnatore adulto)."),
        ("info", [
            ("Durata", "Massimo 1 ora"),
            ("Quando", "Solo su appuntamento, secondo disponibilità"),
            ("Dove", "Regina Coolors, Via San Mamolo 39C, Bologna"),
            ("A chi è rivolta", "Bambini accompagnati e adulti"),
            ("Posti disponibili", "10"),
            ("Prezzo", "Variabile, a partire da 30 € fino a 80 € a persona, a seconda dell’oggetto creato e del materiale utilizzato"),
        ]),
        ("box", ("Anche in gruppo",
                 "Questa esperienza è molto versatile: può svolgersi in maniera guidata con un piccolo gruppo riservando lo spazio in via esclusiva (min 4 partecipanti), anche in occasione di un [evento privato](eventi-privati.html).")),
        ("cta", [("PRENOTA", "WHATSAPP", "primary")]),
    ],
}

PAGINE["tappeto-personalizzato"] = {
    "titolo": "Tappeto personalizzato", "occhiello": "R · Su misura",
    "h1": "ORDINA IL TUO TAPPETO PERSONALIZZATO", "colore": "rosa", "icona": "tappeto",
    "seo": "Tappeti e quadri in tufting su misura, realizzati a mano a Bologna da Regina Coolors.",
    "lead": "Apprezzi i pezzi unici fatti a mano ma non hai voglia di realizzarlo con le tue mani?",
    "blocchi": [
        ("p", "Se desideri un tappeto personalizzato solo tuo, o un quadro, scrivimi per acquistare il tuo pezzo unico realizzato a mano da me: lo progetteremo assieme, oppure ti indicherò io le proposte migliori e più adeguate al tuo ambiente."),
        ("evidenza", "Dimensione, forma, colori e disegno li scegli tu. Se preferisci invece realizzarlo con le tue mani, ti aspetto al [workshop di tufting](tufting.html)."),
        ("cta", [("SCRIVIMI PER UN PREVENTIVO", "WHATSAPP", "primary"), ("SCOPRI IL WORKSHOP DI TUFTING", "tufting.html", "ghost")]),
    ],
}

PAGINE["gift-card"] = {
    "titolo": "Gift card", "occhiello": "G · Idea regalo",
    "h1": "REGALA TEMPO PER CREARE", "colore": "giallo", "icona": "regalo",
    "seo": "Gift card Regina Coolors: regala un’esperienza creativa a Bologna, cartacea o digitale, valida un anno.",
    "lead": "Non il solito regalo, ma un’esperienza da vivere! Se sei alla ricerca di un’idea originale e indimenticabile per un bambino o un adulto, con la Gift Card Regina Coolors regali tempo di qualità e creatività.",
    "blocchi": [
        ("p", "Può essere <b>cartacea</b> (da ritirare personalmente in Via San Mamolo 39C) oppure posso inviartela in <b>formato digitale</b> in pochi secondi. Puoi regalare un’esperienza specifica oppure scegliere soltanto l’importo: chi la riceve deciderà quando venire e cosa creare tra le proposte a calendario."),
        ("p", "Le più amate in assoluto dagli adulti? [Tufting](tufting.html) e [armocromia](armocromia.html). Ma niente paura: potrai anche lasciar scegliere al festeggiato."),
        ("ul", [
            "Utilizzabile anche per partecipare a più esperienze creative differenti, fino a esaurimento dell’importo totale.",
            "Perfetta in occasione di compleanni, lauree, ricorrenze o semplicemente per sorprendere qualcuno a cui vuoi bene.",
            "Un regalo vincente, valido un anno, che stupisce chi lo riceve e di certo non finisce in un cassetto.",
        ]),
        ("evidenza", "Si crea, si vive e si ricorda."),
        ("cta", [("ACQUISTA LA GIFT CARD", "WHATSAPP", "primary"), ("CHIAMAMI", "TELEFONO", "ghost")]),
    ],
}

PAGINE["chi-sono"] = {
    "titolo": "Chi sono", "occhiello": "L · La storia",
    "h1": "CIAO, SONO REGINA", "colore": "rosa", "icona": "cuore",
    "seo": "Chi sono: Regina, fondatrice di Regina Coolors, lab creativo in via San Mamolo 39C a Bologna.",
    "lead": "Sono una mamma millennial cresciuta a dolcetti e creatività.",
    "blocchi": [
        ("p", "Mi occupo di esperienze creative e nel mio nuovo lab <b>Regina Coolors</b>, a Bologna, in via San Mamolo 39C, ho creato uno spazio speciale dedicato a chi ha voglia di staccare dalla routine, mettere in moto la creatività e concedersi qualche ora offline per sé."),
        ("p", "Qui organizzo workshop, corsi, compleanni ed eventi creativi per piccoli gruppi di adulti e bambini, dove poter partecipare soli, con gli amici o in famiglia: momenti per rallentare, imparare qualcosa di nuovo, rilassarsi, conoscere nuove tecniche e persone ma, soprattutto, divertirsi creando con le proprie mani."),
        ("p", "Tufting, ricamo, patch bar, decorazione, armocromia, calligrafia, laboratori floreali, punch needle, acquerello, fluid art, pixel art e tante altre tecniche da scoprire e sperimentare: il [calendario dei workshop e dei corsi](calendario.html) è online, ma il Lab può ospitare anche [eventi privati](eventi-privati.html) organizzati su misura, come e quando preferisci!"),
        ("p", "Regina Coolors è uno spazio comodo, intimo e curato, ideale anche per party, compleanni, addii al nubilato e al celibato e team building, dove poter festeggiare occasioni speciali trasformandole in un’esperienza creativa gratificante da condividere."),
        ("evidenza", "Non serve “essere creativi”, avere manualità o saper già fare qualcosa: si viene per provare, staccare, svagarsi e sorprendersi. Qui semplicemente si crea!"),
        ("cta", [("SCOPRI TUTTI I CORSI", "corsi.html", "primary"), ("SCRIVIMI PER PRENOTARE", "WHATSAPP", "ghost")]),
        ("hr", None),
        ("h", "Perché Regina Coolors e da dove nasce il progetto?"),
        ("p", "Fin da bambina ho respirato creatività, trascorrendo i pomeriggi a inventare insieme a mia mamma e a mia nonna, che mi hanno trasmesso le loro competenze e la loro passione, tra stoffe, macchine da cucire, mercerie, fili e gomitoli."),
        ("p", "Crescendo ho svolto studi classici e conseguito il titolo di avvocato, ma alla fine ho scelto di seguire quello che sentivo più mio, l’istinto creativo: così, dopo anni di esperienza nel mondo della moda, oggi sono qui a realizzare un sogno."),
        ("p", "A contraddistinguermi è sempre stata una grande curiosità e la voglia di imparare cose nuove, soprattutto tutto ciò che potevo creare da sola, con le mie mani. Così, nel tempo, ho ampliato i miei studi e, attraverso tanta pratica e diversi corsi di formazione, ho acquisito competenze in differenti discipline legate al mondo dell’handmade e dei colori, a cominciare dall’[armocromia](armocromia.html), da cui nasce il mio nome (<i>Coolors</i> perché io sono un inverno <i>Cool</i> e perché ho una passione per i colori)."),
        ("p", "A un certo punto, però, alla mia continua voglia di scoprire e imparare nuove tecniche si è aggiunto un desiderio ancora più forte: condividerle con gli altri."),
        ("p", "È proprio da questa esigenza che nasce questo spazio creativo: dalla voglia di mettere a disposizione ciò che ho imparato, trasmettere il valore delle arti manuali e creare un luogo piacevole in cui le persone possano concedersi il tempo di rallentare, allontanarsi per qualche ora dagli schermi e riscoprire il piacere di creare."),
        ("evidenza", "Perché lavorare con le proprie mani non significa soltanto realizzare qualcosa: significa prendersi del tempo per sé, sperimentare, imparare e provare quella soddisfazione speciale che nasce nel poter dire: “Questo l’ho fatto io.”"),
    ],
}

PAGINE["faq"] = {
    "titolo": "Domande frequenti", "occhiello": "FAQ",
    "h1": "DOMANDE FREQUENTI", "colore": "salvia", "icona": "domanda",
    "seo": "Domande frequenti sui workshop creativi di Regina Coolors a Bologna.",
    "lead": "Le domande che mi fanno più spesso. Se non trovi la tua, scrivimi: rispondo io.",
    "blocchi": [
        ("faq", [
            ("Vorresti provare un hobby creativo ma pensi di non avere manualità?",
             "Non serve avere già avuto esperienze o manualità: i workshop che propongo sono adatti ai principianti e, con il mio supporto, riuscirai a portare a termine l’attività e a creare un oggetto."),
            ("Non bastano i tutorial online per imparare?",
             "Beh, che dire? La risposta già la sai! Vivere un’esperienza di 2-3 ore in presenza, in uno spazio creativo curato e con il supporto live di una persona competente, non è esattamente lo stesso che guardare un video di 30 secondi sul telefono…"),
            ("Come prenotare un’esperienza?",
             "Basta scrivermi o chiamarmi al 366 4318918 e pagare la quota o un acconto per fermare il posto."),
            ("Quali modalità di pagamento sono disponibili?",
             "Carta, Bancomat, Bonifico, Satispay, PayPal."),
            ("Quali sono i termini per disdire una prenotazione?",
             "Li trovi tutti nella pagina [rimborsi e cancellazioni](rimborsi.html)."),
            ("Posso farmi accompagnare da qualcuno che non parteciperà al workshop?",
             "I workshop sono individuali e non è prevista la presenza di accompagnatori, salvo per i minori, in casi da concordare."),
            ("Non sai con chi venire?",
             "E che problema c’è? Vieni da sola e unisciti a un gruppo, dove avrai la possibilità di conoscere nuove persone e stare in compagnia!"),
            ("Quante persone puoi ospitare?",
             "Fino a un massimo di 12, ma la capienza varia a seconda dei workshop."),
            ("Quanto tempo durano le esperienze?",
             "Solitamente 2 o massimo 3 ore, ma dipende dall’attività."),
            ("Cosa è incluso nelle esperienze?", "Tutto!"),
            ("Posso scegliere il soggetto da realizzare?",
             "Certamente, purché sia in linea con le indicazioni fornite e sia adatto a una prima esperienza."),
            ("Accogli anche gruppi?",
             "Eccome! I workshop che propongo sono ideali per ritagliarsi un momento tra amici, colleghi, coppie o in famiglia."),
        ]),
        ("cta", [("SCRIVIMI SU WHATSAPP", "WHATSAPP", "primary")]),
    ],
}

PAGINE["rimborsi"] = {
    "titolo": "Rimborsi e cancellazioni", "occhiello": "Z · Condizioni",
    "h1": "RIMBORSI E CANCELLAZIONI", "colore": "viola", "icona": "documento",
    "seo": "Condizioni di prenotazione, rimborso e cancellazione dei workshop Regina Coolors.",
    "lead": "Diritto di rimborso.",
    "blocchi": [
        ("p", "Le prenotazioni si intendono confermate e definitive soltanto ad avvenuto pagamento dell’intera quota o dell’acconto (che varia a seconda dei workshop e verrà comunicato in sede di prenotazione)."),
        ("box", ("Nessun rimborso",
                 "In caso di rinuncia o mancata presentazione all’evento senza comunicazione, o con meno di 72 ore di preavviso, non sarà possibile ottenere alcun rimborso né lo spostamento ad altra data.")),
        ("box", ("Rimborso del 50% o spostamento ad altra data secondo disponibilità",
                 "Se la mancata partecipazione viene comunicata entro 72 ore prima dell’inizio del workshop.")),
        ("cta", [("HAI UN DUBBIO? SCRIVIMI", "WHATSAPP", "ghost")]),
    ],
}

PAGINE["contatti"] = {
    "titolo": "Contatti", "occhiello": "M · Dove trovarmi",
    "h1": "CONTATTI", "colore": "rosa", "icona": "telefono",
    "seo": "Contatti Regina Coolors: via San Mamolo 39C Bologna, telefono e WhatsApp 366 4318918.",
    "lead": "Regina Coolors, via San Mamolo 39C, Bologna. Per prenotare basta scrivermi o telefonarmi!",
    "blocchi": [
        ("contatti_griglia", None),
        ("h", "Scrivimi due righe"),
        ("p", "Compila i campi qui sotto: preparo io il messaggio, tu scegli se mandarmelo su WhatsApp o per e-mail."),
        ("modulo", None),
        ("h", "Dove sono"),
        ("mappa", None),
    ],
}

PAGINE["calendario"] = {
    "titolo": "Calendario", "occhiello": "B · Le date",
    "h1": "CALENDARIO", "colore": "salvia", "icona": "calendario",
    "seo": "Il calendario dei workshop creativi di Regina Coolors a Bologna.",
    "lead": "Tutti i prossimi appuntamenti in via San Mamolo 39C. I posti sono pochi per scelta: accolgo solo piccoli gruppi.",
    "blocchi": [
        ("calendario", None),
        ("nota", CALENDARIO_NOTA),
        ("cta", [("PRENOTA SU WHATSAPP", "WHATSAPP", "primary"), ("CHIAMAMI", "TELEFONO", "ghost")]),
    ],
}

# ------------------------------------------------------------ menu di navigazione
NAV = [
    ("Corsi e workshop", "corsi.html", [
        ("Tufting", "tufting.html"),
        ("Punch needle", "punch-needle.html"),
        ("Ricamo creativo", "ricamo-creativo.html"),
        ("Calligrafia", "calligrafia.html"),
        ("Patch bar", "patch-bar.html"),
        ("Ricama la tua foto", "ricamo-su-foto.html"),
        ("Biglietti d’auguri", "biglietti-auguri.html"),
        ("Fluffy flowers", "fluffy-flowers.html"),
        ("Coroncine di fiori", "coroncine-di-fiori.html"),
    ]),
    ("Calendario", "calendario.html", []),
    ("Feste ed eventi privati", "eventi-privati.html", [
        ("Compleanni creativi", "compleanni-creativi.html"),
        ("Party creativi adulti", "party-adulti.html"),
        ("Team building", "team-building.html"),
        ("Addio al nubilato", "addio-al-nubilato.html"),
        ("Eventi aziendali", "eventi-aziendali.html"),
    ]),
    ("Armocromia", "armocromia.html", []),
    ("Sabato creativo", "sabato-creativo.html", []),
    ("Gift card", "gift-card.html", []),
    ("Chi sono", "chi-sono.html", []),
    ("Contatti", "contatti.html", []),
    ("Pausa creativa", "pausa-creativa.html", []),
    ("Tappeto personalizzato", "tappeto-personalizzato.html", []),
]

PIE = [
    ("Chi sono", "chi-sono.html"), ("Contatti", "contatti.html"),
    ("Mappa", "MAPPA"), ("WhatsApp", "WHATSAPP"), ("Instagram", "INSTAGRAM"),
    ("Domande frequenti", "faq.html"), ("Rimborsi e cancellazioni", "rimborsi.html"),
]
