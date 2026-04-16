---
name: academic-writing
description: "Academic writing for conceptual and theoretical papers with literature reviews. Use when creating scholarly content requiring clear argumentation, proper citation integration (APA 7th), stylish prose following Helen Sword's principles, and structured paragraphs. Supports three modes: (1) Gerüst/scaffolding for argument structure, (2) drafting full paragraphs and articles, (3) critical review of existing drafts. Triggers on requests for academic papers, literature reviews, theoretical contributions, argument structuring, or citation guidance."
---

# Academic Writing Skill

Create publishable academic prose: precise argumentation, elegant expression, rigorous citation.

## Skill Hierarchy

This skill operates at the **execution layer**. Before applying it:

1. **Structure sections** with CARS (argument-architecture skill)
2. **Define arguments** with Toulmin (argument-architecture skill)
3. **Then write prose** with this skill (PEEL, citation, style)

PEEL realizes arguments—it does not invent them. If a paragraph feels weak, check argument structure first (Toulmin), then fix the prose.

## Core Philosophy

**"Elegant ideas deserve elegant expression."** — Helen Sword

Academic writing is not about complexity for its own sake. The goal is clarity that honors the sophistication of ideas while making them accessible.

## Three-Phase Workflow

### Phase 1: Gerüst (Scaffolding)

Structure the argument before writing:

1. **Central Thesis**: One sentence capturing the core contribution
2. **Argument Map**: How each section advances the thesis
3. **Gap Articulation**: What the literature misses, why it matters
4. **Section Outline**: Topic sentences for each major paragraph

Output: Numbered outline with thesis, gap statement, and section flow.

### Phase 2: Drafting

Write complete sections following the frameworks below. Every paragraph uses PEEL structure. Every claim has citation support. Style follows the 6Cs + 5Cs principles.

### Phase 3: Review

Critique drafts against:
- Argument coherence (does each paragraph advance the thesis?)
- Citation integration (are sources woven into argument, not listed?)
- Style quality (active voice? concrete language? no zombie nouns?)
- PEEL compliance (point, evidence, explanation, link in each paragraph?)

## Argument Structure (Rao Framework)

### Introduction (10-15% of paper)
- Introduce discipline/field and topic
- State the underlying question
- Focus: relevant debate, previous research, problem, scope
- **Signpost**: preview section structure
- **Thesis statement**: your main argument/answer to the question

### Body (80% of paper)
Each section:
- Context/theory establishing the frame
- Issues examined through analysis and evaluation
- Evidence integrated with interpretation
- Clear transition to next section

### Conclusion
- Synthesize findings from each section
- Restate thesis in light of evidence
- Implications for the field/debate

## Paragraph Structure (PEEL)

Every academic paragraph contains:

| Element | Function | Example Signal |
|---------|----------|----------------|
| **Point** | Topic sentence stating the paragraph's claim | First sentence |
| **Evidence** | Cited support (paraphrased or quoted) | Sources in parentheses |
| **Explanation** | Analysis answering "So what?" | Interpretation, significance |
| **Link** | Transition to next paragraph or back to thesis | "This suggests...", "Building on this..." |

**Length**: 200-300 words. One idea per paragraph.

## Citation Integration (APA 7th)

### The Cardinal Rule

**Never**: "Smith et al. (2023) argue that trust is foundational..."  
**Always**: "Trust functions as a foundational element in democratic systems (Smith et al., 2023)."

The argument leads. The source supports. The reader encounters the idea first, attribution second.

### When to Cite

| Situation | Action |
|-----------|--------|
| Specific claim, data, or finding | Cite immediately after claim |
| Established concept, first mention | Cite the seminal source |
| Synthesis of multiple sources | Cite all at end of synthesized statement |
| Your own analysis/argument | No citation needed |
| Common knowledge in the field | No citation needed |

### Paraphrase vs. Direct Quote

**Default to paraphrasing.** Direct quotes only when:
- The exact wording is crucial (definitions, contested terms)
- The original phrasing is particularly eloquent
- You will analyze the specific language used

For detailed guidance: `references/citation-guide.md`

## Style Principles

### Helen Sword's 6 Cs

1. **Communication**: Write to be understood, not to impress
2. **Craft**: Treat writing as a skill requiring practice
3. **Creativity**: Break conventions when they obstruct clarity
4. **Concrete language**: Prefer specific nouns and active verbs
5. **Choice**: Every word is a decision; make it deliberately
6. **Courage**: Take intellectual risks in argument and style

### The 5 Cs of Academic Excellence

1. **Clarity**: One idea per sentence, one theme per paragraph
2. **Coherence**: Logical flow from thesis through evidence to conclusion
3. **Competence**: Demonstrate command of relevant literature
4. **Comprehensive**: Address counterarguments and limitations
5. **Critique**: Evaluate sources, don't just report them

### Anti-Patterns

- **Zombie nouns**: "implementation" → "implement"; "utilization" → "use"
- **Hedging stacks**: "It might perhaps be suggested..." → "This suggests..."
- **Passive evasion**: "It was found that..." → "The analysis revealed..."
- **Citation dumping**: Don't list sources—integrate each into argument

For detailed style guidance: `references/style-guide.md`

## Conceptual/Theoretical Paper Structure

1. **Introduction**: Problem, gap, contribution, roadmap
2. **Literature Review**: Organized thematically around the gap
3. **Theoretical Framework**: Your contribution
4. **Discussion/Implications**: What changes given your argument
5. **Conclusion**: Summary, limitations, future research

Literature review paragraphs synthesize sources around themes—not "Author A says X, Author B says Y."

## Quick Checklist

### Before Writing
- [ ] Thesis in one sentence
- [ ] Gap clearly identified
- [ ] Section outline with topic sentences

### During Writing
- [ ] PEEL in every paragraph
- [ ] Citations integrated, not listed
- [ ] Active voice dominant
- [ ] Concrete nouns, strong verbs

### After Writing
- [ ] Each paragraph advances thesis
- [ ] Transitions connect logically
- [ ] No zombie nouns
- [ ] APA 7th correct
- [ ] **Qualitative papers (Gioia, thematic analysis):** Every participant code in prose verified against coding matrix (see data-integrity-guard skill, Qualitative Paper Consistency Protocol). Prose is a presentation of the coding — not independent of it.
- [ ] **Forward-Reference Audit (long documents):** Every concept, construct, model name, or phase label used in a section must have been introduced in a prior section or earlier in the same section. If a concept appears before its definition, either move the definition earlier or remove the forward reference. Common violations: theory sections defining constructs that emerge from data, methods sections naming findings, overview sections assuming knowledge of models not yet presented. In inductive papers (Gioia, Grounded Theory), this is not a style issue but a methodological error: pre-defining emergent constructs contradicts the epistemological claim.

## Reference Files

- `references/citation-guide.md`: APA 7th patterns and integration examples
- `references/style-guide.md`: Helen Sword principles with examples
- `references/paragraph-structure.md`: Extended PEEL guidance

## Mandatory Quality Layer: Anti-AI Writing

**This skill always activates the `anti-ai-writing` skill as a non-negotiable filter.**

Before delivering any output — scaffolds, drafts, or reviews — apply the full `anti-ai-writing` standard:

- Standard prohibitions (present participle inflation, copula substitution, triplet comprehensiveness, transition overload, etc.)
- **Academic Module** (nominalization chains, literature review parades, methodology passive stacking, hedging in contribution statements, conclusion summary loops)

The Academic Module carries particular force here because reviewer sensitivity to AI-pattern text has increased significantly post-2023. Surface credibility and argumentative credibility are the same problem: wherever the prose performs smooth, hedged comprehensiveness, the underlying argument is usually also incomplete.

**Purge Protocol trigger:** If the user provides existing text for review, run the Academic Purge Protocol from `anti-ai-writing` before any other critique.
