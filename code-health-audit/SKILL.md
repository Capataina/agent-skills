---
name: code-health-audit
description: "Performs a comprehensive repository-wide code health audit identifying dead code, unused dependencies, modularisation opportunities, hardcoded patterns extractable to algorithms, performance optimisations, complexity hotspots, inconsistent patterns, API surface bloat, configuration drift, documentation rot, test coverage gaps, and active risks. Reads context to understand systems before exploring code. Produces categorised plan files — analysis only, never edits source code. Every finding includes current state, proposed change, justification, expected benefit, and behavioural impact assessment. All changes must be provably free — identical behaviour, better implementation. Use when asked to audit code health, find code smells, clean up a codebase, refactor, sweep for dead code, optimise performance, or improve quality."
---

# Code Health Audit

Perform a comprehensive, repository-wide code health audit that identifies improvement opportunities across the entire codebase. The output is an organised set of plan files — analysis and planning only, never source code edits. Every proposed change must be provably "free": identical behaviour, better implementation.

Before beginning any audit, read the reference files in this order:

1. Read `references/audit-philosophy.md` first.
   It defines what this skill is, what it is not, and the two inviolable rules that govern every finding.
2. Read `references/analysis-categories.md` second.
   It defines the full taxonomy of finding types, their definitions, and the boundaries between them.
3. Read `references/detection-strategies.md` third.
   It defines how to find issues — the two-pass approach, exploration patterns, when and how to conduct targeted research, and stack-agnostic techniques.
4. Read `references/evidence-and-justification.md` fourth.
   It defines the proof chain every finding requires and how to assess behavioural impact.
5. Read `references/severity-and-prioritisation.md` fifth.
   It defines how to rank, group, and order findings by impact and effort.
6. Read `references/output-structure.md` sixth.
   It defines how to organise the output folder, name files, and structure the index.
7. Read `references/finding-format.md` seventh.
   It defines the template for individual findings — required fields, depth expectations, and writing standards.
8. Read `references/scope-boundaries.md` eighth.
   It defines what the skill must never recommend, common false positives, and the line between cleanup and architecture change.
9. Read `references/examples.md` last.
   It contains worked examples of good audit findings, including rejected findings that looked promising but would have changed behaviour.

## Core Identity

This skill is not a linter, a style checker, or a feature implementer.

It is a **repository-wide code health analyst** that:

- finds dead code, unused dependencies, and obsolete artefacts for removal,
- identifies modularisation and structural improvement opportunities,
- detects hardcoded values and patterns that could be computed algorithmically,
- finds performance optimisation opportunities through better algorithms, data structures, or resource usage,
- spots inconsistent patterns, complexity hotspots, and API surface bloat,
- flags known issues, active risks, configuration drift, documentation rot, and test coverage gaps for critical paths,
- conducts targeted external research to find domain-specific optimisation strategies grounded in the actual codebase,
- produces fully justified, categorised plan files that another engineer or agent can execute confidently.

It must reject:

- making any source code changes,
- proposing changes that alter application behaviour,
- proposing changes that introduce new dependencies, abstraction layers, or maintenance overhead,
- guessing about how systems work instead of reading the code,
- producing vague recommendations without evidence and justification.

## Inviolable Rules

### Rule 1: Zero Functional Change

Every proposed change must produce identical observable behaviour. The application must function exactly the same way before and after the change is implemented.

If a proposed change *might* alter behaviour — even negligibly — it must be explicitly flagged with a behavioural impact assessment. The agent implementing the change can then make an informed decision. But the default posture is: if there is any doubt, do not recommend it as a "free" change.

### Rule 2: No New Overhead

The purpose of this skill is to reduce complexity, not add it. Every proposed change must make the codebase simpler, faster, or cleaner without creating new maintenance burden.

Changes that violate this rule:

- adding a new dependency to replace a few lines of code,
- introducing an abstraction layer for a one-time pattern,
- creating a configuration system for values that are genuinely constant,
- replacing simple code with a "more elegant" but harder-to-understand pattern.

## Structural Rules and Creative Freedom

The structural rules in this skill — output folder location, finding format fields, index structure, category taxonomy — are fixed. They exist to make audit output predictable and actionable across projects and agents.

Everything within that structure is yours. How you explain a finding, what depth of analysis you reach, what visual representations you choose to clarify a complex issue, how you scope your research queries — these are matters of judgment and creative expression. The goal is maximum clarity and usefulness for the engineer who will implement the findings.

## Two-Pass Approach

The audit follows a structured two-pass approach:

### Pass 1 — Context and Broad Scan

1. Read `context/architecture.md` and `context/notes.md` to understand the project's structure, systems, preferences, and guiding principles.
2. Read relevant `context/systems/` files to understand subsystem boundaries and current reality.
3. Read relevant `context/references/` files for existing research and technical context.
4. Perform a broad sweep of the codebase: understand the stack, the architecture, major subsystems, file sizes, obvious hotspots.
5. At this point, you know *what the project is and how it is built*, but you have not gone deep into any specific system.

### Pass 2 — System-by-System Deep Dive

For each major system or subsystem:

1. Read the code deeply — understand the implementation, not just the structure.
2. Conduct targeted research for domain-specific optimisation strategies relevant to what you found (see detection strategies reference for guidance on research scoping).
3. Analyse against every category in the taxonomy.
4. Record findings with full evidence and justification.

The research happens *per system* because it needs to be targeted. You do not research "how to optimise a query planner" before you know the project has a query planner and how it is implemented. You research it when you are deep in the storage engine and can ask the right questions.

## Output

The skill produces a folder inside `context/plans/` named for the audit (e.g., `context/plans/code-health-audit/`). This folder contains:

- an `index.md` file summarising all findings grouped by category and system,
- one file per major category or system, depending on what organisation best serves the findings (see output structure reference for guidance).

The output follows the same lifecycle as any plan file: it exists while the work is active, items get ticked as they are implemented, and the folder is removed once all actionable items are complete or consciously deferred.

## Evidence Standard

Every finding must be grounded in inspected code, not in assumptions about what the code probably does.

- Read the actual implementation before proposing changes.
- Understand the full call chain before declaring code "dead."
- Verify that a pattern is truly hardcoded before proposing algorithmic replacement.
- Confirm that an optimisation applies to the specific implementation, not just to the general case.
- Use context files as orientation, but verify against the code.

When a finding is based partly on inference rather than direct observation, say so explicitly.

## Quality Checklist

Before presenting the audit results, verify:

- every finding includes the full proof chain: current state, proposed change, justification, expected benefit, behavioural impact assessment,
- no finding proposes a change that would alter application behaviour without explicit flagging,
- no finding introduces new overhead, dependencies, or maintenance burden,
- findings are categorised correctly according to the taxonomy,
- the output folder is organised logically with a clear index,
- research was conducted for systems where domain-specific optimisation knowledge was needed,
- research findings are grounded in the actual codebase, not generic advice,
- the audit covers the full codebase, not just the areas that were easiest to analyse,
- dead code identification accounts for dynamic dispatch, reflection, macros, and other indirect usage patterns,
- severity and priority rankings reflect actual impact, not just ease of detection.
