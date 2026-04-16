---
name: evidence-discipline
description: "Enforces epistemic honesty when analysis meets audience. The core problem: smart analysis framed in a way that invites attack rather than building trust. Applies whenever output carries consequences — someone acts on it, funds it, cites it, or decides based on it. Covers evidence hierarchy, causal language discipline, confound transparency, scope discipline, and the separation of evidence from interpretation from recommendation. Not domain-specific: applies equally to policy documents, academic papers, consulting deliverables, funding proposals, investor decks, board papers, or any context where the gap between what the data shows and what the document claims creates risk. Trigger on: 'belastbar', 'haelt das', 'evidence check', 'wuerde ein Reviewer/Gutachter/Entscheider das kaufen', 'ist das ueberzeugend', 'Entscheidungsvorlage', 'policy brief', 'executive summary', or whenever a document moves from exploration to commitment — from 'interesting' to 'someone acts on this'."
---

# Evidence Discipline

Enforces epistemic honesty when analysis meets audience. The problem it solves: smart analysis presented in a way that invites attack rather than building trust. Applies whenever the gap between what the data shows and what the document claims creates risk — in policy, academia, consulting, funding, or any context where someone acts on the output.

## When Active

**ALWAYS** on empirical claims in academic work — not just when explicitly triggered. Like anti-ai-writing runs on all prose and data-integrity-guard runs on all numbers, evidence-discipline runs on all claims that reference data, designs, or measurements. This includes: propositions, research questions, contribution statements, abstracts, discussion sections, and any sentence that connects a finding to a conclusion.

Also active whenever the output carries consequences in non-academic contexts. The test: Would someone spend money, change policy, allocate resources, submit for review, or cite this as evidence? If yes, this skill is active. That includes academic papers (reviewers are decision-makers about publication), consulting deliverables (clients act on them), policy briefs (politicians decide based on them), funding proposals (money follows), and investor decks (capital follows).

## The Seven Rules

### 1. Frame Before You Write

Before producing any deliverable, answer three questions:
- What does the data SHOW? (Evidenz)
- What does it SUGGEST? (Interpretation)
- What FOLLOWS for action? (Empfehlung)

These three must be visually and linguistically separated in the document. Never blend them. A reader must be able to identify which sentences are data, which are inference, and which are recommendation.

### 2. Evidence Hierarchy

Label every finding:

| Level | Criteria | Language allowed |
|---|---|---|
| **Robust** | Large n, significant test, replicated across subgroups | "Die Daten zeigen" |
| **Plausibel** | Significant test but small effect, or single subgroup | "Die Daten legen nahe" |
| **Explorativ** | Small n, no significance test, pattern-level | "Ein explorativer Befund deutet an" |
| **Anekdotisch** | Individual cases, comments, n<10 | "Einzelne Befragte berichten" |

Robust and plausible findings belong in the main text. Exploratory findings belong in an appendix or a clearly marked box. Anecdotal evidence belongs in footnotes or illustrative sidebars — never as standalone findings.

Never present findings at different evidence levels on the same argumentative plane.

### 3. Causal Language Discipline

Cross-sectional data gets associative language. Always.

| FORBIDDEN | ALLOWED |
|---|---|
| X treibt Y | X korreliert mit Y |
| X kompensiert Y | Bei niedrigem Y zeigen Befragte mit hohem X vergleichbare Werte |
| Erfahrung bewegt/konvertiert | Nach der Erfahrung berichten Befragte hoehere Werte |
| Adoption laeuft ueber X | Adoptionsintention haengt mit X zusammen |
| X schlaegt Y | X erklaert mehr Varianz als Y |

Causal claims require: experimental design, randomization, or longitudinal pre-post measurement. If none of these exist, the language must reflect that. No exceptions for readability.

Add at least once per document: "Das Querschnittsdesign erlaubt keine kausalen Schlussfolgerungen. Alle berichteten Zusammenhaenge sind Assoziationen."

### 4. Confound Transparency

When comparing groups that differ on multiple dimensions simultaneously (e.g., digital vs. paper voters who also differ on district, school type, supervision context, timing), state the confounds explicitly at EVERY comparison — not just once in a methods section.

Template: "Die Gruppen unterscheiden sich gleichzeitig nach [Konfunder 1], [Konfunder 2] und [Konfunder 3]. Ein reiner [Effektname] laesst sich nicht isolieren."

### 5. The "Not Yet" Column

Every recommendation section must include three categories:
- **Jetzt handlungsreif:** Directly supported by robust evidence, low risk, reversible
- **Als Pilot testen:** Plausible evidence, needs further validation
- **Noch nicht entscheidungsreif:** Exploratory evidence, open questions, requires further research

The third column creates more credibility than the first. A document that says "we don't know X yet" is more trustworthy than one that claims to know everything.

### 6. Audience Epistemology

| Audience | What they need | What destroys trust |
|---|---|---|
| Decision-maker (executive, board, minister) | 3-5 clear findings, limits stated, decision table | Overselling, causal language without design, advocacy tone |
| Expert advisor / funder | Full evidence, methods visible, alternatives discussed | Hidden limitations, cherry-picked results |
| Academic peer / reviewer | Theory, method, contribution, hedged claims | Unhedged claims, missing lit, overclaiming |
| Public / media | Story, relevance, honesty | Jargon, hedging everything into unreadability |

Write for the actual reader, not for yourself. A policy brief reads differently from a journal paper reads differently from a pitch deck — not because the evidence is different, but because the frame is different. The evidence hierarchy stays the same; the presentation changes.

### 7. The Killer Number Check

Before finalizing: identify the ONE number that, if misframed, would destroy the document's credibility. There is always one. In the Whitepaper case it was "74% = funktioniert" (actually: survey completion, not voting success). Find it. Fix it. The enemy is not wrong numbers — it's correct numbers with wrong frames.

## Anti-Patterns

| Anti-Pattern | Example | Fix |
|---|---|---|
| **Advocacy framing** | "X funktioniert" based on proxy measure | Name what was actually measured: "Survey completion rate under remote conditions" |
| **Causal inflation** | "X kompensiert Y" from cross-sectional data | "Bei niedrigem Y zeigen Befragte mit hohem X vergleichbare Werte" |
| **Flat evidence** | n=7 subgroup alongside N=260 significance test | Label evidence level, move small-n to appendix |
| **Missing limits** | "Vier Typen" without noting clustering is exploratory | "Explorative Cluster-Analyse (k=4, nicht extern validiert)" |
| **Scope creep** | Pilot → "die Zukunft von X" | "Was ein Pilot fuer [spezifischen Kontext] belastbar zeigt" |
| **Suppression betas** | "X reduces Y (β=-.11)" when predictors correlate r>.60 | "Negative Koeffizienten bei Multikollinearitaet inhaltlich nicht interpretierbar" |

## Process

1. **Draft freely** — get the analysis and intuitions down without self-censoring
2. **Label evidence** — go through every claim and assign robust/plausibel/explorativ/anekdotisch
3. **Kill causal language** — search for "treibt", "kompensiert", "konvertiert", "schlaegt", "bewegt"
4. **Add confounds** — at every group comparison, state what else differs
5. **Build decision table** — handlungsreif / Pilot / nicht entscheidungsreif
6. **Find the killer number** — the one that, if challenged, sinks everything
7. **Cut 30%** — if it feels too short, it's probably right

## Academic Module: Claim-Design Alignment

When the output is an academic paper, six additional checks apply before any draft leaves the desk.

### Pre-Check: Prior Work Search Before Gap Claims

Before writing ANY gap claim ("no study has," "the literature lacks," "no review has synthesized"), run a scoping search. A gap claim is the paper's foundation — if a single prior work fills it, the paper collapses. The search does not need to be exhaustive at the draft stage, but the claim must be marked [TODO: verify via systematic search] until confirmed. This applies to academic papers, SLR introductions, and any document that justifies its existence through absence.

### Pre-Check: Scope Narrowing as Strength, Not Weakness

When a study's design (sample, method, measurement) is narrower than the initial framing suggests, the fix is almost always: narrow the claim to match the design, then reframe the narrowness as analytical depth. "Theoretically strategic subsample" is stronger than "all X." "Post-use acceptance" is more honest than "adoption." "Framework development with illustrative coding" is more defensible than "systematic review." The narrower version is harder to attack because it promises only what it delivers.

### Pre-Check: Constructs That Serve Different Psychological Functions

If two constructs serve different psychological functions (e.g., trust = confidence vs. verification = distrust mitigation), they should not be on the same measurement scale. When a scale fails to achieve reliability, ask: is this a measurement problem, or are the items tapping two different functions that don't belong together? PLT (auditability + understanding) failed because it mixed transparency-demand with trust. This check applies whenever a construct "doesn't work" — the first hypothesis should be functional heterogeneity, not bad items.

### Pre-Check: Effect Size over Significance

Statistical significance alone says nothing about substantive importance. When reporting quantitative findings: always report effect sizes (r, R², Cohen's d, eta²) alongside p-values. A "significant" r=.14 is substantively near zero. A non-significant r=.25 in a small sample may be the real finding. For qualitative work: distinguish between themes that are FREQUENT and themes that are CONSEQUENTIAL — frequency is not importance.

### Pre-Check: Theory-Advancing Questions in Conclusions

Conclusions must end with SPECIFIC theoretical questions, not generic "future research should examine X in other contexts." Bad: "Future research should study digital voting in other populations." Good: "Does the legitimation feedback loop between social categorisation and role centrality operate differently when hybrid entrepreneurs lack digital visibility — and if so, does this reveal a boundary condition of the perception-performance framework or a limitation of the observation method?" The question should identify a concrete mechanism, condition, or interaction that remains untested.

### Check 1: Outcome Label
What does the dependent variable actually measure? "Adoption" requires a pre-use decision under uncertainty. If respondents were assigned to the system and surveyed after use, the outcome is post-use acceptance, reuse intention, or continued use intention — not adoption. Always ask: Did participants CHOOSE to use the system? If no, the label must reflect that.

### Check 2: RQ-Proposition Alignment
Do the propositions actually permit the claim made in the research question? If the RQ asks "beyond X independently" but every proposition still contains X, there is a misalignment. The RQ must match the narrowest claim the propositions support, not the broadest.

### Check 3: Construct Label vs. Measurement
Does the theoretical name match the operationalization? If items measure "concrete, tangible, real, immediate," that is experiential realness — not Construal Level Theory (which requires experimental manipulation of psychological distance). Wrong labels load a literature the instrument cannot service. A reviewer who knows the parent theory will catch this immediately.

### Check 4: Framework Picture ≠ Framework Test
A layered diagram in Figure 1 is not a test of the layering. If the analysis (e.g., fsQCA) treats all conditions as parallel inputs, the architecture stays in the picture but not in the test. Either demonstrate the layers analytically (e.g., compare coverage of trust-only vs. trust+social vs. trust+social+experiential solutions) or scale back the architectural claim.

### Check 5: Discriminant Validity Threshold
If two constructs correlate above r=.80, the claim that they are separate constructs is attackable. Options: (a) reframe as facets of a joint construct ("system trust with procedural and technological facets"), (b) run robustness check with combined score, (c) report both models and let the data decide. Never ignore high inter-construct correlations.

### Check 6: Theory Proportionality
An "organizing lens" or "sensitizing framework" is defensible with light theoretical infrastructure. A "grand theory" with four analytically distinct levels requires testing all four levels. If one level (e.g., procedural transparency) cannot be measured reliably, the framework has a gap. Either reduce the framework to what is measured or acknowledge the gap as a limitation — not a future-research afterthought.

### Academic Anti-Patterns

| Anti-Pattern | Example | Fix |
|---|---|---|
| **Outcome inflation** | "Adoption" for post-use acceptance | Name what was measured: post-use acceptance |
| **Label borrowing** | "Construal Level" for experiential realness items | Name matches measurement, not aspiration |
| **RQ-Prop gap** | RQ says "beyond trust" but all Props include trust | Narrow the RQ or broaden the Props |
| **Picture-only architecture** | Layered figure, flat analysis | Show layers analytically or call it a heuristic |
| **Discriminant blindness** | r=.85 between "separate" constructs | Merge or robustness-check |
| **Theory overreach** | STS as grand theory with untested levels | "Organizing lens" / "sensitizing framework" |
| **Missing benchmark** | fsQCA alone without variance-model comparison | Add OLS/PLS-SEM benchmark: "variance model says X, configurational model shows Y" |

## Integration with Other Skills

This skill layers on top of:
- **consulting-strategic-analysis** — evidence-discipline constrains the output
- **schneider-deutsch** — Schneider handles style, evidence-discipline handles epistemic honesty
- **anti-ai-writing** — anti-AI handles word-level tells, evidence-discipline handles claim-level tells
- **data-integrity-guard** — data-integrity checks numbers, evidence-discipline checks framing
- **non-sycophant** — non-sycophant prevents tone-level agreement, evidence-discipline prevents claim-level agreement
- **research-examiner** — research-examiner runs pre-submission, evidence-discipline runs DURING writing

## Known Failure Modes (Session 2026-03-24)

These are cases where this skill SHOULD have fired but DIDN'T. Each one is now a trigger.

| Failure | What happened | What should have been caught |
|---|---|---|
| 74% as "funktioniert" | Survey completion framed as voting success | Killer Number Check (Rule 7) |
| "Adoption" for assigned post-use | Outcome label didn't match design | Academic Check 1 (Outcome Label) |
| "Beyond trust independently" | RQ claimed what Props didn't support | Academic Check 2 (RQ-Prop Alignment) |
| "Construal Level" for experiential items | Construct label loaded wrong literature | Academic Check 3 (Label vs. Measurement) |
| Layer figure without layer test | Architecture in picture but flat in analysis | Academic Check 4 (Picture ≠ Test) |
| TR-TT r=.85 as "three pillars" | High correlation ignored | Academic Check 5 (Discriminant Validity) |
| STS as grand theory | Four-level framework with one level unmeasured | Academic Check 6 (Theory Proportionality) |

When any of these patterns recur, this skill should fire immediately — not wait for external critique.

| PhD "all hybrids" for specific subgroup | Outcome inflation (Academic Check 1) — same pattern as ICIS |
| Blockchain SLR percentages on n=12 | Flat evidence — small purposive sample presented as field prevalence |
| Blockchain SLR "umbrella review" for narrative positioning | Label borrowing — methodological label not earned |
| Blockchain SLR necessity = reviewer judgment as empirics | Advocacy framing — own interpretation in empirical register |

**Transfer rule:** When a pattern is caught in Project A, immediately scan ALL open projects for the same pattern. Learnings are epistemological, not project-specific.

Sprache folgt dem Input (Deutsch / English).
