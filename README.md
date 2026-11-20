# Love Pet · Self check-in

Prototipo dell'app di self check-in per l'accoglienza della Clinica Veterinaria Love Pet (Via Mosca 6, Napoli).
Il cliente registra l'arrivo da un tablet in pochi minuti, vede il proprio codice di urgenza e segue l'attesa dal telefono; l'accoglienza vede la coda in tempo reale, gli allarmi e la soddisfazione.

**Online:** https://love-pet-checkin.netlify.app (escluso dai motori di ricerca)

## Le tre viste

| Indirizzo | Chi la usa | Cosa fa |
|---|---|---|
| `#totem` | Cliente, sul tablet all'ingresso | Segnali d'allarme, dati del proprietario, dati dell'animale, sintomi, riepilogo con codice colore e numero |
| `#accoglienza` | Personale, sul PC | Coda per urgenza e arrivo, minuti di attesa, allarme sulle emergenze, cambio codice con un tocco, attesa media e soddisfazione |
| `#telefono` | Cliente, dal link WhatsApp o dal QR | Percorso Arrivo → Triage → Sala d'attesa → Visita, "Sta peggiorando?", sondaggio a faccine |

Dati raccolti: nome, cognome, cellulare, email e indirizzo del proprietario; specie, nome, età, sesso, sterilizzazione e sintomi dell'animale. Chi è già cliente scrive il cellulare e il resto si compila da solo; chi ha l'appuntamento inserisce solo il cellulare.

## Provarlo

Apri `prototipo-checkin.html` nel browser, oppure il sito online. Numeri di prova:

- `333 111 2233` e `340 222 4455`: clienti con appuntamento oggi
- `347 555 0101`: cliente già registrato, senza appuntamento

I dati sono di esempio e restano nel browser di chi prova: non viene inviato nulla. Il pulsante **Ripristina esempio** riporta tutto allo stato iniziale.

## Triage a tre colori

Il codice proposto dal totem è organizzativo: la valutazione clinica spetta sempre al medico veterinario, che lo conferma o lo cambia dall'accoglienza.

- **Rosso**, emergenza: uno dei segnali d'allarme (respira a fatica, perde molto sangue, convulsioni, collasso, sospetto avvelenamento, trauma, pancia gonfia con conati a vuoto, non riesce a urinare, parto difficile, colpo di calore) oppure il tasto Emergenza. Parte l'allarme all'accoglienza.
- **Giallo**, urgenza: sangue nel vomito o nelle feci, ferita o morso, occhi rossi o chiusi.
- **Verde**, non urgente: gli altri motivi e gli appuntamenti senza novità.
- Il verde diventa giallo se il gatto non mangia da più di un giorno; se c'è vomito, diarrea o inappetenza in un cucciolo sotto 1 anno o in un anziano da 12 anni in su; se il proprietario lo vede molto giù, oppure giù con sintomi digestivi.

Le regole sono da validare con il direttore sanitario. Testi, colori e tono seguono la skill in `.claude/skills/landing-accoglienza-triage-cliente`.

## Struttura

- `prototipo-checkin.html`: il prototipo, un unico file (è anche la versione pubblicata come artifact su claude.ai)
- `build-deploy.py`: genera la cartella `deploy/` con la pagina completa per Netlify
- `.claude/skills/landing-accoglienza-triage-cliente/SKILL.md`: regole su testi per i clienti, triage e grafica

## Pubblicare su Netlify

1. `python3 build-deploy.py`
2. Pubblica la cartella `deploy/` sul sito Netlify `love-pet-checkin` (team Brave Vet Business) dal connettore Netlify, operazione `deploy-site`.

## Limiti del prototipo

- Nessun database: tablet, PC e telefono non condividono i dati. Per vedere il passaggio dal totem all'accoglienza usa le due viste sullo stesso browser.
- I messaggi WhatsApp e il link alla recensione Google sono simulati.
- Nessun collegamento al gestionale della clinica.

## Da decidere dopo il test

Gestionale da collegare, validazione del triage, database condiviso, hardware (tablet e supporto), logo.
