# The Description — Trigger Engineering

## How Triggering Works

Skill triggering is pure LLM reasoning — no embeddings, no keyword matching, no classifiers. The agent reads the text description and decides whether it matches the user's intent. This means natural language quality directly determines activation accuracy.

Empirical data on description quality:

| Approach | Activation Success Rate |
|----------|------------------------|
| No optimisation | ~20% |
| Simple description | ~20% |
| Optimised description | ~50% |
| With trigger examples | 72-90% |

The gap between "optimised description" and "with trigger examples" is 22-40 percentage points. This makes the description the highest-leverage component of any skill.

> **2026-04-18 note on provenance:** The activation-rate table above was not located in primary Anthropic sources during verification. The qualitative claim — that descriptions are the highest-leverage component and that trigger-example inclusion substantially improves activation — is robustly supported by Anthropic's best-practices guidance. The specific percentages should be treated as heuristic rather than cited numbers until primary-source provenance is confirmed.

## Anatomy of an Effective Description

An effective description has four components:

1. **Capability statement** — what the skill does, in third person.
2. **Trigger conditions** — when to activate, with specific phrases and contexts.
3. **Negative triggers** — when NOT to activate, for adjacent skills.
4. **Assertive activation cue** — a direct instruction to use the skill in ambiguous cases.

## Scored Description Examples

**Weak (score: 2/10):**
> Helps with code quality.

Three words, no trigger terms, no activation conditions, no negative triggers. Would activate on nearly anything code-related or nothing at all.

**Adequate (score: 5/10):**
> Analyses a codebase for code health issues including dead code, unused dependencies, and complexity hotspots. Use when asked to audit or review code quality.

Covers the main use case. Missing: specific user phrases ("sweep for dead code," "find unused imports"), negative triggers, assertive cue.

**Strong (score: 9/10):**
> Repository-wide code health audit identifying dead code, unused dependencies, modularisation opportunities, hardcoded patterns extractable to algorithms, algorithm and performance optimisations, data layout and memory access wins, complexity hotspots, and missing or incomplete tests. Use when asked to audit, review, sweep, or clean up a codebase, find dead code, remove unused imports, simplify complex modules, or improve code quality. Not for feature development, bug fixing, or refactoring with changed behaviour.

Dense with trigger terms. Specific categories listed (an agent reading this knows exactly what the skill covers). Negative triggers exclude adjacent activities. A user saying "sweep for dead code" or "find unused imports" or "simplify complex modules" would all trigger this skill.

## Description Design Principles

1. **Write in third person.** "Analyses the codebase for..." not "I can help you..." The description is injected into the system prompt context; inconsistent point-of-view causes discovery problems.

2. **Include both WHAT and WHEN.** Two-part structure: capability statement + trigger conditions.

3. **Be dense with trigger terms.** Include the exact phrases users would say, file types, domain terms, and adjacent vocabulary. A user who says "sweep for dead code" should trigger the same skill as one who says "code health audit."

4. **Include negative triggers for adjacent skills.** "Not for product specs, roadmaps, release notes, changelogs, or general-purpose prose docs." This prevents false activations when another skill is more appropriate.

5. **Make descriptions slightly assertive.** Instead of "How to do X," write "How to do X. Make sure to use this skill whenever the user mentions Y, Z, or wants to W, even if they do not explicitly ask for X."

6. **Maximum 1024 characters, aim for 200-400 dense characters.** Every character should carry trigger signal.
