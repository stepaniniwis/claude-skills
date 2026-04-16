---
name: observation-to-insight
description: Transforms unstructured observations (voice memos, random thoughts, article reactions) into structured insights ready for content creation. Use when raw material needs intellectual processing before becoming a Reel, essay, or post. Identifies reframing opportunities, suggests conceptual terms, maps macro-causes, and flags series potential. Output feeds directly into reel-architect skill.
---

# Observation to Insight Transformer

## Purpose

Convert messy intellectual raw material into structured insight packages. The goal is not to "clean up" but to **find the reframing move** that makes the observation worth sharing.

## Input Types Accepted

1. **Voice memo transcript** – spoken stream of consciousness
2. **Random notes** – bullet points, fragments, half-sentences
3. **Article + reaction** – external source plus "warum so nicht" commentary
4. **Quote + elaboration** – someone else's claim plus your counter/extension
5. **Pattern cluster** – multiple observations that feel related

## Processing Workflow

### Step 1: Extract the Core Irritation

Every worthwhile observation contains an irritation – something that doesn't fit, feels wrong, or contradicts common framing.

Ask:
- What's the **category mismatch**? (Thing is treated as X but is actually Y)
- What's the **hidden assumption** being challenged?
- What **mechanism** is invisible to most observers?

Output: One sentence stating the irritation.

### Step 2: Test Reframing Moves

Apply each pattern from `references/reframing-patterns.md` to the observation. For each that fits, generate:

```
Reframe: [Pattern name]
Setup: [What people think]
Reveal: [What's actually happening]
Tension: [Why this matters / what it costs]
```

Select the 1-2 strongest reframes. "Strongest" = most surprising AND most defensible.

### Step 3: Find the Term

Every insight needs a **handle** – a term that captures the reframe and is memorable.

Options:
- **Reclaim existing term** (give it new precision)
- **Compound new term** (two familiar words, new combination)
- **Borrow from adjacent field** (technical term made cultural)

Test: Can you explain the insight using only this term + one sentence?

### Step 4: Map the Macro-Cause

Zoom out. What structural condition makes this observation possible/inevitable?

Categories to check:
- Platform incentive structure
- Capital allocation logic
- Regulatory gap or excess
- Information asymmetry
- Coordination failure
- Status economy dynamics
- Trust infrastructure gap

Output: One sentence linking micro-observation to macro-cause.

### Step 5: Identify Implications

Who should care, and what should they reconsider?

| Audience | Implication type |
|---|---|
| Practitioners | Method/tool critique |
| Institutions | Governance blind spot |
| Individuals | Reframe personal behavior |
| Researchers | New research question |

Select primary audience. State implication as question or claim.

### Step 6: Check for Series & Connections

**Series potential:** Does this observation...
- Belong to a recurring theme? (trust, platforms, governance, aesthetics)
- Have natural "part 2" potential? (setup/payoff structure)
- Connect to a larger argument building across content?

**Connection to existing work:** Could this...
- Reference or extend a previous Reel?
- Contradict/update a previous position?
- Provide evidence for a standing claim?

Flag any matches. Note: "Masterpiece first, series second" – every piece must stand alone.

---

## Output Format

Deliver structured insight package:

```markdown
## Insight Package: [Working Title]

### Core Irritation
[One sentence]

### Strongest Reframe
- Pattern: [Name]
- Setup: [Common view]
- Reveal: [Actual mechanism]
- Tension: [Stakes]

### Anchor Term
- Term: [Word/phrase]
- Definition: [One sentence]
- Why this term: [Precision gain]

### Macro-Cause
[One sentence: micro → macro link]

### Primary Implication
- Audience: [Who]
- Claim/Question: [What they should reconsider]

### Series/Connection Notes
[Flags, or "Standalone piece"]

### Readiness Assessment
- [ ] Reframe is surprising AND defensible
- [ ] Term is memorable AND precise
- [ ] Macro-cause is structural, not individual
- [ ] Implication is actionable insight, not moral judgment
- [ ] Can be explained in 60 seconds

### Next Step
→ Ready for reel-architect? [Yes / Needs X]
```

---

## Quality Gates

**Do not pass to reel-architect if:**
- Reframe is obvious (everyone already knows this)
- Reframe is indefensible (clever but wrong)
- No clear term emerged (concept soup)
- Implication is "people should be better" (moral, not structural)
- Observation requires >90 seconds to set up (too complex for Reel → essay instead)

**Redirect options:**
- Essay format (for complex, multi-layered arguments)
- Thread format (for evidence-heavy claims)
- Hold for clustering (observation is fragment, wait for pattern)
