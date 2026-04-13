# Agent Skill Quality Evaluation Bible

The definitive reference for evaluating, writing, and improving agent skills. This document answers one question comprehensively: **what does a well-written skill look like at every level of detail?**

This is not a process document. It does not describe the steps for creating a skill (that lives in the project's CLAUDE.md). It describes what makes a skill well-written, how to evaluate one, what patterns to follow, what failures to avoid, and how to test quality.

## Table of Contents

1. [Purpose of This Document](#1-purpose-of-this-document)
2. [Foundational Principles](#2-foundational-principles)
3. [Hard Rules](#3-hard-rules)
4. [The Description — Trigger Engineering](#4-the-description--trigger-engineering)
5. [Instruction Craft](#5-instruction-craft)
6. [Progressive Disclosure and Context Engineering](#6-progressive-disclosure-and-context-engineering)
7. [Reference File Architecture](#7-reference-file-architecture)
8. [Writing Rich Reference Content](#8-writing-rich-reference-content)
9. [Formatting and Notation Standards](#9-formatting-and-notation-standards)
10. [Example Design](#10-example-design)
11. [Anti-Patterns and Failure Catalogue](#11-anti-patterns-and-failure-catalogue)
12. [Quality Assurance Design](#12-quality-assurance-design)
13. [Content Quality and Bias Prevention](#13-content-quality-and-bias-prevention)
14. [Cross-Skill Coherence](#14-cross-skill-coherence)
15. [Scoring Rubric](#15-scoring-rubric)
16. [Testing and Validation](#16-testing-and-validation)
17. [Post-Writing Verification](#17-post-writing-verification)
18. [Sources](#18-sources)

---

## 1. Purpose of This Document

Every skill produced or reviewed in this repository should be evaluated against the principles, rules, rubrics, and patterns in this file. If a reviewer reads this document and nothing else, they should be able to:

- Identify whether a description will trigger correctly in edge cases.
- Evaluate whether instructions are worded for generalisation or rote compliance.
- Detect domain bias, terminology drift, instruction contradictions, and structural violations.
- Score a skill across ten quality dimensions with concrete, observable criteria.
- Design a test plan for validating a skill before deployment.

The document is long by design. It is a reference — read the sections relevant to your current evaluation task.

---

## 2. Foundational Principles

These are the philosophical commitments that inform every specific rule and recommendation in this document. They are not optional — they are the foundation on which quality evaluation rests.

### The Agent Is Already Smart

The single most important design principle: **modern LLMs are already extremely capable.** Every piece of information in a skill should pass the challenge: "Does the agent really need this, or is it something the agent already knows?" Do not explain what PDFs are. Do not teach software engineering fundamentals. The skill's job is to provide what the agent *cannot* derive from its training — your specific conventions, your specific quality standards, your specific edge cases, and the reasoning behind them.

This does not mean skills should be thin. It means every token should carry signal. A 500-line SKILL.md where every line teaches the agent something it would not otherwise know is better than a 100-line SKILL.md padded with obvious instructions and a 200-line SKILL.md that wastes half its tokens restating common knowledge.

There is a counterweight to this principle: research from "What Prompts Don't Say" (2025) found that unspecified requirements are **2× as likely to regress** across model updates (5.9% vs 3.0% regression rate). Relying on the model to "figure it out" works today but may break on the next model version. The principle is not "omit everything the agent knows" — it is "omit the obvious, but explicitly state your specific quality standards and conventions, because those are what break silently when models change."

### Explain Why, Not Just What

Anthropic's own skill-creator captures this principle precisely:

> "Try hard to explain the **why** behind everything you're asking the model to do. Today's LLMs are *smart*. They have good theory of mind and when given a good harness can go beyond rote instructions and really make things happen."

When you explain *why* something matters, the agent generalises from the explanation. It can handle edge cases you never anticipated because it understands the underlying principle. When you only say *what* to do, the agent follows the letter of the instruction and may violate the spirit in novel situations.

| Version | Instruction | Why It's Better/Worse |
|---------|-------------|----------------------|
| Weak | Always use bullet lists for system document sections. | Rigid. Agent uses bullets even when a table or diagram would be clearer. |
| Strong | Use the representation that makes the information clearest. Bullets work for concise takeaways, tables for dense inventories, diagrams for flows that are awkward in prose. The goal is maximum clarity for both human readers and future agents. | Principled. Agent chooses the best representation for each situation because it understands the goal. |

### The Bridge and Field Analogy

Calibrate instruction specificity based on risk:

- **Narrow bridge (high risk, one safe path):** Database migrations, file format specifications, API contracts. Provide exact instructions. The agent has no latitude because getting it wrong is catastrophic.
- **Open field (low risk, many valid paths):** Analysis, writing, creative exploration, code structure decisions. Provide direction and quality standards. The agent has full latitude because many good solutions exist.

Most of the content in this archive's skills falls on the "open field" end. The structural rules (folder layout, naming conventions, file roles) are narrow bridges. The content within those structures (how to explain a subsystem, what depth to reach, what visual representations to choose) is open field.

### Structure Fixed, Content Free

This principle directly follows from the bridge-and-field analogy. In skill design:

- **Fix the structure:** Folder layout, file naming, required sections, output locations, script execution order. These are deterministic and must be consistent.
- **Free the content:** How the agent explains things, what depth it reaches, what formatting it chooses, how it reasons about the domain. These are judgement calls where agent autonomy produces better results than rigid templates.

Research directly supports this split. A 2024 study ("Let Me Speak Freely?") found that **stricter format constraints cause 10–15% performance degradation on reasoning tasks** — forcing format compliance during reasoning interferes with the reasoning itself. The mechanism: when the model must simultaneously reason about the problem and comply with format restrictions, the format constraints consume cognitive capacity that would otherwise go to the actual task. This is why fixing structure at the skill level (folder layout, file naming) works — it is decided before reasoning begins — while constraining content within the output harms quality.

**Evaluation test:** For every instruction in a skill, ask: "Is this fixing structure or constraining content?" If it constrains content without a clear failure-mode justification, it should be rewritten as a principle or removed.

---

## 3. Hard Rules

Hard rules are inviolable structural constraints. They exist because violating them causes measurable degradation in agent performance, context efficiency, or ecosystem coherence. Each rule includes its justification — the *why* is as important as the *what*, because understanding the justification helps evaluators distinguish genuine violations from edge cases.

Hard rules are distinct from guidelines. A guideline can be overridden by good judgement. A hard rule cannot.

### The Rules

| # | Rule | Justification |
|---|------|---------------|
| 1 | **SKILL.md body must remain under 500 lines.** | Context engineering constraint. The SKILL.md body loads into context every time the skill triggers. Beyond 500 lines, token cost degrades performance on unrelated reasoning. Comprehensiveness lives in reference files, which load on demand. |
| 2 | **References are one level deep.** SKILL.md points to reference files. Reference files do not point to other reference files. | When references nest, agents partially read files (using `head -100` or similar), resulting in incomplete information. A two-level chain means the agent may never reach the terminal content. |
| 3 | **Description must be under 1024 characters.** | Descriptions load for every installed skill at every conversation start. Long descriptions waste tokens on skills that do not trigger. Aim for 200–400 characters dense with trigger terms. |
| 4 | **Reference files over 100 lines must have a table of contents at the top.** | Agents preview long files with partial reads. Without a table of contents, the agent cannot see the full scope of available information and may miss critical sections. |
| 5 | **No cross-skill name references.** Skills must not reference other skills by name. Reference artefact patterns instead. | Only the personality/coordinator knows the full skill ecosystem. Skills are specialists that do not know about each other. Name references create coupling and break when skills are renamed. |
| 6 | **Each skill is self-contained within its directory.** | A skill must have everything it needs to function without depending on files outside its directory (except standard tools and the agent's built-in capabilities). External dependencies create fragile coupling. |

### How to Mark Hard Rules Within a Skill

Hard rules within a skill's own instructions should be visually distinct. Use a dedicated section near the end of SKILL.md (before the quality checklist) with a clear header like "Inviolable Rules" or "Structural Constraints." Do not scatter hard rules throughout the body — they get lost in surrounding guidelines and the agent may treat them as suggestions.

---

## 4. The Description — Trigger Engineering

### How Triggering Works

Skill triggering is pure LLM reasoning — no embeddings, no keyword matching, no classifiers. The agent reads the text description and decides whether it matches the user's intent. This means natural language quality directly determines activation accuracy.

Empirical data on description quality:

| Approach | Activation Success Rate |
|----------|------------------------|
| No optimisation | ~20% |
| Simple description | ~20% |
| Optimised description | ~50% |
| With trigger examples | 72–90% |

The gap between "optimised description" and "with trigger examples" is 22–40 percentage points. This makes the description the highest-leverage component of any skill.

### Anatomy of an Effective Description

An effective description has four components:

1. **Capability statement** — what the skill does, in third person.
2. **Trigger conditions** — when to activate, with specific phrases and contexts.
3. **Negative triggers** — when NOT to activate, for adjacent skills.
4. **Assertive activation cue** — a direct instruction to use the skill in ambiguous cases.

### Scored Description Examples

**Weak (score: 2/10):**
> Helps with code quality.

Three words, no trigger terms, no activation conditions, no negative triggers. Would activate on nearly anything code-related or nothing at all.

**Adequate (score: 5/10):**
> Analyses a codebase for code health issues including dead code, unused dependencies, and complexity hotspots. Use when asked to audit or review code quality.

Covers the main use case. Missing: specific user phrases ("sweep for dead code," "find unused imports"), negative triggers, assertive cue.

**Strong (score: 9/10):**
> Repository-wide code health audit identifying dead code, unused dependencies, modularisation opportunities, hardcoded patterns extractable to algorithms, algorithm and performance optimisations, data layout and memory access wins, complexity hotspots, and missing or incomplete tests. Use when asked to audit, review, sweep, or clean up a codebase, find dead code, remove unused imports, simplify complex modules, or improve code quality. Not for feature development, bug fixing, or refactoring with changed behaviour.

Dense with trigger terms. Specific categories listed (an agent reading this knows exactly what the skill covers). Negative triggers exclude adjacent activities. A user saying "sweep for dead code" or "find unused imports" or "simplify complex modules" would all trigger this skill.

### Description Design Principles

1. **Write in third person.** "Analyses the codebase for..." not "I can help you..." The description is injected into the system prompt context; inconsistent point-of-view causes discovery problems.

2. **Include both WHAT and WHEN.** Two-part structure: capability statement + trigger conditions.

3. **Be dense with trigger terms.** Include the exact phrases users would say, file types, domain terms, and adjacent vocabulary. A user who says "sweep for dead code" should trigger the same skill as one who says "code health audit."

4. **Include negative triggers for adjacent skills.** "Not for product specs, roadmaps, release notes, changelogs, or general-purpose prose docs." This prevents false activations when another skill is more appropriate.

5. **Make descriptions slightly assertive.** Instead of "How to do X," write "How to do X. Make sure to use this skill whenever the user mentions Y, Z, or wants to W, even if they do not explicitly ask for X."

6. **Maximum 1024 characters, aim for 200–400 dense characters.** Every character should carry trigger signal.

---

## 5. Instruction Craft

This section covers the literal sentence-level craft of writing instructions — how word choices, framing patterns, and emphasis affect agent behaviour. This is the most impactful area for quality improvement because subtle wording differences produce large behavioural differences.

### Three Tiers of Instruction Wording

Instructions fall into three tiers, each with a distinct wording pattern:

**Tier 1 — Constraints (inviolable structural rules):**
Imperative voice, no hedging, structural justification attached.

| Weak | Strong |
|------|--------|
| Try to keep SKILL.md short. | SKILL.md must remain under 500 lines. This is a context engineering constraint — the body loads every time the skill triggers, and token cost beyond 500 lines degrades reasoning on unrelated tasks. |
| References shouldn't be too nested. | Reference files must not point to other reference files. When references nest, agents partially read files, resulting in incomplete information. |

**Tier 2 — Guidelines (recommended practices with reasoning):**
Recommendation with quantified reasoning. The agent understands the trade-off and can make exceptions when justified.

| Weak | Strong |
|------|--------|
| Use a few examples. | 3–5 examples is the optimal range. Below 3, the agent lacks diversity to generalise. Above 5, token cost outweighs quality gains. Research shows major improvements after 2 examples and a plateau around 4–5. |
| Keep checklists reasonable. | A simple skill needs 5–8 checklist items. A complex skill might need 12–15. Beyond 15, attention dilutes and omission errors increase (IFScale research: models shift to omission beyond saturation). |

**Tier 3 — Principles (direction with freedom):**
A goal statement that the agent can pursue through whatever means it judges best.

| Weak | Strong |
|------|--------|
| Make the output good. | Use the representation that makes the information clearest — tables for comparisons, trees for hierarchies, diagrams for flows, prose for narratives. The goal is maximum clarity for the reader. |
| Be thorough but not too long. | Every section should carry enough information to be useful on its own. If it can be said in one line, say it in one line. If it needs a page, give it a page. Depth should match the judgement involved, the variation across projects, and the cost of mistakes. |

**Evaluation test:** For every instruction in a skill, identify which tier it belongs to. If a Tier 2 guideline is worded like a Tier 1 constraint (imperative, no hedging), it will over-constrain the agent. If a Tier 1 constraint is worded like a Tier 3 principle (vague direction), it will be ignored when it matters most.

### The Scenario-List Anti-Pattern

This is the single most impactful failure pattern discovered in practice. It deserves thorough treatment because it is pervasive, subtle, and produces behaviour that looks like agent disobedience but is actually instruction-following taken literally.

**The pattern:** When instructions include specific examples of when to apply a behaviour, the agent treats the examples as an exhaustive list. If the current situation does not match one of the listed scenarios, the agent skips the behaviour entirely.

**Example — the failing instruction:**

> After completing a task, fixing a bug, or finishing a meaningful chunk of work, commit your changes with a descriptive message.

What happens: The agent completes a refactoring (not a "task," "bug fix," or "meaningful chunk" in its interpretation) and does not commit. It finishes writing documentation and does not commit — documentation was not in the list. It reorganises imports and does not commit. The three scenarios became the complete universe of commit-worthy events.

**Why it happens:** LLMs are pattern-matchers. When they see a list of specific scenarios, they interpret that list as defining the scope of the instruction. The instruction "commit after X, Y, or Z" is parsed as "commit if and only if X, Y, or Z." The "or" is read as exclusive rather than illustrative. This is consistent with research on instruction-following — agents comply with the literal text, and a list of conditions is literal text defining when the behaviour applies.

**The fix:** State the principle and the default stance, then describe only what PREVENTS the behaviour, not what triggers it.

| Failing Version | Fixed Version |
|----------------|---------------|
| After completing a task, fixing a bug, or finishing a meaningful chunk of work, commit your changes with a descriptive message. | Commit early and often. The only constraint is: never push to a remote without explicit permission. |
| When you encounter a naming inconsistency, a dead import, or a formatting issue during your work, fix it immediately. | Fix incidental quality issues as you encounter them. Do not ignore small problems because they are not the current task. The only exception is when a fix would change behaviour in code you are not currently testing. |
| If the user asks for help, wants to discuss architecture, or needs debugging assistance, engage conversationally. | Default to conversational engagement. The only time to skip conversation is when the user has given an explicit, unambiguous command that requires no clarification. |

**The structural pattern of the fix:**

1. State the default behaviour as the norm (commit, fix, engage).
2. State what prevents or constrains the behaviour (no push, no behaviour-changing fixes, no skipping when ambiguous).
3. Do NOT list scenarios that trigger the behaviour — the default stance means it is always on.

**How to detect it during evaluation:** Search the skill for instructions containing comma-separated scenarios ("after X, Y, or Z," "when you encounter A, B, or C," "if the user asks for D, E, or F"). Each one is a candidate for the scenario-list anti-pattern. Ask: "Would the agent skip this behaviour in a situation not listed?" If yes, rewrite using the default-stance pattern.

### Quality Bars vs. Procedures

Quality bars describe the standard the output must meet. Procedures describe the steps to produce the output. Quality bars produce better agent output because they empower the agent to find the best path to the standard. Procedures constrain the agent to a specific path that may not be optimal for the current situation.

| Type | Example |
|------|---------|
| Quality bar | Every finding must include evidence from the actual code, not assumptions about what the code probably does. |
| Procedure | Read lines 1–100 of each file, then check for unused imports, then check for dead functions, then... |
| Quality bar | The description must activate correctly for any reasonable phrasing of the skill's core use case. |
| Procedure | Write five trigger phrases, test each one, then add negative triggers for adjacent skills. |

**When procedures are appropriate:** When the operation is deterministic and the agent cannot derive the correct sequence from principles alone (script execution order, file creation sequence where later files depend on earlier ones, API call chains). These are narrow-bridge situations.

**When quality bars are appropriate:** Everything else — analysis, writing, evaluation, creative work, judgement calls. These are open-field situations where the agent's reasoning about how to meet the bar will outperform a prescribed procedure.

**Evaluation test:** For every procedural instruction in a skill, ask: "Could this be replaced with a quality bar that the agent could meet through its own reasoning?" If yes, the procedure is over-constraining.

### Emphasis Calibration

Research on emphasis (2024) found that **small open-source LLMs struggle to understand emphasised text**, while commercial LLMs **may overinterpret emphasised text**. Stricter format constraints generally lead to greater performance degradation in reasoning tasks.

From Anthropic's skill-creator:

> "If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag — if possible, reframe and explain the reasoning so that the model understands why the thing you're asking for is important."

**Calibration guide:**

| Emphasis Level | When Justified | When Harmful |
|----------------|----------------|--------------|
| **CAPS + bold** (e.g., "NEVER push without permission") | Genuinely inviolable safety or data integrity constraints. Actions that cannot be undone. | Stylistic preferences, recommended practices, anything the agent could reasonably override with good judgement. |
| **Bold only** (e.g., "must remain under 500 lines") | Structural constraints from hard rules. Constraints with measurable degradation if violated. | Soft recommendations. Anything where "usually" or "typically" would be more honest. |
| *Italics* (e.g., "why it matters") | Drawing attention to reasoning, principles, or key concepts within flowing text. | Not harmful, but overuse dilutes the signal. |
| Plain text | Everything else. The vast majority of instructions should be plain text with reasoning. | Never harmful on its own, but a skill written entirely in plain text with no emphasis may bury its most critical rules. |

**The over-emphasis failure mode:** When a skill uses CAPS and bold liberally, the agent treats everything as equally critical. This is equivalent to nothing being critical. The agent cannot distinguish genuinely inviolable constraints from emphatic preferences, so it either over-complies (rigid, conservative output) or abandons some constraints entirely (IFScale omission errors).

**Evaluation test:** Count the number of CAPS/bold emphasis instances in a skill. If more than 3–5 across the entire skill directory, the emphasis is diluted. Each instance should be a genuine hard rule.

### Framing: Positive Over Negative

Research consistently shows positive framing outperforms negative framing. The "Pink Elephant Problem" has an architectural explanation: research presented at CVPR 2024 found that in attention-based models, the embedding for "not A" has a cosine similarity of **0.792** with "A" but only **0.273** with the intended meaning — the model literally represents "don't do X" almost identically to "do X" in embedding space. A 2025 study across 9 models found larger models handle negation substantially better (Spearman correlation 0.867 between model size and negation accuracy), but the fundamental representation problem persists. Anthropic's official documentation explicitly advises telling the agent what to do rather than what not to do.

| Negative (weaker) | Positive (stronger) |
|--------------------|---------------------|
| Do not use shallow bullet lists. | Use the representation that makes the information clearest — tables, diagrams, trees, or bullets depending on the content. |
| Never create thin files. | Every file should carry enough memory value that a reader understands the topic without needing to re-derive it from code. |
| Don't repeat information across files. | Each piece of information has one canonical home. Other files reference it by path rather than restating it. |
| Avoid vague section headers. | Every section header should tell the reader what they will learn by reading that section. |

**When negative framing is appropriate:** When the positive instruction alone is insufficient because the failure mode is non-obvious. In these cases, lead with the positive instruction and add the negative as context:

> Use the representation that makes the information clearest. Note: agents frequently default to bullet lists even when a table would be far more readable for comparative data — actively consider alternatives before choosing bullets.

### Consistent Terminology

Using "case," "ticket," and "issue" interchangeably confuses agents, especially as conversation length increases. Research on prompt sensitivity (2024) provides hard numbers: **"A slight change in a class definition can lead to drastic changes in the final prediction."** Sensitivity values ranged from 0.005 to 0.404 across models. The mechanism is **surface form competition** — when multiple terms refer to the same concept, they fight for probability mass, fragmenting attention and producing inconsistent output.

**Evaluation test:** List the 5–10 most important concepts in the skill. Search the entire skill directory for all terms used to reference each one. If any concept has multiple terms, flag it. Pick one and standardise.

### Instructions That Persist

LLMs exhibit a primacy-recency effect — they attend most to information at the beginning and end of context. Instructions in the middle of long interactions get progressively less attention. To combat this:

- Place the most critical rules early in the SKILL.md body.
- Use the quality checklist at the end as a recency anchor for important requirements.
- The agent's own note-taking (plans, progress tracking) pushes objectives into recent attention.

**Evaluation test:** Identify the 3 most important behavioural instructions in the skill. Are they in the first quarter of SKILL.md or the quality checklist? If they are buried in the middle, they will degrade over long conversations.

---

## 6. Progressive Disclosure and Context Engineering

### The Three-Level Loading System

Skills use progressive disclosure to manage context efficiently:

| Level | What Loads | When | Token Cost |
|-------|-----------|------|------------|
| 1 — Metadata | Name + description | Always at startup | ~100 tokens per skill |
| 2 — SKILL.md body | Core workflow instructions | When skill triggers | Under 5k tokens |
| 3 — Reference files | Detailed standards, templates, examples | On explicit demand | As needed |

This means you can have many skills installed without impacting performance on unrelated tasks. The cost is paid only when the skill activates.

### Context Is a Finite Resource

As token count in the context window increases, the model's ability to accurately recall information decreases proportionally (Chroma Research, "Context Rot," 2025). Every token has a cost — not in money, but in attention. This means:

- Do not front-load reference files that are only needed sometimes. Use conditional loading.
- Do not repeat the same information in multiple reference files.
- Do front-load references that are always needed. If every invocation requires all references, say so and load them all.

### Mandatory-Core vs. Task-Based Conditional Loading

Reference files fall into two categories:

| Category | Description | Loading Instruction |
|----------|-------------|---------------------|
| **Mandatory-core** | Files needed for every invocation of the skill, regardless of task. | "Read these files immediately after SKILL.md loads." List them explicitly and unconditionally. |
| **Task-based conditional** | Files needed only for specific tasks or phases. | "Read this file when [specific condition]." The condition must be concrete and unambiguous. |

**Failure mode:** Listing all reference files sequentially without marking which are mandatory vs. conditional causes the agent to read only the first few (observed in practice — agents given a list of 10 files to read often stop at 3). The fix is explicit categorisation with clear loading triggers.

**Evaluation test:** Count the reference files listed in SKILL.md's loading instructions. If more than 3–4 are listed without clear conditional triggers, the agent will under-load. Mark mandatory files distinctly (e.g., in a separate section or with explicit "always read" language).

### Just-In-Time Context

Rather than pre-loading all context, maintain lightweight pointers (file paths, section references) and let the agent load detailed information on demand. This mirrors how humans work — we do not memorise entire reference manuals, we know where to look.

The skill should tell the agent what each reference file contains and when to read it, so the agent can decide what it needs for the current task. A one-line summary per reference file is sufficient:

> `references/analysis-categories.md` — Taxonomy of finding categories with definitions, boundary rules, and examples. Read before classifying findings.

---

## 7. Reference File Architecture

### When to Split vs. Keep Inline

| Keep in SKILL.md | Split to reference files |
|-------------------|------------------------|
| Core workflow instructions | Detailed templates |
| Quick-start information | Domain-specific standards |
| Navigation to reference files | Extensive examples and worked scenarios |
| Inviolable rules section | Category taxonomies |
| Quality checklist | Format specifications |

**Hard rule:** SKILL.md body under 500 lines. This is a structural constraint, not a content constraint — the comprehensiveness lives in the reference files.

### Critical Rule: One Level Deep

Reference files must not point to other reference files. SKILL.md points to reference files. Reference files are terminal. When references nest, agents partially read files (using `head -100` or similar), resulting in incomplete information. A two-level chain means the agent may never reach the terminal content.

### Table of Contents in Long References

For reference files longer than 100 lines, include a table of contents at the top. This ensures the agent can see the full scope of available information even when previewing with partial reads. The table of contents should list every major section with a brief (3–8 word) description.

### Naming

Name files descriptively. The agent navigates the skill directory like a filesystem — clear names help it find what it needs without reading the file.

| Weak | Strong |
|------|--------|
| ref2.md | analysis-categories.md |
| doc.md | output-format.md |
| templates.md | finding-template.md |
| misc.md | edge-cases-and-boundaries.md |

### File Granularity

Each reference file should cover one coherent topic. If a file covers two unrelated topics, split it — the agent may load it for one topic and get distracted by the other. If two files cover overlapping topics, merge them — the agent may load only one and miss information from the other.

**Evaluation test:** For each reference file, state its topic in one sentence. If the sentence requires "and" to connect two unrelated topics, the file should be split. If two files have sentences that overlap significantly, they should be merged.

---

## 8. Writing Rich Reference Content

This is the hardest part of skill creation. Designing the folder structure is straightforward. Writing a 400-line reference file that is comprehensive, domain-agnostic, teaches through reasoning, and gives the agent freedom without losing quality — that is the craft.

### Calibrating Depth

Not every reference file needs the same depth. The right depth depends on three factors:

1. **How much judgement is involved.** A category taxonomy where the agent must decide which bucket a finding goes in needs extensive definitions, boundary guidance, and examples. A file naming convention where there is one right answer needs a short list.

2. **How much variation exists across projects.** A reference that must work for Rust game engines, Python data pipelines, and TypeScript web apps needs more examples and more principle-based reasoning than one designed for a specific stack. Universal applicability demands depth because you cannot rely on shared assumptions.

3. **How costly mistakes are.** The evidence-and-justification reference in a code health audit needs extreme depth because a poorly justified finding wastes an engineer's time and erodes trust. A file naming reference can be brief because naming mistakes are cheap to fix.

**The heuristic:** If an agent reading this reference file and nothing else could produce output that meets the skill's quality checklist, the file is deep enough. If the agent would need to guess, infer, or improvise to fill gaps, the file needs more content.

### Writing for Universal Applicability

Skills that work across any project type must be written at the level of universal software engineering principles, not stack-specific patterns. This requires a specific writing approach:

**Lead with the principle, follow with diverse illustrations.** Instead of "In Rust, use `clippy` to find dead code," write "Trace the call chain from every function to its callers. If a function has no callers and is not an entry point, public API, or callback target, it is likely dead. Language-specific tools (clippy for Rust, vulture for Python, eslint for TypeScript) can automate the surface-level detection, but dynamic dispatch, reflection, and code generation require manual verification."

**Name the pattern, not the technology.** Instead of "Use a HashMap for O(1) lookups," write "If the operation requires frequent key-based retrieval, a hash-based data structure gives O(1) average lookup. The specific type depends on the language (HashMap in Rust, dict in Python, Map in TypeScript, map in Go)."

**When you give examples, span domains.** A section about "hardcoded patterns that could be algorithmic" should show a raycast spacing example (game dev), a retry interval example (backend), and a grid layout example (frontend) — not three game dev examples. Each example teaches the same principle in a different context, proving the principle is universal.

**Acknowledge that best practice varies by stack.** Some principles genuinely differ across ecosystems. When they do, say so: "Error handling patterns vary significantly by language — Result types in Rust, exceptions in Python, error returns in Go. The important thing is consistency within the project, not adherence to one pattern." This gives the agent permission to adapt rather than forcing one approach.

### Designing Taxonomies and Categories

Several skills require taxonomies — classification systems where the agent must decide which category a finding, a file, or a concept belongs to. Well-designed taxonomies share several properties:

**Mutually exclusive.** Every item should belong to exactly one category. If two categories overlap, the agent wastes time deciding and may inconsistently classify similar items. When overlap is unavoidable, provide explicit boundary rules: "If a finding could belong to both X and Y, use this priority order..."

**Collectively exhaustive.** The taxonomy should cover every plausible finding. If the agent encounters something that fits no category, the taxonomy has a gap. Include a "how to handle items that do not fit" instruction — either a catch-all category or guidance on extending the taxonomy.

**Defined by principle, not by example.** Each category should have a clear definition that the agent can apply to novel situations, not just a list of examples. Examples illustrate the definition — they do not replace it. An agent encountering a finding type it has never seen before should be able to read the category definition and classify correctly.

**Ordered by decision priority.** When categories could compete for the same finding, provide a priority order that resolves ambiguity. "If it is a correctness issue, it goes in Known Issues regardless of what else it could be."

### Writing Templates That Guide Without Becoming the Output

Templates are structural guides — they show the expected shape of the output. The risk is that the agent treats the template as the output and fills in the blanks mechanically rather than reasoning about what each section needs.

**Show the structure, describe the intent.** For each section in a template, explain what the section is *for* — what question it answers, what value it provides to the reader.

| Weak template section | Strong template section |
|-----------------------|------------------------|
| `### Current State` | `### Current State` — What the code does now, grounded in the actual implementation. Include enough detail that an engineer can understand the issue without reading the code first. |
| `### Recommendation` | `### Recommendation` — The specific change proposed, with enough implementation detail that an engineer could act on it without further research. Connect the recommendation to the evidence in Current State. |

**Vary template completeness across examples.** If you show one fully filled template as an example, also show a shorter one for a simpler finding. This teaches the agent that depth should be proportionate to the finding's complexity, not uniform.

**Templates are minimum structure, not maximum structure.** The agent should feel free to add sections, sub-sections, diagrams, tables, or other elements that improve clarity. The template defines what must be present, not what is allowed.

### Writing "Open Field" Content

The hardest reference files to write are the ones where the agent needs maximum creative freedom — detection strategies, analysis approaches, writing standards. These are "open field" content: the skill establishes direction and quality, but the agent determines the path.

**Teach reasoning patterns, not procedures.** Instead of "Step 1: Check file sizes. Step 2: Check function lengths. Step 3: Check nesting depth," write "Look for structural indicators of complexity — files significantly larger than their peers, functions with deep nesting or many branch points, modules that mix multiple responsibilities. The specific indicators depend on the language and project conventions."

**Use conditional guidance.** "If the system involves domain-specific algorithms (ML training, physics simulation, graph traversal), conduct targeted research to find established optimisation strategies for that specific domain. If the system is primarily data transformation and I/O, focus on allocation patterns, unnecessary copies, and hot-path waste."

**State the quality bar, not the procedure for reaching it.** "Every finding must include evidence from the actual code, not assumptions about what the code probably does" is a quality bar. "Read lines 1–100 of each file, then check for..." is a procedure. Quality bars empower; procedures constrain.

**Give the agent explicit permission to be creative.** "The structural rules in this skill are fixed. Everything within that structure is yours — how you explain a system, what depth you reach, what visual representations you choose, how you scope your research queries." This is not filler — it actively counteracts the agent's tendency to be conservative when it senses many rules.

---

## 9. Formatting and Notation Standards

How skills should literally be formatted affects agent comprehension. Consistent formatting also makes skills easier to evaluate and maintain.

### SKILL.md Structure

The canonical structure for a SKILL.md file, in order:

```
1. YAML frontmatter (name, description)
2. One-paragraph skill summary
3. Core workflow / operating instructions
4. Reference file loading instructions (mandatory-core, then conditional)
5. Inviolable rules section (hard rules specific to this skill)
6. Quality checklist (recency anchor)
```

The workflow section is the largest. It describes what the agent does when the skill triggers — not step-by-step procedures, but the framework of the task, the quality standards, and the decision points.

### Reference File Structure

```
1. Table of contents (if >100 lines)
2. Brief purpose statement (1–2 sentences: what this file covers and when to read it)
3. Sections and subsections
```

### Section Header Conventions

- Use `##` for major sections in SKILL.md, `###` for subsections.
- Use `##` for major sections in reference files, `###` and `####` for subsections.
- Headers should be descriptive enough that a reader scanning headers alone understands the file's scope.

| Weak | Strong |
|------|--------|
| `## Section 3` | `## Finding Classification Taxonomy` |
| `### Details` | `### Boundary Rules for Overlapping Categories` |
| `## Misc` | `## Edge Cases and Project-Specific Adaptations` |

### Markdown Patterns That Improve Agent Comprehension

Different information types benefit from different representations:

| Information Type | Best Representation | Example Use |
|-----------------|---------------------|-------------|
| Comparisons (good vs. bad, options A/B/C) | Tables | Instruction wording comparisons, scoring rubrics |
| Hierarchies (file trees, category taxonomies) | Indented trees or nested lists | Directory structures, category breakdowns |
| Sequential operations | Numbered lists | Script execution order, file creation order |
| Parallel options | Bullet lists | Alternative approaches, multiple valid strategies |
| Templates and output formats | Fenced code blocks | File templates, output structure |
| Decision logic | Conditional prose or flowcharts | "If X, do Y. If Z, do W." |

**Anti-pattern:** Using bullet lists for everything. Bullet lists are appropriate for parallel items of equal weight. They are inappropriate for comparisons (use tables), hierarchies (use trees), or sequential steps (use numbered lists).

### How to Format Templates Within Reference Files

Templates should be in fenced code blocks with a content-type label. Each template section should have inline comments explaining intent:

```markdown
## Finding Template

```
### [Finding Title — Specific, Actionable, Domain-Free]

**Category:** [From the taxonomy in analysis-categories.md]
**Severity:** [Critical | High | Medium | Low — based on impact and fix cost]

#### Current State
[What the code does now. Ground every claim in the actual implementation.
Include file paths and function names. An engineer reading this should
understand the issue without opening the code.]

#### Proposed Change
[The specific change. Enough implementation detail that an engineer could
act on it without further research.]

#### Justification
[Why this change matters. Connect the evidence in Current State to the
benefit in Expected Impact. Research-backed where possible.]

#### Expected Impact
[Concrete, measurable where possible. "Reduces allocation in hot path
from O(n) to O(1)" not "improves performance."]
```
```

### How to Mark Hard Rules vs. Guidelines Visually

Within a skill's instructions, hard rules and guidelines should be visually distinguishable:

- **Hard rules:** Collected in a dedicated "Inviolable Rules" or "Structural Constraints" section. Each rule is a single declarative sentence with its justification.
- **Guidelines:** Woven into the workflow sections as principled instructions with reasoning. They do not need special visual marking — the presence of reasoning and the absence of imperative framing signals that they are guidelines.

Do not use emoji, colour, or other non-semantic markers. Structural separation (dedicated section) and wording tier (constraint vs. guideline vs. principle) are sufficient.

---

## 10. Example Design

### The Overfitting Risk

Examples are the single strongest influence on agent output — and the single biggest source of unintentional bias. They carry the risk of overfitting: the agent copies the surface pattern of the example rather than understanding the underlying principle. This is especially dangerous when:

- All examples look similar (the agent learns the superficial format, not the underlying reasoning).
- Examples are domain-specific (the agent applies the domain to unrelated projects).
- Examples are too detailed (the agent treats specifics as requirements).

### How Examples Actually Work in LLMs

The landmark paper "Rethinking the Role of Demonstrations" (Min et al., EMNLP 2022) demonstrated that what examples primarily teach is **format, distribution, and label space** — not content. Ground truth labels barely matter. What matters is the surface structure, vocabulary, and domain of the examples.

Research on **induction heads** (Olsson et al., 2022) presents evidence that attention mechanisms implement a pattern-completion circuit (`[A][B]...[A] → [B]`) — the model copies previous patterns for next-token prediction rather than extracting underlying principles. While this mechanism is robustly demonstrated in small models, the evidence for large models is correlational rather than causal. The practical implication holds regardless: models replicate the surface patterns of their examples.

This means: the domain, structure, length, tone, and vocabulary of your examples will be replicated in the agent's output, regardless of whether those properties are relevant to the current task. Example design is not about showing correct answers — it is about shaping the distribution of outputs.

### Example Design Principles

1. **Use diverse examples.** Vary scenarios, input types, complexity levels, and domains. If the skill will be used across Rust, Python, TypeScript, and Go projects, include examples from multiple languages.

2. **Include rejected examples.** Show a finding that *looked* good but was rejected, and explain why. This teaches the agent the decision boundary, not just the positive space.

3. **Vary content, not just structure.** If every example has the same number of sections, the same tone, and the same depth, the agent will replicate that uniformity. Vary these dimensions to show the range of acceptable output.

4. **3–5 examples is optimal.** Research shows major gains after 2 examples, a plateau around 4–5, and diminishing returns beyond that. More examples burn tokens without improving output.

5. **Frame examples as illustrations, not templates.** "Here is an example of a good finding. Note how the justification connects the research to the specific code." This guides attention to the *principle* the example demonstrates, not the surface format.

6. **Keep examples generic or clearly hypothetical.** If an example references a specific technology, the agent may anchor on that technology when working on unrelated projects. Use examples that teach the format and reasoning without implying a specific domain.

### Worked Comparison: Weak vs. Strong Example Sets

**Weak example set (for a code health audit skill):**

Three examples, all from a machine learning project:
- "Unused TensorFlow import in training pipeline"
- "Hardcoded learning rate in model.py"
- "Dead replay buffer class in agent.py"

**What goes wrong:** The agent auditing a web application looks for ML-specific patterns. It anchors on "training pipeline," "model," and "agent" as concept categories. It may miss web-specific opportunities (unused middleware, hardcoded API endpoints, dead route handlers) because its example-shaped understanding does not include them.

**Strong example set (for a code health audit skill):**

Five examples spanning domains:
- "Unused database connection pool in a Go web service" (backend)
- "Hardcoded retry interval in a Python data pipeline" (data engineering)
- "Dead physics collision handler in a Rust game engine" (game dev)
- "Rejected finding: apparent dead code that is actually called via reflection" (boundary case)
- "Unreachable error branch in a TypeScript CLI tool" (CLI)

**What goes right:** The agent encounters any type of project and can generalise from the principles demonstrated across domains. The rejected example teaches the boundary between dead code and dynamically-invoked code, preventing false positives.

---

## 11. Anti-Patterns and Failure Catalogue

This section documents failure modes observed in practice and from research. Each entry includes: symptom, root cause, example of the failing instruction, and the fix. Use this catalogue both for writing new skills and for diagnosing problems in existing ones.

### Research Foundation

Anti-patterns have a nuanced effect:

- **Specific, well-explained anti-patterns work.** A study found that anti-pattern avoidance prompts reduced code weaknesses by 59–64%. The key is specificity and explanation of *why* the pattern is bad.
- **Vague negative instructions backfire.** "Don't make it bad" is noise. "Do not create milestone-based files because they force readers to reconstruct the present from historical slices" is signal.
- **Many negative instructions fragment attention.** A long list of "do not" items creates ambiguity about what the agent *should* do.

### Best Practice for Documenting Anti-Patterns

1. Lead with the positive instruction. State what the agent should do first.
2. Add the anti-pattern as context for *why* the positive instruction matters.
3. Keep anti-patterns few and specific. Each one should describe a concrete failure mode with a clear explanation of the harm.
4. Consider whether the anti-pattern can be reframed as a positive instruction instead.

### Failure Pattern Catalogue

---

#### F1: Scenario-List Exhaustion

**Symptom:** The agent performs a behaviour in some situations but inexplicably skips it in others that seem equally appropriate.

**Root cause:** The instruction listed specific triggering scenarios, and the agent treats the list as exhaustive. See [Section 5, The Scenario-List Anti-Pattern](#the-scenario-list-anti-pattern) for full treatment.

**Failing instruction:** "After completing a task, fixing a bug, or finishing a meaningful chunk of work, commit."

**Fix:** "Commit early and often. The only constraint is: never push without explicit permission."

**Detection:** Search for instructions containing comma-separated scenarios ("after X, Y, or Z"). Ask whether the agent would skip the behaviour for an unlisted scenario.

---

#### F2: Domain Bias Anchoring

**Symptom:** The agent applies domain-specific patterns to unrelated projects. A web app audit produces ML-flavoured findings. A CLI tool's documentation reads like an API reference.

**Root cause:** Examples in the skill are drawn from a single domain. The agent's induction heads replicate the domain vocabulary and conceptual framework from the examples.

**Failing instruction:** Three examples all referencing ML concepts (training pipelines, replay buffers, model checkpoints) in a general-purpose code health skill.

**Fix:** Span examples across at least 2–3 domains. No single domain should represent more than half the examples in any file. See [Section 10, Example Design](#10-example-design).

**Detection:** Read every example in the skill and ask: "If an agent read only these examples, would it think this skill is designed for one specific kind of project?"

---

#### F3: Decision-Support Cardinality Anchoring

**Symptom:** The agent always produces exactly N options, alternatives, or categories, regardless of the actual decision space. If examples show 3 options, every output has 3 options.

**Root cause:** The examples all had the same number of items (e.g., every comparison showed exactly 3 alternatives). The agent learned the cardinality as part of the format.

**Failing instruction:** Three worked examples, each showing exactly 3 alternatives for a design decision.

**Fix:** Vary the cardinality across examples. One example with 2 options, another with 4, another with 5. Explicitly state: "The number of alternatives depends on the decision space, not on a fixed count."

**Detection:** Check whether all examples of a particular output type have the same structural dimensions (same number of items, same number of sections, same depth). If yes, cardinality anchoring is likely.

---

#### F4: Reference File Under-Loading

**Symptom:** The agent produces output that ignores information available in reference files it was told to read. Quality is inconsistent — sometimes good (when reference was loaded), sometimes shallow (when it was not).

**Root cause:** SKILL.md listed many reference files sequentially without marking which are mandatory vs. conditional. The agent read the first few and stopped. Observed in practice: agents given a list of 10 files to read often stop at 3.

**Failing instruction:**
> Read the following reference files: `categories.md`, `evidence.md`, `format.md`, `examples.md`, `edge-cases.md`, `taxonomy.md`, `quality-bars.md`, `templates.md`, `scoring.md`, `glossary.md`.

**Fix:** Separate mandatory-core files (read immediately, every time) from task-based conditional files (read when specific conditions apply):

> **Always read these files first:**
> - `categories.md` — finding classification taxonomy
> - `evidence.md` — evidence and justification standards
>
> **Read these when relevant to the current task:**
> - `edge-cases.md` — when encountering unusual project structures
> - `templates.md` — when producing output files

**Detection:** Count reference files in the loading instructions. If more than 3–4 are listed without conditional triggers, under-loading is likely.

---

#### F5: Instruction Contradiction Across Files

**Symptom:** The agent's output is inconsistent — it follows different rules at different times, or produces output that seems uncertain and hedging.

**Root cause:** SKILL.md says one thing ("use judgement to choose the best format") but a reference file says something contradictory ("always use bullet lists for this section"). The agent loses confidence and produces inconsistent output.

The paper "LLMs can be easily Confused by Instructional Distractions" (2025) tested six models and found that when task instructions compete with content signals, accuracy on the intended task can fall as low as **30%** (style transfer) or even **5.1%** (question answering). The core finding: when instructions compete, compliance degrades broadly across ALL instructions — not just the contradicting pair.

**Failing instruction:**
- SKILL.md: "Use your judgement to choose the best representation for each section."
- reference/format.md: "All analysis sections must use bullet lists."

**Fix:** Ensure every instruction in every file is consistent. When a reference file provides more specific guidance than SKILL.md, frame it as a refinement, not a contradiction: "For analysis sections, bullets are usually the clearest format, but use tables when comparing alternatives and prose when explaining complex reasoning chains."

**Detection:** For each instruction in the skill, search the entire skill directory for any instruction that could be read as contradicting it. Pay special attention to contradictions across files — they are harder to spot and there are no existing tools for multi-file prompt coherence checking.

---

#### F6: Template-as-Output

**Symptom:** The agent fills in template blanks mechanically. Output sections are shallow, formulaic, and lack genuine reasoning. Every finding looks the same structurally regardless of complexity.

**Root cause:** The template provided labels without intent descriptions. The agent treats the template as a form to fill in rather than a framework for reasoning.

**Failing instruction:**
```
### Current State
[describe current state]

### Recommendation
[describe recommendation]
```

**Fix:** Describe the intent of each section:
```
### Current State
What the code does now, grounded in the actual implementation.
Include enough detail that an engineer can understand the issue
without reading the code first. Reference specific files and
functions.

### Recommendation
The specific change proposed, with enough implementation detail
that an engineer could act on it without further research. Connect
the recommendation to the evidence in Current State.
```

**Detection:** Read the template sections. If any section is just a label with a bracket placeholder, it will produce mechanical output. Every section needs an intent description.

---

#### F7: Mode-Question Friction

**Symptom:** The agent asks the user to choose a mode, depth level, or configuration at startup, even when the context makes the choice obvious. Users experience friction and perceive the skill as unhelpful.

**Root cause:** The skill instructs the agent to ask the user to choose between modes before starting work.

**Failing instruction:** "Ask the user whether they want a quick scan, standard audit, or deep dive before beginning."

**Fix:** "Infer the appropriate depth from context — project size, user's request specificity, and available time signals. If genuinely ambiguous, state your inference and ask for confirmation rather than presenting a menu."

**Detection:** Search for instructions that require the agent to ask the user a question before starting work. Each one is a friction point. Ask whether the question could be answered by inference from context.

---

#### F8: Over-Constraining Collapse

**Symptom:** The agent abandons some instructions entirely rather than partially complying with all of them. Output is missing sections or categories that the skill explicitly requires.

**Root cause:** The skill has too many rigid constraints, and the agent hits its instruction saturation point. The IFScale benchmark (2025) quantifies this: o3, the strongest model tested, achieved only **62.8% accuracy at 500 instructions**, with most models performing significantly worse. Reasoning models maintain near-perfect compliance until roughly 150 instructions, then degrade steeply — o3 scores 98.2% at 100 instructions but crashes to 62.8% at 500. Beyond saturation, models shift overwhelmingly toward **omission errors** — they abandon instructions entirely rather than partially complying, with an extreme 34.88:1 omission-to-modification ratio in the worst case. The paper also identifies a strong **primacy effect**: earlier instructions are followed more reliably than later ones, consistent with attention limitations.

The paper "What Prompts Don't Say" (2025) found that specifying all requirements simultaneously **backfires** — with 19 requirements specified, accuracy drops to 85% from a 98.7% baseline.

**Failing instruction:** A skill with 200+ instructions across SKILL.md and reference files, many of which are rigid constraints rather than principles.

**Fix:** Reduce instruction count by converting rigid constraints to principles with reasoning. Reserve imperative constraints for genuine hard rules. Use quality bars instead of procedures. Trust the agent's judgement for content decisions.

The Sonar Foundation Agent case study (2025) provides direct evidence: a prescriptive two-stage workflow achieved **58% efficacy**, a freer workflow reached **70%**, and distilling to a concise, principle-based prompt with extended thinking reached **75%** — both architectural freedom and prompt conciseness contributed independently.

**Detection:** Count the total instructions across the skill directory. If the count exceeds ~100, the skill is at risk of saturation. Evaluate each instruction: is it a genuine constraint, or could it be a principle?

---

#### F9: Stale Internal References

**Symptom:** The agent tries to read files that do not exist, references concepts by old names, or produces output that follows an outdated structure.

**Root cause:** The skill's structure changed (folders renamed, files moved, concepts reorganised) but internal references were not all updated. No automated tools exist to detect this.

**Fix:** After any structural change, search the entire skill directory for old names. Every stale reference must be updated.

**Detection:** Verify that every file referenced in SKILL.md's loading instructions actually exists with that exact filename. Search for any path or concept name that does not match the current directory structure.

---

## 12. Quality Assurance Design

### The Role of Quality Checklists

Quality checklists at the end of a skill serve two distinct purposes:

1. **Verification:** The agent uses them to check its own output before presenting it.
2. **Recency anchoring:** Items at the end of the skill body receive strong attention due to the primacy-recency effect. The quality checklist is the last thing the agent reads in SKILL.md, making it the most salient set of requirements during output generation.

This dual role means the checklist is not just a final check — it actively shapes the agent's output priorities. Items in the checklist receive disproportionate attention. Use this strategically: the most important quality requirements belong in the checklist.

### Writing Verifiable Checklist Items

Every checklist item must be concrete and verifiable by the agent itself. The test: could the agent read this item and unambiguously answer "yes" or "no" about its own output?

| Weak (unverifiable) | Strong (verifiable) |
|---------------------|---------------------|
| Is the output good? | Every finding includes the full proof chain: current state, proposed change, justification, expected benefit. |
| Are the examples diverse enough? | Examples span at least 3 different project domains and include at least one rejected example demonstrating a decision boundary. |
| Is the format consistent? | Every output file uses the same heading hierarchy, finding template structure, and severity labelling scheme. |
| Did I check everything? | Every file in the repository's `src/` directory has been read and analysed. No directories were skipped. |
| Is the depth appropriate? | Every finding's justification references specific code (file path + function/line) rather than general assertions about what the code "probably" does. |

### Checklist Design Principles

- **Do not duplicate the instructions.** The checklist confirms that the instructions were followed; it does not restate them. If the checklist item is a direct copy of an instruction from earlier in SKILL.md, it wastes tokens and dilutes attention.

- **Keep the checklist proportionate.** A simple skill needs 5–8 items. A complex skill might need 12–15. Beyond 15, attention dilutes and the agent starts omitting items (IFScale saturation effect).

- **Order by importance.** The agent attends most to the first and last items in a list. Place the most critical quality requirements at the top and bottom of the checklist.

- **Make items independent.** Each item should be evaluable on its own, without reference to other items. Dependent items ("Did I do X? If yes, did I also do Y?") should be merged into one item.

### Component-Specific Evaluation Criteria

Different components of a skill require different evaluation approaches:

**Evaluating a description:**
- Does it activate for every reasonable phrasing of the skill's core use case?
- Does it NOT activate for adjacent skills' use cases?
- Is it dense with trigger terms? Count the unique trigger phrases — fewer than 5 is usually too sparse.
- Is it under 1024 characters?
- Is it written in third person?

**Evaluating a reference file:**
- Does it have a table of contents (if over 100 lines)?
- Does it cover one coherent topic?
- Does it explain *why* behind every major instruction?
- Does it include diverse examples (if applicable)?
- Does it avoid pointing to other reference files?
- Is the depth proportionate to the judgement involved, variation across projects, and cost of mistakes?

**Evaluating a quality checklist:**
- Is every item verifiable by the agent (yes/no answer)?
- Are items independent of each other?
- Is the count proportionate (5–15 items)?
- Do the most critical items appear at the top and bottom?
- Does the checklist avoid duplicating instructions from the body?

**Evaluating a template:**
- Does every section have an intent description (not just a label)?
- Are worked examples varied in depth and complexity?
- Is the template framed as minimum structure, not maximum?

**Evaluating an example set:**
- Do examples span at least 2–3 domains?
- Is there at least one rejected example showing a decision boundary?
- Do examples vary in complexity and depth?
- Are examples framed as illustrations of principles, not templates to copy?
- Do all examples avoid anchoring on a single cardinality?

---

## 13. Content Quality and Bias Prevention

A well-structured skill can still produce poor agent output if the *content* within that structure has quality issues. Structure is the skeleton; content is the muscle. Both must be right.

### Domain Bias in Examples

Examples are the single strongest influence on agent output — and the single biggest source of unintentional bias. Research confirms this is not hypothetical:

Research on in-context learning consistently shows that models replicate the surface patterns of their examples — vocabulary, domain, structural format — rather than extracting the abstract principle the examples were meant to illustrate. If every example in a skill references machine learning, the agent will anchor on ML patterns when working on a web app, because the example domain leaks into the agent's understanding of the task itself.

The landmark paper "Rethinking the Role of Demonstrations" (Min et al., EMNLP 2022) demonstrated that what examples primarily teach is **format, distribution, and label space** — not content. Ground truth labels barely matter. What matters is the surface structure, vocabulary, and domain of the examples. This means domain bias in examples leaks directly into the agent's understanding of the task itself.

Further research on **induction heads** (Olsson et al., 2022) shows that attention mechanisms literally "replicate previous patterns for next-token prediction" — the model copies demonstration patterns rather than extracting underlying principles. **Surface form competition** means multiple terms referring to the same concept fight for probability mass, so the specific vocabulary in examples directly biases output vocabulary.

**The test:** Read every example in the skill and ask: "If an agent read only these examples, would it think this skill is designed for one specific kind of project?" If yes, the examples need diversification.

**The standard:** Examples across a skill should span at least 2–3 different domains (web services, data pipelines, CLI tools, desktop applications, infrastructure, etc.). No single domain should represent more than half the examples in any file.

**Template examples are highest risk.** Templates are used as direct structural patterns. If a template's worked example uses domain-specific names (like `reinforcement-learning-path.md` or `replay-buffer.rs`), agents will produce output shaped by that domain even when working on something completely different.

### Instruction Coherence

Instructions within a skill must not contradict each other. Research shows this matters more than you might expect:

The paper "LLMs can be easily Confused by Instructional Distractions" (2025) tested six models and found that competing instruction signals cause accuracy on the intended task to fall as low as 30% in some configurations. When instructions compete with each other for the agent's attention, compliance on all instructions degrades — not just the contradicting pair.

The paper "The Instruction Gap" (2025) found that **instruction compliance and accuracy are independent dimensions** — models that follow all instructions don't necessarily provide accurate answers, and accurate models may struggle with instruction compliance. This means a contradicting instruction can degrade compliance broadly without visibly breaking any single output.

Common contradiction patterns:

- A principle section says "use your judgement to choose the best format" but a later section says "always use bullet lists for this section."
- The SKILL.md says "create files only when justified" but a reference file provides templates that imply files should always be created.
- One reference says "keep it concise" while another says "be exhaustive and comprehensive."

**The test:** For each instruction, search the skill for any instruction that could be read as contradicting it. Pay special attention to instructions in different files — contradictions across files are harder to spot and there are **no existing tools for multi-file prompt coherence checking** (this is entirely manual work today).

### Terminology Drift

Research on prompt sensitivity (2024) provides hard numbers: **"A slight change in a class definition can lead to drastic changes in the final prediction."** Sensitivity values ranged from 0.005 to 0.404 across models. The mechanism is **surface form competition** — when multiple terms refer to the same concept, they fight for probability mass in the model's output distribution, fragmenting attention and producing inconsistent output.

Common drift patterns:

- "System file" vs "system document" vs "system doc" — same thing, three names.
- "Plan file" vs "execution plan" vs "implement-now file" — same thing, three names.

**The test:** List every important concept in the skill. For each one, search the entire skill directory for all terms used to reference it. If there are multiple terms, pick one and standardise. Check terminology against other skills in the ecosystem — a concept that appears in multiple skills should use the same term everywhere.

### Stale Internal References

When a skill's structure changes (folders renamed, files moved, concepts reorganised), internal references may not all get updated. No tools exist to detect this automatically.

**The test:** After any structural change, search the entire skill directory for the old name or concept. Every occurrence must be updated.

### Instruction Framing Quality

Every instruction in the skill should be evaluated:

- **Does it explain *why*?** An instruction with reasoning produces generalised understanding. An instruction without reasoning produces rote compliance.
- **Is it framed positively?** Lead with what to do. Add what not to do as context, not as the primary instruction.
- **Does it use proportionate emphasis?** Reserve ALWAYS/NEVER for genuinely inviolable constraints. For everything else, explain the reasoning.

### Autonomy-Restricting Language

The Sonar Foundation Agent case study (2025) provides direct evidence: a prescriptive two-stage workflow achieved **58% efficacy**, a freer workflow reached **70%**, and distilling to a concise, principle-based prompt with extended thinking reached **75%** — both architectural freedom and prompt conciseness contributed independently.

The IFScale benchmark (2025) quantifies instruction saturation: the strongest reasoning model tested (o3) achieved only **62.8% accuracy at 500 instructions**. Models show three distinct degradation patterns: *threshold decay* (reasoning models maintain near-perfect compliance until ~150 instructions, then crash), *linear decay* (frontier models like Claude Sonnet 4 degrade steadily), and *exponential decay* (smaller models collapse to 7–15% accuracy floors). Beyond saturation, models shift overwhelmingly toward **omission errors** — they abandon instructions entirely rather than partially complying.

The paper "What Prompts Don't Say" (2025) found a critical paradox: specifying all requirements simultaneously **backfires** — with 19 requirements specified, accuracy drops to 85% from a 98.7% baseline.

Scan every instruction for language that unnecessarily restricts agent creativity:

- "Must always" / "must never" — is this genuinely inviolable, or would a principle with reasoning be better?
- "Exactly 5 sections" / "maximum 3 files" / "between 100–200 words" — is this numeric limit structural or arbitrary?
- "These sections should not exist" / "never create these files" — is there a scenario where the agent's judgement should override this?

### Arbitrary Limits and When to Avoid Them

Rigid limits (word counts, file counts, section counts, character limits) constrain agent autonomy without improving output quality. They are appropriate only when:

- The limit is structural (SKILL.md under 500 lines — a context engineering constraint).
- The limit prevents a known failure mode (plan file accumulation — a proven anti-pattern).
- The limit is a floor, not a ceiling (minimum 30 non-empty lines for system docs — a shallow-document detector).

Instead of numeric limits, state the principle and the failure mode:

| Numeric limit (weaker) | Principle + failure mode (stronger) |
|------------------------|-------------------------------------|
| Maximum 3 plan files. | Plans are temporary execution aids. Remove them when complete. Do not let stale plans accumulate. |
| Sections must be 100–200 words. | Each section should carry enough information to be useful. If it can be said in one line, say it in one line. If it needs a page, give it a page. |
| These sections must not exist. | Avoid vague catch-all sections. Every section should have a clear topic and canonical home. |

---

## 14. Cross-Skill Coherence

### The Coordination Problem

When multiple skills exist in the same ecosystem, they can conflict — different terminology, overlapping triggers, contradictory instructions. Agents exposed to conflicting instructions lose confidence and produce inconsistent output. Cross-skill coherence is not optional in a multi-skill ecosystem — it is as important as within-skill coherence.

### Coherence Dimensions

| Dimension | What to Check | Failure Mode |
|-----------|--------------|--------------|
| **Terminology** | Same concept uses same term across all skills. | Agent treats "system file" and "system document" as different concepts, producing inconsistent output or missing connections. |
| **Trigger boundaries** | Descriptions are mutually exclusive with clear boundaries. | Two skills activate for the same user request. The agent either loads both (wasting context) or loads the wrong one. |
| **Artefact references** | Skills reference artefact patterns, not other skills by name. | Renaming a skill breaks references in other skills. Skills develop hidden coupling. |
| **Self-containment** | Each skill has everything it needs within its own directory. | A skill depends on a reference file in another skill's directory. Moving or reorganising either skill breaks the other. |
| **Philosophical consistency** | All skills share the same stance on autonomy, depth, and quality. | One skill grants maximum autonomy while another prescribes rigid procedures. The agent's behaviour oscillates depending on which skill is active. |

### The Personality as Coordinator

Only the personality/coordinator file knows about all skills, how they relate, and when to invoke each one. Skills are specialists that do not know about each other. This means:

- A skill must never say "use the X skill for this" — it does not know the X skill exists.
- A skill may reference artefact patterns: "some files in context/references/ follow a multi-section research paper structure." This describes what exists, not which skill created it.
- When two skills could produce overlapping artefacts, their descriptions must include negative triggers that create clear boundaries.

### Evaluating Cross-Skill Coherence

**Evaluation test:** Take any two skills in the ecosystem. For each pair:

1. Do their descriptions overlap? Could a single user request trigger both?
2. Do they use the same term for the same concept? Search for shared terminology.
3. Does either reference the other by name?
4. Does either depend on files outside its own directory?
5. If both were active in the same conversation, would their instructions conflict?

---

## 15. Scoring Rubric

This rubric provides a structured evaluation framework for any agent skill. Each dimension is scored on a three-point scale with concrete, observable criteria. A skill does not need to be "Strong" on every dimension — but weaknesses should be intentional and justified, not accidental.

### How to Use the Rubric

Score each dimension independently. Record the score and one sentence of evidence (what you observed that led to the score). After scoring all dimensions, identify the lowest-scoring dimensions — these are the highest-leverage improvement targets.

### The Rubric

#### 1. Trigger Accuracy

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Description is vague or generic. Fewer than 3 unique trigger terms. No negative triggers. Would fail to activate for common phrasings of the skill's use case, or would false-activate for adjacent skills. |
| **Adequate (2)** | Description covers the main use case with 3–5 trigger terms. Some negative triggers present. Would activate for standard phrasings but miss edge cases or unusual vocabulary. |
| **Strong (3)** | Description is dense with trigger terms (6+), includes negative triggers for all adjacent skills, covers both formal and informal phrasings. Would activate correctly for any reasonable user request, including edge cases. Assertive activation cue present. |

#### 2. Instruction Clarity

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Instructions are ambiguous, contradictory, or assume domain knowledge. Missing *why* explanations. Heavy use of CAPS/bold for non-critical items. Scenario-list anti-pattern present. |
| **Adequate (2)** | Instructions are clear and mostly consistent. Some *why* explanations present. Emphasis is mostly calibrated. No major contradictions, though minor inconsistencies may exist across files. |
| **Strong (3)** | Every major instruction explains *why*. Emphasis reserved for genuine hard rules. No scenario-list anti-patterns. Instruction tiers (constraint/guideline/principle) are correctly matched to their content. No contradictions within or across files. |

#### 3. Example Diversity

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Single domain. Uniform complexity and depth. No rejected examples. Cardinality is anchored (all examples have same number of items). |
| **Adequate (2)** | 2–3 domains represented. Some variation in complexity. May lack rejected examples or vary cardinality. |
| **Strong (3)** | 3+ domains, varied complexity, includes at least one rejected example demonstrating a decision boundary, varied cardinality. Examples are framed as illustrations of principles with annotations pointing to what makes them good. |

#### 4. Depth Calibration

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Uniformly shallow across all reference files, or uniformly deep regardless of judgement-involvement. The "agent reading only this file" test fails for most references. |
| **Adequate (2)** | Depth is roughly appropriate for most files. Some files could be deeper (high-judgement topics treated shallowly) or shallower (low-judgement topics over-explained). |
| **Strong (3)** | Depth precisely matches the three calibration factors (judgement involvement, cross-project variation, mistake cost). High-judgement files are comprehensive with extensive examples and boundary guidance. Low-judgement files are concise. |

#### 5. Autonomy Balance

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Over-constrained: rigid procedures for open-field decisions, excessive numeric limits, CAPS/bold overuse. Or under-constrained: no guidance, no quality standards, no structural rules. |
| **Adequate (2)** | Reasonable balance. Most structural decisions are fixed, most content decisions are free. Some unnecessary constraints remain. Total instruction count is manageable. |
| **Strong (3)** | Clear framework with explicit freedom grants. Hard rules only where justified with structural reasoning. Principles and quality bars for open-field content. Total instruction count well below saturation (~100). Agent reading the skill would feel empowered, not constrained. |

#### 6. Reference Architecture

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Monolithic SKILL.md (over 500 lines) with no reference files. Or many reference files with no loading guidance. Or nested references (references pointing to references). |
| **Adequate (2)** | Reasonable split between SKILL.md and references. Loading instructions present but may not distinguish mandatory-core from conditional. File names are descriptive. |
| **Strong (3)** | Progressive disclosure with mandatory-core and task-based conditional loading clearly distinguished. One level deep. Descriptive file names. Each file covers one coherent topic. Table of contents in long files. SKILL.md under 500 lines. |

#### 7. Formatting Quality

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Inconsistent markdown. Bullet lists used for everything. No visual hierarchy. Headers are vague ("Section 3," "Details"). Templates lack intent descriptions. |
| **Adequate (2)** | Consistent markdown. Some appropriate use of tables, trees, and code blocks. Headers are mostly descriptive. Templates have basic intent descriptions. |
| **Strong (3)** | Rich representation throughout — tables for comparisons, trees for hierarchies, code blocks for templates. Clear visual hierarchy. All headers descriptive. Templates have comprehensive intent descriptions. Hard rules visually separated from guidelines. |

#### 8. Coherence

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Contradictions between files. Terminology drift (multiple terms for same concept). Philosophical inconsistency (autonomy-granting in one file, prescriptive in another). |
| **Adequate (2)** | Mostly consistent terminology. No major contradictions. Minor inconsistencies in philosophical stance across files. |
| **Strong (3)** | Fully coherent terminology — every concept has exactly one term used consistently across all files. No contradictions. Consistent philosophical stance (same level of autonomy, same approach to depth, same quality expectations) across the entire skill directory. |

#### 9. Quality Checklist

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Missing, or present with vague/unverifiable items ("Is it good?"). Duplicates instructions from the body. More than 15 items (diluted attention). |
| **Adequate (2)** | Present with mostly verifiable items. Proportionate count (5–15). Some items could be more concrete. |
| **Strong (3)** | Every item is concrete and verifiable (yes/no answer). Proportionate count. Ordered by importance. Independent items. Does not duplicate the body. Acts as an effective recency anchor for the skill's most critical quality requirements. |

#### 10. Cross-Skill Fit

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Overlapping triggers with adjacent skills. References other skills by name. Inconsistent terminology with the ecosystem. Depends on files outside its directory. |
| **Adequate (2)** | Non-overlapping triggers. Self-contained. May have minor terminology inconsistencies with the ecosystem. |
| **Strong (3)** | Clean trigger boundaries with negative triggers for all adjacent skills. Artefact-pattern references only (no skill names). Consistent terminology with the entire ecosystem. Fully self-contained. Philosophical stance aligned with ecosystem norms. |

### Interpreting Scores

- **All 3s:** The skill is exceptionally well-crafted. Maintain it.
- **Mostly 3s with one or two 2s:** Strong skill. The 2s are improvement opportunities but not urgent.
- **Mix of 2s and 3s:** Good skill with clear areas for improvement. Address 2s methodically.
- **Any 1:** The skill has a significant weakness that will degrade agent output. Address 1s before deployment.
- **Multiple 1s:** The skill needs substantial rework. Prioritise by impact: Trigger Accuracy and Instruction Clarity affect everything downstream.

---

## 16. Testing and Validation

A skill cannot be fully evaluated by reading it — it must also be tested against realistic scenarios. This section describes how to validate that a skill works as intended.

### Mental Dry-Run

Read the skill as if you were the agent. Walk through a hypothetical task from trigger to output:

1. **Trigger test:** Given a realistic user request, would the description activate this skill? Try 3–5 different phrasings, including informal ones ("sweep for dead code," "clean up this repo," "find unused stuff").

2. **Loading test:** Once triggered, what files would you read? Follow the loading instructions literally. Would you know which reference files to read for this specific task? Are the conditional triggers clear?

3. **Execution test:** With SKILL.md and the relevant references loaded, would you know what to do at every decision point? Where would you get stuck? Where would you need to guess?

4. **Output test:** Would you know exactly what to produce? What format? What depth? Where to put it?

5. **Quality test:** After producing output, would you know how to evaluate it? Does the quality checklist cover the most important dimensions of output quality?

**Record every point of confusion.** Each one is a gap in the skill that needs to be filled.

### Edge Case Scenarios

Test the skill against situations that push its boundaries:

| Scenario | What It Tests |
|----------|--------------|
| **Minimal input** — a one-line user request with no details. | Does the skill guide the agent on what to ask for or infer? Or does it assume rich input? |
| **Unusual project type** — a project in an uncommon language or domain. | Do the examples and instructions generalise? Or do they assume a specific stack? |
| **Ambiguous trigger** — a user request that could activate this skill or an adjacent one. | Do the negative triggers correctly prevent false activation? |
| **Large scope** — a project with hundreds of files or thousands of lines. | Does the skill handle scale? Are there instructions for prioritisation and scoping? |
| **Small scope** — a project with 3 files and 100 lines of code. | Does the skill handle minimal projects without producing empty or padded output? |
| **Mid-conversation trigger** — the skill activates after the agent has already been working on something else. | Do the instructions make sense when the agent already has context? Or do they assume a fresh conversation? |

### First-Session Signals

When a skill is used for the first time in a real session, watch for these signals:

**Positive signals (skill is working):**
- The agent triggers correctly on the first user request.
- The agent loads the appropriate reference files without prompting.
- Output follows the quality checklist without reminders.
- Output depth is proportionate to the topic's complexity.
- The agent makes good judgement calls in open-field areas.

**Warning signals (skill needs adjustment):**
- The agent asks the user which mode to use (mode-question friction — see F7).
- The agent produces output anchored on a specific domain from the examples (domain bias — see F2).
- The agent follows some instructions but ignores others (over-constraining collapse — see F8).
- The agent produces mechanically uniform output regardless of input variation (template-as-output — see F6).
- The agent does not load conditional reference files when they are clearly relevant (under-loading — see F4).

### Regression Signals

After changing a skill, watch for these regression indicators:

- **Trigger regression:** A phrasing that previously activated the skill no longer does (or a phrasing that didn't now does incorrectly).
- **Quality regression:** Output quality decreased in an area that was previously strong. This often happens when adding instructions — the new instructions may conflict with or dilute existing ones.
- **Instruction count regression:** The total instruction count across the skill directory increased beyond the saturation threshold. Count instructions after every change.
- **Coherence regression:** The change introduced a terminology inconsistency or instruction contradiction. Search the directory for the changed terms.

---

## 17. Post-Writing Verification

After writing or editing any skill, run through these verification checks. No automated tools exist for multi-file prompt coherence checking — this is entirely manual work today (the research confirms this gap). These checks catch the kinds of issues that are invisible during writing but create real problems when agents use the skill.

### Bias and Diversity Check

- Read every example, template, and worked scenario across the entire skill directory. Are they drawn from at least 2–3 different domains? Would an agent working on any type of project (web service, game, CLI tool, data pipeline, mobile app, infrastructure) find the examples relatable and non-anchoring?
- Pay special attention to template files — these have the highest contamination risk because agents use them as direct structural patterns.
- Check that example titles, file names, variable names, and function names do not anchor on one domain. `select_experiences()` anchors on ML. `process_batch()` is generic.

### Coherence Check

- Read the SKILL.md and every reference file looking for instructions that contradict each other, even subtly. A "use judgement" instruction in one place and an "always do X" instruction in another is a contradiction.
- Verify that the quality checklist at the end of SKILL.md is consistent with the instructions in the body and reference files.
- Check that the description in the YAML frontmatter accurately reflects what the skill actually does.

### Terminology Check

- List the 5–10 most important concepts in the skill. Search the entire skill directory for each one. Is the same term used consistently?
- Check terminology against other skills in the ecosystem. A concept that appears in multiple skills should use the same term everywhere.

### Reference Integrity Check

- After any structural change (file rename, folder restructure, concept reorganisation), search the entire skill directory for the old names. Every stale reference must be updated.
- Verify that every file referenced in SKILL.md's reference loading instructions actually exists with that exact filename.
- Verify that reference files do not point to other reference files (one-level-deep rule).

### Framing Check

- Search for ALWAYS, NEVER, MUST, and MUST NOT in capitals. For each one, ask: does this need to be this emphatic, or would a principle with reasoning be better?
- Search for negative instructions ("do not," "never," "avoid"). For each one, ask: is there a positive framing that teaches the same lesson?
- Verify that every major instruction includes a *why* — not just what to do, but why it matters.
- Search for scenario-list patterns (instructions with comma-separated triggering scenarios). Evaluate each for the scenario-list anti-pattern.

### Autonomy Check

- Search for numeric constraints (word counts, file counts, section counts, character limits). For each one, ask: is this structural (context engineering) or arbitrary (restricting judgement)?
- Search for prohibitions on specific sections, files, or formats. Are there legitimate scenarios where the agent should be allowed to make a different choice?
- Read the skill from the perspective of a highly capable agent: does it feel like an empowering framework or a restrictive script?
- Count total instructions across the skill directory. If the count approaches or exceeds ~100, evaluate which instructions could be converted from constraints to principles.

### Cross-Skill Check (when the skill is part of an ecosystem)

- Verify that the skill does not reference other skills by name — only artefact patterns.
- Verify that trigger descriptions do not overlap with other skills. Include negative triggers where needed.
- Check that the skill is fully self-contained — it should not depend on the reader knowing about other skills.
- Verify terminology consistency with the ecosystem.

### Scoring Check

- Score the skill against the rubric in [Section 15](#15-scoring-rubric). Any dimension scoring 1 should be addressed before the skill is deployed.

---

## 18. Sources

### Skill Design and Instruction Writing
- [Anthropic Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Anthropic skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
- [Anthropic — Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Anthropic Claude 4 Prompting Best Practices](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- [Augment Code — 11 Prompting Techniques for Better AI Agents](https://www.augmentcode.com/blog/how-to-build-your-agent-11-prompting-techniques-for-better-ai-agents)
- [OpenAI GPT-4.1 Prompting Guide](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide)
- [Elements.cloud — Agent Instruction Patterns and Antipatterns](https://elements.cloud/blog/agent-instruction-patterns-and-antipatterns-how-to-build-smarter-agents/)
- [PromptHub — Few-Shot Prompting Guide](https://www.prompthub.us/blog/the-few-shot-prompting-guide)
- [Claude Code Skills Structure and Usage Guide](https://gist.github.com/mellanon/50816550ecb5f3b239aa77eef7b8ed8d)

### Content Quality, Bias, and Verification Research
- [Rethinking the Role of Demonstrations — Min et al., EMNLP 2022](https://arxiv.org/abs/2202.12837)
- [A Survey on In-context Learning — Dong et al., 2023](https://arxiv.org/abs/2301.00234)
- [In-context Learning with Transformers — Induction Heads — Olsson et al., 2022](https://arxiv.org/abs/2209.11895)
- [LLMs can be easily Confused by Instructional Distractions, 2025](https://arxiv.org/html/2502.04362v1)
- [The Instruction Gap: LLMs get lost in Following Instructions, 2025](https://arxiv.org/html/2601.03269)
- [What Prompts Don't Say: Understanding Underspecification, 2025](https://arxiv.org/html/2505.13360v2)
- [Quantifying LLMs' Sensitivity and Consistency — Errica et al., NAACL 2025](https://arxiv.org/html/2406.12334v1)
- [How Many Instructions Can LLMs Follow at Once? — IFScale, 2025](https://arxiv.org/html/2507.11538v1)
- [Introducing Sonar Foundation Agent — Sonar, 2025](https://www.sonarsource.com/blog/introducing-sonar-foundation-agent/)
- [Does Prompt Formatting Have Any Impact on LLM Performance?, 2024](https://arxiv.org/html/2411.10541v1)
- [PromptDoctor: Automated Prompt Linting and Repair, 2025](https://arxiv.org/abs/2501.12521)
- [Context Rot — Chroma Research, 2025](https://research.trychroma.com/context-rot)
- [Surface Form Competition — Holtzman et al., EMNLP 2021](https://arxiv.org/abs/2104.08315)
- [Do not think about pink elephant! — CVPR 2024 Workshop](https://arxiv.org/abs/2404.15154)
- [Negation: A Pink Elephant in the LLMs' Room?, 2025](https://arxiv.org/abs/2503.22395)
- [Let Me Speak Freely? Format Restrictions and LLM Performance, 2024](https://arxiv.org/abs/2408.02442)
- [Lost in the Middle — Liu et al., 2023](https://arxiv.org/abs/2307.03172)
- [Serial Position Effects of LLMs — Guo et al., ACL Findings 2024](https://arxiv.org/abs/2406.15981)
- [Calibrate Before Use — Zhao et al., ICML 2021](https://arxiv.org/abs/2102.09690)
- [Anthropic — Persona Selection Model, 2026](https://www.anthropic.com/research/persona-selection-model)
- [Manus — Context Engineering for AI Agents, 2025](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
