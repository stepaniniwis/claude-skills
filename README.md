# Wissmann Resources

Skills, frameworks, and thinking tools from a working research and consulting practice.

Built for [Claude Code](https://claude.ai/code). These are production artifacts, not tutorials. They come from academic publishing, qualitative research, strategic consulting, and thought leadership work across defense, digital voting, entrepreneurship, and AI governance.

Some skills chain into each other. Some stand alone. All are opinionated.

## Skills

Plug-and-play skills for Claude Code. Copy a folder to `~/.claude/skills/` and use immediately via `/skill-name`.

### Academic Research

The full pipeline from research question to submission, built from publishing in management, information systems, and defense studies.

- **[research-lifecycle](skills/academic/research-lifecycle/)** -- Full paper pipeline orchestrator: SCOPE, BUILD, REVIEW, FIX, SUBMIT. Chains the right sub-skills in sequence.
- **[paper-feedback-pipeline](skills/academic/paper-feedback-pipeline/)** -- 5-stage sequential review: Referee Report, Section-by-Section, Claim Validation, Consistency Audit, Polish and Journal Fit.
- **[a-journal-architecture](skills/academic/a-journal-architecture/)** -- 7-test structural diagnostic for A-journal DNA. Big Puzzle, Named Mechanism, Portable Device, Contribution Hierarchy. Derived from JMS award paper analysis.
- **[desk-rejection-preventer](skills/academic/desk-rejection-preventer/)** -- 3-gate pre-submission test: Distinctiveness (recombination test), Claim-Design-Weight, Scope-Conditions. Traffic-light verdicts.
- **[rq-architect](skills/academic/rq-architect/)** -- Research question architect combining Sandberg and Alvesson problematization with FINERMAPS quality criteria.
- **[argument-architecture](skills/academic/argument-architecture/)** -- CARS (macro) plus Toulmin (micro) for academic positioning and argumentation.
- **[theory-section-architect](skills/academic/theory-section-architect/)** -- Architects theory sections: construct selection, tension resolution, hypothesis derivation.
- **[methods-narrative-architect](skills/academic/methods-narrative-architect/)** -- Analytical prose chain from data to theory for qualitative and mixed-methods papers. Covers Gioia, Grounded Theory, Case Study, fsQCA, Thematic Analysis.
- **[academic-writing](skills/academic/academic-writing/)** -- Prose execution: PEEL paragraphs, APA 7th citations, Helen Sword style principles.
- **[lit-review-copilot](skills/academic/lit-review-copilot/)** -- Literature review co-pilot. Resolves jangle/mangle, harmonizes constructs, builds integrative frameworks.
- **[qualitative-coder](skills/academic/qualitative-coder/)** -- Independent third coder for interview transcripts. Anti-smoothing, quote verification, interviewer-contamination filters.
- **[saturation-auditor](skills/academic/saturation-auditor/)** -- Saturation assessment grounded in Moore, Aguinis and Darden (2026). AUDIT and DRAFT modes.
- **[citation-risk-auditor](skills/academic/citation-risk-auditor/)** -- Sentence-level audit for missing citations across 8 claim-type categories.

### Quality and Integrity

Cross-cutting filters. These run on every output that carries consequences.

- **[draft-review-loop](skills/quality/draft-review-loop/)** -- Automated produce-attack-fix loop. A fresh-context Review-Agent critiques any substantial deliverable before it reaches the user.
- **[evidence-discipline](skills/quality/evidence-discipline/)** -- Separates data from interpretation from recommendation. Audits causal language in consequential output.
- **[data-integrity-guard](skills/quality/data-integrity-guard/)** -- Source-tracing discipline: every specific value in output must come from a file read in the current session, not from memory or prior AI output.
- **[hallucination-audit](skills/quality/hallucination-audit/)** -- 3-tier back-check for hallucinated content in AI-co-written academic text.
- **[non-sycophant](skills/quality/non-sycophant/)** -- 3-mode behavior correction against LLM agreement bias. Standard, /challenge, /destroy.

### Writing

- **[anti-ai-writing](skills/writing/anti-ai-writing/)** -- Hard-prohibition filter for AI-typical prose patterns. 17 structural tells at word and paragraph level.
- **[schneider-deutsch](skills/writing/schneider-deutsch/)** -- German prose auditor based on Wolf Schneider. 4 modes: AUDIT, PURGE, PREVENTION, COACH.

### Consulting

- **[consulting-strategic-analysis](skills/consulting/consulting-strategic-analysis/)** -- Hypothesis-driven analysis layer: MECE structuring, trade-off mapping, fact/assumption/unknown separation. Runs before any consulting document.

### Content and Thinking

- **[deep-thinking-partner](skills/content/deep-thinking-partner/)** -- Thinking partner for thought leadership. Extracts hidden logic from associative notes, finds cross-domain connections, marks premature conclusions.
- **[observation-to-insight](skills/content/observation-to-insight/)** -- Transforms raw observations into structured insight packages ready for content creation.

## Installation

```bash
# Single skill
cp -r skills/academic/rq-architect ~/.claude/skills/

# All skills
cp -r skills/*/* ~/.claude/skills/
```

## How these skills relate

```
research-lifecycle (orchestrator)
    |
    +-- SCOPE: rq-architect, argument-architecture
    +-- BUILD: theory-section-architect, lit-review-copilot, 
    |         methods-narrative-architect, qualitative-coder,
    |         saturation-auditor, academic-writing
    +-- REVIEW: paper-feedback-pipeline
    |             +-- citation-risk-auditor
    |             +-- hallucination-audit
    +-- FIX: draft-review-loop
    +-- SUBMIT: desk-rejection-preventer, a-journal-architecture

Always active: anti-ai-writing, data-integrity-guard, 
              evidence-discipline, non-sycophant
```

## Context

These come from:
- **Academic publishing** in management (JMS, AMJ-adjacent), information systems (ICIS, HICSS), and defense studies (NATO STO)
- **Qualitative research** across 80+ elite interviews in military, entrepreneurship, and digital governance
- **Strategic consulting** in telecom, fintech, and edge AI
- **Teaching** Marketing of Innovation at Munich Business School

Not everything is polished. Some skills reference frameworks that are explained in the skill itself. Some chain together and work better as a set.

Questions or feedback: post@stepanini.de

## License

MIT
