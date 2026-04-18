# Writing Personalities — Index

The quality evaluation bible for agent personality files (CLAUDE.md, system prompts, custom instructions). Defines what good looks like at every level of detail — from overall structure to individual sentence craft.

If you read this folder and nothing else, you should know exactly how to evaluate a personality file, what patterns produce strong results, what failures to watch for, and how to test whether a personality works.

## Reading order

| File | When to read |
|------|-------------|
| [01-purpose-and-scope.md](01-purpose-and-scope.md) | First time in this folder. What a personality file is and is not. |
| [02-hard-rules.md](02-hard-rules.md) | Before writing any personality. Six inviolable structural constraints. |
| [03-structure-ordering.md](03-structure-ordering.md) | When laying out the file. Primacy-recency, recommended section order, concrete line-number guidance. |
| [04-instruction-craft.md](04-instruction-craft.md) | When writing individual instructions. Positive framing, emphasis calibration, instruction count. |
| [05-control-autonomy.md](05-control-autonomy.md) | When setting the autonomy level. Constraint-permission asymmetry. |
| [06-autonomy-calibration.md](06-autonomy-calibration.md) | When writing the autonomy grant. Intern-vs-engineer test. |
| [07-section-writing-patterns.md](07-section-writing-patterns.md) | When writing specific personality sections — identity, version control, parallelisation, upkeep, proactive improvement, notes, operating loop, engineering standards, skill ecosystem, decision support. |
| [08-what-personality-cannot-fix.md](08-what-personality-cannot-fix.md) | Before writing reliability-critical instructions. Which failure modes wording cannot defeat, and why personality is the installation point for structural defences. |
| [09-obligations-vs-exhortations.md](09-obligations-vs-exhortations.md) | When writing any imperative. The distinction that dominates reliability in personality files. |
| [10-structural-defences.md](10-structural-defences.md) | When failure modes cannot be fixed by wording. Operating loops, recitation, edge-placement, obligation audits, tool-bias naming. |
| [11-startup-routines.md](11-startup-routines.md) | When designing what the agent does at session start. |
| [12-failure-catalogue.md](12-failure-catalogue.md) | When diagnosing a misbehaving personality. 11 named failure modes with fixes. |
| [13-skill-ecosystem-coordination.md](13-skill-ecosystem-coordination.md) | When the personality coordinates multiple skills. |
| [14-source-hierarchies-loops.md](14-source-hierarchies-loops.md) | When writing the source hierarchy and operating loop sections. |
| [15-communication-style.md](15-communication-style.md) | When writing the communication / output norms section. |
| [16-instruction-persistence.md](16-instruction-persistence.md) | When designing for long-session reliability. Primacy-recency, content vs structural persistence, bounded drift equilibrium. |
| [17-multi-personality-coordination.md](17-multi-personality-coordination.md) | When splitting into implementation / teaching variants. |
| [18-content-quality-consistency.md](18-content-quality-consistency.md) | When auditing personality-skill ecosystem coherence. |
| [19-scoring-rubric.md](19-scoring-rubric.md) | When evaluating a personality. 11-dimension rubric. |
| [20-testing-validation.md](20-testing-validation.md) | After writing or editing. Mental dry-run, scenario testing, post-writing verification. |
| [21-context-budget.md](21-context-budget.md) | When checking length and density. Claude-specific IFScale numbers, 6000-word cliff. |
| [22-context-anxiety.md](22-context-anxiety.md) | When the personality will run on Sonnet 4.5 or the agent needs to survive long tasks. |
| [23-completion-honesty.md](23-completion-honesty.md) | When the personality is the coordinator for reliability-critical work. Five patterns for honest completion reporting. |
| [24-sources.md](24-sources.md) | When citing research or extending the material. |

## Provenance

This folder was restructured from a single 1159-line monolith on 2026-04-18, informed by six parallel Opus 4.7 research passes. Files `01`-`18` migrate the original monolith content. Files `19`-`23` include both migration and additive material from research. Files `08`, `09`, `10`, `22`, `23` are entirely new from research. See `../research-2026-04-18/` for the source reports.

## Companion folders

- [`../writing-skills/`](../writing-skills/) — how to write individual skills
- [`../writing-subagents.md`](../writing-subagents.md) — subagent configuration (still monolithic)
- [`../research-2026-04-18/`](../research-2026-04-18/) — the raw research reports from R1-R6
