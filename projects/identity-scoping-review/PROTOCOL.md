# Execution Protocol

## Is 'Entrepreneurial Identity' a Coherent Construct? A Context-Driven Scoping Review

**Status:** Design complete (see `Identity_Review_DiagnosisB.docx` on Drive). This protocol operationalizes sample selection (Phase 3) and coding (Phase 4) so the review can be executed and audited.

**Version:** 1.0 — 2026-07-18. Search-string pilots run 2026-07-18 (Scite, see `search-log.md`).

---

## 0. Review Classification (Phase 1–2 recap, fixed)

| Dimension | Decision |
|---|---|
| Archetype | Critical / problematizing review with scoping logic (mapping problems, theories, outcomes by context) |
| Analytical moves | Problematizing (primary) + Classifying (Problem × Context, Theory × Context matrices) + Configuring (RQ3 outcome comparison) |
| Focus | Domain-based (identity in entrepreneuring), with construct-level critique |
| Motivation pattern | **Incommensurability** — claims across contexts are structurally incompatible, not merely contradictory (Hiebl 2023b pattern 6) |
| Contribution type | **Construct clarification** (A-journal elevation criterion): is EI one construct, a family, or an umbrella term? |
| Well-read-scholar test | A scholar who has read Radu-Lefebvre et al. (2021), Mmbaga et al. (2020), and Wagenschwanz (2021) already knows the field is fragmented. What would surprise them: that fragmentation is *correct* — the systematic demonstration that different contexts pose different identity problems requiring different theories, i.e. that the construct itself may not cohere. |

---

## 1. Search Strategy (Phase 3a–3b)

### 1.1 Databases and approaches

| Approach | Source | Role |
|---|---|---|
| Database keyword search | Web of Science Core Collection; Scopus; EBSCO Business Source | Primary, reproducible corpus |
| Backward snowballing | Reference lists of the 5 prior reviews (IR1–IR5 in `SLR_Identity_entrepreneurship` sheet) + all included papers | Captures canon; mandatory because pilot showed Petriglieri et al. (2019) does not surface via keywords |
| Forward citation tracking | Citations of Fauchart & Gruber 2011; Hoang & Gimeno 2010; Powell & Baker 2014 (via Scite/WoS) | Captures recent context-specific work (2023–2026) |
| Expert/manual inclusion | 21 anchor papers from DiagnosisB reference list | Seed set + validation set; each manual add logged |

### 1.2 Keyword matrix

**Block A — Identity constructs** (OR-linked):
`identit*` OR `"identity work"` OR `"role identity"` OR `"social identity"` OR `"narrative identity"` OR `"possible selves"` OR `"self-concept"` OR `"identity conflict"` OR `"identity centrality"`

**Block B — Entrepreneuring forms** (OR-linked; this block is the review's methodological innovation — prior reviews searched only `entrepreneur* / founder*`):
`entrepreneur*` OR `founder*` OR `intrapreneur*` OR `"corporate entrepreneur*"` OR `"academic entrepreneur*"` OR `"hybrid entrepreneur*"` OR `mumpreneur*` OR `mompreneur*` OR `"gig econom*"` OR `"platform work*"` OR `"portfolio career"` OR `"side hustle"` OR `"self-employ*"`

**Block C — Transitional supplement** (OR-linked, run as separate string):
`"entrepreneurial exit"` OR `"ex-entrepreneur*"` OR `"venture failure"` OR `"business failure"` OR `"serial entrepreneur*"`

**Master string:** `(Block A) AND (Block B)` — title/abstract/keywords.
**Supplementary strings:** `(Block A) AND (Block C)`; plus one targeted string per underindexed context (see 1.3).

### 1.3 Pilot validation (run 2026-07-18, Scite; full hits in `search-log.md`)

| String | Anchor papers surfaced in top 10 | Verdict |
|---|---|---|
| `("entrepreneurial identity" OR "founder identity") AND ("identity work" OR "role identity" OR "social identity")` | Fauchart & Gruber 2011; Leitch & Harrison 2016 | ✅ Core works |
| `("gig economy" OR "platform work" OR "gig workers") AND ("identity work" OR "occupational identity") AND entrepreneur*` | Alacovska et al. (hit #1) | ⚠️ Works, but generic gig-economy literature dominates without the identity-work terms; Petriglieri 2019 missed → snowballing mandatory |
| `(intrapreneur* OR "corporate entrepreneur*" OR "hybrid entrepreneur*" OR "academic entrepreneur*") AND identit*` | Academic-entrepreneur identity stream well covered | ✅ Works |
| `("entrepreneurial exit" OR "ex-entrepreneur" OR "business failure") AND ("identity loss" OR "identity conflict" OR "identity transition")` | Nielsen & Gish 2023 (hit #1) | ✅ Works |

### 1.4 Time frame and rationale

**2009–2026.** Start 2009: Cardon et al. (2009) and Jain et al. (2009) mark the point where (a) EI became a measurable focal construct and (b) the first context-specific problem (academic hybrid) was documented. Earlier foundational work (e.g., Down & Reveley 2004) enters via snowballing with manual-inclusion logging. End: search date.

---

## 2. Inclusion / Exclusion Criteria (Phase 3c)

### Non-content criteria (title/abstract stage)

| # | Include | Exclude |
|---|---|---|
| N1 | English language | Other languages |
| N2 | Peer-reviewed journal articles; landmark books/chapters via manual inclusion (logged) | Conference papers, theses, editorials (except the 5 prior reviews, kept as comparison set, not sample) |
| N3 | 2009–2026 | Earlier (unless snowballed + logged) |
| N4 | Empirical and conceptual papers | Pure teaching cases, practitioner pieces |

### Content criteria (full-text stage)

| # | Include | Exclude |
|---|---|---|
| C1 | Identity of the **entrepreneuring individual** is a focal construct (IV, DV, or process focus) | Organizational identity, venture/brand identity, national identity as focal construct |
| C2 | Context (entrepreneurship form) is identifiable from the method/sample section | Context not codable (e.g., mixed samples with no breakdown) → B-pile, second read |
| C3 | Study permits coding of a focal identity **problem** (see §4.2) | Identity mentioned only as passing variable without theorization |
| C4 | Entrepreneurial intention studies only if identity (not intention) is the focal construct | Intention studies using identity as one of many antecedents |

### Quality criteria

No ranking cutoff for inclusion (a ranking cutoff would systematically exclude the newer context-specific outlets where platform/mumpreneur work appears — that exclusion would bias the review *toward* coherence). Instead: code AJG/ABDC rank per paper and report a robustness check (does the divergence pattern hold in AJG 3+ journals only?). Screen against predatory-journal lists.

### Screening process (Phase 3d)

A/B/C logic per item; solo-reviewer setup: every B decision logged with resolution rationale in `screening-log.csv` (columns: id, decision, criterion invoked, rationale, resolution date). PRISMA flow tracked in `prisma-tracker.md`: identified → deduplicated → title/abstract screened → full-text assessed → included, with exclusion reasons tallied per criterion.

---

## 3. Anchor Set (seed + validation)

The 21 references in DiagnosisB serve two roles: (1) validation set — every search iteration must surface ≥80 % of the database-indexed anchors, else keywords are refined; (2) guaranteed sample members (they pass I/E by construction). Anchor list with DOIs lives in `coding-sheet.csv` rows 1–21.

---

## 4. Coding Scheme (Phase 4)

Coding logic: **deductive** for RQ1/RQ2 (categories fixed below, from DiagnosisB), with an explicit **abductive escape valve**: papers that fit no category go to `problem_code = OTHER` / `theory_code = OTHER` with free-text memo; if ≥5 OTHER memos cluster, a new category is proposed and all previously coded papers are re-checked (constant comparison).

### 4.1 Extraction template (TCCM+, one row per paper)

| Field | Values / instructions |
|---|---|
| `id`, `authors`, `year`, `journal`, `doi` | Bibliographic |
| `ajg_rank` | AJG 2024 rank; NA if unlisted |
| `found_via` | database / backward / forward / manual |
| **T** `theory_code` | See §4.3 |
| **C** `context_locus` | independent / academic / corporate / family / platform / social / other |
| **C** `context_role_structure` | exclusive / hybrid / transitional |
| **C** `context_geography`, `context_sample` | Free text |
| **Ch** `focal_construct` | As named by authors (verbatim) |
| **Ch** `problem_code` | See §4.2 |
| **Ch** `key_finding` | 1–2 sentences, findings not methods |
| **Ch** `mechanism` | What-causes-what-under-what-conditions (Hoon 2013 causal-map input) |
| **M** `design`, `data_source`, `analysis` | e.g., qual-interview / survey / conceptual |
| `outcome_valence` | For RQ3: does the identity process succeed/stabilize (S), fail/destabilize (F), or conditional (C)? |
| `memo` | Anything not captured above; feeds abductive valve |

### 4.2 RQ1 — Focal identity problem codes (deductive, from DiagnosisB Table 2)

Decision rule: code the problem the paper's **research question and contribution** address — not every problem mentioned. One primary code; secondary code allowed if the design explicitly addresses two.

| Code | Definition | Indicator questions | Anchor exemplar |
|---|---|---|---|
| `ACTION` | How does identity guide entrepreneurial action/strategy? | Is identity the IV explaining behavior? Is category membership itself unproblematic? | Powell & Baker 2014 |
| `HIERARCHY` | Which of multiple roles is primary? | Does the paper theorize ordering/priority of coexisting roles? | Jain et al. 2009 |
| `PROTOTYPE` | Is there a clear category/prototype to identify with at all? | Does the paper problematize the availability or clarity of the 'entrepreneur' category? | Starmann et al. 2025 |
| `VALUES` | Does the venture serve/align with the person's values or non-work identities? | Is alignment between venture and a prior identity (motherhood, faith, family) the puzzle? | Phillips et al. 2025 |
| `AUDIENCE` | How is identity performed/signaled to evaluating audiences (incl. algorithms)? | Is the audience (investors, platforms, customers) the theoretical driver? | Alacovska et al. 2025; Navis & Glynn 2011 |
| `PERSISTENCE` | Does an (old) identity survive a role transition? | Is entry/exit/failure the setting and identity continuity the puzzle? | Nielsen & Gish 2023 |
| `OTHER` | None of the above | Mandatory memo | — |

### 4.3 RQ2 — Theory codes (summative)

`SIT` (social identity/self-categorization) · `RIT` (role identity/identity theory, Stryker/McCall) · `NARR` (narrative identity) · `POSS` (possible selves) · `IDWORK` (identity work, Sveningsson/Alvesson tradition) · `IMPR` (impression management/legitimacy signaling) · `CONFLICT` (identity conflict/interference) · `FIT` (founder identity types, Fauchart & Gruber tradition) · `OTHER` (memo). Multiple codes allowed; mark primary. Keyword markers for summative pass: theory named in framing section + ≥1 core citation of the tradition.

### 4.4 RQ3 — Comparative case procedure

1. After coding, group papers by `focal_construct` similarity (same or near-synonymous construct).
2. Retain groups spanning ≥2 distinct `context_locus × context_role_structure` cells.
3. Within each group, compare `outcome_valence` + `mechanism` across contexts.
4. Classify: **convergent** (same outcome/mechanism), **moderated** (same mechanism, different strength), **divergent** (different mechanism or opposite outcome).
5. The three DiagnosisB pairs (Jain↔Starmann; Petriglieri↔Alacovska; Bousfiha↔Nielsen) are hypotheses to be confirmed, not results — the procedure must also search for *convergent* pairs (confirmation-bias guard).

### 4.5 RQ4 — Synthesis decision rules (pre-registered, to prevent post-hoc fitting)

| Conclusion | Pattern required |
|---|---|
| A — Coherent construct, context as moderator | ≥1 problem code appears as primary in ≥5 of 6 context cells AND ≥50 % of RQ3 groups convergent/moderated |
| B — Family of constructs | Problem codes partially overlap across cells (adjacent-cell overlap, no universal problem) AND RQ3 mixed |
| C — Umbrella term | No problem code primary in >2 cells AND majority of RQ3 groups divergent |

Thresholds are working values (v1.0); any revision is logged with rationale *before* synthesis begins.

---

## 5. Workplan

| Step | Task | Output | Est. effort |
|---|---|---|---|
| 1 | Run master + supplementary strings on WoS/Scopus/EBSCO, export | Raw corpus (~1,500–2,500 est.) | 1 day |
| 2 | Deduplicate; title/abstract screening (A/B/C) | Screened set (~250–400 est.) | 3–4 days |
| 3 | Full-text screening + B-pile resolution | Final sample (~120–180 est.) | 3–4 days |
| 4 | Backward/forward snowballing on final sample | +20–40 papers | 2 days |
| 5 | Code all papers per §4 | Filled coding sheet | 8–10 days |
| 6 | RQ1/RQ2 matrices; RQ3 comparative groups; RQ4 synthesis | Results section input | 4–5 days |
| 7 | Write-up (→ `literature-review-writer` skill; PGP-style intro) | Manuscript draft | — |

**Relation to PhD:** The Corporate × Hybrid and Family × Hybrid cells and the `HIERARCHY`/`PROTOTYPE` problem codes map directly onto the thesis question (hybrid entrepreneurs' career identity via RIT/SIT). The coding sheet doubles as the thesis lit-review evidence base; RQ4 outcome B or C would itself motivate the thesis's context-specific design.
