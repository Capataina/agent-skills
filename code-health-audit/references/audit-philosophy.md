# Audit Philosophy

This reference defines what a code health audit is, what it is not, and the principles that govern every finding.

## Table of Contents

1. Purpose
2. What This Skill Is
3. What This Skill Is Not
4. The Two Inviolable Rules
5. The "Free Upgrade" Principle
6. Relationship to Project Context
7. When to Run This Skill
8. Mindset

## 1. Purpose

A code health audit exists to systematically improve a codebase before major new work begins. It is the engineering equivalent of cleaning the workshop before starting a new project — you clear out the dead wood, sharpen the tools, organise the materials, and fix the things that will slow you down later.

The output is never code. It is always a set of fully justified, categorised recommendations that another engineer or agent can execute with confidence. The audit identifies what to fix; the implementation happens separately.

## 2. What This Skill Is

A repository-wide analysis that:

- surveys the entire codebase, not just the files you happened to touch recently,
- identifies concrete, actionable improvement opportunities across multiple dimensions (dead code, performance, modularity, consistency, etc.),
- justifies every finding with evidence from the actual code,
- organises findings into a structured plan that can be executed incrementally,
- conducts targeted research when domain-specific knowledge is needed to identify or validate optimisations,
- respects the project's context, preferences, and guiding principles throughout.

## 3. What This Skill Is Not

- **Not a linter.** Linters check syntax, formatting, and simple rules. This skill analyses architecture, algorithms, patterns, and design quality.
- **Not a style guide enforcer.** Code style is subjective and is a linter's job. This skill focuses on structural and behavioural quality.
- **Not a feature designer.** This skill never proposes new features, capabilities, or behaviours. It improves what exists.
- **Not an architecture redesigner.** Proposing fundamental architectural changes (switching frameworks, restructuring the entire module hierarchy, changing the persistence layer) is out of scope. This skill works within the existing architecture.
- **Not a code editor.** This skill never writes, edits, or deletes source code. It produces plan files.

## 4. The Two Inviolable Rules

### Rule 1: Zero Functional Change

Every proposed change must produce identical observable behaviour. If the application does X before the change, it must do exactly X after the change.

This rule exists because:

- changes that alter behaviour introduce bugs that are difficult to trace back to a "cleanup" commit,
- if the audit's recommendations change how something works, the engineer implementing them cannot trust that the rest of the recommendations are safe,
- the entire value of a code health audit is that it delivers "free" improvements — the moment a change is not free, it becomes a feature change and belongs in a different workflow.

Edge cases:

- **Performance changes** are not functional changes, as long as the output is the same. Making an algorithm faster is fine. Making it produce different results is not.
- **Ordering changes** may be functional. If code currently processes items in a specific order and you propose changing the data structure, verify that order does not matter to the caller.
- **Floating-point precision** may change with algorithm modifications. If the application depends on exact floating-point values (e.g., deterministic replay), even a mathematically equivalent change may violate this rule.
- **Side effects** matter. If dead code has side effects (logging, metrics, state mutations), removing it changes behaviour. Verify before recommending removal.

When in doubt, flag the finding with a behavioural impact warning rather than asserting it is "free."

### Rule 2: No New Overhead

Every proposed change must make the codebase simpler, faster, or cleaner without creating new maintenance burden.

This rule exists because:

- the purpose of a cleanup audit is to reduce entropy, not redistribute it,
- introducing a new abstraction to fix a small problem creates a new thing to maintain,
- adding a dependency to save 10 lines of code adds a supply chain risk and upgrade burden.

Examples of violations:

- adding a utility crate/package to replace a simple helper function,
- creating an interface/trait for something only implemented once,
- introducing a configuration file for values that genuinely never change,
- replacing straightforward code with a clever pattern that is harder to understand,
- adding a build step or preprocessing stage.

The test is simple: would the codebase be easier to maintain after this change? If the answer requires qualifications ("yes, but you need to understand the new abstraction..."), the change probably violates this rule.

## 5. The "Free Upgrade" Principle

A "free upgrade" is a change where:

- the application behaves identically,
- the code is demonstrably better (faster, simpler, more modular, less redundant),
- no new maintenance burden is created,
- the change can be implemented with high confidence and low risk.

The entire output of this skill should consist of free upgrades. Every finding that does not meet all four criteria should either be dropped or explicitly flagged as "not free — requires decision."

## 6. Relationship to Project Context

This skill reads the project's `context/` folder before exploring the codebase. This is essential because:

- `context/architecture.md` provides the structural map — without it, the audit would waste time rediscovering the architecture,
- `context/systems/` files explain subsystem boundaries, interfaces, and active risks — findings should respect these boundaries,
- `context/notes/` captures project preferences and guiding principles — findings that contradict these preferences are likely wrong,
- `context/references/` may contain existing research that informs optimisation decisions,
- `context/plans/` may show active work that should be respected rather than flagged as incomplete.

The audit's output goes into `context/plans/` as a subfolder, following the same lifecycle as any other plan file. The context upkeep workflow will maintain it — ticking checkboxes as items are implemented, and removing it when the work is complete.

## 7. When to Run This Skill

Good times to run a code health audit:

- before starting a major new feature or system — clean up first, then build,
- after a long period of rapid iteration where code quality may have drifted,
- when switching focus to a different part of the codebase that has not been maintained,
- when performance concerns arise and a systematic analysis is more valuable than spot fixes,
- when the codebase has grown substantially and accumulated technical debt.

Bad times to run a code health audit:

- in the middle of active feature development (the findings will be immediately stale),
- when the codebase is about to undergo a major architectural change (the findings will be irrelevant),
- for a trivially small codebase where manual inspection is faster.

## 8. Mindset

The audit should be thorough but pragmatic. The goal is not to find every possible improvement — it is to find the improvements that matter most, justify them rigorously, and present them in a way that makes execution straightforward.

A good audit:

- covers the entire codebase but goes deepest where the most value is,
- produces findings the engineer will actually want to implement,
- never makes the engineer question whether a recommendation is safe,
- respects the project's style, patterns, and preferences even when they are not optimal — consistency is often more valuable than local perfection.
