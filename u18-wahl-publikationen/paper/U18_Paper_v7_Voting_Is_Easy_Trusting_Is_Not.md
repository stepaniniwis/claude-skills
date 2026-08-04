# Voting Is Easy, Trusting Is Not: Acceptance and Trust After a Real Digital Election

*Manuscript v7 (04.08.2026), based on EJIS Draft 2 (18.07.2026). Target: EJIS; fallbacks JIT, GIQ (see submission package). Changes v6→v7: canonical numbers throughout (N = 383); MGCFA invariance and trust-differentiation finding; realness double coding (κ = .90); cluster-robust and wild-bootstrap inference; reference conflict resolved (Abdala et al. 2025, PRQ, and Romanov et al. 2025, GIQ, are two distinct studies, both now cited); Table 1 completed (PLT_Compr = PLT1 + PLT_5; group alphas .62/.62, computed and reproduced against the official total of .62); ethics/data-protection statement integrated.*

*Author-only placeholders remaining: ethics approval number; funding code; author list and ORCID (title page); repository link; realness dossier sign-off (5 checkboxes); GenAI disclosure finalization; word count at upload.*

---

**Abstract.** Digital voting pilots rest on a policy assumption: once citizens experience online voting, trust will follow. We examine this assumption in the first digitally conducted U18 election in Bavaria, Germany, where adolescents in ten municipalities cast a real ballot online while peers elsewhere voted on paper. We compare 259 digital voters surveyed immediately after voting with 124 paper voters who assessed digital voting hypothetically (N = 383). Acceptance constructs differ strongly between the groups (block contrast +0.77 SD); trust constructs differ far less (+0.24 SD). The gap between these contrasts is our central estimate: as a within-person difference it cancels person- and municipality-level confounding, and it survives person-clustered inference, municipality-clustered inference, and a wild cluster bootstrap (all p ≤ .001). Multigroup CFA adds a twist: voters who only imagined digital voting did not distinguish trust in the technology from trust in elections at all (latent r = 1.00); experienced voters did. Prior attitude outweighs all trust and fit predictors in explaining intention. Experience, we conclude, produces users before it produces trusting citizens; the trust problem of digital democracy sits in institutional embedding rather than in the interface.

**Keywords:** digital voting; e-government; trust; technology acceptance; quasi-experiment; measurement invariance

## 1. Introduction

In February 2026, 2,981 adolescents in ten Bavarian municipalities did something no minor in the state had done before: they cast a ballot in a real election over the internet. The election was the U18 municipal election, a civic-education election organized by the Bavarian Youth Council in parallel to the official municipal elections, with more than 30,000 votes cast statewide at roughly 350 paper polling stations. For many participants it was the first democratic act of their lives. About one in five digital voters used the individual verification feature to check that their vote had been recorded. And yet, in the open comment field of our post-vote survey, one of them wrote: "wählen würde sich mit Blatt Papier viel realer anfühlen" (voting would feel much more real with a sheet of paper).

That tension is the subject of this paper. Governments that pilot digital voting typically justify the investment with a learning argument: exposure creates familiarity, familiarity creates trust, and trust carries adoption. The argument treats trust as a downstream product of use. Information systems research offers surprisingly little direct evidence for it. The e-voting literature is dominated by hypothetical acceptance studies, in which respondents evaluate a system they have never touched, and by cross-sectional studies of the long-running Estonian case, where internet voting has been ordinary for two decades (Ehin et al., 2022) and the formative moment of first contact is unobservable. Recent work has begun to unpack whether trust in government or trust in technology drives internet voting (Abdala et al., 2025; Romanov et al., 2025), but the core comparison the policy argument needs, namely experienced versus imagined digital voting in the same real election, has been missing.

The U18 election gave us that comparison, with limits we state plainly. Ten municipalities voted digitally; the rest of Bavaria voted on paper. Assignment was not random, and voters selected themselves into participation and into our survey. We therefore do not frame the group comparison as a causal effect of experience. Our central test does not need that framing. We compare, within each respondent, how strongly the digital-paper contrast shows up in acceptance constructs versus trust constructs. Any confound that shifts acceptance and trust alike, including self-selection, enthusiasm, demand effects, and municipality context, cancels in this difference. What survives is the asymmetry itself.

The asymmetry is large. Acceptance constructs (behavioral intention, performance expectancy, social influence, hedonic motivation) differ between the experienced and the hypothetical group by +0.77 standard deviations after covariate adjustment. Trust constructs differ by +0.24. The interaction is stable under person-clustered inference, municipality-clustered inference with a wild cluster bootstrap, and false-discovery-rate correction. Within trust, the difference concentrates on generalized and institutional trust rather than trust in the technology, though measurement analyses counsel caution at the facet level: a multigroup CFA shows that respondents who merely imagined digital voting did not empirically separate technology trust from general election trust in the first place. Verifiability, the cryptographic community's central trust mechanism, was used by a fifth of digital voters, but our data cannot link verification behavior to individual trust, and we treat it descriptively. Prior attitude toward digital voting, measured as a covariate, explains more variance in intention than all trust and fit constructs combined.

We draw one conclusion for theory and one for practice. Theoretically, experience and trust operate on different timescales: a single real usage episode moves evaluations of the tool while barely moving evaluations of the arrangement behind the tool, and it is the experience itself that first differentiates the trust construct into facets. Practically, pilots that aim at trust should not expect usability to deliver it; the mechanisms that plausibly move trust are institutional, not ergonomic. Experience produces users before it produces trusting citizens.

## 2. Theoretical Background

### 2.1 Trust and adoption in digital government

Trust has been the workhorse construct of e-government adoption research since Carter and Bélanger (2005) showed that citizens' intention to use government services online depends jointly on trust in the internet and trust in government. Two decades of successor studies have refined the object of trust: citizens can trust (or distrust) the technology, the institution operating it, and the surrounding process, and these objects need not move together. Elections sharpen the distinction. Avgerou (2013) argued from the Brazilian e-voting case that trust in IT-mediated elections is not primarily produced by the artifact but by the institutional arrangement in which the artifact is embedded; Brazilian voters trusted electronic voting because they trusted the electoral authority, not because they understood the machines. Field evidence from India points the same way: experiences of electoral malpractice shape whether voters read technology as a safeguard or as a new attack surface (Sandeep & Ravishankar, 2018). The Estonian evidence converges from the quantitative side: institutional trust outweighs technological trust in predicting both trust in internet voting and its actual use (Romanov et al., 2025), while trust in the technology matters most for the narrower choice of channel among those already willing to vote (Abdala et al., 2025).

For digital voting specifically, this institutional reading collides with an engineering reading. The cryptographic literature locates trustworthiness in verifiability (Chaum, 2004; Ryan et al., 2015): if every voter can check that her ballot was recorded as cast, trust becomes unnecessary, or so the argument goes. German constitutional doctrine adds a third reading: the Federal Constitutional Court's voting-computer judgment (BVerfGE 123, 39) requires that the essential steps of an election be checkable by the public without special expertise, which makes lay comprehensibility, not cryptographic verifiability, the benchmark. The three readings make different predictions about what a first real usage episode should change. If trust is ergonomic, experience should raise it. If trust is verificationist, experience plus verification should raise it. If trust is institutional, experience should raise evaluations of the tool and leave trust roughly where the institution left it.

### 2.2 Experience versus imagination

Attitude research has long held that attitudes formed through direct experience are stronger, more accessible, and more predictive of behavior than attitudes formed through description (Regan & Fazio, 1977; Fazio & Zanna, 1981; Glasman & Albarracín, 2006). Applied to technology, the distinction separates pre-use acceptance, measured on an imagined system, from post-use acceptance, measured on an experienced one. The UTAUT tradition (Venkatesh et al., 2003; Venkatesh et al., 2012) supplies the standard acceptance constructs but is largely silent on what a single episode of real use does to trust, as opposed to expectancies. The digital-voting literature compounds the problem: most acceptance studies are hypothetical by necessity, because real digital elections are rare, and the rare real deployments are studied after routinization, when internet voting has become a habit rather than an event (Solvak & Vassil, 2018).

What is missing is the moment in between: the first contact. First contact is precisely where the policy argument places its bet, and precisely where evaluation modes differ most. An experienced evaluator answers "using the system was easy" from memory; a hypothetical evaluator answers "using the system would be easy" from imagination. Our design tests whether a usage episode changes everything equally. Our expectation, from the institutional reading of trust, is that it does not.

### 2.3 Hypotheses and research questions

**H1.** Voters who experienced digital voting evaluate it more favorably on acceptance constructs (behavioral intention, performance expectancy, social influence, hedonic motivation) than voters who assess it hypothetically.

**H2.** The difference between the experienced and the hypothetical group is larger for acceptance constructs than for trust constructs.

H2 carries the paper. H1 alone would be compatible with a mundane story (people who chose digital voting like digital voting). H2 is a statement about the shape of that difference, estimated within persons, and it is what the learning argument denies: if experience produced trust the way it produces acceptance, the two contrasts would be similar in size.

**RQ1 (exploratory).** Within the trust block, which facets carry the group difference: generalized trust in digital elections, institutional trust, or trust in the technology? We treat the facet pattern as exploratory here and as a confirmatory target for a follow-up study in a binding staff-council election.

**RQ2 (exploratory).** Does experienced "realness" of the voting act behave as a boundary condition of the experience-acceptance link?

## 3. Method

### 3.1 Setting

The U18 election is a Germany-wide civic-education election for minors, held in the run-up to official elections and organized in Bavaria by the Bavarian Youth Council. In February 2026, for the first time, ten municipalities and districts offered the U18 municipal election digitally as part of [research project, blinded for review]. The digital system used a municipal identity infrastructure (OpenID Connect) for eligibility, pseudonymized ballots, and an individual "recorded-as-cast" verification feature based on receipt codes. Coercion resistance and receipt-freeness were explicitly out of scope for this non-binding election. 17,850 eligible adolescents were invited by letter; 2,981 cast a digital vote (16.7%), and roughly 570 of them (19%) used the verification feature, according to system logs. Elsewhere in Bavaria the U18 election ran as usual on paper, with more than 30,000 votes at about 350 polling stations.

### 3.2 Design and identification

We fielded one questionnaire in two versions. Digital voters were surveyed online immediately after submitting their ballot; they evaluated a system they had just used, in the past tense. Paper voters were recruited via QR-code posters at analog polling stations; they evaluated digital voting hypothetically, in the subjunctive. The design is a quasi-experimental field comparison. Municipalities were not assigned at random, voters chose whether to vote and whether to answer, and the two groups differ in evaluation mode by construction: experience stands against imagination.

These features rule out a causal reading of any single group contrast, and we do not offer one. H1 results are reported as adjusted descriptive contrasts. Identification of H2 rests on a different logic. For each respondent we observe both an acceptance evaluation and a trust evaluation. The H2 estimate is the difference of the two group contrasts, which is a within-person comparison: whatever makes a self-selected digital voter more enthusiastic in general (motivation, tech affinity, the glow of having just voted, the wish to please the researchers) inflates her acceptance answers and her trust answers alike, and drops out of the difference. What does not drop out are confounds that act on one block only. We discuss the plausible candidates in Section 5.3 and probe them with a composite that excludes the most desirability-prone construct. The analysis plan for the results reported here was documented internally before the analyses were run, but after data collection; it is an internal analysis plan, not a preregistration.

### 3.3 Sample

Of 511 questionnaire starts, 506 remained after removing five test cases. The scale-complete dataset contained 390 respondents (266 digital, 124 paper). Requiring complete data on all 14 scales and the three covariates left the analysis sample of N = 383 (259 digital, 124 paper); Figure 1 shows the flow. Respondents were 14 to 17 years old. Dropout analyses showed no substantively relevant differences on intention and trust scores. Sensitivity is bounded: with n = 259 versus 124 and covariate adjustment, the minimal detectable effect at 80% power is d ≈ .27 to .31. Null results below that band are uninformative, a point we return to when interpreting facet-level trust contrasts.

[Abbildung 1 hier: Fig1_flow.png]

### 3.4 Measures

The questionnaire comprised 74 closed items (five-point Likert scales) and one open comment field, administered in German. Fifty-six items measured 15 constructs; 14 were retained as scales (Table 1). The acceptance block adapted UTAUT2 constructs to the voting context; the trust block distinguished generalized trust in digital elections, institutional trust, and technology trust, following the facet logic of the Estonian trust literature. Effort expectancy items were administered but not scaled. FC and CDV fall below conventional reliability thresholds; we report their contrasts for completeness and mark them exploratory. Covariates were school type, self-rated technology competence, and prior attitude toward digital voting.

**Table 1. Constructs and reliabilities by group.**

| Construct | Items | α total | α digital | α paper |
|---|---|---|---|---|
| Behavioral intention (BI) | 3 | .80 | .72 | .84 |
| Performance expectancy (PE) | 3 | .82 | .75 | .81 |
| Social influence (SI) | 3 | .84 | .76 | .83 |
| Hedonic motivation (HM) | 3 | .79 | .69 | .80 |
| Institutional trust (IT) | 3 | .83 | .84 | .78 |
| Technology trust (TT) | 5 | .86 | .86 | .87 |
| Generalized trust (TR) | 2 | .76 | .79 | .64 |
| Civic duty (CDV)† | 3 | .52 | .54 | .31 |
| Civic competence (CVC) | 3 | .78 | .70 | .83 |
| Democratic significance (PDS) | 6 | .88 | .87 | .90 |
| Perceived realness (PRR) | 5 | .66 | .64 | .68 |
| Platform comprehension (PLT_Compr)‡ | 2 | .62 | .62 | .62 |
| Categorical legitimacy (CL) | 5 | .90 | .89 | .92 |
| Facilitating conditions (FC)† | 2 | .48 | .11 | .64 |

† Below reliability threshold; exploratory. ‡ PLT_Compr comprises items PLT1 and PLT_5 (comprehension of how the digital vote works and of what happens to the ballot after submission); the two-item Spearman-Brown coefficient reproduces the reported total (.62) and is stable across groups. [Itemquellen-Spalte aus Item-Pool ergänzen.]

Because the two groups answered in different modes, we tested measurement invariance with multigroup CFA (lavaan, MLR, FIML) over the seven acceptance and trust constructs (22 items; Table 3). Configural fit was acceptable. Metric invariance held (Δχ²(15) = 20.6, p = .150). Full scalar invariance was rejected (Δχ²(15) = 43.2, p < .001); freeing two intercepts flagged by a DIF screen (BI2, TT4) yielded partial scalar invariance by the ΔCFI criterion (ΔCFI = −.003; Chen, 2007; Cheung & Rensvold, 2002), with the likelihood-ratio test remaining marginally significant (p = .028). We therefore base conclusions on block-level contrasts, report facet-level contrasts with DIF sensitivity checks, and disclose one further group difference in Section 4.4.

### 3.5 Analysis

For each of the 14 constructs we estimated an ANCOVA-type regression of the z-standardized scale score on voting modality plus the three covariates, with HC3 robust standard errors, and corrected the 14 modality p-values with the Benjamini-Hochberg procedure (Benjamini & Hochberg, 1995). Bootstrap confidence intervals (1,000 replicates) accompany the seven core constructs. H2 was tested in a long-format model of block means (383 persons × 2 blocks) with a modality-by-block interaction; because the 766 observations come from 383 persons, we report person-clustered standard errors as primary inference. Because assignment varied at municipality level and the survey lacks a municipality identifier, we additionally assigned digital respondents to the nearest pilot municipality by IP-based geolocation (within 25 km; unassignable cases as singletons; paper respondents by geographic cells), yielding 76 clusters, and computed cluster-robust and wild cluster bootstrap inference (Rademacher weights, null imposed, 4,999 replicates; Cameron et al., 2008). We flag the geolocation assignment as a proxy. Relative importance was assessed with hierarchical regressions and permutation-based importance (5,000 permutations). Analyses used Python (statsmodels) and R (lavaan); scripts and seeds at [Repository].

## 4. Results

### 4.1 Group contrasts across constructs (H1)

Table 2 reports all 14 adjusted contrasts; Figure 2 displays them. The four acceptance constructs show the largest differences (BI +0.71, PE +0.70, SI +0.82, HM +0.81, all q < .0001; model R² .33 to .40). Trust constructs differ far less: TR +0.29 (q = .003), IT +0.27 (q = .016), TT +0.18 (q = .090, not significant after correction). Among the remaining constructs, civic duty, civic competence, facilitating conditions, and perceived democratic significance show positive contrasts (the first three with reliability caveats), while platform comprehension, perceived realness, and categorical legitimacy do not differ. H1 is supported as a descriptive pattern.

**Table 2. Adjusted digital-paper contrasts (ANCOVA, HC3, BH-corrected).**

| Construct | Block | b (z) | SE | p | q (BH, 14) | 95% CI | Boot-CI | R² |
|---|---|---|---|---|---|---|---|---|
| SI | Acceptance | 0.82 | .098 | <.001 | <.001 | [0.63, 1.02] | [0.65, 0.99] | .38 |
| HM | Acceptance | 0.81 | .098 | <.001 | <.001 | [0.62, 1.00] | [0.63, 1.01] | .40 |
| BI | Acceptance | 0.71 | .095 | <.001 | <.001 | [0.53, 0.90] | [0.53, 0.91] | .37 |
| PE | Acceptance | 0.70 | .097 | <.001 | <.001 | [0.51, 0.89] | [0.52, 0.88] | .33 |
| TR | Trust | 0.29 | .092 | .002 | .003 | [0.11, 0.47] | [0.11, 0.47] | .32 |
| IT | Trust | 0.27 | .106 | .010 | .016 | [0.07, 0.48] | [0.08, 0.47] | .12 |
| TT | Trust | 0.18 | .100 | .075 | .090 | [−0.02, 0.37] | [0.00, 0.36] | .26 |
| FC† | Other | 0.50 | .123 | <.001 | <.001 | [0.26, 0.74] | — | .20 |
| CVC | Other | 0.48 | .116 | <.001 | <.001 | [0.25, 0.71] | — | .14 |
| CDV† | Other | 0.47 | .108 | <.001 | <.001 | [0.26, 0.69] | — | .14 |
| PDS | Other | 0.25 | .111 | .024 | .033 | [0.03, 0.47] | — | .12 |
| PLT_Compr | Other | 0.19 | .110 | .077 | .090 | [−0.02, 0.41] | — | .13 |
| PRR | Other | 0.18 | .111 | .105 | .113 | [−0.04, 0.40] | — | .10 |
| CL | Other | −0.05 | .108 | .663 | .663 | [−0.26, 0.17] | — | .13 |

N = 383; ANCOVA Score_z ~ MODALITY + CV3 + CV5 + CV9, HC3; bootstrap 1,000 replicates. † α < .60, exploratory.

[Abbildung 2 hier: Fig2_forest.png]

### 4.2 The acceptance-trust asymmetry (H2)

The block model estimates the digital-paper contrast at +0.769 z for acceptance and +0.241 z for trust. The interaction, our central estimate, is 0.528 (person-clustered SE = 0.077, 95% CI [0.38, 0.68], p = 2.6 × 10⁻¹¹; model R² = .40; Figure 3). Table 4 collects the robustness battery: the estimate is insensitive to clustering choice (municipality-proxy clustered p = 8.2 × 10⁻¹¹; wild cluster bootstrap p = .0012) and to excluding social influence from the acceptance composite (SI-free contrast +0.84 [0.66, 1.01]). The trust main effect is cluster-sensitive (person-clustered p = .001; municipality-clustered p = .012; wild bootstrap p = .018); we read it as real but modest. The asymmetry is the robust fact: whatever a first real episode of digital voting is associated with, it is associated with roughly three times more of it in acceptance than in trust.

[Abbildung 3 hier: Fig3_interaction.png]

**Table 4. Robustness of the H2 interaction and the trust main effect.**

| Procedure | Interaction | p | Trust effect | p |
|---|---|---|---|---|
| HC3 (observation level) | 0.528 | 2.7×10⁻⁷ | 0.241 | .001 |
| Person-clustered (383) | 0.528 | 2.6×10⁻¹¹ | 0.241 | .001 |
| Municipality proxy (76) | 0.528 | 8.2×10⁻¹¹ | 0.241 | .012 |
| Wild cluster bootstrap (B = 4,999) | — | .0012 | — | .018 |
| SI-free acceptance composite | +0.84 [0.66, 1.01] | <.001 | — | — |
| DIF sensitivity (BI w/o BI2; TT w/o TT4) | BI 0.82; TT 0.25 | <.001; .013 | — | — |
| Minimal detectable effect (power .80) | d ≈ .27–.31 | — | — | — |

### 4.3 Prior attitude dominates trust and fit predictors

Hierarchical models predicting intention (and the SI-free acceptance composite) from institutional trust and a categorical-fit block (CL, PRR, PLT_Compr), over and above the covariates, add little: institutional trust contributes ΔR² ≤ .016 and the fit block ΔR² ≤ .028, in either entry order. Permutation importance makes the imbalance vivid (Figure 4): permuting the covariate block costs .16 to .18 in R², permuting institutional trust at most .004, the fit block at most .013, almost entirely through categorical legitimacy. In this sample, who the adolescent already was predicts intention better than anything the adolescent believes about the system. That is consistent with self-selection, and we intend it as a sobering benchmark for models that explain post-use intention from post-use beliefs alone.

[Abbildung 4 hier: Fig4_permutation.png]

### 4.4 Trust facets, measurement, and a discriminant-validity finding (RQ1)

At face value the trust block suggests a facet pattern: the group difference runs through generalized and institutional trust while technology trust stays flat. Two measurement results temper that reading. First, TT4 is one of the two DIF-flagged items; rescoring TT without it raises the TT contrast to +0.25 (p = .013 uncorrected), comparable to the other facets. The facet asymmetry within trust is therefore fragile, and we do not claim it. Second, and more interesting: in the multigroup CFA, the latent correlation between technology trust and generalized election trust is 1.00 in the paper group, an inadmissible-boundary solution indicating that respondents who had never used digital voting did not empirically distinguish the two facets, whereas experienced respondents did. What looks like a null effect on technology trust is partly the absence of a separate construct to move. We offer this as a finding in its own right: trust differentiation is itself a product of experience. Facet-level claims about trust in digital voting should be conditioned on usage experience, in measurement models and in theory.

**Table 3. Measurement invariance (MGCFA, MLR/FIML, 22 items, 7 factors).**

| Model | χ²(df) scaled | CFI rob. | RMSEA rob. | SRMR | Comparison | Δχ²(Δdf) | p | ΔCFI |
|---|---|---|---|---|---|---|---|---|
| Configural | 584.2 (376) | .947 | .055 | .056 | — | — | — | — |
| Metric | 604.7 (391) | .945 | .055 | .059 | vs. config. | 20.6 (15) | .150 | −.002 |
| Scalar | 648.0 (406) | .937 | .058 | .062 | vs. metric | 43.2 (15) | <.001 | −.008 |
| Partial scalar (BI2, TT4 free) | 629.1 (404) | .942 | .056 | .061 | vs. metric | 24.4 (13) | .028 | −.003 |

Note. Latent TT-TR correlation in the paper group = 1.00 (boundary solution); see text.

### 4.5 Realness as articulated versus realness as measured (RQ2)

The perceived-realness scale shows no group difference (q = .11), against our expectation. The free texts point to why. Of 92 comments (69 digital, 23 paper), five, all from digital voters, articulate a realness deficit in so many words: the digital vote "doesn't feel like a real voting booth," paper voting is "more human," voting "would feel much more real with a sheet of paper," easy access could make the vote "lose value." Two independent coders agreed on these five (blind double coding, Cohen's κ = .90; procedure disclosed in the GenAI statement). Respondents who articulated the deficit do not score lower on the realness scale; they score, if anything, higher (+0.30 z, n.s.), and higher on perceived democratic significance (+0.54, n.s.). The scale, we conclude, captured how much realness matters rather than how much realness was experienced; the two readings were conflated at item level. We treat RQ2 as unanswered and report it as a construct-validity result: the follow-up instrument separates tangibility (haptics, place, ritual) from experienced authenticity. With five coded cases, any moderation analysis would be decoration, and we refrain from one.

### 4.6 Verification

According to system logs, roughly 570 of 2,981 digital voters (19%) used the individual verification feature. The survey contains no verification-behavior item, so verification cannot be linked to individual trust in these data. We note the aggregate figure for what it descriptively is: four in five first-time digital voters did not check, in an election where checking cost one click. The follow-up study records verification behavior as a survey item with consent-based linkage to logs.

## 5. Discussion

### 5.1 What a first episode of use does, and does not do

The learning argument behind digital-voting pilots predicts that experience builds trust. In this election, experience was associated with acceptance three times more strongly than with trust, and the trust movement that did occur ran through generalized and institutional judgments rather than through beliefs about the technology, insofar as those beliefs existed as a separate object at all. The pattern fits the institutional reading of election trust (Avgerou, 2013; Romanov et al., 2025) and extends it with a measurement-level twist: institutions do not merely anchor trust, they anchor it so firmly that for inexperienced citizens the technology has no independent trust identity. The first usage episode begins to carve that identity out. This is, to our knowledge, the first field evidence locating trust differentiation itself downstream of use.

The asymmetry also disciplines how post-use acceptance findings should be read. Immediately after a smooth usage episode, acceptance constructs are high and intention is high; a naive model would celebrate the pilot. The same respondents' trust judgments barely moved, and their intention is better predicted by the attitude they walked in with than by anything they came to believe about the system. Post-use surveys of self-selected pilot users flatter the technology. The within-person asymmetry estimate is the piece of such surveys that does not flatter, because the flattery cancels.

### 5.2 Practical implications

For administrations, the result relocates the trust budget. Usability work made voting easy, and easy voting made users: the acceptance contrast, the high completion, and the enthusiastic comments all say so. None of that is the trust problem. If trust responds to institutional signals rather than interface quality, the leverage lies with the bodies that run and audit the election: visible institutional ownership, comprehensible public checking in the spirit of the German constitutional requirement of lay verifiability, and communication that explains who answers for the count. Experience programs remain worthwhile, but for adoption, not as a trust machine. The verification finding sharpens the point: a cryptographic guarantee that four in five users do not invoke cannot be the trust mechanism of a mass election; it can at best be the trust mechanism of an auditing minority on whom the others free-ride. That reading is consistent with usability evidence that voters rarely complete, and rarely understand, verification procedures even when they use them (Acemyan et al., 2014; Hilt et al., 2024).

### 5.3 Limitations

Self-selection is the design's largest liability, and we have argued where it bites (group contrasts, H1) and where it cancels (the within-person asymmetry, H2). The remaining threat to H2 is a confound that acts on one block only. The most plausible candidate is item tone: acceptance items about an experience one just chose may license more enthusiasm than trust items about elections in general. We cannot exclude this, and three observations bound it. The asymmetry survives the exclusion of social influence, the most desirability-prone construct (+0.84). The trust block does move, in theoretically expected facets, which a pure tone artifact would not predict. And partial scalar invariance held after freeing two intercepts. Second, the comparator is hypothetical by design; the asymmetry is a statement about experienced versus imagined evaluation, not about digital versus paper voting as such. Third, the election was non-binding and the participants were minors; both restrict generalization and both are addressed by the planned replication in a binding staff-council election with adults. Fourth, two scales fell below reliability thresholds and two items showed intercept DIF; affected results are labeled. Fifth, municipality clustering uses an IP-geolocation proxy pending administrative identifiers; the wild cluster bootstrap is our hedge, and it does not change any conclusion. Sixth, the analysis plan postdates data collection; we claim documented, not preregistered, analyses.

### 5.4 Future research

Three studies follow from here. The staff-council election replicates H2 and tests the facet pattern confirmatorily, with a slimmed instrument that separates tangibility from experienced authenticity and measures verification behavior individually. A survey experiment contrasts trust-by-technology (end-to-end verifiability) with trust-by-governance (citizen oversight) as framings. And the trust-differentiation finding deserves its own measurement study: if facet structure depends on experience, longitudinal invariance, not cross-group invariance, is the right lens for trust in novel civic technology.

## 6. Conclusion

A real digital election moved adolescents' acceptance of digital voting by three quarters of a standard deviation and their trust by a third of that, and it was the experience itself that first taught them to distinguish the technology from the institution behind it. Digital democracy's binding constraint is not the interface. Making voting easy makes voters willing; it does not, by itself, make the arrangement trustworthy in their eyes. Whoever wants trusted digital elections must build trustworthy institutions around verifiable technology, and must expect the two to be judged separately only once citizens have voted digitally at least once.

## Declarations

**Ethics.** The survey accompanied the U18 election, a non-binding civic-education election organized by the Bavarian Youth Council (Bayerischer Jugendring, BJR) [ggf.: under the research project blinded for review, funded by the Federal Ministry of Research, Technology and Space (BMFTR) through a DATI Innovation Sprint]. Participation in the survey was voluntary, separate from the act of voting, and open to voters aged 14 to 17. Respondents were informed about the purpose of the study, data handling, and their right to withdraw before starting the questionnaire; proceeding constituted informed consent. [PLATZHALTER: Ethikvotum — Gremium, Nummer, Datum; Regelung elterliche Einwilligung bei Minderjährigen klären.]

**Data protection.** No names or contact details were collected. Survey responses were pseudonymous; IP-based coarse geolocation collected by the survey platform was used solely to approximate municipality clusters for robustness analyses and is removed from any shared dataset. Data processing followed the GDPR. [PLATZHALTER: Verantwortlicher, DSFA ja/nein, Aufbewahrungsfrist.]

**Funding / Competing interests.** [PLATZHALTER: DATI/BMFTR-Förderkennzeichen; Rolle der Stadt München und des BJR; Erklärung, dass die Förderer keinen Einfluss auf Analyse und Interpretation hatten.] The authors report no competing interests. [prüfen]

**Data availability.** Anonymized data and analysis scripts at [Repository]; IP addresses and geolocation removed.

**GenAI disclosure.** [Nach Dossier-Freigabe finalisieren; enthält die Offenlegung der KI-gestützten Doppelcodierung der Freitextkommentare (zwei unabhängige KI-Coder, κ = .90, menschliche Validierung durch die Autorin).]

## References

- Abdala, M., et al. (2025). Trust in government or in technology? What really drives internet voting. *Political Research Quarterly*. https://doi.org/10.1177/10659129251321424 [Autorenliste von Verlagsseite übernehmen]
- Acemyan, C. Z., Kortum, P., Byrne, M. D., & Wallach, D. S. (2014). Usability of voter verifiable, end-to-end voting systems: Baseline data for Helios, Prêt à Voter, and Scantegrity II. *Journal of Election Technology and Systems, 2*(3), 26–56.
- Avgerou, C. (2013). Explaining trust in IT-mediated elections: A case study of e-voting in Brazil. *Journal of the Association for Information Systems, 14*(8). https://doi.org/10.17705/1jais.00340
- Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B, 57*(1), 289–300.
- BVerfGE 123, 39 — Bundesverfassungsgericht, Urteil vom 3. März 2009 (Wahlcomputer).
- Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *Review of Economics and Statistics, 90*(3), 414–427.
- Carter, L., & Bélanger, F. (2005). The utilization of e-government services: Citizen trust, innovation and acceptance factors. *Information Systems Journal, 15*(1), 5–25. https://doi.org/10.1111/j.1365-2575.2005.00183.x
- Chaum, D. (2004). Secret-ballot receipts: True voter-verifiable elections. *IEEE Security & Privacy, 2*(1), 38–47.
- Chen, F. F. (2007). Sensitivity of goodness of fit indexes to lack of measurement invariance. *Structural Equation Modeling, 14*(3), 464–504.
- Cheung, G. W., & Rensvold, R. B. (2002). Evaluating goodness-of-fit indexes for testing measurement invariance. *Structural Equation Modeling, 9*(2), 233–255.
- Ehin, P., Solvak, M., Willemson, J., & Vinkel, P. (2022). Internet voting in Estonia 2005–2019: Evidence from eleven elections. *Government Information Quarterly, 39*(4), 101718. https://doi.org/10.1016/j.giq.2022.101718
- Fazio, R. H., & Zanna, M. P. (1981). Direct experience and attitude–behavior consistency. *Advances in Experimental Social Psychology, 14*, 161–202.
- Glasman, L. R., & Albarracín, D. (2006). Forming attitudes that predict future behavior: A meta-analysis of the attitude–behavior relation. *Psychological Bulletin, 132*(5), 778–822.
- Hilt, T., et al. (2024). Usability and understanding of individual verifiability in the 2023 GI-election. *Proceedings of the Ninth International Joint Conference on Electronic Voting (E-Vote-ID 2024)*. [Autorenliste ergänzen]
- Regan, D. T., & Fazio, R. H. (1977). On the consistency between attitudes and behavior: Look to the method of attitude formation. *Journal of Experimental Social Psychology, 13*(1), 28–45.
- Romanov, B., et al. (2025). State versus technology: What drives trust in and usage of internet voting, institutional or technological trust? *Government Information Quarterly*. [Autorenliste von Verlagsseite übernehmen]
- Ryan, P. Y. A., Schneider, S., & Teague, V. (2015). End-to-end verifiability in voting systems, from theory to practice. *IEEE Security & Privacy, 13*(3), 59–62.
- Sandeep, M. S., & Ravishankar, M. N. (2018). Trusting e-voting amid experiences of electoral malpractice: The case of Indian elections. *Journal of Information Technology*. https://doi.org/10.1177/0268396218816199
- Solvak, M., & Vassil, K. (2018). Could internet voting halt declining electoral turnout? New evidence that e-voting is habit forming. *Policy & Internet, 10*(1). https://doi.org/10.1002/poi3.160
- Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly, 27*(3), 425–478.
- Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending UTAUT. *MIS Quarterly, 36*(1), 157–178.

*Reference status: DOIs and titles verified via Consensus/Scite (July 18 and August 4, 2026). Author lists still to be completed from publisher pages: Abdala et al. (2025); Romanov et al. (2025); Hilt et al. (2024). Note that Abdala et al. (2025, PRQ) and Romanov et al. (2025, GIQ) are two distinct Estonian studies; earlier drafts conflated them.*
