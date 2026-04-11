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

A code health audit exists to systematically improve a codebase before major new work begins, or to surface the accumulated wins a codebase contains after a period of rapid iteration. It is the engineering equivalent of cleaning the workshop before starting a new project — you clear out the dead wood, sharpen the tools, organise the materials, fix the things that will slow you down later, and find the optimisations that have been quietly waiting for someone to look carefully.

The output is never code. It is always a set of fully justified, categorised recommendations that another engineer or agent can execute with confidence. The audit identifies what to fix; the implementation happens separately.

## 2. What This Skill Is

A repository-wide analysis that:

- surveys the entire codebase, not just the files you happened to touch recently,
- identifies concrete, actionable improvement opportunities across multiple dimensions (dead code, performance, modularity, data layout, consistency, and so on),
- justifies every finding with evidence from the actual code,
- **writes diagnostic tests when they would resolve uncertainty about a finding** — benchmarks to compare alternatives, equivalence tests to verify two functions behave the same, coverage tests to confirm dead-looking code is actually dead, integration tests to validate that an optimisation preserves behaviour,
- organises findings into a structured plan that can be executed incrementally,
- conducts targeted external research for systems where domain-specific knowledge would materially improve the analysis,
- respects the project's context, preferences, and guiding principles throughout.

## 3. What This Skill Is Not

- **Not a linter.** Linters check syntax, formatting, and simple rules. This skill analyses architecture, algorithms, patterns, data layout, and design quality.
- **Not a style guide enforcer.** Code style is subjective and is a linter's job. This skill focuses on structural and behavioural quality.
- **Not a feature designer.** This skill never proposes new features, capabilities, or behaviours. It improves what exists.
- **Not an architecture redesigner.** Proposing fundamental architectural changes (switching frameworks, restructuring the entire module hierarchy, changing the persistence layer) is out of scope. This skill works within the existing architecture.
- **Not a production code editor.** This skill never writes, edits, or deletes production source code. The carve-out is tests: the audit may write unit tests, integration tests, benchmarks, and minimal test infrastructure when those are needed to gather evidence for findings or to safely make a recommendation. Production source files are off-limits; the audit produces plan files for those.

## 4. The Two Inviolable Rules

### Rule 1: Zero Functional Change

Every proposed change must produce identical observable behaviour. If the application does X before the change, it must do exactly X after the change.

This rule exists because:

- changes that alter behaviour introduce bugs that are difficult to trace back to a "cleanup" commit,
- if the audit's recommendations change how something works, the engineer implementing them cannot trust that the rest of the recommendations are safe,
- the entire value of a code health audit is that it delivers improvements with high confidence — the moment a change is not provably safe, it becomes a feature change and belongs in a different workflow.

Edge cases:

- **Performance changes** are not functional changes, as long as the output is the same. Making an algorithm faster is fine. Making it produce different results is not.
- **Ordering changes** may be functional. If code currently processes items in a specific order and you propose changing the data structure, verify that order does not matter to the caller.
- **Floating-point precision** may change with algorithm modifications. If the application depends on exact floating-point values (deterministic replay, hash comparisons, reproducibility), even a mathematically equivalent change may violate this rule.
- **Side effects** matter. If dead code has side effects (logging, metrics, state mutations), removing it changes behaviour. Verify before recommending removal.

When in doubt, flag the finding with a behavioural impact warning rather than asserting it is safe.

### Rule 2: No New Overhead

Every proposed change must make the codebase simpler, faster, or cleaner without creating new maintenance burden.

This rule exists because:

- the purpose of a cleanup audit is to reduce entropy, not redistribute it,
- introducing a new abstraction to fix a small problem creates a new thing to maintain,
- adding a dependency to save a few lines of code adds a supply chain risk and an upgrade burden.

Examples of violations:

- adding a utility crate or package to replace a simple helper function,
- creating an interface or trait for something only implemented once,
- introducing a configuration file for values that genuinely never change,
- replacing straightforward code with a clever pattern that is harder to understand,
- adding a build step or preprocessing stage.

The test is simple: would the codebase be easier to maintain after this change? If the answer requires qualifications ("yes, but you need to understand the new abstraction..."), the change probably violates this rule.

**Test infrastructure is not "new overhead" in the prohibited sense.** Diagnostic tests the audit writes — unit tests, integration tests, benchmarks, equivalence checks, minimal test framework setup — count as verification infrastructure, not as the kind of overhead this rule forbids. Tests pay for themselves by catching regressions, resolving diagnostic uncertainty, and giving the implementing engineer confidence that proposed changes are safe. The discrimination is: production-code abstractions that exist only to scaffold a small fix violate the rule; tests that exist to prove a finding's correctness or to lock in current behaviour before a change do not.

## 5. The "Free Upgrade" Principle

A "free upgrade" is a change where:

- the application behaves identically,
- the code is demonstrably better — faster, simpler, more modular, less redundant, more cache-friendly, easier to read,
- no new maintenance burden is created,
- the change can be implemented with high confidence and low risk to correctness.

The entire output of this skill should consist of free upgrades. Every finding that does not meet all four criteria should either be dropped or explicitly flagged as "not free — requires decision."

### "Free" Does Not Mean "Easy" or "Surface-Level"

The most valuable findings in an audit are often free but not easy. A change that flattens a fragmented buffer into a contiguous one and gains a many-fold throughput improvement is free — it produces identical output, removes maintenance cost rather than adding it, and can be verified rigorously. It is not surface-level. It is not a one-line edit. It still belongs in the audit, and skipping it because it requires careful work would defeat the purpose of running the audit at all.

Effort and freeness are independent dimensions. Do not drop a finding because implementing it would take real engineering work. Drop a finding only when implementing it would change observable behaviour or add maintenance burden.

The audit's job is to surface the real wins, including the deep ones. The trivial wins (unused imports, dead branches, obvious dead code) belong in the audit too, but they are the floor of the audit's value, not the ceiling.

## 6. Relationship to Project Context

This skill reads the project's `context/` folder before exploring the codebase. This is essential because:

- `context/architecture.md` provides the structural map — without it, the audit would waste time rediscovering the architecture,
- `context/systems/` files explain subsystem boundaries, interfaces, and active risks — findings should respect these boundaries,
- `context/notes/` captures project preferences and guiding principles — findings that contradict these preferences are likely wrong, and the notes should be checked before recommending a change that would diverge from a stated preference,
- `context/references/` may contain existing research that informs optimisation decisions,
- `context/plans/` may show active work that should be respected rather than flagged as incomplete.

Project preferences and patterns matter. A finding that asks the codebase to diverge from an established convention should clear a higher bar — it must offer a concrete, substantial benefit and explain why the divergence is worth the consistency cost. But the bar is not infinite. When local optimisation delivers a substantial speedup, removes a real correctness risk, or eliminates a maintenance burden, the audit should still surface it. The implementing engineer can decide whether the consistency cost is worth paying.

The audit's output goes into `context/plans/` as a subfolder, following the same lifecycle as any other plan file. The context upkeep workflow will maintain it — ticking checkboxes as items are implemented, and removing it when the work is complete.

## 7. When to Run This Skill

Good times to run a code health audit:

- before starting a major new feature or system — clean up first, then build,
- after a long period of rapid iteration where code quality may have drifted,
- when switching focus to a different part of the codebase that has not been maintained,
- when performance concerns arise and a systematic analysis is more valuable than spot fixes,
- when the codebase has grown substantially and accumulated technical debt,
- when a deep optimisation pass on a specific subsystem reveals that the broader codebase likely has similar wins waiting to be found.

Bad times to run a code health audit:

- in the middle of active feature development where the findings will be immediately stale,
- when the codebase is about to undergo a major architectural change that would invalidate the findings,
- for a trivially small codebase where manual inspection is faster.

## 8. Mindset

The audit should be thorough and ambitious. The goal is to find every meaningful improvement opportunity the codebase contains, justify each one rigorously, and present them in a way that makes execution straightforward.

A good audit:

- covers the entire codebase and goes deep into every system that does substantive work, regardless of whether the system "looks computationally heavy,"
- conducts targeted research per system rather than relying only on generic detection techniques,
- finds wins that are free (identical behaviour, no new burden) but are not necessarily obvious or easy,
- produces findings the engineer will actually want to implement,
- never makes the engineer question whether a recommendation is safe,
- respects the project's existing patterns where consistency matters more than local optimisation, but does not let consistency become an excuse for missing high-leverage wins.

Surface findings on a substantial system are a red flag, not a sign that the system was clean. The trap to watch for is the assumption that "this system isn't math-heavy, so there's nothing deep to find here." That assumption is almost always wrong. Optimisation opportunities live everywhere — not only in numerical kernels and tight inner loops, but also in:

- a request handler that runs the same query four times because the result was not cached,
- a response builder that walks the same dictionary three times because the loop structure was not consolidated,
- a parser that allocates a new buffer for every token instead of reusing one,
- a permission check that scans an entire role list instead of using a set,
- a logger that formats expensive structured payloads even when the log level discards them,
- a config loader that re-reads the file from disk on every call,
- a job dispatcher that uses an O(n²) match instead of an index,
- a serialiser that traverses objects twice because the schema lookup is in the wrong place.

None of these systems "look computationally heavy." None of them involve linear algebra or simulation or graphics. Every one of them is a real opportunity that an audit should find. The agent's job is to read the code carefully enough to notice the wasted work, regardless of whether the surface looks numerical.

If a system returned only minor findings, the deep dive did not happen. Go back, read the actual logic, trace the hot paths, conduct domain-specific research where it applies, and look for the algorithmic, layout, allocation, redundancy, and indirection wins that were missed on the first pass. The bar for "audited" is "you understood the system well enough to spot what a senior engineer specialising in this domain would spot," not "you skimmed the file and saw nothing obvious."

The audit's value is proportional to the depth of the analysis. A thorough audit on a substantial codebase should usually surface findings that surprise the engineer — wins they would not have thought to look for, framed in a way that makes them obvious in retrospect. If the audit only finds things the engineer already suspected, it has not done enough work.
