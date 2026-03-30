# Evidence and Justification

This reference defines the proof chain every finding requires and how to assess whether a proposed change is truly "free."

## Table of Contents

1. The Proof Chain
2. Current State Documentation
3. Proposed Change Documentation
4. Justification Standards
5. Behavioural Impact Assessment
6. Confidence Levels
7. Research-Backed Findings

## 1. The Proof Chain

Every finding must include five components, in this order:

1. **Current state** — what the code does now, grounded in the actual implementation.
2. **Proposed change** — what should change and how.
3. **Justification** — why the change is an improvement, with evidence.
4. **Expected benefit** — what concrete improvement the change delivers.
5. **Behavioural impact assessment** — whether the change affects observable behaviour.

A finding without all five components is incomplete and should not be included in the audit output.

## 2. Current State Documentation

The current state must be grounded in the actual code, not in assumptions.

### What to Include

- **Location:** exact file path(s) and approximate line numbers or function names.
- **Description:** what the code currently does, in plain language.
- **Relevant context:** how this code fits into the larger system, what calls it, what it calls.
- **Observed behaviour:** what you verified by reading the code — not what you think it probably does.

### What to Avoid

- Vague descriptions ("the code is suboptimal").
- Assumptions about what the code does without reading it.
- Describing the general category of problem without grounding it in the specific code.

### Example

Good:
> `src/brain/training.rs:142-189` — The `select_experiences` function sorts the entire replay buffer (currently ~50,000 entries) using `.sort_by()` and then takes the first 64 entries. The sort is O(n log n) where only the top-k elements are needed.

Bad:
> The experience selection could probably be optimised.

## 3. Proposed Change Documentation

The proposed change must be specific enough that an engineer can implement it without needing to re-derive the solution.

### What to Include

- **What to change:** the specific modification, in plain language.
- **Where to change it:** exact files and functions affected.
- **How to change it:** enough detail to guide implementation without being pseudocode. The goal is clarity, not prescriptive line-by-line instructions.
- **What stays the same:** explicitly state which interfaces, inputs, and outputs are preserved.

### What to Avoid

- "Refactor this function" without saying how.
- Proposing a change that is more complex than the current code without justifying the complexity.
- Leaving ambiguity about what the function's callers will experience.

## 4. Justification Standards

The justification must explain *why* the change is an improvement, not just *what* it does.

### Levels of Justification

**Direct evidence (strongest):**
- The code demonstrably has no callers (dead code).
- The values demonstrably match a mathematical formula (pattern extraction).
- A profiler or benchmark shows the code is a bottleneck (performance).
- The same operation is demonstrably done differently in two places (inconsistency).

**Analytical evidence (strong):**
- Complexity analysis shows the current algorithm is suboptimal for the data size (algorithm optimisation).
- The code's cyclomatic complexity is measurably higher than necessary (complexity hotspot).
- The dependency is not imported anywhere in the codebase (dependency hygiene).

**Research-backed evidence (moderate):**
- Established research or authoritative sources confirm that an alternative approach is better for this specific use case. Must include the source and explain why it applies.

**Inference (weakest, but acceptable when disclosed):**
- Based on the code structure, this appears to be unused, but dynamic dispatch makes certainty impossible. Flagged for triage.
- The code likely allocates unnecessarily in this loop, but without profiling data, the actual impact is uncertain.

Always use the strongest available evidence. Fall back to weaker evidence only when stronger evidence is not obtainable.

### Justification Red Flags

These patterns indicate weak justification:

- "It would be cleaner" — clean is subjective. State the concrete improvement.
- "Best practices say..." — cite the specific practice and explain why it applies here.
- "This is a code smell" — name the concrete risk or cost.
- "Modern code would..." — the standard is whether the change is an improvement in this project, not whether it matches a hypothetical ideal.

## 5. Behavioural Impact Assessment

Every finding must include an assessment of whether the proposed change affects observable behaviour.

### Assessment Categories

**No impact (highest confidence):**
The change cannot affect behaviour by construction. Examples:
- Removing code that is provably never executed.
- Reducing visibility of a function that is only called internally.
- Removing an unused dependency.

**No impact (verified):**
The change does not affect behaviour based on analysis of the code. Examples:
- Replacing an algorithm that produces identical output for all possible inputs.
- Extracting a hardcoded array that exactly matches a formula's output.
- Pre-allocating a buffer instead of growing it dynamically.

**Negligible impact (flagged):**
The change may have a trivial, practically insignificant effect on behaviour. Examples:
- Floating-point rounding may differ by epsilon.
- Ordering of elements in an unordered collection may change.
- Timing characteristics may change in concurrent code.

These must be explicitly flagged. The implementing engineer can decide whether the impact is acceptable.

**Possible impact (requires decision):**
The change may affect behaviour in ways that require human judgment. Examples:
- Removing code that has side effects (logging, metrics).
- Changing an algorithm that may produce different results for edge-case inputs.
- Modifying error handling that currently silently swallows errors.

These should be clearly marked as "not free — requires decision" and must not be presented as safe cleanup.

### Proving Zero Impact

To claim "no impact," you must demonstrate one of:

- **Dead path proof:** the code is never reached (no callers, unreachable branch, disabled feature flag).
- **Equivalence proof:** the new code produces identical output for all inputs the system generates. This requires understanding the input domain, not just the algorithm.
- **Isolation proof:** the change is contained within a boundary that does not affect external interfaces (e.g., reducing visibility, removing unused imports).

## 6. Confidence Levels

When the evidence is not definitive, state your confidence level:

- **High confidence:** based on direct evidence. "This function has zero callers in the codebase."
- **Moderate confidence:** based on strong analysis. "This algorithm is O(n^2) and the dataset is typically 10,000 items, making this a meaningful bottleneck."
- **Low confidence:** based on inference. "This code appears unused, but it may be invoked via the plugin system. Flagged for triage."

Low-confidence findings should be categorised as "Triage Needed" rather than given definitive recommendations.

## 7. Research-Backed Findings

When a finding is supported by external research:

- **Cite the source:** what research, documentation, or authoritative reference supports this recommendation.
- **Explain applicability:** why the research applies to this specific implementation, not just to the general case.
- **Ground it:** show the connection between the research finding and the actual code in the project.
- **Acknowledge limits:** if the research was conducted on different conditions (different hardware, different data sizes, different language), note those differences.

A research finding that says "KD-trees are faster for nearest-neighbour search" is not sufficient. The finding must say "KD-trees are faster for nearest-neighbour search in 2D continuous space with ~1,000 points, which matches our spatial query in `src/environment/proximity.rs:89`. The current linear scan is O(n) per query with n=1,024; a KD-tree would give O(log n) queries after an O(n log n) build step. Since the point set changes infrequently, the build cost is amortised."
