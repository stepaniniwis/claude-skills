---
name: supervisor-review
description: >
  Simuliert das Review der drei PhD-Betreuerinnen (MJS = Retha Scheepers,
  JC = Jenna Campton, RB = Renee Barnes) auf Basis von 152 realen Kommentaren
  am Confirmation-Dokument (v7, Jan 2025). Anwenden auf jeden Thesis-Entwurf
  VOR der Abgabe an die Betreuer: Kapitel, Abschnitte, Methodenteile.
  Trigger: "supervisor review", "Betreuer-Check", "wie würde Retha das lesen",
  Einreichen eines Kapitel-Drafts.
---

# Supervisor-Review-Protokoll

Prüfe den Text in drei Durchgängen — je Perspektive einmal. Melde Befunde
mit Fundstelle + konkretem Umformulierungsvorschlag, nicht nur Diagnose.

## Durchgang 1 — MJS-Perspektive (Makro: Argument, Redundanz, Präzision)
- [ ] REDUNDANZ (häufigster Kritikpunkt): Wird ein Konzept/eine Quelle mehr als
      einmal definiert oder erklärt? ("Is this the 4th or 7th time…") Jede
      Definition genau einmal; bei jedem Absatz fragen: Was ist hier NEU?
- [ ] GAP-LOGIK: Hält die behauptete Forschungslücke einem "So this has been
      done already?" stand? Lücke aus der vorgestellten Literatur ableiten,
      nicht behaupten.
- [ ] ARGUMENT ZUERST: Kernaussage an den Abschnittsanfang, Beispiele als
      Beleg dahinter. Kein "In summary" mitten im Abschnitt.
- [ ] BEGRIFFSPRÄZISION: Container-Wörter (engagement, dynamics, resources,
      framework, strategic) konkretisieren oder streichen. Terminologie
      dokumentweit konsistent; keine internen Widersprüche (dynamisch vs. statisch).
- [ ] KONZEPT-KORREKTHEIT: Fachaussagen gegen kanonische Definitionen prüfen
      (z.B. Entrepreneurship = Innovation + Proaktivität + Risiko, nicht nur Innovation).
- [ ] PUBLIKUM: Leser sind PhD-Examiner — Grundlagen nicht lehrbuchartig
      erklären, nicht über-erklären.
- [ ] LLM-SPRACHE: KI-typische Wörter/Floskeln entfernen (MJS flaggt diese explizit).
- [ ] ABBILDUNGEN: In Druckgröße lesbar? Notwendig? Ggf. auf Kernaussage reduzieren.
- [ ] FORM: Australian English, Harvard-Referenzen, Seitenzahl bei wörtlichen
      Zitaten, Referenz direkt hinter Autorennennung.

## Durchgang 2 — JC-Perspektive (Mikro: Absatz- und Satzhandwerk)
- [ ] TOPIC SENTENCE: Jeder Absatz beginnt mit einem Satz, der beantwortet,
      warum dieses Thema hier steht.
- [ ] ABSCHLUSS: Abschnitte enden mit zusammenfassendem/überleitendem Satz.
- [ ] RUN-ON-TEST: Satz laut lesen — wo man Luft holen muss, gehört ein Punkt hin.
      Keine Ein-Satz-Absätze, keine Satzanfänge mit "And".
- [ ] INLINE-DEFINITION: Fachbegriffe bei Erstnennung in einem Halbsatz definieren.
- [ ] ABSOLUTE CLAIMS ENTSCHÄRFEN: "no research" → "limited research" (kann
      sich bis zur Abgabe ändern).
- [ ] QUELLEN-AKTUALITÄT: Sind die Referenzen des Abschnitts aktuell? Gibt es
      neuere Kritik/Reviews mit "call for research", der die eigene Lücke stützt?
- [ ] PLATZIERUNG: Passt der Abschnitt an diese Stelle oder gehört er
      verschoben (vgl. vereinbarte Kapitelstruktur)?

## Durchgang 3 — RB-Perspektive (Methoden, v.a. Qualitativ/Ethnographie)
- [ ] ROLLENTERMINOLOGIE: Beschreibt der Text exakt die geplante Forscherrolle
      (participant as observer vs. observer as participant — interagieren oder
      nur beobachten)?
- [ ] NUR GEPLANTES NENNEN: Jedes erwähnte Verfahren wird wirklich
      durchgeführt — sonst streichen ("Do you plan on doing this? If not
      then don't include").
- [ ] VOLLSTÄNDIGKEIT: Stichprobengröße, Auswahlkriterien, Varianz der
      Perspektiven explizit beantwortet.
- [ ] SYNTHESE: Konvergierende Studien in einem Satz mit Sammelzitat bündeln,
      nicht ein Satz pro Studie.
- [ ] THEORIE-SPRACHE: Theorien "erklären/informieren" Phänomene, sie
      "fördern" nichts.

## Output-Format

Pro Befund: [Perspektive] [Muster] Fundstelle → Zitat der Stelle → Fix-Vorschlag.
Abschließend: die 3 wichtigsten Baustellen priorisiert. Positiv-Signale
(klare Diagramme, fokussierte Absätze, explizite Kriterienlisten) benennen.

## Herkunft und Grenzen

Destilliert aus 164 Kommentar-Threads am Dokument
"PhD_transition_combined_work_so_far_070125_v7_1701_MJS_JC-4"
(111 MJS, 23 JC, 18 RB, Rest Eigen-/Systemkommentare). Momentaufnahme des
Confirmation-Stadiums (Kap. 1–3); Muster zu Ergebnis-/Diskussionskapiteln
fehlen naturgemäß. Gewichte bei späteren Feedbackrunden neu prüfen und den
Skill fortschreiben.
