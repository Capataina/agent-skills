# How to Write Effective Agent Skills

A comprehensive reference for designing, writing, and maintaining agent skills that maximise agent creativity, autonomy, and output quality while ensuring consistent, reproducible results.

## Table of Contents

1. [Foundational Principles](#1-foundational-principles)
2. [The Description — Your Most Important Line](#2-the-description--your-most-important-line)
3. [Instruction Design Philosophy](#3-instruction-design-philosophy)
4. [Progressive Disclosure and Context Engineering](#4-progressive-disclosure-and-context-engineering)
5. [Reference File Architecture](#5-reference-file-architecture)
6. [Writing Rich Reference File Content](#6-writing-rich-reference-file-content)
7. [Example Design — Guiding Without Biasing](#7-example-design--guiding-without-biasing)
8. [Anti-Pattern Sections — When They Help, When They Hurt](#8-anti-pattern-sections--when-they-help-when-they-hurt)
9. [Quality Assurance Design](#9-quality-assurance-design)
10. [Arbitrary Limits and When to Avoid Them](#10-arbitrary-limits-and-when-to-avoid-them)
11. [Content Quality and Bias Prevention](#11-content-quality-and-bias-prevention)
12. [Cross-Skill Coherence](#12-cross-skill-coherence)
13. [Post-Writing Verification](#13-post-writing-verification)
14. [Sources](#14-sources)

---

## 1. Foundational Principles

### The Agent Is Already Smart

The single most important design principle: **modern LLMs are already extremely capable.** Every piece of information in a skill should pass the challenge: "Does the agent really need this, or is it something the agent already knows?" Do not explain what PDFs are. Do not teach software engineering fundamentals. The skill's job is to provide what the agent *cannot* derive from its training — your specific conventions, your specific quality standards, your specific edge cases, and the reasoning behind them.

This does not mean skills should be thin. It means every token should carry signal. A 500-line SKILL.md where every line teaches the agent something it would not otherwise know is better than a 100-line SKILL.md padded with obvious instructions and a 200-line SKILL.md that wastes half its tokens restating common knowledge.

### Explain Why, Not Just What

Anthropic's own skill-creator captures this principle precisely:

> "Try hard to explain the **why** behind everything you're asking the model to do. Today's LLMs are *smart*. They have good theory of mind and when given a good harness can go beyond rote instructions and really make things happen."

When you explain *why* something matters, the agent generalises from the explanation. It can handle edge cases you never anticipated because it understands the underlying principle. When you only say *what* to do, the agent follows the letter of the instruction and may violate the spirit in novel situations.

**Example — rigid instruction:**
> Always use bullet lists for system document sections.

**Example — principled instruction:**
> Use the representation that makes the information clearest. Bullets work for concise takeaways, tables for dense inventories, diagrams for flows that are awkward in prose. The goal is maximum clarity for both human readers and future agents.

The second version produces better output across more situations because the agent understands the goal and can exercise judgment.

### The Bridge and Field Analogy

Calibrate instruction specificity based on risk:

- **Narrow bridge (high risk, one safe path):** Database migrations, file format specifications, API contracts. Provide exact instructions. The agent has no latitude because getting it wrong is catastrophic.
- **Open field (low risk, many valid paths):** Analysis, writing, creative exploration, code structure decisions. Provide direction and quality standards. The agent has full latitude because many good solutions exist.

Most of the content in this archive's skills falls on the "open field" end. The structural rules (folder layout, naming conventions, file roles) are narrow bridges. The content within those structures (how to explain a subsystem, what depth to reach, what visual representations to choose) is open field.

### Structure Fixed, Content Free

This principle directly follows from the bridge-and-field analogy. In skill design:

- **Fix the structure:** Folder layout, file naming, required sections, output locations, script execution order. These are deterministic and must be consistent.
- **Free the content:** How the agent explains things, what depth it reaches, what formatting it chooses, how it reasons about the domain. These are judgment calls where agent autonomy produces better results than rigid templates.

---

## 2. The Description — Your Most Important Line

### How Triggering Works

Skill triggering is pure LLM reasoning — no embeddings, no keyword matching, no classifiers. The agent reads the text description and decides whether it matches the user's intent. This means natural language quality directly determines activation accuracy.

Empirical data on description quality:

| Approach | Activation Success Rate |
|----------|------------------------|
| No optimisation | ~20% |
| Simple description | ~20% |
| Optimised description | ~50% |
| With trigger examples | 72–90% |

### Writing Effective Descriptions

1. **Write in third person.** "Analyses the codebase for..." not "I can help you..." or "Use this to..." The description is injected into the system prompt context, and inconsistent point-of-view causes discovery problems.

2. **Include both WHAT and WHEN.** Two-part structure: capability statement + trigger conditions. "Maintains a repository-level context folder as durable implementation memory. Use when asked to create, initialise, regenerate, audit, clean up, restructure, repair, or update a project's context/ documentation..."

3. **Be dense with trigger terms.** Include the exact phrases users would say, file types, domain terms, and adjacent vocabulary. A user who says "sweep for dead code" should trigger the same skill as one who says "code health audit."

4. **Include negative triggers for adjacent skills.** "Not for product specs, roadmaps, release notes, changelogs, or general-purpose prose docs." This prevents false activations when another skill is more appropriate.

5. **Make descriptions slightly assertive.** Instead of "How to do X," write "How to do X. Make sure to use this skill whenever the user mentions Y, Z, or wants to W, even if they do not explicitly ask for X."

6. **Maximum 1024 characters, aim for 200–400 dense characters.** Every character should carry trigger signal.

---

## 3. Instruction Design Philosophy

### Positive Framing Over Negative Constraints

Tell the agent what TO DO, not what NOT to do. Research consistently shows positive framing is more effective:

- Instead of "Do not use shallow bullet lists" → "Use the representation that makes the information clearest — tables, diagrams, trees, or bullets depending on the content."
- Instead of "Never create thin files" → "Every file should carry enough memory value that a reader understands the topic without needing to re-derive it from code."

### The ALWAYS/NEVER Yellow Flag

From Anthropic's skill-creator:

> "If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag — if possible, reframe and explain the reasoning so that the model understands why the thing you're asking for is important. That's a more humane, powerful, and effective approach."

Reserve emphatic language for genuinely inviolable rules (safety constraints, data integrity). For everything else, explain the principle and trust the agent.

### Consistent Terminology

Using "case," "ticket," and "issue" interchangeably confuses agents, especially as conversation length increases. Pick one term per concept across the entire skill and use it consistently. This applies across the skill ecosystem — if one skill calls it a "system file" and another calls it a "subsystem document," the agent treats them as different concepts.

### Instructions That Persist

LLMs exhibit a primacy-recency effect — they attend most to information at the beginning and end of context. Instructions in the middle of long interactions get progressively less attention. To combat this:

- Place the most critical rules early in the SKILL.md body.
- Use the quality checklist at the end as a recency anchor for important requirements.
- The agent's own note-taking (plans, progress tracking) pushes objectives into recent attention.

---

## 4. Progressive Disclosure and Context Engineering

### The Three-Level Loading System

Skills use progressive disclosure to manage context efficiently:

| Level | What Loads | When | Token Cost |
|-------|-----------|------|------------|
| 1 — Metadata | Name + description | Always at startup | ~100 tokens per skill |
| 2 — SKILL.md body | Core workflow instructions | When skill triggers | Under 5k tokens |
| 3 — Reference files | Detailed standards, templates, examples | On explicit demand | As needed |

This means you can have many skills installed without impacting performance on unrelated tasks. The cost is paid only when the skill activates.

### Context Is a Finite Resource

As token count in the context window increases, the model's ability to accurately recall information decreases proportionally. Every token has a cost — not in money, but in attention. This means:

- Do not front-load reference files that are only needed sometimes. Use conditional loading.
- Do not repeat the same information in multiple reference files.
- Do front-load references that are always needed. If every invocation requires all references, say so and load them all.

### Just-In-Time Context

Rather than pre-loading all context, maintain lightweight pointers (file paths, section references) and let the agent load detailed information on demand. This mirrors how humans work — we do not memorise entire reference manuals, we know where to look.

The skill should tell the agent what each reference file contains and when to read it, so the agent can decide what it needs for the current task.

---

## 5. Reference File Architecture

### When to Split vs Keep Inline

- **Keep in SKILL.md:** Core workflow instructions, quick-start information, navigation to reference files, inviolable rules, quality checklist.
- **Split to references:** Detailed templates, domain-specific standards, extensive examples, category taxonomies, format specifications, worked examples.
- **Hard limit:** SKILL.md body under 500 lines. This is a structural constraint, not a content constraint — the comprehensiveness lives in the reference files.

### Critical Rule: One Level Deep

Reference files should NOT point to other reference files. SKILL.md points to reference files. Reference files are terminal. When references nest, agents partially read files (using `head -100` or similar), resulting in incomplete information.

### Table of Contents in Long References

For reference files longer than 100 lines, include a table of contents at the top. This ensures the agent can see the full scope of available information even when previewing with partial reads.

### Naming

Name files descriptively. `analysis-categories.md` not `ref2.md`. `output-format.md` not `doc.md`. The agent navigates the skill directory like a filesystem — clear names help it find what it needs without reading the file.

---

## 6. Writing Rich Reference File Content

This is the hardest part of skill creation. Designing the folder structure is straightforward. Writing a 400-line reference file that is comprehensive, domain-agnostic, teaches through reasoning, and gives the agent freedom without losing quality — that is the craft.

### Calibrating Depth

Not every reference file needs the same depth. The right depth depends on three factors:

1. **How much judgment is involved.** A category taxonomy where the agent must decide which bucket a finding goes in needs extensive definitions, boundary guidance, and examples. A file naming convention where there is one right answer needs a short list.

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

**Show the structure, describe the intent.** For each section in a template, explain what the section is *for* — what question it answers, what value it provides to the reader. "Current State: What the code does now, grounded in the actual implementation. Include enough detail that an engineer can understand the issue without reading the code first." This tells the agent the purpose, not just the label.

**Vary template completeness across examples.** If you show one fully filled template as an example, also show a shorter one for a simpler finding. This teaches the agent that depth should be proportionate to the finding's complexity, not uniform.

**Templates are minimum structure, not maximum structure.** The agent should feel free to add sections, sub-sections, diagrams, tables, or other elements that improve clarity. The template defines what must be present, not what is allowed.

### Writing "Open Field" Content

The hardest reference files to write are the ones where the agent needs maximum creative freedom — detection strategies, analysis approaches, writing standards. These are "open field" content: the skill establishes direction and quality, but the agent determines the path.

**Teach reasoning patterns, not procedures.** Instead of "Step 1: Check file sizes. Step 2: Check function lengths. Step 3: Check nesting depth," write "Look for structural indicators of complexity — files significantly larger than their peers, functions with deep nesting or many branch points, modules that mix multiple responsibilities. The specific indicators depend on the language and project conventions."

**Use conditional guidance.** "If the system involves domain-specific algorithms (ML training, physics simulation, graph traversal), conduct targeted research to find established optimisation strategies for that specific domain. If the system is primarily data transformation and I/O, focus on allocation patterns, unnecessary copies, and hot-path waste."

**State the quality bar, not the procedure for reaching it.** "Every finding must include evidence from the actual code, not assumptions about what the code probably does" is a quality bar. "Read lines 1-100 of each file, then check for..." is a procedure. Quality bars empower; procedures constrain.

**Give the agent explicit permission to be creative.** "The structural rules in this skill are fixed. Everything within that structure is yours — how you explain a system, what depth you reach, what visual representations you choose, how you scope your research queries." This is not filler — it actively counteracts the agent's tendency to be conservative when it senses many rules.

---

## 7. Example Design — Guiding Without Biasing

### The Overfitting Risk

Examples are a double-edged sword. They point the agent in the right direction, but they carry the risk of overfitting — the agent copies the surface pattern of the example rather than understanding the underlying principle. This is especially dangerous when:

- All examples look similar (the agent learns the superficial format, not the underlying reasoning).
- Examples are domain-specific (the agent applies the domain to unrelated projects).
- Examples are too detailed (the agent treats specifics as requirements).

### Mitigation Strategies

1. **Use diverse examples.** Vary scenarios, input types, complexity levels, and domains. If the skill will be used across Rust, Python, TypeScript, and Go projects, include examples from multiple languages.

2. **Include rejected examples.** Show a finding that *looked* good but was rejected, and explain why. This teaches the agent the decision boundary, not just the positive space.

3. **Vary content, not just structure.** If every example has the same number of sections, the same tone, and the same depth, the agent will replicate that uniformity. Vary these dimensions to show the range of acceptable output.

4. **3–5 examples is optimal.** Research shows major gains after 2 examples, a plateau around 4–5, and diminishing returns beyond that. More examples burn tokens without improving output.

5. **Frame examples as illustrations, not templates.** "Here is an example of a good finding. Note how the justification connects the research to the specific code." This guides attention to the *principle* the example demonstrates, not the surface format.

6. **Keep examples generic or clearly hypothetical.** If an example references a specific technology, the agent may anchor on that technology when working on unrelated projects. Use examples that teach the format and reasoning without implying a specific domain.

---

## 8. Anti-Pattern Sections — When They Help, When They Hurt

### The Research

Anti-patterns have a nuanced effect:

- **Specific, well-explained anti-patterns work.** A study found that anti-pattern avoidance prompts reduced code weaknesses by 59–64%. The key is specificity and explanation of *why* the pattern is bad.
- **Vague negative instructions backfire.** "Don't make it bad" is noise. "Do not create milestone-based files because they force readers to reconstruct the present from historical slices" is signal.
- **Many negative instructions fragment attention.** A long list of "do not" items creates ambiguity about what the agent *should* do.

### Best Practice

1. Lead with the positive instruction. State what the agent should do first.
2. Add the anti-pattern as context for *why* the positive instruction matters.
3. Keep anti-patterns few and specific. Each one should describe a concrete failure mode with a clear explanation of the harm.
4. Consider whether the anti-pattern can be reframed as a positive instruction instead.

---

## 9. Quality Assurance Design

### Self-Evaluation Checklists

Quality checklists at the end of a skill serve two purposes:

1. **Verification:** The agent uses them to check its own output before presenting it.
2. **Recency anchoring:** Items at the end of the skill body receive strong attention due to the recency effect.

### Checklist Design Rules

- Every item must be concrete and verifiable. "Is it good?" is useless. "Every finding includes the full proof chain: current state, proposed change, justification, expected benefit, behavioural impact assessment" is verifiable.
- Do not duplicate the instructions. The checklist confirms that the instructions were followed, it does not restate them.
- Keep the checklist proportionate. A simple skill needs 5–8 items. A complex skill might need 12–15. More than 15 starts diluting attention.

---

## 10. Arbitrary Limits and When to Avoid Them

### The Problem with Rigid Numeric Constraints

Rigid limits (word counts, file counts, section counts, character limits) constrain agent autonomy without improving output quality. They are appropriate only when:

- The limit is structural (SKILL.md under 500 lines — a context engineering constraint).
- The limit prevents a known failure mode (plan file accumulation — a proven anti-pattern).
- The limit is a floor, not a ceiling (minimum 30 non-empty lines for system docs — a shallow-document detector).

### When Limits Harm

Limits harm when they prevent the agent from making good judgment calls:

- "Maximum 3 note files" prevents thorough note-taking in complex projects.
- "Each section must be 100–200 words" forces padding in simple sections and truncation in complex ones.
- "No more than 5 categories" prevents the agent from capturing a finding that does not fit the taxonomy.
- "Sections that should not exist" prevents the agent from adapting to project-specific needs.

### The Better Alternative

Instead of numeric limits, state the principle and the failure mode:

- Instead of "maximum 3 plan files" → "Plans are temporary execution aids. Remove them when complete. Do not let stale plans accumulate."
- Instead of "sections must be 100–200 words" → "Each section should carry enough information to be useful. If a section can be said in one line, say it in one line. If it needs a page, give it a page."
- Instead of "these sections must not exist" → "Avoid vague catch-all sections. Every section should have a clear topic and canonical home."

This gives the agent the constraint (do not accumulate, do not pad, do not dump) without removing the judgment call about how to satisfy it.

---

## 11. Content Quality and Bias Prevention

A well-structured skill can still produce poor agent output if the *content* within that structure has quality issues. Structure is the skeleton; content is the muscle. Both must be right.

### Domain Bias in Examples

Examples are the single strongest influence on agent output — and the single biggest source of unintentional bias. Research confirms this is not hypothetical:

**"The programs in the prompt will bias the model towards generating similar programs and ignore the specification"** (Huang et al., 2023, ACM TOSEM). Models rely on generating "arbitrary, commonly used snippets that vaguely fit for the block by only observing patterns in the examples." If every example in a skill references machine learning, the agent will anchor on ML patterns when working on a web app.

The landmark paper "Rethinking the Role of Demonstrations" (Min et al., EMNLP 2022) demonstrated that what examples primarily teach is **format, distribution, and label space** — not content. Ground truth labels barely matter. What matters is the surface structure, vocabulary, and domain of the examples. This means domain bias in examples leaks directly into the agent's understanding of the task itself.

Further research on **induction heads** (Olsson et al., 2022) shows that attention mechanisms literally "replicate previous patterns for next-token prediction" — the model copies demonstration patterns rather than extracting underlying principles. **Surface form competition** means multiple terms referring to the same concept fight for probability mass, so the specific vocabulary in examples directly biases output vocabulary.

**The test:** Read every example in the skill and ask: "If an agent read only these examples, would it think this skill is designed for one specific kind of project?" If yes, the examples need diversification.

**The standard:** Examples across a skill should span at least 2–3 different domains (web services, data pipelines, CLI tools, desktop applications, infrastructure, etc.). No single domain should represent more than half the examples in any file.

**Template examples are highest risk.** Templates are used as direct structural patterns. If a template's worked example uses domain-specific names (like `reinforcement-learning-path.md` or `replay-buffer.rs`), agents will produce output shaped by that domain even when working on something completely different.

### Instruction Coherence

Instructions within a skill must not contradict each other. Research shows this matters more than you might expect:

The paper "LLMs can be easily Confused by Instructional Distractions" (2025) tested six models and found average accuracy on distraction-laden tasks dropped to **30.1%**. When instructions compete with each other for the agent's attention, compliance on all instructions degrades — not just the contradicting pair.

The paper "The Instruction Gap" (2025) found that **instruction compliance and accuracy are independent dimensions** — models that follow all instructions don't necessarily provide accurate answers, and accurate models may struggle with instruction compliance. This means a contradicting instruction can degrade compliance broadly without visibly breaking any single output.

Common contradiction patterns:

- A principle section says "use your judgment to choose the best format" but a later section says "always use bullet lists for this section."
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

Research consistently shows positive framing outperforms negative framing. Analysis of the "Pink Elephant Problem" in LLMs draws on Ironic Process Theory — telling the model "don't do X" forces it to process X, potentially producing it. Real-world evidence: users report LLMs produce worse outputs with more "DO NOTs" in prompts. Anthropic's official documentation explicitly advises telling the agent what to do rather than what not to do.

Research on emphasis (2024) found that **small open-source LLMs struggle to understand emphasised text**, while commercial LLMs **may overinterpret emphasised text**. Stricter format constraints generally lead to greater performance degradation in reasoning tasks.

Every instruction in the skill should be evaluated:

- **Does it explain *why*?** An instruction with reasoning produces generalised understanding. An instruction without reasoning produces rote compliance.
- **Is it framed positively?** Lead with what to do. Add what not to do as context, not as the primary instruction.
- **Does it use proportionate emphasis?** Reserve ALWAYS/NEVER for genuinely inviolable constraints. For everything else, explain the reasoning.

### Autonomy-Restricting Language

The Sonar Foundation Agent case study (2025) provides direct evidence: with a highly detailed, prescriptive prompt, their agent achieved **~70% efficacy**. After distilling to a concise, principle-based prompt: **75% efficacy**. Their conclusion: "As underlying models grow more powerful, we must grant them more autonomy."

The IFScale benchmark (2025) quantifies instruction saturation: even frontier models achieve only **68% accuracy at 500 instructions**. Reasoning models maintain near-perfect compliance until ~150 instructions, then crash. Beyond the saturation point, models shift overwhelmingly toward **omission errors** — they abandon instructions entirely rather than partially complying.

The paper "What Prompts Don't Say" (2025) found a critical paradox: specifying all requirements simultaneously **backfires** — with 19 requirements specified, accuracy drops to 85% from a 98.7% baseline.

Scan every instruction for language that unnecessarily restricts agent creativity:

- "Must always" / "must never" — is this genuinely inviolable, or would a principle with reasoning be better?
- "Exactly 5 sections" / "maximum 3 files" / "between 100-200 words" — is this numeric limit structural or arbitrary?
- "These sections should not exist" / "never create these files" — is there a scenario where the agent's judgment should override this?

The goal is that an agent reading the skill feels empowered to make good decisions within a clear framework, not constrained by a rigid script that fights the model's own reasoning capabilities.

---

## 12. Cross-Skill Coherence

### The Coordination Problem

When multiple skills exist in the same ecosystem, they can conflict — different terminology, overlapping triggers, contradictory instructions. Agents exposed to conflicting instructions lose confidence and produce inconsistent output.

### Strategies

1. **Consistent terminology across all skills.** If one skill calls it a "system file," all skills call it a "system file."
2. **Non-overlapping triggers.** Make descriptions mutually exclusive with clear boundaries. Include negative triggers for adjacent skills.
3. **Do not reference skills by name inside other skills.** Reference artefact patterns instead ("some files in context/references/ follow a multi-section research paper structure"). Only the personality/coordinator knows about all skills.
4. **Each skill is self-contained.** A skill should have everything it needs within its own directory.
5. **The personality is the coordinator.** It knows about all skills, how they relate, and when to invoke each one. Skills are specialists that do not know about each other.

---

## 13. Post-Writing Verification

After writing or editing any skill, run through these verification checks. No automated tools exist for multi-file prompt coherence checking — this is entirely manual work today (the research confirms this gap). These checks catch the kinds of issues that are invisible during writing but create real problems when agents use the skill.

### Bias and Diversity Check

- Read every example, template, and worked scenario across the entire skill directory. Are they drawn from at least 2–3 different domains? Would an agent working on any type of project (web service, game, CLI tool, data pipeline, mobile app, infrastructure) find the examples relatable and non-anchoring?
- Pay special attention to template files — these have the highest contamination risk because agents use them as direct structural patterns.
- Check that example titles, file names, variable names, and function names do not anchor on one domain. `select_experiences()` anchors on ML. `process_batch()` is generic.

### Coherence Check

- Read the SKILL.md and every reference file looking for instructions that contradict each other, even subtly. A "use judgment" instruction in one place and an "always do X" instruction in another is a contradiction.
- Verify that the quality checklist at the end of SKILL.md is consistent with the instructions in the body and reference files.
- Check that the description in the YAML frontmatter accurately reflects what the skill actually does.

### Terminology Check

- List the 5–10 most important concepts in the skill. Search the entire skill directory for each one. Is the same term used consistently?
- Check terminology against other skills in the ecosystem. A concept that appears in multiple skills should use the same term everywhere.

### Reference Integrity Check

- After any structural change (file rename, folder restructure, concept reorganisation), search the entire skill directory for the old names. Every stale reference must be updated.
- Verify that every file referenced in SKILL.md's reference loading instructions actually exists with that exact filename.
- Verify that reference files do not point to other reference files (one level deep rule).

### Framing Check

- Search for ALWAYS, NEVER, MUST, and MUST NOT in capitals. For each one, ask: does this need to be this emphatic, or would a principle with reasoning be better?
- Search for negative instructions ("do not", "never", "avoid"). For each one, ask: is there a positive framing that teaches the same lesson?
- Verify that every major instruction includes a *why* — not just what to do, but why it matters.

### Autonomy Check

- Search for numeric constraints (word counts, file counts, section counts, character limits). For each one, ask: is this structural (context engineering) or arbitrary (restricting judgment)?
- Search for prohibitions on specific sections, files, or formats. Are there legitimate scenarios where the agent should be allowed to make a different choice?
- Read the skill from the perspective of a highly capable agent: does it feel like an empowering framework or a restrictive script?

### Cross-Skill Check (when the skill is part of an ecosystem)

- Verify that the skill does not reference other skills by name — only artefact patterns.
- Verify that trigger descriptions do not overlap with other skills. Include negative triggers where needed.
- Check that the skill is fully self-contained — it should not depend on the reader knowing about other skills.

---

## 14. Sources

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
- [Bias Testing and Mitigation in LLM-based Code Generation — Huang et al., ACM TOSEM 2023](https://arxiv.org/abs/2309.14345)
- [LLMs can be easily Confused by Instructional Distractions, 2025](https://arxiv.org/html/2502.04362v1)
- [The Instruction Gap: LLMs get lost in Following Instructions, 2025](https://arxiv.org/html/2601.03269)
- [What Prompts Don't Say: Understanding Underspecification, 2025](https://arxiv.org/html/2505.13360v2)
- [Quantifying LLMs' Sensitivity and Consistency to Prompt Engineering, 2024](https://arxiv.org/html/2406.12334v1)
- [How Many Instructions Can LLMs Follow at Once? — IFScale, 2025](https://arxiv.org/html/2507.11538v1)
- [The Pink Elephant Problem — Negative Instructions in LLMs](https://eval.16x.engineer/blog/the-pink-elephant-negative-instructions-llms-effectiveness-analysis)
- [Introducing Sonar Foundation Agent — Sonar, 2025](https://www.sonarsource.com/blog/introducing-sonar-foundation-agent/)
- [Does Prompt Formatting Have Any Impact on LLM Performance?, 2024](https://arxiv.org/html/2411.10541v1)
- [PromptDoctor: Automated Prompt Linting and Repair, 2025](https://arxiv.org/abs/2501.12521)
- [Context Rot — Chroma Research, 2025](https://research.trychroma.com/context-rot)
