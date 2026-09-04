# SoSci Survey: Aufbau der Begleitbefragung zum Testdurchlauf (Variante A, 79 Items)

Stand 04.09.2026, v1.0. Ersetzt das Gerüst vom selben Tag, das noch auf dem Konstruktrahmen vom 26.08. beruhte (Dispositionsblock, Situationsstärke). Maßgeblich ist jetzt `FRAGEBOGEN_Variante_A_Messkontinuitaet_2026-09-02.md` mit der fsQCA-Festlegung aus `FRAGEBOGEN_fsQCA_Thaler_Laenge_2026-09-02.md`. Zugehörige Dateien in diesem Ordner:

- `SoSci_Pasteblocks_VarianteA.md`: alle Fragetexte, Items und Optionen als Einfügeblöcke, Frage für Frage.
- `Codebuch_VarianteA_SoSci.csv`: SoSci-Variable, Paper-Code, Block, Konstrukt, Wortlaut, Format, Werte, Umpolung, fsQCA-Rolle, Thaler-Tag, Status, Variantenzugehörigkeit (A/B/C).

Beide Dateien sind aus einer Itemliste erzeugt; Kontrollzählung 79 (77 geschlossen, 2 Freitext), Variante B 72, Variante C 69, identisch mit der Entscheidungsvorlage.

## 1. Warum A gebaut wird, auch wenn die Runde noch entscheidet

Die Varianten unterscheiden sich nur durch Streichungen (Blockvergleich, Zeilen 2, 6, 8a, 8c). In SoSci ist Löschen eines Items ein Klick, Nachtragen erfordert Neuanlage, Testlauf und Codebuchpflege. Deshalb wird A vollständig angelegt; die Umschaltung auf B oder C steht in Abschnitt 9 und dauert unter zehn Minuten. Das Codebuch trägt die Variantenzugehörigkeit je Item, damit der Export nach der Entscheidung ohne Umschlüsselung lesbar bleibt.

## 2. Projektanlage

| Einstellung | Wert | Grund |
|---|---|---|
| Sprache, Anrede | Deutsch, Sie | Verwaltungskontext |
| Zugang | Allgemeiner anonymer Link, kein Personenbezug | Freigabebedingung Anonymität (Analysebericht 6.3); Rekrutierung läuft über die WiLMA-Kampagne und Rundmail |
| IP-Adresse speichern | aus | Anonymität |
| Fortsetzen nach Unterbrechung | aus | eine Sitzung, keine Wiederaufnahme mit veränderter Blockreihenfolge |
| Zurück-Button | aus | verhindert Nacharbeiten früherer Blöcke nach Sicht auf spätere |
| Fortschrittsbalken | an | 16 bis 19 Minuten, Abbruchrisiko ist das Hauptargument gegen A |
| Pflichtangaben | Skalen: "Antwort erforderlich" mit Hinweis, kein Blockieren | Missing bleibt messbar, Abbruch wird nicht provoziert |
| Feldzeit | mit Testwahl-Start 14.09.2026 öffnen, mindestens zwei Wochen nach Testwahl-Ende (25.09.) offen halten | Nachzügler; Abschlussquoten-Monitoring gegen die Schwellen 57,1 % (560 Anmeldungen) bzw. 32,0 % (1.000) |

Dauerangabe im Einladungstext: "etwa 15 bis 20 Minuten" (Entscheidungsvorlage, ehrliche Angabe).

## 3. Namenskonvention

SoSci verlangt Fragen-IDs aus zwei Buchstaben und zwei Ziffern; Items erhalten automatisch `_01`, `_02` … Die Paper-Codes (BI1, TT_5, PDS_6 …) bleiben im Codebuch und in der Auswertung erhalten; die Zuordnung läuft immer über den Itemtext, nie über die laufende Nummer (TT_5-Falle aus dem Wahrheitsdokument 4.5: in SoSci ist TT_5 die Variable `TT01_04`, TT4 ist `TT01_05`, weil die Reihenfolge der Variante A gefolgt wird).

| Block | SoSci-Fragen | Fragetyp |
|---|---|---|
| Einstieg | `EW01` | Auswahl, Pflicht |
| 1 Testkontext | `TK01` bis `TK07` | Auswahl; `TK07` Mehrfachauswahl; `TK02`, `TK06`, `TK07` mit Eingabefeld an einer Option |
| 2 Demografie | `DM01` bis `DM14` | Auswahl; `DM08`, `DM09`, `DM11`, `DM12`, `DM14` Skala 5 |
| 3 Akzeptanz | `BI01`, `PE01`, `EE01`, `SI01`, `FC01` | Skala 5, Items randomisiert |
| 4 Transfer | `BR01` | Skala 5, 2 Items |
| 5 Vertrauen | `TR01`, `TT01`, `IT01`, `VT01`, danach `QS01` (Q1) | Skala 5, Items randomisiert; Q1 einzeln |
| 6 Legitimität | `LG01` | Skala 5, feste Reihenfolge |
| 7 Prüfbarkeit | `PL01`, `VE01`, `RV01` | Skala 5, Items randomisiert |
| 8 Erleben | `CL01`, `CV01`, `PD01` | Skala 5, Items randomisiert |
| 9 Freitext | `FT01`, `FT02` | Text mehrzeilig |
| 10 Qualität | `QS02` | Skala 5, 1 Item |
| intern | `IV01` | Interne Variable (Blockreihenfolge) |
| Instruktionen | `TX01` bis `TX08` | Textelemente |

## 4. Skalen

Eine Skalenvorlage anlegen und bei jeder Skala-Frage übernehmen: 5 Stufen, endpunktbenannt, Mitte beschriftet ("teils/teils"), Werte 1 bis 5. Der Analysebericht setzt den fsQCA-Crossover auf die beschriftete neutrale Mitte (3.1), deshalb muss die Mitte im Fragebogen sichtbar beschriftet sein.

Ankerwortlaut: In den Paste-Blöcken steht der U18-Wortlaut "stimme gar nicht zu … stimme voll zu", weil Messkontinuität der Zweck der Variante A ist. Die Itembank v1.1 verwendet "stimme überhaupt nicht zu". Das ist Open Item der Entscheidungsvorlage; wer v1.1 wählt, ändert die Vorlage einmal und den Wortlaut von Q1 (`QS01`).

Umgepolte Items (BI-R2r `BR01_02`, PLTV3 `PL01_03`, RV2 `RV01_02`) werden nicht in SoSci gedreht, sondern im Rohexport belassen und in der Auswertung rekodiert. Der Rohdatensatz entspricht so dem Instrument.

## 5. Randomisierung

Vorgabe aus Variante A: Blockreihenfolge der Einstellungsblöcke 3 bis 8 randomisieren, Itemreihenfolge innerhalb der Blöcke randomisieren. Umsetzung:

- **Items innerhalb einer Batterie:** Option "Items in zufälliger Reihenfolge anzeigen" in jeder Skala-Frage. Ausnahmen: `LG01` (Instruktion verweist auf "die letzte Aussage"), `BR01` (2 Items, egal), `QS01`, `QS02`.
- **Batterien innerhalb eines Blocks:** per PHP in zufälliger Reihenfolge aufgerufen (Abschnitt 6). Damit bleibt die Konstruktgruppierung wie bei U18 erhalten (dort wurde innerhalb der Konstrukte randomisiert), und die Blockvorgabe "innerhalb der Blöcke" ist trotzdem erfüllt. Wer stattdessen alle Items eines Blocks in einer einzigen Matrix mischen will, legt je Block eine Skala-Frage mit allen Items an; das bricht die Konstruktgruppierung gegenüber U18 und wird nicht empfohlen.
- **Blöcke 3 bis 8:** einmal pro Fall gemischt, Reihenfolge in `IV01_01` gespeichert, Anzeige über sechs Positionsseiten (Abschnitt 6). Block 4 (Transfer) folgt inhaltlich auf Block 3; wenn die Runde Block 4 fest hinter Block 3 haben will, im Array unten `B4` entfernen und auf der Seite von B3 mit anhängen.
- Q1 hängt fest an Block 5 und wandert mit ihm.

## 6. Seitenstruktur und PHP-Code

```
start        TX00 Einladung/Studieninfo, EW01                 PHP: Filter Einwilligung
block1       TX01, TK01 … TK07
block2       TX02, DM01 … DM14
mix          (leere Seite, nur PHP)                          PHP: Blockreihenfolge ziehen
pos1 … pos6  (je eine Seite, nur PHP)                        PHP: Block laut Position anzeigen
freitext     FT01, FT02
ende_q       QS02
ende         Dank
ende_nein    Ende ohne Einwilligung
```

Seite `start`:

```php
if (value('EW01') == 2) {
  goToPage('ende_nein');
}
```

Seite `mix` (nur PHP, keine Fragen):

```php
if (!isset($blockOrder)) {
  $blockOrder = array('B3', 'B4', 'B5', 'B6', 'B7', 'B8');
  shuffle($blockOrder);
  registerVariable($blockOrder);
  put('IV01_01', implode(',', $blockOrder));
}
goToPage('pos1');
```

Seiten `pos1` bis `pos6`, identischer Code bis auf den Index (`$blockOrder[0]` auf pos1, `[1]` auf pos2 … `[5]` auf pos6):

```php
$b = $blockOrder[0];   // pos1: [0], pos2: [1], pos3: [2], pos4: [3], pos5: [4], pos6: [5]

if ($b == 'B3') {
  question('TX03');
  $q = array('BI01', 'PE01', 'EE01', 'SI01', 'FC01');
  shuffle($q);
  foreach ($q as $id) { question($id); }
}
if ($b == 'B4') {
  question('TX04');
  question('BR01');
}
if ($b == 'B5') {
  question('TX05');
  $q = array('TR01', 'TT01', 'IT01', 'VT01');
  shuffle($q);
  foreach ($q as $id) { question($id); }
  question('QS01');          // Q1 Aufmerksamkeitsprüfung, fest nach Block 5
}
if ($b == 'B6') {
  question('TX06');
  question('LG01');          // feste Itemreihenfolge, PROP1 zuletzt
}
if ($b == 'B7') {
  question('TX07');
  $q = array('PL01', 'VE01', 'RV01');
  shuffle($q);
  foreach ($q as $id) { question($id); }
}
if ($b == 'B8') {
  question('TX08');
  $q = array('CL01', 'CV01', 'PD01');
  shuffle($q);
  foreach ($q as $id) { question($id); }
}
```

Hinweise zur SoSci-Mechanik: `registerVariable()` hält das Array über Seiten hinweg, `put()` schreibt in die interne Variable, `question()` rendert eine Katalogfrage auf der aktuellen Seite. Die Batteriereihenfolge innerhalb eines Blocks wird nicht gespeichert; wer sie braucht, speichert `implode(',', $q)` in weiteren internen Variablen `IV01_02` bis `IV01_05`. Die Anzahl Fragen je Seite ist bei B3 (15 Items in 5 Batterien) und B8 (14 Items in 3 Batterien) die höchste; im Pretest auf dem Smartphone prüfen, bei Bedarf B3 auf zwei Positionsseiten teilen.

Freitextfilter: `TK02` Option 2 trägt das Eingabefeld direkt an der Option ("nein, abgebrochen bei:"), es ist keine Sprungregel nötig. Es gibt sonst keine Filter (Einmodus-Design, alle Items gelten für alle).

## 7. Einladung und Einwilligung (Textelement TX00, Entwurf)

Titel: Befragung zum Testdurchlauf der digitalen Personalratswahl.

Zweck: Die Landeshauptstadt München erprobt gemeinsam mit der Universität der Bundeswehr München einen Prototyp für die digitale Stimmabgabe bei Personalratswahlen (Förderung BMFTR, DATIpilot). Diese Befragung erfasst, wie Beschäftigte den Testdurchlauf erlebt haben und wie sie digitales Wählen bewerten.

Dauer: etwa 15 bis 20 Minuten.

Freiwilligkeit: Die Teilnahme ist freiwillig. Ein Abbruch ist jederzeit ohne Nachteile möglich. Die Teilnahme hat keine Auswirkungen auf das Beschäftigungsverhältnis.

Anonymität: Die Befragung ist anonym. Es werden keine Namen, Personalnummern, IP-Adressen oder Organisationseinheiten unterhalb des Referats erhoben. Alter und Beschäftigungsdauer werden nur in groben Spannen erfragt. Es gibt keine Verknüpfung mit dem Wahlsystem oder der Anmeldung zum Test. Ausgewertet wird nur in Gruppen mit mindestens fünf Personen; die Kombination aus Referat, Altersgruppe und Geschlecht wird nie berichtet.

Verantwortlich, Speicherung, Kontakt, Datenschutzbeauftragte: [einsetzen: Lehrstuhl UniBw; Speicherung auf SoSci-Servern in München für die Dauer der Erhebung, danach UniBw; Kontaktadresse; DSB].

Freigabe vor Feldstart durch Personalrat und Datenschutzbeauftragte der LHM ist Voraussetzung (Analysebericht 6.3). Die Freigabevorlage braucht die finale Variante.

## 8. Pretest

SoSci-Pretest-Modus mit Kommentarfunktion, fünf Personen aus RIT und KVR außerhalb der Stichprobe, davon mindestens zwei am Smartphone. Pflichtprüfungen aus der Entscheidungsvorlage: Zeitmessung (`TIME_SUM`; kippt A über 20 Minuten, dann B), kognitiver Pretest für VAL1, VAL2, PROP1, T6, T7, die D-Formate und PDS4 (Wahlrechtsbezug im Test, nicht umformulieren). Dazu: Blockrandomisierung anhand von `IV01_01` über mehrere Testfälle kontrollieren, Q1 sichtbar hinter Block 5, Eingabefelder an den Optionen von TK02, TK06, TK07.

## 9. Umschalten auf Variante B oder C

Variante B: in `CL01` die Items `_01`, `_02`, `_05` löschen (bleiben: "real angefühlt", "wirklich ankommen"); in `PD01` die Items `_01`, `_03`, `_04`, `_05` löschen (bleiben: "Gewicht und Bedeutung", "macht einen Unterschied"). Ergebnis 72 Items.

Variante C zusätzlich: `LG01_03` (PROP1) löschen, `DM11` und `DM14` von der Seite `block2` entfernen. Ergebnis 69 Items. Die Instruktion TX06 dann kürzen (kein Satz mehr zur "letzten Aussage").

Löschen vor Feldstart, nie im Feld; die Variablennummern der verbleibenden Items bleiben stabil, das Codebuch führt die Zugehörigkeit in der Spalte `varianten`.

## 10. Export, Bereinigung, Aufbereitung

Export als R-Skript oder SPSS mit Labels. Bereinigungsregel vor der Analyse als `_MASSGEBLICH.md` neben die Rohdaten legen (Analysebericht 3.7). Vorschlag, vorab zu binden:

- `FINISHED == 1`, `MISSING < 20`, `TIME_SUM >= 300` Sekunden, `DEG_TIME < 100`, `QS01_01 == 1` (Q1 korrekt), `EW01 == 1`.
- Rekodierung: `BR01_02`, `PL01_03`, `RV01_02` mit `6 - x`.
- Mittelwertskalen für Outcome und Bedingungen: BI (`BI01_01:_03`), SI (`SI01_01:_03`), TR (`TR01_01:_02`), TT (`TT01_01:_05`), IT (`IT01_01:_03`), ER (`CL01_01:_05`), PDS (`PD01_01:_06`); Robustheits-Outcome BI-R (`BR01_01`, `BR01_02` rekodiert).
- FC-Abbruchregel: α < 0,70, dann nur Einzelitem-Deskription.

R-Skizze (Paket `QCA`), Kalibrierung Option A mit festen Ankern 2/3/4 und dem 0,001-Zuschlag gegen exakte 0,5-Fälle:

```r
library(dplyr); library(QCA)
d <- d %>% mutate(
  BR01_02r = 6 - BR01_02, PL01_03r = 6 - PL01_03, RV01_02r = 6 - RV01_02,
  BI  = rowMeans(across(BI01_01:BI01_03)),
  SI  = rowMeans(across(SI01_01:SI01_03)),
  TR  = rowMeans(across(TR01_01:TR01_02)),
  TT  = rowMeans(across(TT01_01:TT01_05)),
  IT  = rowMeans(across(IT01_01:IT01_03)),
  ER  = rowMeans(across(CL01_01:CL01_05)),
  PDS = rowMeans(across(PD01_01:PD01_06)),
  BIR = rowMeans(cbind(BR01_01, BR01_02r)))
cal <- function(x) { m <- calibrate(x, type = "fuzzy", thresholds = c(2, 3, 4)); ifelse(m == 0.5, m + 0.001, m) }
fz <- d %>% transmute(across(c(BI, SI, TR, TT, IT, ER, PDS), cal))
# Vor der Truth Table: Deckeneffekt-Bindung (Entscheidungsvorlage): Anteil > 0,95 oder < 0,05 je Bedingung; > 80 % = quasi-konstant.
```

Truth-Table-Schwellen laut Analysebericht 3.2: raw consistency 0,80, PRI 0,70, Frequenz nach Fallzahl (über 150 Fälle: 3), Notwendigkeitsprüfung vorab (3.3), Negationsanalyse für ~BI verpflichtend (3.5), Robustheitsvarianten 5/3/1, Perzentil p20/p50/p80, Consistency 0,75 und 0,85, Frequenz ±1 (3.6).

## 11. Offene Punkte vor Feldstart

1. Variantenentscheidung (A empfohlen); danach Freigabe Personalrat und DSB.
2. Skalenanker: U18-Wortlaut (voreingestellt) oder v1.1.
3. Wortgleich-Spannung SI2, SI3, IT3: U18-Wortlaut wiederherstellen oder Adaption als Bruch dokumentieren. Bei Wiederherstellung nur den Itemtext in `SI01_02`, `SI01_03`, `IT01_03` tauschen.
4. Block 4 fest hinter Block 3 oder frei randomisiert (Abschnitt 5).
5. Batteriereihenfolge je Block speichern (vier weitere interne Variablen) oder nicht.
6. Verteilung der Anmeldungen auf RIT und KVR (referatsgetrennte fsQCA).
7. Registry-Dokument mit Kalibrierung, Deckeneffekt-Bindung, Truth-Table-Schwellen, Bereinigungsregel vor Öffnung der Befragung datiert ablegen.
