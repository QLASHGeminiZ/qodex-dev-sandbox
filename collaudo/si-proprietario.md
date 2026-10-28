# Qodex: consenso del proprietario per il collaudo sul sandbox

Questo documento registra il consenso del proprietario **Luca Pagano**, trasportato da QLASHY-Codex nelle forme di ADR-0255. QLASHY-Codex attua e trasporta il mandato; non e un operatore autorizzante e non firma un consenso proprio. Il seggio Claude che dispaccia non da il consenso del proprietario.

## Mandato e provenienza

Il 28 ottobre 2026 Luca ha scritto nella chat Codex `01a17e55-7843-79b2-9da5-39b7cf63c8f6`:

> Continua con Claude fino a rendere Qodex operativo su dev, con una PR di prova pubblicata e verificata. Aggiornami a collaudo concluso o se serve un mio intervento.

Prima comunicazione al seggio: **2026-10-28T02:10:28Z**, ora di trasporto successiva al messaggio, non ora attribuita al clic. Ricevuta canonica del percorso diretto: [QODEX-OPERATIVE-20261027-001 REV 2, deposito del destinatario](https://github.com/Qlash-IT/qlash-dev-knowledge/issues/486#issuecomment-6459019710), stato ricevuto il 28 ottobre alle 02:29:47Z. Prosegue la medesima esecuzione di [REV 1 / I-1246](https://github.com/Qlash-IT/qlash-dev-knowledge/issues/486#issuecomment-6454869145); non e un nuovo incarico o una seconda esecuzione.

Origine e fork sono la scelta gia confermata da Luca nella risposta personale al passaggio di configurazione. Luca ha riportato l'esito del suo deposito: «✅ item creato.» La [direttiva QODEX-GITHUB-TOKEN-20261027-001 REV 1 / I-1248](https://github.com/Qlash-IT/qlash-dev-knowledge/issues/487#issuecomment-6456379607) registra la risposta e gli esatti campi approvati; prima registrazione successiva alla risposta **2026-10-27T23:44Z**, non ora attribuita al clic. Non si attribuisce a Luca una formula «go» che non ha scritto. Nessun valore di credenziale e presente in questo documento.

| Ambito | Valore |
|---|---|
| Origine di staging | `QLASHGeminiZ/qodex-dev-sandbox` |
| Fork dell'agente | `QLASH-Qodex/qodex-dev-sandbox` |
| Account dell'agente | `QLASH-Qodex` |
| Dispaccia | `codex-agy-orcb`, GitHub `Qlash-Ramon` |
| Rivede le PR dell'agente | `flotta`, GitHub `QLASHGeminiZ`, distinto dal dispacciante |
| Scadenza del mandato | `2026-12-05T23:59:00Z`, senza rinnovo del contratto |

## I due testi ammessi

I testi firmati dal seggio sono fissati al [commit KB caa0e20ae6fff3f6c6b3f0a93f680343dde2a913](https://github.com/Qlash-IT/qlash-dev-knowledge/tree/caa0e20ae6fff3f6c6b3f0a93f680343dde2a913/fronti/codex-agy/collaudo). Gli hash e il piccolo incarico di sviluppo sono la concretizzazione tecnica del mandato da parte degli agenti, **non parole attribuite a Luca**.

| Testo | SHA256 | File ammessi |
|---|---|---|
| `dispatch-di-prova-3.txt` | `6f9febf06b0b4a1aaa66f4c27dd85740d8b34f9bbbecb47fb3a66a0f563db82e` | solo `collaudo/qodex-<data>.md`, una riga di collaudo |
| `f6-normalise-display-name.txt` | `5f3a563b430cb7472bded5fd9835c2d5b17f6d643de988a28e33a76f6cf0ae7e` | solo `display_name.py` e `tests/test_display_name.py` |

Il primo testo usa il ramo locale `codex/qodex-collaudo-<data>`; il secondo `codex/qodex-f6-collapse-whitespace`. L'F6 comprime le sequenze interne di whitespace, preserva gli altri caratteri Unicode e il rifiuto degli input non testuali, con i casi di regressione specificati nel testo firmato.

Il consenso vale soltanto per questi due testi e questi hash. Ogni altro incarico, repository o file resta fuori. Se cambia un byte, occorrono riconciliazione, rifirma del testo e aggiornamento del consenso prima dell'invio.

## Ordine e verifica

- Il dispatch di prova numero 3 parte soltanto dopo i passi 1-11 di `services/dev-a/collaudo.md` in Qovh.
- L'F6 parte soltanto con **A1-A7 verdi**, accompagnati dalla tabella delle misure. Un criterio non misurato non e verde.
- Questo documento non anticipa alcun gate, login, avvio di sessione o pubblicazione.
- Qodex committa localmente; soltanto l'helper revisionato pubblica dal fork e apre la PR. Qodex non ha scrittura diretta sull'origine.
- La review Claude e i controlli GitHub rimangono necessari. Il revisore non coincide con chi dispaccia.
- Prima di ogni invio il seggio rilegge questo documento su `main` e confronta entrambi gli hash con i testi firmati.

Questa PR documentale e preparazione del collaudo da parte dell'operatore: **non e la PR autentica di prova attribuita a Qodex**, ne prova che il collaudo sia gia passato.
