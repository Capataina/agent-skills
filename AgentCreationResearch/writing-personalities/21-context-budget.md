# Context Budget and Length

## The Research

- Claude Code's system prompt contains ~50 instructions. Adding a personality file adds to this total.
- Research suggests ~150-200 instructions is the reliable following limit for frontier models.
- Personality files beyond ~60-80 lines risk instruction dilution, where later instructions receive less attention.
- Prompt bloat research shows reasoning performance degrades at around 3,000 tokens of instruction.
- Chroma's context rot research (2025) found that every frontier model tested showed significant accuracy degradation on full-context prompts (~113k tokens) compared to focused prompts — length itself is harmful, not just irrelevance. Well-structured irrelevant context is more harmful than random noise.

## The Practical Approach

The personality file should be:

- **Short in the personality file itself** — only what applies broadly to every session.
- **Expansive in the files it points to** — skills, references, and context files carry the detailed instructions.
- **High signal density** — every line should pass the test: "Would removing this cause the agent to make mistakes?"

This does not mean the personality should be stripped to a skeleton. It means the personality should contain the *right* information at the *right* density. A 200-line personality file where every line shapes behaviour is better than a 50-line file that omits important guidance.

The key is offloading. Detailed instructions about *how to maintain context files* belong in the upkeep skill, not the personality. Detailed instructions about *how to write research papers* belong in the research skill. The personality says *when* to invoke these skills and *what role they play* — the skills themselves carry the detailed instructions.

## Budget Allocation Guidance

A rough budget model for a project with 5-8 skills:

| Component | Approximate Instruction Count |
|-----------|-------------------------------|
| Claude Code system prompt | ~50 (fixed) |
| Personality file | 40-80 |
| Loaded skill (when active) | 30-60 |
| **Total when skill is active** | **120-190** |

This leaves headroom within the ~150-200 reliable following limit. Exceeding the budget does not cause a hard failure — it causes gradual, uniform degradation in compliance quality. The most recently added instructions tend to degrade first.

## 2026-04-18 addition — Claude-specific numbers

Per IFScale (arXiv 2507.11538):
- Claude Opus 4: 44.6% joint compliance at **N=500 instructions**
- Claude Sonnet 4: 42.9%
- Claude 3.7 Sonnet: 52.7%

Newer Claude models are **worse** at dense-instruction compliance — not monotonic improvement.

Per AgentIF (arXiv 2505.16944): **ISR drops to ~0 past 6000 words of instructions** on all tested models. This cliff applies to the loaded content as a whole.

Implications for the budget model:
- The 40-80 personality + 30-60 skill budget translates to roughly ~3-6k words loaded at once — comfortably below the AgentIF cliff.
- Personality files above ~100 lines risk pushing into the cliff zone when a skill is loaded.
- For reliability-critical skills, the priority for budget space is: (1) identity and autonomy, (2) operating loop, (3) skill ecosystem coordination, (4) obligation audit / structural defences, (5) communication style recency anchor. Everything else is a candidate for offloading.

## Drift equilibrium and budget interaction

Drift is bounded, not runaway (Dongre 2025), but the equilibrium value depends on instruction count — denser personalities have higher baseline drift equilibria. Combining structural defences (operating loop + recitation) with budget discipline (personality <80 lines) produces the lowest equilibrium in practice.
