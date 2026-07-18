# PRISMA Flow Tracker

| Stage | Scite (pass 1) | WoS | Scopus | EBSCO | Snowball | Manual | Total |
|---|---|---|---|---|---|---|---|
| Records identified | ~230 (13 strings) | — | — | — | — | 21 | ~251 |
| After deduplication | ~150 | | | | | 21 | |
| Title/abstract screened | 63 retained | | | | | 21 | 84 |
| Excluded (N1–N4) | non-EN, book-chapters, off-topic (protein moonlighting etc.) removed inline | | | | | | |
| Full-text assessed | pending | | | | | pending | |
| Excluded (C1–C4, reasons tallied below) | | | | | | | |
| **Included (title-stage A)** | 60 | | | | | 21 | **81** |
| B-pile (needs 2nd read) | 3 (D56,D62,D63) | | | | | | 3 |

**Note:** Scite pass 1 = 13 keyword strings run 2026-07-18 covering all six context cells + transitional supplement. This is one database of three; WoS/Scopus/EBSCO still required for a defensible PRISMA count. Scite figures are approximate (relevance-ranked, no dedup export).

## Full-text exclusion tally
| Criterion | Count |
|---|---|
| C1 (not individual identity) | |
| C2 (context not codable) | |
| C3 (identity not theorized) | |
| C4 (intention-focal) | |


## Update — saturated multi-database sweep (2026-07-18)
| Metric | Value |
|---|---|
| Coded rows total | 223 |
| In-sample (A or B, problem-coded) | 218 |
| Clear include (A) | 153 |
| Uncertain (B, full-text needed) | 65 |
| Databases | Scite + Consensus + Scholar Gateway |
| Search agents | 6 parallel (platform, corporate, family, transitional, academic, cross-theory) |
| Cross-agent DOI duplicates removed at merge | tracked via merge.py dedup |

Cell sizes (in-sample): independent 91, family 37, platform 33, academic 25, social 14, corporate 11, other 4, multiple 2.
Still pending: WoS/Scopus/EBSCO exports (institutional access) for a formal PRISMA identified->screened->included count; full-text adjudication of 65 B-papers.
