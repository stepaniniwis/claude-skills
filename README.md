# Claude Skills

20 production skills for [Claude Code](https://claude.ai/code). Built from academic publishing, qualitative research, and consulting across management, information systems, and defense studies.

Organized by what they do, not where they come from.

## Guard — enforce quality on every output

Cross-cutting filters. These run on everything, regardless of task.

- **[anti-ai-writing](skills/guard/anti-ai-writing/)** — Kills 17 AI-typical prose patterns at word and paragraph level. No "delve", no "it's important to note", no balanced-binary sentences, no enumeration templates.
- **[non-sycophant](skills/guard/non-sycophant/)** — Forces honest disagreement instead of agreement-seeking. Three modes: Standard (honest), `/challenge` (active counterposition), `/destroy` (strongest possible attack).
- **[data-integrity-guard](skills/guard/data-integrity-guard/)** — Every number in output must trace to a file read in the current session. Not memory, not prior AI output, not "likely." Prevents the most common LLM failure: plausible-sounding output that doesn't match actual data.
- **[evidence-discipline](skills/guard/evidence-discipline/)** — Separates what the data shows from what the document claims from what the recommendation is. Audits causal language, enforces evidence hierarchy, flags where interpretation is presented as finding.
- **[draft-review-loop](skills/guard/draft-review-loop/)** — Automated produce-attack-fix loop. A fresh-context Review-Agent critiques any substantial deliverable against explicit checklists before it reaches you. One reviewed version replaces five unreviewed ones.

## Audit — check existing work for problems

- **[desk-rejection-preventer](skills/audit/desk-rejection-preventer/)** — Three gates before A-journal submission: Distinctiveness (can your construct be explained by recombining existing ones?), Claim-Design-Weight (does your design carry your claims?), Scope-Conditions (specified or asserted?). Traffic-light verdicts.
- **[a-journal-architecture](skills/audit/a-journal-architecture/)** — 7 structural tests for A-journal DNA: Big Puzzle, Named Mechanism, Portable Device, Paper-in-One-Sentence, Contribution Hierarchy, Concept Boundary Defense, Intellectual Deficiency.
- **[citation-risk-auditor](skills/audit/citation-risk-auditor/)** — Sentence-level scan for missing citations. 8 claim types that trigger reviewer skepticism: literature-claims, empirical trends, strong generalizations, absolute gaps, superlatives, causal inference from anecdote, methodological absolutism, theoretical concept orphans.
- **[hallucination-audit](skills/audit/hallucination-audit/)** — Three-tier back-check for AI-co-written academic text. Run before submission, before sharing with supervisors, before citing. Separate protocols for high, medium, and low-risk claims.
- **[paper-revision-diagnostic](skills/audit/paper-revision-diagnostic/)** — 7 hard framing questions before any substantive revision. Prevents the most expensive failure: polishing a paper whose framing doesn't hold.
- **[saturation-auditor](skills/audit/saturation-auditor/)** — Assesses saturation in qualitative research. AUDIT mode diagnoses weaknesses, DRAFT mode writes saturation sections. Grounded in Moore, Aguinis and Darden (2026).

## Build — construct deliverables from scratch

- **[qualitative-coder](skills/build/qualitative-coder/)** — Independent third coder for interview transcripts. Gioia, Thematic Analysis, Template Analysis. Anti-smoothing filters, quote verification, interviewer-contamination detection, speaker separation.
- **[methods-narrative-architect](skills/build/methods-narrative-architect/)** — Writes the analytical prose chain from data to theory. Solves "the transition from data to model is too abrupt" (the most common reviewer complaint in qualitative papers). Covers Gioia, Grounded Theory, Case Study, fsQCA, Thematic Analysis.
- **[abductive-bridge](skills/build/abductive-bridge/)** — Builds the reasoning that connects qualitative codes to abstract constructs. Forces explicit logic: why this grouping, what the shared theoretical function is, what alternatives exist, what would falsify the construct.
- **[rq-architect](skills/build/rq-architect/)** — Moves research questions from gap-spotting to genuine problematization. Combines Sandberg and Alvesson (2010) with FINERMAPS quality criteria and RQ-type taxonomy.
- **[argument-architecture](skills/build/argument-architecture/)** — CARS model (macro: Introduction architecture, research space creation) plus Toulmin (micro: claim-evidence-warrant for each argument). Two levels of structure for academic positioning.
- **[theory-section-architect](skills/build/theory-section-architect/)** — Architects theory sections: construct selection, framework construction, tension surfacing, hypothesis derivation. Three modes: Scaffold (architecture), Draft (write), Review (diagnose).
- **[theory-map-architect](skills/build/theory-map-architect/)** — Produces a strategic 2-page theory memo for configurational (fsQCA, QCA) and qualitative (Gioia, grounded theory, case study) papers with finished results but unclear theoretical artifact. Forces three explicit decisions: primary lens, secondary lens, artifact genre. Audits self-developed constructs for theoretical anchoring. Sits between empirical results and writing prose.

## Orchestrate — chain multiple skills into a pipeline

- **[research-lifecycle](skills/orchestrate/research-lifecycle/)** — Full paper pipeline from ideation to submission: SCOPE (what paper, what journal, what contribution), BUILD (theory, methods, findings), REVIEW (feedback pipeline), FIX (revision), SUBMIT (formatting, final checks). Calls the right sub-skills in sequence.
- **[paper-feedback-pipeline](skills/orchestrate/paper-feedback-pipeline/)** — 5-stage sequential review: Referee Report, Section-by-Section Analysis, Claim Validation, Consistency Audit, Polish and Journal Fit. Each stage builds on the previous one.

## Installation

```bash
# Single skill
cp -r skills/guard/anti-ai-writing ~/.claude/skills/

# One category
cp -r skills/guard/* ~/.claude/skills/

# Everything
cp -r skills/*/* ~/.claude/skills/
```

## How they relate

```
research-lifecycle (orchestrator)
    |
    +-- SCOPE: rq-architect, argument-architecture
    +-- BUILD: theory-section-architect, qualitative-coder,
    |         methods-narrative-architect, abductive-bridge
    +-- REVIEW: paper-feedback-pipeline
    |             +-- citation-risk-auditor
    |             +-- hallucination-audit
    +-- FIX: draft-review-loop, paper-revision-diagnostic
    +-- SUBMIT: desk-rejection-preventer, a-journal-architecture

Always active: anti-ai-writing, data-integrity-guard,
              evidence-discipline, non-sycophant
```

## Context

From a working practice across:
- Academic publishing in management, information systems, and defense studies
- 80+ qualitative interviews across military, entrepreneurship, and digital governance
- Strategic consulting in telecom, fintech, and edge AI
- Teaching at Munich Business School

Questions or feedback: post@stepanini.de

## License

MIT
