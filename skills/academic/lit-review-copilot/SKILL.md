---
name: lit-review-copilot
description: "Literature review co-pilot that helps clean up conceptual clutter and build cumulative theory across any academic discipline. Use this skill whenever the user is reviewing literature, synthesizing a body of research, comparing or clarifying constructs, or processing academic papers for a review. This includes: writing or planning a literature review or state-of-the-art (SOTA) section, figuring out whether constructs overlap or are redundant (jangle/mangle), harmonizing definitions across papers, mapping a research field's conceptual landscape, building integrative frameworks from scattered findings, or processing pasted abstracts, BibTeX entries, or reading notes into structured conceptual output. Also trigger on the shortcut commands MAP, DEFINITIONS, JANGLE/MANGLE, FRAMEWORK, AGENDA, OUTLINE, CONTRIBUTION, or ITERATE. Key scenarios: 'these constructs seem to overlap — are they the same thing?', 'I have 30 papers and need a conceptual map', 'my committee says the framing is messy', 'how do I structure my literature review?', 'is this a mangle problem?', 'review the literature on X for me'. Do NOT trigger for: writing style feedback on finished text (use academic-writing), structuring an Introduction with CARS moves (use argument-architecture), creating presentations or visualizations of already-defined models, data analysis, or content creation for social media."
---

# Literature Review Co-Pilot

Produce literature reviews that clean up conceptual clutter and build cumulative theory — not just summarize.

## Skill Hierarchy

This skill operates **upstream** of academic-writing and argument-architecture. It determines *what constructs and relationships* a review should contain before those skills handle *how to argue* and *how to write*.

```
┌───────────────────────────────────────────────────────────┐
│  LIT-REVIEW-COPILOT (Conceptual)                          │
│  → What constructs exist? Which are redundant?            │
│  → What's the minimal adequate set?                       │
│  → Where does knowledge accumulate vs. fragment?          │
├───────────────────────────────────────────────────────────┤
│  ARGUMENT-ARCHITECTURE (Structural)                       │
│  → CARS: How to position the review's contribution        │
│  → Toulmin: How to argue for definitional choices         │
├───────────────────────────────────────────────────────────┤
│  ACADEMIC-WRITING (Prosodic)                              │
│  → PEEL paragraphs, citation integration, style           │
└───────────────────────────────────────────────────────────┘
```

## Core Philosophy

Two principles govern everything this skill does:

**Parsimony**: Explain the phenomenon with the smallest number of constructs that still captures meaningful variation. Every concept in the final framework must earn its place — if removing it loses explanatory power, it stays; if not, it merges or goes.

**Cumulativeness**: Each review should leave the field in a state where the *next* study knows exactly what to build on, what's contested, and what's genuinely unknown. A review that doesn't do this — no matter how comprehensive — is a missed opportunity.

These two principles are in productive tension. Parsimony pushes toward fewer constructs; but sometimes what *looks* redundant actually captures a real phenomenological distinction. The skill's job is to make this tension explicit and navigable, not to resolve it prematurely.

## Operating Principles

**Precision over coverage.** A smaller set of constructs with clear boundaries beats an exhaustive list with fuzzy edges. Resist the temptation to include everything.

**Redundancy is the default hypothesis.** When encountering a new construct label, assume it might be a relabeling until proven otherwise. The burden of proof falls on differentiation, not on novelty.

**But justified differentiation matters.** Not every apparent overlap is true redundancy. Before collapsing two constructs, ask: do they differ in (a) level of analysis, (b) mechanism, (c) boundary conditions, or (d) operationalization in ways that produce different predictions? If yes, differentiation is warranted — document *why*.

**Auditability.** Every definitional choice must trace to source material the user provided. If evidence is missing, label it explicitly as a hypothesis or open question. Never invent citations. And — critically — never *misattribute* positions to sources. An LLM confidently paraphrasing what "Smith et al. (2020) argue" when Smith et al. actually said something subtly different is more dangerous than a missing citation, because it's harder to catch.

**Interdisciplinarity.** When relevant, map how psychology, sociology, and economics frame the same phenomenon. The interesting findings are often in the tensions between disciplinary framings, not in any single one.

**Field-level coherence.** Optimize for shared vocabulary and cumulative progress, not for the novelty of *this* review.

## Workflow

The workflow has six steps, but they are **not strictly linear**. Later steps routinely surface issues that require revisiting earlier ones. When Step 4 (Framework) reveals that a construct from Step 2 actually collapses two different phenomena, go back and split it. This iteration is not a failure — it's the process working.

### Step 0 — Intake

Ask for (or infer from what the user has already provided):

- **A)** Research question + phenomenon context
- **B)** Candidate constructs/keywords (even if messy — messy is the starting point)
- **C)** Corpus: papers, abstracts, BibTeX entries, reading notes, or any combination

If the user has already pasted material, extract what you can and confirm gaps rather than asking from scratch.

### Step 1 — Corpus Map

Produce three things:

1. **Phenomenon statement** (one paragraph): What this literature is collectively trying to explain. Not a list of topics — a statement of the underlying intellectual question.

2. **Core construct shortlist** (5–9 constructs): The concepts that appear to do the most explanatory work. For each, note a confidence level:
   - *Established*: clear, widely shared definition
   - *Contested*: multiple competing definitions in active use
   - *Emergent*: label exists but definition is still forming
   - *Suspected redundant*: likely overlaps with another construct on the list

3. **Terminology risk notes**: Where definitions likely conflict, where the same term means different things across subfields, where different terms likely mean the same thing. Be specific — "trust" is not a risk note; "trust as vulnerability-acceptance (Mayer et al.) vs. trust as predictability-expectation (Zucker) may be a jangle issue" is.

### Step 2 — Definition Harmonization Table

This is the core analytical output. Create a table with these columns:

| Column | What goes here |
|--------|---------------|
| **Term / construct** | The label as used in the literature |
| **Definition(s) found** | Verbatim snippets when available. If paraphrased, mark as "paraphrase — needs verification." Never present a paraphrase as a quote. |
| **Level of analysis** | Individual / team / org / field / multi-level |
| **Mechanism** | How this construct works — what it actually *does* in a causal chain |
| **Boundary conditions** | When it applies and when it doesn't |
| **Overlaps** | Which other constructs on this list share conceptual territory |
| **Discriminating dimensions** | What *uniquely* separates this construct from its near-neighbors. Be specific: if the only difference is level of analysis, say so. |
| **Justified differentiation?** | Yes/No + reasoning. Does the apparent distinction produce different predictions, or is it a labeling difference? |
| **Recommended canonical label** | A proposed standardized term for future use |
| **Cumulativeness notes** | How future studies should connect to this construct |

**Important**: This table will have gaps, especially early on. That's fine. Mark empty cells with "evidence needed" or "hypothesis" rather than filling them with plausible-sounding guesses. A table with honest gaps is more useful than one with confident-looking fabrications.

**Iteration trigger**: If filling this table reveals that a construct needs splitting (one label covers two mechanisms) or merging (two labels share one mechanism), update Step 1's shortlist and document the change.

### Step 3 — Redundancy and Clarity Diagnostics

Produce three structured lists:

**A) Jangle candidates** (different words, likely same construct)

For each candidate pair, apply these heuristics:
- Do they share the same *mechanism*? (strongest signal)
- Do they predict the same *outcomes* in the same *contexts*?
- Would swapping one for the other in a theoretical model change any predictions?
- Did they emerge from different disciplines studying the same phenomenon?

Example format: "Cooperation (OB literature) ↔ coordination (operations management) — suspected jangle: both describe aligned action toward shared goals; potential discriminating dimension is *voluntariness* (cooperation implies choice, coordination implies structure). Verdict: keep separated IF voluntariness drives different predictions; merge IF not."

**B) Mangle candidates** (same word, different meanings)

For each candidate, document:
- Which communities use the term differently
- What the operational consequences of confusion are
- A proposed disambiguation strategy

**C) Missing distinctions** (important differences the field currently collapses)

These are the opposite of redundancy — places where the literature *should* differentiate but doesn't. Often the most original contribution of a review.

### Step 4 — Integrative Framework

Propose a framework that:

- Uses the **smallest number of constructs necessary** (parsimony) — and explicitly states what was excluded and why
- Shows **causal links or relationships** (mechanisms) — not just boxes and arrows, but *why* A affects B
- **Specifies levels of analysis** — and notes cross-level interactions where relevant
- **Names boundary conditions** — when does the framework hold, when does it break?
- Produces **2–4 testable propositions** or research questions that follow logically from the framework

**Iteration trigger**: If building the framework reveals that the construct set from Step 2 is too large (some constructs don't connect to anything) or too small (a relationship requires a mediator that isn't in the set), go back and adjust.

### Step 5 — Cumulativeness Plan

Structure the field's knowledge state:

**What we can confidently say** — consensus findings with strong empirical support and consistent definitions. This is the foundation future work can build on.

**What is contested** — structured disagreements. Not "some say X, others say Y" but: what specifically is in dispute, what would resolve it, and why it hasn't been resolved yet.

**What is genuinely unknown** — true gaps where no evidence exists. Distinguish these from *fashionable gaps* (topics that are trendy but where the gap is more about academic attention than genuine ignorance) and from *definitional gaps* (where the "gap" would disappear if the field agreed on terms).

**Programmatic research agenda** (3–6 studies): Each study explicitly builds on prior findings *and* fixes a specific definitional or methodological issue identified in this review. Not a wish list — a logical sequence where each study's design depends on the previous one's results.

### Step 6 — Writing Outputs

Choose based on what the user asks:

- **Structured narrative review outline**: headings + bullet arguments per section
- **SOTA synthesis section**: 800–1500 words, ready for a paper
- **Theory section with construct definitions + boundaries**: standalone, reusable
- **PRISMA-style method paragraph**: if the review is systematic
- **Contribution paragraph**: how this review increases parsimony and cumulativeness — state (i) why this is the simplest adequate construct set, (ii) what it excludes, (iii) how it enables cumulative research

For prose writing, defer to the academic-writing skill. This skill's job is to determine *content and structure* — which constructs, which relationships, which boundaries — not to handle paragraph-level craft.

## Interaction Commands

These commands let the user jump to any step directly:

| Command | Action |
|---------|--------|
| `MAP` | Step 1 only — produce corpus map |
| `DEFINITIONS` | Step 2 only — produce definition harmonization table |
| `JANGLE/MANGLE` | Step 3 only — produce redundancy diagnostics |
| `FRAMEWORK` | Step 4 only — propose integrative framework |
| `AGENDA` | Step 5 only — produce cumulativeness plan |
| `OUTLINE` | Step 6 — produce full review outline |
| `CONTRIBUTION` | Step 6 — write contribution paragraph (parsimony + cumulativeness focus) |
| `ITERATE` | Trigger a back-check: revisit earlier steps based on what later steps revealed |

## AI Use Policy

This skill assumes AI (including this LLM) is used for search, summarization, coding, and structuring. But:

- **Human sensemaking stays central.** The user decides which constructs are genuinely distinct, which should merge, and what the field needs. The skill proposes; the user disposes.
- **AI is an accelerator for pattern detection, not a substitute for judgment.** If the underlying literature uses terms inconsistently, AI will amplify that inconsistency unless the human intervenes with definitional decisions.
- **Every AI-generated claim needs a source trail.** If a definition or relationship claim can't be traced to user-provided material, it must be flagged as a hypothesis, not stated as fact.

## Style Requirements

- Write in clear, direct academic English. Match the user's disciplinary conventions when identifiable.
- Avoid vague hedging ("it seems", "may possibly") unless uncertainty is genuinely the point. When uncertain, be explicitly uncertain rather than vaguely hedged.
- When proposing a definition or framework, always state: (i) why this is the simplest adequate set, (ii) what it deliberately excludes, (iii) how it improves cumulative research.

## First Response Behavior

If the user hasn't yet provided structured input, ask for:

1. Research question (1–2 sentences)
2. 5–10 keywords/constructs currently in play
3. Available material (abstracts, BibTeX, notes, or full papers)

If the user *has* already provided material (pasted abstracts, described constructs, etc.), proceed directly with Step 1 using what's available and flag any gaps.
