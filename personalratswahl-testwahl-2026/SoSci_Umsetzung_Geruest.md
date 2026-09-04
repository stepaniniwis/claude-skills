# SoSci Survey: Umsetzungsgerüst für die Begleitbefragung zur Testwahl (14.–25.09.2026)

Stand: 04.09.2026, v0.1. Variantenunabhängig. Die Items kommen aus `FRAGEBOGEN_Variante_A_Messkontinuitaet_2026-09-02` (79 Items), sobald die Datei im Repo liegt. Dieses Dokument regelt, wie der Fragebogen in SoSci gebaut wird, nicht was gefragt wird.

Randbedingungen aus dem Konstruktrahmen (Teil D, 26.08.2026) und dem LHM-Update-Deck (31.08.2026):
Post-only, rund 500 Freiwillige aus der WiLMA-Anmeldung, Prüfschritt (Verifikationscode) für alle sichtbar, keine Randomisierung von Bedingungen. Dispositionsblock vor jeder Bewertung. Befragung läuft über ein Zeitfenster, damit "Tage seit Stimmabgabe" Varianz hat.

## 1. Projektanlage

| Einstellung | Wert |
|---|---|
| Projekttyp | Umfrage, Sprache Deutsch (Sie-Form) |
| Zugang | Allgemeiner anonymer Link (kein Personenbezug, keine Serienmail nötig). Reminder über RIT-/it@M-Blog wie bei der Anmeldekampagne. |
| Feldzeit | Start 14.09.2026 (erster Tag der Testwahl), Ende frühestens 09.10.2026. Zwei Wochen Nachlauf nach Wahlende sind Pflicht für H4′ (Zeitachse). |
| Unterbrechung | "Fragebogen später fortsetzen" deaktivieren (Post-hoc-Disposition soll in einer Sitzung erhoben werden). |
| IP-Speicherung | Aus. |
| Fragebogen-Einstellungen | Fortschrittsbalken an, Zurück-Button aus (verhindert Nachjustieren der Dispositionsitems nach den Bewertungen). |

## 2. Namenskonvention

SoSci verlangt Fragen-IDs aus zwei Buchstaben und zwei Ziffern (`AB01`); Items werden automatisch `AB01_01`, `AB01_02` … Die Zuordnung Konstrukt → SoSci-ID wird beim Import der Variante A festgelegt. Vorschlag (wird angepasst, sobald die Blöcke feststehen):

| Block | Konstrukt | SoSci-ID | Fragetyp |
|---|---|---|---|
| Einstieg | Einwilligung | `EW01` | Auswahl, Pflicht |
| Einstieg | Teilnahmecheck (Stimme in der Testwahl abgegeben?) | `TC01` | Auswahl, Filter |
| 1 Disposition | TRI 2.0 Optimism | `TO01` | Skala 5-stufig |
| 1 Disposition | TRI 2.0 Innovativeness | `TI01` | Skala 5-stufig |
| 1 Disposition | Technikbereitschaft Neyer: Akzeptanz / Kompetenz / Kontrolle | `TB01` / `TB02` / `TB03` | Skala 5-stufig |
| 2 Erfahrung | Situationsstärke (Klarheit, Konsistenz, Beschränkung, Konsequenz) | `SS01` | Skala 5-stufig |
| 2 Erfahrung | Gerät, Authentifizierung, Dauer, Störungen | `SE01`–`SE04` | Auswahl / Mehrfachauswahl |
| 2 Erfahrung | Tag der Stimmabgabe | `SZ01` | Auswahl (14.–25.09. als Liste, kein Datumsfeld: weniger Fehleingaben) |
| 2 Erfahrung | Vorerfahrung (Probelauf, andere Online-Wahl, vergleichbares System) | `VE01` | Mehrfachauswahl |
| 3 Verständnis | Objektiver Verständnisindex zum Prüfcode | `VK01`–`VK03` | Auswahl, je eine richtige Option |
| 3 Verständnis | Selbsteinschätzung Verständnis | `VS01` | Skala |
| 4 Akzeptanz | BI, PE, EE, SI, HM | `BI01`, `PE01`, `EE01`, `SI01`, `HM01` | Skala 5-stufig |
| 5 Vertrauen | TR, TT, IT | `TR01`, `TT01`, `IT01` | Skala 5-stufig |
| 6 Legitimität | PDS, CVC, ER, CL, PLT, Thaler VAL1/VAL2/PROP1 | `PD01`, `CV01`, `ER01`, `CL01`, `PL01`, `TH01` | Skala 5-stufig |
| 7 Kontrolle | CDV, retrospektive Vorab-Einstellung | `CD01`, `RV01` | Skala / bipolar |
| 8 Demografie | Alter, Geschlecht, Status, Referat (RIT/KVR/sonstige), Dienstjahre, letzte PR-Wahl, Wahlmethode | `DM01`–`DM07` | Auswahl |
| Abschluss | Offenes Feedback | `OF01` | Text, mehrzeilig |

Regel: Item-Nummern innerhalb einer Frage folgen der Reihenfolge im Variante-A-Dokument, damit Codebuch und SoSci-Export ohne Umschlüsselung zusammenpassen.

## 3. Fragetypen und Einstellungen

Likert-Batterien: Fragetyp "Skala (endpunktbenannt)" oder "Skala (vollbenannt)", 5 Stufen, Beschriftung wie in Variante A (1 = stimme gar nicht zu, 5 = stimme voll zu). Einheitlich über alle Batterien, keine Mischung von 5 und 7 Stufen.

Item-Randomisierung: In jeder Skala-Frage die Option "Items in zufälliger Reihenfolge anzeigen" aktivieren. Nur innerhalb des Konstrukts, nie über Konstrukte hinweg (Anforderung aus dem U18-Instrument). Ausnahme: CDV1 (bipolar) und die Thaler-Items, wenn sie als Einzelfragen laufen.

Pflichtfelder: Alle Skalen-Items als "Antwort erforderlich" mit Hinweis statt Blockade ("Sie haben eine Frage nicht beantwortet, möchten Sie fortfahren?"). Harte Pflicht nur bei Einwilligung und Teilnahmecheck.

Umgepolte Items: Nicht in SoSci umkodieren, sondern im Codebuch markieren und in R rekodieren. So bleibt der Rohexport identisch mit dem Instrument.

Verständnisindex (VK01–VK03): Fragetyp "Auswahl", Optionen fest, nicht randomisiert (die Distraktoren sind nach Plausibilität geordnet). Richtig/falsch wird erst in der Analyse kodiert. Die Optionen müssen mit dem Entwicklerteam gegen die reale Garantie des Systems abgeglichen werden: Der Prüfcode belegt die Aufnahme der verschlüsselten Stimme ins öffentliche Protokoll (recorded-as-cast). Er belegt nicht den Stimminhalt, nicht die korrekte Auszählung im Einzelnen und offenbart nicht die Identität. Öffentliche Prüfbarkeit der Auszählung läuft über die veröffentlichten Beweise, nicht über den individuellen Code.

Aufmerksamkeitscheck: Ein Item in Block 4 oder 5 ("Bitte wählen Sie hier 'stimme eher zu'."). Auswertung als Ausschlusskriterium, nicht als Abbruch.

## 4. Seitenstruktur (Fragebogen zusammenstellen)

```
S01 start        Begrüßung, Studieninformation, Einwilligung EW01
S02 check        Teilnahmecheck TC01  -> Filter
S03 dispo1       TO01, TI01
S04 dispo2       TB01, TB02, TB03
S05 erfahrung1   SZ01, SE01–SE04
S06 erfahrung2   SS01 (Situationsstärke), VE01
S07 verstehen    VK01–VK03, VS01
S08 akzeptanz    BI01, PE01, EE01, SI01, HM01 (je eine Batterie, Aufmerksamkeitscheck in EE01 oder SI01)
S09 vertrauen    TR01, TT01, IT01
S10 legitim1     PD01, CV01, ER01
S11 legitim2     CL01, PL01, TH01
S12 kontrolle    CD01, RV01
S13 demo         DM01–DM07
S14 offen        OF01
S15 ende         Dank, Hinweis auf Ergebnisrückmeldung
S99 ende_nt      Ende für Nicht-Teilnehmende (kein Stimmabgabe-Erlebnis)
```

Blockreihenfolge ist fest. Disposition vor Erfahrung vor Bewertung ist eine Designentscheidung (Post-hoc-Disposition soll nicht durch die Bewertungsfragen eingefärbt werden), keine Randomisierung auf Seitenebene.

## 5. PHP-Code

Teilnahmecheck (Seite S02). Wer keine Stimme in der Testwahl abgegeben hat, bekommt keine Erfahrungs- und Bewertungsblöcke:

```php
// S02: TC01 = 1 "Ja, ich habe in der Testwahl abgestimmt", 2 "Nein"
if (value('TC01') == 2) {
  goToPage('ende_nt');
}
```

Tage seit Stimmabgabe werden nicht in SoSci berechnet, sondern in der Analyse aus `STARTED` (Zeitstempel des Fragebogenstarts) und `SZ01` (gewählter Tag). Grund: Zeitfunktionen in SoSci-PHP sind eingeschränkt, und die Rohdaten sollen die Eingabe, nicht eine Ableitung enthalten.

Situationsstärke-Facette "Beschränkung": Wer bei SE04 "keine Störungen" angibt, überspringt die Nachfrage zur Art der Störung:

```php
// S05: SE04_01 = 1 "keine Störungen"
if (value('SE04_01') == 2) {
  question('SE05');   // Art der Störung (Mehrfachauswahl)
}
```

Aufmerksamkeitscheck ohne Abbruch: kein Code nötig, nur Item in der Batterie.

Optionaler Mindset-Block (Hildebrandt et al., 7 Items) nur für Fälle, die schnell sind: nicht empfohlen, weil das die Stichprobe für den Block verzerrt. Entweder ganz rein oder ganz raus (Entscheidung liegt in der Entscheidungsvorlage vom 02.09.).

## 6. Einwilligungstext (Entwurf, DSGVO)

Verantwortliche Stelle: Universität der Bundeswehr München, [Lehrstuhl], in Kooperation mit der Landeshauptstadt München (IT-Referat, KVR). Förderung: BMFTR, DATIpilot.

Zweck: Wissenschaftliche Begleitung der Testwahl. Erhoben werden Einschätzungen zu Technik, Vertrauen und Wahlerleben sowie wenige demografische Angaben in groben Kategorien.

Freiwilligkeit: Teilnahme ist freiwillig; Abbruch jederzeit ohne Nachteile. Keine Auswirkungen auf das Beschäftigungsverhältnis. Die Befragung wird nicht vom Arbeitgeber ausgewertet, sondern von der UniBw.

Anonymität: Keine IP-Adresse, kein Name, keine Personalnummer, keine Verknüpfung mit dem Wahlsystem oder der WiLMA-Anmeldung. Demografie nur in Kategorien, die keine Einzelperson identifizieren (Referatszugehörigkeit nur RIT / KVR / andere).

Speicherung: Auf Servern von SoSci Survey (München) für die Dauer der Erhebung, danach auf Systemen der UniBw. Veröffentlichung nur aggregiert.

Kontakt und Datenschutzbeauftragte: [einsetzen].

Zustimmung: "Ich habe die Informationen gelesen und bin mit der Teilnahme einverstanden." (Pflicht, sonst Ende.)

Vor Feldstart abstimmen mit: Datenschutz UniBw, Personalrat LHM (Beschäftigtenbefragung ist mitbestimmungsrelevant), RIT-I-A2 (Anja Tischer).

## 7. Pretest

SoSci-Pretest-Modus mit Kommentarfunktion, 5 Personen aus RIT/KVR, die nicht zur Stichprobe gehören. Prüfen: Verständlichkeit der Verständnisindex-Optionen, Dauer (Ziel unter 15 Minuten für Variante A), Darstellung auf Mobilgerät (Testwahl läuft mit BundID/BayernID, viele werden am Smartphone antworten), Filterpfad Nicht-Teilnehmende.

## 8. Export und Qualitätsfilter

Export als SPSS oder R (SoSci liefert ein R-Skript mit Labels). Standardvariablen für die Bereinigung: `FINISHED` (1), `MISSING` (unter 20 %), `TIME_SUM` (über 5 Minuten), `DEG_TIME` (Geschwindigkeitsindex unter 100), `MAXPAGE`. Aufmerksamkeitscheck korrekt. Danach Rekodierung der umgepolten Items, Mittelwertskalen, Tage seit Stimmabgabe = Datum(`STARTED`) minus `SZ01`.

fsQCA-Kalibrierung (Outcome BI, Bedingungen TR, TT, IT, SI, ER, PDS) nach den Ankern aus `FRAGEBOGEN_fsQCA_Thaler_Laenge_2026-09-02.md`; hier nur die Regel: Anker werden vor Öffnung der Befragung registriert, nicht aus der Verteilung abgeleitet.

## 9. Offene Entscheidungen

1. Variante A, B oder C (Entscheidungsvorlage empfiehlt A, 79 Items).
2. Wortlaut der Verständnisindex-Optionen mit dem Entwicklerteam abgleichen.
3. Feldende: 09.10. oder später, abhängig vom Rücklauf nach Wahlende.
4. Mitbestimmung: Freigabe der Beschäftigtenbefragung durch den Personalrat der LHM klären.
5. Ob ein Probelauf vor der Testwahl stattfand (dann ist VE01 Pflichtitem mit eigener Option).
