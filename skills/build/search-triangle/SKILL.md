---
name: search-triangle
description: >
  Plans, executes, and audits academic literature searches with the "Search Triangle" (Gusenbauer & Haddaway, 2021): goals, heuristics, and systems must match. Classifies every search as lookup, exploratory, or systematic, then prescribes the fitting heuristics (building blocks, snowballing, pearl growing, most specific first, successive fraction, post-query filtering, handsearching, wayfinding) and search systems, and flags mismatches such as cherry-picking via lookup, skipped scoping, or Google Scholar / semantic or AI search tools used as stand-alone sources for systematic reviews. Three modes: PLAN (before searching), RUN (during searching with Elicit, Consensus, Scite, Scholar Gateway, OpenAlex), AUDIT (search sections of reviews, methods sections, or a colleague's "I googled it"). Trigger on: "literature search", "search strategy", "Suchstrategie", "Recherche planen", "search string", "Boolean", "which database", "welche Datenbank", "Google Scholar enough?", "scoping", "snowballing", "is my search systematic", "PRISMA-S", "find papers on", or before any literature-review-architect sample-selection phase.
---

# Search Triangle

Searching is a trained skill, not a by-product of internet use. Most researchers use the system they know, in the way they are used to, for every kind of search. The result is biased, intransparent, and irreproducible evidence bases (Gusenbauer & Haddaway, 2021).

Source: Gusenbauer, M., & Haddaway, N. R. (2021). What every researcher should know about searching – clarified concepts, search advice, and an agenda to improve finding in academia. *Research Synthesis Methods, 12*(2), 136–147. https://doi.org/10.1002/jrsm.1457 (CC BY). Companion study: Gusenbauer & Haddaway (2020), *RSM 11*(2), 181–217, https://doi.org/10.1002/jrsm.1378, which tested 28 academic search systems.

---

## The Model

```
                 GOALS  (why am I searching?)
                /     \        → lookup / exploratory / systematic
               /MATCH! \
     SYSTEMS ─────────── HEURISTICS
 (what am I searching   (how am I searching?)
  with?)
                 ↺ KNOWLEDGE: better mental models sharpen goals;
                   better skills improve use of systems and heuristics
```

Efficient and effective search only works when all three corners match. The goal decides the search type. The search type constrains the heuristics. Heuristics and type together decide which systems qualify. No heuristic belongs exclusively to one type; the same heuristic (e.g., snowballing) is run with different rigour depending on the type.

---

## The Three Search Types

| | **Lookup** | **Exploratory** | **Systematic** |
|:--|:--|:--|:--|
| **Goal** | Find one or a few known items fast; goal and path are clear | Learn a concept or body of research; goal is fuzzy and sharpens iteratively | Identify *all* relevant records on a scoped topic, unbiased, transparent, reproducible |
| **Use cases** | Fact retrieval, verification, re-finding, question answering | Discovery, keeping up to date, narrative reviews, **scoping** before a systematic review, "negative searches" (spotting gaps) | Systematic reviews, meta-analyses, systematic maps, bibliometric analyses |
| **Dominant heuristics** | Straightforward search, navigation, most specific first | Wayfinding, most specific first, snowballing / pearl growing, post-query filtering | Building blocks (Boolean), snowballing / pearl growing, handsearching, successive fraction, post-query filtering |
| **System requirements** | Simple interface, high coverage, good interpretation of intent | Low latency, many navigation options (query, browse, filter), many cues; best-match systems favoured | Exact-match, transparent, reproducible (same query → same results), supports complex Boolean, full export of results |
| **Typical failure** | **Cherry-picking**: first fitting result treated as representative, or post-hoc support for a decision already made | Mistaken for "the literature search" of a paper; no stop rule; no record of paths taken | **Skipped scoping**: jumping into Boolean strings while key terms are still unclear; non-reproducible systems; undocumented final string |

Key relations:
- A systematic search is *preceded* by an exploratory scoping phase. That phase is where the hermeneutic circle happens. The systematic search itself is not a learning process: it is predefined, protocol-driven, and only the final string iteration needs full documentation.
- Lookup and systematic both have a known goal; they differ in rigour of planning and reporting and in the scope of the search area.
- Search sessions often mix types. Name the type of each episode, not just of the session.

---

## Heuristics Glossary

- **Most specific first**: start with the most specific concept, broaden only if needed.
- **Wayfinding**: learning by moving through a field with little prior knowledge; following cues.
- **Snowballing / citation chasing / pearl growing**: from known relevant records, follow references (backward) and citing works (forward); extract new terms from "pearls".
- **Building blocks**: split the question into concepts, collect synonyms per block, combine with OR within and AND between blocks.
- **Successive fraction**: shrink a result set step by step via exclusion lists (NOT).
- **Post-query filtering**: restrict by metadata (year, document type, field) after querying.
- **Handsearching**: manual screening of key journals, proceedings, or reference lists.

---

## Systems: Two Families

- **Comprehensive-transparent** (e.g., Web of Science, Scopus, PubMed, ProQuest, EBSCO databases): detailed query control, Boolean, reproducible. Required for systematic searching.
- **Efficient-slick** (e.g., Google Scholar, Semantic Scholar): fast, intuitive, opaque relevance ranking. Very good for lookup, weak for systematic searching. In the 2020 study, roughly half of the 28 systems were recommendable as stand-alone systems for systematic searching, and none of the semantic systems tested met the requirements. Google Scholar fails on transparency and reproducibility.

Two warnings from the paper:
1. **Platform ≠ database.** Web of Science is a platform; Science Citation Index Expanded is a database. Report the database, not just the platform.
2. **Efficiency can erode exploration.** Systems that turn exploratory search into lookup through pre-selected cues push users toward quick, unconsciously biased lookup. For questions that need a balanced information diet, keep the search exploratory.

**Extension (not from the paper; apply the paper's logic):** AI research assistants (Elicit, Consensus, Scite Assistant, Scholar Gateway, ChatGPT/Claude search) are efficient-slick systems with opaque retrieval and ranking, and their results may vary between runs. Use them for lookup and exploratory work, scoping, and pearl finding. Never use them as the stand-alone or reported source of a systematic search. Run the final string in comprehensive-transparent databases.

---

## Mode 1: PLAN (before searching)

Work through the triangle explicitly and output a short plan:

1. **Goal.** What must this search achieve? Which claim or decision will rest on it? Classify it as lookup, exploratory, or systematic. If the user calls it "systematic" but cannot yet name the core concepts and synonyms, reclassify it as exploratory scoping first.
2. **Knowledge state.** What does the user already know (key terms, seminal papers, adjacent fields with different vocabulary)? Gaps here mean scoping is not done.
3. **Heuristics.** Pick from the table for that type. For systematic: draft building blocks (concept × synonyms), name seed papers for snowballing, define post-query filters and their justification.
4. **Systems.** Pick systems that support the type and the chosen heuristics. For systematic: at least two comprehensive-transparent databases relevant to the discipline, named at database level, plus snowballing. Note what each system *cannot* do (e.g., field searching limited to title/abstract/keywords, no full-text search, truncation rules).
5. **Stop rule and record.** Exploratory: when does it stop (saturation of new terms, time box)? Systematic: what will be documented (databases, platforms, dates, full strings, filters, results per source) following PRISMA-S.

Output format:

```
SEARCH PLAN
Goal:         <one sentence>   → Type: <lookup | exploratory | systematic>
Knowledge:    <known terms / seed papers / gaps>
Heuristics:   <list with rationale>
Systems:      <system — why — known limitations>
Stop/record:  <stop rule; documentation standard>
Mismatch risk:<the most likely triangle mismatch for this case>
```

## Mode 2: RUN (during searching)

- Label each search episode with its type.
- **Lookup:** fine to use efficient tools; but if the result will support a claim in a paper, say so and check for counter-evidence (move to exploratory).
- **Exploratory:** log new terms, authors, and journals discovered; harvest pearls for snowballing; keep a list of "negative results" (no hits = possible gap, verify before claiming).
- **Systematic:** freeze the final string, run it identically per database, record date and hit counts, export full result sets, then snowball from included records.
- When using connected tools (Elicit, Consensus, Scite, Scholar Gateway), state that they act as exploratory instruments and say which comprehensive-transparent database would be needed to make the search systematic.

## Mode 3: AUDIT (existing search or search section)

Check against these items and give each a status: OK, WEAK, or FAIL.

1. **Type declared?** Is it clear whether the search was lookup, exploratory, or systematic, and does the claim made from it match the type? ("A systematic review of…" built on Google Scholar alone = FAIL.)
2. **Scoping documented?** For systematic searches: evidence of a prior exploratory phase that fixed concepts and inclusion criteria.
3. **Heuristics fit?** Building blocks with synonyms, not a single keyword; snowballing reported; filters justified.
4. **Systems fit?** Comprehensive-transparent databases named at database level, not just platform; more than one source; limitations of each acknowledged.
5. **Reproducible?** Full strings, dates, fields searched, filters, hit counts per source (PRISMA-S).
6. **Bias exposure.** Reliance on opaque ranking (Scholar, semantic or AI tools); first-page-only screening; cherry-picking signs (only confirming studies cited for a contested claim).
7. **Narrative reviews.** These usually rely on exploratory search alone. Acceptable if declared as such; a problem if the review implies completeness.

End with the single most consequential mismatch and the concrete fix.

---

## Relation to Other Skills

- **literature-review-architect**: run PLAN before its sample-selection phase.
- **citation-risk-auditor / hallucination-audit**: claims that "no study has examined X" need a documented negative search, ideally exploratory plus systematic.
- **evidence-discipline / non-sycophant**: call out cherry-picking via lookup, including the user's own.
