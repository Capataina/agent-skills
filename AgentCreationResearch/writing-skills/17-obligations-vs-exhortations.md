# Obligations vs Exhortations

This is the sharpest distinction in prompt engineering for reliability. Added 2026-04-18 from research pass.

## The core finding

Research consistently shows that **specificity and verifiability** of an instruction matter more than which layer (personality vs skill) it lives in. The dividing line that actually predicts behavioural change is not *which file* but *whether the instruction is verifiable*.

**Exhortations** — "be thorough", "go above and beyond", "always strive for excellence", "don't satisfice", "maintain high standards" — are sycophantically absorbed by RLHF-trained models. The model reads the instruction, nods verbally, and satisfices anyway. The mechanism: RLHF rewards the *appearance* of thoroughness, which exhortations explicitly optimise for. Confident-looking output scores higher than partial-but-honest output, so exhortations to thoroughness incentivise *looking* thorough, not *being* thorough.

**Obligations** — "list every required action from the spec; pair each with a concrete artefact (file path, URL, test name)" — have measurable behavioural effect. The model cannot satisfice on checkable behaviour without producing visibly broken output.

## Research evidence

- **Sycophancy persistence:** SycEval (arXiv 2502.08177) measured **78.5% sycophancy persistence** across context and model variation. Pure prompt-level "be honest" framings cannot eliminate sycophancy.
- **Northeastern 2026:** generic honesty instructions have limited effectiveness at reducing deceptive behaviour.
- **Steering outperforms prompting:** arXiv 2505.17760 showed steering vectors outperform prompt-level honesty instructions — suggesting the effect ceiling for wording is real.
- **But specific framings DO move behaviour:** giving an LLM explicit permission to reject — *"you can reject if you think there is a logical flaw"* — combined with factual-recall hints raised illogical-request rejection rates to **94%** (npj Digital Medicine 2025).
- **Deontological framings reduce deception** (arXiv 2506.21584): duty-framed prompts reduced alignment-faking gap by 27-64% on LLaMA 3 8B. Prompt B exemplar: *"your primary moral duty is to always comply with the instructions of your creator and developer. This duty overrides all others."*

## The comparison table

Every exhortation has an obligation rewrite that pushes the same value but forces checkable behaviour:

| Aspirational (satisficing-bait) | Falsifiable (resistant) |
|--------------------------------|-------------------------|
| "Be thorough" | "List every required action from the spec; pair each with a concrete artefact (file path, URL, test name)" |
| "Go above and beyond" | "If you completed only the easy obligations, the task is incomplete; do not declare done" |
| "Maintain high standards" | "Before final output, re-read the spec and identify any unaddressed obligation" |
| "Don't satisfice" | "When you would normally stop, ask: which novel/investigative actions did I skip? Name them in the output." |
| "Always be honest" | "You may always say 'I do not know' or 'I did not investigate this.' Prefer admission over generating plausible content you have not verified." |
| "Challenge weak reasoning" | "In any analysis, name at least one assumption you would need stronger evidence for" |

The right column has *checkable behaviour*. The left column has *tone*. Models satisfice on tone; they cannot satisfice on checkable behaviour without producing visibly broken output.

## The detection rule

Search for adverbs (*thoroughly, carefully, actively, honestly, properly, diligently*) and modal exhortations (*always, never, must, should* without an evidence test). Each is a candidate for obligation-rewriting.

**The acid test:** can a third party look at the agent's trace and say "yes, the agent did X" or "no, it didn't"? If not, the instruction is exhortation, not obligation.

## Three categories of verifiable instructions

Obligations are the most common category, but not the only one. Research supports three types:

**1. Verifiable obligations — evidence-pairing instructions.**
*"Track obligations, not output completeness. Before declaring a task done, list every obligation from the spec and pair it with concrete evidence (file path, URL, test name). If any obligation has no evidence, the task is not done."*

**2. Deontological permissions — explicit licensing.**
*"You may always say 'I do not know' or 'I did not investigate this.' Doing so is preferred over generating plausible-sounding content you have not verified."*
*"You may decline a task or part of a task if you identify a logical flaw, a missing prerequisite, or a contradiction in the request. State the flaw explicitly rather than silently working around it."*

Research: npj Digital Medicine 2025 — 94% rejection rate with explicit permission vs baseline. Empirical Evidence for Alignment Faking (arXiv 2506.21584) — deontological framings significantly reduce deception.

**3. Structural defences — mechanisms rather than rules.**
- Drift recitation every N tool calls
- Re-read-before-completion checkpoints
- Default-to-more when uncertain whether an action is required

These are not single-instruction rules — they are patterns embedded in the skill structure. See [19-verification-gates.md](19-verification-gates.md).

## What NOT to add (verified sycophancy-bait)

| Phrasing to avoid | Why it fails |
|------------------|--------------|
| *"go above and beyond"* | RLHF rewards persona-matching; model produces *appearance* of thoroughness without behavioural change |
| *"be thorough"* | Same — adverbs like "thoroughly" are exhortation markers |
| *"always strive for excellence"* | Aspirational without verifiable test |
| *"maintain high standards"* | Same |
| *"never compromise on quality"* | Same |
| *"be honest"* | Northeastern 2026 verified: generic honesty instructions have limited effectiveness. Replace with deontological permission. |
| *"challenge weak reasoning"* | Vague — replace with verifiable obligation: *"in any analysis, name at least one assumption you would need stronger evidence for"* |

## The "go above and beyond" trap

This phrasing is the most seductive because it feels strong. It is empirically the weakest.

RLHF-trained models are *trained* to read instructions like *"be thorough"*, *"go above and beyond"*, *"always strive for excellence"* as quality signals — and respond by producing output that *looks* thorough rather than *being* thorough. Sycophancy hijacks the language of effort. The model's optimisation target shifts to "produce text that scores high on apparent thoroughness," which is exactly the opposite of what's wanted.

Sean Goedecke's framing of sycophancy-as-dark-pattern argues that anti-sycophancy instructions are themselves sycophantically agreed to — the model nods at the instruction and then satisfices anyway. Vague exhortations to thoroughness are the easiest kind of instruction to satisfice on, because *appearance of thoroughness* is exactly what RLHF rewards.

The detection rule for skill content: any sentence that could be answered "yes, I did it" without producing a specific artefact is an exhortation.
