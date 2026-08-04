# Trying Is Not Trusting: Experience Effects on Acceptance, but Not Trust, in Digital Voting. Quasi-Experimental Evidence from the 2026 Bavarian U18 Election

Stephanie Wißmann
Universität der Bundeswehr München, dtec.bw

*Working paper, v6. Target outlets: HICSS / Information & Management / Government Information Quarterly.*

**Keywords:** digital voting, e-voting acceptance, trust in technology, UTAUT2, experience effect, quasi-experiment, verifiability, youth voters

---

## Abstract

Public administrations that pilot internet voting face a practical question: does letting citizens try a digital voting system build the acceptance and trust that adoption requires, or must trust be built first? We use a rare quasi-experimental setting to separate the two. In the Bavarian U18 election of February 2026, ten municipalities offered 14- to 17-year-olds a real online vote from home, while all other municipalities voted on paper in polling stations. Modality was fixed at the municipality level: no individual chose, and no individual switched. An identical post-vote questionnaire measured six UTAUT2 acceptance constructs, three trust constructs, and six experiential constructs in both groups (N = 390 analytic sample; N = 383 in covariate-complete models), with the digital group rating a system it had just used and the paper group rating the same system hypothetically.

Experience moved acceptance and trust by very different amounts. After adjusting for school type, technology competence, and prior attitude toward digital voting, acceptance constructs showed effects around three quarters of a standard deviation (block mean +0.77 z, 95% CI [0.62, 0.91]), while trust constructs moved by roughly one quarter (+0.24 z, CI [0.10, 0.39]); the modality-by-block interaction was highly significant (p < .001). Technology trust alone fell to non-significance once prior attitude was controlled. Acceptance and trust were psychometrically separable (two near-orthogonal factors; all HTMT below .85). The digital system included real individual vote verification, used by roughly one in five digital voters, yet comprehension of what happens to one's vote did not reliably improve, and the belief that the system is hard to manipulate was identical across groups.

Piloting, in short, converts hypothetical skepticism into experienced acceptance, but it does not manufacture trust. For research, the finding separates two belief systems that adoption models routinely blend. For practice, it fixes a sequence: trust-building through institutional credibility and audit transparency must precede pilots, because pilots will not do that work.

---

## 1. Introduction

In February 2026, roughly 2,981 Bavarian teenagers did something no cohort in Germany had done before: they cast a vote in an officially organized election over the internet, from home, on their own devices. Ten municipalities took part in the digital pilot of the U18 election, the established mock election for minors that runs parallel to real elections with the real candidate lists. Everywhere else, teenagers voted the traditional way, on paper, in polling stations run by youth organizations and schools. Whether a given adolescent voted digitally or on paper was decided by one thing only: the municipality they lived in.

This administrative detail creates an unusual research opportunity. The central open question in digital voting research is not whether people say they would accept internet voting. It is what actually happens to acceptance and trust when people use a real system in a real election, compared to merely imagining one. Existing acceptance studies rely overwhelmingly on hypothetical scenarios rated by convenience samples (Carter & Bélanger, 2005; Schaupp & Carter, 2005; Warkentin et al., 2018). The few field settings that exist confound experience with self-selection: in Estonia, those who vote online are those who already wanted to (Solvak & Vassil, 2016; Ehin et al., 2022), and the one field experiment that varied voting technology, in Salta, Argentina, compared machines within polling stations rather than remote voting from home (Alvarez et al., 2013). A comparison in which experienced and hypothetical evaluators are separated by residence rather than by choice, answer an identical instrument, and do so minutes after casting a real vote is, to our knowledge, not available elsewhere in the literature.

The stakes of the question are practical. Administrations weighing digital voting pilots implicitly choose between two theories of adoption. The campaign theory holds that acceptance is an information problem: explain the system well enough, and support follows. The pilot theory holds that acceptance is an experience problem: nothing persuades like using the system. A large experience effect would favor pilots over campaigns. But there is a second question hiding under the first, and it is the one this paper is about. Acceptance and trust are not the same belief. Finding a system useful, easy, and enjoyable is a judgment about a tool. Trusting a system with the integrity of an election is a judgment about an institution, and about the people and rules behind it (McKnight et al., 2002; Warkentin et al., 2018). If experience moves the first belief system but not the second, then pilots are a powerful but bounded instrument, and administrations that expect pilots to generate trust will be disappointed in a specific, predictable way.

That asymmetry is our core finding. Covariate-adjusted modality effects on the four core acceptance constructs cluster between +0.70 and +0.82 standard deviations in favor of the digital group. The three trust constructs move between +0.18 and +0.29, and the effect on technology trust is not significant once prior attitude toward digital voting is controlled. The difference between the two blocks is itself highly significant and survives every robustness check we ran: leave-one-out construct deletion, reliability screening, alternative covariate sets, and bootstrap resampling. The asymmetry is not an artifact of measurement, because acceptance and trust separate cleanly into two near-orthogonal factors with satisfactory convergent and discriminant validity.

A third finding sharpens the trust result. The digital system offered real individual verifiability: voters could check, via a code, that their ballot had arrived in the digital ballot box. Roughly one in five digital voters used this function. Yet the group that experienced a verifiable system did not reliably understand it better (comprehension: adjusted d = +0.19, not significant after false-discovery-rate correction), did not find it harder to manipulate (the single manipulation item was identical across groups, M = 2.55 in both), and wanting to verify was uncorrelated with understanding (r = .04). Verifiability as an offered function and verifiability as a trust-building experience came apart. This bears directly on the German constitutional requirement that the essential steps of an election be comprehensible to citizens without special expertise (BVerfG, 2009), and it replicates, in a field setting with minors, the usability paradox reported for verifiable voting systems in the laboratory (Acemyan et al., 2014).

The study supplies field evidence on the experience effect in digital voting with the cleanest assignment mechanism reported to date, and the effect turns out to be real, large, and confined to acceptance. Because acceptance and trust also separate empirically in these data, not just conceptually, adoption models that blend them into a single antecedent structure will keep producing contradictory coefficients: the two belief systems respond differently to the same treatment. For administrations, a sequence replaces the pilots-versus-campaigns binary. Trust work comes first, pilots second, campaigns third, because each instrument moves a different belief at a different cost.

We are deliberate about what the study is not. Assignment was clustered at the municipality level without randomization, the two groups differ in composition, survey access routes differed by modality, and the paper-voting context was a supervised group setting while digital voting happened at home. We treat all estimates as adjusted associations from a strong quasi-experiment, not as randomized-trial effects, and we discuss each threat explicitly in Section 6.

## 2. Background and Theory

### 2.1 Acceptance: judgments about a tool

Technology acceptance research explains the intention to use a system through beliefs about the system's usefulness and usability, extended in UTAUT2 by hedonic motivation, social influence, and facilitating conditions (Venkatesh et al., 2003; Venkatesh et al., 2012). Applied to voting, these constructs capture judgments about digital voting as a tool: whether it is sensible, easy, enjoyable, socially approved, and feasible for me. The e-voting literature has repeatedly confirmed that these beliefs predict stated intention to vote online (Carter & Bélanger, 2005; Choi & Kim, 2019; Zhu et al., 2021). What the literature has not resolved is where these beliefs come from, because almost all measurements are hypothetical: respondents rate a system they have never used. Construal level theory gives a specific reason to distrust that measurement situation. Psychologically distant objects are represented abstractly, in terms of schemas and generalized risk; direct experience shifts representation to concrete features (Trope & Liberman, 2010). A hypothetical digital voting system is evaluated as a category ("online voting, is that safe?"); an experienced one is evaluated as an episode ("that took two minutes and worked"). If construal drives these tool judgments, experience should raise acceptance substantially.

The attitude-strength tradition makes the same prediction through a different mechanism and gives it four decades of experimental backing. Attitudes formed through direct behavioral experience with an object are more accessible, held with more confidence, more stable, and more predictive of later behavior than attitudes formed through indirect information (Regan & Fazio, 1977; Fazio & Zanna, 1981); a meta-analysis across 128 conditions confirms direct experience as one of the strongest moderators of the attitude–behavior link (Glasman & Albarracín, 2006). The marketing analogue is exact: attitudes based on product trial predict purchase, attitudes based on advertising barely do (Smith & Swinyard, 1983). A voting pilot is a trial. The prediction that follows is not merely that the digital group reports higher acceptance, but that experience-based acceptance is the more behaviorally consequential kind, which is what makes the pilot-versus-campaign question a fair fight worth settling empirically.

### 2.2 Trust: judgments about an institution

Trust in digital voting is a different belief with a different object structure. Trust research has moved from treating trust as one holistic judgment to distinguishing trust objects: trust in a specific technology has its own components (reliability, functionality, helpfulness) and its own measurement tradition, separate from trust in people or providers (McKnight et al., 2011; Lankton et al., 2015), and which trust relationship matters depends on which target the user must rely on (Söllner et al., 2016). A recent meta-analysis shows that trust in technology and trust in provider carry distinct antecedent structures, familiarity feeding the former and institution-based assurance the latter, and that model results shift materially depending on which entities are specified (Kuen et al., 2023). The e-voting literature has begun to adopt this differentiation: trust in government and trust in technology contribute separately to internet-voting intention in Estonia (Abdala et al., 2025), multi-dimensional technology trust predicts e-voting intention (Zhu et al., 2021), and trust in e-voting has been theorized as political trust in a socio-technical arrangement in which perceptions of the technology and of the electoral authority are interdependent (Avgerou, 2013).

Following Carter and Bélanger (2005) and the institution-based trust tradition (Zucker, 1986; McKnight et al., 2002), we therefore measure three trust layers: technology trust (the system works reliably, keeps the ballot secret, resists manipulation), institutional trust (the responsible institutions run elections fairly and protect my vote), and generic trust in the procedure of digital voting. Together they capture whether the election, as an institution, remains intact when it becomes digital. Two properties distinguish these trust judgments from acceptance judgments. They refer to properties a user cannot observe in use: a smooth voting session reveals nothing about server-side integrity, and post-use trust accordingly draws on perceptions accumulated around the technology's institutional context rather than on the transaction alone (Hernández-Ortega, 2011). And they are anchored in dispositions and prior attitudes toward the state and toward technology rather than in episodic evidence (Warkentin et al., 2018); prior attitudes have been shown to govern how people interpret subsequent direct experience with an institution, rather than being overwritten by it (Rosenbaum et al., 2005). Both properties predict that experience should move trust much less than acceptance. A pleasant user experience is simply not evidence about the things trust is about. Field data point the same way: in the Salta e-voting field experiment, voters found the new technology easier and supported its adoption while concerns about ballot secrecy persisted (Alvarez et al., 2013), and in a UK conjoint experiment internet voting was perceived as less trustworthy than in-person voting across the board, with integrity concerns dominating support (Turnbull-Dugarte & Devine, 2023).

### 2.3 Verifiability and the legibility problem

Cryptographic end-to-end verifiability decomposes into cast-as-intended, recorded-as-cast, and tallied-as-recorded guarantees, with individual verification (a voter checks her own ballot) distinct from universal verification (anyone checks the tally) (Chaum, 2004; Benaloh, 2006; Adida, 2008). The system studied here implemented individual recorded-as-cast verification: after voting, a voter could check that her ballot had arrived in the digital ballot box. In trust terms, this function targets exactly the technology trust layer; it replaces a promise with a checkable receipt. Whether it works psychologically is an open question with mounting negative evidence. Laboratory studies of verifiable systems find severe usability problems and voters who can rarely explain what verification proves (Karayumak et al., 2011; Acemyan et al., 2014; Marky et al., 2018); a comparative evaluation of individually verifiable internet-voting schemes concludes that verification steps burden precisely the human factors on which the security argument depends (Marky et al., 2021); improved interfaces raise manipulation detection but leave voters unsure how to act on anomalies (Kulyk et al., 2020). Closest to our setting, an online study around a real German association election using second-device verification, the same approach deployed here, found good perceived usability alongside insufficient understanding of what verification establishes (Hilt et al., 2024). The German Federal Constitutional Court has made public comprehensibility without special expertise a constitutional condition for electronic voting (BVerfG, 2009). What has been missing is a field test of whether experiencing a verifiable system in a real election produces comprehension and technology trust in the voters it is meant to reassure.

### 2.4 Hypotheses

The confirmatory hypothesis concerns the asymmetry:

**H1.** Direct experience of digital voting is associated with higher acceptance and higher trust relative to hypothetical evaluation, and the association is substantially stronger for acceptance constructs than for trust constructs.

H1 presupposes that acceptance and trust are distinct measurement objects; we test discriminant validity as a precondition (Section 5.2). Two further analyses were specified as exploratory and are labeled as such throughout. One asks whether institutional trust amplifies the effect of social endorsement on intention (an IT × SI interaction). The other compares how much variance in intention is explained by second-hand assurance (institutional trust, social influence) against the fit of the digital act to the concept of "a real election" (concreteness, ritual, comprehension). Both explorations generate hypotheses; neither tests one.

## 3. Method

### 3.1 Setting: a real election with municipality-level modality assignment

The empirical setting is the U18 election accompanying the Bavarian municipal elections of March 8, 2026. The U18 election is an officially organized election for those too young to vote, run by the Bavarian Youth Ring (Bayerischer Jugendring); it uses the real candidate lists and real ballot structure but does not bind the official result. U18 polling stations were open across Bavaria from February 16 to 27, 2026, organized by local youth rings, youth associations, municipalities, and schools.

For the first time, and in cooperation with the Bavarian State Ministry for Digital Affairs, ten areas offered digital voting: Augsburg (city), Dasing, Donauwörth, the district of Regensburg, Lauf an der Pegnitz, Lappersdorf, Mellrichstadt, Pegnitz, Tutzing, and Zeitlarn. In these areas, all 14- to 17-year-olds with German or EU citizenship received a personal polling notification by mail (17,850 notifications) and could vote online from home; 2,981 did. In all other areas, voting took place on paper in U18 polling stations.

The design point that carries the study is the assignment mechanism. Modality was not chosen by individuals and not assigned at polling stations; it was fixed by municipality of residence. This is cluster assignment at the municipality level. There was no individual self-selection into modality and no switching between modalities. The design is quasi-experimental, not randomized: municipalities were selected, not drawn, and digital and paper municipalities differ in composition (Section 6). But the mechanism excludes the individual-level self-selection that contaminates comparisons of online and paper voters in settings like Estonia, where every voter chooses a channel.

The digital system included a real individual verification function (recorded-as-cast): voters could check, via a code, that their ballot had been received in the digital ballot box. About 570 digital voters used it, roughly 19% of digital votes cast.

### 3.2 Procedure and instrument

The survey was attached to the act of voting, with one instrument and two access routes. Digital voters were shown the questionnaire directly after casting their vote; they rated a system they had just used. Paper voters reached the same questionnaire via QR codes on posters in the polling stations; they rated a digital voting system they had not experienced. The two versions are item-identical and differ only in tense: experiential past tense in the digital version ("the digital vote was easy to cast") and subjunctive in the paper version ("would be easy to cast").

The questionnaire comprises 64 content items measuring 17 constructs, ten sociodemographic and attitudinal covariates (CV1–CV10), and an open comment field. Four construct clusters matter here. The acceptance cluster operationalizes six UTAUT2 constructs (behavioral intention BI, performance expectancy PE, effort expectancy EE, social influence SI, facilitating conditions FC, hedonic motivation HM), adapted to the voting domain and translated into age-appropriate German (Venkatesh et al., 2012). The trust cluster measures technology trust (TT), institutional trust (IT), and generic trust in digital voting (TR), following Carter and Bélanger (2005) and Warkentin et al. (2018). The disposition cluster measures technology optimism (TO) and innovativeness (IN) from the technology readiness tradition (Parasuraman & Colby, 2015); these are stable person characteristics used to probe selection, not outcomes. The experiential cluster contains six constructs, five of them newly developed for this study and piloted with 15 adolescents in November 2025: process legibility (PLT, with a comprehension subscale PLT_Compr and a verification-desire subscale), concrete liveness (CL, the felt reality of the vote arriving), procedural ritual (PRR), personal democratic significance (PDS), commitment to vote choice (CVC), and civic duty (CDV, following the calculus-of-voting tradition; Riker & Ordeshook, 1968; Blais, 2000).

Covariates used in adjustment models are school type (CV3), self-rated technology competence (CV5), and prior attitude toward digital voting (CV9); political interest (CV4) enters robustness variants. A legal constraint shaped the design: pre-election surveying was not permitted because election organizers classified it as potential undue influence on the vote. CV9 is therefore a retrospective post-vote measure of prior attitude, a limitation we return to in Section 6.

### 3.3 Sample

The raw data comprise 511 responses (387 digital, 124 paper). Completed, non-test interviews yield the analytic sample of N = 390 (266 digital, 124 paper). Complete covariates (CV3, CV5, CV9) reduce this to N = 384 (260 digital, 124 paper); one further case with incomplete standardized scales leaves N = 383 (259 digital, 124 paper) for the adjusted models. The covariate filter costs six digital cases and shifts the modality composition by less than one percentage point; dropout comparisons on core scales show no signs of modality-related selection. In the analytic sample, 54.1% identified as female, 39.7% as male, and 2.1% as diverse; ages ranged from 14 to 17 (the paper group additionally contains twelve younger participants, addressed in robustness checks); 61.5% attended a Gymnasium, which overrepresents that school type; and for 69.2% this was their first official election experience.

### 3.4 Analytic strategy

Reliability was estimated with Cronbach's alpha. Alphas for the seven focal acceptance and trust scales range from .76 to .86 (BI .80, PE .82, SI .84, HM .79, TT .86, IT .83, TR .76); CL (.90) and PDS (.88) are high; FC (.48), CDV (.52), and the full PLT scale are weak, and results involving them are labeled accordingly and never carry the main argument.

The analysis proceeds in five steps. (1) Group contrasts: Welch t-tests and Cohen's d on the unadjusted digital–paper differences. (2) Adjusted contrasts: ANCOVA models on z-standardized outcomes with modality plus CV3, CV5, and CV9, HC3-robust standard errors, on the fixed N = 383 sample; Benjamini–Hochberg false-discovery-rate correction across the 14 construct tests; 1,000 bootstrap replications per focal construct. (3) Measurement separation: exploratory factor analysis with parallel analysis over the 20 acceptance and trust items, average variance extracted, Fornell–Larcker comparisons, and HTMT ratios (Fornell & Larcker, 1981; Henseler et al., 2015). (4) The asymmetry test: a person-by-block model with each participant contributing an acceptance-block mean (BI, PE, SI, HM) and a trust-block mean (IT, TT, TR), regressed on modality, block, their interaction, and covariates with HC3 errors (766 block observations from 383 persons), plus a construct-level comparison of the seven adjusted coefficients (Welch and Mann–Whitney), leave-one-out sensitivity, and a check that effect sizes do not track scale reliabilities. (5) Attenuation analysis: single-covariate models quantifying how much of each modality effect is absorbed by each covariate, foremost prior attitude.

Given the cluster assignment, the ideal specification would include municipality random effects. Municipality identifiers were not collected with the survey responses, so multilevel models are not possible; we treat p-values conservatively and flag this as the design's principal inferential limitation.

## 4. Results

### 4.1 Balance: what assignment equalized and what it did not

The two groups are balanced exactly where the experience-effect argument needs them to be, and unbalanced where a municipality-clustered design predicts. Technology optimism, a stable disposition, is essentially identical across groups (d = 0.06, p = .54), and technology competence differs only marginally (d = 0.26). The digital group was not a group of technology enthusiasts. Composition, however, differs: the digital group is more gymnasial (school type d = 0.62), more politically interested (d = 0.64), and holds more favorable prior attitudes toward digital voting (d = 0.55). A propensity model separates the groups well (AUC = .86), which is why we base all substantive conclusions on covariate-adjusted estimates and treat even these as associations. The imbalance pattern also fixes the direction of the remaining bias: uncontrolled selection favors the digital group, so unadjusted effects overstate, and the question is what survives adjustment.

### 4.2 Acceptance and trust are two constructs, not one

An exploratory factor analysis of the 20 acceptance and trust items yields a clear two-factor solution: acceptance items (BI, PE, SI, HM) load on one factor, trust items (TT, IT, TR) on the other, with factor scores correlating near zero (r ≈ .00). Convergent validity is satisfactory for all seven scales (AVE .64 to .81), every scale passes the Fornell–Larcker criterion, and all cross-block HTMT ratios remain below the .85 threshold. Composite acceptance and composite trust correlate at r ≈ .60: related, as any adoption model would expect, but well below the discriminant-validity bounds. The asymmetry reported next is therefore a difference between two separable belief systems, not between two labels for the same factor.

### 4.3 The experience effect and its asymmetry

Unadjusted contrasts are large across the board and largest for acceptance: SI d = 1.19, HM d = 1.14, PE d = 1.02, BI d = 0.97, EE d = 1.54 (the largest single effect; EE is available in the descriptive pipeline only), against TR d = 0.53, TT d = 0.39, IT d = 0.44. Adjustment for school type, technology competence, and prior attitude cuts these roughly in half but preserves the pattern. Table 1 reports the adjusted modality coefficients on z-standardized outcomes.

**Table 1. Adjusted modality effects (digital vs. paper), ANCOVA with CV3, CV5, CV9; z-standardized outcomes; N = 383.**

| Block | Construct | b (z) | 95% CI | p | BH-significant |
|---|---|---|---|---|---|
| Acceptance | SI Social influence | +0.82 | [0.63, 1.02] | < .001 | yes |
| Acceptance | HM Hedonic motivation | +0.81 | [0.62, 1.00] | < .001 | yes |
| Acceptance | BI Behavioral intention | +0.71 | [0.53, 0.90] | < .001 | yes |
| Acceptance | PE Performance expectancy | +0.70 | [0.51, 0.89] | < .001 | yes |
| Trust | TR Generic trust | +0.29 | [0.11, 0.47] | .002 | yes |
| Trust | IT Institutional trust | +0.27 | [0.07, 0.48] | .010 | yes |
| Trust | TT Technology trust | +0.18 | [−0.02, 0.37] | .075 | no |
| Experiential | CVC Commitment to vote choice | +0.48 | [0.25, 0.70] | < .001 | yes |
| Experiential | PDS Democratic significance | +0.25 | [0.03, 0.47] | .024 | yes |
| Experiential | PLT_Compr Comprehension | +0.19 | [−0.02, 0.41] | .077 | no |
| Experiential | PRR Procedural ritual | +0.18 | [−0.04, 0.40] | .105 | no |
| Experiential | CL Concrete liveness | −0.05 | [−0.26, 0.16] | .663 | no |

*Note.* FC (+0.50) and CDV (+0.47) also reach significance but rest on scales with α < .55 and are reported for completeness only. EE was not available in the covariate-complete pipeline; its unadjusted d of 1.54 and an earlier adjusted estimate near +1.5 mark it as the strongest acceptance effect. Bootstrap confidence intervals (1,000 replications) closely match the analytic intervals.

The formal asymmetry test aggregates constructs into blocks. The adjusted digital advantage is +0.77 z (95% CI [0.62, 0.91]) for the acceptance block and +0.24 z (CI [0.10, 0.39]) for the trust block; the modality-by-block interaction is −0.53 (p = 2.1 × 10⁻⁷). At the construct level, the mean adjusted coefficient is 0.762 for acceptance versus 0.248 for trust (difference 0.514; Welch t = 10.75, p < .001; all four acceptance coefficients exceed all three trust coefficients, Mann–Whitney p = .057 at minimal power). The asymmetry survives every probe we ran. Leaving out any single construct changes the block difference by at most 0.04 and never flips its sign. Effect sizes do not track reliabilities (trust scales are among the most reliable, yet move least; TT has the highest alpha in the set, .86, and the smallest effect). The difference is nearly identical whether computed at construct level (0.514) or in the person-by-block model (0.528). And the asymmetry concerns magnitude, not direction: trust also moves upward with experience, by about a quarter standard deviation, before covariate adjustment absorbs most of it.

### 4.4 What drives the effects: prior attitude anchors trust

Single-covariate attenuation models locate the mechanism. Controlling prior attitude toward digital voting (CV9) alone reduces the raw-scale modality effect on technology trust by roughly three quarters, from −0.42 to −0.10 scale points (p = .23, non-significant), and on generic trust by roughly 60%, from −0.65 to −0.25. The same control reduces the behavioral-intention effect by only about a third and leaves a large residual (−0.72 scale points, p < 10⁻¹⁰); SI, HM, and PE behave like BI. Prior attitude also correlates with trust at the person level (CV9 with TR r = .48, with TT r = .44) at similar strength in both modality groups. The picture is consistent: trust judgments are anchored in the attitude a person brings to the election, and experience adds little on top; acceptance judgments respond to the episode itself. Moderation, by contrast, is weak and scattered: 6 of 42 modality-by-covariate interactions reach p < .05 with coefficients between |0.17| and |0.26|, none of which alters the block-level conclusion.

### 4.5 Verification offered is not verification understood

The digital system's verification function gives the trust result a sharp edge. Around 19% of digital voters actually checked that their ballot had arrived, a substantial uptake for an optional technical function. Yet experiencing the verifiable system did not reliably raise comprehension: the adjusted effect on the comprehension subscale is +0.19 (p = .077, not significant after correction), with a bootstrap interval spanning zero. More telling still, the single item measuring perceived manipulation resistance ("hard to manipulate") is the only item in the entire instrument with no modality difference at all (M = 2.55 in both groups, p = .99), and its absolute level is the lowest in the trust block: skepticism about manipulability is both universal and untouched by experience. Comprehension and the desire to verify, finally, are uncorrelated (r = .04 in the factor analysis of the PLT items; r = .01 in a replication round). Wanting to check is not an expression of understanding, and understanding does not create the wish to check. Because responses were anonymous, verification use could not be linked to individual survey responses; the natural follow-up, whether verifiers trust more, remains open. What the group-level data show is a boundary: a real, used verification function did not convert into measurable comprehension or technology trust. Offering verifiability is necessary for the constitutional standard of a citizen-comprehensible election; it is evidently not sufficient.

### 4.6 Experience does not cheapen the act

A recurring objection to digital voting holds that removing effort drains the act of its meaning. The experiential constructs speak against this, in both directions. The felt reality of the vote (concrete liveness, including "it felt like my vote really arrived") shows no modality effect whatsoever (−0.05); the digital vote did not feel less real, and it did not need the polling station to feel real. Ritual quality (+0.18, n.s.) did not measurably suffer either. Meanwhile commitment to vote choice (+0.48) and personal democratic significance (+0.25) were higher in the digital group. One cultural belief item, "if voting is too easy, it feels less meaningful," retained in the instrument as a single indicator, correlates negatively with intention in both groups: the conviction that voting must be effortful depresses willingness independently of what voters actually experienced. The experiential layer of the vote is, in these data, modality-invariant; the evaluative layer is not.

### 4.7 Exploratory analyses

Two pre-specified exploratory analyses are reported as hypothesis-generating. One concerns social influence: the IT × SI interaction on intention is small but survives FDR correction (b = 0.08, p_FDR = .031), and the effect of social endorsement on intention rises from 0.39 (low IT) to 0.55 (high IT). Peer endorsement appears to matter more when the institutional frame is trusted, a pattern worth a targeted test in adult populations. The other weighs second-hand assurance against experiential fit: institutional trust and social influence explain substantially more variance in intention (R² = .42) than the concreteness-ritual-comprehension block (R² = .29, largely carried by the prior-attitude covariate), and adding the fit constructs to the assurance model raises R² by less than .01. In a supplementary fsQCA exploration, configurations combining generic and technology trust with concreteness and democratic significance were sufficient for high intention (solution coverage .55, consistency .84); given the method's sensitivity to calibration choices we use it only as a source of configurational hypotheses, not as evidence.

## 5. Discussion

### 5.1 Two belief systems, one treatment, two responses

The study set out to measure what experiencing digital voting does that imagining it does not. The answer has a shape: experience is a powerful treatment for acceptance and a weak one for trust. Three quarters of a standard deviation, the adjusted acceptance effect, is a large distance in attitude research; it is the difference between a skeptical and a supportive median respondent. One quarter of a standard deviation, most of it absorbed by prior attitude, is what the same episode did to trust. The factor structure shows these are genuinely different judgments; the attenuation analysis shows why they respond differently. Acceptance feeds on episodic evidence, and the episode delivered: the vote was fast, easy, and worked. Trust feeds on priors about institutions and unobservable system properties, and a smooth two-minute session is simply not evidence about those. Voters, including 14-year-olds, appear to know the difference.

This reading disciplines the experience-effect literature in both directions. Against the hypothetical-scenario tradition, it shows that intention measured on imagined systems substantially understates the acceptance that real use produces; construal-level theory predicted exactly this shift from abstract category to concrete episode (Trope & Liberman, 2010), and the attitude-strength tradition adds that experience-based acceptance is also the more accessible, more confident, and more behavior-predictive kind (Fazio & Zanna, 1981; Glasman & Albarracín, 2006). Against adoption optimism, it shows that the shift stops at the border of trust. The pattern has precedents that were never read together as one finding: in Salta, e-voters judged the technology easier and supported it while ballot-secrecy concerns persisted (Alvarez et al., 2013), and in Estonia trust followed use only slowly across a decade of habituation (Solvak & Vassil, 2016; Ehin et al., 2022). Both look less like communication failures and more like the normal operation of the asymmetry documented here within a single election.

### 5.2 The verification paradox, now in the field

The verifiability result extends laboratory findings into a real election with a population of first-time voters. Verification was not an exotic feature: nearly one in five used it. Yet neither comprehension nor perceived manipulation resistance moved. That combination, willing use without understanding, mirrors what usability research keeps finding in controlled settings, from voters who cannot complete or explain verification (Acemyan et al., 2014; Marky et al., 2018) to participants who check their vote but do not know what to do with the result (Kulyk et al., 2020; Hilt et al., 2024). The mechanism verifiability is supposed to trigger, replacing trust in authorities with checkable evidence, presupposes that voters understand what the check proves; the orthogonality of comprehension and verification desire (r ≈ .04) suggests that for many users the check works as ritual and reassurance, not as a way of understanding the system. For the German debate, the implication is direct. The Federal Constitutional Court's public-comprehensibility standard (BVerfG, 2009) will not be met by deploying cryptographic verifiability alone; it requires an institutional translation layer, independent audits, public key ceremonies, comprehensible verification interfaces, and formal objection rights, that converts mathematical verifiability into civic comprehensibility. Building that layer is trust work, and per Section 4.4 it is work that pilots do not do by themselves.

### 5.3 A sequencing logic for administrations

The policy question that motivated the study was pilots versus campaigns. The data replace that binary with a sequence. Trust work comes first: institutional credibility, audit transparency, and oversight must be in place before piloting, because the pilot will not create them, and because prior attitude, the strongest anchor of trust, is formed before the first login. Pilots come second, and they are the strongest acceptance instrument available: no realistic information campaign moves attitudes by three quarters of a standard deviation. Campaigns come third, targeted at what they can actually do, which is inform the never-users whose acceptance a pilot cannot reach. Skeptic work comes last and must be specific: prior skeptics moved least in these data, and the belief that the system can be manipulated was immune to experience, which suggests engagement formats that address manipulation resistance directly (public audits, adversarial testing, observable recounts) rather than more user experience. The often-proposed alternative ordering, building trust through use, is the one ordering these data reject.

### 5.4 Theoretical implications

For acceptance research, the results argue for treating trust not as another antecedent in the UTAUT nomological net but as a separate belief system with its own formation mechanism: dispositional anchoring rather than episodic updating. Models that regress intention on trust and usability jointly will keep finding context-dependent coefficients as long as they ignore that one predictor updates with experience and the other barely does. For trust research, the three-layer measurement (technology, institution, procedure) behaved as theorized, and the layers moved together in their resistance to experience, which is what the dispositional-anchoring account predicts and a system-property account would not; the result also illustrates the meta-analytic point that conclusions about trust depend on which trust entities a model specifies (Kuen et al., 2023). The immovable manipulation-resistance belief invites a further differentiation the present instrument cannot deliver: trust and distrust are increasingly modeled as separate constructs with separate consequences rather than poles of one scale (Hosseini Shoabjareh et al., 2024), and a distrust measure may be what a manipulation-focused belief actually requires. For the construal-level account of the experience effect, the modality invariance of concrete liveness is a useful negative: experience lowered construal for evaluative judgments while the phenomenal reality of the act was already medium-independent. Feeling that a vote is real and judging a system acceptable are, empirically, different operations.

## 6. Limitations

The design invites specific objections, several of them raised in research colloquia on this project, and we prefer to name them precisely.

**Assignment and clustering.** Municipalities were selected, not randomized, and survey responses carry no municipality identifier, so multilevel models and design-based cluster corrections are unavailable. All estimates are adjusted associations. The balance analysis brackets the problem, dispositions balanced, composition not, but cannot eliminate unobserved municipality-level confounding.

**Urban–rural composition.** The ten digital areas mix one large city, a rural district, and several small towns; paper municipalities span all of Bavaria. Group-level urbanity therefore differs in ways individual covariates only partly capture. Because the digital municipalities are identified by name, a municipality-level contextual comparison (population size, density, school infrastructure) is feasible without individual identifiers and is the first robustness analysis we recommend for reanalysis.

**Context of the voting act.** Paper voting happened in a supervised group setting, often as a class activity with teacher preparation and immediate peer presence; digital voting happened alone at home following a mailed notification. The modality contrast is therefore also a social-context contrast. The direction of this confound is not obvious (group settings could inflate social influence in the paper group, which would bias the SI effect downward), but it cannot be removed, and teacher-level intensity of preparation is unobserved.

**Survey access routes.** Digital voters flowed into the survey directly after voting; paper voters had to scan a poster QR code. Differential selection into the survey, on motivation among paper respondents in particular, cannot be excluded, and the direction of the resulting bias is unclear.

**No pre-measurement.** Election organizers prohibited pre-vote surveying as potential undue influence. Prior attitude (CV9) is therefore measured retrospectively after the vote and may itself be colored by the experience, which would make our covariate adjustment conservative for acceptance (experience inflating reported prior favorability) but could work either way for trust. Panel designs around lower-stakes ballots are the clean solution.

**Measurement.** FC and CDV are weakly reliable and carry no conclusions. The full PLT scale is not unidimensional; we analyzed its comprehension subscale separately, and the factor evidence (two orthogonal subdimensions) suggests that "experiential realness" style constructs may split into tangibility and election-authenticity components, which should be modeled as distinct constructs and checked with factor analyses rather than alphas alone. The 97 open-text comments, several of which articulate exactly the "did not feel quite real" experience the quantitative CL scale does not detect, can be dummy-coded and entered as an independent variable and as a moderator; we flag this as an inexpensive follow-up analysis rather than performing it post hoc here.

**Method scope.** We deliberately keep fsQCA out of the confirmatory chain: with seven conditions, calibration cutoffs materially change solutions, and configurational output resists the compact interpretation that regression-based replication requires. Where configurations suggested hypotheses (Section 4.7), the forward path is a simple moderated model with two or three predictors, not a larger truth table.

**Generalizability.** Participants are 14- to 17-year-olds in one German state, most voting for the first time, in an election without legal effect. First-time youth voters are arguably the hardest test for an experience effect on trust (no accumulated electoral habits) but an easy one for acceptance (high baseline digital fluency). Adult populations with entrenched paper habits may show smaller acceptance effects; the trust asymmetry, being dispositional in origin, should replicate. That is a testable claim, not an assumption.

## 7. Future Research

The project continues in two Munich settings that vary exactly the dimensions this study could not: staff council elections (an adult workforce with wide variance in technology exposure, including entire units without workplace PC access) and the foreign residents' advisory board election (a low-turnout electorate where digital voting is hoped to raise participation). Both will offer in-person, postal, and digital channels with free choice, which replaces cluster assignment with self-selection and thus demands a different design: channel-choice modeling plus the pre/post panels that were legally impossible here, feasible around non-electoral participation formats (budget consultations, siting decisions) where pre-measurement does not constitute election influence. Three instrument changes follow from the limitations: model realness as two constructs (tangibility, election-authenticity) with confirmatory factor checks; carry the verification-desire subscale into a dedicated study linking actual verification behavior to trust, which requires a consented identifier; and retain the manipulation-resistance item as the single most informative trust indicator in the set. Finally, the experience-effect proposition should meet a randomized test: within a single municipality willing to run parallel modalities, random assignment of invitation waves would deliver the causal estimate this design can only approximate.

## 8. Conclusion

Ten Bavarian municipalities let teenagers vote online in a real election; the rest voted on paper; an identical questionnaire caught both groups minutes later. That configuration yields the cleanest field estimate to date of what experiencing digital voting does to the beliefs that govern adoption. It does a great deal, to exactly one belief system: acceptance rose by about three quarters of a standard deviation after adjustment, while trust rose by a quarter at most, technology trust not significantly at all once prior attitudes were controlled, and a genuinely used verification function failed to produce measurable comprehension. Trying is believing, for usefulness, ease, and enjoyment. Trying is not trusting. Administrations should read the two results together: pilots are the strongest acceptance instrument available to them, and pilots relieve them of none of the institutional trust work, because that work is the precondition, not the product, of letting citizens try.

---

## References

Acemyan, C. Z., Kortum, P., Byrne, M. D., & Wallach, D. S. (2014). Usability of voter verifiable, end-to-end voting systems: Baseline data for Helios, Prêt à Voter, and Scantegrity II. *Journal of Election Technology and Systems, 2*(3), 26–56.

Abdala, M., et al. (2025). Trust in government or in technology? What really drives internet voting. *Political Research Quarterly*. Advance online publication.

Adida, B. (2008). Helios: Web-based open-audit voting. *Proceedings of the 17th USENIX Security Symposium*, 335–348.

Alvarez, R. M., Levin, I., Pomares, J., & Leiras, M. (2013). Voting made safe and easy: The impact of e-voting on citizen perceptions. *Political Science Research and Methods, 1*(1), 117–137.

Avgerou, C. (2013). Explaining trust in IT-mediated elections: A case study of e-voting in Brazil. *Journal of the Association for Information Systems, 14*(8), 420–451.

Benaloh, J. (2006). Simple verifiable elections. *Proceedings of the USENIX/ACCURATE Electronic Voting Technology Workshop*.

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B, 57*(1), 289–300.

Blais, A. (2000). *To vote or not to vote: The merits and limits of rational choice theory.* University of Pittsburgh Press.

Bundesverfassungsgericht. (2009). Urteil des Zweiten Senats vom 3. März 2009, 2 BvC 3/07 (Wahlcomputer-Urteil). BVerfGE 123, 39.

Carter, L., & Bélanger, F. (2005). The utilization of e-government services: Citizen trust, innovation and acceptance factors. *Information Systems Journal, 15*(1), 5–25.

Chaum, D. (2004). Secret-ballot receipts: True voter-verifiable elections. *IEEE Security & Privacy, 2*(1), 38–47.

Choi, S., & Kim, B. (2019). Voter intention to use e-voting technologies: Security, technology acceptance, election type, and political ideology. *Journal of Information Technology & Politics, 16*(4), 344–362.

Ehin, P., Solvak, M., Willemson, J., & Vinkel, P. (2022). Internet voting in Estonia 2005–2019: Evidence from eleven elections. *Government Information Quarterly, 39*(4), 101718.

Fazio, R. H., & Zanna, M. P. (1981). Direct experience and attitude–behavior consistency. *Advances in Experimental Social Psychology, 14*, 161–202.

Fornell, C., & Larcker, D. F. (1981). Evaluating structural equation models with unobservable variables and measurement error. *Journal of Marketing Research, 18*(1), 39–50.

Glasman, L. R., & Albarracín, D. (2006). Forming attitudes that predict future behavior: A meta-analysis of the attitude–behavior relation. *Psychological Bulletin, 132*(5), 778–822.

Henseler, J., Ringle, C. M., & Sarstedt, M. (2015). A new criterion for assessing discriminant validity in variance-based structural equation modeling. *Journal of the Academy of Marketing Science, 43*(1), 115–135.

Hernández-Ortega, B. (2011). The role of post-use trust in the acceptance of a technology: Drivers and consequences. *Technovation, 31*(10–11), 523–538.

Hilt, T., et al. (2024). Usability and understanding of individual verifiability in the 2023 GI-election. *Proceedings of the Ninth International Joint Conference on Electronic Voting (E-Vote-ID 2024)*.

Hosseini Shoabjareh, A., et al. (2024). The role of trust and distrust in technology usage: An in-depth investigation of traffic information apps usage for mandatory and non-mandatory trips. *Travel Behaviour and Society, 34*.

Karayumak, F., Olembo, M. M., Kauer, M., & Volkamer, M. (2011). Usability analysis of Helios: An open source verifiable remote electronic voting system. *Proceedings of the USENIX Electronic Voting Technology Workshop/Workshop on Trustworthy Elections (EVT/WOTE '11)*.

Kuen, L., Westmattelmann, D., Bruckes, M., & Schewe, G. (2023). Who earns trust in online environments? A meta-analysis of trust in technology and trust in provider for technology acceptance. *Electronic Markets, 33*, Article 61.

Kulyk, O., Volkamer, M., et al. (2020). Towards improving the efficacy of code-based verification in internet voting. *Financial Cryptography and Data Security Workshops (Voting 2020)*.

Lankton, N. K., McKnight, D. H., & Tripp, J. (2015). Technology, humanness, and trust: Rethinking trust in technology. *Journal of the Association for Information Systems, 16*(10), 880–918.

Marky, K., Kulyk, O., Renaud, K., & Volkamer, M. (2018). What did I really vote for? On the usability of verifiable e-voting schemes. *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems*.

Marky, K., et al. (2021). Investigating usability and user experience of individually verifiable internet voting schemes. *ACM Transactions on Computer-Human Interaction, 28*(5).

McKnight, D. H., Carter, M., Thatcher, J. B., & Clay, P. F. (2011). Trust in a specific technology: An investigation of its components and measures. *ACM Transactions on Management Information Systems, 2*(2), Article 12.

McKnight, D. H., Choudhury, V., & Kacmar, C. (2002). Developing and validating trust measures for e-commerce: An integrative typology. *Information Systems Research, 13*(3), 334–359.

Parasuraman, A., & Colby, C. L. (2015). An updated and streamlined technology readiness index: TRI 2.0. *Journal of Service Research, 18*(1), 59–74.

Regan, D. T., & Fazio, R. H. (1977). On the consistency between attitudes and behavior: Look to the method of attitude formation. *Journal of Experimental Social Psychology, 13*(1), 28–45.

Riker, W. H., & Ordeshook, P. C. (1968). A theory of the calculus of voting. *American Political Science Review, 62*(1), 25–42.

Rosenbaum, D. P., Schuck, A. M., Costello, S. K., Hawkins, D. F., & Ring, M. K. (2005). Attitudes toward the police: The effects of direct and vicarious experience. *Police Quarterly, 8*(3), 343–365.

Schaupp, L. C., & Carter, L. (2005). E-voting: From apathy to adoption. *Journal of Enterprise Information Management, 18*(5), 586–601.

Smith, R. E., & Swinyard, W. R. (1983). Attitude-behavior consistency: The impact of product trial versus advertising. *Journal of Marketing Research, 20*(3), 257–267.

Söllner, M., Hoffmann, A., & Leimeister, J. M. (2016). Why different trust relationships matter for information systems users. *European Journal of Information Systems, 25*(3), 274–287.

Solvak, M., & Vassil, K. (2016). *E-voting in Estonia: Technological diffusion and other developments over ten years (2005–2015).* Johan Skytte Institute of Political Studies, University of Tartu.

Trope, Y., & Liberman, N. (2010). Construal-level theory of psychological distance. *Psychological Review, 117*(2), 440–463.

Turnbull-Dugarte, S. J., & Devine, D. (2023). Support for digitising the ballot box: A systematic review of i-voting pilots and a conjoint experiment. *Electoral Studies, 86*, 102679.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly, 27*(3), 425–478.

Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology. *MIS Quarterly, 36*(1), 157–178.

Warkentin, M., Sharma, S., Gefen, D., Rose, G. M., & Pavlou, P. (2018). Social identity and trust in internet-based voting adoption. *Government Information Quarterly, 35*(2), 195–209.

Zhu, Y.-Q., Azizah, A. H., & Hsiao, B. (2021). Examining multi-dimensional trust of technology in citizens' adoption of e-voting in developing countries. *Information Development, 37*(2), 193–208.

Zucker, L. G. (1986). Production of trust: Institutional sources of economic structure, 1840–1920. *Research in Organizational Behavior, 8*, 53–111.

*Working-paper note on references: entries marked "et al." (Abdala 2025; Hilt 2024; Hosseini Shoabjareh 2024; Kulyk 2020; Marky 2021) and the co-author list of Kuen et al. (2023) could not be fully verified against the published records from the current environment; complete and check them before submission. Titles, first authors, venues, and DOIs of these entries were verified via Consensus and Scite on July 18, 2026.*

---

*Appendix note: The complete item documentation (64 items, 17 constructs, German originals with tense variants) follows the instrument documented in the study setup; sample sizes across analysis stages are 511 raw responses, 390 analytic, 384 covariate-complete, 383 model sample. Two data-cleaning discrepancies between analysis rounds (treatment of 12 flagged potential duplicate cases; construct item counts for TT/CL/PDS/PRR between the 4- and 5/6-item variants) are documented in the analysis archive and do not affect the block-level results, which are stable across all sample variants (±0.01–0.06).*
