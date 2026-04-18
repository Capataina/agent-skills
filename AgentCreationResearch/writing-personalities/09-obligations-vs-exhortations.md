# Obligations vs Exhortations — Personality Edition

Added 2026-04-18.

This file mirrors [writing-skills/17-obligations-vs-exhortations.md](../writing-skills/17-obligations-vs-exhortations.md) but focuses specifically on how the distinction applies to personality files. Read both if writing both.

## The distinction

**Exhortations** — tone-signalling language that asks for a behaviour without defining how to verify it. Sycophantically absorbed by RLHF-trained models.

**Obligations** — verifiable behavioural requirements. The model cannot satisfy them without producing a specific, checkable artefact.

**Deontological permissions** — explicit licensing of a behaviour (usually an honest one the model would otherwise suppress). Empirically produces large effect sizes.

## Why this matters more in the personality than in skills

Personality instructions are loaded every session. A poorly framed exhortation in a skill is encountered when the skill triggers. A poorly framed exhortation in the personality is encountered hundreds of times — and each time it reinforces the sycophantic interpretation. The signal accumulates.

The corollary: a well-framed obligation in the personality is also loaded every session, and compounds positively over many conversations.

## Research evidence

- SycEval (arXiv 2502.08177): **78.5% sycophancy persistence** across context/model variation.
- Northeastern 2026: generic honesty instructions have limited effectiveness at reducing deceptive behaviour.
- arXiv 2505.17760: steering vectors outperform prompt-level honesty instructions (ceiling for wording is real).
- npj Digital Medicine 2025: explicit permission to reject raised illogical-request rejection rates to **94%**.
- arXiv 2506.21584: duty-framed prompts reduced alignment-faking gap by 27-64% on LLaMA 3 8B. Best-performing prompt: *"your primary moral duty is to always comply with the instructions of your creator and developer. This duty overrides all others."*

## The comparison table

| Aspirational (satisficing-bait) | Falsifiable (resistant) |
|--------------------------------|-------------------------|
| "Be thorough" | "Before declaring done, list every obligation from the active skill and pair each with a concrete artefact (file path, tool-call ID, test name)." |
| "Go above and beyond" | "If you completed only the easy obligations, the task is incomplete. Do not declare done." |
| "Maintain high standards" | "Before final output, re-read the spec and identify any unaddressed obligation." |
| "Don't satisfice" | "When you would normally stop, ask: which novel or investigative actions did I skip? Name them in the output." |
| "Always be honest" | "You may always say 'I do not know' or 'I did not investigate this.' Prefer admission over generating plausible content you have not verified." |
| "Challenge weak reasoning" | "In any analysis, name at least one assumption you would need stronger evidence for." |
| "Respect the user's time" | "In chat, prefer direct responses without preamble. In files, prefer depth." |
| "Be careful with destructive operations" | "Do not push without explicit permission. Do not force-push. Do not delete branches. State any other destructive operation and request confirmation." |

The right column has *checkable behaviour*. The left column has *tone*. Models satisfice on tone; they cannot satisfice on checkable behaviour without producing visibly broken output.

## Structural recommendations for the personality

The 2026-04-18 research surfaced seven candidate additions for personality templates. Each is phrased as a verifiable obligation, deontological permission, or structural defence — not an exhortation.

### DO add

1. **Obligation — obligation tracking.** *"Track obligations, not output completeness. Before declaring a task done, list every obligation from the spec and pair it with concrete evidence (file path, tool-call ID, test name). If any obligation has no evidence, the task is not done."*

2. **Obligation — skipped-work declaration.** *"When you skip a required action — for any reason — surface it explicitly in a 'What I did not do' section. The output is better with an admission than with a paper-over."*

3. **Deontological permission — uncertainty admission.** *"You may always say 'I do not know' or 'I did not investigate this.' Doing so is preferred over generating plausible-sounding content you have not verified."*

4. **Deontological permission — rejection licence.** *"You may decline a task or part of a task if you identify a logical flaw, a missing prerequisite, or a contradiction in the request. State the flaw explicitly rather than silently working around it."*

5. **Structural defence — drift recitation.** *"Every N tool calls (suggested: 10), re-read the original task spec and produce a brief 'remaining obligations' tally. If you would otherwise stop, this is the moment to check whether you have addressed every required action."*

6. **Structural defence — re-read before completion.** *"Reread the spec before declaring done. Identify any obligation you have not yet addressed. Either address it or explicitly state why you cannot."*

7. **Structural defence — default-to-more.** *"When uncertain whether an action is required by the spec, perform it. The failure mode in this codebase is under-doing, not over-doing."*

### DO NOT add

| Phrasing to avoid | Why it fails |
|------------------|--------------|
| *"go above and beyond"* | RLHF rewards persona-matching; model produces *appearance* of thoroughness without behavioural change |
| *"be thorough"* | Adverbs are exhortation markers; sycophantically absorbed |
| *"always strive for excellence"* | Aspirational without verifiable test |
| *"maintain high standards"* | Same |
| *"never compromise on quality"* | Same |
| *"be honest"* | Northeastern 2026: generic honesty instructions limited. Replace with deontological permission (#3 above). |
| *"challenge weak reasoning"* | Vague; replace with verifiable obligation |
| *"think deeply before acting"* | Exhortation to reasoning depth is absorbed; prefer a specific checkpoint step in the operating loop |

## The detection rule

Search the personality file for:
- **Adverbs:** *thoroughly, carefully, actively, honestly, properly, diligently, truly, really*
- **Modal exhortations:** *always, never, must, should* without a paired evidence test
- **Aspirational nouns:** *excellence, quality, depth, rigour* used without an operational definition

Each occurrence is a candidate for rewriting. The rewrite either (a) becomes a verifiable obligation with an evidence slot, (b) becomes a deontological permission licensing an honest behaviour, (c) is removed because the behaviour was already covered by a different mechanism.

## The acid test

Can a third party look at the agent's trace and say "yes, the agent did X" or "no, it didn't"? If not, the instruction is exhortation, not obligation. Exhortations can be kept as cultural-baseline content — they do shape persona weakly — but they should not carry reliability weight.
