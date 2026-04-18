# Hard Rules

These are inviolable constraints with structural justification. They are not preferences or guidelines — violating any of them produces measurably worse results.

## Rule 1: Every token is loaded every session

The personality file is loaded at the start of every conversation. Unlike skills (loaded on demand) or reference files (loaded when needed), the personality consumes context budget permanently. This is a context engineering constraint, not a stylistic preference.

**Implication:** Every line in the personality must pass the test: "Does this need to shape behaviour in every session, or only when a specific task triggers?" If only when a specific task triggers, it belongs in a skill.

## Rule 2: Identity and role MUST be first

The primacy effect is one of the most robust findings in LLM instruction-following research. The agent attends most strongly to the first instructions it encounters. Identity and role definition activate the right reasoning mode — they frame every instruction that follows.

**Implication:** The first section of any personality file is always identity, role, and the autonomy grant. No preamble, no table of contents above it, no administrative metadata.

## Rule 3: The personality never contains detailed "how to" that belongs in skills

This is the personality-skill boundary. The personality says *when* and *what* — when to invoke a skill, what role it plays, what triggers justify it. Skills say *how* — the detailed process, templates, standards, and quality checks. Violating this boundary wastes context budget every session on content that is only relevant when a specific skill triggers, and creates drift risk when the skill is updated but the personality copy is not.

**The test:** For each instruction in the personality, ask: "Is this about when to do something (personality's job) or how to do it (skill's job)?" If it is about "how," it belongs in the skill.

## Rule 4: Only the personality references skill names

Skills are self-contained specialists. They do not know about other skills. They reference artefact patterns ("plan files in context/plans/"), not skill names. Only the personality references skill names, because only the personality is the coordinator. This prevents circular dependencies and ensures skills remain portable.

## Rule 5: Quality standards and communication style near the end

The recency effect means the agent attends strongly to the last instructions it reads before responding. Quality standards and communication style placed at the end of the personality act as recency anchors — they shape every response because they are the freshest instructions in attention.

**Implication:** Do not bury communication style in the middle. Do not place quality checklists early. These belong at the end, exploiting recency.

## 2026-04-18 addendum — Rule 6: Structural defences belong in the personality

Research from R5 (Anthropic Persona Selection Model, arXiv 2506.21584, Manus context engineering) establishes that personality wording cannot defeat several failure modes — mechanical attention decay, Lost-in-the-Middle for middle-zone content, Curse-of-Instructions multiplicative decay, tool-action asymmetry, sycophantic absorption of vague exhortations. But the personality **is the correct installation point for structural defences that mitigate these** — operating loops, recitation patterns, edge-placement rules, obligation tracking, tool-trace obligations.

**Implication:** when the personality encounters a mode it cannot fix by wording, the right response is to install a structural mechanism, not to write stronger exhortations.

See [08-what-personality-cannot-fix.md](08-what-personality-cannot-fix.md) and [10-structural-defences.md](10-structural-defences.md).
