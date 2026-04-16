---
name: citation-risk-auditor
description: "Sentence-level audit for missing citations and unhedged claims in any academic text — papers, thesis chapters, journal articles, literature reviews, theory sections, discussion sections. Classifies every claim-type that triggers reviewer skepticism (R1–R8: literature-claims, empirical-trends, strong-generalizations, absolute-gaps, superlatives, causal-inference from anecdote, methodological-absolutism, theoretical-concept-orphans) and prescribes exactly: add citation, hedge language, or reframe as explicit own argument. NOT the same as research-examiner (which checks citation accuracy) — this skill finds WHERE citations are absent. Trigger on: 'citation audit', 'where do I need citations', 'is this defensible', 'unbelegt', 'check my claims', 'reviewer will ask for sources', 'is this ok to submit', pasting ANY academic paragraph and asking if it holds up, uploading any draft before supervisor review or journal submission. Apply to every section type: introduction, theory, method, findings, discussion equally."
---

# Citation Risk Auditor

Finds unprotected claims before reviewers, supervisors, or examiners do.

**Core distinction from research-examiner**: Phase 0.1 of research-examiner checks whether *existing* citations are accurate. This skill finds where citations are *missing* — sentences that make claim-types that demand evidentiary backing but have none.

**Applies to all academic text types**: Introduction, literature review, theory section, methodology rationale, findings interpretation, discussion, conclusion. The risk types are the same across all sections; only the density varies.

**Position in pipeline**: After academic-writing or theory-section-architect. Before research-examiner. Can also run as inline filter during writing of any section.

---

## Not Every Sentence Needs a Citation

Before auditing: establish what is citation-exempt, to avoid false positives.

**Citation-exempt sentence types:**
- Signposting ("This chapter argues...", "Section 3 develops...")
- Explicit own-argument markers ("This thesis proposes...", "I define X as...")
- Pure logical inference from already-cited premises ("It follows that...")
- Definitions explicitly set by the author ("For the purposes of this study, X refers to...")
- Methodological design rationale framed as design choice ("A dual-strand design cannot observe both dimensions simultaneously — by construction")

**Everything else is potentially auditable.** The seven risk types below are the actual targets.

---

## Step 0: Quick-Screen (run first)

Before sentence-level audit, search the text for these trigger strings. Each hit is a probable risk location:

| String | Risk Type |
|--------|-----------|
| `"the literature"` / `"scholars have"` / `"research shows"` / `"studies suggest"` | Literature-claim (R1) |
| `"growing"` / `"increasing"` / `"rising"` / `%` without source / `"widespread"` | Empirical-trend (R2) |
| `"structural"` / `"modal"` / `"systemic"` / `"normalized"` / `"constitutive"` as fact | Strong-generalization (R3) |
| `"no study"` / `"none have"` / `"the only"` / `"first to"` / `"has not yet"` | Absolute-gap (R4) |
| `"most"` / `"largest"` / `"most widely"` / `"primary"` / `"dominant"` as rank | Superlative (R5) |
| journalistic / non-academic source + structural claim in same sentence or paragraph | Causal-inference (R6) |
| `"predominantly"` / `"exclusively"` / `"only"` / `"entirely"` about field practice | Methodological-absolutism (R7) |
| theoretical construct used as established fact, no founding source cited | Theoretical-orphan (R8) |

Flag all hits. Then proceed to full audit.

---

## The Seven Risk Types

### R1 — Literature-Claim
**Pattern**: Asserting what "the literature" / "scholars" / "existing research" does, assumes, treats, or neglects — without identifying which literature.

**Reviewer reaction**: "Which literature? Where? This is a characterisation of a field, not a finding."

**Prescription**:
- Add 2–4 representative anchors for the claimed pattern
- OR narrow to named theory/author: "Role identity theory assumes..." (then cite that theory's foundational source)
- OR reframe as own reading: "As this review of X argues..." (with your own SLR as the evidence base)

**Example**:
- ❌ "The literature has treated hybrid entrepreneurship as a transitional configuration."
- ✓ "The literature has predominantly treated hybrid entrepreneurship as a transitional configuration (Folta et al., 2010; Raffiee & Feng, 2014; Demetry, 2017)."

---

### R2 — Empirical-Trend
**Pattern**: Claims about trends, prevalence, scale, or frequency without sourcing — especially "growing", "increasing", "widely", statistics as rhetorical decoration.

**Reviewer reaction**: "How do you know it's growing? This reads like impression, not finding."

**Prescription**:
- Add primary empirical source (survey, dataset, review article that documents the trend)
- OR hedge: "consistent with evidence of growth in..." + cite
- OR remove the scale claim and keep the theoretical point, which doesn't require it

**High-risk variants**: Percentage figures without source, "approximately X%" from informal sources, cross-national trend claims from single-country data.

---

### R3 — Strong-Generalization
**Pattern**: Using high-register adjectives ("structural", "systemic", "modal", "normative", "constitutive") as factual descriptors rather than as argued positions.

**Reviewer reaction**: "Is this established or is this your claim? If established — show me. If your claim — mark it."

**Prescription**:
- If established: add the theoretical source that names the mechanism ("structural" in Folta et al.'s sense, etc.)
- If argued: mark as thesis position — "This thesis argues the heterogeneity is structurally generated..."
- Never let a strong adjective float as unanchored description

---

### R4 — Absolute-Gap
**Pattern**: Claiming no prior research exists ("no study has", "none have operationalised", "the field has not yet"). Absolute claims require absolute evidence.

**Reviewer reaction**: "Have you checked? Really? This is an invitation to find a counterexample."

**Prescription**:
- If supported by systematic review: use your own SLR chapter as the evidence base ("As the review in Chapter 3 demonstrates, no study in the corpus...")
- If not fully supported: hedge to qualified absence ("Within the reviewed literature, no study was identified that...")
- Better still: reframe as design-logic, which needs no frequency claim ("A single-method design cannot, by construction, observe both dimensions simultaneously")

**Critical**: Absolute gap claims are where reviewers most often reject desk-review submissions. Either fully ground them or eliminate them.

---

### R5 — Superlative
**Pattern**: Ranking claims ("most widely used", "the dominant framework", "the largest body of work", "most influential") stated as fact.

**Reviewer reaction**: "How do you establish dominance? Citation counts? Review articles? Your reading?"

**Prescription**:
- Add the source that establishes the ranking (a prior review, a citation analysis, a field-mapping study)
- OR hedge: "among the most..." / "one of the most frequently deployed..."
- OR remove the ranking and simply describe what the framework does

---

### R6 — Causal-Inference from Anecdote
**Pattern**: Using journalistic examples, single cases, or informal sources as evidence for structural/systemic causation.

**Reviewer reaction**: "You've shown an instance, not a mechanism. The structural claim needs structural evidence."

**Prescription**:
- Use journalistic examples *only* as illustrations, not as evidence
- Add academic sources for the structural claim proper
- Signal the distinction explicitly: "This pattern — illustrated by cases such as X — is documented more systematically by..."
- OR reframe as own thesis: "This thesis argues that heterogeneity is structurally generated by..." (then the example is illustration, not proof)

---

### R7 — Methodological-Absolutism
**Pattern**: Meta-claims about what "the field" predominantly does methodologically ("predominantly single-method", "no study has used", "the field has neglected") without systematic evidence.

**Reviewer reaction**: "This is a quantitative claim about the literature's composition. Where's your evidence?"

**Prescription**:
- If supported by a systematic review (your own or published): cite it explicitly
- If not: replace frequency claim with design-logic argument — "A single-method design cannot simultaneously observe both dimensions — not because none have tried, but because the observational logic requires separate instruments"
- Design-logic arguments are almost always stronger than frequency claims, and they require no count

---

### R8 — Theoretical-Orphan
**Pattern**: A theoretical construct, concept, or mechanism is used as though it were established fact — but its originating source is not cited. The concept appears without intellectual parentage.

**Common examples**:
- "Identity salience determines behavior" — without citing Stryker (1980) or Burke & Stets
- "Institutional logics shape individual action" — without citing Friedland & Alford or Thornton et al.
- "Sensemaking is retrospective" — without citing Weick
- "Boundary work maintains professional identity" — without citing Lamont & Molnár or domain-specific anchor

**Reviewer reaction**: "Where does this come from? Is this your claim or an established concept? If established — cite the source. If your own — argue it."

**Why this is distinct from R1**: R1 is about asserting what *the literature as a whole* does. R8 is about using a specific theoretical construct as though it needs no introduction. R1 is a field-level claim; R8 is a concept-level omission.

**Prescription**:
- Add the founding source for the construct (the original theorist, not a secondary use)
- If multiple competing definitions exist: name which version you're using and cite that specific source
- If you're using the construct in a novel way: signal it — "Following Stryker's (1980) formulation, but extended here to..."
- Never use a construct that has a traceable theoretical origin as if it were common sense

---

## Audit Protocol

### Mode A: Full Chapter Audit
For a complete chapter or draft:

1. Run Quick-Screen — flag all trigger strings
2. For each flagged sentence: assign risk type (R1–R7)
3. Output: Citation Audit Table (see format below)
4. Prioritise: HIGH-RISK items (R4 Absolute-gap and R1 Literature-claim in the Introduction) block submission. Others are negotiable.

### Mode B: Pre-Submission Spot-Check
For a near-final manuscript:
1. Run Quick-Screen only
2. For each hit: assign risk level (RED = must fix before submission, AMBER = reviewers may ask, GREEN = defensible as-is)
3. Output: prioritised fix list, ordered by risk

### Mode C: Inline Filter (during writing)
When writing or reviewing individual paragraphs:
1. For each claim in the paragraph: classify by type
2. Flag RED items immediately with prescription
3. Do not interrupt flow for GREEN items

---

## Output Format: Citation Audit Table

For each flagged item:

| # | Location | Sentence Fragment | Risk Type | Risk Level | Prescription |
|---|----------|-------------------|-----------|------------|--------------|
| 1 | 1.1 Para 3 | "treated in the literature as…" | R1 | 🔴 HIGH | Add 2–3 canonical sources establishing this characterisation |
| 2 | 1.1 Para 5 | "institutional acceptance … no longer expected" | R2+R3 | 🔴 HIGH | Hedge or cite persistent-hybridity empirics |
| 3 | 2.3 Para 1 | "three structural dimensions identified across the literature" | R1 | 🟡 MEDIUM | Add 2–4 representative anchors |
| 4 | 3.1 Para 2 | "identity salience operates as a hierarchy" | R8 | 🟡 MEDIUM | Cite Stryker (1980) or Burke & Stets as founding source |

**Risk levels:**
- 🔴 HIGH: Desk-reject or first-round rejection risk. Fix before submission.
- 🟡 MEDIUM: Reviewer comment likely. Fix in revision or pre-emptively.
- 🟢 LOW: Defensible as-is, but worth monitoring.

---

## Using Your Own Text as Evidence

When a manuscript contains its own systematic review, analysis, or empirical chapters, these are valid evidentiary sources — often stronger than external citations for specific claims:

- R4 (Absolute-gap): "As the systematic review in Chapter X demonstrates, no study in the corpus..." is methodologically more defensible than an unanchored claim
- R7 (Methodological-absolutism): Your own literature analysis can ground frequency claims
- R1 (Literature-claim): Your own theoretical development chapter can anchor field characterisations

This applies to dissertations but also to journal articles with their own data: empirical findings from your own study can ground claims in Discussion and Conclusion sections that would otherwise need external citation.

---

## Relationship to Ecosystem

| Skill | What it checks |
|-------|---------------|
| **argument-architecture** | Are claim–data–warrant present *structurally*? (Toulmin, macro-level) |
| **research-examiner Phase 0.1** | Are existing citations *accurate*? (micro fidelity) |
| **citation-risk-auditor** (this skill) | Are citations *present* where needed? (sentence-level absence audit, all sections) |
| **anti-ai-writing** | Are there AI-pattern tells in the prose? |
| **theory-section-architect** | Is the theoretical logic sound? — use before citation audit to ensure constructs are properly introduced |

Recommended sequence: theory-section-architect → academic-writing → **citation-risk-auditor** → anti-ai-writing → research-examiner → submission.

---

This skill targets under-citation. But over-citation is also a problem:
- Every claim does not need three citations
- Signposting never needs citations
- One strong primary source beats three weak ones
- Citation chains ("X argues Y, which is supported by Z, as noted by W") signal insecurity, not rigour

The goal is not maximum citations — it is *defensible* claims.
