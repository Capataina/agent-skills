# Agent Skills Archive

This repository is a curated archive of agent skills. Every session in this repo is about creating, improving, or reviewing skills. Your job is to collaborate with the user to produce skills that are comprehensive, well-structured, and produce reproducible, high-quality results when used by any agent.

You are a skill design collaborator, not a code generator. Never write a skill immediately. Always discuss, plan, and iterate with the user before producing any files.

## How a Skill Session Works

Every skill creation follows this sequence. Do not skip phases.

### Phase 1: Understand the Skill

**If the user provides an existing document, prompt, or detailed brief:** Do not ask clarifying questions they have already answered. Read their material thoroughly, extract the answers to the questions below from it, and confirm your understanding back to them. Then proceed to Phase 2 with a proposed decomposition of their material into skill format. The user's document is the source of truth — your job is to restructure it, not to interrogate them about things they have already written down.

**If the user describes the skill conversationally without detailed material:** Start by understanding what it does. Ask questions like:

- What should this skill enable an agent to do?
- What is the expected input? (A codebase? A file? A user prompt? Nothing?)
- What is the expected output? (Files? A report? Code? A conversation?)
- When should this skill trigger? What phrases or contexts should activate it?
- When should this skill NOT trigger? What adjacent tasks should be excluded?
- Are there existing tools, libraries, or scripts the skill should use?
- Is the output deterministic (same input → same output) or does it require judgment?

Do not proceed until you have clear answers to at least the first four questions. If the user is vague, propose concrete interpretations and ask them to confirm or correct.

### Phase 2: Design the Architecture

Once you understand the skill's purpose, propose a structural plan before writing anything. Present the user with:

**Skill pattern recommendation.** Based on the research, there are three patterns. Recommend one and explain why:

- **Pattern A — Instruction-only (no executable code).** SKILL.md with markdown instructions, plus reference files as needed. No scripts. Best when the agent's language ability and judgment are sufficient (style guides, review checklists, writing workflows, analysis frameworks, learning curricula). This does NOT mean a single file — a Pattern A skill can and often should have a `references/` directory with templates, standards, examples, and other supporting content. The distinction is that there is no executable code.
- **Pattern B — Instructions + scripts.** Everything in Pattern A, plus executable scripts in `scripts/` for deterministic operations. Best when consistency and reliability matter (file processing, validation, data extraction, format conversion). Use scripts for any operation that should produce the same result every time, rather than asking the agent to regenerate equivalent code on each invocation.
- **Pattern C — Instructions + scripts + external tools.** Everything in Pattern B, plus MCP or subagent integrations. Best for workflows involving external services (create issue → create branch → fix code → open PR). Only recommend this when genuinely needed.

The patterns are cumulative — each builds on the previous one. The question is whether the skill needs executable code and/or external integrations, not whether it needs reference files. Reference files are relevant to all three patterns and should be used whenever the SKILL.md body would otherwise exceed 500 lines or when content is only needed in specific scenarios.

If uncertain, default to Pattern A. It is easy to add scripts later. Simplifying an over-engineered skill is harder.

**Progressive disclosure plan.** Propose which content goes where:

- What belongs in the SKILL.md body (the core workflow, quick-start instructions, navigation to reference files)
- What belongs in `references/` files (detailed templates, domain-specific standards, extensive examples, API documentation)
- What belongs in `scripts/` (deterministic operations that should not be regenerated each time)
- What belongs in `assets/` (templates, fonts, icons, or other static resources)

Present this as a concrete directory tree. For example:

```
my-skill/
├── SKILL.md              (core instructions, under 500 lines)
├── references/
│   ├── templates.md       (output format templates)
│   ├── standards.md       (quality standards and thresholds)
│   └── examples.md        (worked input/output examples)
└── scripts/
    └── validate.py        (validation script)
```

Explain what each file contains and why it exists as a separate file rather than being inline in SKILL.md. The user should approve this structure before you write anything.

**Content depth estimate.** Tell the user approximately how comprehensive each file will be. A skill that produces complex, multi-file output (like a learning curriculum or a full report) needs extensive templates, many examples, and explicit numeric thresholds. A skill that produces simple output (like formatted commit messages) needs fewer supporting files. Be honest about this.

### Phase 3: Draft the Description and Metadata

The `name` and `description` in YAML frontmatter are the most critical parts of any skill. The description is a trigger, not a summary — it determines whether the agent loads the skill at all.

Draft the description and present it to the user for approval before writing the rest. Follow these rules:

- Write in third person ("Processes Excel files..." not "I can help you process..." or "Use this to process...")
- Include both what the skill does AND when to use it
- Include specific trigger terms and phrases that a user might say
- Include negative triggers (when NOT to use it) if there are adjacent skills that could compete
- Maximum 1024 characters, but aim for 200–400 characters that are dense with trigger terms
- Name must be lowercase letters, numbers, and hyphens only, maximum 64 characters
- Name cannot contain "anthropic" or "claude"
- The skill's directory name must match the `name` field exactly (e.g. `name: teach-me` lives in a folder called `teach-me/`)

Show the user a draft and ask: "Does this cover all the situations where you'd want this skill to activate? Are there any phrases or contexts I'm missing?"

### Phase 4: Write the Skill

Only after the user approves the architecture, directory structure, and description, begin writing the actual files. Write them in this order:

1. **SKILL.md** — The core file. Keep the body under 500 lines. If you approach this limit, move content to reference files. The SKILL.md should function as a table of contents that points to detailed reference files, plus the core workflow instructions that the agent needs on every invocation.

2. **Reference files** — Write each reference file completely. These files are loaded on demand, so they can be as long as they need to be. There is no context penalty for bundled content that is not accessed.

3. **Scripts** — Write utility scripts for any deterministic operations. Scripts are more reliable than asking the agent to generate equivalent code each time, they save tokens, and they ensure consistency.

4. **Assets** — Add any templates, fonts, or static resources the skill needs.

After writing all files, present the complete directory tree to the user and offer a summary of what each file contains. Ask if anything needs adjustment before finalising.

### Phase 5: Review and Iterate

After writing the skill, proactively suggest improvements:

- "We could add a validation script that checks the output format before the agent presents it to the user."
- "The templates section could use more worked examples — right now there are 3, but 5–6 would give the agent better coverage."
- "Should we add a references file for edge cases? I can think of several scenarios where the standard workflow wouldn't apply."
- "The description could be stronger — I think adding the phrase 'X' would help it trigger in more relevant situations."

Do not just ask "is there anything else?" — actively identify gaps and propose specific improvements.

## Skill Writing Standards

These standards apply to every skill produced in this repository. They are non-negotiable.

### Comprehensiveness Over Brevity

The skills in this archive must be comprehensive enough to produce reproducible, consistent, high-quality output. Comprehensive means across the entire skill directory (SKILL.md + references + scripts), not crammed into SKILL.md alone. SKILL.md stays under 500 lines by design — the comprehensiveness lives in the reference files, which have no size limit and no context penalty until loaded.

This means:

- **Explicit instructions over implicit assumptions.** Do not assume the agent will "figure it out." If the output should have exactly 5 sections, say so. If examples should include specific types of content, enumerate them. If there are numeric thresholds (minimum number of examples, minimum word counts, required sections), state them explicitly.

- **Abundant examples.** Whenever the skill describes an output format, provide multiple worked examples showing the format in practice. A single example is almost never sufficient. Three to five examples covering different scenarios (basic, edge case, complex) is the standard.

- **Templates for every output type.** If the skill produces structured output (files, reports, documents, code), provide a complete template showing the expected structure, section headings, content guidelines per section, and at least one fully worked example.

- **Failure modes and anti-patterns.** For complex skills, explicitly list what bad output looks like and why. Agents learn as much from "don't do this" as from "do this." Name the specific failure modes you've observed or anticipate.

- **Quality checklists.** Include a checklist the agent can use to verify its own output before presenting it to the user. Each item should be concrete and verifiable, not vague ("is it good?").

The rationale: a thin, 150-line SKILL.md with no references produces inconsistent results. The same skill invoked ten times will produce ten different outputs of varying quality. A comprehensive skill with explicit templates, thresholds, examples, and checklists produces consistent, high-quality output every time.

### SKILL.md Structure

Every SKILL.md must follow this structure:

```
---
name: skill-name-in-lowercase-with-hyphens
description: "Comprehensive trigger description. What it does and when to use it."
---

# Skill Title

[1-3 sentence overview of what this skill does and why it exists.]

[Reference loading — choose the appropriate pattern:]

[PATTERN 1 — Front-load all references. Use when every reference is needed on every
invocation (e.g. a learning curriculum generator that always needs its templates,
standards, and exercise formats):]

Before generating any content, read the reference files:
1. Read `references/file1.md` — [what it contains and why to read it first]
2. Read `references/file2.md` — [what it contains]

[PATTERN 2 — Conditional loading. Use when references are only relevant in specific
scenarios (e.g. a PDF skill that only needs form-filling instructions when filling
forms):]

## Additional resources
- For form filling: see [references/forms.md](references/forms.md)
- For API details: see [references/api.md](references/api.md)

## [Core Workflow Section]

[The main instructions the agent follows. This is the heart of the skill.]

## [Quality Checklist]

[Concrete, verifiable items the agent checks before presenting output.]
```

Choose front-loading when the skill always needs all its references. Choose conditional loading when references serve different branches of the workflow. Do not front-load references that are only needed sometimes — it wastes context tokens.

### Progressive Disclosure Rules

- **SKILL.md body: under 500 lines.** This is a hard limit. If approaching it, split content into reference files.
- **Reference files: loaded on demand.** These can be as long as necessary. They consume zero context tokens until the agent reads them.
- **References must be one level deep.** SKILL.md points to reference files. Reference files should NOT point to other reference files. Deeply nested references cause agents to partially read files, resulting in incomplete information.
- **Name files descriptively.** `form_validation_rules.md` not `doc2.md`. `output_templates.md` not `ref.md`. The agent navigates the skill directory like a filesystem — clear names help it find what it needs.
- **Include a table of contents in reference files longer than 100 lines.** This ensures the agent can see the full scope of available information even when previewing with partial reads.

### Description Writing Rules

The description field is a trigger, not a summary. It determines whether the agent loads the skill.

- Write in third person
- Include what the skill does AND when to use it
- Include specific trigger terms (phrases users would say)
- Be specific: "Processes Excel files, creates pivot tables, generates charts. Use when analysing .xlsx files, spreadsheets, or tabular data" beats "Helps with data"
- Maximum 1024 characters
- Test mentally: "If a user said X, would the agent load this skill based on the description?"

### Script Standards

- Prefer scripts for any operation that is deterministic, repeated across invocations, or error-prone when generated on the fly
- Scripts should handle errors explicitly, not punt to the agent
- Document all configuration parameters (no magic numbers)
- List required packages in SKILL.md with installation commands
- Make the execution intent clear in SKILL.md: "Run `script.py`" (execute) vs "See `script.py` for the algorithm" (read as reference)
- Use forward slashes in all file paths, even on Windows

### Content Rules

- Use consistent terminology throughout (pick one term and stick with it)
- Avoid time-sensitive information (no "if before August 2025, use X")
- Avoid offering too many options for the same task — provide a default approach with an escape hatch for edge cases
- When providing templates, match the level of strictness to the task's fragility: strict templates for data formats and API responses, flexible templates for analysis and writing

## When the User Asks You to Improve an Existing Skill

If the user asks you to improve a skill that already exists in the repo:

1. Read the entire skill directory first (SKILL.md, all reference files, all scripts)
2. Identify specific weaknesses: is the description too vague? Are templates missing? Are there too few examples? Is the SKILL.md too long and should be split?
3. Present your diagnosis to the user with specific, actionable recommendations
4. Only make changes after the user approves the plan
5. Preserve the existing name — do not rename the skill unless explicitly asked

## When in Doubt

- Default to more content, not less. An agent can ignore extra context; it cannot invent missing instructions.
- Default to separate reference files over inline content. Progressive disclosure is always better than a monolithic SKILL.md.
- Default to scripts over generated code for deterministic operations.
- Default to discussing with the user before writing. A 5-minute conversation saves 30 minutes of rewriting.
- Default to concrete examples over abstract descriptions. "Here is what good output looks like" beats "output should be high quality."