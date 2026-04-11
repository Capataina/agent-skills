---
name: code-health-audit
description: "Repository-wide code health audit identifying dead code, unused dependencies, modularisation opportunities, hardcoded patterns extractable to algorithms, algorithm and performance optimisations, data layout and memory access wins, complexity hotspots, inconsistent patterns, API surface bloat, configuration drift, documentation rot, test coverage gaps, and active risks. Reads context, conducts targeted research per substantive system, and writes diagnostic tests (unit, integration, benchmarks, equivalence checks) when they would resolve uncertainty before findings are issued. Produces categorised plan files plus the diagnostic tests written — never edits production source code. Every finding is provably free: identical behaviour, no new maintenance burden, full evidence chain. Use when asked to audit code health, find code smells, clean up a codebase, sweep for dead code, optimise performance, write diagnostic tests, or improve quality."
---

# Code Health Audit

Perform a comprehensive, repository-wide code health audit that identifies improvement opportunities across the entire codebase. The output is an organised set of plan files plus the diagnostic tests the audit wrote to verify its findings. Production source code is never edited; tests are written when they would resolve uncertainty before issuing a recommendation. Every proposed change must be provably "free": identical behaviour, better implementation.

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
- finds algorithm-level optimisation opportunities through better algorithms, data structures, or eliminated work,
- finds general performance wins through reduced waste, better resource usage, and removed redundancy,
- finds data layout and memory access pattern wins — buffer flattening, contiguous storage, allocation reuse, cache locality, vectorisation-friendliness, removed indirection — which are often the highest-leverage findings in computationally heavy systems,
- spots inconsistent patterns, complexity hotspots, and API surface bloat,
- flags known issues, active risks, configuration drift, documentation rot, and test coverage gaps for critical paths,
- conducts targeted external research per system to find domain-specific optimisation strategies grounded in the actual codebase,
- writes diagnostic tests — unit tests, integration tests, benchmarks, equivalence checks, baseline pins, and minimal test infrastructure — when they would resolve uncertainty about a finding before that finding is issued,
- produces fully justified, categorised plan files that another engineer or agent can execute confidently.

It must reject:

- making any production source code changes,
- proposing changes that alter application behaviour without explicit flagging,
- proposing changes that introduce new dependencies, abstraction layers, or maintenance overhead in production code,
- guessing about how systems work instead of reading the code,
- producing vague recommendations without evidence and justification,
- skipping deep analysis on substantive systems because the surface looks clean,
- writing tests as a way to bulk up output rather than to gather evidence for findings.

## Inviolable Rules

### Rule 1: Zero Functional Change

Every proposed change must produce identical observable behaviour. The application must function exactly the same way before and after the change is implemented.

If a proposed change *might* alter behaviour — even negligibly — it must be explicitly flagged with a behavioural impact assessment. The agent implementing the change can then make an informed decision. But the default posture is: if there is any doubt, do not recommend it as a "free" change.

### Rule 2: No New Overhead in Production Code

The purpose of this skill is to reduce complexity, not add it. Every proposed change to production code must make the codebase simpler, faster, or cleaner without creating new maintenance burden.

Changes that violate this rule:

- adding a new dependency to replace a few lines of code,
- introducing an abstraction layer for a one-time pattern,
- creating a configuration system for values that are genuinely constant,
- replacing simple code with a "more elegant" but harder-to-understand pattern.

**Test infrastructure is the carve-out.** Diagnostic tests the audit writes — unit tests, integration tests, benchmarks, equivalence checks, baseline pins, and minimal test framework setup — count as verification infrastructure, not as the kind of overhead this rule forbids. Tests pay for themselves by catching regressions, resolving diagnostic uncertainty, and giving the implementing engineer confidence that proposed changes are safe. The discrimination is: production-code abstractions that exist only to scaffold a small fix violate the rule; tests that exist to prove a finding's correctness or to lock in current behaviour before a change do not.

### Rule 3: Production Source Code Stays Untouched

The audit does not write, edit, or delete production source files. Production code is the implementing engineer's territory; the audit produces plan files for those changes. The carve-out for tests in Rule 2 does not extend to production source.

## Two-Pass Approach

The audit follows a structured two-pass approach:

### Pass 1 — Context and Broad Scan

1. Read `context/architecture.md` and `context/notes.md` to understand the project's structure, systems, preferences, and guiding principles.
2. Read relevant `context/systems/` files to understand subsystem boundaries and current reality.
3. Read relevant `context/references/` files for existing research and technical context.
4. Perform a broad sweep of the codebase: understand the stack, the architecture, major subsystems, file sizes, obvious hotspots.
5. At this point, you know *what the project is and how it is built*, but you have not gone deep into any specific system. Prioritise the systems where the deep dive will be most valuable.

### Pass 2 — System-by-System Deep Dive

Pass 2 is iterative, not strictly sequential. The flow is: read the code until you hit an uncertainty, resolve the uncertainty with whichever tool fits (more reading, research, or a diagnostic test), then continue. The kinds of work that happen in Pass 2:

1. **Read the code deeply** — understand the implementation, follow the call chain, trace the hot paths, read the actual data access patterns.
2. **Conduct targeted research** for almost every substantive system, not just the obviously computational ones — request handlers, business logic, query handlers, schedulers, parsers, middleware, batch processors, and so on all benefit from research. Skip research only for genuinely trivial modules.
3. **Write diagnostic tests** when reading and research surface a question that a test would resolve — equivalence tests for "do these two functions actually behave the same," benchmarks for "which is faster," coverage probes for "is this code reachable," baseline pins for "what does the current behaviour look like before I propose changing it." Tests are interleaved with reading, not batched at the end. See the detection strategies reference for the full guidance.
4. **Analyse against every category in the taxonomy**. Pay particular attention to the Data Layout and Memory Access Patterns category for systems with hot loops over substantial data.
5. **Record findings with full evidence and justification**, referencing any diagnostic tests the audit wrote so the implementing engineer can re-run them.

Research and diagnostic test writing happen *per system* because they need to be targeted. You do not research "how to optimise a query planner" or write a benchmark for it before you know the project has one and how it is implemented. You do both when you are deep in the storage engine and can ask the right questions, with the actual code in front of you to validate the findings against.

## Output

The skill produces two kinds of output:

**A plan folder inside `context/plans/`** named for the audit (e.g., `context/plans/code-health-audit/`). This folder contains:

- an `index.md` file summarising all findings grouped by category and system,
- one file per major category or system, depending on what organisation best serves the findings (see output structure reference for guidance).

The plan folder follows the same lifecycle as any plan file: it exists while the work is active, items get ticked as they are implemented, and the folder is removed once all actionable items are complete or consciously deferred.

**Diagnostic tests in the project's test suite.** The audit writes tests directly into the project's existing test directory, following the project's existing test conventions. These tests live permanently in the test suite — they are not scaffolding to be deleted. Each finding that is grounded in a test the audit wrote should reference the test file path so the implementing engineer can re-run it to verify their changes. If the project has no test infrastructure at all, the audit can stand up the minimal setup needed (test framework, runner config, conventional directory) — but only what is required for the diagnostic work.

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
- no finding introduces new overhead, dependencies, or maintenance burden in production code,
- findings are categorised correctly according to the taxonomy,
- the plan folder is organised logically with a clear index,
- research was conducted for every substantive system in the project — not only the obviously computational ones — and not skipped because the surface looked clean,
- research findings are grounded in the actual codebase, not generic advice,
- diagnostic tests were written wherever they would resolve uncertainty about a finding before that finding was issued,
- diagnostic tests live in the project's test suite (not in the plan folder) and are referenced from the findings they support,
- if the audit stood up new test infrastructure, it is the minimal version needed for the diagnostic work and follows the project's conventions for the stack,
- no test was written to bulk up output rather than to gather evidence,
- the audit covers the full codebase, not just the areas that were easiest to analyse,
- the Data Layout and Memory Access Patterns category was applied to every system with hot loops, hot allocation paths, or substantial data movement,
- dead code identification accounts for dynamic dispatch, reflection, macros, and other indirect usage patterns — and is backed by coverage probes the audit wrote where reflection or dynamic dispatch make static analysis insufficient,
- severity and priority rankings reflect actual impact, not just ease of detection,
- "free" findings are free in the sense of zero behavioural change and no new production-code burden, not in the sense of trivial implementation effort,
- production source code was not modified — only test files and the plan folder.
