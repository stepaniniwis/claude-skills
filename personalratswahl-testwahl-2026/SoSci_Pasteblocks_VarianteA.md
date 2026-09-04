# SoSci Paste-Blöcke, Variante A (79 Items)

Stand 04.09.2026. Erzeugt aus derselben Itemliste wie `Codebuch_VarianteA_SoSci.csv`. Jeder Codeblock ist so formatiert, dass er direkt in das SoSci-Feld "Items" bzw. "Antwortoptionen" eingefügt werden kann (eine Zeile je Item/Option). Der Skalenanker ist auf den U18-Wortlaut gesetzt ("stimme gar nicht zu"), Open Item bleibt.

## Skalenanker (einmal als Vorlage anlegen, dann bei jeder Skala-Frage 'Skala übernehmen')

```
stimme gar nicht zu
stimme eher nicht zu
teils/teils
stimme eher zu
stimme voll zu
```

Endpunktbenannt reicht: links "stimme gar nicht zu", rechts "stimme voll zu"; die Mitte ist als "teils/teils" beschriftbar (der Analysebericht 3.1 setzt den Crossover auf die beschriftete neutrale Mitte, also Mitte beschriften).

## Seite start

### EW01 (EW): Auswahl, Pflichtfrage

Fragetext:
```
Ich habe die Informationen gelesen und bin mit der Teilnahme einverstanden.
```
Optionen:
```
ja, ich bin einverstanden
nein
```

## Block 1: Testkontext

Instruktion (Textelement TX01): `Zuerst einige Fragen zum Testdurchlauf selbst.`

### TK01 (T1): Auswahl

Fragetext:
```
Auf welchem Gerät haben Sie den Test durchgeführt?
```
Optionen:
```
dienstlicher Rechner
privater Rechner
Smartphone
Tablet
```

### TK02 (T2): Auswahl

Fragetext:
```
Haben Sie den Testdurchlauf vollständig abgeschlossen?
```
Optionen:
```
ja
nein, abgebrochen bei:   [Option mit Eingabefeld]
```

### TK03 (T3): Auswahl

Fragetext:
```
Haben Sie die Möglichkeit genutzt, Ihre Test-Stimme zu überprüfen?
```
Optionen:
```
ja
nein
war mir nicht bekannt
```

### TK04 (T4): Auswahl

Fragetext:
```
Haben Sie ausprobiert, Ihre Test-Stimme zu ändern (erneut abzustimmen)?
```
Optionen:
```
ja
nein
war mir nicht bekannt
```

### TK05 (T5): Auswahl

Fragetext:
```
Wo haben Sie den Test gemacht?
```
Optionen:
```
am Arbeitsplatz
zu Hause
unterwegs
```

### TK06 (T6): Auswahl

Fragetext:
```
Wie haben Sie von der Möglichkeit erfahren, den Testdurchlauf auszuprobieren?
```
Optionen:
```
Intranet oder Rundmail
Vorgesetzte
Kolleg:innen
Personalrat
anders:   [Option mit Eingabefeld]
```

### TK07 (T7): Mehrfachauswahl

Fragetext:
```
Was hat Sie bewogen, am Test teilzunehmen? (Mehrfachnennung möglich)
```
Optionen:
```
Interesse an neuer Technik
Interesse an der Personalratswahl
Bitte von Vorgesetzten oder Kolleg:innen
dienstliche Befassung mit dem Thema
anderes:   [Option mit Eingabefeld]
```

## Block 2: Demografie und Struktur

Instruktion (TX02): `Einige Angaben zu Ihrer Person und Ihrem Arbeitsumfeld. Alle Angaben sind bewusst grob gehalten, damit keine Rückschlüsse auf einzelne Personen möglich sind.`

### DM01 (D1): Auswahl

Fragetext:
```
In welchem Referat arbeiten Sie?
```
Optionen:
```
RIT
KVR
```

### DM02 (D2): Auswahl

Fragetext:
```
Wie alt sind Sie?
```
Optionen:
```
unter 35
35 bis 49
50 und älter
```

### DM03 (D3): Auswahl

Fragetext:
```
Geschlecht
```
Optionen:
```
weiblich
männlich
divers
keine Angabe
```

### DM04 (D4): Auswahl

Fragetext:
```
Seit wie vielen Jahren sind Sie bei der Stadtverwaltung München beschäftigt?
```
Optionen:
```
unter 5 Jahre
5 bis 15 Jahre
über 15 Jahre
```

### DM05 (D5): Auswahl

Fragetext:
```
Wie häufig arbeiten Sie mobil, also außerhalb Ihres Arbeitsplatzes?
```
Optionen:
```
(praktisch) nie
teilweise
überwiegend
```

### DM06 (D6): Auswahl

Fragetext:
```
Welchen Anteil Ihrer Arbeitszeit verbringen Sie am Bildschirm?
```
Optionen:
```
praktisch nie
unter einem Viertel
etwa die Hälfte
mehr als drei Viertel
fast vollständig
```

### DM07 (D7): Auswahl

Fragetext:
```
Haben Sie an Ihrem Arbeitsplatz einen dienstlichen Rechner- oder Gerätezugang?
```
Optionen:
```
eigener
gemeinsam genutzt
keiner
```

### DM08 (D8): Skala 5, endpunktbenannt

Fragetext: `Wie schätzen Sie Ihre Technologie- und Internetkompetenz ein?`  Pole: `sehr gering` / `sehr hoch`

### DM09 (D9): Skala 5, Zustimmungsanker

Item: `Ich probiere gerne neue Apps und digitale Dienste aus.`

### DM10 (D10): Auswahl

Fragetext:
```
An wie vielen Personalratswahlen haben Sie bisher teilgenommen?
```
Optionen:
```
0
1
2
3 oder mehr
```

### DM11 (D11): Skala 5, endpunktbenannt [Variante A, B]

Fragetext: `Wie gut fühlten Sie sich vor dem Test über den Ablauf informiert?`  Pole: `sehr schlecht` / `sehr gut`

### DM12 (D12): Skala 5, endpunktbenannt

Fragetext: `Wie haben Sie VOR dem Testdurchlauf über digitales Wählen gedacht?`  Pole: `sehr negativ` / `sehr positiv`

### DM13 (D13): Auswahl

Fragetext:
```
Der Test hat meine Sicht auf digitales Wählen verändert.
```
Optionen:
```
verbessert
unverändert
verschlechtert
```

### DM14 (D14): Skala 5, endpunktbenannt [Variante A, B]

Fragetext: `Wie zufrieden sind Sie damit, wie die Mitbestimmung in Ihrer Dienststelle funktioniert?`  Pole: `sehr unzufrieden` / `sehr zufrieden`

## Block 3: Akzeptanz

Instruktion (TX03): `Die folgenden Aussagen beziehen sich auf die digitale Stimmabgabe, wie Sie sie im Testdurchlauf erlebt haben. Bitte geben Sie an, wie sehr Sie zustimmen.`

### BI01: Behavioral Intention

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Ich würde bei zukünftigen Wahlen gerne wieder digital abstimmen.
Ich würde die digitale Wahl einer Papier- oder Briefwahl vorziehen.
Ich würde die digitale Wahl meinen Kolleg:innen empfehlen.
```

| SoSci-Variable | Paper-Code |
|---|---|
| BI01_01 | BI1 |
| BI01_02 | BI2 |
| BI01_03 | BI3 |

### PE01: Performance Expectancy

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Ich finde es sinnvoll, dass man bei dieser Wahl digital abstimmen kann.
Durch die digitale Wahl habe ich Zeit und Aufwand gespart.
Die digitale Abstimmung ist praktischer als eine Papier- oder Briefwahl.
```

| SoSci-Variable | Paper-Code |
|---|---|
| PE01_01 | PE1 |
| PE01_02 | PE2 |
| PE01_03 | PE3 |

### EE01: Effort Expectancy

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Die digitale Stimmabgabe im Test war einfach zu bedienen.
Ich habe auf Anhieb verstanden, wie die digitale Wahl funktioniert.
Es war leicht für mich zu verstehen, wie ich digital wähle.
```

| SoSci-Variable | Paper-Code |
|---|---|
| EE01_01 | EE1 |
| EE01_02 | EE2 |
| EE01_03 | EE3 |

### SI01: Social Influence

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Meine Kolleg:innen finden es gut, dass digital gewählt werden konnte.
Personen in meinem Umfeld würden es befürworten, wenn ich digital wähle.
Personen, deren Meinung mir wichtig ist, würden digitales Wählen für richtig halten.
```

| SoSci-Variable | Paper-Code |
|---|---|
| SI01_01 | SI1 |
| SI01_02 | SI2 |
| SI01_03 | SI3 |

### FC01: Facilitating Conditions

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Ich hatte alles, was ich brauchte, um digital zu wählen.
Ich hatte das nötige Wissen, um die digitale Wahl zu nutzen.
Ich konnte die digitale Wahl ungestört durchführen.
```

| SoSci-Variable | Paper-Code |
|---|---|
| FC01_01 | FC1 |
| FC01_02 | FC2 |
| FC01_03 | FC3 |

## Block 4: Transfer auf die echte Wahl

Instruktion (TX04): `Nun zwei Aussagen zur echten Personalratswahl, nicht zum Test.`

### BR01: Transfer (BI-R2r invers, nicht in SoSci umpolen)

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Bei der echten Personalratswahl würde ich digital abstimmen.
Ich hätte Bedenken, bei der echten Wahl digital abzustimmen.
```

| SoSci-Variable | Paper-Code |
|---|---|
| BR01_01 | BI-R1 |
| BR01_02 | BI-R2r |

## Block 5: Vertrauen

Instruktion (TX05): `Die folgenden Aussagen betreffen digitales Wählen als Verfahren, unabhängig vom Testdurchlauf.`

### TR01: General Trust

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Ich halte digitale Wahlen für vertrauenswürdig.
Digitale Wahlen können ihren Zweck genauso gut erfüllen wie Papierwahlen.
```

| SoSci-Variable | Paper-Code |
|---|---|
| TR01_01 | TR1 |
| TR01_02 | TR2 |

### TT01: Technological Trust

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Ich halte die Technik hinter digitalen Wahlen für zuverlässig.
Ich vertraue darauf, dass das System einer digitalen Wahl zuverlässig funktioniert.
Bei einer digitalen Wahl kann niemand sehen, was ich gewählt habe.
Die Datenübertragung bei einer digitalen Wahl ist sicher.
Eine digitale Wahl ist schwer zu manipulieren.
```

| SoSci-Variable | Paper-Code |
|---|---|
| TT01_01 | TT1 |
| TT01_02 | TT2 |
| TT01_03 | TT3 |
| TT01_04 | TT_5 |
| TT01_05 | TT4 |

### IT01: Institutional Trust

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Die Verantwortlichen führen die Wahl fair und korrekt durch.
Meine Dienststelle schützt meine Stimme.
Die Personen, die diese Wahl organisieren, haben das im Griff.
```

| SoSci-Variable | Paper-Code |
|---|---|
| IT01_01 | IT1 |
| IT01_02 | IT2 |
| IT01_03 | IT3 |

### VT01: Vendor Trust

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Ich vertraue dem Unternehmen, das die Wahlsoftware bereitstellt.
Ich möchte wissen, wer die Wahlsoftware betreibt.
Bei einer Wahl sollte die Technik in öffentlicher Hand liegen.
```

| SoSci-Variable | Paper-Code |
|---|---|
| VT01_01 | VT1 |
| VT01_02 | VT2 |
| VT01_03 | VT3 |

### QS01: Aufmerksamkeitsprüfung Q1 (nach dem Block-5-Inhalt auf derselben Seite)

Fragetyp: Skala, 1 Item, keine Randomisierung.

```
Bitte kreuzen Sie hier "stimme gar nicht zu" an.
```

## Block 6: Legitimität

Instruktion (TX06): `Bei den nächsten Aussagen geht es darum, wie digitales Wählen in Ihrem Umfeld allgemein gesehen wird, unabhängig von Ihrer eigenen Meinung. Bei der letzten Aussage geht es um Ihre eigene Sicht.`

### LG01: Validity und Propriety (feste Reihenfolge, PROP1 zuletzt; PROP1 nur Variante A, B)

Fragetyp: Skala (endpunktbenannt), 5 Stufen. KEINE Randomisierung, die Instruktion verweist auf 'die letzte Aussage'.

```
Die meisten Beschäftigten der Stadtverwaltung halten digitales Wählen für eine angemessene Art, den Personalrat zu wählen.
Unabhängig davon, was ich selbst denke: Digitales Wählen gilt in meinem Arbeitsumfeld allgemein als akzeptierte Form der Stimmabgabe.
Ich selbst halte digitales Wählen für eine angemessene Art, den Personalrat zu wählen.
```

| SoSci-Variable | Paper-Code |
|---|---|
| LG01_01 | VAL1 |
| LG01_02 | VAL2 |
| LG01_03 | PROP1 |

## Block 7: Prüfbarkeit und Re-Voting

Instruktion (TX07): `Es folgen Aussagen zur Überprüfbarkeit der Stimme und zur Möglichkeit, die Test-Stimme zu ändern.`

### PL01: PLT-V Verifikationswunsch (PLTV3 invers)

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Ich möchte selbst verstehen können, warum das System sicher ist, nicht nur hören, dass es sicher sein soll.
Mein Vertrauen würde steigen, wenn ich die korrekte Zählung meiner Stimme selbst prüfen könnte.
Es reicht mir, wenn Fachleute das System geprüft haben.
```

| SoSci-Variable | Paper-Code |
|---|---|
| PL01_01 | PLTV1 |
| PL01_02 | PLTV2 |
| PL01_03 | PLTV3 |

### VE01: Verifikation

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Die Möglichkeit, meine Stimme zu überprüfen, war mir wichtig.
Durch die Überprüfbarkeit habe ich mehr Vertrauen in das Ergebnis.
```

| SoSci-Variable | Paper-Code |
|---|---|
| VE01_01 | VER1 |
| VE01_02 | VER2 |

### RV01: Re-Voting (RV2 invers)

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Dass ich meine Stimme während des Wahlzeitraums ändern könnte, finde ich beruhigend.
Dass eine abgegebene Stimme änderbar ist, verunsichert mich.
```

| SoSci-Variable | Paper-Code |
|---|---|
| RV01_01 | RV1 |
| RV01_02 | RV2 |

## Block 8: Erleben der Stimmabgabe

Instruktion (TX08): `Die folgenden Aussagen beziehen sich auf Ihre Stimmabgabe im Testdurchlauf.`

### CL01: Experiential Realness (Variante B/C: nur CL01_03, CL01_04)

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Die Stimmabgabe hat sich für mich konkret und greifbar angefühlt.
Ich hatte das Gefühl, wirklich "dabei" zu sein.
Meine Stimme abzugeben hat sich "real" angefühlt.
Es hat sich angefühlt, als würde meine Stimme wirklich "ankommen".
Der Wahlakt war für mich ein unmittelbares, direktes Erlebnis.
```

| SoSci-Variable | Paper-Code |
|---|---|
| CL01_01 | CL1 |
| CL01_02 | CL2 |
| CL01_03 | CL3 |
| CL01_04 | CL4 |
| CL01_05 | CL_5 |

### CV01: Entscheidungsfestigkeit

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Ich stehe voll hinter meiner Wahlentscheidung.
Meine Wahlentscheidung fühlt sich endgültig und verbindlich an.
Nach der Stimmabgabe war mir klar: Das war meine Entscheidung.
```

| SoSci-Variable | Paper-Code |
|---|---|
| CV01_01 | CVC1 |
| CV01_02 | CVC2 |
| CV01_03 | CVC3 |

### PD01: Perceived Democratic Significance (Variante B/C: nur PD01_02, PD01_06)

Fragetyp: Skala (endpunktbenannt), 5 Stufen, Items in zufälliger Reihenfolge anzeigen.

```
Durch meine Stimmabgabe habe ich einen echten Beitrag geleistet.
Meine Stimme hat Gewicht und Bedeutung.
Die Teilnahme an dieser Wahl war für mich ein bedeutsamer Moment.
Ich empfinde Stolz, wenn ich mein Wahlrecht ausübe.
Ich fühle mich als aktiver Teil der demokratischen Gemeinschaft.
Meine Teilnahme an der Wahl macht einen Unterschied.
```

| SoSci-Variable | Paper-Code |
|---|---|
| PD01_01 | PDS1 |
| PD01_02 | PDS2 |
| PD01_03 | PDS3 |
| PD01_04 | PDS4 |
| PD01_05 | PDS_5 |
| PD01_06 | PDS_6 |

## Block 9: Freitext

### FT01 (F1): Text, mehrzeilig

```
Was hat aus Ihrer Sicht bei diesem Test gut funktioniert, und was nicht?
```

### FT02 (F2): Text, mehrzeilig

```
Hat sich die Stimmabgabe für Sie anders angefühlt als bei früheren Wahlen? Wenn ja, wie?
```

## Block 10: Qualitätssicherung

### QS02 (Q2): Skala, 1 Item

```
Ich habe die Fragen sorgfältig und ehrlich beantwortet.
```

### IV01: Interne Variablen

Fragetyp "Interne Variablen", 1 Variable (Text). Wird per PHP mit der Blockreihenfolge befüllt, erscheint nie im Fragebogen.
