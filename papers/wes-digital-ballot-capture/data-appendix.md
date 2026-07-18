# Data Appendix: WES Pilot Evaluation, Munich Municipal Election 2026

Quelldateien (nicht im Repo, liegen lokal vor):
- `Evaluierungsbericht_Einsatz_des_Wahllokalerfassungssystems_WES_POC.pdf` (KVR-interner Evaluierungsbericht, 19 Seiten)
- `Export_13042026_FragebogenWESWahlhelfende_Auswertung.xlsx` (WES-Wahlhelfenden-Befragung, n=102 auswertbar)
- `Export_13042026_FragebogenWahlhelfende_Allg._Auswertung.xlsx` (Allgemeine Wahlhelfenden-Befragung, n=3.198)

## 1. Prozesskennzahlen (Bericht, Kap. 7)

| Prozessschritt | Zeitaufwand |
|---|---|
| Erfassung eines Stadtratsstimmzettels | ca. 60 Sek. (bis 100 Sek.) |
| Beschlussfassung über Stimmzettel | ca. 1 Min. |
| Zusammenführung der Daten (3 PCs, USB) | ca. 13–15 Min. |
| Urnenöffnung, Verpackung, Niederschrift | ca. 30 Min. |
| Vorbereitung/Nacharbeit (mengenunabhängig) | ca. 45 Min. |

Rahmen: 8–9 Wahlvorstandsmitglieder, 3 Erfassungsteams, ca. 400 Stimmzettel in ca. 3 h (19:30–22:30), ca. 60 Stimmzettel pro Team und Stunde. Manuelle Referenz: ca. 3 Min./Stimmzettel, ca. 10 Personen, Abschluss häufig Folgetag.

## 2. Berichtigungsquoten (Bericht, Kap. 8/10)

| Gruppe | Bezirke | Berichtigungen | Quote |
|---|---|---|---|
| WES (digital) | 23 | 0 | 0,0 % |
| Vergleichsgruppe (analog, Nr. 1950–1999) | 27 | 1 | 3,7 % |
| Alle konventionellen Briefwahlbezirke | 667 | 35 | 5,2 % |
| davon Standort MOC | – | – | 9,7 % |
| davon Standort Messe Riem | – | – | 4,4 % |

Zusätzlich: 307 beschlussbedürftige Stimmzettel in WES-Bezirken ohne nachträgliche Korrektur; Abweichung ungeprüftes vs. amtliches Endergebnis max. 0,3 Prozentpunkte; Anteil ungültiger Stimmzettel in beiden Gruppen nahezu identisch.

### Inferenzstatistik (eigene Berechnung)

- WES 0/23 vs. alle konventionellen 35/667: einseitiger Fisher-Exakt-Test **p = 0,296**
- WES 0/23 vs. Vergleichsgruppe 1/27: einseitiger Fisher-Exakt-Test **p = 0,54**
- Binomial-Check: P(0 von 23 | p = 0,0525) = 0,289

**Konsequenz für das Manuskript:** Die Formulierung "signifikante Verbesserung" aus dem Bericht ist statistisch nicht haltbar und wird im Paper nicht übernommen. Framing: mechanismus-konsistentes, richtungsuniformes, aber nicht signifikantes Qualitätssignal.

## 3. WES-Wahlhelfenden-Befragung (n=102 auswertbar, Rücklauf ~50 % von 203 Geschulten)

Item-n variiert; Prozentwerte auf antwortende n bezogen.

| Item | Verteilung |
|---|---|
| B1 Rolle | Beisitzer*in 60 (62,5 %), Wahlvorsteher*in/Stv. 18 (18,8 %), Schriftführer*in/Stv. 18 (18,8 %), n=96 |
| B2 Schon Wahlhelfer*in gewesen | Ja 72/96 (75,0 %) |
| B32 Davon schon Kommunalwahl | Ja 42/72 (58,3 %) |
| B33 Zufriedenheit WES vs. manuell (nur Erfahrene) | Sehr gut 41/42 (97,6 %), Eher gut 1/42 |
| C1 WES-Schulung besucht | Ja 88/95 (92,6 %) |
| C2 Unterlagen hilfreich | Ja 76/88 (86,4 %), Teilweise 11, Nein 1 |
| D1 Zurechtkommen mit WES | Sehr gut 82/92 (89,1 %), Eher gut 10/92 (10,9 %), 95%-CI sehr gut [81,1; 94,0] |
| D2 Durch Schulung vorbereitet | Sehr gut 72/85 (84,7 %), Eher gut 12, Eher schlecht 1 |
| D5 Benutzerfreundlichkeit | Sehr gut 71/92 (77,2 %), Eher gut 20 (21,7 %), Eher schlecht 1 |
| D6 Niederschrift-Erstellung | Sehr einfach 44/86 (51,2 %), Einfach 37 (43,0 %), Aufwendig 4, Sehr aufwendig 1 |
| D7 WES wieder einsetzen | Ja 92/92 (100 %), 95%-CI [96,0; 100] |
| F1 BWST konnte helfen | Ja 76/91 (83,5 %), Teilweise 8, Keine Probleme 7, Nein 0 |
| F2 Betreuung BWST | Sehr gut 78/92 (84,8 %), Eher gut 14 (15,2 %) |
| F3 Standort geeignet | Ja 89/91 (97,8 %) |

### Ungeschulte Wahlhelfende (Pivot ZF1)

- Mit Schulung (n=85): Sehr gut 89,4 %, Eher gut 10,6 %
- Ohne Schulung (n=7): Sehr gut 85,7 % (6/7), Eher gut 14,3 % (1/7); alle 7 nutzten die Kurzübersicht

### Vergleich mit allgemeiner Befragung (identische Items)

| Item | WES | Allgemein |
|---|---|---|
| F1 „mir konnte nicht geholfen werden" | 0 % | 1,1 % (9/842) |
| F2 Betreuung sehr/eher gut | 100 % | 95,2 % (801/841) |

## 4. Freitext-Themen (informelle Codierung, WES-Befragung)

**Positiv (häufig):** praktische Übung als wertvollster Schulungsteil; spürbare Entlastung vs. manuelle Auszählung; explizite Forderungen nach flächendeckendem Rollout (≥8 Nennungen); Verknüpfung WES ↔ Bereitschaft, wieder zu helfen.

**Defekte/Verbesserungen (häufig):** USB-Stick-Zusammenführung fehleranfällig/umständlich (mehrfach, inkl. unklarer Stick-Benamung); Eingabe-Bug mit plötzlich hochgezählten Stimmen (mehrfach berichtet, mühsam reversibel); Wunsch nach 4. Laptop pro Gremium (modaler Verbesserungsvorschlag); Drucker-/Ausdruck-Umweg bei Niederschrift; Wunsch nach Online-Bereitstellung statt USB; Hinweis auf schwaches Hallen-Internet als Randbedingung; Wunsch nach Kürzel-Übersichtstabelle für Experteneingabemodus; Excel-artige „Runterzieh"-Funktion für Listenplätze.

## 5. Kontextzahlen (Bericht)

- 23 von 690 Briefwahlbezirken digital; zentrale Auszählung MOC Atrium 3.1
- 203 Geschulte, 18 Termine, 10 Trainer*innen, je 3,5 h, Praxisübung mit 150 statt 50 Stimmzetteln
- 108 USB-Sticks (92 Einsatz, 16 Reserve); 3 Laptops + 3 WES-Sticks je Gremium; verschlüsselter Transfer-Stick an WAS
- Belastbare Zwischenergebnisse nach ca. 30 Min.; vollständige Daten zentral erst Dienstagabend (Integrationskette, nicht Erfassung)
- OB-Wahl parallel konventionell ausgezählt
