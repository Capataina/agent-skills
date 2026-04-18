# Writing Skills — Index

The definitive reference for evaluating, writing, and improving agent skills. Answers one question comprehensively: **what does a well-written skill look like at every level of detail?**

This is not a process document. It does not describe the steps for creating a skill (that lives in the project's CLAUDE.md). It describes what makes a skill well-written, how to evaluate one, what patterns to follow, what failures to avoid, and how to test quality.

## Reading order

The files are numbered for a linear read-through, but every file is self-contained. Navigate by topic for a specific task.

| File | When to read |
|------|-------------|
| [01-purpose.md](01-purpose.md) | First time in this folder; orienting new contributors. |
| [02-foundational-principles.md](02-foundational-principles.md) | Before writing or evaluating any skill. The philosophical commitments that inform every specific rule. |
| [03-hard-rules.md](03-hard-rules.md) | Before starting any skill. Six inviolable structural constraints with justification. |
| [04-trigger-engineering.md](04-trigger-engineering.md) | When writing or scoring the YAML description. Highest-leverage component of any skill. |
| [05-instruction-craft.md](05-instruction-craft.md) | When writing the body of SKILL.md or any reference file. Three instruction tiers, scenario-list anti-pattern, emphasis calibration, positive framing. |
| [06-progressive-disclosure.md](06-progressive-disclosure.md) | When deciding what goes in SKILL.md vs references. The three-level loading system and the 6000-word cliff. |
| [07-reference-architecture.md](07-reference-architecture.md) | When designing the skill's folder structure. One-level-deep rule, naming, granularity. |
| [08-writing-reference-content.md](08-writing-reference-content.md) | When filling in a reference file. Depth calibration, universal applicability, taxonomies, templates. |
| [09-formatting-standards.md](09-formatting-standards.md) | When structuring a file. Canonical SKILL.md structure, markdown patterns, header conventions. |
| [10-example-design.md](10-example-design.md) | When adding or reviewing examples. Overfitting risk, diversity principles, worked comparisons. |
| [11-failure-catalogue.md](11-failure-catalogue.md) | When diagnosing a misbehaving skill. F1-F14 catalogue of named failure modes. |
| [12-quality-assurance.md](12-quality-assurance.md) | When writing the quality checklist at the end of SKILL.md. Obligation vs quality rubric distinction. |
| [13-content-bias-prevention.md](13-content-bias-prevention.md) | When reviewing a skill for bias, contradictions, terminology drift, autonomy restriction. |
| [14-cross-skill-coherence.md](14-cross-skill-coherence.md) | When a skill lives in a multi-skill ecosystem. Coherence dimensions and the personality-as-coordinator principle. |
| [15-scoring-rubric.md](15-scoring-rubric.md) | When evaluating a skill. 12-dimension rubric with concrete criteria. |
| [16-testing-validation.md](16-testing-validation.md) | After writing or editing a skill. Mental dry-run, edge cases, post-writing verification passes. |
| [17-obligations-vs-exhortations.md](17-obligations-vs-exhortations.md) | When writing any imperative. The distinction that dominates reliability: verifiable behaviour vs tone. |
| [18-claude-specific-calibration.md](18-claude-specific-calibration.md) | When designing a skill that will run on Claude specifically. Per-version behaviour numbers, context anxiety, cross-family findings that don't transfer. |
| [19-verification-gates.md](19-verification-gates.md) | When a skill has non-negotiable obligations that the agent will be tempted to skip. Four-tier verification model. |
| [20-tool-action-patterns.md](20-tool-action-patterns.md) | When a skill has obligations requiring tools the agent is biased against (WebSearch, Task dispatch, writing new tests). |
| [21-orchestrator-worker.md](21-orchestrator-worker.md) | When considering splitting a skill across multiple agents. When multi-agent helps and when it hurts. |
| [22-infrastructure-mechanisms.md](22-infrastructure-mechanisms.md) | When designing reliability infrastructure around a skill. Claude Code hooks, subagent frontmatter, plan-validate-execute. |
| [23-sources.md](23-sources.md) | When citing research or extending the material. |

## Provenance

This folder was restructured from a single 1251-line monolith on 2026-04-18, informed by six parallel Opus 4.7 research passes. Files `01`-`16` are migrated from the original monolith with content preserved. Files `17`-`22` are new, added from the 2026-04-18 research. See `../research-2026-04-18/` for the source reports.

## Companion folders

- [`../writing-personalities/`](../writing-personalities/) — how to write personality / CLAUDE.md files
- [`../writing-subagents.md`](../writing-subagents.md) — subagent configuration (still monolithic; smaller scope)
- [`../research-2026-04-18/`](../research-2026-04-18/) — the raw research reports from R1-R6
