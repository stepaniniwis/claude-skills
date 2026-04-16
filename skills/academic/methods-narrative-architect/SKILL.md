---
name: methods-narrative-architect
description: >
  Builds the prose narration of analytical procedures for qualitative and mixed-methods papers.
  Not the design (that exists), but the STORY of how data became findings became theory.
  Solves the most common reviewer complaint: "the transition from data to model is too abrupt."
  Covers: research design justification, sampling logic narration, analytical step chains,
  trustworthiness arguments, data-structure-to-model bridges. Methodology-aware: knows what
  Gioia, Grounded Theory, Case Study, fsQCA, and Thematic Analysis each require in the methods
  narration. Grounded in Pratt (2009), Gioia et al. (2013), Langley (1999), Eisenhardt (1989).
  Trigger: "write my methods section", "methods narrative", "analytical procedure", "how do I
  explain my analytical steps", "reviewer says data-to-theory is opaque", "methods transparency",
  "analytical bridge", "how did I get from data to model".
---

# Methods Narrative Architect

Writes the analytical story that makes reviewers trust your findings.

## The Problem This Skill Solves

Qualitative researchers often HAVE a rigorous analytical process but FAIL to narrate it. The result: reviewers write "the derivation of models from the data lacks transparency" — not because the work was sloppy, but because the prose skipped steps the reader needed to follow.

This skill builds the narration. Not the design. Not the analysis. The prose that connects them.

## Core Principle: Show the Chain

Every methods section must contain an unbroken chain from **raw data** to **final theoretical claim**. Each link must be visible:

```
Transcripts → Segments → Codes → Themes → Constructs → Model
     ↑            ↑          ↑         ↑          ↑          ↑
   "We had"   "We read"  "We coded" "We grouped" "We theorized" "We assembled"
```

The reviewer must be able to point to ANY construct in your model and trace it backward to specific data through explicit analytical steps. If any link is missing, the reviewer writes "insufficiently transparent."

---

## Mode Detection

| Input | Mode |
|---|---|
| Research design + data + request to write methods | → NARRATE |
| Existing methods section + "what's missing?" | → DIAGNOSE |
| "Reviewer says my methods are opaque" + section | → REPAIR |
| Coding results + "how do I explain how I got here" | → BRIDGE (→ use abductive-bridge for construct-level) |

---

## Mode NARRATE: Build the Methods Story

### Step 1: Identify the Methodology's Narration Requirements

Different methodologies demand different narration structures. Match first.

| Methodology | Required Narration Elements | Common Gap |
|---|---|---|
| **Gioia** | Data structure table, FOC→SOT→AD progression, informant quotes as evidence | The leap from SOT to AD — how themes became dimensions |
| **Grounded Theory** | Open → axial → selective coding, theoretical sampling decisions, memo excerpts | When and why theoretical sampling changed direction |
| **Case Study (Eisenhardt)** | Within-case analysis → cross-case patterns → theory | How cross-case comparison produced constructs vs. just listing similarities |
| **Thematic Analysis (Braun & Clarke)** | Familiarization → coding → theme searching → reviewing → defining | How themes were DEFINED (not just found) |
| **fsQCA** | Calibration decisions, truth table construction, logical minimization | Why calibration thresholds were set where they were |
| **Process Research (Langley)** | Temporal bracketing, event identification, mechanism abstraction | How events became mechanisms |

### Step 2: Write the Analytical Step Chain

For EACH step in the analytical process, write one paragraph containing:

1. **What was done** (the action — e.g., "We coded 14 transcripts")
2. **How it was done** (the procedure — e.g., "attending to participants' language")
3. **What it produced** (the output — e.g., "yielding 249 coded segments")
4. **What decision it forced** (the analytical judgment — e.g., "requiring us to distinguish between pragmatic and symbolic formalization")
5. **What came next and why** (the transition — e.g., "This distinction prompted a second coding pass focused on...")

**The critical element is #4.** Steps 1-3 are mechanical. Step 4 is where the researcher's judgment enters — and where reviewers need transparency. A methods section that only has steps 1-3 reads like a recipe. A methods section with step 4 reads like an analytical narrative.

### Step 3: Write the Data-to-Model Bridge

This is the hardest paragraph in any qualitative paper. It answers: "How did your analytical steps produce your theoretical model?"

**Template (adapt, never use verbatim):**

> [The final analytical step / After completing X analysis], we [specific action — e.g., "re-read all coded material"]. [The question that guided this step — e.g., "asking which themes recur across multiple phases"]. [What the action revealed — e.g., "Three themes operated across phase boundaries"]. We [theorized / interpreted / conceptualized] these as [construct name] because [explicit reasoning — e.g., "they shared a common function: converting X into Y"]. [Alternative interpretation considered and why rejected — e.g., "An alternative reading — that these themes simply appeared late — was inconsistent with their presence in early-phase accounts"].

**Anti-patterns to avoid:**
- "Themes emerged from the data" — themes don't emerge; researchers construct them. Say how.
- "Through iterative analysis, we identified..." — what was iterated? Between what? When did you stop?
- "The model was grounded in the data" — show the grounding, don't assert it.
- "We followed Gioia methodology" — following is not narrating. What did following look like?
- **Naming results in the methods section** — the methods section describes analytical STEPS (what you did), not analytical RESULTS (what you found). Do not name emergent constructs, phase labels, mechanism names, or model components. Use generic language: "temporal analysis revealed phase clustering" not "we identified six phases called X, Y, Z." "Cross-case comparison identified recursive patterns" not "we found a Growth Loop and a Recalibration Loop." The findings section is where constructs get their names. This applies to all inductive methodologies (Gioia, Grounded Theory, Thematic Analysis). Violation is not a prose issue but an epistemological one: it implies the constructs were known before the analysis produced them.

### Step 4: Write the Trustworthiness Paragraph

This is NOT a checklist ("we ensured credibility, transferability, dependability, confirmability"). It's a narrative of the specific measures taken and why.

| Criterion | What to narrate (not assert) | Example |
|---|---|---|
| Credibility | What verification was done and what it found | "Verification of 249 segments against transcripts revealed 14 misattributions — nine interviewer speech, three content mismatches, two duplicates" |
| Transferability | What contextual detail enables readers to judge applicability | "The German Nebengewerbe framework provides structural conditions absent in other jurisdictions" |
| Dependability | What coding consistency was achieved and how | "Two coders independently coded a subset; 89% agreement; disagreements resolved through discussion" |
| Confirmability | How researcher bias was managed | "The anti-smoothing protocol required active search for counter-evidence after each case" |

### Step 5: Assemble and Check

Before output, run the **Invisible Step Test**:

Read the methods section aloud. At every point where a reasonable reviewer could ask "but how did you get from X to Y?", there must be a sentence that answers. If there isn't, write one.

**Specific checkpoints:**
- [ ] Can a reader trace any construct in the model backward to specific data?
- [ ] Is every analytical judgment made explicit (not buried in "iterative analysis")?
- [ ] Are alternative interpretations mentioned at least once?
- [ ] Is the number of analytical steps stated and consistent?
- [ ] Does the section explain WHEN coding stopped and WHY?

---

## Mode DIAGNOSE: Find What's Missing

Read the existing methods section. For each of the five elements in Step 2 (what/how/output/decision/transition), mark present or absent per analytical step.

**Output format:**

```
## Methods Transparency Diagnosis

### Analytical Steps Identified: [n]

| Step | What | How | Output | Decision | Transition | Verdict |
|------|------|-----|--------|----------|------------|---------|
| 1. Open coding | ✓ | ✓ | ✓ | ✗ | ✗ | OPAQUE — reader cannot see why coding decisions were made |
| 2. Theme grouping | ✓ | ✗ | ✓ | ✗ | ✗ | BLACK BOX — procedure not described |
| ... | | | | | | |

### Critical Gaps:
[List the missing links that a reviewer will flag]

### Suggested Additions:
[Specific sentences or paragraphs to write, with placement instructions]
```

---

## Mode REPAIR: Fix Reviewer-Flagged Opacity

Input: Reviewer comment + existing methods section.

Process:
1. Parse exactly what the reviewer is asking for
2. Identify which analytical step(s) the comment targets
3. Draft the missing narration using Step 2 protocol
4. Check that the addition doesn't contradict other parts of the section

**Common reviewer complaints and what they actually mean:**

| Reviewer writes | They mean | Fix |
|---|---|---|
| "The derivation lacks transparency" | I can't see how data became model | Add Step 4 (decisions) to each analytical step |
| "Insufficient analytical mediation" | The jump from quotes to constructs is too fast | Add a data-to-model bridge paragraph (Step 3) |
| "How was X identified?" | The construct appeared without explanation | Show the coding path that produced it |
| "The relationship between [framework] and [model] is unclear" | Two theoretical structures coexist without explicit connection | Add a paragraph explaining how they nest/interact |
| "The interpretation moves too quickly" | Findings section mixes data and theory | Separate descriptive findings from theoretical interpretation |

---

## Methodology-Specific Requirements

### Gioia

The Gioia data structure (FOC → SOT → AD) is a TABLE, not a narration. The methods section must narrate what the table shows:
- How were first-order concepts generated? (from participant language, in-vivo where possible)
- How were second-order themes derived? (constant comparison across FOCs — say WHAT was compared)
- How were aggregate dimensions formed? (grouping SOTs — say WHAT principle guided grouping)
- How does the data structure connect to the process model? (THIS is usually missing)

### Grounded Theory

Narrate the theoretical sampling decisions: who was sampled next and WHY, based on what the previous data showed. This is the hallmark of GT and is almost always under-narrated.

### Case Study (Eisenhardt)

Narrate the cross-case analysis explicitly: which cases were compared, on what dimensions, what patterns held vs. broke. The word "pattern" requires evidence.

### fsQCA

Narrate calibration: why were thresholds set where they were? What theory or empirical distribution justified full-membership, crossover, and full-non-membership anchor points?

---

## Integration with Other Skills

- **qualitative-coder:** Produces the coding that this skill narrates. Use qualitative-coder first, methods-narrative-architect second.
- **abductive-bridge:** Handles the construct-level leap (codes → constructs). This skill handles the procedural narration; abductive-bridge handles the theoretical reasoning.
- **research-examiner:** Uses this skill's output as input for its Methods Transparency Audit (Section 0.3 and Dimension 6).
- **paper-arc-architect:** The methods section's emotional job is Doubt → Confidence. This skill builds the confidence.
- **saturation-auditor:** Produces saturation claims that this skill integrates into the trustworthiness narration.
- **anti-ai-writing:** Always active on the output. Methods prose is especially vulnerable to template-speak ("we iteratively analyzed", "themes emerged").

## Key References (Embedded Knowledge)

- **Pratt (2009)** "For the Lack of a Boilerplate" AMJ — What qualitative methods sections need
- **Gioia et al. (2013)** "Seeking Qualitative Rigor" ORM — Data structure methodology
- **Langley (1999)** "Strategies for Theorizing from Process Data" AMR — 7 strategies for process research narration
- **Eisenhardt (1989)** "Building Theories from Case Study Research" AMR — Cross-case analysis narration
- **Tracy (2010)** "Qualitative Quality" QI — Eight criteria for excellent qualitative research

Sprache folgt dem Input (Deutsch / English).
