---
name: research-lifecycle
description: "Orchestrates the full academic paper lifecycle from ideation to submission. Chains existing skills into an agentic pipeline. Five phases: SCOPE (what paper, what journal, what contribution), BUILD (theory + methods + findings), REVIEW (feedback pipeline), FIX (revision based on feedback), SUBMIT (formatting + final checks). Trigger on: 'new paper', 'start paper', 'paper lifecycle', 'full pipeline', 'von Anfang bis Ende', or when the user wants to develop a paper from scratch rather than fix an existing one. Also trigger PROACTIVELY when a user has clearly decided on a paper direction and needs the next step identified."
---

# Research Paper Lifecycle

Orchestrates the full journey from "I have an idea" to "ready to submit." Chains existing skills into an agentic pipeline so the user does not have to remember which skill comes next.

## The Problem This Solves

46 skills exist. Each works well in isolation. But the user must know: which skill, in what order, at what stage? That cognitive overhead defeats the purpose. This skill removes it by managing the sequence.

## Five Phases

### Phase 1: SCOPE
**When:** User has an idea, a dataset, or a rough direction but no clear paper yet.
**Skills chained:** `rq-architect` → `a-journal-architecture` Test 1-2 (Big Puzzle, Intellectual Deficiency)
**Outputs:** Research question, target journal, contribution type, 2-3 benchmark papers
**Decision point:** User confirms direction before Phase 2 starts.

### Phase 2: BUILD
**When:** Scope is confirmed. Time to construct the paper.
**Sub-phases:**

2a. **Theory** — `paper-revision-diagnostic` Phase 1 (Q1-Q7) → `theory-section-architect` Scaffold → Draft
2b. **Methods** — `methods-narrative-architect` (design justification, analytical steps, trustworthiness)
2c. **Findings** — `qualitative-coder` (if qual) or data analysis → `academic-writing` Draft mode
2d. **Discussion** — `argument-architecture` (CARS echo) → `academic-writing`
2e. **Introduction + Abstract** — written LAST, using `a-journal-architecture` Tests 3-6

**Skills chained:** `paper-revision-diagnostic` → `theory-section-architect` → `methods-narrative-architect` → `academic-writing` → `a-journal-architecture`
**Decision point:** Complete draft exists. User reviews before Phase 3.

### Phase 3: REVIEW
**When:** Draft is complete enough for substantive feedback.
**Skills chained:** `paper-feedback-pipeline` (5 stages: Referee Report → Section-by-Section → Claim Validation → Consistency Audit → Polish + Fit)
**Output:** Consolidated feedback report with prioritized fix list.
**Decision point:** User decides which fixes to implement.

### Phase 4: FIX
**When:** Feedback report exists, fixes needed.
**Skills chained:** `draft-review-loop` (fix blockers → self-critique → present)
**Sub-tasks:**
- Concept boundary defense (if flagged in Phase 3)
- Contribution hierarchy adjustment
- Methods defense strengthening
- Missing references
- Table/Figure consistency
**Decision point:** Fixed version ready for final checks.

### Phase 5: SUBMIT
**When:** Paper is revised and needs final preparation.
**Skills chained:** `research-examiner` (desk-reject check) → `hallucination-audit` → `anti-ai-writing` Purge → formatting
**Checklist:**
- [ ] Word count within journal limit
- [ ] All tables/figures referenced in text
- [ ] All in-text citations in reference list (and vice versa)
- [ ] Anonymization complete (for blind review)
- [ ] AI use disclosure (if required)
- [ ] Cover letter drafted
- [ ] Supplementary materials prepared (Online Appendix, data structure, replication)
**Output:** Submission-ready manuscript + checklist.

## How Phases Connect

```
SCOPE ──→ BUILD ──→ REVIEW ──→ FIX ──→ SUBMIT
  ↑                    │                  │
  └────────────────────┘                  │
  (if Review reveals framing problem,     │
   return to SCOPE)                       │
                                          ↓
                                      SUBMITTED
                                          │
                                     [Reviews arrive]
                                          │
                                          ↓
                                   REVIEW (re-run Phase 3
                                   against reviewer comments)
                                          │
                                          ↓
                                   FIX (point-by-point response)
                                          │
                                          ↓
                                   SUBMIT (R1/R2)
```

## Proactive Behavior

This skill should PROACTIVELY:
1. After any phase completes, suggest the next phase
2. After SCOPE, say "Direction confirmed. Ready for BUILD — start with Theory Section?"
3. After BUILD, say "Draft complete. Ready for REVIEW — run feedback pipeline?"
4. After REVIEW, present the fix list and say "Which fixes should I implement first?"
5. After FIX, say "Ready for SUBMIT — run final checks?"

The user can always skip phases or jump ahead. The pipeline is a default sequence, not a prison.

## Cross-Cutting Skills (Active in ALL Phases)

These skills run in the background, always:
- `anti-ai-writing` — on every prose output
- `data-integrity-guard` — on every number/fact
- `non-sycophant` — on every judgment
- `evidence-discipline` — on every claim

## What This Skill Does NOT Do

- It does not replace the user's conceptual decisions (which theory, which RQ, which journal)
- It does not write the paper autonomously — each phase produces output for user review
- It does not skip phases — but the user can
- It does not handle co-author coordination, Paperpile, or journal submission portals

## Current Paper Status Tracking

When working on a paper through this lifecycle, track status:

```
PAPER: [Name]
TARGET: [Journal]
PHASE: [1-5]
SUB-PHASE: [if applicable]
LAST COMPLETED: [what was done]
NEXT STEP: [what comes next]
BLOCKERS: [what needs user decision]
```

This status should be updated in the project memory after each work session.

Sprache folgt dem Input (Deutsch / English).
