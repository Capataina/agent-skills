# Analysis Categories

This reference defines the full taxonomy of finding types. Every finding in the audit must be classified into exactly one category. The categories are designed to be mutually exclusive and collectively exhaustive for the scope of this skill.

## Table of Contents

1. Dead Code Removal
2. Triage Needed
3. Modularisation
4. Pattern Extraction
5. Algorithm Optimisation
6. Performance Improvement
7. Inconsistent Patterns
8. Dependency Hygiene
9. Configuration Drift
10. API Surface Bloat
11. Test Coverage Gaps
12. Documentation Rot
13. Complexity Hotspots
14. Known Issues and Active Risks

## 1. Dead Code Removal

### Definition

Code that is demonstrably unused and has no remaining purpose. It was once relevant but the codebase has moved past it.

### What to Look For

- Functions, methods, classes, or modules that are never called from any live code path.
- Imports that are never used.
- Feature flags or conditional branches for features that were fully removed or fully shipped.
- Commented-out code blocks that have been there for a significant time.
- Old implementations that were replaced but never deleted (e.g., a `ReLU` activation function left behind after switching to `tanh`).
- Deprecated API endpoints or handlers that are no longer routed to.
- Test fixtures or helper code for tests that no longer exist.

### What NOT to Flag

- Code that appears unused but is invoked via reflection, dynamic dispatch, macros, code generation, serialisation, or external configuration. Verify the call chain before declaring code dead.
- Code that is part of a public library API — external consumers may depend on it even if the internal codebase does not use it.
- Code that is intentionally retained as a fallback or emergency mechanism, documented as such.
- Recently added code that may not have callers yet because the integration work is in progress (check active plans).

### Severity Guidance

- Large dead modules or files: high — they create confusion and maintenance burden.
- Individual dead functions: medium — less confusing but still clutter.
- Unused imports: low — trivial to fix, minimal impact.

## 2. Triage Needed

### Definition

Code that appears unused or questionable but requires a human decision because the intent is ambiguous. The audit cannot confidently classify it as dead code or as intentionally retained.

### What to Look For

- Functions that are not called anywhere but seem too specific or well-crafted to be accidental leftovers.
- Utility functions that may have been written for future use that never arrived.
- Modules that are partially integrated — some functions are used, others are not.
- Code behind feature flags where the flag's current state is unclear.
- Code that seems to duplicate functionality in another module but with slight differences.

### What NOT to Flag

- Code that is clearly dead (belongs in Dead Code Removal).
- Code that is clearly used (not a finding at all).

### Severity Guidance

- Items in this category do not have a severity ranking because the correct action depends on context only the user has. Present them clearly and let the user decide.

## 3. Modularisation

### Definition

Code that is functional but structurally monolithic — large files, tightly coupled components, or mixed responsibilities that would benefit from being split into smaller, more focused units.

### What to Look For

- Files above a reasonable size threshold for their language and role (context-dependent — a 500-line Rust module may be fine, a 500-line utility file probably is not).
- Functions or methods that do multiple distinct things sequentially.
- Classes or structs that have too many responsibilities (violation of single responsibility).
- Modules that mix business logic with infrastructure concerns (I/O, serialisation, logging).
- Code that would be independently testable if extracted.
- Repeated patterns across files that could share a common extracted component.

### What NOT to Flag

- Files that are large because the domain genuinely requires it (e.g., a comprehensive state machine, a parser for a complex format).
- Code that is already well-structured internally even if the file is large.
- Cases where splitting would create worse coupling (two modules that constantly need to import from each other).

### Severity Guidance

- Modules with mixed responsibilities that make changes risky: high.
- Large files that are hard to navigate but internally coherent: medium.
- Minor opportunities to extract shared utilities: low.

## 4. Pattern Extraction

### Definition

Hardcoded values, repetitive constructs, or manually specified sequences that follow a computable pattern and could be expressed algorithmically.

### What to Look For

- Arrays or lists of values that follow a mathematical progression (e.g., `[5, 15, 45, 135]` — a geometric sequence that could be generated).
- Manually specified coordinates, angles, offsets, or spacings that follow a regular pattern (e.g., 32 raycasts with equal angular spacing).
- Repeated code blocks that differ only in a parameter that follows a pattern.
- Lookup tables that could be computed from a formula.
- Configuration arrays where the values are derived from a rule.

### What NOT to Flag

- Hardcoded values that do NOT follow a computable pattern — if the values are arbitrary or specifically tuned, they need to stay hardcoded. Changing them to algorithmic generation would alter behaviour.
- Constants that are genuinely constant and benefit from being explicit (e.g., `PI`, gravitational constants, protocol magic numbers).
- Values that were intentionally tuned through experimentation — even if they look like they follow a pattern, they may not. Check project notes for context.

### Important

This category has the highest risk of violating the Zero Functional Change rule. Before proposing a pattern extraction:

- verify that the values exactly match the proposed algorithm's output,
- confirm that the order of values does not matter, or that the algorithm preserves the same order,
- check whether the values were manually tuned (project notes may say so).

### Severity Guidance

- Large arrays of values that are clearly generated from a formula: high — reduces maintenance and makes the pattern explicit.
- Small sets of values with an obvious pattern: medium.
- Micro-patterns (2-3 values): low — may not be worth the change.

## 5. Algorithm Optimisation

### Definition

Cases where the current algorithm works correctly but a better algorithm or data structure exists that would improve performance without changing observable behaviour.

### What to Look For

- Sorting + truncation when a partial sort or selection algorithm would suffice (e.g., sorting an entire list to get the top 10).
- Linear search in a collection that could use a more efficient data structure (hash map, binary search tree, KD-tree, spatial index).
- Quadratic or worse algorithms where a linear or log-linear solution exists.
- Repeated computation of the same value that could be cached or memoised.
- String concatenation in a loop where a builder/buffer pattern would be more efficient.
- Brute-force approaches where established algorithms solve the same problem (e.g., brute-force nearest neighbour vs. KD-tree).

### What NOT to Flag

- Algorithms that are already optimal for their input size — an O(n^2) algorithm on a list of 10 items is not a problem.
- Cases where the "better" algorithm has significant implementation complexity and the current one is not a bottleneck.
- Optimisations that would require restructuring the data model to implement.
- Cases where algorithmic correctness is not identical (e.g., approximate vs. exact algorithms, unless the approximation is proven equivalent for the use case).

### Important

Algorithm changes require careful justification. The finding must demonstrate:

- what the current algorithm's complexity is,
- what the proposed algorithm's complexity is,
- why the improvement matters for the actual data sizes in the project,
- that the output is identical for all inputs the application produces.

### Severity Guidance

- Quadratic or worse algorithms on potentially large datasets: high.
- Suboptimal but not catastrophic algorithms on medium datasets: medium.
- Minor improvements on small datasets: low.

## 6. Performance Improvement

### Definition

General performance wins that do not involve algorithm changes — eliminating waste, reducing allocations, avoiding unnecessary work, or improving resource usage.

### What to Look For

- Unnecessary heap allocations in hot paths (e.g., creating vectors in a tight loop that could be pre-allocated).
- Redundant copies or clones where a reference or borrow would work.
- Unnecessary intermediate collections (e.g., collecting into a vector only to iterate again).
- Repeated file I/O, database queries, or network calls where a single call and caching would suffice.
- Synchronous blocking operations in async contexts.
- Unnecessary serialisation/deserialisation round-trips.
- Resource leaks (unclosed file handles, connections, subscriptions).
- Computations in hot paths that could be hoisted out of loops.
- Texture, asset, or resource loading that happens every frame instead of being cached.

### What NOT to Flag

- Performance characteristics that are inherent to the chosen architecture.
- Micro-optimisations that would make code harder to read for negligible gain.
- Performance issues that would require architectural changes to fix (out of scope).

### Severity Guidance

- Hot-path waste in performance-critical loops: high.
- Redundant I/O or allocations in moderately exercised code: medium.
- Minor allocation waste in cold paths: low.

## 7. Inconsistent Patterns

### Definition

The same conceptual operation done differently in different parts of the codebase. Not a bug, but a maintenance trap — inconsistency makes the codebase harder to understand and changes riskier.

### What to Look For

- Error handling done differently across modules (Result in one, panics in another, silent fallback in a third).
- Multiple patterns for the same structural concern (e.g., three different ways of reading configuration).
- Naming conventions that vary across modules.
- Different serialisation approaches for the same data.
- Inconsistent logging levels or formats.
- Mixed use of sync and async for similar operations.

### What NOT to Flag

- Deliberate variation that exists for good reason (e.g., different error handling in library code vs. application code).
- Variation across language boundaries in polyglot projects (a Rust backend and a TypeScript frontend will naturally have different patterns).
- Style differences that are purely aesthetic.

### Severity Guidance

- Inconsistent error handling in critical paths: high — likely to cause bugs.
- Inconsistent patterns that affect readability but not correctness: medium.
- Minor naming variations: low.

## 8. Dependency Hygiene

### Definition

Issues with the project's dependency graph — unused dependencies, outdated dependencies with known issues, or dependencies that could be removed by using built-in alternatives.

### What to Look For

- Dependencies listed in the manifest that are never imported or used.
- Dependencies that duplicate functionality available in the standard library or in another dependency already in the project.
- Dependencies with known security vulnerabilities (check if the dependency ecosystem provides audit tools).
- Dependencies pinned to very old versions when newer versions offer relevant improvements.
- Heavy dependencies pulled in for a single small function that could be trivially implemented.

### What NOT to Flag

- Dependencies that are used indirectly (e.g., pulled in as a transitive requirement by another dependency).
- Dependencies that are used in build scripts, procedural macros, or code generation even if they do not appear in runtime code.
- Version pins that exist for compatibility reasons documented in the project.

### Severity Guidance

- Dependencies with known security vulnerabilities: high.
- Completely unused dependencies: medium.
- Heavy dependencies for trivial use: medium.
- Outdated but functional dependencies: low.

## 9. Configuration Drift

### Definition

Values, thresholds, or settings buried in source code that logically belong in configuration — not because they change frequently today, but because they are the kind of value that will need tuning and are currently invisible to anyone who does not read that specific source file.

### What to Look For

- Magic numbers in business logic (e.g., `if score > 0.75` where 0.75 is a tuning threshold).
- Timeouts, retry counts, batch sizes, and buffer sizes hardcoded in implementation.
- File paths, URLs, or connection strings in source code.
- Feature toggles implemented as boolean constants in source files.
- Hardware-specific values (thread counts, memory limits) hardcoded rather than derived or configured.

### What NOT to Flag

- Constants that are genuinely constant and derived from the domain (e.g., number of degrees in a circle, protocol version numbers).
- Values that are already defined as named constants in a central location — the problem is solved even if they are not in a config file.
- Values in projects that intentionally avoid configuration files for simplicity (check project preferences in notes).

### Important

This category is distinct from Pattern Extraction. Configuration drift is about values that *will need tuning*. Pattern extraction is about values that *follow a computable formula*. A hardcoded threshold of 0.75 is configuration drift. An array of `[5, 15, 45, 135]` is pattern extraction.

### Severity Guidance

- Security-sensitive values (credentials, keys) in source: critical — but this skill does not handle security. Flag and recommend a security audit.
- Tuning parameters buried in logic: medium.
- Paths and URLs: medium if they vary by environment, low otherwise.

## 10. API Surface Bloat

### Definition

Public functions, methods, types, or modules that are only used internally and could have their visibility reduced. A smaller public API surface makes refactoring safer and the codebase easier to understand.

### What to Look For

- Public functions that are only called from within the same module or crate/package.
- Exported types that are only used internally.
- Public methods on structs/classes that are never called from outside the owning module.
- Entire modules that are marked public but only consumed by one sibling module.

### What NOT to Flag

- Items that are part of a library's public API contract.
- Items that are public for testing purposes (some languages require this).
- Items that are public because the language requires it for the module system to work (e.g., re-exports).
- Items in projects that are intentionally designed as libraries for external consumption.

### Severity Guidance

- Large modules with many unnecessarily public items: medium.
- Individual public functions that could be private: low.

## 11. Test Coverage Gaps

### Definition

Critical code paths that have zero or near-zero test coverage. This is not "write tests for everything" — it is specifically about identifying high-risk, high-importance code that is not tested at all.

### What to Look For

- Core business logic with no tests.
- Data transformation pipelines with no validation tests.
- Error handling paths that are never exercised.
- Integration points between systems with no integration tests.
- Algorithms that implement complex logic with no correctness tests.

### What NOT to Flag

- Code that is adequately tested by higher-level tests even if it lacks unit tests.
- Trivial getters, setters, or boilerplate.
- UI code where visual testing is more appropriate than unit testing.
- Code in rapid prototyping phases where testing is intentionally deferred.

### Severity Guidance

- Untested core business logic: high.
- Untested error handling in critical paths: high.
- Untested utility functions: low.

## 12. Documentation Rot

### Definition

Comments, docstrings, or inline documentation that describe behaviour the code no longer has. These are worse than no documentation — they actively mislead.

### What to Look For

- Comments describing a parameter that was renamed or removed.
- Docstrings explaining an algorithm that was replaced.
- TODO comments for work that was completed.
- Comments referencing files, modules, or functions that no longer exist.
- Module-level documentation that describes a different architecture than what is implemented.

### What NOT to Flag

- Missing documentation — the audit does not demand that all code be documented, only that existing documentation is accurate.
- Documentation that is slightly imprecise but not misleading.

### Severity Guidance

- Misleading module or function documentation in critical paths: high.
- Stale TODO comments: low.
- Minor inaccuracies in non-critical documentation: low.

## 13. Complexity Hotspots

### Definition

Functions, methods, or modules with unusually high complexity — deep nesting, long parameter lists, excessive branching, or tangled control flow. These are the places where bugs hide and where future changes are most likely to introduce regressions.

### What to Look For

- Functions with deeply nested conditionals (3+ levels).
- Functions with very high cyclomatic complexity.
- Functions with many parameters (typically 5+).
- God functions that orchestrate too many concerns.
- Control flow that is hard to trace due to early returns, exceptions, and goto-equivalents.
- Modules where understanding one function requires understanding many others.

### What NOT to Flag

- Inherently complex algorithms that are correctly implemented — sometimes the domain is complex and the code reflects that.
- Generated code or serialisation code that is verbose but mechanical.
- Pattern-matching or dispatch functions that are long but each case is simple and independent.

### Severity Guidance

- High-complexity functions in critical, frequently modified paths: high.
- Complex but stable, rarely modified functions: medium.
- Complex test setup code: low.

## 14. Known Issues and Active Risks

### Definition

Bugs, fragile code, race conditions, error-swallowing, and other correctness or reliability risks discovered during the audit. Unlike other categories, these may represent actual functional issues rather than cleanup opportunities.

### What to Look For

- Silent error swallowing (catching exceptions and doing nothing).
- Race conditions in concurrent code.
- Integer overflow risks in arithmetic code.
- Resource leaks that could cause failures under load.
- Assumptions about input that are not validated at system boundaries.
- Fragile code that depends on specific timing, ordering, or environmental conditions.
- Off-by-one errors or boundary condition issues.

### What NOT to Flag

- Known issues that are already documented in `context/systems/` files under "Known Issues / Active Risks."
- Issues that are acknowledged and intentionally deferred in project notes.

### Severity Guidance

- Correctness bugs in production code paths: critical.
- Race conditions or resource leaks: high.
- Missing input validation at system boundaries: medium.
- Minor edge case risks in non-critical code: low.

## Category Boundaries

When a finding could belong to multiple categories, use this priority order:

1. If it is a correctness issue → **Known Issues and Active Risks**
2. If it involves dead or unused code → **Dead Code Removal** or **Triage Needed**
3. If it involves an algorithm change → **Algorithm Optimisation**
4. If it involves a structural split → **Modularisation**
5. If it involves values that follow a formula → **Pattern Extraction**
6. If it involves values that need tuning → **Configuration Drift**
7. For all other performance issues → **Performance Improvement**
8. For cross-cutting consistency → **Inconsistent Patterns**

If a single code area has findings in multiple categories, file each finding separately in its correct category rather than trying to create a combined finding.
