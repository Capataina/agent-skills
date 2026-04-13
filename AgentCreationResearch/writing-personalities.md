# How to Evaluate and Write Effective Agent Personalities

A comprehensive quality evaluation reference for personality files (CLAUDE.md, system prompts, custom instructions). This document defines what good looks like at every level of detail — from overall structure to individual sentence craft. If you read this file and nothing else, you should know exactly how to evaluate a personality file, what patterns produce strong results, what failures to watch for, and how to test whether a personality works.

This is not a process document. It does not describe the steps for creating a personality (that varies per project). It describes what makes a personality well-written and how to verify it.

## Table of Contents

1. [Purpose of This Document](#1-purpose-of-this-document)
2. [What a Personality File Is](#2-what-a-personality-file-is)
3. [Hard Rules](#3-hard-rules)
4. [Structure and Ordering](#4-structure-and-ordering)
5. [Instruction Craft for Personalities](#5-instruction-craft-for-personalities)
6. [Balancing Control and Autonomy](#6-balancing-control-and-autonomy)
7. [Autonomy Calibration](#7-autonomy-calibration)
8. [Section Writing Patterns](#8-section-writing-patterns)
9. [Failure Pattern Catalogue](#9-failure-pattern-catalogue)
10. [Startup Routines](#10-startup-routines)
11. [Skill Ecosystem Coordination](#11-skill-ecosystem-coordination)
12. [Source Hierarchies and Operating Loops](#12-source-hierarchies-and-operating-loops)
13. [Communication Style](#13-communication-style)
14. [Instruction Persistence](#14-instruction-persistence)
15. [Multi-Personality Coordination](#15-multi-personality-coordination)
16. [Content Quality and Consistency](#16-content-quality-and-consistency)
17. [Scoring Rubric](#17-scoring-rubric)
18. [Testing and Validation](#18-testing-and-validation)
19. [Post-Writing Verification](#19-post-writing-verification)
20. [Context Budget and Length](#20-context-budget-and-length)
21. [Sources](#21-sources)

---

## 1. Purpose of This Document

This document is the quality evaluation bible for agent personality files. It serves three audiences:

- **Writers** creating a new personality from scratch — use the section writing patterns, failure catalogue, and scoring rubric to produce strong output on the first pass.
- **Reviewers** evaluating an existing personality — use the scoring rubric, hard rules, and post-writing verification to identify specific weaknesses.
- **Improvers** iterating on a personality that mostly works — use the failure pattern catalogue and testing methodology to find the gaps between current and ideal behaviour.

Every claim about what works and what fails is grounded in either published research or observed practice. The [Sources](#21-sources) section at the end catalogues all references.

---

## 2. What a Personality File Is

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

## 3. Hard Rules

These are inviolable constraints with structural justification. They are not preferences or guidelines — violating any of them produces measurably worse results.

### Rule 1: Every token is loaded every session

The personality file is loaded at the start of every conversation. Unlike skills (loaded on demand) or reference files (loaded when needed), the personality consumes context budget permanently. This is a context engineering constraint, not a stylistic preference.

**Implication:** Every line in the personality must pass the test: "Does this need to shape behaviour in every session, or only when a specific task triggers?" If only when a specific task triggers, it belongs in a skill.

### Rule 2: Identity and role MUST be first

The primacy effect is one of the most robust findings in LLM instruction-following research. The agent attends most strongly to the first instructions it encounters. Identity and role definition activate the right reasoning mode — they frame every instruction that follows.

**Implication:** The first section of any personality file is always identity, role, and the autonomy grant. No preamble, no table of contents above it, no administrative metadata.

### Rule 3: The personality never contains detailed "how to" that belongs in skills

This is the personality-skill boundary. The personality says *when* and *what* — when to invoke a skill, what role it plays, what triggers justify it. Skills say *how* — the detailed process, templates, standards, and quality checks. Violating this boundary wastes context budget every session on content that is only relevant when a specific skill triggers, and creates drift risk when the skill is updated but the personality copy is not.

**The test:** For each instruction in the personality, ask: "Is this about when to do something (personality's job) or how to do it (skill's job)?" If it is about "how," it belongs in the skill.

### Rule 4: Only the personality references skill names

Skills are self-contained specialists. They do not know about other skills. They reference artefact patterns ("plan files in context/plans/"), not skill names. Only the personality references skill names, because only the personality is the coordinator. This prevents circular dependencies and ensures skills remain portable.

### Rule 5: Quality standards and communication style near the end

The recency effect means the agent attends strongly to the last instructions it reads before responding. Quality standards and communication style placed at the end of the personality act as recency anchors — they shape every response because they are the freshest instructions in attention.

**Implication:** Do not bury communication style in the middle. Do not place quality checklists early. These belong at the end, exploiting recency.

---

## 4. Structure and Ordering

### The Primacy-Recency Effect

LLMs attend most strongly to information at the beginning and end of their context, with the middle receiving diminished attention. This directly determines how personality files should be structured:

- **Beginning:** Identity, role, autonomy grant, and the most critical behavioural rules (primacy effect).
- **Middle:** Operational details — startup routines, source hierarchies, upkeep instructions, skill ecosystem.
- **End:** Quality standards, operating loop, review procedures, and communication style (recency effect).

### Recommended Section Order

1. **Role and identity** — Who the agent is and what its job is. This activates the right reasoning mode.
2. **Universal output standards** — How the agent should approach all output (depth, formatting, explanation style).
3. **Startup behaviour** — What to read and do at the beginning of every session.
4. **Source hierarchy** — What sources to trust and in what order.
5. **Version control guidance** — Commit stance and the few hard constraints.
6. **Subagent and parallelisation guidance** — Default parallelism stance.
7. **Incremental upkeep** — Responsibility to maintain documentation and context.
8. **Proactive improvement** — When to act without being asked.
9. **Note capture** — What to write down and when.
10. **Skill ecosystem** — What specialist skills exist and when to invoke them.
11. **Engineering standards** — Code quality principles.
12. **Operating loop** — The per-task workflow rhythm.
13. **Decision support** — How to present options and recommendations.
14. **Communication style** — Formatting, tone, verbosity norms.

### Why This Order Works

- The role definition (section 1) is the highest-leverage instruction. It frames everything that follows.
- Output standards (section 2) are referenced constantly, so they benefit from early positioning.
- Startup (section 3) is only used once per session, but it sets the tone, so it belongs early.
- The middle sections (5–10) are operational details that structure the agent's work.
- Communication style (section 14) is the recency anchor — the last thing the agent reads before responding.
- The operating loop (section 12) reinforces values through repetition, compensating for middle-section attention decay.

### Structural Markers

Use clear markdown hierarchy. Each major section should have a level-2 heading (`##`). Subsections use level-3 (`###`). This gives the agent a scannable table of contents and makes it easy to reference specific sections.

Tables are particularly effective for structured comparisons (source hierarchies, skill ecosystems, mode differences). The agent parses them reliably and they compress information that would take many more tokens in prose.

---

## 5. Instruction Craft for Personalities

### What Makes Instructions the Agent Actually Follows

**Clarity and directness matter more than emphasis.** Claude 4.6 is more responsive to system prompts than previous models. Aggressive language ("CRITICAL: You MUST...") can cause overtriggering. Normal prompting ("Use this tool when...") is more reliable. Reserve emphasis for the genuinely inviolable constraints — if everything is emphasised, nothing is (see [Emphasis Overuse](#emphasis-overuse) in the failure catalogue).

**Positive framing over negative constraints.** Instead of "Do not use shallow bullet lists," write "Use the representation that makes the information clearest." The agent generalises from positive examples better than negative prohibitions. Research on the "Pink Elephant Problem" has an architectural explanation: in attention-based models, the embedding for "not A" has a cosine similarity of 0.792 with "A" — the model literally represents "don't do X" almost identically to "do X" in embedding space (CVPR 2024 Workshop).

**Context and motivation behind instructions.** Explaining *why* enables generalisation. Instead of "Never use ellipses," write "Your response will be read aloud by a text-to-speech engine, so never use ellipses since the engine cannot pronounce them." The agent now avoids all unpronounceables, not just ellipses.

**Examples over rules.** "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." Include 3–5 examples for best results. One well-chosen example teaches more than a paragraph of abstract rules.

**Instruction count matters.** Research suggests frontier LLMs can follow approximately 150–200 instructions with reasonable consistency. Claude Code's own system prompt already contains ~50 instructions, leaving ~100–150 for the personality file and loaded skills combined. As count increases, following quality decreases uniformly. Every instruction must earn its place.

### The Compounding Effect

Everything from the skill writing research about instruction framing applies to personalities, with one critical addition: personality instructions are read at the start of *every* session, so framing issues compound. A single poorly framed instruction in a skill is encountered only when that skill triggers. A poorly framed instruction in the personality is encountered hundreds of times.

The paper "What Prompts Don't Say" (2025) found that specifying all requirements simultaneously **backfires** — with 19 requirements, accuracy drops to 85% from a 98.7% baseline. The Sonar Foundation Agent case study showed a clear progression: a prescriptive two-stage workflow achieved 58% efficacy, a freer workflow reached 70%, and distilling to a concise, principle-based prompt with extended thinking reached 75%. These findings compound in personalities because the personality is always loaded.

### The Golden Rule

> "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too."

### Personality-Specific Framing Checks

- **Startup instructions should enable, not prohibit.** "Read context/ and README.md first for fast orientation; pull additional files when the task requires them" is better than "Do not read learning/ at startup. Do not explore code at startup."
- **Mode instructions should be flexible.** "Ask the user whether they want teaching or implementation; if their message already makes it clear, confirm and proceed" is better than "Ask exactly this question and stop."
- **Upkeep instructions should describe the responsibility, not the procedure.** "Keep context/ and learning/ current throughout the session by making proportionate updates when the project changes" is better than a detailed list of every allowed action.

---

## 6. Balancing Control and Autonomy

### The Research

Anthropic's analysis of millions of agent interactions found:

- 80% of tool calls come from agents with at least one safeguard in place, and only 0.8% of actions appear to be truly irreversible.
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

### The Constraint-Permission Asymmetry

A strong personality names the few things the agent must NOT do and grants broad freedom for everything else. A weak personality lists the many things the agent IS ALLOWED to do, implicitly restricting everything not listed.

| Approach | Example | Effect |
|----------|---------|--------|
| **Weak** (listing permissions) | "You may commit, create files, edit files, run commands, spawn subagents..." | The agent hesitates on any action not listed |
| **Strong** (listing constraints) | "You may not push without explicit permission. Everything else is your judgment call." | The agent acts confidently on all unlisted actions |

The strong version is shorter, more robust to novel situations, and produces a more empowered agent.

---

## 7. Autonomy Calibration

### The Goal

The autonomy grant is one of the highest-leverage sections of a personality file. Its purpose is to make the agent feel like a senior engineer with an operating charter, not an intern with a permission slip. The agent sees opportunities in real time that the user cannot orchestrate — refactoring opportunities, inconsistencies, documentation drift, parallelisation possibilities. Effective autonomy calibration unlocks this capability.

### How to Write It

**Place it near the top.** The autonomy grant should be in or immediately after the identity and role section. The primacy effect means early positioning produces stronger adherence.

**Name the few hard constraints explicitly.** These are the guardrails — the narrow bridges where getting it wrong is irreversible or high-cost. Typical hard constraints:

- Do not push to a remote without explicit permission.
- Do not delete branches without explicit permission.
- Ask before invoking a skill (skills consume significant context).

**Grant broad autonomy for everything else.** After naming the constraints, explicitly state that everything outside them is the agent's judgment call:

| Weak | Strong |
|------|--------|
| "You may commit changes after completing work. You may create new files when needed. You may run tests. You may spawn subagents for parallel work." | "You have full autonomy in how you work. The hard constraints are few and explicit — everything else is your judgment call." |

The weak version lists permissions, implicitly restricting everything not mentioned. The strong version names constraints, explicitly granting everything not restricted.

**Explain WHY autonomy matters.** The agent calibrates its behaviour based on understanding. "The user cannot orchestrate every detail of a complex multi-file change. You see the code, the context, and the opportunities in real time — act on them" gives the agent a reason to exercise judgment rather than waiting for instructions.

**Persona implications shape behaviour beyond literal instructions.** Anthropic's research on persona selection (2026) found that the character traits implied by instructions shape behaviour beyond the literal meaning of those instructions — training an agent to cheat on coding tasks inadvertently taught it other subversive behaviours, because the persona of "someone who cheats" carries broader traits. The same principle works in reverse: an autonomy grant does not just permit specific actions — it activates a *persona* of a confident, judgment-exercising engineer, which shapes behaviour in situations the grant never explicitly mentioned.

### The Intern-vs-Engineer Test

Read the personality from the agent's perspective. Ask: "Does this read like an operating charter for a principal engineer, or a permission slip for an intern?"

Intern-style signals:
- Lists of specific actions the agent is allowed to take
- "Confirm before doing X" for low-risk, reversible actions
- Detailed step-by-step procedures for routine operations
- "Always ask" as a default stance

Engineer-style signals:
- A few named hard constraints, broad freedom otherwise
- "Use your judgment" as the default stance
- Principles with reasoning, not procedures
- Trust expressed explicitly

---

## 8. Section Writing Patterns

This section covers how to write each type of personality section effectively. For each section type: what it needs to achieve, common mistakes, evaluation criteria, and side-by-side comparisons.

### 8.1 Identity and Role

**What it needs to achieve:** Activate the right reasoning mode immediately. The identity section frames every instruction that follows — the agent reasons differently as a "principal-engineering collaborator" than as an "AI assistant that helps with code."

**Common mistakes:**
- Generic identity ("You are a helpful AI assistant") that does not activate any specific reasoning mode.
- Missing autonomy grant — the agent defaults to cautious, permission-seeking behaviour.
- Listing permissions instead of constraints.

**Evaluation criteria:**
- Does the identity activate a specific, appropriate reasoning mode?
- Is the autonomy grant explicit and near the top?
- Are hard constraints named as guardrails (few, absolute) rather than freedoms named as permissions (many, implicit)?
- Does the section explain WHY autonomy matters?

**Comparison:**

| Weak | Strong |
|------|--------|
| "You are an AI assistant that helps with code. Always ask before making changes. Follow the user's instructions carefully." | "You are a principal-engineering collaborator. You have full autonomy in how you work — creativity, agency, and initiative are expected. The hard constraints are few and explicit: do not push without permission, ask before invoking a skill. Everything else is your judgment call, because the user cannot orchestrate every detail of complex work." |

The weak version activates a generic, cautious reasoning mode. The strong version activates a senior-engineer reasoning mode with explicit permission to act independently.

### 8.2 Version Control Guidance

**What it needs to achieve:** Establish the agent's default stance on version control (typically: commit early and often) and name the few hard constraints (typically: never push without permission).

**Common mistakes:**
- The scenario-list anti-pattern (see [Section 9.1](#91-the-scenario-list-anti-pattern)). Listing specific situations that should trigger commits causes the agent to treat the list as exhaustive.
- Prescribing commit message formats in detail (belongs in a skill or linter, not the personality).
- Mixing version control stance with detailed Git procedures.

**Evaluation criteria:**
- Does it state the principle and default stance?
- Does it describe only what PREVENTS the behaviour (the rare exception), not what ENABLES it (the default case)?
- Is it free of scenario lists?

**Comparison:**

| Weak | Strong |
|------|--------|
| "After completing a task, fixing a bug, or finishing a meaningful chunk of work, commit your changes. Always write descriptive commit messages." | "Commit early and often. Any coherent unit of completed work is a natural commit point. The only hard constraint: never push to a remote without explicit permission." |

The weak version lists three specific triggers (completing a task, fixing a bug, finishing a chunk). Observed in practice: an agent following this instruction never committed during multi-phase plans because no individual phase matched "completing a task" or "fixing a bug" — the agent was mid-plan, not finishing one. The strong version states the principle and the single constraint, trusting the agent's judgment about when a unit of work is coherent.

### 8.3 Subagent and Parallelisation Guidance

**What it needs to achieve:** Make parallel execution the default, not something the agent considers when specific conditions are met. Describe what breaks parallelism (sequential dependency) rather than what enables it.

**Common mistakes:**
- The scenario-list anti-pattern again. Listing situations where parallelism "applies" causes the agent to serialise everything that does not match a listed scenario.
- Missing guidance on background agents (dispatch isolated work, then continue working yourself).
- Framing parallelism as an optimisation rather than the default.

**Evaluation criteria:**
- Is parallelism framed as the default, with sequential execution as the exception?
- Does it describe what BREAKS parallelism (sequential dependency), not what ENABLES it?
- Does it cover background agents (dispatch and continue)?
- Is it free of scenario lists?

**Comparison:**

| Weak | Strong |
|------|--------|
| "When work has independent threads — disjoint file sets, independent research questions, multi-subsystem analysis, exploration that can fan out — run in parallel." | "Default toward parallelisation. The only thing that prevents it is sequential dependency — when task B requires the output of task A. For isolated work, dispatch a background agent and continue working yourself." |

Observed in practice: an agent following the weak instruction wrote 14 independent files sequentially because "14 file writes" did not match any of the listed scenarios (disjoint file sets, independent research questions, multi-subsystem analysis, exploration). The strong version makes parallel the default and names only the exception.

### 8.4 Documentation Upkeep

**What it needs to achieve:** Establish that documentation maintenance is a continuous responsibility, not an event. The agent should make proportionate updates whenever work changes the project.

**Common mistakes:**
- Listing specific triggers for when to update ("when a new system is added, when behaviour changes, when an item completes, when a plan is done").
- Mixing upkeep responsibility (personality's job) with upkeep procedures (skill's job).
- Making upkeep feel like a separate task rather than part of normal work.

**Evaluation criteria:**
- Does it state the responsibility without listing specific triggers?
- Is it principle-based ("make proportionate updates as the work changes the project") rather than event-based ("update when X, Y, or Z happens")?
- Does it distinguish inline edits (personality's responsibility) from full skill passes (invoke the skill)?

**Comparison:**

| Weak | Strong |
|------|--------|
| "Update documentation when a new system is added, when behaviour changes, when an item completes, or when a plan is done." | "Make proportionate updates as the work changes the project. A small code change gets a small doc update. A large architectural shift gets a large doc update. For accumulated drift too broad for inline edits, recommend a skill pass." |

Observed in practice: an agent following the weak version skipped documentation updates during a substantial refactoring because the refactoring did not match any of the four listed triggers — it was not adding a new system, not completing an item, not finishing a plan, and the agent did not classify the refactoring as a "behaviour change." The strong version trusts the agent to judge proportionality.

### 8.5 Proactive Improvement

**What it needs to achieve:** Give the agent a clear discrimination principle for when to act without being asked. The agent sees opportunities the user cannot — dead code, inconsistencies, performance issues, documentation drift. Proactive improvement unlocks this, but without a discrimination principle the agent either does nothing (too cautious) or makes unwanted changes (too aggressive).

**Common mistakes:**
- No discrimination principle — just "fix things you notice" with no guidance on scope.
- Over-constraining with "always ask first" for every improvement, which defeats the purpose.
- Missing the diff-surprise test.

**Evaluation criteria:**
- Is there a clear discrimination principle?
- Does the principle distinguish between safe proactive actions and actions that need permission?
- Are specific examples anchored to the principle (illustrative, not exhaustive)?

**Pattern that works well:**

The discrimination principle "Would the user be surprised to see this in the diff?" is highly effective. It cleanly separates:
- **Not surprising (safe to do proactively):** Fixing a typo, removing dead code adjacent to the edit, correcting an obvious inconsistency.
- **Surprising (ask first):** Changing an algorithm, restructuring a module, modifying public APIs.

Lists of specific examples are acceptable here IF they are explicitly framed as illustrations of the principle, not as the complete list.

### 8.6 Note Capture

**What it needs to achieve:** Establish what the agent should write down during work and when. Notes serve a dual purpose: they preserve knowledge for future sessions and they push objectives into recent attention, combating instruction fade-out.

**Common mistakes:**
- No discrimination principle for what warrants a note vs what is transient.
- Listing specific triggers without explaining the underlying boundary.

**Evaluation criteria:**
- Does it lead with the discrimination principle?
- Is the boundary clear (resolved knowledge vs in-flight deliberation)?
- Are specific triggers framed as illustrations of the principle?

**Pattern that works well:**

The discrimination principle "Resolved knowledge belongs in notes; in-flight deliberation does not" cleanly separates what to capture. Resolved knowledge includes: user preferences discovered during work, design decisions with rationale, outcomes of experiments, patterns that worked or failed. In-flight deliberation includes: current thinking about how to approach a problem, tentative plans not yet confirmed.

Specific trigger examples are acceptable here because they demonstrate a boundary that is genuinely hard to infer from the principle alone.

### 8.7 Operating Loops

**What it needs to achieve:** Define the per-task workflow rhythm. The operating loop is one of the most powerful persistence mechanisms — every iteration naturally reinforces the personality's values without needing to re-read the personality file.

**Common mistakes:**
- Too long to memorise — the agent cannot internalise a 15-step loop.
- Prescribes specific actions instead of describing the rhythm.
- Missing the verification and upkeep steps that make the loop self-reinforcing.

**Evaluation criteria:**
- Is it short enough to memorise (typically 4–7 steps)?
- Does it describe a rhythm rather than prescribing specific actions?
- Does it reinforce the personality's values (ground in context, verify against intent, update documentation)?
- Is it general enough to apply to any task?

**Comparison:**

| Weak (too specific) | Strong (rhythm) |
|---------------------|-----------------|
| "1. Read the relevant context file. 2. Check the plan file. 3. Read the code. 4. Ask the user. 5. Write the code. 6. Run the tests. 7. Update the plan. 8. Update the context file. 9. Commit. 10. Summarise." | "1. Ground the next step in existing sources. 2. Clarify scope and trade-offs before acting. 3. Execute. 4. Verify against intent and interfaces. 5. Update context where the work created drift. 6. Assess whether accumulated drift warrants a skill pass." |

The weak version prescribes specific files and specific actions. The strong version describes a rhythm that applies to any task — the agent fills in the specifics based on the current situation.

### 8.8 Engineering Standards

**What it needs to achieve:** Establish the project's code quality principles. These should be principle-based, not rule-based, and each principle should carry equal weight.

**Common mistakes:**
- Rule-based standards ("always use const," "never use any") that duplicate what the linter enforces.
- Unequal weight — one principle gets a paragraph of explanation while others get a single line, causing the agent to prioritise the verbose one.
- Missing the failure mode that each principle prevents.

**Evaluation criteria:**
- Are standards principle-based (explain *why*) rather than rule-based (state *what*)?
- Do all principles carry roughly equal weight in terms of space and emphasis?
- Does each principle explain the failure mode it prevents?
- Are linter-enforceable rules excluded (they belong in the linter, not the personality)?

**Comparison:**

| Weak (rule-based) | Strong (principle-based) |
|--------------------|--------------------------|
| "Always use TypeScript strict mode. Never use `any`. Use `const` over `let`." | "Type safety prevents runtime surprises — prefer the narrowest type that accurately describes the value. Immutability prevents accidental mutation — prefer `const` and readonly patterns. Both are enforced by the linter; the principle matters for cases the linter does not catch." |

### 8.9 Skill Ecosystem

**What it needs to achieve:** Tell the agent what specialist skills exist, when to invoke each one, and how they relate to each other. The personality is the only coordinator — each skill is a self-contained specialist that does not know about other skills.

**Common mistakes:**
- Including HOW the skill works (belongs in the skill itself).
- Missing the relationship map showing how skills interact.
- Missing invocation etiquette (ask before running, name the skill, give a reason).
- Vague triggers ("when needed") instead of observable conditions.

**Evaluation criteria:**
- Does each skill entry describe WHAT it does and WHEN to invoke it?
- Is there a relationship map showing how data flows between skills?
- Is invocation etiquette established (ask before running, name the skill, give a reason)?
- Are triggers observable and concrete, not vague?
- Is HOW completely absent (delegated to the skill files)?

**Pattern that works well:**

A table for skill entries (name, what, when, when NOT), followed by an ASCII relationship map, followed by a prose section on invocation etiquette. The table compresses information; the map shows flows; the prose establishes norms.

### 8.10 Decision Support

**What it needs to achieve:** Define how the agent presents options and recommendations when a decision is needed. The number of options should match the problem, not a template.

**Common mistakes:**
- The 3-option anchoring anti-pattern (see [Section 9.2](#92-3-option-anchoring)). Showing exactly 3 options in examples causes the agent to always produce exactly 3.
- Presenting options without a recommendation.
- Missing the principle of variable cardinality.

**Evaluation criteria:**
- Does it emphasise that the number of options should match the problem?
- Do examples (if any) show different numbers of options across different scenarios?
- Does it require a recommendation with reasoning, not just a list of options?

**Comparison:**

| Weak | Strong |
|------|--------|
| "When presenting options, always provide 3 alternatives with pros and cons." | "Match the number of options to the decision. Some decisions are binary. Some have five viable approaches. Present however many genuinely exist, recommend one, and explain the trade-offs." |

---

## 9. Failure Pattern Catalogue

These are failure modes observed in practice or documented in research. Each entry describes the pattern, its root cause, its observable symptoms, and the fix.

### 9.1 The Scenario-List Anti-Pattern

**Severity: Critical.** This is the single most impactful failure pattern observed in personality design. It deserves thorough treatment because it is subtle, pervasive, and devastating to agent behaviour.

**The pattern:** Instructions include specific examples of when to apply a behaviour. The agent treats the list as exhaustive. If the current situation does not match one of the listed examples, the agent skips the behaviour entirely — even when the principle clearly applies.

**Root cause:** LLMs are pattern matchers. A list of scenarios creates a strong pattern: "this behaviour applies when [scenario A], [scenario B], or [scenario C]." The agent generalises from the list structure, not from the underlying principle. Novel situations that do not match any listed scenario fail to trigger the behaviour.

**Three real examples from practice:**

**Version control:**
- Instruction: "After completing a task, fixing a bug, or finishing a meaningful chunk of work, commit your changes."
- Failure: The agent never committed during a multi-phase plan. No individual phase matched "completing a task" (the task was the whole plan), "fixing a bug" (it was new development), or "finishing a meaningful chunk" (the agent interpreted each phase as incomplete).
- Fix: "Commit early and often. Any coherent unit of completed work is a natural commit point."

**Parallelisation:**
- Instruction: "When work has independent threads — disjoint file sets, independent research questions, multi-subsystem analysis, exploration that can fan out — run in parallel."
- Failure: The agent wrote 14 independent files sequentially. "14 independent file writes" did not match "disjoint file sets" (the agent interpreted this as separate subsystems), "independent research questions" (no research involved), "multi-subsystem analysis" (no analysis), or "exploration that can fan out" (no exploration).
- Fix: "Default toward parallelisation. The only thing that prevents it is sequential dependency."

**Documentation upkeep:**
- Instruction: "Update documentation when a new system is added, when behaviour changes, when an item completes, or when a plan is done."
- Failure: The agent skipped documentation updates during a substantial refactoring. The refactoring was not adding a new system, not completing an item, not finishing a plan, and the agent did not classify it as a "behaviour change."
- Fix: "Make proportionate updates as the work changes the project."

**The fix pattern:** State the principle and default stance. Describe what PREVENTS the behaviour (the rare exception), not what ENABLES it (the default case). Trust the agent's judgment about when to apply the behaviour.

**The deeper lesson:** This is a specific instance of a general principle from the research — "judgment guidelines that teach the agent how to think about decisions rather than making every decision for it." Specific scenario lists are the personality equivalent of over-constraining. They attempt to enumerate the space of situations where a behaviour applies, but the space is too large and varied to enumerate. The principle plus the exception covers all cases; the scenario list covers only the listed cases.

**How to detect it:** Read each instruction in the personality and ask: "Does this describe specific situations when a behaviour should happen?" If yes, it is likely a scenario list. Rewrite it as a principle with a default stance and an exception.

### 9.2 3-Option Anchoring

**The pattern:** Decision support examples in the personality show exactly 3 options. The agent produces exactly 3 options for every decision, regardless of the actual decision space.

**Root cause:** Examples are the strongest steering signal for LLM output. An example showing 3 options teaches the agent that 3 is the correct number.

**Observable symptom:** The agent presents 3 options for binary decisions (padding with a weak third option) and 3 options for decisions with 5+ viable approaches (omitting valid alternatives).

**The fix:** Either show examples with different numbers of options (2, 4, 5), or state the principle explicitly: "Match the number of options to the decision. Some decisions are binary. Some have five viable approaches."

### 9.3 Mode-Question Friction

**The pattern:** The personality instructs the agent to ask the user to choose a mode (implementation vs teaching, aggressive vs conservative, etc.) at the start of every session.

**Root cause:** The personality designer wants different behaviour in different contexts but implements the routing as a runtime question.

**Observable symptom:** The user is asked a meta-question before their actual work can begin. This adds friction to every session and trains the user to expect overhead.

**The fix:** Split into separate personality files (one per mode), or infer from context (implementation mode when the user gives a task, teaching mode when the user asks a question). The split should eliminate a startup decision, not create one — the user chooses which personality file to use before the conversation starts, which is lower friction than answering a question inside every conversation.

### 9.4 Confirm-Everything Paralysis

**The pattern:** Too many "confirm before doing X" instructions cause the agent to ask permission for everything, including trivial, reversible actions.

**Root cause:** Each individual "confirm before" instruction seems reasonable in isolation. Collectively, they train the agent that its default stance should be to ask permission.

**Observable symptom:** The agent asks "Should I proceed?" after every step, even for trivial file edits or obvious next steps. Sessions feel slow and frustrating.

**The fix:** Name the few hard constraints that genuinely require confirmation (push to remote, invoke a skill, delete data). Grant broad autonomy for everything else. The default should be "act," not "ask."

### 9.5 Reference Under-Loading

**The pattern:** The personality lists 10+ reference files that the agent should read but does not distinguish mandatory from conditional. The agent reads only a few (typically the first 2–3 listed) and misses critical context.

**Root cause:** A flat list of references provides no priority signal. The agent optimises for speed and reads the minimum.

**Observable symptom:** The agent misses conventions or standards documented in reference files it did not load.

**The fix:** Mark mandatory-core references (always read at startup) separately from task-based conditional references (read when the task requires them). Keep the mandatory set small (2–4 files).

### 9.6 Personality-as-Skill-Manual

**The pattern:** The personality contains detailed "how to" instructions for specific tasks — how to write context files, how to run a code audit, how to generate reports.

**Root cause:** The personality designer wants consistent quality and puts the instructions where they will always be seen.

**Observable symptom:** The personality file is excessively long. Context budget is wasted every session on content that is only relevant when a specific task triggers. When the skill is updated, the personality's copy drifts.

**The fix:** Move all "how to" content to skills. The personality retains only "when" and "what" — when to invoke the skill and what role it plays.

### 9.7 Instruction Fade-Out

**The pattern:** Instructions in the middle of the personality get progressively less attention over long conversations. The agent starts the session following all instructions but gradually drifts from middle-section content.

**Root cause:** The primacy-recency effect. Early instructions (primacy) and late instructions (recency) receive more attention than middle instructions. Over long conversations, this effect intensifies as the personality file recedes further into the context window.

**Observable symptom:** The agent follows identity/role and communication style consistently but drifts on operational details (upkeep, version control, parallelisation) during long sessions.

**The fix:** Multiple reinforcement mechanisms:
- **Operating loops** that naturally reinforce values through repetition.
- **Quality checklists** at the end of the personality as recency anchors.
- **Note-taking** that pushes objectives into recent attention.
- **Structural placement** — the most critical middle-section instructions should be reinforced by the operating loop.

### 9.8 Emphasis Overuse

**The pattern:** ALWAYS, NEVER, MUST, CRITICAL appear throughout the personality in capitalised form. Everything is emphatic.

**Root cause:** The personality designer wants strong compliance on every instruction.

**Observable symptom:** The agent cannot distinguish genuinely inviolable constraints from strong preferences. Compliance on the genuinely critical instructions (e.g., "never push without permission") is diluted because the emphasis signal has been devalued.

**The fix:** Reserve emphasis (capitalisation, bold, "MUST") for the genuinely inviolable constraints — typically 3–5 items in an entire personality. Use normal prose for everything else. The contrast between emphatic and normal is what gives emphasis its power.

---

## 10. Startup Routines

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
- Loading reference or learning material at startup — educational material is reference, not startup context.

---

## 11. Skill Ecosystem Coordination

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

## 12. Source Hierarchies and Operating Loops

### Writing a Source Hierarchy

Most projects have multiple sources of truth that can conflict: a README, context files, the code itself, learning material. The personality should establish a clear priority order so the agent knows what to trust when sources disagree.

A well-written source hierarchy:

1. **Names each source** and its semantic role. "README.md: project intent, scope, direction" tells the agent what kind of truth to extract from the README.
2. **Establishes priority** for different kinds of questions. Code determines implementation reality. The README determines intended direction. Context files are the maintained memory layer. Priority depends on what question the agent is answering.
3. **Describes conflict resolution.** "If context/ says feature X exists but the code has no trace of it, the code wins — context/ has drifted and needs updating." This prevents the agent from trusting stale documentation over observed reality.

### Writing an Operating Loop

The operating loop is the per-task workflow the agent follows. It reinforces the personality's values through repetition — every cycle through the loop naturally reminds the agent to ground in context, clarify scope, verify work, and update documentation.

Effective operating loops:

1. **Ground the next step** in existing sources (context, README, conversation).
2. **Clarify scope and trade-offs** before acting.
3. **Execute** (in implementation mode) or **explain** (in teaching mode).
4. **Verify** against intent, interfaces, and documentation.
5. **Update** context and learning material where the work created drift.
6. **Assess** whether accumulated drift warrants a full skill pass.

The loop should be short enough to memorise and general enough to apply to any task. It should not prescribe specific actions — it describes the *rhythm* of the agent's work.

### Why the Loop Matters for Persistence

Research on instruction fade-out shows that LLM instruction adherence decays over long conversations. The operational loop combats this because the agent executes it every cycle, naturally reinforcing the personality's priorities (ground in context, update documentation, assess drift) without needing to re-read the personality file.

The loop is one of the few mechanisms that provides *structural* persistence — it is built into the workflow rather than relying on the agent's memory. This makes it far more reliable than hoping the agent will remember a middle-section instruction 50 turns into a conversation.

### Loop Design Checklist

- [ ] 4–7 steps (short enough to internalise)
- [ ] Describes rhythm, not specific actions
- [ ] Includes a grounding step (consult existing sources)
- [ ] Includes a verification step (check against intent)
- [ ] Includes an upkeep step (update documentation)
- [ ] Includes an assessment step (is drift accumulating?)
- [ ] Applies to any task in the project, not just coding tasks

---

## 13. Communication Style

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

## 14. Instruction Persistence

### The Problem

Instructions fade over long conversations. The primacy-recency effect means middle-of-conversation instructions receive less attention as the conversation grows. This is well-documented: "Lost in the Middle" (Liu et al., 2023) found that multi-document QA performance drops by more than 20% when relevant information is positioned in the middle rather than at the beginning or end — in the worst case, performance was *lower than having no documents at all*. Serial position research (Guo et al., 2024) found that primacy effects appeared in 73 out of 104 tested instances (70%), with the first third of labels accounting for more than 40% of predictions. Encouragingly, chain-of-thought reasoning effectively mitigated these effects across most models — which means skills that encourage step-by-step reasoning may naturally reduce lost-in-the-middle problems.

The personality file, placed at the very beginning of the context, benefits from primacy — but as the conversation grows, even primacy attenuates. An instruction that shapes behaviour perfectly at turn 3 may have no effect at turn 50.

### The Two Types of Persistence

**Content persistence** relies on the agent remembering specific instructions. It is the weakest form — the agent must recall text from potentially thousands of tokens ago, competing with all the intermediate conversation for attention. Content persistence degrades predictably as conversations lengthen.

**Structural persistence** is built into the workflow. The agent does not need to remember the instruction because the workflow naturally produces the behaviour. Structural persistence is far more reliable because it does not depend on memory.

| Mechanism | Type | How It Works | Reliability |
|-----------|------|-------------|-------------|
| Personality section placement | Content | Primacy-recency effect keeps early and late instructions in attention | Moderate — degrades as conversation grows |
| Operating loop | Structural | Every task cycle reinforces grounding, verification, and upkeep | High — each iteration is fresh |
| Quality checklists at end | Content (recency) | Last thing the agent reads before responding | Moderate — effective for output quality |
| Note-taking / plan files | Structural | Agent writes objectives into recent context, keeping them in attention | High — objectives are literally in the recent conversation |
| Self-reinforcing workflows | Structural | Steps that naturally produce desired behaviour (e.g., verify step forces re-reading intent) | High — behaviour emerges from structure |

### Concrete Positioning Guidance

Based on the primacy-recency effect:

- **Lines 1–20 of the personality:** Highest persistence. Identity, role, autonomy grant, and the most critical universal standards belong here.
- **Lines 20–60:** Strong persistence. Startup routines, source hierarchy, and version control stance.
- **Lines 60–120:** Moderate persistence. Operational details — upkeep, parallelisation, note capture. These benefit most from structural reinforcement via the operating loop.
- **Final 20 lines:** Strong persistence (recency). Communication style, quality checklist, and formatting norms.

Instructions in the moderate-persistence zone (lines 60–120) should be reinforced by at least one structural mechanism. If the operating loop includes an "update context" step, the upkeep instruction does not need to rely solely on being remembered — the loop naturally triggers the behaviour.

### How Long Conversations Cause Instruction Drift

Over a long conversation (50+ turns), several mechanisms cause drift:

1. **Context window pressure.** The personality file represents a shrinking fraction of total context. At turn 5, the personality might be 10% of context; at turn 50, it might be 1%.
2. **Recency bias.** The most recent turns dominate attention. If recent turns involved a specific coding pattern, the agent gravitates toward continuing that pattern even if the personality says otherwise.
3. **Implicit instruction override.** If the user approves output that violates a personality instruction (e.g., accepts a shallow commit message), the agent infers that the instruction is not important and stops following it.
4. **Accumulated conversational norms.** The conversation develops its own norms through repetition. If the first three tool calls used a particular pattern, that pattern becomes the conversational norm regardless of personality instructions.

### Structural Defences Against Drift

1. **Operating loops** — every iteration is a fresh reinforcement cycle. The agent does not need to remember "update documentation" from the personality if the loop step is "update context where the work created drift."

2. **Note-taking and plan files** — when the agent writes its objectives into a plan file or notes, those objectives appear in recent context. They are literally the most recent thing the agent read. This converts a content-persistence problem (remembering the personality) into a recency advantage (the plan file is recent). Manus (2025) calls this "recitation" — constantly updating todo.md files step-by-step so that objectives are recited into the end of context, keeping goals in the agent's recent attention span without requiring architectural changes.

3. **Quality checklists as recency anchors** — placing the quality checklist at the end of the personality exploits recency. Placing verification steps at the end of skill invocations exploits recency again. The agent's last read before producing output contains the quality standards.

4. **Self-reinforcing step dependencies** — design workflow steps that require consulting context before proceeding. "Verify against the architecture file" forces the agent to re-read the architecture, which naturally grounds it in the project's actual state.

---

## 15. Multi-Personality Coordination

### When to Split

A single personality file is almost always sufficient. Split only when the personality needs to operate in fundamentally different modes with incompatible defaults:

- **Implementation vs teaching.** An implementation personality commits, runs commands, and modifies files. A teaching personality explains, plans, and reviews without executing.
- **Different role boundaries.** A full-autonomy personality for experienced users vs a confirm-more personality for collaborative sessions.
- **Different output scopes.** A personality that proactively improves everything it touches vs one that stays strictly within the requested scope.

The critical test: "Do these modes conflict within a single file?" If you can write "In implementation mode, do X; in teaching mode, do Y" without the instructions conflicting, you do not need a split. If the modes have incompatible defaults (commit freely vs never commit), a split is cleaner.

### What Should Stay Aligned

When maintaining multiple personality variants, these elements must be identical or structurally parallel across all variants:

- **Output standards.** What "good" looks like should not depend on which personality is loaded.
- **Formatting philosophy.** Tables, diagrams, markdown depth — consistent across variants.
- **Engineering principles.** Code quality expectations should not vary by mode.
- **Terminology.** The same term for the same concept in every variant.
- **Source hierarchy.** What to trust and in what order.
- **Skill ecosystem.** What skills exist and what they do — the skills themselves do not change per mode.

### What Should Differ

- **Role boundaries.** What the agent does (execute vs explain) and how autonomous it is.
- **Operating loop steps.** The implementation loop includes "execute" and "commit." The teaching loop includes "explain" and "illustrate."
- **Proactive improvement scope.** An implementation personality may fix adjacent issues. A teaching personality may only flag them.
- **Version control stance.** An implementation personality commits. A teaching personality may not touch version control at all.

### Drift Risk

The primary risk with multiple personality variants is drift — one file is updated and the other is not. Over time, the shared sections diverge: one uses new terminology, updated skill descriptions, or revised engineering principles while the other retains stale content.

**Structural mitigations:**
- Keep shared content structurally parallel. If section 5 is "Engineering Standards" in both files, changes to engineering standards should be applied to both files in the same session.
- Review both files together when either changes. The cost is low (read the other file) and the risk of drift is high.
- Consider extracting shared content into a separate file that both personalities reference. This works if the agent system supports subdirectory CLAUDE.md files or similar inclusion mechanisms.

### The Startup Decision Problem

The split should eliminate a startup decision, not create one. If the personality previously asked "Do you want implementation mode or teaching mode?" at the start of every session, the split moves that decision to file selection — the user chooses which personality file to load before the conversation starts.

This is strictly better than a runtime mode question because:
- File selection happens once (when starting the agent), not every session.
- The agent's behaviour is consistent from the first turn — no mode-switching confusion.
- The personality file can be fully optimised for its mode without conditional branching.

---

## 16. Content Quality and Consistency

### The Personality-Skill Boundary

The most common content quality issue in personality files is scope creep — the personality accumulates detailed "how to" instructions that belong in skills. Research shows why this matters:

1. **Context bloat degrades everything.** Chroma's research (2025) tested 18 frontier models and found that every single one gets worse as input length increases — performance on full-context prompts (~113k tokens) was significantly lower than on focused prompts (~300 tokens) across all model families. Notably, well-structured irrelevant context is *more* harmful than random noise, because structural coherence makes distractors compete more effectively for attention. The personality is loaded every session. Every token of detailed skill-level instruction in the personality degrades the agent's performance on every task, even when those instructions are irrelevant.

2. **Instruction conflicts cause broad degradation.** The paper "LLMs can be easily Confused by Instructional Distractions" (2025) found that competing instruction signals can cause accuracy on the intended task to fall as low as 30% in some configurations. When the personality says "do X this way" and the skill says "do X that way," compliance degrades across *all* instructions, not just the conflicting pair.

3. **Instruction saturation is real.** The IFScale benchmark (2025) found that even the strongest reasoning model (o3) achieved only 62.8% accuracy at 500 instructions. Models show three degradation patterns: *threshold decay* (reasoning models maintain near-perfect compliance until ~150, then crash), *linear decay* (frontier models degrade steadily), and *exponential decay* (smaller models collapse to 7–15% floors). Claude Code's own system prompt already contains ~50 instructions. The personality and loaded skills share the remaining budget. Every instruction in the personality that could be in a skill is wasting a slot in this limited budget.

**The principle:** The personality should say *when* and *what* — when to invoke a skill, what role it plays, what triggers justify it. The skills should say *how* — the detailed process, templates, standards, and quality checks.

**The test:** For each instruction in the personality, ask: "Is this about when to do something (personality's job) or how to do it (skill's job)?" If it is about "how," it probably belongs in the skill.

### Consistency Across the Personality-Skill Ecosystem

The personality and all skills must present a consistent worldview:

- **Same terminology.** If the personality calls them "plan files," no skill should call them "implement-now files."
- **Same folder model.** If the personality describes a `notes/` folder, no skill should still reference `decisions/`.
- **Same philosophical stance.** If the personality says "depth is a virtue, not a problem," no skill should instruct the agent to "keep it brief."
- **Same formatting philosophy.** If the personality encourages rich markdown (tables, diagrams, trees), no skill should restrict the agent to bullets.

### The Consistency Verification Method

Read the personality, then read each skill it references. For each pair, check:

1. Do they use the same terms for the same concepts?
2. Do they agree on folder structure and file locations?
3. Do they agree on quality standards and depth expectations?
4. Does the personality's description of the skill match what the skill actually does?
5. Are there instructions in both that could conflict?

Any mismatch is a quality defect. The fix is always to align them — typically by updating the less-recently-revised document to match the more-recently-revised one.

---

## 17. Scoring Rubric

Use this rubric to evaluate personality files across nine dimensions. Each dimension has concrete, observable criteria for Weak, Adequate, and Strong.

### Autonomy Balance

| Level | Criteria |
|-------|----------|
| **Weak** | Lists specific permissions ("you may commit, create files, run tests"). Contains "confirm before" for more than 3 actions. No explicit autonomy grant. Or: no guardrails at all — the agent has zero hard constraints. |
| **Adequate** | Has an autonomy grant and some named constraints. Mixes permission-listing with constraint-listing. The agent would know roughly how much latitude it has. |
| **Strong** | Few explicit hard constraints (typically 2–4), broad autonomy grant, explicit explanation of WHY autonomy matters. Reads like an operating charter for a senior engineer. The agent feels empowered. |

### Instruction Persistence

| Level | Criteria |
|-------|----------|
| **Weak** | Critical instructions appear only once, in the middle of the file. No operating loop. No structural reinforcement. Identity section is more than 20 lines in. |
| **Adequate** | Identity is first. Communication style is last. Some reinforcement via operating loop. Plan/note capture exists but is not tied to persistence. |
| **Strong** | Identity and autonomy first (primacy). Quality standards and communication style last (recency). Operating loop reinforces all critical middle-section values. Note-taking pushes objectives into recent attention. Every instruction in the moderate-persistence zone (middle of file) is reinforced by at least one structural mechanism. |

### Section Ordering

| Level | Criteria |
|-------|----------|
| **Weak** | Sections in random or alphabetical order. Identity is not first. Communication style is not last. Critical instructions scattered throughout. |
| **Adequate** | Identity is first. Reasonable grouping of related sections. Communication style is near the end. |
| **Strong** | Fully primacy-recency optimised. Identity and autonomy first. Output standards early. Operational details in the middle with structural reinforcement. Quality anchors and communication style last. The ordering has clear reasoning for every section's position. |

### Constraint Calibration

| Level | Criteria |
|-------|----------|
| **Weak** | Rigid procedures, scenario lists (see [9.1](#91-the-scenario-list-anti-pattern)), numeric limits everywhere, ALWAYS/NEVER in caps on more than 5 instructions. |
| **Adequate** | Mix of principles and constraints. Some scenario lists remain but critical sections are principle-based. Emphasis is used selectively. |
| **Strong** | All instructions are principle-based with reasoning. Hard rules only where justified by irreversibility or structural necessity. No scenario-list anti-pattern. Emphasis reserved for genuinely inviolable constraints (3–5 items). Every constraint explains why it exists. |

### Skill Coordination

| Level | Criteria |
|-------|----------|
| **Weak** | Detailed how-to in personality. Skills described vaguely ("use when needed"). No relationship map. Skill descriptions do not match what skills actually do. |
| **Adequate** | Skills described with what and when. No how-to leaking. Skill descriptions mostly accurate. Missing relationship map or invocation etiquette. |
| **Strong** | Clear what/when/when-NOT for each skill. Relationship map showing data flow. Invocation etiquette established (ask before, name the skill, give a reason). No how-to leaking. All skill descriptions verified against actual skill content. |

### Coherence

| Level | Criteria |
|-------|----------|
| **Weak** | Contradictions between personality sections. Terminology drift (same concept called different things). Personality contradicts skill instructions. |
| **Adequate** | Mostly consistent within the personality. Minor terminology variations. Not verified against all skills. |
| **Strong** | Fully coherent within the personality and with all referenced skills. Consistent terminology throughout. No contradictions. Verified against actual skill content. |

### Formatting Quality

| Level | Criteria |
|-------|----------|
| **Weak** | Wall of text. No structural hierarchy. No tables, no visual aids. |
| **Adequate** | Headers and paragraphs. Some tables. Readable but not optimised. |
| **Strong** | Rich markdown hierarchy. Tables for structured comparisons (skill ecosystems, source hierarchies). Visual relationship maps. Clear heading structure. Information density appropriate to each section. |

### Budget Efficiency

| Level | Criteria |
|-------|----------|
| **Weak** | Contains skill-level procedures. Redundant with skill content. Explains things the agent already knows (software engineering basics). More than 30% of content could be offloaded to skills. |
| **Adequate** | Mostly personality-level content. Some how-to that could be in skills. Reasonable length. |
| **Strong** | Every token earns its place. All how-to offloaded to skills. No redundancy. The personality is as short as it can be while retaining all genuinely personality-level instructions. Passes the "would removing this cause mistakes?" test for every line. |

### Personality-Skill Boundary

| Level | Criteria |
|-------|----------|
| **Weak** | Personality contains step-by-step procedures for specific tasks. "How to write a context file" appears in the personality. Skill descriptions include implementation details. |
| **Adequate** | Mostly clean boundary. Occasional procedural detail that could be in a skill. Skill descriptions focus on what and when. |
| **Strong** | Clean boundary — the personality says when and what, skills say how. No procedural detail in the personality beyond the operating loop. Every instruction passes the when/what vs how test. |

---

## 18. Testing and Validation

### Mental Dry-Run

The most efficient pre-deployment test. Read the entire personality as if you are the agent. Start a hypothetical session and walk through the first few turns:

1. **Startup.** Do you know what to read? In what order? What to summarise? What to ask?
2. **First task.** A user says "Add a new API endpoint for user preferences." Do you know what to commit? When to parallelise? What to update afterward?
3. **Mid-session.** You are 30 turns in on a multi-phase plan. Do you know when to commit? Do you feel compelled to update documentation? Would you parallelise the next two independent steps?
4. **Edge case.** The user asks for something that partially overlaps with a skill. Do you know whether to handle it inline or invoke the skill? Do you know how to ask?

If any answer is unclear, the personality has a gap.

### Scenario Testing

Walk through specific scenarios designed to test known failure modes:

| Scenario | Tests | What to Watch For |
|----------|-------|-------------------|
| Multi-phase plan (5 phases, each producing files) | Version control, instruction persistence | Does the agent commit between phases? Or only at the end? |
| 14 independent files to create | Parallelisation | Does the agent create them in parallel? Or sequentially? |
| Broad refactoring across 8 files | Documentation upkeep | Does the agent update documentation afterward? Or skip because "refactoring" was not a listed trigger? |
| Binary decision (do X or do not do X) | Decision support, 3-option anchoring | Does the agent present 2 options? Or pad to 3? |
| User approves low-quality output | Instruction persistence, quality standards | Does the agent lower its standards in subsequent output? Or maintain personality-defined quality? |
| Trivial file edit | Autonomy, confirm-everything paralysis | Does the agent just do it? Or ask permission? |
| Accumulated drift over many small changes | Skill invocation threshold | Does the agent recommend a skill pass? Or keep making inline edits past the point of effectiveness? |

### First-Session Signals

When deploying a personality for the first time, watch for these signals:

**Positive signals:**
- Agent follows the startup routine without prompting
- Agent commits at natural boundaries without being asked
- Agent parallelises when work is independent
- Agent captures notes without being asked
- Agent distinguishes inline edits from skill-worthy passes
- Agent asks permission only for the named hard constraints

**Negative signals:**
- Agent asks "Should I proceed?" after trivial actions
- Agent serialises independent work
- Agent does not commit until the user asks
- Agent does not update documentation after making changes
- Agent presents exactly 3 options for every decision
- Agent includes how-to detail that belongs in skills

### Regression Testing

After changing a personality, check:

1. **Did existing behaviours break?** Read the diff and identify any instruction that was removed or reworded. Verify the behaviour it produced is still produced by the new version.
2. **Did instruction count increase beyond budget?** Count the approximate instructions. If the personality grew substantially, verify nothing was added that belongs in a skill.
3. **Was a scenario-list anti-pattern introduced?** Search for new lists of specific situations where a behaviour should apply. Rewrite as principle + exception.
4. **Did emphasis inflate?** Count ALWAYS/NEVER/MUST/CRITICAL in caps. If the count increased, verify the new emphatic instructions are genuinely inviolable.
5. **Did the shared sections drift from other variants?** If multiple personality variants exist, verify the changed file is still aligned with the others on shared content.

---

## 19. Post-Writing Verification

After writing or editing a personality file, verify these dimensions. This section provides a concrete checklist; the [Scoring Rubric](#17-scoring-rubric) provides the evaluation framework.

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

### Scenario-List Check

- Search for instructions that list specific situations when a behaviour should apply. For each one, ask: "Would the agent apply this behaviour in a novel situation not on the list?" If no, rewrite as principle + exception.

### Persistence Check

- Are the most critical instructions placed early (primacy effect) and late (recency effect)?
- Are there instructions in the moderate-persistence zone (middle of the file) without structural reinforcement? If so, add reinforcement via the operating loop or note-taking.

### Emphasis Check

- Count ALWAYS/NEVER/MUST/CRITICAL in capitalised form. Is the count below 5? If not, identify which emphatic instructions are genuinely inviolable and normalise the rest.

### Budget Check

- Is the personality as short as it can be while retaining all genuinely personality-level instructions?
- Could any section be offloaded to a skill that loads on demand instead of every session?
- Does every line pass the test: "Would removing this cause the agent to make mistakes?"

### Multi-Variant Check (if applicable)

- Are shared sections aligned across all personality variants?
- Has the change been applied to all variants where it applies?
- Do the variants still differ only in the dimensions that justified the split?

---

## 20. Context Budget and Length

### The Research

- Claude Code's system prompt contains ~50 instructions. Adding a personality file adds to this total.
- Research suggests ~150–200 instructions is the reliable following limit for frontier models.
- Personality files beyond ~60–80 lines risk instruction dilution, where later instructions receive less attention.
- Prompt bloat research shows reasoning performance degrades at around 3,000 tokens of instruction.
- Chroma's context rot research (2025) found that every frontier model tested showed significant accuracy degradation on full-context prompts (~113k tokens) compared to focused prompts — length itself is harmful, not just irrelevance. Well-structured irrelevant context is more harmful than random noise.

### The Practical Approach

The personality file should be:

- **Short in the personality file itself** — only what applies broadly to every session.
- **Expansive in the files it points to** — skills, references, and context files carry the detailed instructions.
- **High signal density** — every line should pass the test: "Would removing this cause the agent to make mistakes?"

This does not mean the personality should be stripped to a skeleton. It means the personality should contain the *right* information at the *right* density. A 200-line personality file where every line shapes behaviour is better than a 50-line file that omits important guidance.

The key is offloading. Detailed instructions about *how to maintain context files* belong in the upkeep skill, not the personality. Detailed instructions about *how to write research papers* belong in the research skill. The personality says *when* to invoke these skills and *what role they play* — the skills themselves carry the detailed instructions.

### Budget Allocation Guidance

A rough budget model for a project with 5–8 skills:

| Component | Approximate Instruction Count |
|-----------|-------------------------------|
| Claude Code system prompt | ~50 (fixed) |
| Personality file | 40–80 |
| Loaded skill (when active) | 30–60 |
| **Total when skill is active** | **120–190** |

This leaves headroom within the ~150–200 reliable following limit. Exceeding the budget does not cause a hard failure — it causes gradual, uniform degradation in compliance quality. The most recently added instructions tend to degrade first.

---

## 21. Sources

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
- [Introducing Sonar Foundation Agent — Sonar, 2025](https://www.sonarsource.com/blog/introducing-sonar-foundation-agent/)
- [Do not think about pink elephant! — CVPR 2024 Workshop](https://arxiv.org/abs/2404.15154)
- [Negation: A Pink Elephant in the LLMs' Room?, 2025](https://arxiv.org/abs/2503.22395)
- [Lost in the Middle — Liu et al., 2023](https://arxiv.org/abs/2307.03172)
- [Serial Position Effects of LLMs — Guo et al., ACL Findings 2024](https://arxiv.org/abs/2406.15981)
- [Anthropic — Persona Selection Model, 2026](https://www.anthropic.com/research/persona-selection-model)
- [Anthropic — Measuring AI Agent Autonomy, 2026](https://www.anthropic.com/research/measuring-agent-autonomy)
- [Manus — Context Engineering for AI Agents, 2025](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Let Me Speak Freely? Format Restrictions and LLM Performance, 2024](https://arxiv.org/abs/2408.02442)
- [Surface Form Competition — Holtzman et al., EMNLP 2021](https://arxiv.org/abs/2104.08315)

### Observed in Practice
- Scenario-list anti-pattern — version control, parallelisation, and documentation upkeep failures observed across multiple production personality files during iterative refinement sessions.
- 3-option anchoring — observed when decision support examples showed exactly 3 options; the agent consistently produced 3 regardless of the actual decision space.
- Mode-question friction — observed when the personality required a mode selection at startup; replacing with separate personality files eliminated the overhead.
- Confirm-everything paralysis — observed when more than 5 "confirm before" instructions accumulated; the agent defaulted to asking permission for all actions.
- Emphasis overuse — observed when ALWAYS/NEVER/MUST appeared on 10+ instructions; compliance on genuinely critical constraints degraded.
- Instruction fade-out — observed in conversations exceeding 40 turns; middle-section instructions (upkeep, parallelisation) were the first to lose effect.
