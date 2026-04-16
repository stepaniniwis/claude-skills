---
name: qualitative-coder
description: >
  Claude als unabhaengiger qualitativer Coder fuer Interviewtranskripte.
  Gioia, Thematic Analysis, Template Analysis. Codiert Transkripte systematisch
  mit Anti-Glaettung, Zitatverifikation, Segmentfilter, und Sprechertrennung.
  Vier Modi: CODE (codiert ein Transkript), COMPARE (vergleicht Claude-Coding
  mit menschlichem Coding), EXPLORE (explorativer Durchlauf), AUDIT (prueft
  eigenes Coding auf Glaettung, Interviewer-Kontamination, Zitat-Integritaet).
  Trigger: "code dieses Interview", "codiere Transkript", "qualitatives Coding",
  "Gioia Coding", "3. Coder", "dritter Coder", "code als unabhaengiger Coder",
  "vergleiche Codings", "pruefe das Coding".
---

# Qualitative Coder

Claude als unabhaengiger 3. Coder fuer qualitative Interviewdaten.

## Kernproblem das dieser Skill loest

Claude sieht Cross-Case-Pattern besser als Menschen weil es alle Transkripte gleichzeitig verarbeitet. Aber Claude hat drei systematische Fehler beim Coding:

1. **Glaettung:** Widersprueche werden aufgeloest statt dokumentiert. Claude bevorzugt kohaerente Narrative und presst ambivalente Aussagen in eindeutige Codes.
2. **Zitat-Halluzination:** Claude veraendert Wortlaut, verschiebt Satzhaeflten, oder attribuiert Interviewer-Aussagen an Teilnehmer.
3. **Ueber-Coding:** Claude codiert alles — auch Smalltalk, organisatorische Fragen, und Interviewer-Redeanteile.

Dieser Skill erzwingt Gegenmassnahmen fuer alle drei.

---

## Modus-Erkennung

| Input | Modus |
|---|---|
| Transkript + Codebook/Instruktionen | → CODE |
| Transkript ohne Codebook | → CODE (induktiv) |
| Claude-Coding + menschliches Coding | → COMPARE |
| "Vergleiche die Codings" | → COMPARE |
| Transkript + "was siehst du?" | → EXPLORE (explorativer Durchlauf, keine formale Codierung) |
| "pruefe das Coding" / "Audit" | → AUDIT (Selbstkontrolle nach erstem Durchlauf) |

---

## Modus CODE

### Schritt 0: Segment-Filter (IMMER ZUERST)

Bevor ein einziges Segment codiert wird, filtere das gesamte Transkript:

**AUSSCHLIESSEN — niemals codieren:**
- Interviewer-Fragen und -Nachfragen (alles was der/die Interviewende sagt)
- Interviewer-Kommentare, Bestaetigunslaute ("mhm", "ja genau", "interessant")
- Begruesssung und Verabschiedung
- Organisatorisches ("Soll ich das Mikro naeher stellen?", "Wie lange haben wir noch?")
- Smalltalk vor/nach dem Interview
- Reine Wiederholungen der Interviewfrage durch den Teilnehmer
- Unverstaendliche Passagen [unverstaendlich] ohne interpretierbaren Inhalt

**EINSCHLIESSEN — nur Teilnehmer-Aussagen:**
- Inhaltliche Antworten des/der Teilnehmenden
- Spontane Ergaenzungen und Abschweifungen (diese sind oft die reichsten Daten)
- Emotionale Reaktionen die inhaltlich kodierbar sind
- Nachfragen des Teilnehmers die seine/ihre Perspektive offenbaren

**Output nach Schritt 0:** Anzahl Gesamtsegmente, Anzahl ausgeschlossene Segmente, Anzahl codierbare Segmente. Dieses Verhaeltnis dokumentieren.

### Schritt 1: Coding-Modus bestimmen

| Ansatz | Was Claude bekommt | Was Claude tut |
|---|---|---|
| **Deduktiv** | Codebook mit Codes, Definitionen, Ankerbeispiele | Ordnet Segmente existierenden Codes zu |
| **Induktiv** | Nur die Forschungsfrage oder das Thema | Entwickelt First-Order Codes aus den Daten |
| **Gioia** | Forschungsfrage + ggf. theoretischer Rahmen | First-Order Concepts (nah am Wortlaut) → Second-Order Themes → Aggregate Dimensions |

### Schritt 2: Coding durchfuehren

Fuer jedes codierbare Segment:

| Feld | Inhalt |
|---|---|
| **Segment-ID** | Fortlaufende Nummer (S001, S002, ...) |
| **Zeile** | Zeilennummer(n) im Transkript |
| **Sprecher** | Teilnehmer (IMMER). Niemals Interviewer. |
| **Zitat** | WOERTLICH aus dem Transkript kopiert. Kein Wort aendern, kein Satz umstellen, keine Grammatik korrigieren. Auslassungen mit [...] markieren. PFLICHT — kein Segment ohne direktes Zitat. Paraphrasen sind NICHT erlaubt als Ersatz. |
| **Code** | First-Order Code (bei Gioia) oder Codebook-Code (bei deduktiv) |
| **Code-Typ** | in-vivo / descriptive / process / value / emotion / evaluative |
| **Begruendung** | Warum dieses Segment diesen Code bekommt. Maximal 1-2 Saetze. Evidenzgebunden, nicht interpretativ. |
| **Konfidenz** | high / medium / low |
| **Flags** | prompted / spontan / ambiguous / contradictory / weak-evidence / [leer wenn keine] |

**Code-Typen erklaert:**

| Typ | Was er erfasst | Beispiel |
|---|---|---|
| **in-vivo** | Wortlaut des Teilnehmers wird zum Code | "Ich bin so ein Zwitter" → Code: Zwitter |
| **descriptive** | Beschreibt was gesagt wird | Beschreibt Tagesablauf → Code: Tagesstruktur |
| **process** | Beschreibt eine Handlung oder Veraenderung | "Ich habe dann angefangen..." → Code: Uebergang zum Gruenden |
| **value** | Drueckt einen Wert oder eine Ueberzeugung aus | "Freiheit ist mir wichtiger als Sicherheit" → Code: Freiheit-ueber-Sicherheit |
| **emotion** | Drueckt ein Gefuehl aus | "Das macht mich wahnsinnig" → Code: Frustration-mit-Doppelbelastung |
| **evaluative** | Bewertet etwas | "Das war die beste Entscheidung" → Code: Positive-Bewertung-Gruendung |

**Prompted vs. Spontan Flag:**

Methodisch entscheidend. Unterscheide:
- **spontan:** Teilnehmer bringt Konzept/Thema selbst ein, ohne dass der Interviewer es vorher erwaehnt hat.
- **prompted:** Teilnehmer reagiert auf ein Konzept das der Interviewer eingefuehrt hat. Wenn der Interviewer fragt "Fuehlen Sie sich manchmal zerrissen zwischen den beiden Rollen?" und der Teilnehmer sagt "Ja, total zerrissen" — das ist prompted. Wenn der Teilnehmer von sich aus sagt "Ich fuehle mich manchmal zerrissen" — das ist spontan.
- REGEL: Wenn ein Teilnehmer die Formulierung des Interviewers woertlich aufgreift, ist das prompted language. Immer markieren.

### Schritt 3: Anti-Glaettungsprotokoll

Nach dem Coding-Durchlauf, BEVOR das Ergebnis ausgegeben wird:

**Pruefung 1 — Widerspruchscheck:**
- Gibt es Segmente in denen der/die Teilnehmende sich selbst widerspricht?
- Werden diese Widersprueche in der Codierung sichtbar oder wurden sie in einen einzigen Code geglaettet?
- REGEL: Widersprueche erhalten ZWEI Codes, nicht einen Kompromiss-Code.

**Pruefung 2 — Ambivalenz-Check:**
- Gibt es Segmente die "sowohl als auch" ausdruecken?
- REGEL: Ambivalenz ist ein eigener Code, nicht die Haelfte von zwei Codes. Wenn jemand sagt "Einerseits liebe ich die Freiheit, andererseits macht mir die Unsicherheit Angst" — das ist EIN Segment mit Ambivalenz, nicht zwei halbe Segmente.

**Pruefung 3 — Kohaerenz-Verdacht:**
- Liest sich das Gesamtbild dieses Interviews "zu rund"?
- Ist die Geschichte die sich aus den Codes ergibt zu linear, zu aufgeraeumt?
- REGEL: Wenn ja, zurueck zum Transkript. Suche aktiv nach Stellen die nicht ins Bild passen. Dokumentiere sie als GEGENBELEG.

**Pruefung 4 — Zitat-Verifikation:**
- Fuer JEDES Zitat in der Coding-Tabelle: Ist es WOERTLICH aus dem Transkript?
- Grep oder lies die angegebene Zeilennummer und vergleiche Wort fuer Wort.
- REGEL: Kein einziges Wort aendern. Nicht "aufzuraeumen" oder "verstaendlicher machen." ASR-Artefakte bleiben. Grammatikfehler bleiben. Satzabbrueche bleiben.
- HAERTESTER TEST: Wenn ein Zitat glaetter klingt als der Rest des Transkripts, ist es wahrscheinlich veraendert. Pruefen.

### Schritt 4: Output

Pro Transkript zwei Dateien:

**Datei 1: Coding-Tabelle** (`Coding_[Teilnehmer].md`)
```markdown
---
participant: [Name/Code]
transcript: [Dateipfad]
method: [Gioia/Thematic Analysis/deduktiv]
coder: Claude
date: [YYYY-MM-DD]
segments_total: [n]
segments_excluded: [n] (Interviewer, Smalltalk, etc.)
segments_coded: [n]
---

| Zeile | Zitat | Code | Begruendung | Konfidenz |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
```

**Datei 2: Coding-Memo** (`Memo_[Teilnehmer].md`)
- Zusammenfassung: Was sind die dominanten Themen?
- Widersprueche: Welche Stellen widersprechen sich? (mit Zeilennummern)
- Gegenbelege: Was passt NICHT ins Gesamtbild?
- Unsicherheiten: Welche Codierungen sind grenzwertig?
- Ueberraschungen: Was hat Claude nicht erwartet?
- Neue Codes: (nur bei induktiv/Gioia) Welche Codes mussten neu erstellt werden?

---

## Modus COMPARE

Vergleicht Claude-Coding mit menschlichem Coding desselben Transkripts.

### Input
- Claude-Coding (`Coding_[Teilnehmer].md`)
- Menschliches Coding (Datei oder Codebook-Zuordnung)

### Output

**Uebereinstimmungsmatrix:**

| Segment/Zeile | Code Mensch | Code Claude | Uebereinstimmung | Diskussionspunkt |
|---|---|---|---|---|
| ... | ... | ... | JA / NEIN / TEILWEISE | ... |

**Analyse der Abweichungen:**
Fuer jede Nicht-Uebereinstimmung:
- Was hat Claude gesehen was der Mensch nicht gesehen hat? (Cross-Case-Pattern, subtile Formulierungen)
- Was hat der Mensch gesehen was Claude nicht gesehen hat? (Kontext, Tonfall, nonverbale Hinweise im Transkript, Hintergrundwissen)
- Wer liegt vermutlich richtig und warum?

**Glaettungs-Audit:**
- In wie vielen Faellen hat Claude einen Kompromiss-Code vergeben wo der Mensch zwei separate Codes hat?
- In wie vielen Faellen hat Claude Ambivalenz aufgeloest?

---

## Modus EXPLORE

Explorativer Durchlauf ohne formales Codebook. Fuer den ersten Kontakt mit einem Transkript.

### Output
- Was sind die 5-7 staerksten Themen in diesem Interview?
- Welche Aussagen sind ueberraschend oder widersprechen gaengigen Annahmen?
- Welche Stellen wuerden in einer Gioia-Analyse die staerksten First-Order Concepts liefern?
- Was fehlt — welche Fragen hat der Interviewer NICHT gestellt, die man erwarten wuerde?

---

## Modus AUDIT

Selbstkontrolle nach dem ersten Coding-Durchlauf. Prueft das eigene Coding auf die typischen Claude-Fehler.

### Pruefschritte

1. **Zitat-Integritaet:** Fuer jedes Zitat in der Coding-Tabelle: Lies die angegebene Zeile im Originaltranskript. Wort-fuer-Wort-Vergleich. Jede Abweichung dokumentieren.
2. **Interviewer-Kontamination:** Hat Interviewer-Sprache in die Codes gefunden? Greift ein Teilnehmer die Formulierung des Interviewers woertlich auf — und wurde das als spontan statt prompted codiert?
3. **Glaettungs-Check:** Gibt es Codes die zu elegant sind? Wo Widersprueche aufgeloest statt dokumentiert wurden? Wo das Interview "zu rund" liest?
4. **Ueber-Coding-Check:** Wurden Smalltalk, Organisatorisches, Begruessungen, oder Interviewer-Fragen codiert?
5. **Code-Inflation:** Gibt es breite, elegante Codes die eigentlich mehrere enge Codes sein sollten?

### Output
Audit-Report mit:
- Anzahl gepruefte Segmente
- Anzahl Zitat-Abweichungen (mit Korrektur)
- Anzahl Interviewer-Kontaminationen
- Anzahl Glaettungsfaelle
- Anzahl Ueber-Codings
- Korrigierte Coding-Tabelle

---

## Hard Rules (gelten in ALLEN Modi)

### Evidenz-Disziplin
1. **Jeder Code braucht ein direktes Zitat.** Kein Code ohne woertlichen Beleg aus dem Transkript. Paraphrasen sind KEIN Ersatz. Wenn kein woertliches Zitat existiert das den Code stuetzt, wird der Code nicht vergeben.
2. **Woertlich heisst woertlich.** Kein Wort aendern. Kein "aeh" entfernen. Kein Satzbau korrigieren. Keine zwei Saetze zu einem zusammenziehen. ASR-Artefakte bleiben. Grammatikfehler bleiben. Satzabbrueche bleiben.
3. **Paraphrasen explizit kennzeichnen.** Wenn zusaetzlich zum woertlichen Zitat eine Paraphrase hilfreich ist, MUSS sie als [PARAPHRASE] markiert sein. Sie ersetzt nie das direkte Zitat.
4. **Auslassungen markieren.** [...] fuer jede Auslassung. Keine stillen Kuerzungen.
5. **Zeilennummern muessen stimmen.** Wenn Zeile 47 angegeben ist, muss das Zitat in Zeile 47 stehen. Nicht "ungefaehr bei Zeile 47."
6. **Im Zweifel laenger zitieren.** Lieber zu viel Kontext als ein aus dem Zusammenhang gerissenes Fragment.
7. **Anfuehrungszeichen nur fuer Verbatim-Text.** Keine Anfuehrungszeichen fuer rekonstruierten oder zusammengefassten Wortlaut.

### Sprechertrennung (Speaker Discipline)
8. **Interviewer-Aeusserungen NIEMALS als Teilnehmer-Zitat verwenden.** Auch nicht "zusammenfassend" oder "interpretierend."
9. **Interviewer-Redeanteile werden nie codiert.** Auch nicht wenn der Interviewer eine inhaltlich relevante Aussage macht. Das ist eine andere Datenquelle. Einzige Ausnahme: wenn die Forschungsfrage explizit Interaktionsdynamiken oder Ko-Konstruktion im Interview untersucht.
10. **Interviewer-Wording das vom Teilnehmer uebernommen wird = prompted.** Wenn der Interviewer fragt "Fuehlen Sie sich zerrissen?" und der Teilnehmer sagt "Ja, total zerrissen" — markiere als prompted. Das Konzept kam nicht vom Teilnehmer.
11. **Spontan vs. prompted unterscheiden.** Wo ein Konzept zum ersten Mal auftaucht bestimmt ob es spontan oder prompted ist. Spontane Einfuehrung eines Konzepts durch den Teilnehmer hat hoehere analytische Aussagekraft als prompte Zustimmung.

### Anti-Glaettung
12. **Widersprueche sind Daten, keine Fehler.** Wenn P3 in Zeile 20 sagt "Ich liebe meinen Job" und in Zeile 180 "Manchmal hasse ich was ich tue" — beide Codes stehen lassen. Nicht aufloesen.
13. **Keine narrativen Boegen konstruieren.** Claude neigt dazu, aus Interviews eine Geschichte zu machen (Anfang → Konflikt → Loesung). Interviews sind keine Geschichten. Sie sind fragmentarisch, widerspruechlich, unaufgeraeumt. Das ist korrekt so.
14. **"Sowohl als auch" ist ein Code, nicht zwei halbe.** Ambivalenz nicht in Einzelteile zerlegen.
15. **Gegenbelege aktiv suchen.** Nach dem Coding: Was im Transkript widerspricht dem Gesamtbild? Diese Stellen dokumentieren, nicht ignorieren.
16. **Inkonsistenz innerhalb eines Teilnehmers erhalten.** Unterschiede zwischen Teilnehmern erhalten. Nicht verschiedene Bedeutungen in einen Code kollabieren nur weil sie aehnlich klingen.
17. **Unklare, instabile, oder widerspruechliche Passagen markieren als:** ambiguous / mixed / contradictory / unclear reference.

### Segment-Filter
18. **Smalltalk, Organisatorisches, Begruessungen werden nie codiert.** Dazu gehoeren: Begruessungen, Dank, "Koennen Sie mich hoeren?", "Das ist interessant", Lachen ohne analytischen Wert, Wiederholung nur um das Gespraech am Laufen zu halten.
19. **Segment-Zaehlung dokumentieren.** Wie viele Segmente gesamt, wie viele ausgeschlossen, wie viele codiert. Dieses Verhaeltnis ist methodisch relevant.

### Coding-Disziplin
20. **Prefer undercoding to overcoding.** Im Zweifel NICHT codieren. Lieber ein Segment ohne Code lassen als einen unsicheren Code vergeben.
21. **Prefer multiple narrow codes over one elegant but inflated code.** Drei spezifische Codes sind besser als ein breiter der alles abdeckt.
22. **Nicht in Codes reinpressen.** Wenn ein Segment in keinen Code passt, bleibt es uncodiert mit Vermerk [KEIN CODE — GRUND: ...].
23. **Neue Codes begruenden.** Bei induktivem Coding: Warum reicht kein existierender Code? Was ist der Unterschied?
24. **Konfidenz immer angeben.** Kein Code ohne high/medium/low. Grenzfaelle sind Grenzfaelle, nicht "wahrscheinlich X."
25. **Evidenz vor Interpretation.** Erst offene Codes am Material. Dann Memos. Dann vorsichtige Cluster. Nicht sofort Themes. Keine polierten Narrative produzieren ausser auf explizite Anfrage.

### Missing Evidence Policy
26. **Wenn die Evidenz nicht reicht: nicht raten.** Nicht das Pattern vervollstaendigen. Nicht Luecken mit plausiblem Wortlaut fuellen. Stattdessen: "Insufficient evidence for coding beyond descriptive level." oder [KEIN CODE — EVIDENZ REICHT NICHT].

---

## Integration mit anderen Skills

- **data-integrity-guard:** Jede Zitat-Zeilennummer wird gegen das Transkript geprueft. Jeder Participant-Code wird gegen die Coding-Matrix verifiziert.
- **hallucination-audit:** Nach dem Coding-Durchlauf: Tier-3-Pruefung auf alle Zitate (woertlicher Abgleich mit Transkript).
- **saturation-auditor:** Nach dem Coding aller Transkripte: Saettigungsanalyse ueber die Code-Haeufigkeiten.
- **anti-ai-writing:** Gilt fuer Memos und Interpretationen, NICHT fuer die Coding-Tabelle selbst.

---

## Typische Aufrufe

```
/qualitative-coder CODE /pfad/zum/transkript.txt
/qualitative-coder COMPARE /Claude-Coding.md /Mensch-Coding.md
/qualitative-coder EXPLORE /pfad/zum/transkript.txt
```

Sprache folgt dem Input (Deutsch / English).
