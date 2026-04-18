# What Personality Cannot Fix

Added 2026-04-18.

An honest section. The personality layer is powerful but bounded. Several failure modes cannot be fixed by personality *wording* — they require structural mechanisms. This file is about distinguishing the two, so authors don't write weaker and weaker exhortations when the real problem needs a different intervention.

## The reframe

**Personality wording cannot fix:**
- Mechanical attention decay (Mode 8 — instruction drift over tool-call count)
- Lost-in-the-Middle for middle-zone content (Mode 2)
- Curse-of-Instructions multiplicative decay (Mode 1)
- Tool-action asymmetry (Mode 5 — pretraining bias against WebSearch, Task dispatch, novel actions)
- Sycophantic absorption of vague exhortations (Mode 4 — "be thorough" fails)

**But personality is the correct installation point for structural defences against all five:**
- Operating loops (drift mitigation)
- Recitation / todo.md patterns (drift mitigation + middle-zone re-anchoring)
- Edge-placement rules (Lost-in-the-Middle mitigation)
- Instruction budget (Curse-of-Instructions)
- Tool-trace obligations / naming the bias (tool-action asymmetry)
- Verifiable obligations replacing exhortations (sycophancy)

The previous framing — "personality cannot fix X" — was too strong. The accurate version: **personality wording cannot defeat these modes, but the personality is the right home for structural mechanisms that DO defend against them.**

## Evidence

- **Drift (Mode 8).** Lee et al. COLM 2024 (arXiv 2402.10962) measured >30% persona-consistency degradation after 8 dialogue turns. Wording like "stay on task" is mechanically ineffective. But Dongre et al. 2025 (arXiv 2510.07777) measured 7-12% KL reduction from mid-session reminders at turns 4 and 7 — a structural mechanism embedded in the personality (operating loop, recitation) that produces the reminder.

- **Lost-in-the-Middle (Mode 2).** RoPE positional bias is an architectural phenomenon. Wording saying "pay attention to middle content" is a weak partial (Guo et al. 2024 ACL Findings — CoT prompting reduces but doesn't eliminate). But a personality rule that *"reference files must place imperatives at the start or end, never the middle"* is structural, installed at the personality layer, and defends against the mode.

- **Curse of Instructions (Mode 1).** IFScale (arXiv 2507.11538) showed multiplicative compliance decay operates on instruction *count*. Adding personality instructions about "following every instruction" makes the curse worse, not better. But a personality that establishes an instruction budget (~100-150 total across personality + loaded skills) structurally limits the count.

- **Tool-action asymmetry (Mode 5).** BiasBusters (arXiv 2510.00307) measured 20x pretraining-frequency effect — tool selection is at the weight level, not the prompt level. Wording saying "call WebSearch more" is weak. But a personality that names the bias explicitly as a pretraining artefact (*"you will feel pulled toward Read/Edit and away from WebSearch — this is a training-distribution artefact, not a judgement"*) combined with a structural mechanism (PreToolUse hook, forced tool calls, tool-trace exit gate) can defend against it.

- **Sycophancy (Mode 4).** SycEval (arXiv 2502.08177) found 78.5% sycophancy persistence across context/model variation. Generic "be honest" framings have limited effectiveness (Northeastern 2026). But *specific* personality framings produce measurable change: deontological permissions raised illogical-request rejection rates to 94% (npj Digital Medicine 2025).

## The right division of labour

| Layer | Role | Example |
|-------|------|---------|
| **Personality (CLAUDE.md)** | Cultural baseline + verifiable obligations + anti-sycophancy posture + structural-defence installation | *"Success = obligations met with concrete evidence, not output looking done. Before declaring done, enumerate every obligation and mark done/skipped/partial. You may always admit skipped work."* |
| **Skill (SKILL.md + references)** | Task-specific enforcement structure | Numbered obligation checklist with evidence slots, tool gating, verification subagent, mid-skill reminders |
| **Runtime infrastructure (hooks, subagents)** | Out-of-loop verification | Stop hook that greps the transcript for required tool invocations |

**Personality alone** gets you nicely-stated good intentions the model satisfices on.
**Skill structure alone** gets you compliance without judgement (the model executes the checklist mechanically without caring why).
**Infrastructure alone** is expensive overhead without behavioural framing.

The pattern that works: personality sets the value, skill enforces the behaviour, infrastructure splits the load when the skill gets too large.

## The "go above and beyond" trap

RLHF-trained models are *trained* to read instructions like *"be thorough"*, *"go above and beyond"*, *"always strive for excellence"* as quality signals — and respond by producing output that *looks* thorough rather than *being* thorough. Sycophancy hijacks the language of effort.

Any personality language addressing reliability must be **specific and falsifiable**, not aspirational. See [09-obligations-vs-exhortations.md](09-obligations-vs-exhortations.md) for the comparison table and full treatment.

## The acid test

For every instruction in the personality, ask:

> "Can a third party look at the agent's trace and say 'yes, the agent did X' or 'no, it didn't'?"

If yes: the instruction is a verifiable obligation and will produce behavioural change.
If no: the instruction is exhortation. Either rewrite it as an obligation, or acknowledge that it is cultural-baseline content with weaker effect.

Both are valid in the personality, but an author who thinks exhortations are strong reliability tools will be repeatedly disappointed.
