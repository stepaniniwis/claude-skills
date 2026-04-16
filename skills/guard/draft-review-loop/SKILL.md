---
name: draft-review-loop
description: "Automated self-critique loop for substantial deliverables. Draft-Agent produces output, Review-Agent attacks it against explicit checklists, Draft-Agent fixes blockers, User receives reviewed output + critique report. Solves the version-sprawl problem: one reviewed version replaces five unreviewed ones. Trigger AUTOMATICALLY on any substantial deliverable — paper sections, whitepapers, policy briefs, proposals, executive summaries, theory sections, contribution claims. Also trigger on: 'schreib mir', 'draft this', 'erstell', 'build v[N]', or any request that will produce a document someone acts on. Do NOT trigger on quick answers, file edits, data analysis, or exploratory work."
---

# Draft-Review Loop

Automated self-critique before delivery. The pattern: produce → attack → fix → present with transparency.

## Why This Exists

Session 2026-03-24 produced 14 paper versions and 5 whitepaper versions. Every critical problem (74% misframed, adoption vs. post-use acceptance, overclaimed RQs, wrong construct labels) was caught by external critique — not by Claude. The knowledge to catch these existed. The workflow to apply it didn't.

This skill closes the loop.

## When Active

On every deliverable where someone will act on the output: submit it, fund it, cite it, decide based on it, or send it to co-authors. The test: If a hostile expert read this, would they find something I should have caught myself? If plausible → run the loop.

Do NOT run on: quick answers, data lookups, file organization, brainstorming, or explicitly exploratory work where the user said "just draft freely."

## The Loop

### Step 1: Draft

Produce the deliverable as requested. Write freely. Follow the user's direction. Don't self-censor during drafting — that kills the good ideas alongside the bad ones.

### Step 2: Review (Subagent — FRESH CONTEXT)

Spawn a Review-Agent as a **fresh-context agent**. This means: the agent gets ONLY the draft + the checklists + study design context. It does NOT get the conversation history, the reasoning behind design decisions, or the user's stated goals. This removes self-bias — the review agent judges the text as a stranger would, not as someone who watched it being built.

The fresh-context principle matters because: when you build something over multiple iterations, you develop justifications for every choice. A reviewer who shared that journey will unconsciously defend those choices. A reviewer who sees only the output will find the weaknesses that the builder's context made invisible.

Spawn with this exact prompt structure:

```
You are a hostile but fair reviewer. You have NEVER seen this paper before. You know NOTHING about why decisions were made. Your job is to find the sharpest attack vectors in this draft. You are measured by whether you find the weaknesses — not by whether the draft looks good.

Apply these checklists IN ORDER:

CHECKLIST A: Evidence Discipline (7 rules)
1. Is evidence separated from interpretation separated from recommendation?
2. Does every finding carry an evidence level (robust/plausible/exploratory/anecdotal)?
3. Is causal language proportional to the design? (Cross-sectional → associative only)
4. Are confounds stated at every group comparison?
5. Is there a "not yet / open questions" section?
6. Is the audience-appropriate frame applied?
7. KILLER NUMBER CHECK: Which single number, if misframed, destroys credibility?

CHECKLIST B: Claim-Design Alignment (6 checks)
1. OUTCOME LABEL: Does the DV name match what was actually measured?
2. RQ-PROPOSITION ALIGNMENT: Do the propositions actually permit the RQ's claim?
3. CONSTRUCT LABEL: Does every theoretical name match its operationalization?
4. FRAMEWORK PICTURE ≠ TEST: Is every framework element analytically tested or acknowledged as heuristic?
5. DISCRIMINANT VALIDITY: Are "separate" constructs actually separable (r<.80)?
6. THEORY PROPORTIONALITY: Is the theoretical claim proportional to the empirical test?

CHECKLIST C: Non-Sycophant /destroy
1. STEEL-MAN: What is the strongest version of the argument?
2. BEST ATTACK: What would a hostile reviewer say that would actually hurt?
3. CLAIM SYCOPHANCY: Where did the draft build the claim the user wants rather than the claim the data supports?

CHECKLIST D: Revision Execution Quality (6 checks)
1. LEAD CASE: For each finding — is the participant with the most extreme/clear manifestation the lead case? If not, why not?
2. THEORETICAL DEPTH: For each finding — is there a canonical theory explaining WHY this pattern exists (not just describing WHAT)? Missing mechanism = missing generalizability.
3. DATA EXPLOITATION: Are all data sources doing analytical work? Prescreener, metadata, extreme cases, contradictory cases — each should have a named role beyond "sampling" or "context."
4. DROP-IN FORMAT: Are revision suggestions delivered as finished text blocks with explicit placement ("Insert after X, replacing Y")? Ambiguous suggestions = integration confusion.
5. CITATION DENSITY: Does every factual statement have a reference? Does every theoretical claim cite a source or explicitly mark itself as the paper's own argument ("we argue", "the evidence suggests")? Scan every paragraph — if a sentence reads like a fact and has no citation, it is an attack surface. Papers that were READ but UNDERUSED are the biggest gap source.
6. NEGATIVE FRAMING: Does the draft say what something IS NOT instead of what it IS? "This is not X" plants X in the reader's mind. Every negation should be replaced with a positive assertion. "This is not a gap" → "This is a structural zone." "This is not confusion" → "This variation is structural."

For each finding, classify severity:
- BLOCKER: Must fix before delivery. Would cause rejection, loss of credibility, or factual error.
- WARNING: Should fix. Weakens the argument but doesn't sink it.
- NOTE: Worth knowing. Could improve but isn't critical.

Return a structured critique report.
```

The Review-Agent gets: the draft + the checklists + context about the study design (sample, method, measurement).

### Step 3: Fix

Read the Critique Report. Fix all BLOCKERs. For WARNINGs: fix what can be fixed quickly, note the rest. NOTEs are optional.

**After fixing: ask "Is this the BEST version or just the error-free one?"** If the text has been through 3+ patch rounds, a clean rewrite of the affected section is almost always better than another incremental edit. Patching accumulates scar tissue. The review loop catches problems — but it does not produce the best prose. If the answer is "error-free but not great," rewrite from scratch with the final positioning in mind.

### Step 3b: Reference Gap Check

After fixing blockers, scan for claims that lack theoretical grounding. The review agent catches unearned claims — but it does not suggest missing references. Proactively ask: "Where does this argument need a citation I haven't provided?" Suggest candidate references even if they require [VERIFY] markers. A claim without a reference is weaker than a claim with a candidate reference that needs checking.

### Step 4: Present

Deliver to the user:
1. The fixed draft
2. The Critique Report (full)
3. A summary line: "X blockers fixed, Y warnings remain: [list]"

The user sees what was caught AND what remains open. Transparency is the point.

## Implementation with Claude Code Subagents

```python
# Pseudocode for the loop

# Step 1: Main agent writes draft
draft = write_draft(user_request)

# Step 2: Spawn review agent
review = Agent(
    prompt=REVIEW_PROMPT + draft + study_context,
    subagent_type="general-purpose",
    description="Review draft against evidence-discipline checklists"
)
critique = review.result

# Step 3: Parse and fix
blockers = [f for f in critique if f.severity == "BLOCKER"]
warnings = [f for f in critique if f.severity == "WARNING"]
fixed_draft = fix_blockers(draft, blockers)

# Step 4: Present
present(fixed_draft, critique, f"{len(blockers)} blockers fixed, {len(warnings)} warnings remain")
```

In practice with Claude Code's Agent tool:
- Main agent drafts the deliverable
- Main agent spawns a background Agent with the review prompt
- When the review agent completes, main agent reads the critique
- Main agent fixes blockers and presents the result

## Calibration

The review is only as good as the checklists. When a new failure mode is discovered (the user or an external reviewer catches something the loop missed), add it to:
1. The relevant checklist (A, B, or C)
2. The Known Failure Modes table in evidence-discipline
3. This skill's "Failure History" section below

## Failure History

**2026-03-24, Session 1:**
- PhD Transition Document v7: Claim-Design mismatch (broad title/RQ for narrow sample) was NOT caught by the loop — because the loop was never run on the PhD. The ICIS and Whitepaper versions of the same error had been caught and fixed, but the learning was not transferred to the PhD. **Root cause: transfer failure. Learnings stayed project-specific instead of being applied cross-project.**
- Blockchain SLR v1: Three blockers (percentages as field claims, "umbrella review" label, necessity-as-empirics) were caught by the review agent. **The loop worked here.** But the PhD failure shows the loop must be triggered on ALL open documents, not just the one currently being drafted.

**Transfer rule added to the loop:** After fixing blockers in Project A, scan all other open projects for the same pattern before moving on.

## When to Skip the Loop

- User explicitly says "just draft, don't review" or "exploratory"
- Quick edits to existing files (< 200 words changed)
- Data analysis, calculations, file management
- Brainstorming, Zettel creation, note-taking
- When the user is iterating rapidly and wants speed over scrutiny (they'll say so)

The loop adds ~2-3 minutes per deliverable. For a paper section that would otherwise spawn 5 versions, that's a net time save.

## Integration

This skill orchestrates:
- **evidence-discipline** (Checklist A)
- **non-sycophant** (Checklist C)
- **claim-design-alignment** from feedback memory (Checklist B)
- **data-integrity-guard** (numbers in the draft)
- **anti-ai-writing** (prose quality)

It does not replace these skills — it ensures they are actually executed on every substantial output, not just when someone remembers to invoke them.

Sprache folgt dem Input (Deutsch / English).
