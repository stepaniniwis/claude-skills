# Skill-Drift-Audit: Repo vs. installierte Skills (Stand 19.07.2026)

Abgleich der 20 Repo-Skills gegen die installierten Kopien in `~/.claude/skills/` (58 Skills). Ziel: eine Quelle der Wahrheit pro Skill. Grundregel dieses Audits: **Das Repo ist die kanonische Quelle** — Features, die nur in installierten Kopien existieren, werden ins Repo portiert; veraltete installierte Kopien werden aus dem Repo neu installiert.

## In diesem Commit behoben

| Skill | Befund | Aktion |
|---|---|---|
| argument-architecture | Installierte Version = Repo + **Substitution Stress Test** (SKILL.md-Sektion + `references/substitution-stress-test.md`); Repo hatte das Feature nicht | Ins Repo portiert, README aktualisiert |
| theory-map-architect | Identischer Body, installierte Frontmatter-Description ist die gestraffte, besser scannbare Iteration | Description ins Repo übernommen |

## Installierte Kopien sind veraltet — bei Gelegenheit neu installieren

`cp -r skills/<kategorie>/<name> ~/.claude/skills/` (bzw. euer Install-Weg). Die Repo-Versionen sind hier weiter:

| Skill | Repo | Installiert | Was der installierten Kopie fehlt |
|---|---|---|---|
| anti-ai-writing | 417 Zeilen | 315 | Erweiterungen der Repo-Version (u.a. Paragraph-Level-Sektionen) |
| non-sycophant | 77 | 75 | Claim-Sycophancy-Regel + Design-Proportionalitäts-Check |
| rq-architect | 420 | 269 | Substanzielle Erweiterung der Repo-Version |
| theory-section-architect | 486 | 385 | Substanzielle Erweiterung der Repo-Version |

## Synchron (keine Aktion)

citation-risk-auditor, saturation-auditor.

## Offene Konsolidierungsentscheidung (nicht automatisch auflösbar)

**qualitative-coder (Repo, DE) vs. qual-first-coder (installiert, EN):** Keine Versionen desselben Skills, sondern Geschwister mit unterschiedlichem Zuschnitt:

- Repo `qualitative-coder`: Deutsch, 4 Modi (CODE / COMPARE / EXPLORE / AUDIT), Rolle „unabhängiger 3. Coder", explizite COMPARE-Funktion gegen menschliches Coding.
- Installiert `qual-first-coder`: Englisch, breiterer Materialscope (Fokusgruppen, offene Survey-Antworten), explizit design-agnostisch, nur First-Cycle.

Optionen: (a) mergen zu einem Skill mit Modi + breitem Scope, (b) bewusst getrennt lassen und Abgrenzung in beide Descriptions schreiben, (c) qual-first-coder als englische Hauptversion ins Repo holen und qualitative-coder auf COMPARE/AUDIT-Spezialist eindampfen. Empfehlung: (a) — die Anti-Glättungs-Regeln sind in beiden nahezu identisch, die Differenz ist Verpackung.

**Nur installiert, nicht im Repo** (bewusste Kuratierung oder Kandidaten für Aufnahme?): research-examiner, rq-wording-checker, academic-writing, paper-arc-architect, scope-condition-architect, qual-method-auditor, synthesis-prose-architect, pgp-style, literature-review-architect/-writer, mulcahy-*-Familie u.a. — falls das Repo das „production set" bleiben soll, ist keine Aktion nötig; falls es die Gesamtsammlung werden soll, fehlen diese.
