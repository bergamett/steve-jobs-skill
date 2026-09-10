<p align="center">
  <img src="assets/hero.svg" alt="Ask Steve — una skill per Claude Code che ragiona come Steve Jobs" width="820">
</p>

<h1 align="center">Ask Steve</h1>

<p align="center"><strong>Non un chatbot su Steve Jobs. Una revisione alla Steve Jobs.</strong></p>

<p align="center"><a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a> · <a href="README.it.md">Italiano</a></p>

Ogni altro prompt su Steve Jobs risponde alla domanda *"chi era Steve Jobs?"*

Non serve a nessuno. Serve l'altra cosa: qualcuno che guardi quello che hai fatto davvero, oggi pomeriggio, e dica la frase che stai evitando.

La skill legge i tuoi file, esegue il tuo comando, conta i passi da `git clone` al primo momento in cui qualcosa funziona, e poi decide: il verdetto, l'intuizione che c'è sotto, cosa tagliare, la prossima mossa, e la frase che lo vende.

Ecco la skill puntata su questa stessa pagina, prima che venisse sistemata:

```
> /steve verdict README.md

Mode: verdict · this repo's own README

Verdict. Not yet. Il README più disciplinato sul tema del feedback onesto
si dimostra interamente su un prodotto che non esiste. Metti al suo posto
il verdetto su se stesso e diventa great.

What's wrong.
1. La prova è inventata, ed esiste in tre versioni diverse. TaskFlow Pro è
   fittizio e il README non lo dice mai. Il blocco qui, il file di esempio
   e il sito sono tre testi diversi della stessa esecuzione, tutti
   etichettati come output reale. Chi ne apre due smette di credere al terzo.
2. Undici titoli, milleseicento parole, e dici tutto due volte.
3. SETUP.md è nella root del repo. L'ultimo passo dice "esegui la skill sul
   README di questo repository e sistema quello che dice". Hai pubblicato
   il biglietto che dice che la cosa non è finita.

What Steve would say. (imagined) "Hai costruito una macchina per dire alla
gente la verità sul loro lavoro, e poi l'hai dimostrata su un'azienda
inventata."
```

Tutte e tre le osservazioni erano vere. Sono state corrette nel commit successivo; la revisione completa e le modifiche che ha causato sono in [`examples/self-verdict.md`](examples/self-verdict.md). Questo è l'intero argomento, ed è costato un comando.

## Installazione

**Claude Code**:

```
/plugin marketplace add bergamett/steve-jobs-skill
/plugin install steve@steve
```

**Qualsiasi agente che legge SKILL.md** (Claude Code, Codex, Cursor, Gemini CLI, OpenCode):

```
npx skills add bergamett/steve-jobs-skill
```

**A mano**:

```
git clone https://github.com/bergamett/steve-jobs-skill
cp -r steve-jobs-skill/skills/steve ~/.claude/skills/steve
```

**In una finestra di chat**, dove non c'è una cartella da leggere: incolla [`dist/steve-full.md`](dist/steve-full.md), la stessa skill appiattita in un solo file.

Poi scrivi `/steve` e quello che ti preoccupa. Senza modalità, ne sceglie una e ti dice quale.

| Modalità | La domanda a cui risponde | Prova |
|---|---|---|
| **verdict** | Cosa direbbe Steve di questo? | `/steve verdict README.md` |
| **why** | Qual è l'intuizione che c'è sotto? | `/steve why are we building this` |
| **cut** | Quali sette cancelliamo? | `/steve cut ROADMAP.md` |
| **next** | Qual è l'unica scommessa, e cosa costa? | `/steve next` |
| **pitch** | Come lo dico in una frase? | `/steve pitch` |
| **email** | Come rispondo senza mentire e senza perderli? | `/steve email` |

Avevamo undici modalità. Ne abbiamo cancellate cinque.

## Cosa la rende diversa

**Tiene in mano la cosa.** Legge i file, esegue la CLI, conta i passi da `git clone` al primo momento utile. Non recensisce mai una descrizione del prodotto. Gli input su cui è stata puntata sono [nel repository](examples/inputs/), così puoi eseguire gli stessi comandi.

**Finisce con una riscrittura.** Una critica che si ferma alla critica è uno sfottò. Ogni risposta restituisce il nuovo titolo, le tre funzioni che restano, il messaggio di errore che adesso dice cosa fare.

**Ogni citazione ha una fonte.** [`quotes.md`](skills/steve/references/quotes.md) riporta luogo, anno, link e un indicatore di affidabilità per tutte le settanta righe, più una tabella delle [frasi famose che non ha mai detto](skills/steve/references/quotes.md#14-what-people-say-he-said-and-what-he-actually-said). Un [job di integrazione continua](scripts/check_sources.py) fa fallire la build se una citazione compare senza fonte. Quando la skill scrive cosa *direbbe* della tua cosa, lo etichetta come immaginato.

**Sa dove aveva torto.** Il Cube, MobileMe, il mouse a disco, "i tablet da sette pollici nascono morti". [`failures.md`](skills/steve/references/failures.md) elenca anche quando smettere di ascoltarlo: accessibilità, domini regolamentati o critici per la sicurezza, e ogni volta che hai dati d'uso reali che contraddicono l'intuizione.

**È breve, e attacca il lavoro.** Una schermata. Prima il verdetto. Niente sulla persona che ha fatto la cosa. Lui poteva essere crudele; questa no.

È per il pomeriggio in cui hai trenta funzioni e nessuna frase, in cui tutti hanno chiesto qualcosa e hai detto sì a tutti, in cui la tua landing page ha senso per te e per nessun altro, in cui sai cosa costruire dopo ma non cosa smettere, in cui qualcuno vuole una funzione e non trovi le parole per dire no, e in cui fissi lo stesso schermo da otto mesi e non lo vedi più.

Non è per curiosità, biografia o "in che anno ha fatto X". Lo fanno altre skill. E non finge di sapere cosa avrebbe pensato di qualsiasi cosa dopo ottobre 2011.

## Esempi

Output reali. I due input fittizi sono nel repository, etichettati come tali.

| | |
|---|---|
| [**Il README di questo repository**](examples/self-verdict.md) | la revisione qui sopra, completa, con le modifiche che ha causato |
| [**Un README gonfio**](examples/readme-verdict.md) | quindici funzioni, nove passi di installazione, nessuna frase che dica cos'è |
| [**Una roadmap da dodici voci**](examples/roadmap-cut.md) | due persone, 900 clienti paganti, e ogni voce ha qualcuno che la chiede |
| [**Un tagline che nessuno capisce**](examples/pitch-devtool.md) | otto mesi di lavoro che non si riescono a spiegare a un meetup |
| [**"Una funzione, non un prodotto"**](examples/why-insight.md) | l'intuizione sotto un'idea che tutti liquidano |
| [**Un cliente che offre soldi veri**](examples/email-feature-request.md) | per un port che lo sviluppatore non vuole fare |
| [**Un prodotto in stallo**](examples/next-move.md) | 4.000 utenti gratuiti, zero ricavi, tre funzioni in programma |
| [**La stessa domanda, senza la skill**](examples/_baseline-no-skill.md) | da leggere insieme al precedente |

## Come funziona

```
skills/steve/
├── SKILL.md                    123 righe: sei modalità, il ciclo, le regole, la forma di una risposta
└── references/
    ├── playbooks/              uno per modalità: passi, template di output, trappole
    ├── quotes.md               70 citazioni: luogo, anno, link, affidabilità
    ├── principles.md           le quattordici mosse documentate e le prove di ciascuna
    ├── episodes.md             decisioni reali come template riutilizzabili
    ├── voice.md                come parlava, e le parole da non usare mai
    └── failures.md             dove aveva torto, e quando non ascoltarlo
```

`SKILL.md` contiene il ciclo in otto passi che la skill esegue sul tuo lavoro e resta piccolo, così caricarlo costa quasi niente. I quattordici principi dietro quei passi, le citazioni e gli episodi vengono letti solo quando la modalità in uso ne ha bisogno. Questa è tutta l'architettura.

Contributi benvenuti, con [una regola](CONTRIBUTING.md): nessuna citazione senza fonte.

## Crediti, e cosa questo non è

Costruito da materiale pubblico: il discorso di Stanford, la "Lost Interview" del 1995, la sessione di chiusura del WWDC 1997, il discorso interno Think Different del 1997, le interviste a Playboy e Wired, i keynote, "Thoughts on Flash", le interviste a Fortune e All Things Digital, *Make Something Wonderful* dello Steve Jobs Archive, folklore.org di Andy Hertzfeld, il tributo di Jony Ive alla commemorazione, e il resoconto di Walter Isaacson sulle lezioni di leadership. Ogni fonte è linkata in [`quotes.md`](skills/steve/references/quotes.md) e [`episodes.md`](skills/steve/references/episodes.md).

Questo progetto non è affiliato, approvato o collegato ad Apple Inc., allo Steve Jobs Archive o agli eredi di Steve Jobs. È una lente per guardare il proprio lavoro, costruita da ciò che lui ha detto in pubblico. Non è lui, non lo evoca, e non pretende di sapere cosa avrebbe pensato. Dove scrive con la sua voce, lo dice.

Licenza MIT. Vedi [LICENSE](LICENSE).
