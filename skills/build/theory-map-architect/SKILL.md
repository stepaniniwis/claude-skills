---
name: theory-map-architect
description: Produziert ein zweiseitiges strategisches Theorie-Memo für konfigurationale (fsQCA, QCA) und qualitative (Gioia, Grounded Theory, case study) Paper, deren Ergebnisse bereits stehen, aber bei denen das theoretische Artefakt über den Befunden noch unscharf ist. Macht die drei strategischen Entscheidungen explizit, die ein Paper von "empirisch fertig" zu "einreichbar" tragen – Kernlinse, Hilfslinse, Artefakt-Genre – und prüft Eigenkonstrukte auf theoretische Verankerung (inklusive Kanonisch-Naming-Check gegen etablierte Theorien wie Construal Level Theory, UTAUT etc.). NICHT für Theorie-Sektions-Prosa (dafür theory-section-architect), NICHT für Theorietyp-Klassifikation (dafür mulcahy-theory-diagnostics), NICHT für RQ-Entwicklung (dafür rq-architect). Dieser Skill sitzt zwischen Empirie und Schreiben. Trigger auf: "Theory Map", "Theorie-Memo", "welche Theorie trägt mein Paper", "Konfigurationen theoretisch einordnen", "middle-range theory oder propositions paper", "abductive theory extension", "welches Genre für mein qualitatives Paper", "Kernlinse Hilfslinse", "meine fsQCA-Solutions stehen, was jetzt", "meine aggregate dimensions stehen, was jetzt", "theoretisches Artefakt unscharf", "Paper braucht theoretische Schärfung", "welche Referenzpaper strukturell imitieren", "freischwebende Konstrukte verankern", "Eigenkonstrukte theoretisch einbetten", "Kontrast-Paper zum Feld", oder wenn User ein konfigurationales oder qualitatives Paper vorlegt mit bestehenden Ergebnissen und fragt, wie es nun theoretisch gerahmt werden soll. Auch trigger wenn User sagt "die Ergebnisse stehen" zusammen mit Theorie-Fragen. Der Skill ist schärfer und strategischer als theory-section-architect – er produziert KEIN Sektions-Draft, sondern eine strukturierte Entscheidungsgrundlage, aus der danach Prosa entstehen kann.
---

# Theory Map Architect

## Zweck

Ein **strategisches Zwischenprodukt** zwischen fertiger Empirie und geschriebener Theorie-Sektion. Der Skill produziert **keine Prosa** – er produziert eine strukturierte Entscheidungsgrundlage, aus der danach Prosa werden kann.

Die Leitfrage: **Welches theoretische Artefakt soll über den empirischen Befunden stehen?**

Das ist nicht trivial. Konfigurationale und qualitative Paper scheitern im Review selten daran, dass die Ergebnisse unklar wären – sie scheitern an drei typischen Schwachstellen:

1. **Unklare Kernlinse.** Das Paper zieht aus drei Theorien gleichzeitig, ohne dass eine davon wirklich trägt.
2. **Frei schwebende Eigenkonstrukte.** Konstrukte wie "Perceived Democratic Significance" oder eigene aggregate dimensions sind empirisch fundiert, aber theoretisch nirgendwo verankert.
3. **Falsches Genre.** Das Paper will middle-range theory sein, argumentiert aber wie ein typologisches Paper – oder umgekehrt.

Dieser Skill adressiert genau diese drei Schwachstellen, bevor geschrieben wird.

## Wann dieser Skill triggert

- User legt Ergebnisse eines fsQCA-, QCA-, Gioia-, grounded-theory- oder vergleichbaren Paper vor und fragt, wie es theoretisch gerahmt werden soll.
- User hat Konfigurationen / aggregate dimensions / Muster identifiziert, aber das theoretische Artefakt über den Befunden ist unklar.
- User fragt nach Kernlinse, Hilfslinse, middle-range theory vs. propositions paper, abductive theory extension.
- User fragt, welche Referenzpaper strukturell imitiert werden sollten.
- User hat Eigenkonstrukte entwickelt und fragt, wie sie theoretisch eingebettet werden.

## Wann dieser Skill NICHT triggert

- **Ergebnisse stehen noch nicht.** Dann zuerst fsQCA-Skill (`fsqca-analyst`) oder Gioia-basierte Coding-Skills (`qual-first-coder`, `saturation-auditor`). Siehe Voraussetzungs-Gate unten.
- **User will Prosa der Theorie-Sektion.** Dann `theory-section-architect` nach Abschluss dieses Skills.
- **User will Theorietyp klassifizieren (Descriptive/Explanatory/Causal).** Dann `mulcahy-theory-diagnostics`.
- **User will RQ entwickeln / problematisieren.** Dann `rq-architect`.
- **User will prüfen, ob Theorie konsistent durch das Paper läuft.** Dann `mulcahy-theory-coherence` (nach diesem Skill).
- **Rein quantitatives SEM-/Regressionspaper.** Andere Logik (Hypothesen aus nomologischem Netz); hier nicht anwendbar.

## Sprachregel

**Sprache des Inputs spiegeln.** Wenn User Deutsch schreibt: Memo auf Deutsch. Wenn User Englisch schreibt: Memo auf Englisch.

**Ausnahme für Propositions:** Wenn das Memo auf Deutsch ist, aber das Paper erkennbar für ein englischsprachiges Journal vorgesehen ist (JMS, ISJ, MISQ, OS, AMJ, ASQ etc.), dann die Propositions in Sektion 7 **zusätzlich in Englisch** liefern. Begründung: sie landen am Ende eh im englischen Paper, und englische Proposition-Formulierung hat ihre eigene Präzision, die beim Übersetzen verloren geht.

## Interaktionsmodus

Bevor der Skill das Memo schreibt, prüft er die Informationslage. Der Skill **fragt aktiv nach**, wenn etwas fehlt – er rät nicht. Konkret:

1. **Stehen die Ergebnisse?** Wenn unklar: fragen. Wenn erkennbar nicht: Voraussetzungs-Gate auslösen (Sektion 1 unten).
2. **Welches Journal / welche Community ist Ziel?** Ohne Journal-Info kann der Skill weder Genre noch Referenzpaper sinnvoll einordnen.
3. **Gibt es Referenzpaper, die der User als strukturelle Blaupause erwägt?** Falls ja: hochladen oder nennen lassen. Falls nein: mit Genre-Archetypen arbeiten.
4. **Welche Konstrukte sind Eigenentwicklungen?** Der Skill muss das wissen, um Sektion 4 (Verankerungs-Audit) zu machen.

Diese Fragen werden **gebündelt** gestellt, nicht einzeln – eine Runde Rückfragen, dann Memo. Wenn der User bereits genug Information im initialen Prompt liefert, direkt zum Memo übergehen.

---

## Das Template: Acht Sektionen

Das Memo hat **feste Struktur**. Abweichungen nur, wenn eine Sektion nicht anwendbar ist (dann explizit markieren: *"nicht anwendbar, weil …"*). Zielumfang: **zwei Seiten**, knapp. Keine Wiederholung des empirischen Befunds – der steht bereits. Keine Höflichkeitsrhetorik. Keine generischen Formulierungen.

### 1. Voraussetzungs-Gate

Knapper Check (3–5 Zeilen): Sind die Voraussetzungen für dieses Memo erfüllt?

- Stehen die Ergebnisse (Konfigurationen / aggregate dimensions / Muster)?
- Ist die RQ stabil formuliert?
- Ist das Zieljournal / die Zielcommunity benannt?

**Wenn nein:** Memo **nicht schreiben**, sondern auf vorgelagerten Schritt verweisen. Konkret:
- Ergebnisse fehlen → `fsqca-analyst` oder `qual-first-coder` / `saturation-auditor`
- RQ unscharf → `rq-architect`
- Zieljournal unklar → User fragen, keine Annahme

**Wenn ja:** Einzeiler wie "Voraussetzungen erfüllt: [X fsQCA-Konfigurationen] stehen, RQ stabil, Ziel: [Journal]. Fortfahren." Dann Sektion 2.

### 2. Kernlinse

**Eine** Haupttheorie, die das Paper trägt. Nicht zwei gleichberechtigte. Nicht "Theorie-Eintopf".

Liefere:
- **Name und Herkunft** der Theorie (inkl. Schlüsselreferenz)
- **Warum diese und nicht eine andere** – mit expliziter Nennung der Alternative, die naheliegen würde, aber *nicht* trägt. Das ist der Kern der Entscheidung.
- **Wie sie die empirischen Ergebnisse rahmt** – in ein bis zwei Sätzen, nicht ausbuchstabiert.
- **Reichweite** – erklärt sie alle Befunde oder nur den Kern? Wenn nur den Kern: Übergang zur Hilfslinse (Sektion 3).

Wenn mehrere Kernlinsen plausibel sind: **Entscheide dich**. Eine empfohlen, Alternativen in einem Halbsatz benannt. Unentschlossenheit wird in diesem Memo nicht ausgehalten.

### 3. Hilfslinse(n)

Was die Kernlinse nicht abdeckt, fängt die Hilfslinse auf. Maximal **zwei** Hilfslinsen. Wenn mehr: Kernlinse ist falsch gewählt.

Pro Hilfslinse:
- **Was sie abdeckt**, was die Kernlinse nicht kann (konkret, nicht vage)
- **Wie sie mit der Kernlinse verbunden ist** – komplementär (ergänzt) / kontingent (wirkt unter Bedingung X) / substitutiv (ersetzt unter Bedingung Y). Das ist die Sprache, die Reviewer erwarten.
- **Schlüsselreferenz** (1, maximal 2)

### 4. Verankerungs-Audit für Eigenkonstrukte

**Die diagnostische Kernleistung dieses Skills.**

Gehe jedes Eigenkonstrukt einzeln durch. Für jedes:

- **Name und Definition**
- **Kanonisch-Naming-Check.** Wenn die Abkürzung oder der Name des Konstrukts bereits eine kanonische Lesart in einer etablierten Theorie hat (z.B. "CL" = Construal Level Theory; "SI" = Social Influence aus UTAUT; "TAM" = Technology Acceptance Model), **immer explizit prüfen**, ob das gewollt ist. Drei mögliche Fälle: (a) Gewollt – dann muss im Paper klar an die kanonische Theorie angeschlossen werden, sonst liest der Reviewer die Kollision als unbeabsichtigte Verwechslung. (b) Nicht gewollt – umbenennen, bevor das Paper submitted wird. (c) Unklar – User fragen, welche Lesart intendiert war. Diesen Check *vor* dem eigentlichen Verankerungs-Audit machen, denn er kann die Verankerungs-Empfehlung verändern.
- **Ist es theoretisch verankert?** Prüfe drei Ebenen:
  - (a) Gibt es einen etablierten theoretischen Begriff, unter dem das Konstrukt subsumierbar ist? (Dann: Verankerung über Subsumption.)
  - (b) Ist es eine Neuentwicklung, die aber an einer bestehenden Theorie andockt? (Dann: Verankerung über Anschluss.)
  - (c) Schwebt es frei? (Dann: **Rotes Flag** – muss verankert werden, bevor das Paper einreichbar ist.)
- **Empfehlung:** Konkret. Entweder "verankere an [Theorie X, Autor Y]" oder "umbenennen zu [etablierter Begriff]" oder "als Hilfslinse aus Sektion 3 re-framen".

Wenn der User keine Eigenkonstrukte hat: Sektion explizit als "nicht anwendbar" markieren. Nicht leer lassen.

### 5. Artefakt-Entscheidung

**Welches Genre soll das Paper am Ende sein?** Die Haupt-Archetypen für konfigurational / qualitativ:

- **Middle-range theory mit boundary conditions** – typischerweise 2–4 Propositions + explizite Geltungsbedingungen. Gut, wenn Konfigurationen stabile Mechanismen nahelegen.
- **Propositions paper (pure)** – 3–6 Propositions, ohne ausgearbeitetes Modell. Gut, wenn die Befunde mechanismus-fokussiert sind, aber noch kein abgeschlossenes Modell tragen.
- **Abductive theory extension** – nimmt existierende Theorie und erweitert sie auf Basis der Befunde. Gut, wenn eine dominante Theorie schon im Feld existiert und die Befunde diese erweitern.
- **Typological theory** – baut eine Typologie aus den Konfigurationen. Gut, wenn die Konfigurationen wirklich qualitativ verschieden sind und nicht ineinander übergehen.
- **Process theory** – baut ein Prozessmodell mit zeitlicher Sequenz. Gut für Gioia-Paper mit longitudinalen Daten.
- **Grounded theory contribution** – für qualitative Paper ohne a priori Theorie.

**Empfehlung konkret:** *"Dieses Paper sollte [Genre X] sein, weil [Grund]."* Ein Genre, nicht drei. Alternativen in einem Halbsatz.

**Referenzpaper-Einordnung (wenn vorhanden):** Wenn der User Referenzpaper genannt hat, ordne sie strukturell ein. Nicht inhaltlich paraphrasieren, sondern: *"Paper X trägt zweistufig (fsQCA plus qualitatives Follow-up), Paper Y ist rhetorisch straffer, Paper Z arbeitet mit reinen Propositions."* Dann: *"Für euer Paper passt strukturell am ehesten [Y], weil […]."* Das ist die Blaupausen-Logik.

**Warnung vor 1:1-Imitation:** Wenn der User ein Referenzpaper kopieren will, dessen methodische Dramaturgie das eigene Datenmaterial nicht trägt (z.B. fsQCA plus qualitatives Follow-up, aber kein Follow-up vorhanden): explizit warnen. *"Nicht 1:1 übernehmen – das Anschlussmaterial trägt das nicht."*

### 6. Literaturcluster

**Maximal drei** fokussierte Literaturpakete. Kein breiter Review. Kein "lies nochmal 50 Paper".

Pro Cluster:
- **Name** (z.B. "Trust architecture", "Legitimation/meaning", "Social norms")
- **Zweck** – welche Funktion hat dieses Cluster im Paper? (z.B. "fundiert die Kernlinse", "trägt die Hilfslinse", "verankert Eigenkonstrukt X")
- **Ausgangspunkt** – 1–2 Schlüsselreferenzen, mit denen man beginnt. Nicht 20.
- **Was NICHT zu lesen** – wenn es eine naheliegende Literatur gibt, die verführerisch aussieht, aber nicht trägt (z.B. "Technology Acceptance Literature für CL/PDS – nein, geh in political efficacy"): explizit benennen.

**Kontrast-Cluster (optional, vierter Cluster).** Wenn es eine im Feld breit geteilte Annahme oder ein etabliertes Paper gibt, das den eigenen Befund *gerade nicht stützt* oder *kontrastiert*, lohnt es sich, dieses Paper oder diese Literatur explizit als Kontrast-Referenz zu nennen – nicht als "zu lesen", sondern als "zu positionieren gegen". Beispiel: Ein Paper findet, dass politischer Trust eher informelle als formale Partizipation treibt, während das eigene Paper das Gegenteil zeigt. Solche Kontrast-Referenzen schärfen die Positionierung und nehmen Reviewer-Einwänden den Wind aus den Segeln. Maximal ein Kontrast-Cluster, klein gehalten (eine Referenz genügt).

Diese Sektion ist bewusst restriktiv. Der Wert des Skills liegt in der Fokussierung, nicht im Auflisten.

### 7. Propositions-Entwurf

**2–4 Propositions**, direkt aus den Ergebnissen abgeleitet, reviewer-resistent formuliert.

Pro Proposition:
- **Nummerierung** (P1, P2 …)
- **Formulierung** – präzise, nicht vage. Bedingungsstruktur explizit ("Under conditions of X and Y, Z will …").
- **Verbindung zu Kern-/Hilfslinse** in einem Halbsatz.
- **Empirische Basis** – auf welche Konfiguration / aggregate dimension stützt sie sich?

**Wenn Memo auf Deutsch, Paper aber Englisch:** Propositions zusätzlich in Englisch.

**Reviewer-Resistenz prüfen:** Würde ein Reviewer fragen "Warum nicht einfach X existing theory?" Wenn ja: Substitutionstest in die Formulierung einbauen (Anschluss an Substitution Stress Test aus `argument-architecture`).

### 8. Risiko-Flag und nächster Schritt

**Zwei bis drei Zeilen**, nicht mehr.

- **Größter Reviewerrisiko-Punkt** im aktuellen Stand. Ein Satz. Konkret. Nicht "die Theorie könnte stärker sein", sondern "CL und PDS sind derzeit frei schwebend – ohne Verankerung Desk-Reject-Risiko."
- **Nächster sinnvoller Schritt.** Ein Satz. Konkret. Nicht "mehr lesen", sondern "ein- bis zweitägiger Theorie-Sprint zu [Cluster X], dann Discussion schreiben." Oder: "zuerst Verankerung von [Konstrukt Y] klären, dann Propositions finalisieren."

---

## Formatierung

- **Markdown**, klare Überschriften, keine Füllworte.
- **Zwei Seiten** Zielumfang. Wenn länger: zu viel.
- **Keine Bullets innerhalb der Argumentation** – Prosa in Sektionen 2, 3, 4, 5 (wo argumentiert wird). Bullets erlaubt in Sektion 6 (Cluster) und 7 (Propositions), wo Struktur dominiert.
- **APA 7th** für alle Referenzen, inline.
- **Keine Emojis, keine rhetorischen Verzierungen.** Das ist ein Arbeitsdokument, kein Essay.

## Interaktion mit anderen Skills

- **Vorgelagert:** `fsqca-analyst`, `qual-first-coder`, `saturation-auditor`, `rq-architect`
- **Nachgelagert:** `theory-section-architect` (Prosa schreiben), `argument-architecture` (Substitution Stress Test, CARS-Positionierung), `mulcahy-theory-coherence` (prüfen, ob die gewählte Theorie tatsächlich durch das ganze Paper läuft), `scope-condition-architect` (Boundary Conditions ausarbeiten, wenn Artefakt = middle-range theory)
- **Parallel denkbar:** `paper-positioning`, `rq-wording-checker`

Wenn der User nach Abschluss des Memos Prosa schreiben will: explizit auf `theory-section-architect` verweisen.

## Was der Skill NIEMALS tut

- Prosa für die Theorie-Sektion schreiben. (Das macht `theory-section-architect`.)
- Mehr als drei Literaturcluster vorschlagen.
- Generische Statements wie "die Theorie könnte stärker sein" oder "mehr Literatur würde helfen".
- Dem User zustimmen, wenn er eine unklare Kernlinse hat. Der Skill entscheidet – oder fragt explizit.
- 1:1-Imitation eines Referenzpapers empfehlen, wenn das Anschlussmaterial nicht trägt.
- Das Memo länger als zwei Seiten machen.
