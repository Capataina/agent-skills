# Section Writing Patterns

This file covers how to write each type of personality section effectively. For each section type: what it needs to achieve, common mistakes, evaluation criteria, and side-by-side comparisons.

## Table of contents

- 7.1 Identity and Role
- 7.2 Version Control Guidance
- 7.3 Subagent and Parallelisation Guidance
- 7.4 Documentation Upkeep
- 7.5 Proactive Improvement
- 7.6 Note Capture
- 7.7 Operating Loops
- 7.8 Engineering Standards
- 7.9 Skill Ecosystem
- 7.10 Decision Support

## 7.1 Identity and Role

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

## 7.2 Version Control Guidance

**What it needs to achieve:** Establish the agent's default stance on version control (typically: commit early and often) and name the few hard constraints (typically: never push without permission).

**Common mistakes:**
- The scenario-list anti-pattern (see [12-failure-catalogue.md](12-failure-catalogue.md)). Listing specific situations that should trigger commits causes the agent to treat the list as exhaustive.
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

## 7.3 Subagent and Parallelisation Guidance

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

## 7.4 Documentation Upkeep

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

## 7.5 Proactive Improvement

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

## 7.6 Note Capture

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

## 7.7 Operating Loops

**What it needs to achieve:** Define the per-task workflow rhythm. The operating loop is one of the most powerful persistence mechanisms — every iteration naturally reinforces the personality's values without needing to re-read the personality file.

**Common mistakes:**
- Too long to memorise — the agent cannot internalise a 15-step loop.
- Prescribes specific actions instead of describing the rhythm.
- Missing the verification and upkeep steps that make the loop self-reinforcing.

**Evaluation criteria:**
- Is it short enough to memorise (typically 4-7 steps)?
- Does it describe a rhythm rather than prescribing specific actions?
- Does it reinforce the personality's values (ground in context, verify against intent, update documentation)?
- Is it general enough to apply to any task?

**Comparison:**

| Weak (too specific) | Strong (rhythm) |
|---------------------|-----------------|
| "1. Read the relevant context file. 2. Check the plan file. 3. Read the code. 4. Ask the user. 5. Write the code. 6. Run the tests. 7. Update the plan. 8. Update the context file. 9. Commit. 10. Summarise." | "1. Ground the next step in existing sources. 2. Clarify scope and trade-offs before acting. 3. Execute. 4. Verify against intent and interfaces. 5. Update context where the work created drift. 6. Assess whether accumulated drift warrants a skill pass." |

The weak version prescribes specific files and specific actions. The strong version describes a rhythm that applies to any task — the agent fills in the specifics based on the current situation.

## 7.8 Engineering Standards

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

## 7.9 Skill Ecosystem

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

## 7.10 Decision Support

**What it needs to achieve:** Define how the agent presents options and recommendations when a decision is needed. The number of options should match the problem, not a template.

**Common mistakes:**
- The 3-option anchoring anti-pattern (see [12-failure-catalogue.md](12-failure-catalogue.md)). Showing exactly 3 options in examples causes the agent to always produce exactly 3.
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
