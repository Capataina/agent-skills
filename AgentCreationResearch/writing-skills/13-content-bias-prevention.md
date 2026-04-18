# Content Quality and Bias Prevention

A well-structured skill can still produce poor agent output if the *content* within that structure has quality issues. Structure is the skeleton; content is the muscle. Both must be right.

## Domain Bias in Examples

Examples are the single strongest influence on agent output — and the single biggest source of unintentional bias. Research confirms this is not hypothetical:

Research on in-context learning consistently shows that models replicate the surface patterns of their examples — vocabulary, domain, structural format — rather than extracting the abstract principle the examples were meant to illustrate. If every example in a skill references machine learning, the agent will anchor on ML patterns when working on a web app, because the example domain leaks into the agent's understanding of the task itself.

The landmark paper "Rethinking the Role of Demonstrations" (Min et al., EMNLP 2022) demonstrated that what examples primarily teach is **format, distribution, and label space** — not content. Ground truth labels barely matter. What matters is the surface structure, vocabulary, and domain of the examples. This means domain bias in examples leaks directly into the agent's understanding of the task itself.

Further research on **induction heads** (Olsson et al., 2022) shows that attention mechanisms literally "replicate previous patterns for next-token prediction" — the model copies demonstration patterns rather than extracting underlying principles. **Surface form competition** means multiple terms referring to the same concept fight for probability mass, so the specific vocabulary in examples directly biases output vocabulary.

**The test:** Read every example in the skill and ask: "If an agent read only these examples, would it think this skill is designed for one specific kind of project?" If yes, the examples need diversification.

**The standard:** Examples across a skill should span at least 2-3 different domains (web services, data pipelines, CLI tools, desktop applications, infrastructure, etc.). No single domain should represent more than half the examples in any file.

**Template examples are highest risk.** Templates are used as direct structural patterns. If a template's worked example uses domain-specific names (like `reinforcement-learning-path.md` or `replay-buffer.rs`), agents will produce output shaped by that domain even when working on something completely different.

## Instruction Coherence

Instructions within a skill must not contradict each other. Research shows this matters more than you might expect:

The paper "LLMs can be easily Confused by Instructional Distractions" (2025) tested six models and found that competing instruction signals cause accuracy on the intended task to fall as low as 30% in some configurations. When instructions compete with each other for the agent's attention, compliance on all instructions degrades — not just the contradicting pair.

The paper "The Instruction Gap" (2025) found that **instruction compliance and accuracy are independent dimensions** — models that follow all instructions don't necessarily provide accurate answers, and accurate models may struggle with instruction compliance. This means a contradicting instruction can degrade compliance broadly without visibly breaking any single output.

Common contradiction patterns:

- A principle section says "use your judgement to choose the best format" but a later section says "always use bullet lists for this section."
- The SKILL.md says "create files only when justified" but a reference file provides templates that imply files should always be created.
- One reference says "keep it concise" while another says "be exhaustive and comprehensive."

**The test:** For each instruction, search the skill for any instruction that could be read as contradicting it. Pay special attention to instructions in different files — contradictions across files are harder to spot and there are **no existing tools for multi-file prompt coherence checking** (this is entirely manual work today).

## Terminology Drift

Research on prompt sensitivity (2024) provides hard numbers: **"A slight change in a class definition can lead to drastic changes in the final prediction."** Sensitivity values ranged from 0.005 to 0.404 across models. The mechanism is **surface form competition** — when multiple terms refer to the same concept, they fight for probability mass in the model's output distribution, fragmenting attention and producing inconsistent output.

Common drift patterns:

- "System file" vs "system document" vs "system doc" — same thing, three names.
- "Plan file" vs "execution plan" vs "implement-now file" — same thing, three names.

**The test:** List every important concept in the skill. For each one, search the entire skill directory for all terms used to reference it. If there are multiple terms, pick one and standardise. Check terminology against other skills in the ecosystem — a concept that appears in multiple skills should use the same term everywhere.

## Stale Internal References

When a skill's structure changes (folders renamed, files moved, concepts reorganised), internal references may not all get updated. No tools exist to detect this automatically.

**The test:** After any structural change, search the entire skill directory for the old name or concept. Every occurrence must be updated.

## Instruction Framing Quality

Every instruction in the skill should be evaluated:

- **Does it explain *why*?** An instruction with reasoning produces generalised understanding. An instruction without reasoning produces rote compliance.
- **Is it framed positively?** Lead with what to do. Add what not to do as context, not as the primary instruction.
- **Does it use proportionate emphasis?** Reserve ALWAYS/NEVER for genuinely inviolable constraints. For everything else, explain the reasoning.

## Autonomy-Restricting Language

The Sonar Foundation Agent case study (2025) provides direct evidence: a prescriptive two-stage workflow achieved **58% efficacy**, a freer workflow reached **70%**, and distilling to a concise, principle-based prompt with extended thinking reached **75%** — both architectural freedom and prompt conciseness contributed independently.

The IFScale benchmark (2025) quantifies instruction saturation: the strongest reasoning model tested (o3) achieved only **62.8% accuracy at 500 instructions**. Models show three distinct degradation patterns: *threshold decay* (reasoning models maintain near-perfect compliance until ~150 instructions, then crash), *linear decay* (frontier models like Claude Sonnet 4 degrade steadily), and *exponential decay* (smaller models collapse to 7-15% accuracy floors). Beyond saturation, models shift overwhelmingly toward **omission errors** — they abandon instructions entirely rather than partially complying.

The paper "What Prompts Don't Say" (2025) found a critical paradox: specifying all requirements simultaneously **backfires** — with 19 requirements specified, accuracy drops to 85% from a 98.7% baseline.

Scan every instruction for language that unnecessarily restricts agent creativity:

- "Must always" / "must never" — is this genuinely inviolable, or would a principle with reasoning be better?
- "Exactly 5 sections" / "maximum 3 files" / "between 100-200 words" — is this numeric limit structural or arbitrary?
- "These sections should not exist" / "never create these files" — is there a scenario where the agent's judgement should override this?

## Arbitrary Limits and When to Avoid Them

Rigid limits (word counts, file counts, section counts, character limits) constrain agent autonomy without improving output quality. They are appropriate only when:

- The limit is structural (SKILL.md under 500 lines — a context engineering constraint).
- The limit prevents a known failure mode (plan file accumulation — a proven anti-pattern).
- The limit is a floor, not a ceiling (minimum 30 non-empty lines for system docs — a shallow-document detector).

Instead of numeric limits, state the principle and the failure mode:

| Numeric limit (weaker) | Principle + failure mode (stronger) |
|------------------------|-------------------------------------|
| Maximum 3 plan files. | Plans are temporary execution aids. Remove them when complete. Do not let stale plans accumulate. |
| Sections must be 100-200 words. | Each section should carry enough information to be useful. If it can be said in one line, say it in one line. If it needs a page, give it a page. |
| These sections must not exist. | Avoid vague catch-all sections. Every section should have a clear topic and canonical home. |

## Exhortation vs Obligation (2026-04-18 addition)

Research from the verification pass (SycEval 2502.08177, Northeastern 2026, arXiv 2505.17760, npj Digital Medicine 2025) establishes a sharp distinction:

**Exhortations** — "be thorough", "go above and beyond", "always strive for excellence", "don't satisfice" — are sycophantically absorbed by RLHF-trained models. The model nods at the exhortation and satisfices anyway, because RLHF rewards the *appearance* of thoroughness, which exhortations explicitly optimise for.

**Obligations** — "list every required action from the spec; pair each with a concrete artefact (file path, URL, test name)" — have measurable behavioural effect. The model cannot satisfice on checkable behaviour without producing visibly broken output.

**Deontological permissions** — "you may decline if you identify a logical flaw" — raised illogical-request rejection rates to 94% in one study (npj Digital Medicine). Explicit permission outperforms exhortation.

**Detection rule:** search the skill for adverbs (*thoroughly, carefully, actively, honestly*) and modal exhortations (*always, never, must, should* without an evidence test). Each is a candidate for obligation-rewriting. The acid test: can a third party look at the agent's trace and say "yes, the agent did X" or "no, it didn't"? If not, the instruction is exhortation, not obligation.

See [17-obligations-vs-exhortations.md](17-obligations-vs-exhortations.md) for the full treatment and comparison table.
