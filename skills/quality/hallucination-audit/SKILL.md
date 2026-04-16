---
name: hallucination-audit
description: >
  Systematic back-check for hallucinated content in academically co-written texts.
  Activate BEFORE any academic paper draft is submitted, shared with supervisors,
  or cited. Three risk tiers with distinct verification protocols.
  Trigger phrases: "ready to submit", "check before I send", "ist das alles korrekt",
  "back-check", "verify against data", "halluziniert?", or whenever a paper
  was co-written with Claude and contains methods details, theory attributions,
  or qualitative claims.
---

# Hallucination Audit Skill

## Core Principle

Claude produces coherent, plausible text — not necessarily accurate text.
The risk is not random error. It is *calibrated plausibility*: numbers that look
right, citations that sound real, methodological details that fit the genre.
These are harder to catch than obvious errors because they do not trigger doubt.

Academic co-writing with Claude has three distinct hallucination risk tiers.
Each requires a different verification protocol.

---

## Risk Tier 1: LOW — Quantitative Data from Structured Source

**What:** Correlations, means, SDs, p-values, effect sizes, sample sizes,
field dates — when drawn from a documented analysis summary in the session.

**Risk:** Low. Claude reads numbers from structured summaries and reproduces
them. Rounding occurs (r = .296 → "r = .30") but is transparent.

**Protocol:**
- Spot-check 3–5 numbers against the original dataset or analysis output
- Flag rounding: always report the precise value in the paper, not the rounded version
- Verify that n-values in subgroup analyses match actual subgroup sizes

---

## Risk Tier 2: HIGH — Qualitative Methodology Details

**What:** Intercoder agreement percentages, coder count, specific procedural
steps in the analysis process, saturation claims, sampling justifications.

**Why high risk:** These details are expected by reviewers, follow genre
conventions, and sound methodologically normal. Claude produces them by
pattern-matching to "what a rigorous methods section looks like" — not from
actual documentation of what happened.

**Known hallucination patterns:**
- Intercoder reliability figures (e.g., "78% initial agreement") — invented
- Third coder / member-checking claims — invented if not documented
- Specific software versions for qualitative analysis — often invented
- Precise sample selection criteria phrasing — may not match actual procedure

**Protocol:**
1. For every methodological claim: ask "Do I have a document that says this?"
2. If no document exists: either generate the evidence (run the intercoder
   check, document the process) or reframe as reflexive description
3. Braun & Clarke (2006) qualitative standard: replace reliability statistics
   with explicit reflexivity account — this is methodologically defensible
   and removes the hallucination risk entirely

---

## Risk Tier 3: VERY HIGH — Theory Attributions with Specific Claims

**What:** Citations of specific concepts, distinctions, or arguments to named
theorists, especially when the attribution is precise (e.g., "X distinguishes
between A and B").

**Why very high risk:** Claude has absorbed vast secondary literature.
It knows theory names and roughly what they are associated with. It does NOT
reliably know which specific distinction appears in which specific work.
The error pattern: plausible name + real concept + wrong source.

**Known example from this session:**
- Attributed "trust as delegation vs. testimony" to Origgi (2017) — WRONG
- Correct source: Hardwig (1991, *The Role of Trust in Knowledge*, Journal of Philosophy)
- Origgi (2017) works on reputation and epistemic trust but not this specific distinction

**Protocol:**
1. For every theory attribution: verify the source independently before submission
2. High-risk attributions: any claim of the form "X distinguishes between A and B"
   or "X argues that..." with a specific page-level claim
3. Safe attributions: well-known frameworks cited for their general approach
   (e.g., "Braun & Clarke (2006) thematic analysis") — these are stable
4. If source cannot be verified: use the concept without the attribution,
   or attribute to a secondary source you have actually read

**Verified alternatives for common hallucination-prone citations:**
- Epistemic delegation / trust in experts → Hardwig (1991)
- Epistemic injustice / testimonial credibility → Fricker (2007)
- Technology trust delegation → Blind (2006) [verified in this session's data]
- Saturation → Moore, Aguinis & Darden (2026) [per saturation-auditor skill]

---

## Risk Tier 4: MODERATE — Qualitative Quotes

**What:** Verbatim quotes attributed to specific respondent codes
(e.g., "CD51", "P07").

**Risk:** Claude produces quotes that are thematically accurate but
may not match the exact wording in the raw data.

**Protocol:**
1. Every quote used in a paper must be verified against the raw data file
   before submission — no exceptions
2. Code numbers (CD51, CD28) must exist in the actual dataset
3. If raw data is not accessible at the time of writing: mark all quotes
   as [TO VERIFY] and do not submit until checked
4. One hour of verification work protects against the most serious
   form of academic integrity failure

---

## Pre-Submission Checklist

Run this before every submission, supervisor review, or public presentation
of co-written academic text:

### Quantitative claims
- [ ] All correlations verified against analysis output
- [ ] All n-values match actual (sub)group sizes
- [ ] Rounded values reported precisely in final text

### Methods section
- [ ] Every procedural claim has a source document
- [ ] Intercoder reliability: either verified figure or replaced with reflexivity
- [ ] No phantom coders, reviewers, or quality-check steps

### Theory section
- [ ] Every "X argues that..." attribution independently verified
- [ ] Specific conceptual distinctions traced to actual source text
- [ ] Origgi / other reputation-adjacent citations flagged for verification

### Qualitative quotes
- [ ] Every verbatim quote checked against raw data file
- [ ] Respondent codes confirmed to exist in dataset
- [ ] Wording matches source, not just meaning

---

## Integration with Other Skills

This skill runs as a **mandatory final-pass audit** after:
- `academic-writing` — before any draft leaves the session
- `qualitative-method-auditor` — before methods section is finalised
- `research-examiner` — as the first step, before examiner-level critique
- `literature-review-architect` — before citation lists are submitted

**Sequence:**
1. Co-write with Claude (academic-writing, theory-section-architect, etc.)
2. Run hallucination-audit before sharing with anyone
3. Then run research-examiner for contribution-level critique

The hallucination audit precedes the quality critique.
A paper with invented methodological details fails before it is evaluated
for theoretical contribution.

---

## The Underlying Epistemology

Claude optimises for textual coherence within genre conventions.
A methods section that reads like a rigorous methods section is the output
target — regardless of whether the described procedures occurred.

This is not deception. It is pattern completion. But in academic writing,
pattern completion without empirical grounding is fabrication.

The researcher's job in co-writing is to hold the boundary between
"this sounds right" and "this is documented."
Claude cannot hold that boundary. Only you can.
