---
name: theory-section-architect
description: "Architects theory sections for academic manuscripts — the intellectual heavy lifting between positioning (CARS) and prose (PEEL). Handles theoretical grounding in literature, coherent framework construction, theoretical tension surfacing and resolution, hypothesis/proposition development, and theory-empirics linkage. Supports conceptual papers, empirical papers, mixed-methods, and systematic reviews. Three modes: (1) Scaffold — architecture the theory section's logic, (2) Draft — write actual theory section prose, (3) Review — diagnose weaknesses in existing theory sections. Triggers on: 'theory section', 'theoretical framework', 'build my theory', 'develop hypotheses from theory', 'ground my argument', 'theoretical contribution', 'conceptual model', 'construct definitions', 'theoretical tensions', or any request to write, structure, or critique a theory section. Also trigger when a user has a CARS-positioned paper and needs to build out the theoretical argument before writing prose."
---

# Theory Section Architect

Construct theory sections that carry argumentative weight — not literature summaries with a framework bolted on.

## Position in the Skill Hierarchy

```
argument-architecture (CARS + Toulmin)
  → Positions paper, identifies gap, structures claims
    ↓
theory-section-architect (THIS SKILL)
  → Constructs the theoretical framework that fills the gap
  → Grounds in literature, resolves tensions, derives hypotheses
    ↓
academic-writing (PEEL + Style)
  → Renders the framework in publishable prose
```

This skill bridges the gap between "why this paper matters" and "how to write it well." It handles the substantive theoretical thinking that neither positioning nor prose skills address: What constructs? Why these and not others? How do they relate? What tensions exist? What follows logically?

If the user has already used argument-architecture, start from their CARS output. If not, begin with a brief positioning check before diving into theory construction.

## Six Design Principles

These govern every theory section this skill produces.

### 1. Ground Theory in Existing Literature

Start from the scholarly conversation, not from a blank canvas. Every construct, relationship, and mechanism in the framework should trace back to existing work — even when challenging it. Grounding means showing the intellectual genealogy of ideas: where they come from, how they evolved, and why the current state is insufficient.

**Not this**: "We define X as..." (appearing from nowhere)
**This**: "While early work conceptualized X as [original definition] (Author, Year), subsequent research revealed [limitation] (Author, Year). We reconceptualize X as [your definition] to account for [what was missing]."

Grounding is not citation dumping. It is showing the reader the logical path from existing knowledge to your theoretical position.

### 2. Develop a Coherent Theoretical Framework

A theory section is not a parade of constructs. It is an architecture where every element has a function and every relationship has a justification. Coherence means:

- **Ontological consistency**: Constructs operate at compatible levels of analysis
- **Logical necessity**: Each construct earns its place (remove it and the framework breaks)
- **Relational clarity**: Every arrow in the model has a named mechanism
- **Boundary specification**: The framework explicitly states where it applies and where it doesn't

Test coherence by asking: "If I remove construct X, does the framework still make its argument?" If yes, X doesn't belong.

### 3. Surface and Resolve Theoretical Tensions

The best theory sections don't just synthesize — they reveal where existing perspectives collide and then offer resolution. Tension management involves:

- **Identifying contradictions**: Where do established theories make incompatible predictions about the phenomenon?
- **Diagnosing the source**: Is the tension definitional (same term, different meanings), level-based (individual vs. organizational), contextual (different boundary conditions), or paradigmatic (different epistemological commitments)?
- **Resolving productively**: Integration (show both are right under different conditions), synthesis (create a higher-order framework), dialectical resolution (thesis + antithesis → new synthesis), or strategic bracketing (acknowledge and scope out)

Tension is not a problem to avoid — it is where theoretical contribution lives.

### 4. Focus on Theoretical Contribution

Every theory section should pass the "So what?" test at the framework level. Contribution types for theory sections specifically:

| Type | What It Does | Example Move |
|------|-------------|--------------|
| **New construct** | Introduces a concept the field lacks | "We introduce the construct of X, defined as..." |
| **New relationship** | Proposes an untheorized connection | "We argue that X influences Y through mechanism Z" |
| **Reconceptualization** | Redefines an existing construct | "Contrary to [prior view], we propose X is better understood as..." |
| **Integration** | Bridges separate theoretical streams | "Bringing together [Theory A] and [Theory B] reveals..." |
| **Boundary condition** | Shows where theory breaks or holds | "This relationship holds when [condition], but reverses when..." |
| **Mechanism specification** | Explains the how/why behind a known relationship | "The mechanism connecting X to Y operates through..." |

Articulate the contribution type explicitly. Reviewers should never have to guess what's new.

### 5. Use Clear and Precise Language

Theoretical sophistication lives in the precision of concepts, not the complexity of sentences.

- **Define every construct** on first use — with boundaries (what it is AND what it is not)
- **Distinguish adjacent constructs** explicitly — if two terms could be confused, explain the difference
- **Name mechanisms** — "influences" is not a mechanism; "reduces perceived risk, which increases willingness to..." is
- **Avoid false precision** — don't quantify what's qualitative; don't claim causation from correlation
- **Match abstraction to purpose** — abstract enough to generalize, concrete enough to operationalize

### 6. Link Theory to Empirical Research

Theory that cannot be tested is philosophy. Every theoretical claim should have an empirical shadow — a way it could, in principle, be supported or falsified. Linkage means:

- **Constructs → Measurable variables**: Each construct maps to observable indicators
- **Relationships → Testable predictions**: Each proposed relationship generates specific expectations
- **Mechanisms → Observable processes**: Each causal pathway implies intermediate steps that can be traced
- **Boundary conditions → Moderators**: Each scope limitation translates to testable contingencies

For purely conceptual papers, this means making the framework "empirically inviting" — showing future researchers how to test it. For empirical papers, this directly informs research design.

### 7. Manage Borrowed Frameworks (Epistemic Status + Threading)

When a paper imports an external framework — one the paper did not develop — four questions must be resolved before writing begins. This principle draws on methodological literature about theory visibility in qualitative research (Bradbury-Jones et al., 2014, 2022), deductive qualitative analysis (Fife & Gossner, 2024), theory-method fit (Gehman et al., 2018), internal coherence (Howard-Grenville et al., 2021), and qualitative writing (Pratt, 2009).

**Question 1: What is the framework's epistemic status in THIS paper?**

Three possible statuses, following Fife & Gossner's (2024) distinction between sensitizing constructs, working hypotheses, and theory under expansion:

| Status | Meaning | What the findings must show | Theory visibility (Bradbury-Jones et al., 2022 QUANTUM) |
|--------|---------|---------------------------|-------------------------------------------------------|
| **Sensitizing concept** | Framework guides attention during analysis but is not itself tested (Blumer, 1954; Bowen, 2006) | Findings stand alone; framework appears in Discussion to explain why they matter. Must state what the data showed that the concept alone could not have predicted. | Level 4 acceptable (theory applied to design) |
| **Empirical finding** | Data demonstrate that participants enact the framework | Findings must show the framework in action — not just label data with its vocabulary | Level 5-6 required (theory applied to analysis / integrated throughout) |
| **Theoretical extension** | Paper modifies or extends the borrowed framework based on evidence | The extension is a contribution; findings must demonstrate what the original framework cannot explain | Level 5-6 required |

These are mutually exclusive *per claim*. A paper can use a framework as sensitizing concept AND make an extension claim — but each specific assertion about the framework must have one status. Ambiguity here is the single most common source of "theory and findings stand next to each other" reviewer feedback.

**Sensitizing concept protocol** (when this status is chosen):
- The framework must NOT appear as a finding header or aggregate dimension
- It appears primarily in the Discussion as interpretive frame
- In Findings, it may appear in 1–2 interpretive sentences per subsection but must not organize the data structure
- The paper must state what the data showed that the concept alone could not have predicted

**Question 2: Does the theory-method fit hold?**

Before scaffolding, declare the paper's theorizing type (Gehman et al., 2018). Then check whether the amount of prior theory matches the declared type:

| Theorizing type | Prior theory in findings | Framework role |
|----------------|------------------------|----------------|
| **Inductive** (Gioia, grounded theory) | Minimal — rich theoretical engagement belongs in Discussion | Sensitizing at most; importing a developed framework into the data structure creates fit problems |
| **Abductive** | Prior theory and emergent findings iterate | Framework can organize analysis but must show modification through data encounter |
| **Deductive-qualitative** (Fife & Gossner, 2024) | Framework explicitly structures analysis | Findings sections organized by framework elements; permitted to "test" propositions qualitatively |
| **Interpretive** | Framework provides vocabulary for meaning-making | Findings show how participants' experiences are illuminated by the framework, not reduced to it |

A mismatch between declared type and actual theory use is a desk-reject risk. Importing a fully developed framework into a Gioia design while claiming inductive emergence is the most common version of this mismatch.

**Question 3: Where must the framework be visible beyond the theory section?**

Produce a **Theory Threading Map** with a postulation/demonstration distinction for each entry. This addresses Bradbury-Jones et al.'s (2014) finding that theory cannot just "be there" — it must perform a visible function in the text.

For each findings subsection, specify:
- Which framework element is active
- Whether the claim is **postulated** (interpretive reading: "this can be read as...") or **demonstrated** (empirical evidence: "P9 enacted X by doing Y, which constitutes Z")
- If demonstrated: cite the specific data that supports the claim
- If postulated: use language that signals interpretive status ("read through the lens of...", "this pattern is consistent with...")

Postulation is not weakness — it is methodological honesty. But a paper that postulates everywhere while claiming empirical findings has a credibility gap.

Template:

```
THEORY THREADING MAP

Framework: [name]
Epistemic status: [sensitizing / finding / extension]
Theorizing type: [inductive / abductive / deductive-qual / interpretive]

| Findings Section | Framework element active | Postulated or demonstrated | How it appears in interpretation |
|-----------------|------------------------|---------------------------|-------------------------------|
| 4.1 Overview    | [element]              | [P/D]                     | [specific interpretive move]   |
| 4.2 Phase 1     | [element or "none"]    | [—]                       | [how, or "not active — justified because..."] |
| ...             | ...                    | ...                       | ...                           |

RQ-Findings alignment check (Howard-Grenville et al., 2021):
- RQ component A: answered in Section [X]
- RQ component B: answered in Section [Y]
- RQ component C: NOT YET ADDRESSED → [action needed]
```

The **RQ-Findings alignment check** is mandatory: extract every theoretical term from the RQ and map it to a specific findings section. Unaddressed components = misfit. Either add findings coverage or narrow the RQ. No exceptions for "implicit" coverage.

**Question 4: Does the framework do work the findings couldn't do without it?**

Three tests, applied sequentially:

*Subtraction test* (from Principle 4): Remove the borrowed framework entirely. Do the findings lose interpretive depth, or do they still make sense as standalone descriptions? If the latter, the framework is decorative.

*Parallel tracks test* (Pratt, 2009): Read the findings section while mentally removing all theoretical vocabulary. Does the section still make sense as pure description? If yes, the theory is labeling, not interpreting. Then read only the theoretical sentences. Do they form a coherent argument? If not, the interpretation is scattered. Both layers must work independently AND together.

*Gioia bridge check* (applies when Gioia or Gioia-adjacent methods are used; Gioia et al., 2013): At the 2nd-order level, verify that each theme name reflects an *analytical* move, not just a framework label. "4D Looping in Phase 2" is a label. "Compressed design-deliver iteration under time pressure" is an analytical move that *earns* the 4D connection.

**Common pathology — the bookend problem**: Framework introduced in theory section → restated in findings overview → absent from actual empirical material → reappears in discussion. The reader experiences theory and findings as parallel narratives rather than integrated analysis.

**Fix pattern**: In at least 2–3 findings subsections, add 1–2 sentences that show the framework *interpreting* the data — not labeling it. "P9's move from freelance writing to negotiating creative conditions at a new employer enacts a compressed Design-Deliver-Discuss cycle" is interpretation. "Phase 2 corresponds to the Design dimension" is labeling.

**Methodological references for this principle:**
- Blumer, H. (1954). What is wrong with social theory? *American Sociological Review, 19*(1), 3–10.
- Bowen, G. A. (2006). Grounded theory and sensitizing concepts. *International Journal of Qualitative Methods, 5*(3), 12–23.
- Bradbury-Jones, C., Taylor, J., & Herber, O. (2014). How theory is used and articulated in qualitative research. *Nurse Researcher, 22*(2), 32–37.
- Bradbury-Jones, C., Breckenridge, J. P., Clark, M. T., Herber, O. R., Jones, C., & Taylor, J. (2022). Improving the visibility and description of theory in qualitative research: The QUANTUM typology. *International Journal of Qualitative Methods, 21*, 1–10.
- Fife, J. E., & Gossner, J. D. (2024). Deductive qualitative analysis: Evaluating, expanding, and refining theory. *Organizational Research Methods*.
- Gehman, J., Glaser, V. L., Eisenhardt, K. M., Gioia, D., Langley, A., & Corley, K. G. (2018). Finding theory-method fit. *Journal of Management Inquiry, 27*(3), 284–300.
- Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2013). Seeking qualitative rigor in inductive research. *Organizational Research Methods, 16*(1), 15–31.
- Howard-Grenville, J., Lahneman, B., & Mitzinneck, B. C. (2021). Achieving fit and avoiding misfit in qualitative research. *Organizational Research Methods*.
- Pratt, M. G. (2009). For the lack of a boilerplate: Tips on writing up (and reviewing) qualitative research. *Academy of Management Journal, 52*(5), 856–862.

## Three Modes

### Mode 1: Scaffold

Architect the logic of the theory section before any prose is written.

**Input**: Research question, identified gap (from CARS), key literatures, initial theoretical intuitions.

**Process**:

1. **Construct Inventory**: List all theoretical constructs needed. For each:
   - Working definition
   - Theoretical origin (which literature stream?)
   - Level of analysis
   - Role in framework (independent, dependent, mediating, moderating, boundary condition)

2. **Tension Mapping**: Identify where existing theories disagree about the phenomenon
   - What predictions conflict?
   - What's the source of disagreement?
   - How will you resolve it?

3. **Framework Architecture**: Design the relational structure
   - Core argument in one sentence
   - Construct relationships with named mechanisms
   - Boundary conditions
   - Level of analysis consistency check

4. **Hypothesis/Proposition Derivation** (if applicable):
   - Each hypothesis flows logically from the framework
   - Warrants are explicit (why does this relationship hold?)
   - Qualifiers are specified (under what conditions?)
   - Alternative explanations are acknowledged

5. **Section Outline**: Sequence the theory section's argument
   - What comes first and why?
   - Where do key definitions go?
   - Where does the framework figure fit?
   - How does it build to hypotheses/propositions?
   - For each section: estimated word count (~pages) and **transition logic** — how §N ends by motivating §N+1 (e.g., "§2 ends with the limitation that RIT explains perception but not enactment, which motivates §3's turn to SIT")

6. **Diagnostic Self-Check**: Run the scaffold through the Contribution Distinctiveness Test and Paper-Type Compliance Check (see below) before presenting to user.

**Output**: A structured scaffold document with construct table, tension map, framework architecture, hypothesis derivation logic, section outline with transition logic, and diagnostic self-check.

### Scaffold → Draft Handoff

When transitioning from Scaffold to Draft mode, the scaffold's section outline becomes the draft's work order. For each section in the outline:

1. **Import**: Pull the relevant constructs, tensions, and mechanisms from the scaffold
2. **Expand**: Each scaffold bullet becomes 1-3 PEEL paragraphs (hand off to academic-writing skill for prose execution)
3. **Transition sentences**: Write the actual prose that connects sections — these are the argumentative joints that hold the theory section together. Each section's final paragraph should contain the "limitation/gap/question that motivates the next section" identified in the scaffold's transition logic.
4. **Check accumulation**: After drafting each section, verify it has advanced the overall argument — not just defined terms

### Mode 2: Draft

Write actual theory section prose, following the scaffold or building one implicitly.

**Process**:

1. **Opening Move**: Establish the theoretical context. Not a full literature review — a targeted synthesis that sets up the framework. Signal the theoretical tradition and where the departure begins.

2. **Construct Development Paragraphs**: For each major construct:
   - Introduce with intellectual genealogy (where does this concept come from?)
   - Define precisely (what it is, what it is not, how it differs from adjacent constructs)
   - Position in the framework (what role does it play?)

3. **Relationship Arguments**: For each proposed relationship:
   - State the claim
   - Provide the theoretical mechanism (not just "X affects Y" but "X affects Y because...")
   - Ground in existing evidence where available
   - Address why alternative mechanisms are less plausible

4. **Tension Resolution** (where applicable):
   - Surface the tension explicitly ("Theories A and B make competing predictions about...")
   - Diagnose the source
   - Present the resolution with justification

5. **Hypothesis/Proposition Statements** (if applicable):
   - Derive each from the preceding argument
   - State formally
   - Include any qualifiers or boundary conditions

6. **Framework Integration**: Tie the pieces together, usually with a theoretical model figure callout and a paragraph explaining how the full framework operates as a system.

**Paper-Type Adaptations**:

**Conceptual papers**: The framework IS the contribution — go deep on construct development and relationships. Every construct needs full intellectual genealogy (not just a definition). Propositions replace hypotheses. Each proposition must specify what empirical pattern would support or falsify it, even though the paper doesn't test it. End the theory section with an explicit "empirical invitation" — a paragraph showing future researchers how to operationalize and test the framework.

**Empirical papers**: The framework serves hypotheses — balance theoretical depth with operational efficiency. Each hypothesis must trace back to a specific construct relationship in the framework AND forward to specific measurement items or operationalizations. Include an explicit construct-to-item mapping table or integrate item references into hypothesis derivation. Flag cross-sectional limitations in the derivation itself (e.g., "indirect effects" not "mediation" when temporal ordering is not established). If novel constructs lack validated scales, acknowledge this and justify the deductive item development.

**Mixed-methods papers**: The framework must justify both qualitative and quantitative components. Theory should show why some constructs require interpretive exploration (qual) while others are ready for measurement (quant). The framework figure should mark which pathways are explored qualitatively and which are tested quantitatively. Sequence justification (qual→quant or quant→qual) must be grounded in the framework's logic, not just methodological convention.

**Systematic reviews**: The framework organizes the analysis — constructs become coding categories, relationships become expected patterns in the literature. Each construct definition must be operationalized as inclusion/exclusion criteria or coding rules. The framework should generate specific questions the review will answer (not just "what do we know about X" but "how do studies differ in their treatment of the X-Y relationship and what explains this variation?").

### Mode 3: Review

Diagnose weaknesses in an existing theory section.

**Diagnostic Protocol**:

| Check | Question | Red Flags |
|-------|----------|-----------|
| **Grounding** | Is every construct traced to literature? | Constructs appearing from nowhere; no intellectual genealogy |
| **Coherence** | Do constructs form a logical system? | Level-of-analysis mixing; constructs without relationships; orphan variables |
| **Tension** | Are competing perspectives acknowledged? | One-sided literature use; ignoring contradicting evidence |
| **Contribution** | Is the novelty explicit AND distinct? | "We combine A and B" without explaining what combination reveals; contribution that sounds like 3+ existing papers |
| **Distinctiveness** | Does the framework pass all five questions of the Contribution Distinctiveness Test? | Fails completion test (reviewer knows 3+ papers doing the same); fails subtraction test (novel element is decorative) |
| **Precision** | Are definitions clear and bounded? | Fuzzy constructs; "influences" without mechanism; overlapping definitions |
| **Empirical Link** | Can the framework be tested? | Untestable claims; constructs without observable indicators |
| **Item Linkage** (empirical papers) | Does each hypothesis trace to specific items/measures? | Hypotheses about constructs that have no operational counterpart in the methods |
| **Flow** | Does the argument build logically? | Constructs defined after they're used; hypotheses disconnected from arguments; missing transition logic between sections |

**Output**: Diagnostic report with specific paragraph-level recommendations, organized by severity (critical / important / refinement).

## Construct Definition Template

When defining constructs, follow this structure (adapt flexibly, not rigidly):

```
[Construct Name]

Intellectual genealogy: Where the concept originates and how it evolved.
Working definition: What it is — precise, bounded.
Boundary: What it is NOT — distinguish from adjacent constructs.
Level of analysis: Individual / team / organization / field / etc.
Role in framework: IV, DV, mediator, moderator, boundary condition.
Observable indicators: How it manifests empirically.
```

## Hypothesis Derivation Logic

Strong hypotheses follow this structure:

```
1. Theoretical premise (grounded in framework):
   "Because [construct X] operates through [mechanism], it should..."

2. Logical inference:
   "When [condition], [X] leads to [Y] because [warrant]"

3. Formal statement:
   "Hypothesis N: [X] is [positively/negatively] related to [Y]
   [when/under conditions of Z]."

4. Alternative consideration:
   "One might argue [alternative]. However, [counter-reasoning]."
```

Every hypothesis is a Toulmin argument in compressed form: claim (the hypothesis), data (the theoretical premises), warrant (the mechanism), qualifier (boundary conditions), rebuttal (alternatives considered).

## Proposition Derivation for Qualitative/Conceptual Papers

Propositions differ from hypotheses: they are testable but not operationalized into variables and scales. They guide data collection and interpretation rather than statistical testing.

Strong propositions follow this structure:

```
1. Theoretical premise (grounded in framework):
   "The framework suggests that [construct X] and [construct Y] interact through [mechanism]."

2. Observable implication:
   "If this holds, we would expect to observe [specific pattern in interviews/cases/texts]."

3. Formal statement:
   "Proposition N: [X] [verb describing relationship] [Y] through [mechanism],
   manifesting as [observable pattern]."

4. Data collection guidance:
   "To explore this proposition, ask/look for: [specific interview questions,
   observational foci, or archival indicators]."
```

The "observable implication" and "data collection guidance" steps are what distinguishes useful propositions from armchair speculation. Every proposition should tell the qualitative researcher what to look for in the data — which interview questions to ask, which episodes in narratives to attend to, which comparisons to make across cases.

## Contribution Distinctiveness Test

After building the framework (in Scaffold or Draft mode), run this test before finalizing. The test catches the most common rejection reason at A-journals: the contribution sounds like what other papers already claim.

### The Five Questions

1. **Completion test**: "If I describe my contribution in one sentence, would a reviewer immediately think of 3+ papers that already do this?"
   - If yes: the contribution is not distinct enough. Sharpen by specifying WHAT the integration/extension/reconceptualization reveals that wasn't visible before.
   - Example fail: "We integrate Role Identity Theory and Social Identity Theory." (Dozens of papers claim this.)
   - Example pass: "We show that the structural impossibility of full prototype conformity in both employee and entrepreneur groups forces hybrid entrepreneurs into managed multiplicity rather than identity integration — a pattern invisible to either theory alone."

2. **Subtraction test**: "If I remove MY novel element, does the framework collapse or does it still work as a reasonable literature review?"
   - If it still works: the novel element is decorative, not structural. Redesign so the framework depends on the contribution.

3. **Prediction test**: "Does my framework generate at least one non-obvious prediction — something a reviewer wouldn't have guessed without the framework?"
   - Non-obvious means: contradicts intuition, specifies an unexpected boundary condition, or identifies a mechanism that changes how we interpret existing findings.

4. **Specificity test**: "Could another researcher read my contribution statement and know exactly what constructs, relationships, or boundary conditions are new?"
   - If the contribution is vague ("we add nuance to...," "we extend understanding of..."), it fails. Rewrite with specific theoretical objects.

5. **Phenomenon test**: "Is there a specific empirical phenomenon or pattern that ONLY my framework can explain?"
   - This is the strongest form of contribution. If yes, name that phenomenon in the theory section. If no, articulate what existing frameworks get wrong that yours corrects.

### Applying the Test

In Scaffold mode: Run after Step 5 (Section Outline), before presenting to user. Report results in the Diagnostic Self-Check.

In Draft mode: Run after completing the framework integration paragraph. If the test reveals weakness, flag it and suggest revisions before proceeding to hypotheses.

In Review mode: Always apply as part of the diagnostic protocol.

## Common Pathologies and Fixes

| Pathology | Symptom | Fix |
|-----------|---------|-----|
| **Literature Report** | Theory section reads like annotated bibliography | Reorganize around YOUR argument, not chronologically or by author |
| **Framework Drop** | Figure appears without build-up | Develop each construct before assembling the framework |
| **Hypothesis Leap** | "Therefore, H1: X→Y" with thin reasoning | Add mechanism paragraph between argument and hypothesis |
| **Construct Sprawl** | 8+ constructs with unclear relationships | Apply parsimony: can any constructs be collapsed? |
| **Tension Avoidance** | Only citing supporting literature | Actively seek and address contradicting perspectives |
| **Level Confusion** | Individual-level mechanism, org-level outcome, no bridge | Specify cross-level mechanisms explicitly |
| **Definition Drift** | Construct means different things in different sections | Define once, use consistently, reference back |
| **Mechanism Vacuum** | "X influences Y" without explaining how | Name the process: through what pathway? |

## Integration with Other Skills

- **Before this skill**: Use argument-architecture to position the paper (CARS) and structure individual claims (Toulmin)
- **After this skill**: Use academic-writing to render the framework in publishable prose (PEEL + Style)
- **Parallel**: Use theory-figure-architect or academic-concept-visualizer for the theoretical model figure
- **Quality check**: Use research-examiner for pre-submission diagnostic

## Reference Files

- `references/tension-resolution-patterns.md`: Extended examples of how to surface and resolve theoretical tensions across paradigms
- `references/framework-archetypes.md`: Common theoretical framework structures (mediation, moderation, process, typology, multi-level) with examples from top journals

## Mandatory Quality Layer: Anti-AI Writing

**This skill always activates the `anti-ai-writing` skill as a non-negotiable filter.**

Theory sections are the highest-risk zone for AI pattern detection because LLMs are specifically trained on theoretical academic prose — and tend to produce construct definitions, relationship statements, and literature syntheses that read as smooth, balanced, non-committal. Apply the full `anti-ai-writing` standard + Academic Module on every output.

Particular vigilance required here:
- **Construct definition nominalization:** "X is conceptualized as the process through which..." → revert to verb-based language
- **Present-participle inflation in proposition statements:** "...thereby highlighting the need for further theoretical development" → cut entirely or make the specific claim
- **Triplet balance in framework descriptions:** frameworks described as "rigorous, systematic, and theoretically grounded" signal LLM origin; describe *what specifically* makes them so, or cut

Meta-argumentative note: A theory section on distrust, legitimacy, or epistemic infrastructure that itself exhibits AI-typical smoothness and hedged comprehensiveness is self-undermining. The argument must be legible in the prose texture.

---

## Theory Contribution Playbook (8-Step Checklist)

Run this checklist on every theory section before delivery. Based on the principle that theory advances through disciplined testing and refinement, not through invention of new frameworks.

### Step 1: Diagnose the Limits of the Dominant Theory
Start with intellectual honesty. Where is the existing theory underspecified, weakly supported, or only partially explanatory? Diagnosing limits is not criticizing theory — it is using evidence to show that even influential theories leave specific questions unanswered. This creates the natural pathway for contribution.

*Test: Can you name the specific assumption, mechanism, or scope condition where the dominant theory falls short — not just "there is a gap"?*

### Step 2: Think Cumulatively, Not in Isolation
A single study rarely advances theory. Position findings within cumulative evidence. Where do prior studies converge? Where do they diverge? What does the overall pattern suggest that individual studies cannot? This is especially important for qualitative work that builds on prior conceptual foundations.

*Test: Does the theory section cite findings from multiple studies to establish a pattern — or does it rely on single-paper claims?*

### Step 3: Separate Core Predictions from Boundary Conditions
Theories make broad claims; evidence reveals where those claims hold and where they break. Distinguish the theory's core mechanism from the conditions that limit its applicability. This increases precision and prevents the false binary of "theory confirmed" vs. "theory failed."

*Test: Can you state one condition under which the theory's central claim does NOT hold — and does the paper frame this as a finding rather than a limitation?*

### Step 4: Integrate Competing Theories
Treat alternative explanations as opportunities, not distractions. Combining theoretical perspectives can reveal mechanisms that a single theory misses. The perception-performance distinction in the PhD (RIT + SIT) is an example: neither theory alone captures the full identity dynamic.

*Test: Does the theory section engage at least one competing or complementary framework — and does it show what each explains that the other cannot?*

### Step 5: Use Effect Sizes to Calibrate Claims
Statistical significance alone says nothing about substantive importance. A "significant" r=.14 does not support the same theoretical claim as a significant r=.62. For qualitative work: distinguish themes that are frequent from themes that are consequential. Frequency is not importance.

*Test: For every empirical claim that supports a theoretical mechanism — is the MAGNITUDE of the effect proportional to the weight the theory section places on that mechanism?*

### Step 6: Clarify Constructs to Prevent Conflation
Theoretical progress often depends on showing that what looks like one construct is actually two (or vice versa). Rename constructs when labels load a literature the operationalization cannot service (CL → Experiential Realness). Split constructs when items serve different psychological functions (PLT = understanding + transparency-demand). Merge constructs when empirical separation is not achieved (TR + TT → System Trust as robustness check).

*Test: For every construct in the framework — does the theoretical label match what the items/data actually capture? Would a specialist in the parent theory recognize their concept in your operationalization?*

### Step 7: Read Inconsistent Findings as Theoretical Signals
Unexpected, weak, or contradictory results are frequently the most valuable sources of theoretical development. When findings diverge from predictions, the question is: what does this discrepancy reveal about the theory? Missing mechanisms, unrecognized boundary conditions, and unmeasured variables often hide in the anomalies.

*Test: Does the discussion treat at least one unexpected finding as a theoretical signal rather than dismissing it as noise or limitation?*

### Step 8: End with Theory-Advancing Questions
Conclusions must articulate specific theoretical questions that emerge from the findings — not generic "future research should." These questions should identify concrete mechanisms, conditions, or interactions that remain unexplored and that would move the theoretical conversation forward.

*Test: Does the conclusion contain at least one question specific enough that a doctoral student could build a study around it — with a clear theoretical mechanism to investigate?*

### Playbook Application Modes

**In Scaffold mode:** Use the 8 steps to DESIGN the theory section's logic before writing.
**In Draft mode:** Use the 8 steps as self-check after writing each subsection.
**In Review mode:** Use the 8 steps as a diagnostic checklist — which steps are present, which are missing?
