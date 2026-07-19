# Internes Review-Memo (kritischer Gutachterdurchgang, 18.07.2026)

Simulierte Begutachtung der v0.2 aus Reviewer-Perspektive; alle Befunde wurden direkt umgesetzt (v0.3).

## Major

**R1 – Selbstwiderspruch bei der Neuheitsbehauptung (umgesetzt).** Titel, Abstract, Einleitung und Fazit behaupteten den "ersten rechtsverbindlichen Einsatz in einer deutschen Großstadt"; Abschnitt 2.3 nannte aber selbst den vorherigen Realbetrieb in Bremen (Großstadt) und Bremer Unterstützungskräfte mit Praxiserfahrung. Ein Gutachter hätte das in fünf Minuten gefunden; Desk-Reject-Risiko. Fix: Neuheitsclaim durchgängig auf die *Evaluation* verschoben ("erste systematische wissenschaftliche Evaluation eines rechtsverbindlichen Einsatzes"), Bremer Praxiseinsätze in der Einleitung explizit gewürdigt und die Lücke als Evaluationslücke präzisiert. Titel entsprechend geändert.

**R2 – Einseitiger Fisher-Test unbegründet (umgesetzt).** Die Wahl der Testrichtung war nicht begründet; Gutachter fragen das standardmäßig. Fix: Begründung in 4.4 ergänzt, inkl. des Arguments, dass die einseitige Wahl hier die strengere ist (findet Signifikanz leichter; verfehlt bereits sie das Kriterium, gilt das zweiseitig erst recht).

## Moderate

**R3 – Befunde ohne Ergebnistabelle (umgesetzt).** Die Akzeptanzbefunde standen nur im Fließtext. Fix: Tabelle 2 mit allen zentralen Indikatoren, Verteilungen und Fallzahlen in 5.3 eingefügt.

**R4 – Unverifizierte Rechtsnorm (umgesetzt).** "Art. 34 GLKrWG" war aus dem Gedächtnis zitiert und nicht verifiziert. Fix: auf "(GLKrWG)" generalisiert; exakte Artikelangabe vor Einreichung nachtragen (Checkliste).

**R5 – Fehlende Verortung in der Verwaltungsdigitalisierungsforschung (umgesetzt).** Für dms fehlte der Anschluss an die Digital-Government-Literatur. Fix: Mergel et al. 2019 (GIQ, verifiziert via Scite, DOI 10.1016/j.giq.2019.06.002) in 6.4 als Kontrastfolie ergänzt: Wahlorganisation als Digitalisierung einer Kernfunktion von Staatlichkeit statt einer Serviceleistung.

## Minor (alle umgesetzt)

- Ton: "politisch tot" → "politisch nicht mehr ernsthaft verfolgt"; "gehören in die Akten" → "gehören gleichberechtigt ins Protokoll".
- Missverständliche Formulierung "Die Helfenden ertrugen das System nicht" (lesbar als Ablehnung) → umformuliert.
- Rundung: "99 Prozent" → "rund 99 Prozent" (84/85 = 98,8 %).
- Wortdopplung "Anordnung" an zwei Stellen variiert ("Verfahrensvariante", "Konfiguration").

## Nicht umgesetzt / bewusst belassen

- Deckeneffekt-Diskussion bleibt wie ist: Sie ist bereits selbstkritisch geführt; weitere Relativierung würde den Befund künstlich schwächen.
- Platzhalter in 4.5 (Stadt-Freigabe) bleibt bis zur Klärung; darf nicht in die finale Einreichungsdatei.

## Runde 2 (18.07.2026, auf v0.4, alle umgesetzt → v0.5)

**R2-1 (Major, Recht):** Die Paraphrase des BVerfG-Urteils ("maßgebliches Stimmendokument der Laienkontrolle entzogen") war dogmatisch angreifbar; das Urteil verlangt Nachvollziehbarkeit der wesentlichen Verfahrensschritte ohne Sachkenntnis, nicht ein bestimmtes Dokumentenarrangement. Präzisiert. Zusätzlich expliziter Reichweiten-Hedge: Der Beitrag leistet bewusst keine abschließende wahl-/verfassungsrechtliche Würdigung (dms führt "Recht" im Titel; ein juristischer Gutachter hätte die implizite Zulässigkeitsbehauptung attackiert).

**R2-2 (Major):** Kostendimension fehlte vollständig; "Effizienz" ohne Wirtschaftlichkeit ist eine offene Flanke. Als Limitation in 6.3 ergänzt (Zeit- statt Wirtschaftlichkeitsaussagen, offene Kostenseite) und als Praxisfolgerung in 6.4 (Wirtschaftlichkeitsbetrachtung vor Skalierung).

**R2-3 (Moderate):** IT-Sicherheit war weder evaluiert noch als Nichtgegenstand markiert. In 6.2 explizit ausgewiesen: Sicherheitsarchitektur beschrieben, nicht auditiert.

**R2-4 (Moderate):** Rücklaufquote der allgemeinen Befragung nicht bezifferbar (Grundgesamtheit unbekannt); jetzt offen ausgewiesen statt verschwiegen.

**R2-5 (Minor):** Forschungsfragen als FF1–FF3 nummeriert und in den Überschriften von 5.1–5.3 sowie in 6.1 rückgebunden; dms-Gutachter prüfen die RQ-Befund-Kopplung explizit.

## Runde 3: Tiefenprüfung Daten und Argumentlogik (18.07.2026, auf v0.5 → v0.6)

**T1 (Major, Datenfehler):** 5.4 schrieb die ≤0,3-pp-Genauigkeit fälschlich dem 30-Minuten-Zwischenergebnis zu; sie gilt für die vollständigen ungeprüften Ergebnisse. Korrigiert und getrennt. Vollständiger Zahlenabgleich Manuskript ↔ Rohexport dokumentiert in `06-zahlenpruefung.md` (31/31 Prüfpunkte OK).

**T2 (Analyse):** Schärfste faire Vergleichsebene ergänzt: WES-Bezirke wurden am Standort mit der höchsten konventionellen Berichtigungsquote (MOC, 9,7 %) ausgezählt; Binomialnäherung P(0|0,097; 23) ≈ 0,10. Stärkt das Signal und bleibt ehrlich nicht-signifikant.

**T3 (Präzision):** "Stimmen für die 25 Bezirksausschüsse" war als Wahl aller 25 Gremien lesbar; präzisiert auf den Bezirksausschuss des jeweiligen Stadtbezirks.

**T4 (Konsistenz):** 6.3 zählte "drei Messvorbehalte", listete nach der Kosten-Ergänzung aber vier; korrigiert.

**T5 (Theoriepolitur):** Explizite Geltungsbedingungen in 6.1 (Komplexität, zentrale Auszählung, ehrenamtliche Bedienung, maßgebliches Papier) mit klarer Nicht-Geltungs-Aussage.

## Runde 4: Abgleich mit Editor-Checkliste zu KI-typischen Paper-Fehlern (18.07.2026, → v0.7)

Vorlage: Beobachtungsliste eines Journal-Editors (Screenshot des Autors). Punkt-für-Punkt-Prüfung:

| Editor-Kritik | Befund im Manuskript | Aktion |
|---|---|---|
| Jargon-Overdrive in Titel/Abstract | Titel konkret; ein überladener Schachtelsatz in der Zusammenfassung | Satz geteilt und entzerrt |
| "Conceptual synthesis" statt Empirie | Trifft nicht zu: empirische Studie mit eigenen Daten, FF1–FF3 empirisch beantwortet | keine |
| Lit-Review als Referenz-Listen zur Gutachter-Besänftigung | Kein 4er-Cluster; Review um Spannungen organisiert; ein identisch wiederholtes 3er-Tripel | Tripel bei Zweitnennung auf zwei Anker gekürzt |
| Methoden von genAI-Affordanzen geprägt | Trifft nicht zu: reale Erhebungen, Instrument offengelegt inkl. Grenzen | keine |
| Analyse als Bullet-Listen + Akronym-Framework | Kein Framework, kein Akronym; ABER 6.4-Behördenabsatz war eine Parallel-Deklarativ-Liste in Prosaform | Absatz zu gewichteter Prosa umgebaut (wichtigster Hebel ausgebaut, Nebenpunkte komprimiert) |
| Schluss mit "testbaren Propositionen"-Listen | Trifft nicht zu: narrativer Schluss ohne Propositionen | keine |
| Frankencitations | Alle 35 Referenzen verifiziert (siehe Runden 1–3, `06-zahlenpruefung.md`) | keine |
| Exakt am Wortlimit geschrieben | Umfang inhaltsgetrieben (~57.000 Zeichen), Limit-Abgleich steht ohnehin aus | keine |

## Restposten (Checkliste)

- Taylor 2010: Seitenzahlen in ELJ 9(2) nicht auffindbar (Verlagsseiten proxy-gesperrt); am PDF/Browser nachtragen.
- Exakte GLKrWG-Norm für Kumulieren/Panaschieren einsetzen.
- DeMora et al. 2022 und Hostetter/Atkeson 2025: Heft/Seiten einfach belegt, am PDF prüfen.
