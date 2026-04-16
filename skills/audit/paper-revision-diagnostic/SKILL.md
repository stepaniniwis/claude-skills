---
name: paper-revision-diagnostic
description: "Pre-revision diagnostic that runs BEFORE any substantive paper revision. Asks the hard framing questions before a single word is written. Prevents the most expensive failure mode: polishing a paper whose framing doesn't hold. Trigger BEFORE starting any paper revision, major rewrite, or version bump. Also trigger on: 'rewrite section X', 'revise for journal Y', 'strengthen the paper', 'new version', 'v[N+1]', or any request that will produce a new paper version. Do NOT trigger on minor edits, formatting, reference fixes, or copy-editing."
---

# Paper Revision Diagnostic

The most expensive revision failure is not bad prose — it is good prose serving a weak frame. This skill forces the framing questions BEFORE any writing begins.

## Why This Exists

Session 2026-03-25: An external advisor reviewed the MDO paper and did not polish — he repositioned. "Readiness Trap" became "Selective Adaptation under Geopolitical Pressure." New RQ, new findings architecture, new theoretical vocabulary. The content was the same data. The framing was completely different. The result was a fundamentally stronger paper.

Claude's default behavior is to improve within the existing frame — better formulations, cleaner structure, tighter prose. That is revision as polishing. What was missing: revision as repositioning. Asking whether the frame itself holds before optimizing within it.

## When Active

Before ANY substantive paper revision. The diagnostic takes 5-10 minutes. A wrong frame wastes days.

Trigger on:
- "Revise paper X for journal Y"
- "New version / v[N+1]"
- "Strengthen the theory / contribution / framing"
- "Rewrite section X" (if section is Introduction, Theory, or Discussion)
- Any request that will produce a new paper version
- When returning to a paper after a break (session boundary = frame check)

Do NOT trigger on:
- Copy-editing, formatting, reference fixes
- Minor prose improvements within a section
- Data analysis, figure generation
- When the user explicitly says "just fix X, don't re-evaluate"

## The Diagnostic (7 Questions)

Run these IN ORDER. Present findings to the user BEFORE starting any revision work. The user decides which findings to act on.

### Q1: Does the Framing Hold?

Read the current draft's title, abstract, RQ, and contribution claim. Then ask:

- Is the framing proportional to what the data actually show?
- Could a hostile reviewer reframe the entire paper more compellingly with the same data?
- Is there a stronger story hiding inside the current story?

**The test:** State the paper's core claim in one sentence. Does it sound like a genuine insight — or like a dressed-up description? If the latter, the frame needs work before anything else.

**What the advisor did that Claude didn't:** He looked at MDO data showing Tech > Governance asymmetry and asked: "Is this a readiness problem or a selective adaptation problem?" Same data, fundamentally different theoretical claim. The reframe changed the RQ, the findings structure, and the contribution.

### Q2: What is the Construct-Level Contribution?

Most papers describe findings. Strong papers make construct-level moves: purification (showing a composite is actually multiple independent things), reconceptualization (redefining what something IS), or mechanism specification (explaining WHY, not just WHAT).

- What construct does this paper advance, challenge, or purify?
- Is the contribution currently stated as a finding ("we found X") or as a construct move ("X is not what prior theory assumed")?
- If the construct contribution is buried in the findings — pull it into the abstract and introduction.

**The test:** Would a theorist in the parent literature recognize this paper as advancing THEIR conversation — or would they see it as an empirical case study that happens to cite their work?

### Q3: Which Benchmark Papers Define the Target Architecture?

Every target journal has implicit structural norms. Before revising, identify 2-3 published papers that:

- Appeared in the target journal (or same tier)
- Used a comparable method (qual field study, survey, experiment, etc.)
- Made a similar TYPE of contribution (construct development, mechanism identification, theory extension)
- Came from a specialized setting but generalized to broader management theory

These papers are the architectural blueprint. Not for content — for structure: How long is the theory section? How many findings? How does the Discussion connect back to theory? What level of generalization does the journal expect?

**The test:** Can you name the 2-3 papers whose structure this revision should mirror? If not, find them before writing.

### Q4: Are All Data Sources Analytically Exploited?

Most papers underuse their data. Common blind spots:

- **Prescreener/survey data** treated as sampling tool only (could be triangulation evidence)
- **Extreme cases** buried in the cross-case analysis (could be lead cases for key findings)
- **Contradictory cases** mentioned as limitations (could be boundary condition evidence)
- **Metadata** (timing, sequence, role differences) ignored

For each data source: What analytical work is it currently doing? What COULD it do?

**The test:** For each data source in the study, state its current analytical role AND one additional role it could play. If you can't think of an additional role, you've exploited it. If you can — you haven't.

### Q5: Who is the Lead Case for Each Finding?

Strong qualitative papers anchor each finding in a vivid, extended case — not in a parade of short quotes from different participants. The lead case is the participant whose data most powerfully illustrates the mechanism.

For each finding:
- Who is the current lead case? (The participant with the most quotes/space)
- Who SHOULD be the lead case? (The participant with the most extreme/clear manifestation of the mechanism)
- Are these the same person? If not, why not?

**The test:** For each finding, identify the participant with the most extreme score/manifestation. If that person is not the lead case, there should be a good reason (data quality, confidentiality). If there's no good reason, restructure.

### Q6: What Canonical Theory Explains the WHY?

Findings describe WHAT happens. Theory explains WHY. For each major finding, ask:

- Is there a canonical theoretical explanation for this mechanism?
- Is that theory currently cited — or is the finding presented as self-evident?
- Would adding the theoretical mechanism change how the finding reads?

Look specifically for:
- **Institutional theory** (Meyer & Rowan, DiMaggio & Powell, Brunsson) for decoupling, selective adoption, talk-action gaps
- **Attention-based view** (Ocasio) for why some things get prioritized
- **Resource dependence** (Pfeffer & Salancik) for cross-boundary coordination failures
- **Diffusion theory** (Strang & Soule, Rogers) for why some innovations spread faster
- **Capability traps** (Levinthal & March) for why organizations exploit rather than explore

This is not about citation padding. It is about giving findings theoretical depth — showing that the observed pattern is an instance of a known mechanism, which makes the contribution generalizable.

### Q7: What Would a Hostile Reviewer Attack First?

Before the user invests time in revision, surface the three most likely attack vectors:

1. **Framing attack:** "This is just [simpler description] — why do we need a new construct/framework?"
2. **Method attack:** "The sample/design cannot support this claim"
3. **Theory attack:** "Author X already showed this in [year]"

For each: state the attack, assess its severity (fatal / serious / manageable), and suggest the defense.

## Output Format

Present the diagnostic as a structured report:

```
PAPER REVISION DIAGNOSTIC — [Paper Name] — [Date]

TARGET: [Journal, deadline if known]
CURRENT VERSION: [filename]

Q1 FRAMING: [Hold / Needs Repositioning / Uncertain]
[2-3 sentences on what the frame is and whether it holds]

Q2 CONSTRUCT CONTRIBUTION: [Clear / Buried / Missing]
[What the construct move is — or should be]

Q3 BENCHMARK PAPERS: [Named / Not Yet Identified]
[2-3 papers with journal, year, and why they're relevant as architecture]

Q4 DATA EXPLOITATION: [Fully Used / Underused Sources Listed]
[Which data sources have untapped analytical potential]

Q5 LEAD CASES: [Aligned / Misaligned]
[Per finding: current lead vs. optimal lead]

Q6 THEORETICAL DEPTH: [Grounded / Gaps Listed]
[Which findings lack canonical theoretical explanation]

Q7 ATTACK VECTORS: [Top 3]
[Attack, severity, defense]

RECOMMENDATION: [What to do before writing — reframe, restructure, or proceed]
```

## After the Diagnostic

The user decides. Possible outcomes:

- **Proceed:** Frame holds, start revising within existing structure
- **Reframe first:** Frame needs work — do Q1/Q2 work before touching prose
- **Load benchmarks:** Find and analyze benchmark papers before revising
- **Restructure findings:** Realign lead cases and data exploitation before prose
- **Partial revision:** Some sections need the diagnostic findings, others don't

The diagnostic is information, not a mandate. But the information comes BEFORE the writing, not after five versions.

## Phase 2: Section-by-Section Revision Map

After the diagnostic (Phase 1) and before writing (Phase 3), run a section-by-section revision map. This phase translates diagnostic findings into concrete revision instructions per section. Derived from advisor feedback on MDO v12 revision (2026-03-25) and analysis of JMS award paper patterns.

### Abstract Revision

Check whether the Abstract delivers the full mechanism chain in one movement:
- Geopolitical pressure → [mechanism] → [structural location] → [outcome]
- All three named elements (mechanism, structure, outcome) must appear
- The Abstract must contain the paper's reviewer-memorable sentence

**Test:** Read the Abstract. Can a reviewer paraphrase the contribution in one sentence? If not, the chain is broken.

### Introduction Revision

The Introduction is the highest-leverage revision zone. Check:

1. **Paper-in-one-sentence:** Does the Introduction contain a single sentence that captures the entire argument? It should appear in the first third, after the puzzle is established. Template: "This paper explains why [puzzle] by showing that [mechanism], which produces [outcome]."

2. **No Findings in the Introduction.** BLOCKER if the Introduction contains empirical results: numbers ("27 of 33"), breakdowns ("10 of 12 military practitioners"), D-scores, interview quotes, or cross-category patterns. The Introduction opens the puzzle and announces the approach. It says THAT a pattern exists (as motivation) but not HOW STRONG or HOW EXACTLY. Details belong in Findings. This error occurs because writers try to make the Introduction "more convincing" by adding evidence — but evidence in the Introduction spoils the Findings and signals poor structural discipline.

3. **Contribution hierarchy:** Are multiple contributions ranked, not listed as equals? The strongest (typically theoretical) contribution leads. Methodological contributions are subordinated or dropped. Three equally weighted contributions signal scatter.

3. **Rhetorical density:** Is the Introduction carrying too much material? Award papers win by saying less, more sharply. After few paragraphs, there must be one sentence the reader cannot forget.

4. **Call-fit language:** If targeting a Special Issue, does the Introduction echo the Call's vocabulary in 1-2 sentences? This is not cosmetic — it helps editors recognize the submission instantly.

### Theory Section Revision

Check three things:

1. **Concept boundary defense:** Immediately after the first definition of the new concept, are there 3 explicit contrast sentences? Template: "[New concept] is not simply [adjacent concept A], because [distinction]. It is not equivalent to [adjacent concept B], because [distinction]. And it is not reducible to [adjacent concept C], because [distinction]." Without these, reviewers will reject as relabeling.

2. **Mechanism-Structure-Outcome chain:** Is the theoretical chain explicitly named? Mechanism (process/why) + Structural Location (where/what space) + Outcome (observable result). All three must be defined, named, and linked. Example: convergent neglect (mechanism) → governance interstitium (structural location) → selective adaptation (outcome).

3. **Alternative theory proactive dismissal:** Are neighboring theories (decoupling, partial organization, institutional complexity, responsibility diffusion) explicitly distinguished from the paper's argument? This must happen in the Theory Section, not wait for Discussion.

### Findings Revision

1. **Finding subordination:** Is every finding explicitly connected to the main mechanism? Finding 1 should be framed as enabling condition, not as competing insight. Use transitional framing: "Before explaining why adaptation becomes selective, it is important to show why the field can mobilize despite persistent conceptual contestation."

2. **Parallel structure across logics:** If the paper uses multiple categories (logics, types, phases), the findings should mirror the category structure from the Theory Section. Each logic/type gets parallel treatment: same questions answered, same depth, same structure. This increases reviewer confidence.

3. **Deviant cases as boundary conditions:** Deviant cases are not appendix material — they specify when the mechanism weakens. Frame them through the theory: "Where local actors reconfigure the logic structure, the interstitium narrows."

### Discussion Revision

Enforce this sequence:

1. Restate puzzle + mechanism in one compact paragraph
2. Primary contribution to theory (strongest, most space)
3. Secondary contribution (organizations under pressure / field-specific)
4. Boundary conditions
5. Portability beyond the setting (EARLY, not at the end)
6. Adjacent theories: what this IS and IS NOT
7. Implications for future research

**Portability:** The setting is the revealing case, not the terminal scope. The portability paragraph must come in the first half of the Discussion, not as an afterthought. Template: "[Setting] is the revealing case, not the terminal scope condition. The mechanism should travel to any [general class] in which [abstract version of conditions]."

**Inferential tone:** Not "this proves" but "the field-level pattern is best explained by X because alternative accounts fail to explain Y." Claims become robuster by being precise about what the design can and cannot establish.

### Methods Revision (for qualitative papers)

1. **D-score / scorecard defense:** If ordinal scores are used, make the defensive framing maximally visible: "These scores discipline cross-case comparison. They are not measurement." Pratt (2009) warns explicitly against pseudo-quantification of qualitative data.

2. **Prescreener boundary:** If a prescreener/survey exists alongside interviews, the boundary must be explicit: "The prescreener is analytically secondary. The interviews are the primary empirical basis." State this more than once.

3. **Rival explanation display:** List alternative explanations the design addresses (low familiarity, subgroup bias, technology-easier-than-governance) and show why the data pattern is inconsistent with each. This is an inferential virtue, not a weakness.

## Integration

This skill runs in three phases:

**Phase 1 (Diagnostic):** The 7 Questions (Q1-Q7) — assesses framing, data, theory, cases
**Phase 2 (Revision Map):** Section-by-section plan — translates diagnostic into revision instructions
**Phase 3 (Writing):** Handed off to `theory-section-architect`, `academic-writing`, `draft-review-loop`

The skill also connects to `a-journal-architecture` which provides the 7 structural tests for A-journal readiness. Run both: this skill for content/framing questions, `a-journal-architecture` for structural/architectural questions.

Sequence: `paper-revision-diagnostic` (Phase 1+2) → `a-journal-architecture` (structural check) → `theory-section-architect` / `academic-writing` (writing) → `draft-review-loop` (quality assurance)

Sprache folgt dem Input (Deutsch / English).
