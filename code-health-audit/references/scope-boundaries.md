# Scope Boundaries

This reference defines what the skill must never recommend, common false positives, and the line between code health cleanup and architecture change.

## Table of Contents

1. Hard Exclusions
2. The Architecture Boundary
3. Common False Positives
4. The Zero Functional Change Rule in Practice
5. The No New Overhead Rule in Practice
6. Grey Areas

## 1. Hard Exclusions

The following are always out of scope for a code health audit. Do not produce findings in these areas:

### Source Code Edits

This skill never writes, edits, or deletes source code. It only produces plan files. If you find yourself about to modify a source file, stop.

### New Features

Do not propose adding capabilities the application does not currently have. "The application should also support X" is a feature request, not a code health finding.

### Framework or Language Migrations

"Rewrite this in language X" or "switch from framework A to framework B" is out of scope, even if the current choice is suboptimal. These are architectural decisions, not cleanup.

### Style and Formatting

Code style, indentation, bracket placement, naming conventions (beyond the scope of the Inconsistent Patterns category), and formatting are linter responsibilities. Do not flag them.

### Architecture Redesign

Changing the fundamental organisation of the application — its module hierarchy, its persistence model, its communication patterns, its deployment architecture — is out of scope. The audit works *within* the existing architecture.

### Test Writing

The audit may flag test coverage gaps, but it never writes tests. Recommending "add tests for X" in the Known Issues category is acceptable. Providing test code is not.

### Dependency Upgrades

Flagging unused or vulnerable dependencies is in scope. Recommending major version upgrades of active dependencies is out of scope — version upgrades may introduce breaking changes and belong in a separate workflow.

### Configuration of External Systems

Build system configuration, CI/CD pipeline changes, deployment configuration, and infrastructure changes are out of scope unless they are trivially wrong (e.g., a build flag that is clearly incorrect).

## 2. The Architecture Boundary

The line between "cleanup" and "architecture change" is critical. Here is how to distinguish them:

### Cleanup (In Scope)

- Extracting a function from a large function.
- Splitting a large file into smaller files within the same module.
- Reducing the visibility of internal functions.
- Replacing an algorithm with a better one that has the same interface.
- Removing dead code.
- Consolidating duplicated code into a shared function.

### Architecture Change (Out of Scope)

- Moving modules to different locations in the project hierarchy.
- Changing the dependency direction between major subsystems.
- Introducing a new architectural pattern (event bus, plugin system, middleware chain).
- Changing how data flows between major components.
- Introducing new abstraction layers that span multiple subsystems.
- Changing the build or module system.

### The Test

Ask: "Does this change affect how the system is *organised at the highest level*, or just how one part *works internally*?"

If it affects high-level organisation: architecture change, out of scope.
If it affects internal implementation: cleanup, in scope.

## 3. Common False Positives

These patterns look like findings but usually are not:

### "Unused" Code That Is Dynamically Invoked

Many languages and frameworks invoke code through mechanisms that do not appear in static analysis:

- **Reflection/introspection** — methods invoked by name at runtime.
- **Macros and code generation** — code generated at compile time that calls functions.
- **Serialisation/deserialisation** — struct fields that appear unused but are populated by a deserialiser.
- **Plugin or extension systems** — functions registered as callbacks.
- **External callers** — code in a library that is called by downstream consumers.
- **Event handlers** — functions registered with a framework's event system.
- **Template engines** — functions called from templates that are not Rust/Python/etc. files.

Before declaring code dead, check for these patterns. If you are unsure, classify as "Triage Needed."

### Intentionally Retained Fallback Code

Code that is not currently used but is kept as a documented fallback or emergency mechanism. Check project notes and comments for indications like "retained as fallback" or "emergency override."

### Recently Added Code

Code that was recently added as part of ongoing work may not have callers yet. Check active plans before flagging it.

### Platform-Specific Code

Code that only executes on certain platforms or under certain configurations. It may appear dead in the current build but is active on other targets.

### Test Code and Fixtures

Test helpers, fixtures, and mocks may not be called from production code. That is by design. Only flag test code that is genuinely unused by any test.

### Intentionally Simple Code

Code that looks like it could be "optimised" but is intentionally simple for readability, debuggability, or correctness:

- Explicit loops instead of iterator chains for clarity in complex logic.
- Separate variables instead of chained expressions for debuggability.
- Redundant bounds checks for safety in critical code.

Check project notes for explicit preferences about code style in specific areas.

## 4. The Zero Functional Change Rule in Practice

### Easy Cases

- Removing a function with zero callers: zero functional change (verified).
- Removing an unused import: zero functional change (by construction).
- Pre-allocating a buffer: zero functional change (same output, less allocation).

### Hard Cases

- **Changing sort algorithm:** most sort algorithms are not stable. If the input contains equal elements and the code depends on their relative order, changing the algorithm changes behaviour. Verify stability requirements.
- **Changing floating-point operations:** mathematically equivalent operations may produce different floating-point results. If the application depends on exact values (deterministic replay, hash comparisons), this is a functional change.
- **Removing logging or metrics:** even if logging is "not functional," removing it changes what operators can observe. Flag this explicitly.
- **Changing error handling:** replacing a panic with a Result return changes the API contract. Catching an error that was previously uncaught changes behaviour for callers.
- **Changing iteration order:** if you replace a HashMap with a BTreeMap for performance, the iteration order changes. If any consumer depends on that order, this is a functional change.

### When in Doubt

If you cannot prove zero functional change with confidence, either:
- classify the finding as "Possible impact (requires decision)," or
- drop the finding entirely.

Never present a finding as "free" when the impact analysis is uncertain.

## 5. The No New Overhead Rule in Practice

### Easy Cases

- Deleting dead code: reduces overhead (by definition).
- Replacing an algorithm with a simpler one: reduces overhead.
- Extracting a function: neutral overhead (same code, different location).

### Hard Cases

- **Adding a caching layer:** reduces compute overhead but adds memory overhead and cache invalidation complexity. May or may not be a net improvement.
- **Introducing a shared utility module:** reduces duplication but adds a new module to maintain. Usually worth it if three or more callsites benefit.
- **Replacing hardcoded values with configuration:** adds configuration management overhead. Only worth it if the values genuinely need tuning.
- **Adding type wrappers or newtypes:** adds a small abstraction but improves type safety. Usually worth it in safety-critical code, overkill in utility code.

### The Test

Would a new engineer, encountering this change for the first time, say "this made the code simpler" or "this added a new thing I need to understand"?

If the latter, the change may violate the no-new-overhead rule.

## 6. Grey Areas

Some findings exist in grey areas between categories or between in-scope and out-of-scope. Handle them explicitly:

### Performance vs. Architecture

If a performance improvement requires restructuring how data flows between systems, it is an architecture change and out of scope. If it only requires changing the implementation within one system, it is in scope.

### Modularisation vs. Redesign

Splitting a large file into smaller files within the same module is in scope. Reorganising the module hierarchy is out of scope.

### Consistency vs. Style

Flagging three different error handling approaches in the same project is in scope (inconsistent patterns). Flagging that the project uses `snake_case` instead of `camelCase` is out of scope (style).

### Bug Fix vs. Known Issue

Flagging a bug is in scope (known issues). Fixing the bug is not (this skill does not write code). The finding should clearly identify the bug and suggest how to fix it, but the fix is implemented separately.

When a grey area is genuinely ambiguous, include the finding but explicitly note the ambiguity and let the implementing engineer decide whether to act on it.
