---
name: desk-rejection-preventer
description: "Three-gate pre-submission test focused specifically on the most common desk-rejection patterns at A-journals: (1) Distinctiveness — can your core construct be explained by recombining 2-3 existing constructs? (2) Claim-Design-Weight — does your empirical design carry the theoretical weight of your claims, especially for mechanism claims? (3) Scope-Conditions — are boundary conditions specified explicitly, avoiding the too-specific/too-abstract double-bind? This skill does NOT rewrite the paper. It forces the author through the three gates BEFORE submission, produces a traffic-light diagnosis per gate, and demands written answers to gate questions. Use AFTER paper-feedback-pipeline and BEFORE research-examiner. Derived from JMS 2026-04 MDO desk-rejection pattern-analysis. Triggers: 'desk rejection check', 'distinctiveness test', 'is this ready for A-journal', 'will this survive desk review', 'pre-submission gates', 'rekombinations-test', 'contribution check vor submission'."
---

# Desk-Rejection-Preventer

Pre-Submission-Test auf drei Gates, auf die A-Journals bei hoher Selektionsdichte als Desk-Rejection-Trigger reagieren. Die Skill schreibt das Paper nicht um. Sie zwingt Autoren durch die Gates und verlangt schriftliche Antworten.

## Positionierung

- **Vor:** research-examiner (operational compliance + epistemic depth)
- **Nach:** paper-feedback-pipeline (content-quality)
- **Nicht ersetzbar durch:** a-journal-architecture (DNA-Tests) oder mulcahy-contribution-auditor (PhD-level)

Der Unterschied zu research-examiner: research-examiner prueft breit und gibt Handlungsoptionen. Dieser Skill prueft schmal und bindend, mit Ampel-Diagnose. Ein rotes Gate ist ein Submission-Stopp.

## Grundlage

Desk-Rejection-Patterns aus drei konkreten A-Journal-Rueckmeldungen:
1. "Construct kann durch Recombination bestehender Konstrukte erklaert werden" — Distinctiveness-Defizit
2. "Empirische Strategie traegt die theoretische Last nicht" — Claim-Design-Misalignment
3. "Portability asseriert, nicht demonstriert, Scope-Conditions unterentwickelt" — Boundary-Defizit

Jedes Gate hat eine spezifische Frage, die der Autor beantworten MUSS, bevor die Submission freigegeben wird. Ohne Antwort kein Gate-Pass.

---

## Gate 1: Distinctiveness (Rekombinations-Test)

**Kernfrage:** Kann dein Kernkonstrukt durch Recombination von 2-3 etablierten Konstrukten erklaert werden? Wenn ja, wo genau versagt die Summe der Alternativen?

**Protokoll:**

1. Autor benennt das Kernkonstrukt des Papiers in einem Satz.
2. Autor listet mindestens drei etablierte Konstrukte aus der relevanten Literatur, die zusammen die gleiche Pointe abdecken koennten. Der Skill fragt aktiv nach den naheliegenden Alternativen.
3. Autor formuliert: "Meine Konstrukt leistet X, was die Summe aus [A, B, C] nicht leistet, weil [mechanism-spezifischer Grund]."
4. Skill testet den Satz gegen drei Ausschluss-Kriterien:
   - Nicht "wir integrieren" — Integration ist keine Distinctiveness
   - Nicht "wir wenden an ein neues Feld an" — Anwendung ist keine Distinctiveness
   - Nicht "wir zeigen empirisch" — empirische Neuheit ist keine theoretische Distinctiveness
5. Wenn der Satz eines der Kriterien trifft: rote Ampel. Autor muss neu formulieren.
6. Wenn der Satz keines trifft: Skill prueft, ob der Distinctiveness-Claim explizit im Paper steht (Introduction + Theory). Fehlt er im Paper: gelbe Ampel mit Einbau-Auftrag.
7. Wenn Satz scharf und im Paper: gruene Ampel.

**Typische Fallen:**
- Contribution-Claims der Form "we extend X to Y" ohne spezifische Leistung des Extends
- Mechanismus-Labels, die bei Ocasio + Greenwood + Espeland + Olson bereits implizit sind
- "Novel combination" als Contribution-Claim (siehe mulcahy-contribution-auditor: das ist PhD-ungenuegend)

---

## Gate 2: Claim-Design-Weight (Empirische Tragkraft)

**Kernfrage:** Traegt das Design den Claim? Konkret: kann die Datenbasis Mechanismus-Claims stuetzen, oder nur Muster-Beobachtungen?

**Protokoll:**

1. Skill klassifiziert den Haupt-Claim des Papiers:
   - **Assoziation:** X kommt mit Y vor (schwach)
   - **Muster:** X tritt systematisch unter Bedingung B auf (mittel)
   - **Mechanismus:** X fuehrt ueber konkreten Prozess zu Y (stark)
   - **Kausalitaet:** X verursacht Y unter Identifikationsbedingungen (stark+)
   - **Theorie-Building:** X liefert neues Konstrukt, das in bestehende Theorie integriert (stark)

2. Skill inventarisiert Design-Weight:
   - N, Sampling-Logik
   - Datenarten (Interviews, Dokumente, Beobachtung, Archive, longitudinal)
   - Triangulation
   - Prozess-Daten (zeitliche Aufloesung, episodische Rekonstruktion)
   - Mitglieder-Validierung

3. Skill prueft Match nach Tabelle:

| Claim-Typ | Minimal-Design |
|-----------|---------------|
| Assoziation | Single-Method, N moderat |
| Muster | Multi-Case, Triangulation |
| Mechanismus | Prozess-Daten, konkrete Episoden, process tracing |
| Kausalitaet | Identifikations-Design (RCT, Quasi-Experiment, fsQCA) |
| Theorie-Building | Abduktive Iterationen, saturation, boundary-condition-tests |

4. Wenn Design unter Claim-Weight: Ampel rot. Autor muss entweder Claim abschwaechen oder Design ergaenzen.
5. Wenn Design gleich Claim-Weight: gelbe Ampel mit Verstaerkungs-Pruefung.
6. Wenn Design ueber Claim-Weight: gruene Ampel (seltener Fall, meist Claim-Upgrade moeglich).

**Typische Fallen:**
- N=30-50 Eliten-Interviews fuer Mechanism-Claims (traegt Muster, nicht Mechanismus)
- Cross-Actor-Convergence statt Process-Tracing (traegt Muster, nicht Mechanismus-in-Action)
- Survey-Daten fuer Kausal-Claims ohne Identifikations-Strategie

---

## Gate 3: Scope-Conditions (Boundary-Specification)

**Kernfrage:** Unter welchen Bedingungen gilt dein Mechanismus? Wann greift er nicht? Steht das explizit im Paper?

**Protokoll:**

1. Skill verlangt vom Autor eine Liste der drei wichtigsten Scope-Conditions in folgendem Format:
   - "Die Theorie greift, wenn A (z.B. geopolitische Urgenz), B (z.B. Multi-Level-Sovereignty), C (z.B. Klassifikations-Beschraenkung) vorliegen."
   - "Ohne A greift der Mechanismus nicht, weil..."
   - "Ohne B greift der Mechanismus nicht, weil..."
   - "Ohne C greift der Mechanismus nicht, weil..."

2. Skill testet Scope-Liste gegen Double-Bind:
   - **Too-specific:** wenn alle drei Conditions ausschliesslich im gewaehlten Feld vorliegen, Portability ist nicht gegeben, Paper wird als context-bound gelesen. Rot.
   - **Too-abstract:** wenn die Conditions so generisch sind, dass sie ueberall zutreffen, der Mechanismus ist nicht abgrenzbar. Rot.
   - **Middle:** mindestens zwei Conditions sind in anderen Feldern empirisch identifizierbar, mindestens eine grenzt das Feld scharf ab. Gruen.

3. Skill prueft, ob Scope-Block im Paper sichtbar ist (Theory-Section oder Discussion-Boundary-Block).
   - Fehlt explizit: gelbe Ampel mit Einbau-Auftrag.
   - Vorhanden aber zu schwach formuliert ("our findings may not generalize"): gelbe Ampel mit Schaerfungs-Auftrag.
   - Explizit, abgegrenzt, mit Gegenbeispielen: gruene Ampel.

**Typische Fallen:**
- "Future research should test in other contexts" ohne Angabe, welche Contexts
- "Our findings are generalizable" ohne Mechanismus-basierte Portability-Argumente
- Boundary-Conditions nur in der Limitations-Sektion, nicht in der Theorie

---

## Gesamt-Verdict

Drei Gates, drei Ampeln. Moegliche Kombinationen:

- **3x Gruen:** Submission freigegeben.
- **2x Gruen + 1x Gelb:** Submission nach Einbau-Arbeit (<1 Tag) freigegeben.
- **Alles andere:** Submission-Stopp. Wahl:
  - Major-Revision durchziehen, dann neu testen
  - Journal-Target wechseln (weniger selektives A-, oder B-Journal)
  - Paper-Format wechseln (Phaenomen-Paper statt Theorie-Paper)

## Output-Format

Report als Datei im Projekt-Ordner: `Desk_Rejection_Preventer_YYYY-MM-DD.md`

Struktur:
```
# Desk-Rejection-Preventer Report
## Gate 1: Distinctiveness — [AMPEL]
- Kernkonstrukt: ...
- Alternative Rekombinations-Liste: ...
- Autor-Antwort: ...
- Diagnose: ...
- Einbau-Auftrag (falls noetig): ...

## Gate 2: Claim-Design-Weight — [AMPEL]
- Claim-Klassifikation: ...
- Design-Inventar: ...
- Match-Urteil: ...
- Einbau-Auftrag (falls noetig): ...

## Gate 3: Scope-Conditions — [AMPEL]
- Scope-Liste: ...
- Double-Bind-Test: ...
- Paper-Sichtbarkeit: ...
- Einbau-Auftrag (falls noetig): ...

## Gesamt-Verdict
[Freigegeben / Nach Nachbesserung / Submission-Stopp]

## Empfohlene naechste Schritte
...
```

## Sprachregelung

Sprache folgt Input (Deutsch / Englisch). Bei deutscher Konversation wird der Report auf Deutsch gehalten, die Claim-Formulierungen folgen den Sprachregeln der Ziel-Journals (meist Englisch).

## Wann NICHT verwenden

- Waehrend Draft-Entwicklung (zu frueh, blockiert Exploration)
- Fuer Workshop- und Conference-Papers (zu streng, Format ist anderes)
- Fuer Revisions nach ersten Reviewer-Reports (dann paper-revision-diagnostic)
- Fuer Non-A-Journal-Submissions ohne Desk-Rejection-Druck (ueberflussig)

## Herkunft

Abgeleitet aus MDO-Paper Desk-Rejection JMS 2026-04. Die drei Gates korrespondieren 1-zu-1 zu den drei Kritikpunkten des JMS-Editorial-Screening. Generalisierung basiert auf Annahme, dass diese Muster an allen A-Journals mit hoher Selektionsdichte wiederkehren.
