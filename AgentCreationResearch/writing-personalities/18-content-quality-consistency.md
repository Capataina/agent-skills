# Content Quality and Consistency

## The Personality-Skill Boundary

The most common content quality issue in personality files is scope creep — the personality accumulates detailed "how to" instructions that belong in skills. Research shows why this matters:

1. **Context bloat degrades everything.** Chroma's research (2025) tested 18 frontier models and found that every single one gets worse as input length increases — performance on full-context prompts (~113k tokens) was significantly lower than on focused prompts (~300 tokens) across all model families. Notably, well-structured irrelevant context is *more* harmful than random noise, because structural coherence makes distractors compete more effectively for attention. The personality is loaded every session. Every token of detailed skill-level instruction in the personality degrades the agent's performance on every task, even when those instructions are irrelevant.

2. **Instruction conflicts cause broad degradation.** The paper "LLMs can be easily Confused by Instructional Distractions" (2025) found that competing instruction signals can cause accuracy on the intended task to fall as low as 30% in some configurations. When the personality says "do X this way" and the skill says "do X that way," compliance degrades across *all* instructions, not just the conflicting pair.

3. **Instruction saturation is real.** The IFScale benchmark (2025) found that even the strongest reasoning model (o3) achieved only 62.8% accuracy at 500 instructions. Models show three degradation patterns: *threshold decay* (reasoning models maintain near-perfect compliance until ~150, then crash), *linear decay* (frontier models degrade steadily), and *exponential decay* (smaller models collapse to 7-15% floors). Claude Code's own system prompt already contains ~50 instructions. The personality and loaded skills share the remaining budget. Every instruction in the personality that could be in a skill is wasting a slot in this limited budget.

**The principle:** The personality should say *when* and *what* — when to invoke a skill, what role it plays, what triggers justify it. The skills should say *how* — the detailed process, templates, standards, and quality checks.

**The test:** For each instruction in the personality, ask: "Is this about when to do something (personality's job) or how to do it (skill's job)?" If it is about "how," it probably belongs in the skill.

## Consistency Across the Personality-Skill Ecosystem

The personality and all skills must present a consistent worldview:

- **Same terminology.** If the personality calls them "plan files," no skill should call them "implement-now files."
- **Same folder model.** If the personality describes a `notes/` folder, no skill should still reference `decisions/`.
- **Same philosophical stance.** If the personality says "depth is a virtue, not a problem," no skill should instruct the agent to "keep it brief."
- **Same formatting philosophy.** If the personality encourages rich markdown (tables, diagrams, trees), no skill should restrict the agent to bullets.

## The Consistency Verification Method

Read the personality, then read each skill it references. For each pair, check:

1. Do they use the same terms for the same concepts?
2. Do they agree on folder structure and file locations?
3. Do they agree on quality standards and depth expectations?
4. Does the personality's description of the skill match what the skill actually does?
5. Are there instructions in both that could conflict?

Any mismatch is a quality defect. The fix is always to align them — typically by updating the less-recently-revised document to match the more-recently-revised one.

## 2026-04-18 addition — Claude-specific IFScale calibration

Per IFScale 2025 for Claude models:
- Claude Opus 4: 44.6% joint compliance at N=500
- Claude Sonnet 4: 42.9%
- Claude 3.7 Sonnet: 52.7%

Newer Claude models are **worse** at dense-instruction compliance. The personality and loaded skills share the instruction budget — typical rough limit ~100-150 instructions before joint compliance drops below 50% on current Claude. Every instruction in the personality that could be principled or structural (not rule-based) is a win against the instruction budget.

AgentIF (arXiv 2505.16944): **ISR drops to ~0 past 6,000 words of instructions** on all tested models. This cap applies to the *loaded* content, so the personality plus any loaded skills must stay under this threshold.

Implication: ruthlessly purge anything from the personality that could live in a skill, and ruthlessly purge from skills anything the agent already knows.
