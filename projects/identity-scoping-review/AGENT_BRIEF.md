# Search-Agent Brief — Identity-in-Entrepreneurship Scoping Review

You are building the sample for a scoping review testing whether "entrepreneurial identity" (EI) is a coherent construct or an umbrella term. Your job: search your assigned slice to **saturation**, screen against criteria, and return coded CSV rows.

## Tools
Use `mcp__Scite__search_literature`, `mcp__Consensus__search`, and `mcp__Scholar_Gateway__semanticSearch`. Run MULTIPLE query formulations for your slice (by construct, by theory, by population, by outcome) until new queries stop surfacing new includable papers — that is saturation. Run at least 5-8 distinct queries. Batch at most 3 Consensus calls at once (rate limits); if you hit a rate-limit error, switch to Scite/Scholar Gateway.

## Inclusion criteria (screen every hit)
- English, peer-reviewed journal article (or landmark book chapter), 2009–2026, empirical or conceptual.
- **C1**: identity of the *entrepreneuring individual* is a focal construct (NOT organizational/venture/brand identity — exclude those).
- **C3**: identity is theorized, not a passing variable.
- **C4**: intention studies only if identity (not intention) is focal.
- Exclude pure teaching cases, practitioner pieces, non-English, conference abstracts (mark as B if borderline).

## Deduplicate
Do NOT return any paper whose DOI is in the existing-DOI list provided in your task. Check each hit's DOI against it.

## Coding — return ONE CSV row per included paper, columns in THIS exact order:
`id,authors,year,journal,doi,ajg_rank,found_via,theory_code,theory_secondary,context_locus,context_role_structure,context_geography,context_sample,focal_construct,problem_code,problem_secondary,key_finding,mechanism,design,data_source,analysis,outcome_valence,screening_decision,memo`

- `id`: use the prefix assigned in your task + a number (e.g. F01, F02...).
- `found_via`: `database-scite` / `database-consensus` / `database-scholar` as appropriate.
- `theory_code` (primary; secondary optional): `SIT` (social identity/self-categorization) · `RIT` (role identity, Stryker/Burke) · `NARR` (narrative identity) · `POSS` (possible selves) · `IDWORK` (identity work, Sveningsson/Alvesson) · `IMPR` (impression mgmt/legitimacy signaling) · `CONFLICT` (identity conflict) · `FIT` (Fauchart-Gruber founder identity types) · `OTHER`. Leave blank only if truly undeterminable from abstract.
- `context_locus`: `independent` / `academic` / `corporate` / `family` / `platform` / `social` / `multiple` / `other`.
- `context_role_structure`: `exclusive` (full-time sole role) / `hybrid` (dual role e.g. employed+venturing, academic+commercial, parent+venture) / `transitional` (entry/exit/failure/re-entry).
- `problem_code` — the focal identity PROBLEM the paper's RQ/contribution addresses (ONE primary; secondary optional):
  - `ACTION` — how identity guides entrepreneurial action/strategy (category membership itself unproblematic)
  - `HIERARCHY` — which of multiple coexisting roles is primary
  - `PROTOTYPE` — is there a clear category/prototype to identify with at all
  - `VALUES` — does the venture align with the person's values / non-work identities
  - `AUDIENCE` — how identity is performed/signaled to evaluating audiences (incl. algorithms)
  - `PERSISTENCE` — does an (old) identity survive a role transition
  - `OTHER` — none fit (add a memo)
- `outcome_valence` (for RQ3, if determinable from abstract): `S` succeeds/stabilizes · `F` fails/destabilizes · `C` conditional/mixed · blank if unclear.
- `key_finding`: 1 sentence, findings not methods. `mechanism`: what-causes-what-under-what-condition if stated.
- `ajg_rank`: your best estimate of ABS/AJG rank (4*/4/3/2/1) or blank.
- `screening_decision`: `A` clear include · `B` uncertain (say why in memo).
- Quote NOTHING you didn't retrieve. If a field is unknown, leave it blank. Commas inside a field: wrap the field in double quotes.

## Return format
Return ONLY the CSV rows (no header, no prose, no code fences). If you found nothing new, return the single line: `NONE`. Then, on a final line after a `---` separator, give a one-sentence saturation note (how many queries you ran, whether new hits had tailed off).
