# Hard Rules

Hard rules are inviolable structural constraints. They exist because violating them causes measurable degradation in agent performance, context efficiency, or ecosystem coherence. Each rule includes its justification — the *why* is as important as the *what*, because understanding the justification helps evaluators distinguish genuine violations from edge cases.

Hard rules are distinct from guidelines. A guideline can be overridden by good judgement. A hard rule cannot.

## The Rules

| # | Rule | Justification |
|---|------|---------------|
| 1 | **SKILL.md body must remain under 500 lines.** | Context engineering constraint. The SKILL.md body loads into context every time the skill triggers. Beyond 500 lines, token cost degrades performance on unrelated reasoning. Comprehensiveness lives in reference files, which load on demand. |
| 2 | **References are one level deep.** SKILL.md points to reference files. Reference files do not point to other reference files. | When references nest, agents partially read files (using `head -100` or similar), resulting in incomplete information. A two-level chain means the agent may never reach the terminal content. |
| 3 | **Description must be under 1024 characters.** | Descriptions load for every installed skill at every conversation start. Long descriptions waste tokens on skills that do not trigger. Aim for 200-400 characters dense with trigger terms. |
| 4 | **Reference files over 100 lines must have a table of contents at the top.** | Agents preview long files with partial reads. Without a table of contents, the agent cannot see the full scope of available information and may miss critical sections. |
| 5 | **No cross-skill name references.** Skills must not reference other skills by name. Reference artefact patterns instead. | Only the personality/coordinator knows the full skill ecosystem. Skills are specialists that do not know about each other. Name references create coupling and break when skills are renamed. |
| 6 | **Each skill is self-contained within its directory.** | A skill must have everything it needs to function without depending on files outside its directory (except standard tools and the agent's built-in capabilities). External dependencies create fragile coupling. |

> **2026-04-18 update:** Rule 5 should be softened in practice — Anthropic's own `skill-creator` references its grader subagent by path. See [15-cross-skill-coherence.md](15-cross-skill-coherence.md) for the refined position. Within a coordinated skill family, shared paths are acceptable; the prohibition is on ad-hoc coupling between unrelated skills.

## How to Mark Hard Rules Within a Skill

Hard rules within a skill's own instructions should be visually distinct. Use a dedicated section near the end of SKILL.md (before the quality checklist) with a clear header like "Inviolable Rules" or "Structural Constraints." Do not scatter hard rules throughout the body — they get lost in surrounding guidelines and the agent may treat them as suggestions.
