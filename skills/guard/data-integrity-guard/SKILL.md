---
name: data-integrity-guard
description: "Cross-cutting accuracy guard. Prevents the most common LLM failure mode: producing plausible-sounding output that doesn't match the actual data. ALWAYS ACTIVE when working with files that contain verifiable facts — spreadsheets, databases, participant lists, code, configs, any structured data. Triggers automatically whenever output references specific values (numbers, IDs, names, dates, codes) that originate from files. Also trigger on: 'check my numbers', 'is this consistent', 'audit this', or any task where getting a fact wrong has downstream consequences."
---

# Data Integrity Guard

Prevents confident-sounding output that contradicts the actual data. The hardest LLM failure to catch because the output reads well.

## Core Problem This Solves

LLMs generate text that is internally coherent but externally wrong. The output sounds right, follows logical patterns, and uses correct grammar — but the specific values (ages, counts, IDs, mappings, percentages) don't match what's in the files. Users trust the output because it's well-written. Errors compound across sessions.

## When Active

Always, whenever output contains verifiable facts sourced from files. Not optional. Not "when explicitly invoked." If the task involves data from files, this is active.

## Protocol

### Before Starting

1. **Identify the authoritative source.** Which file(s) contain the ground truth? If multiple files exist with overlapping data, resolve which is authoritative BEFORE proceeding. Ask the user if unclear.
2. **Read, don't remember.** Even if a file was read earlier in the session or a previous session, re-read it before using its data. Context summaries and memory are lossy. The file is not.
3. **Never use prior Claude output as source.** Previous AI-generated drafts, summaries, or versions may contain errors. Always trace back to the original human-created or system-generated source.

### During Work

4. **Every specific value must have a source.** If you write a number, name, ID, date, or percentage — it must come from a file you read in this session, or from the user's explicit statement. No inference. No "approximately." No "likely."
5. **Cross-reference across representations.** If the same entity appears in multiple places (table row, prose mention, appendix, separate file), all representations must be consistent. Check this actively — don't assume consistency.
6. **Flag uncertainty explicitly.** If you cannot verify a value, say so. "I don't have Mara's age from the prescreener" is correct. "Mara is likely ~27" is a failure.

### Before Delivering

7. **Count check.** Any list or table: count the rows. Compare to stated n. If they don't match, stop and fix.
8. **Reference check.** Any ID/code used in prose: verify against the lookup table. Every instance. Not a spot check — every instance.
9. **Grep for stale values.** After changing any number (sample size, percentage, count), search the entire document for the old value. Update every occurrence.
10. **Denomination check.** Any fraction, percentage, or "out of N" claim: verify N matches current sample/population size.

## Anti-Patterns (What Goes Wrong)

| Anti-Pattern | What Happens | Fix |
|---|---|---|
| **Plausible fill** | Value sounds right but was never looked up | Read the source file |
| **Stale carry-forward** | Value was correct in v01 but changed; text still says v01 value | Grep for old value after any change |
| **Table-text mismatch** | Table says P2=Davina, prose uses P14 for Davina's content | Systematic cross-reference check |
| **Count drift** | Table has 12 rows but text claims n=13 | Count rows, compare to claim |
| **Source confusion** | Using data from the wrong file (superseded version, wrong sheet) | Establish authoritative source first |
| **Context-loss guess** | Data was available earlier but context was compacted; guessing instead of asking | Ask the user |
| **Derivative trust** | Using a previous Claude draft as source of truth | Read the original |

## Qualitative Paper Consistency Protocol

Active whenever a qualitative paper (Gioia, thematic analysis, grounded theory) references participant codes in prose alongside a coding matrix or coverage table.

### The Core Rule

Every participant code in prose is an implicit claim about the coding matrix. If the text says "P6 described priority excavation," the coding matrix must show P6=1 for priority excavation. No exceptions.

### Three Mismatch Types

| Type | What Happens | Fix Strategy |
|---|---|---|
| **Wrong theme label** | Quote is genuine, but the prose labels it as Theme X while participant is coded 0 for Theme X (and 1 for Theme Y that the quote actually illustrates) | Relabel: change the theme attribution, keep the quote |
| **Wrong participant** | Participant cited as exemplifying a theme they are coded 0 for; the behavior described doesn't match their coding | Remove participant or replace with one coded 1 |
| **Quote in wrong section** | Quote belongs to a theme the participant IS coded for, but the prose places it under a different thematic heading | Move quote to the correct thematic section |

### The "Plausible Attribution" Trap

The most dangerous variant. The quote genuinely exists in the transcript. The participant genuinely said it. But rigorous coding determined the theme is NOT present across the interview — a single quote does not equal theme presence. The prose must respect the coding threshold, not cherry-pick isolated quotes that sound like they fit.

### Fix Hierarchy

When a mismatch is found, prefer in this order:
1. **Reframe** to a theme the participant IS coded for (if the quote supports it)
2. **Move** the quote to the thematically correct section
3. **Replace** with a participant who IS coded 1 (requires verified quote)
4. **Generalize** — remove the P-code, make the claim aggregate
5. **Delete** the passage entirely

### Verification Protocol

After writing or editing any qualitative findings section:
1. Grep all participant codes (P1–Pn) in prose
2. For each reference, identify which theme the surrounding text claims
3. Check that participant against the coding matrix for that theme
4. Flag every coded-0 reference
5. Apply fix hierarchy to each flag

This is not a spot check. Every instance. The plausible ones are the ones that slip through.

## Version Regression Check

Active whenever working on version N of any document (paper, scaffold, transition document).

### The Problem

Content silently disappears between versions. A prior Claude session or manual edit removes sections, shortens discussions, or drops conclusions — and the next session treats the shorter version as authoritative without noticing the loss. The user discovers the regression days later by accident.

**HELD example (2026-03-22):** v12 had 7,977 words. v13 had 6,523. The entire Conclusion (Section 6) was deleted. Nobody noticed until the user asked why the paper was 1,400 words under limit.

### Protocol

When starting work on any versioned document:
1. **Word count comparison.** Run `wc -w` on version N and version N-1. If N is >10% shorter, stop and investigate what was removed.
2. **Structural diff.** Compare section headings between versions (`grep "^##"` on both). Flag any sections present in N-1 but missing in N.
3. **Report before proceeding.** If content loss is detected, tell the user: "v[N] is [X] words shorter than v[N-1]. Missing sections: [list]. Intentional?"

Do NOT silently accept a shorter version as the new baseline.

## Quote-Context Alignment Check

Active whenever bilingual quotes appear (German quote + English framing/translation).

### The Problem

The English framing sentence introduces a quote by describing one aspect of the participant's situation, but the German quote actually illustrates a different aspect. Both are real and correct — but the introduction doesn't match the evidence.

**HELD example (2026-03-22):** Text said "P9's relationship between insurance work and poetry" but the quote was "Fotografie ist eine Kompensation" (photography). P9 has both ventures, but the framing didn't match the specific quote.

### Protocol

For every German quote with English framing:
1. Read the German quote first.
2. Verify the English framing sentence describes what the quote actually says — not what the participant does in general.
3. If mismatch: adjust the framing to match the quote, or find a quote that matches the framing.

## Figure/Table Sequential Numbering Check

Active whenever figures or tables are referenced in a document.

### The Problem

When figures are removed or reorganized, numbering gaps appear (Fig. 1, Fig. 3 — no Fig. 2). Editors treat this as sloppiness; reviewers treat it as a signal of careless preparation.

### Protocol

After any figure/table audit:
1. List all figure/table numbers in order.
2. Verify the sequence is gapless (1, 2, 3... not 1, 3).
3. If gaps exist: renumber all references in the text AND rename/copy the files.

## Cross-Section Participant Code Consistency

Active whenever participant codes appear in multiple sections of a paper (e.g., Findings AND Discussion).

### The Problem

The same conceptual slot (e.g., "inverted cases") is populated with different P-codes in different sections. One section says P27, another says P31. Both sound right. Only one is.

**MDO example (2026-03-22):** Section 4.6 listed P31 in Subtype B. The Discussion (line 354) listed P27 instead. These are different participants.

### Protocol

After writing or editing any paper with P-codes:
1. Grep every P-code across the entire document.
2. For each P-code, note which claim/category it's assigned to in each location.
3. If the same P-code appears with conflicting assignments, or the same slot has different P-codes: flag and resolve against primary coding data.

## AI-Generated Source Verification

Active whenever AI systems (including Claude itself) cite sources, references, authors, or findings.

### The Problem

AI systems produce citations that look correct — plausible author names, realistic journal titles, reasonable years — but point to papers that don't exist, or attribute claims to papers that say something different. The output is confident and well-formatted, which makes the fabrication harder to catch than an obvious gap.

### Protocol

1. **Demand primary sources.** When any AI system (including this one) cites a study, framework, or empirical finding: ask for the full reference (authors, year, journal, DOI).
2. **Verify the source exists.** Check DOI, Google Scholar, or the journal archive. A plausible-sounding reference is not a real reference.
3. **Verify the claim matches the source.** A real paper cited for something it doesn't actually argue is worse than a missing citation — it looks verified but isn't.
4. **Never chain AI-generated citations.** If Claude cited Smith (2019) in Session A, and Session B builds on that citation without re-verifying: the chain is unverified. Each session must trace back to the primary source independently.

This applies to Claude's own output. If this system generates a reference, the user should verify it before using it in any deliverable. The rule is symmetric: demand sources, then check them. No exceptions for confidence or formatting quality.

## Integration with Other Skills

This skill is a **filter layer**, like anti-ai-writing. It doesn't produce output — it constrains output. Active underneath any skill that touches data:
- research-examiner: data integrity guard runs before epistemic-depth analysis
- academic-writing: data integrity guard validates any empirical claim in prose
- consulting-strategic-analysis: data integrity guard verifies numbers in analysis
- ops-rhythm-manager: data integrity guard checks task counts and dates

Sprache folgt dem Input (Deutsch / English).
