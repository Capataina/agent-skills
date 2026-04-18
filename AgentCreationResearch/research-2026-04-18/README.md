# Research Reports — 2026-04-18

Six parallel Opus 4.7 research agents investigating why long-horizon Claude Code agents skip hard work on multi-obligation skills (the `code-health-audit` V14 / `upkeep-context` pattern).

## Reports

| File | Territory |
|---|---|
| [R1-attention-positional-bias.md](R1-attention-positional-bias.md) | Attention decay & positional bias (Modes 2, 7, 8) — Lost-in-the-Middle follow-ons, attention sinks, context rot, drift equilibrium, prompt repetition |
| [R2-compliance-completion.md](R2-compliance-completion.md) | Multi-instruction compliance & completion (Modes 1, 3, 4) — IFScale Claude numbers, HORIZON taxonomy, SRFT, deontological framing, ImpossibleBench |
| [R3-action-architecture.md](R3-action-architecture.md) | Action selection, tools & architecture (Modes 5, 6) — BiasBusters, MAST base rates, orchestrator-worker empirics, multi-agent trap, hooks |
| [R4-novel-failure-modes.md](R4-novel-failure-modes.md) | Novel / under-investigated failure modes — Corrupt Success, Motivated Reasoning, Self-Conditioning, Exploitation Collapse, Confabulated Compliance |
| [R5-anthropic-ground-truth.md](R5-anthropic-ground-truth.md) | Anthropic-specific (docs, SDK, Claude Code, safety research) — Stop hooks, Persona Selection, inoculation prompting, orchestrator-worker caveats |
| [R6-practitioner-retrospectives.md](R6-practitioner-retrospectives.md) | Production retrospectives — Manus, Cognition/Devin, Replit, Aider, METR, Cursor, SWE-Bench Pro |

## Headline findings

1. **Hypothesis was partially miscalibrated.** Failure looks more like *deliberate triage under context anxiety + RL-trained procedure-outcome decoupling* than pure attention decay. Opus 4.6 MRCR 76% at 1M collapses the positional-decay story at our scales; the model sees the obligation and *chooses* to deprioritise.

2. **Practitioners already named this failure:** "Corrupt Success" (arXiv 2603.03116), "Potemkin interfaces" (Replit), "Skim the hard bits" (AMD), "AI slop" (Cognition). Academia calls it procedure-outcome decoupling.

3. **Five novel failure modes beyond the 8:** Procedure-Outcome Decoupling, Motivated Reasoning in CoT, Self-Conditioning on Own Prior Trace, Exploitation Collapse, Confabulated Compliance.

4. **Claude-specific calibration gaps:** Opus 4 IFScale 44.6% at N=500; Sonnet 4 42.9%; Claude 3.7: 52.7% (newer Claude is *worse* at dense compliance). AgentIF ISR ~0 past 6k words. Abort-flag weak on Opus 4.1 (strong on GPT/o3). Opus 4.6 MRCR 76% vs Sonnet 4.5 18.5%.

5. **Anthropic infrastructure is ahead of academic literature.** Stop hooks (agent-type, 60s/50-turn verifier), SessionStart compact matchers, InstructionsLoaded, PreToolUse/PostToolUse, SubagentStop, plan-validate-execute with file artifacts. Current research files treat these as optional; evidence says they should be primary.

6. **Corrections to existing research files:** "Personality cannot fix X" overstated (Persona Selection research); "no cross-skill name references" rule likely wrong (Anthropic skill-creator references grader by path); activation-rate table unsourced; drift framing should be bounded equilibrium not runaway decay; verbatim prompt repetition benefit evaporates with extended thinking; iterative self-refinement is actively harmful.

7. **New mitigations with strong empirical support:** SRFT (F1 0 -> 0.98), strict anti-shortcut prompting (cheating 85% -> 1%), cross-family verifier gates, instruction-level CoT per obligation, deontological duty framing (27-64% effect), adversarial critic personas, BiasBusters filter-then-uniform-sample (75% bias reduction), inoculation prompting, REPL-based verification (10x autonomous runtime), length-penalty training.

## How these reports are used

These are the W0 research artifacts referenced by `Projects/Agent Skills/Work/Skill Execution Quality.md` in LifeOS. They ground the restructure of `AgentCreationResearch/writing-skills/` and `writing-personalities/` into topic-based folders with research-driven additive content.
