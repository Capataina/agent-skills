# Instruction Craft for Personalities

## What Makes Instructions the Agent Actually Follows

**Clarity and directness matter more than emphasis.** Claude 4.6 is more responsive to system prompts than previous models. Aggressive language ("CRITICAL: You MUST...") can cause overtriggering. Normal prompting ("Use this tool when...") is more reliable. Reserve emphasis for the genuinely inviolable constraints — if everything is emphasised, nothing is (see Emphasis Overuse in the failure catalogue).

**Positive framing over negative constraints.** Instead of "Do not use shallow bullet lists," write "Use the representation that makes the information clearest." The agent generalises from positive examples better than negative prohibitions. Research on the "Pink Elephant Problem" has an architectural explanation: in attention-based models, the embedding for "not A" has a cosine similarity of 0.792 with "A" — the model literally represents "don't do X" almost identically to "do X" in embedding space (CVPR 2024 Workshop).

**Context and motivation behind instructions.** Explaining *why* enables generalisation. Instead of "Never use ellipses," write "Your response will be read aloud by a text-to-speech engine, so never use ellipses since the engine cannot pronounce them." The agent now avoids all unpronounceables, not just ellipses.

**Examples over rules.** "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." Include 3-5 examples for best results. One well-chosen example teaches more than a paragraph of abstract rules.

**Instruction count matters.** Research suggests frontier LLMs can follow approximately 150-200 instructions with reasonable consistency. Claude Code's own system prompt already contains ~50 instructions, leaving ~100-150 for the personality file and loaded skills combined. As count increases, following quality decreases uniformly. Every instruction must earn its place.

## The Compounding Effect

Everything from the skill writing research about instruction framing applies to personalities, with one critical addition: personality instructions are read at the start of *every* session, so framing issues compound. A single poorly framed instruction in a skill is encountered only when that skill triggers. A poorly framed instruction in the personality is encountered hundreds of times.

The paper "What Prompts Don't Say" (2025) found that specifying all requirements simultaneously **backfires** — with 19 requirements, accuracy drops to 85% from a 98.7% baseline. The Sonar Foundation Agent case study showed a clear progression: a prescriptive two-stage workflow achieved 58% efficacy, a freer workflow reached 70%, and distilling to a concise, principle-based prompt with extended thinking reached 75%. These findings compound in personalities because the personality is always loaded.

## The Golden Rule

> "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too."

## Personality-Specific Framing Checks

- **Startup instructions should enable, not prohibit.** "Read context/ and README.md first for fast orientation; pull additional files when the task requires them" is better than "Do not read learning/ at startup. Do not explore code at startup."
- **Mode instructions should be flexible.** "Ask the user whether they want teaching or implementation; if their message already makes it clear, confirm and proceed" is better than "Ask exactly this question and stop."
- **Upkeep instructions should describe the responsibility, not the procedure.** "Keep context/ and learning/ current throughout the session by making proportionate updates when the project changes" is better than a detailed list of every allowed action.

## 2026-04-18 addition — Verifiable obligations, deontological permissions, not exhortations

Research from R2 and R4 establishes that personality instructions split into three categories by empirical effect:

**Verifiable obligations** — instructions with a concrete evidence test — produce measurable behavioural change. *"Before declaring any task complete, enumerate every obligation from the active skill and mark each as done/skipped/partial."*

**Deontological permissions** — explicit licensing of a behaviour — produce large effect sizes. npj Digital Medicine 2025: explicit permission to reject raised illogical-request rejection rates to **94%** baseline. Example: *"You may always say 'I do not know' or 'I did not investigate this.' Doing so is preferred over generating plausible-sounding content you have not verified."*

**Vague exhortations** — *"be thorough", "go above and beyond", "always strive for excellence"* — are sycophantically absorbed with negligible behavioural effect. RLHF rewards the appearance of thoroughness, which exhortations explicitly optimise for. The model nods at the exhortation and satisfices anyway.

**Detection rule:** search the personality for adverbs (*thoroughly, carefully, actively, honestly*) and modal exhortations (*always, never, must, should* without an evidence test). Each is a candidate for obligation-rewriting.

See [09-obligations-vs-exhortations.md](09-obligations-vs-exhortations.md) for the full treatment and comparison table.
