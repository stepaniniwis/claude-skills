---
name: anti-ai-design
description: >
  Visual counterpart to anti-ai-writing. Prevents the generic "AI look" in any UI, HTML page, artifact, dashboard, slide, landing page, or figure by forcing a DESIGN.md (Google Labs format) before the first line of CSS: one specific real-world reference object instead of adjectives, a small token set, prose rationale, and intentional Do's and Don'ts. Then builds strictly against it and audits the result for AI-design tells (purple-blue gradients, glassmorphism, rounded-2xl cards with soft shadows, emoji headers, 3-card feature grids, Inter everywhere). Trigger on: "design", "UI", "layout", "landing page", "dashboard", "artifact", "HTML", "styling", "looks too AI", "zu sehr KI", "sieht generisch aus", "DESIGN.md", "design system", or any request that produces something visual.
---

# Anti-AI Design

Generic AI design comes from the same mechanism as generic AI prose. Without a specific anchor, a model renders the statistical center of "modern, clean, premium": the average of every SaaS landing page in its training data. The fix is the same as for writing. Commit to something specific before producing anything.

This skill uses the [DESIGN.md format](https://github.com/google-labs-code/design.md) (Google Labs, Apache-2.0, alpha) as the commitment device. Full spec: `references/design-md-spec.md`. Rationale: `references/design-md-philosophy.md`.

---

## The Core Principle

> Adjectives describe a region. A specific reference describes a point. (DESIGN.md Philosophy)

"Modern, clean, trustworthy" gets you the centroid. "A 1970s graduate seminar handout, one ink, generous margins, serif at reading size" gets you a design, and the negative constraints come with it automatically: a handout does not glow.

**Prose carries the design. Tokens are only reference values.** A DESIGN.md with 50 Material color tokens and no point of view is still generic. Several of Google's own examples show this failure.

---

## Workflow

### Step 1: Find or write the DESIGN.md

- If the project has a `DESIGN.md`, read it fully and treat it as binding. Do not "improve" it silently.
- If none exists, **write one before any markup**. Show it to the user and get agreement when the task is substantial.

### Step 2: Choose the reference object (the decisive step)

Name a **concrete artifact from the physical or historical world** with a known audience and purpose. Not a style label.

| Generic (reject) | Specific (accept) |
|:--|:--|
| "Modern minimalist dashboard" | "The quarterly statistical bulletin of a central bank, printed, two columns, one accent ink" |
| "Clean academic website" | "A university press monograph's front matter: half-title, generous leading, small caps for running heads" |
| "Professional consulting deck" | "A partner's hand-annotated board memo: dense, numbered exhibits, source lines under every chart" |
| "Friendly civic voting app" | "A municipal ballot and its official explanatory leaflet: plain, numbered, legally neutral, one colour for emphasis" |

Test: could two different designers read the reference and land in roughly the same place? If not, it is still an adjective.

### Step 3: Write the file

Follow the spec's section order: Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts. Constraints that keep it non-generic:

- **Colors:** 3–6 tokens. Name each by its material role ("Paper", "Ink", "Vermilion"), and state in prose where it may and may not appear. One accent, used scarcely. No pure `#FFFFFF` page or pure `#000000` text unless the reference demands it.
- **Typography:** 1–2 families, chosen *because of the reference* (a broadsheet suggests a news serif, a lab report a grotesk plus mono). Modest scale ratios. Write down which weights are forbidden.
- **Shapes and Elevation:** Decide explicitly. "Zero radius, no shadows, hairline rules" is a valid and often better answer than a radius scale.
- **Do's and Don'ts:** 6–12 intentional lines specific to this reference. A long rambling list signals that the reference is too vague.
- Extra sections (Motion, Iconography, Data Visualisation) are allowed and encouraged where relevant.

Minimal skeleton:

````md
---
version: alpha
name: <Reference-derived name>
colors:
  paper: "#F4F0E4"
  ink: "#1E1A14"
  accent: "#C3402A"
  rule: "#B8B0A2"
typography:
  body:
    fontFamily: Source Serif 4
    fontSize: 17px
    lineHeight: 1.55
  label:
    fontFamily: IBM Plex Mono
    fontSize: 12px
    letterSpacing: 0.04em
rounded:
  none: 0px
spacing:
  unit: 8px
---

## Overview
<One paragraph naming the reference object, its audience, and its job.>

## Colors
- **Paper** {colors.paper}: …where it is used, where never.

## Do's and Don'ts
- **Don't** …
- **Do** …
````

### Step 4: Validate

If `npx` is available:

```bash
npx @google/design.md lint DESIGN.md          # broken refs, WCAG contrast, section order
npx @google/design.md export --format css-tailwind DESIGN.md > theme.css   # optional
```

Fix every `error` and every `contrast-ratio` warning. Treat `orphaned-tokens` as a hint that the palette is too large.

### Step 5: Build strictly against it

Define CSS custom properties from the tokens and use only those. Any value not in the DESIGN.md is a decision. Either add it to the file with a reason, or do not use it.

### Step 6: Audit for AI-design tells

Run this list against the output. Each hit needs removal or a written justification grounded in the reference.

**Colour**
1. Purple-to-blue or pink-to-orange gradients, especially on text or hero backgrounds
2. Neon accent on near-black "dark mode by default"
3. Every element tinted with the brand colour; no true neutral
4. Rainbow category colours with no semantic logic

**Surface and shape**
5. Glassmorphism, backdrop blur, frosted cards
6. `rounded-2xl` plus soft drop shadow on every container
7. Cards inside cards inside cards
8. Glow, blob, or grain-noise backgrounds with no relation to the content

**Layout**
9. Centred hero with big gradient headline, subline, and two buttons
10. Three equal feature cards with icon + title + two lines
11. KPI tile row with huge numbers and tiny labels, even when the numbers are not the point
12. Identical vertical rhythm everywhere; no section is denser or looser than another
13. Everything centred

**Typography and decoration**
14. Inter, Geist, or Space Grotesk chosen by default rather than by reason
15. Emoji or a line icon in front of every heading
16. Pill badges ("✨ New", "Beta") as decoration
17. Eyebrow labels in small caps above every heading
18. Bounce, fade-up-on-scroll, or hover-lift animations on static content

**Content**
19. Placeholder-perfect copy ("Empower your workflow")
20. Decorative charts or illustrations that encode no data

---

## Relation to Other Skills

- **anti-ai-writing**: same logic for prose. Run both on any artifact with text.
- **non-sycophant**: if the user's own brief is generic ("make it modern"), say so and propose a specific reference instead of complying with the centroid.
- **dataviz / academic figures**: the DESIGN.md colour and type tokens are the palette source. Data colours still follow the dataviz rules for contrast and semantics.

## Source and Licence

The DESIGN.md format, spec, and philosophy are by Google Labs (`google-labs-code/design.md`, commit `9bf8eae`), licensed Apache-2.0. Copies in `references/` are unmodified; see `references/LICENSE-design-md`. Workflow, reference-object test, and AI-tell audit in this file are original to this skill.
