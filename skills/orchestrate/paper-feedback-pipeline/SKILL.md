---
name: paper-feedback-pipeline
description: "Orchestrated 5-stage feedback pipeline for academic papers. Runs Referee Report → Section-by-Section → Claim Validation → Consistency Audit → Polish + Journal Fit as a sequential pipeline. Uses existing skills as building blocks. Produces a consolidated feedback report. Trigger on: 'feedback pipeline', 'run feedback', 'review my paper', 'Baeckman pipeline', 'full paper review', 'give me feedback on', or when a paper draft is ready for comprehensive review before submission. Inspired by Claes Baeckman (2026) 'Feedback Machines'."
---

# Paper Feedback Pipeline

Five-stage sequential feedback pipeline for academic papers. Runs the full cycle from high-level assessment to journal fit. Each stage builds on the previous.

## Origin

Inspired by Claes Baeckman's "Feedback Machines" (Substack, 2026) — AI as feedback machine for academic writing. Adapted to use existing skill infrastructure. The key insight: individual review skills exist, but without orchestrated sequencing they miss interaction effects between stages.

## When to Use

- Paper draft is complete enough for substantive review (not for outlines or scaffolds)
- Before sending to co-authors, supervisors, or journal
- After a major revision round to verify all fixes landed
- When you want "what would a reviewer say?" before the reviewer says it

## When NOT to Use

- On outlines, scaffolds, or very early drafts (use `paper-revision-diagnostic` instead)
- On individual sections in isolation (use `draft-review-loop` instead)
- For planning what to write (use `paper-revision-diagnostic` Phase 1+2)

## The Five Stages

### Stage 1: Referee Report (High-Level Assessment)

**What:** Read the entire paper. Write a 1-page referee report as a hostile but fair reviewer would.

**Covers:**
- What is the claimed contribution? Is it convincing?
- What are the 3 strongest aspects?
- What are the 3 most vulnerable points?
- Are there unsupported claims that a reviewer would circle?
- Would this paper survive desk review at the target journal?

**Skill basis:** `research-examiner` (epistemic depth layer)

**Output:** Referee report with ACCEPT / MAJOR REVISION / MINOR REVISION / REJECT verdict and justification.

**Critical rule:** The referee report must identify the ONE thing that would make a reviewer recommend rejection. Not three things — one. The single most dangerous weakness.

### Stage 2: Section-by-Section Review

**What:** Walk through each major section. For each section, assess:

- Does this section do what the paper promises it does?
- Are there internal inconsistencies within the section?
- Does the section align with the paper's overall argument?
- Is the transition to the next section motivated?
- Are there passages where the argument loses the reader?

**Section-specific checks:**

| Section | Key question |
|---|---|
| Abstract | Does it contain the full mechanism chain? (puzzle → mechanism → structure → outcome) |
| Introduction | Is there a paper-in-one-sentence? Are contributions hierarchized? Does it contain ANY findings (numbers, breakdowns, direct quotes from data)? If yes: BLOCKER. The Introduction opens the puzzle and announces the contribution. It does NOT report results. No "27 of 33", no cross-category breakdowns, no interview quotes. Those belong in Findings. |
| Theory | Is the new concept boundary-defended? (3 contrast sentences) |
| Methods | Is the design honestly labeled? Are D-scores/scorecards defensively framed? |
| Findings | Is Finding 1 subordinated to the main mechanism? Parallel structure across categories? |
| Discussion | Does it follow the 7-step sequence? Is portability early enough? |
| Conclusion | Does it restate mechanism, not just findings? |

**Skill basis:** `draft-review-loop` Checklists A-D + `a-journal-architecture` Tests 1-7

**Output:** Per-section verdict (STRONG / NEEDS WORK / WEAK) with specific paragraph-level suggestions.

### Stage 3: Claim Validation

**What:** Identify every empirical or theoretical claim in the paper. For each claim, check:

- Is it supported by data, citation, or explicit own argument? Every factual sentence needs a reference or an explicit "we argue" marker. Papers that were READ but UNDERUSED are the biggest gap source — scan for references in the bibliography that appear only once and could strengthen claims made elsewhere.
- Is the causal language proportional to the design?
- Are confounds acknowledged at group comparisons?
- Is the evidence level stated (robust / plausible / exploratory)?

**Special attention to:**
- Claims that cite "the literature shows" without specific references
- Quantified claims where the number should be verified against source data
- Generalizations from the specific setting beyond what the design supports
- Theory attributions (does Author X really argue Y?)

**Skill basis:** `citation-risk-auditor` (R1-R8) + `evidence-discipline` (7 rules)

**Output:** Claim-by-claim table with severity (BLOCKER / WARNING / NOTE).

### Stage 4: Consistency Audit

**What:** Cross-check all mechanical consistency across the paper:

- Are all tables and figures referenced in the text?
- Are table/figure numbers sequential and correctly labeled?
- Do in-text numbers match the numbers in tables?
- Are construct names / variable labels used consistently throughout?
- Are all references cited in text present in the reference list (and vice versa)?
- Are abbreviations defined on first use?
- Is the N / sample size consistent across all mentions?
- Do P-codes / case identifiers match across text, tables, and appendices?

**Skill basis:** `data-integrity-guard` (accuracy checks)

**Output:** List of inconsistencies with location (section + paragraph).

**This stage catches the errors that are invisible during writing but obvious to reviewers.** A wrong N in one place, a table referenced as "Table 3" when it is Table 4, a construct called "experiential realness" in the theory section and "construal level" in the methods — these are desk-reject triggers.

### Stage 5: Polish + Journal Fit

**What:** Two passes:

**Pass A — Language Polish:**
- Apply anti-ai-writing filter: check for AI-typical patterns (enumeration templates, zero-friction flow, balanced binaries, present-participle inflation)
- Check for hedging inflation ("it is important to note", "it should be mentioned")
- Check for repetition across sections (same idea stated three times in different words)
- Prose quality: is it clear, direct, economical?

**Pass B — Journal Fit:**
- Does the paper match the target journal's scope, style, and ambition level?
- Are the right benchmark papers cited (papers from the target journal)?
- Does the contribution claim match what the journal typically publishes?
- For Special Issues: does the paper use the Call's vocabulary?
- Word count within limits?

**Skill basis:** `anti-ai-writing` (word + paragraph level) + `a-journal-architecture` (7 tests)

**Output:** Language issues list + Journal fit assessment with specific adjustments needed.

## Execution Protocol

When the pipeline is triggered:

1. **Read the full paper** (all sections, references, tables)
2. **Run Stage 1** (Referee Report) — present to user
3. **Run Stage 2** (Section-by-Section) — present to user
4. **Run Stages 3+4 in parallel** (Claim Validation + Consistency Audit) — present together
5. **Run Stage 5** (Polish + Fit) — present to user
6. **Produce consolidated report**

The consolidated report follows this format:

```
PAPER FEEDBACK PIPELINE — [Paper Name] — [Date]
TARGET: [Journal]
VERSION: [filename]
WORD COUNT: [N]

STAGE 1 VERDICT: [Accept / Major / Minor / Reject]
Single most dangerous weakness: [one sentence]

STAGE 2 SECTION VERDICTS:
- Abstract: [STRONG/NEEDS WORK/WEAK]
- Introduction: [...]
- Theory: [...]
- Methods: [...]
- Findings: [...]
- Discussion: [...]
- Conclusion: [...]

STAGE 3 CLAIM ISSUES:
- BLOCKERS: [count] — [list]
- WARNINGS: [count] — [list]

STAGE 4 CONSISTENCY ISSUES:
- [count] issues found — [list]

STAGE 5:
- AI-writing patterns: [count]
- Journal fit: [HIGH/MEDIUM/LOW]

PRIORITY FIX LIST (top 5):
1. [most urgent]
2. ...
3. ...
4. ...
5. ...
```

## Parallelization

Stages 3 and 4 are independent and can run as parallel subagents. All other stages are sequential (each builds on the previous).

For maximum speed, the pipeline can also be split across 3 parallel agents:
- Agent A: Stage 1 (Referee Report)
- Agent B: Stage 3 (Claim Validation) — can run without Stage 2
- Agent C: Stage 4 (Consistency Audit) — fully independent

Then Stage 2 and 5 run sequentially after Agent A completes.

## Baeckman's Key Warning

"My biggest concern is that the model smooths over conceptual problems rather than fixing them."

This pipeline is designed to FIND problems, not to fix them. The fixes are the user's job. The pipeline produces a prioritized problem list. The user decides what to act on.

"AI suggestions are candidate edits, not 'always-accept' edits."

## Integration with Existing Skills

| Stage | Primary Skill | Secondary Skills |
|---|---|---|
| 1. Referee Report | `research-examiner` | `a-journal-architecture` |
| 2. Section-by-Section | `draft-review-loop` | `paper-arc-architect`, `argument-architecture` |
| 3. Claim Validation | `citation-risk-auditor` | `evidence-discipline` |
| 4. Consistency Audit | `data-integrity-guard` | — |
| 5. Polish + Fit | `anti-ai-writing` | `a-journal-architecture` |

## Difference from Other Skills

- `draft-review-loop`: Runs DURING writing as self-critique. This pipeline runs AFTER writing as comprehensive review.
- `research-examiner`: Stage 1 only. This pipeline adds 4 more stages.
- `paper-revision-diagnostic`: Runs BEFORE revision to assess framing. This pipeline runs AFTER revision to catch remaining issues.

The full workflow is: `paper-revision-diagnostic` (before) → write/revise → `paper-feedback-pipeline` (after) → fix → submit.

Sprache folgt dem Input (Deutsch / English).
