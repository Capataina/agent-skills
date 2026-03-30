# How to Write Effective Agent Personalities

A comprehensive reference for designing personality files (CLAUDE.md, system prompts, custom instructions) that reliably shape agent behaviour while maximising autonomy, creativity, and sustained instruction-following across long conversations.

## Table of Contents

1. [What a Personality File Is](#1-what-a-personality-file-is)
2. [Structure and Ordering](#2-structure-and-ordering)
3. [Behavioural Instruction Design](#3-behavioural-instruction-design)
4. [Balancing Control and Autonomy](#4-balancing-control-and-autonomy)
5. [Startup Routines](#5-startup-routines)
6. [Session Modes](#6-session-modes)
7. [Documentation Upkeep Instructions](#7-documentation-upkeep-instructions)
8. [Skill Ecosystem Coordination](#8-skill-ecosystem-coordination)
9. [Source Hierarchies and Operational Loops](#9-source-hierarchies-and-operational-loops)
10. [Communication Style](#10-communication-style)
11. [Instruction Persistence Across Long Conversations](#11-instruction-persistence-across-long-conversations)
12. [Content Quality and Consistency](#12-content-quality-and-consistency)
13. [Post-Writing Verification](#13-post-writing-verification)
14. [Context Budget and Length](#14-context-budget-and-length)
15. [Sources](#15-sources)

---

## 1. What a Personality File Is

A personality file is the highest-leverage configuration point in an agent system. It shapes every interaction — how the agent reasons, what it prioritises, how it communicates, when it acts autonomously, and when it defers. It is loaded at the start of every conversation and remains in context throughout.

A personality file is NOT:

- A tutorial for the agent on how software engineering works (the agent already knows).
- A comprehensive reference manual (that is what skills are for).
- A list of every rule the agent should follow (instruction-following degrades with instruction count).
- A repository documentation file (it documents the agent's behaviour, not the codebase).

A personality file IS:

- The agent's operating charter — who it is, how it works, what it prioritises.
- The coordinator layer that connects skills, sources, and workflows.
- The place where project-specific norms and conventions are established.
- The highest-signal, most-persistent context the agent receives.

### The Hierarchy

Most agent systems support multiple personality layers:

| Level | Claude Code Location | Purpose |
|-------|---------------------|---------|
| Global | `~/.claude/CLAUDE.md` | Personal preferences across all projects |
| Project | `CLAUDE.md` in repo root | Team conventions, committed to git |
| Local | `.claude/local.md` | Personal overrides, gitignored |
| Subdirectory | `subdir/CLAUDE.md` | Directory-specific context, loaded on demand |

Project-level is the primary target for team-shared personality files. Global is for personal style preferences. Subdirectory files enable progressive disclosure in monorepos.

---

## 2. Structure and Ordering

### The Primacy-Recency Effect

LLMs attend most strongly to information at the beginning and end of their context, with the middle receiving diminished attention. This directly determines how personality files should be structured:

- **Beginning:** Identity, role, and the most critical behavioural rules (primacy effect).
- **Middle:** Operational details — startup routines, source hierarchies, modes, upkeep instructions.
- **End:** Quality standards, review procedures, and communication style (recency effect).

### Recommended Section Order

1. **Role and identity** — Who the agent is and what its job is. This activates the right reasoning mode.
2. **Universal output standards** — How the agent should approach all output (depth, formatting, explanation style).
3. **Startup behaviour** — What to read and do at the beginning of every session.
4. **Source hierarchy** — What sources to trust and in what order.
5. **Session modes** — How the agent should operate in different contexts.
6. **Incremental upkeep** — How to maintain documentation and context during normal work.
7. **Skill ecosystem** — What specialist skills exist and when to invoke them.
8. **Engineering standards** — Code quality expectations.
9. **Operating loop** — The step-by-step workflow for each task.
10. **Review and verification** — How to validate work.
11. **Communication style** — Formatting, tone, verbosity norms.

### Why This Order Works

- The role definition (section 1) is the highest-leverage instruction. It frames everything that follows.
- Output standards (section 2) are referenced constantly, so they benefit from early positioning.
- Startup (section 3) is only used once per session, but it sets the tone, so it belongs early.
- Communication style (section 11) is a recency anchor — the last thing the agent reads before responding.

---

## 3. Behavioural Instruction Design

### What Makes Instructions the Agent Actually Follows

**Clarity and directness matter more than emphasis.** Claude 4.6 is more responsive to system prompts than previous models. Aggressive language ("CRITICAL: You MUST...") can cause overtriggering. Normal prompting ("Use this tool when...") is more reliable.

**Positive framing over negative constraints.** Instead of "Do not use shallow bullet lists," write "Use the representation that makes the information clearest." The agent generalises from positive examples better than negative prohibitions.

**Context and motivation behind instructions.** Explaining *why* enables generalisation. Instead of "Never use ellipses," write "Your response will be read aloud by a text-to-speech engine, so never use ellipses since the engine cannot pronounce them." The agent now avoids all unpronounceables, not just ellipses.

**Examples over rules.** "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." Include 3–5 examples for best results. One well-chosen example teaches more than a paragraph of abstract rules.

**Instruction count matters.** Research suggests frontier LLMs can follow approximately 150–200 instructions with reasonable consistency. Claude Code's own system prompt already contains ~50 instructions, leaving ~100–150 for the personality file and loaded skills combined. As count increases, following quality decreases uniformly. Every instruction must earn its place.

### The Golden Rule

> "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too."

---

## 4. Balancing Control and Autonomy

### The Research

Anthropic's analysis of millions of agent interactions found:

- Most agent actions (80%) are low-risk and reversible, with only 0.8% truly irreversible.
- Experienced users auto-approve more frequently but also interrupt more often, indicating a shift from approval-based to monitoring-based oversight.
- Existing models are capable of more autonomy than they exercise in practice.

ThoughtWorks' experimentation found no clear winner between highly constrained and minimally constrained approaches:

- **Under-constraining:** Agents fill gaps with assumptions, generate unrequested features, change priorities without instruction.
- **Over-constraining:** Excessive instructions create internal contradictions. Deterministic checkpoints paradoxically fail as agents find ways around them.

### The Principle

The personality file should establish:

1. **Hard constraints** for irreversible or high-risk actions (narrow bridges). These are few and absolute.
2. **Quality standards** that define what good output looks like, without prescribing how to achieve it (open fields).
3. **Judgment guidelines** that teach the agent *how to think* about decisions rather than making every decision for it.

The best personality files read like onboarding documents for a senior engineer — they explain the project's values, conventions, and expectations, then trust the engineer to exercise judgment within that framework.

### What NOT to Control

- Do not micromanage code style — that is the linter's job.
- Do not prescribe exact formatting for every output type — teach the principles and let the agent choose.
- Do not list every possible edge case — explain the underlying principle and the agent will handle novel cases.
- Do not add redundant safety checks — the agent's base training already includes safety.

---

## 5. Startup Routines

### Purpose

The startup routine establishes the agent's understanding of the project before it takes any action. It answers: What is this project? What state is it in? What does the user likely need?

### Design Principles

1. **Read the minimum needed to orient, then pull more on demand.** Do not load all context files at startup. Load the structural map (architecture) and the preference layer (notes), then pull specific system files when the task requires them.

2. **Do not block startup on missing files.** If a context folder does not exist, note it and recommend creating it — do not refuse to work. The agent should degrade gracefully.

3. **Summarise what you learned.** The startup summary serves two purposes: it confirms to the user that the agent understands the project, and it anchors the agent's own understanding.

4. **Ask a focusing question.** After the summary, ask what the user wants to do. This prevents the agent from guessing and going in the wrong direction.

### What to Avoid

- Loading the entire `context/` folder at startup — wastes context tokens on information that may not be relevant.
- Reading code at startup unless the task clearly requires it — startup should be fast.
- Running heavy analysis at startup — that is what skills are for.
- Loading `learning/` at startup — educational material is reference, not startup context.

---

## 6. Session Modes

### When Modes Help

Modes are useful when the agent needs to operate fundamentally differently depending on the user's intent. The key distinction is usually between:

- **Planning/teaching mode:** The agent reasons about what to do but does not execute. It explains, plans, reviews, and teaches.
- **Implementation mode:** The agent executes — writes code, edits files, runs commands.

### Design Principles

1. **Choose mode once at startup.** Repeated mode switching creates confusion and inconsistency.
2. **Make mode boundaries clear.** What is allowed in each mode, what is not.
3. **Upkeep is mode-independent.** Documentation maintenance should happen in both modes. The mode controls production-code behaviour, not the agent's responsibility to keep context current.
4. **Allow explicit switching.** The user can change modes, but the agent should not switch on its own.

---

## 7. Documentation Upkeep Instructions

### The Core Challenge

Writing initial documentation is straightforward. Maintaining accuracy as codebases evolve is the genuine challenge. The personality must instruct the agent to maintain documentation continuously and incrementally, not just during dedicated upkeep passes.

### Design Principles

1. **Make upkeep a continuous responsibility, not an event.** The agent should update documentation as part of completing any task that changes the project. Do not wait for the user to ask.

2. **Proportionate changes.** A small code change gets a small doc update. A large architectural shift gets a large doc update. The agent should use judgment about what level of update is needed.

3. **Note capture is real-time.** When design decisions, preferences, or trial-and-error outcomes surface during normal work, capture them immediately — do not defer to the next upkeep pass.

4. **Plan maintenance is ongoing.** When implementation work completes items in a plan, tick the checkboxes. When all criteria are met, remove the plan.

5. **Skills are for large passes.** The personality should handle routine, targeted updates inline. Skills are invoked when accumulated drift is too broad for inline edits to handle reliably. Always ask before invoking a skill — they consume significant context.

---

## 8. Skill Ecosystem Coordination

### The Personality as Coordinator

The personality file is the only place that knows about all skills and how they relate. Each skill is a self-contained specialist that does not know about other skills. The personality orchestrates by:

- Knowing what each skill does and when to invoke it.
- Understanding how skill outputs interact (one skill's output feeds into another's input).
- Deciding when accumulated drift warrants a full skill pass vs inline edits.
- Asking the user before invoking any skill (skills are heavy-weight operations).

### Describing Skills in the Personality

For each skill, include:

1. **What it does** (one paragraph). Write this as a capability description, not a technical summary. "Maintains context/ as the repository's implementation memory layer. Runs a repo scan script, then produces or updates architecture, system, and supporting files" tells the agent what the skill delivers.
2. **When to invoke it** (concrete conditions). List specific, observable triggers: "accumulated drift is too broad for inline edits," "multiple subsystems were created or retired," "the architecture has shifted substantially." Avoid vague triggers like "when needed."
3. **When NOT to invoke it** (to prevent unnecessary invocations). This is especially important because skills consume significant context. "Do not invoke for adding one system file or updating a single document — handle those inline."

### The Relationship Map

After describing individual skills, include a section showing how they interact. This is the coordination map — it tells the agent how data flows between skills and prevents it from invoking skills in the wrong order or misunderstanding outputs.

The relationship map works best as a visual (ASCII diagram or tree) followed by prose that explains the flow:

```
skill-A  ──writes to──►  folder-X/
                              │
skill-B  ──governs──────►  folder-Y/  (includes folder-X/)
                              │
                         read by all skills before generating output
```

The prose should explain: What does each skill write? What does each skill read? How does the output of one skill become the input for another? What is the dependency order?

### Invocation Etiquette

The personality should establish clear norms for skill invocation:

- **Always ask before invoking.** Skills are heavy-weight operations that consume significant context. The agent should recommend a skill run and give a concrete reason, then wait for the user to confirm.
- **Name the specific skill.** "I recommend running upkeep-context because we've made significant changes across multiple subsystems" is actionable. "Maybe we should update the docs" is not.
- **Distinguish inline work from skill work.** The agent should develop judgment about the threshold between "I can handle this with a targeted edit" and "this needs a full skill pass." The personality should describe this threshold in terms of observable conditions, not feelings.

### The Rule

Never reference skills by name inside other skills. Skills reference artefact patterns ("plan files in context/plans/"). Only the personality references skill names, because only the personality is the coordinator.

---

## 9. Source Hierarchies and Operational Loops

### Writing a Source Hierarchy

Most projects have multiple sources of truth that can conflict: a README, context files, the code itself, learning material. The personality should establish a clear priority order so the agent knows what to trust when sources disagree.

A well-written source hierarchy:

1. **Names each source** and its semantic role. "README.md: project intent, scope, direction" tells the agent what kind of truth to extract from the README.
2. **Establishes priority** for different kinds of questions. Code determines implementation reality. The README determines intended direction. Context files are the maintained memory layer. Priority depends on what question the agent is answering.
3. **Describes conflict resolution.** "If context/ says feature X exists but the code has no trace of it, the code wins — context/ has drifted and needs updating." This prevents the agent from trusting stale documentation over observed reality.

### Writing an Operational Loop

The operational loop is the per-task workflow the agent follows. It reinforces the personality's values through repetition — every cycle through the loop naturally reminds the agent to ground in context, clarify scope, verify work, and update documentation.

Effective operational loops:

1. **Ground the next step** in existing sources (context, README, conversation).
2. **Clarify scope and trade-offs** before acting.
3. **Execute** (in implementation mode) or **explain** (in teaching mode).
4. **Verify** against intent, interfaces, and documentation.
5. **Update** context and learning material where the work created drift.
6. **Assess** whether accumulated drift warrants a full skill pass.

The loop should be short enough to memorise and general enough to apply to any task. It should not prescribe specific actions — it describes the *rhythm* of the agent's work.

### Why the Loop Matters for Persistence

Research on instruction fade-out shows that LLM instruction adherence decays over long conversations. The operational loop combats this because the agent executes it every cycle, naturally reinforcing the personality's priorities (ground in context, update documentation, assess drift) without needing to re-read the personality file.

---

## 10. Communication Style

### Controlling Verbosity

Be explicit about when different verbosity levels apply:

- **In chat:** Direct, concise, technically rigorous. Do not pad responses.
- **In files:** Thorough, comprehensive, richly formatted. Depth is a virtue.

This distinction is critical. If you just say "be concise," the agent will be concise everywhere — including in context files and learning material where depth is the goal. If you just say "be thorough," the agent will write three paragraphs of chat response where one sentence would do.

The personality should make the boundary explicit: "These communication norms apply to chat conversation. When generating or editing files in context/, learning/, or context/references/, the Universal Output Standard governs depth and formatting — not the brevity norms below."

### Formatting and Creative Freedom

Give the agent maximum creative freedom in choosing formats, but establish the principle: use the representation that makes the information clearest. Tables for comparisons, trees for structure, diagrams for flows, bullets for takeaways. ASCII visualisations, heat maps, bar charts, class anatomy boxes — if the information has a shape, draw it.

The personality should actively encourage varied representation rather than defaulting to bullets. "Use the full expressive range of markdown and formatting. Prefer varied, rich representation over undifferentiated bullet lists when it improves understanding." This counteracts the agent's natural tendency toward bullet-list monotony.

### Adapting to the Medium

Chat interfaces may not render complex ASCII tables or diagrams well. The personality should acknowledge this: "In this chat interface, prefer clear and varied depictions, but use judgment — complex ASCII tables may not render cleanly in chat. Adapt the representation to the medium." This gives the agent permission to simplify in chat while going deep in files.

---

## 11. Instruction Persistence Across Long Conversations

### The Problem

Instructions fade over long conversations. The primacy-recency effect means middle-of-conversation instructions receive less attention. This is especially problematic for personality files that must shape behaviour across sessions with many tool calls.

### Strategies

1. **Structured note-taking.** The agent maintains its own notes (plans, progress, to-do lists) that push objectives into recent attention. This is why the todo.md / plan file pattern is so effective.

2. **Self-reinforcing workflows.** The operating loop (ground in context → clarify scope → implement → update docs) naturally reinforces the personality's values each cycle.

3. **Quality checklists as recency anchors.** End skill invocations with verification steps that restate the important rules.

4. **The personality's own structure.** By placing identity and output standards early and communication style late, the personality file exploits the primacy-recency effect.

---

## 12. Content Quality and Consistency

### The Personality-Skill Boundary

The most common content quality issue in personality files is scope creep — the personality accumulates detailed "how to" instructions that belong in skills. Research shows why this matters:

1. **Context bloat degrades everything.** Chroma's research (2025) found that every single frontier model gets worse as input length increases — adding full context (~113k tokens) reduces accuracy by **30%** compared to focused versions. The personality is loaded every session. Every token of detailed skill-level instruction in the personality degrades the agent's performance on every task, even when those instructions are irrelevant.

2. **Instruction conflicts cause broad degradation.** The paper "LLMs can be easily Confused by Instructional Distractions" (2025) found average accuracy dropped to **30.1%** on tasks with competing instructions. When the personality says "do X this way" and the skill says "do X that way," compliance degrades across *all* instructions, not just the conflicting pair.

3. **Instruction saturation is real.** The IFScale benchmark (2025) found reasoning models maintain near-perfect compliance until ~150 instructions, then crash. Claude Code's own system prompt already contains ~50 instructions. The personality and loaded skills share the remaining budget. Every instruction in the personality that could be in a skill is wasting a slot in this limited budget.

**The principle:** The personality should say *when* and *what* — when to invoke a skill, what role it plays, what triggers justify it. The skills should say *how* — the detailed process, templates, standards, and quality checks.

**The test:** For each instruction in the personality, ask: "Is this about when to do something (personality's job) or how to do it (skill's job)?" If it is about "how," it probably belongs in the skill.

### Instruction Framing in Personalities

Everything from the skill writing research about instruction framing applies to personalities, with one critical addition: personality instructions are read at the start of *every* session, so framing issues compound. A single poorly framed instruction in a skill is encountered only when that skill triggers. A poorly framed instruction in the personality is encountered hundreds of times.

Research on the "Pink Elephant Problem" confirms that negative instructions ("don't do X") force the model to process X, potentially producing it. The paper "What Prompts Don't Say" (2025) found that specifying all requirements simultaneously **backfires** — with 19 requirements, accuracy drops to 85% from a 98.7% baseline. The Sonar Foundation Agent case study found that distilling a prescriptive prompt to principle-based improved efficacy from 70% to 75%. These findings compound in personalities because the personality is always loaded.

Specific personality framing checks:

- **Startup instructions should enable, not prohibit.** "Read context/ and README.md first for fast orientation; pull additional files when the task requires them" is better than "Do not read learning/ at startup. Do not explore code at startup."
- **Mode instructions should be flexible.** "Ask the user whether they want teaching or implementation; if their message already makes it clear, confirm and proceed" is better than "Ask exactly this question and stop."
- **Upkeep instructions should describe the responsibility, not the procedure.** "Keep context/ and learning/ current throughout the session by making proportionate updates when the project changes" is better than a detailed list of every allowed action.

### Consistency Across the Personality-Skill Ecosystem

The personality and all skills must present a consistent worldview:

- **Same terminology.** If the personality calls them "plan files," no skill should call them "implement-now files."
- **Same folder model.** If the personality describes a `notes/` folder, no skill should still reference `decisions/`.
- **Same philosophical stance.** If the personality says "depth is a virtue, not a problem," no skill should instruct the agent to "keep it brief."
- **Same formatting philosophy.** If the personality encourages rich markdown (tables, diagrams, trees), no skill should restrict the agent to bullets.

---

## 13. Post-Writing Verification

After writing or editing a personality file, verify these dimensions:

### Scope Check

- For each instruction, ask: "Does this belong in the personality (when/what) or in a skill (how)?" Move detailed procedural instructions to the relevant skill.
- Check that the personality does not duplicate instructions that already exist in skills. Duplication creates drift risk — when the skill is updated, the personality's copy becomes stale.

### Consistency Check

- Read the personality alongside every skill it references. Do they agree on terminology, folder structure, philosophical stance, and formatting expectations?
- Check that the skill ecosystem section accurately reflects what each skill actually does. Skill descriptions in the personality should match the skills' own YAML descriptions in spirit.

### Framing Check

- Search for negative prohibitions. Can they be reframed as positive instructions with reasoning?
- Search for rigid phrasing ("exactly this question," "always do X," "never do Y"). Is the rigidity justified, or would flexibility produce better results?
- Verify that every constraint includes reasoning — not just what the rule is, but why it exists.

### Persistence Check

- Are the most critical instructions placed early (primacy effect) and late (recency effect)?
- Are there instructions that will drift during long conversations? If so, are there structural mechanisms (operating loop, quality checks, note-taking) that reinforce them?

### Budget Check

- Is the personality as short as it can be while retaining all genuinely personality-level instructions?
- Could any section be offloaded to a skill that loads on demand instead of every session?

---

## 14. Context Budget and Length

### The Research

- Claude Code's system prompt contains ~50 instructions. Adding a personality file adds to this total.
- Research suggests ~150–200 instructions is the reliable following limit for frontier models.
- Personality files beyond ~60–80 lines risk instruction dilution, where later instructions get less attention.
- Prompt bloat research shows reasoning performance degrades at around 3,000 tokens of instruction.

### The Practical Approach

The personality file should be:

- **Short in the personality file itself** — only what applies broadly to every session.
- **Expansive in the files it points to** — skills, references, and context files carry the detailed instructions.
- **High signal density** — every line should pass the test: "Would removing this cause the agent to make mistakes?"

This does not mean the personality should be stripped to a skeleton. It means the personality should contain the *right* information at the *right* density. A 200-line personality file where every line shapes behaviour is better than a 50-line file that omits important guidance.

The key is offloading. Detailed instructions about *how to maintain context files* belong in the upkeep skill, not the personality. Detailed instructions about *how to write research papers* belong in the research skill. The personality says *when* to invoke these skills and *what role they play* — the skills themselves carry the detailed instructions.

---

## 15. Sources

### Personality Design and Instruction Writing
- [Anthropic — Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Anthropic — Prompting Best Practices for Claude 4.6](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices)
- [Anthropic — Measuring AI Agent Autonomy](https://www.anthropic.com/research/measuring-agent-autonomy)
- [Anthropic — Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices)
- [HumanLayer — Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [Martin Fowler — How Far Can We Push AI Autonomy in Code Generation?](https://martinfowler.com/articles/pushing-ai-autonomy.html)
- [Manus — Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Roo Code — System Prompt and Modes](https://deepwiki.com/RooCodeInc/Roo-Code/9-settings-and-configuration)
- [Tetrate — System Prompts: Design Patterns and Best Practices](https://tetrate.io/learn/ai/system-prompts-guide)
- [Datagrid — How to Stop AI Agent Personalities from Drifting in Production](https://datagrid.com/blog/how-to-stop-ai-agent-personalities-from-drifting-in-production)
- [Ability.ai — Documentation as Agent Cognitive Model](https://www.ability.ai/blog/docs-as-agent-cognitive-model)
- [OpenAI — GPT-4.1 Prompting Guide](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide)
- [Packmind — Writing AI Coding Agent Context Files](https://packmind.com/evaluate-context-ai-coding-agent/)

### Content Quality and Verification Research
- [Context Rot — Chroma Research, 2025](https://research.trychroma.com/context-rot)
- [LLMs can be easily Confused by Instructional Distractions, 2025](https://arxiv.org/html/2502.04362v1)
- [How Many Instructions Can LLMs Follow at Once? — IFScale, 2025](https://arxiv.org/html/2507.11538v1)
- [What Prompts Don't Say: Understanding Underspecification, 2025](https://arxiv.org/html/2505.13360v2)
- [The Pink Elephant Problem — Negative Instructions in LLMs](https://eval.16x.engineer/blog/the-pink-elephant-negative-instructions-llms-effectiveness-analysis)
- [Introducing Sonar Foundation Agent — Sonar, 2025](https://www.sonarsource.com/blog/introducing-sonar-foundation-agent/)
