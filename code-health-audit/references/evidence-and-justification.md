# Evidence and Justification

This reference defines the proof chain every finding requires and how to assess whether a proposed change is truly "free."

## Table of Contents

1. The Proof Chain
2. Current State Documentation
3. Proposed Change Documentation
4. Justification Standards
5. Confidence Upgrade Pathway
6. Behavioural Impact Assessment
7. Confidence Levels
8. Research-Backed Findings

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

**Direct evidence from a test the audit wrote (strongest):**
- An equivalence test the audit wrote shows two implementations produce identical output across the input space (algorithm replacement, dead code removal of duplicates).
- A benchmark the audit wrote shows implementation B is measurably faster than implementation A on the project's actual data (performance, algorithm optimisation, data layout).
- A coverage probe the audit wrote shows the code path is never reached, even via reflection or dynamic dispatch (dead code).
- A baseline test the audit wrote pins the current observable behaviour, making the proposed refactor safe to verify against (modularisation, refactoring).
- A failing test the audit wrote reveals an actual bug (known issues — promote immediately).

This is the strongest evidence type because the audit gathered it itself, against the project's actual code, using a test that lives in the project's test suite and can be re-run by anyone.

**Direct evidence from existing artefacts (strong):**
- The code demonstrably has no callers (dead code).
- The values demonstrably match a mathematical formula (pattern extraction).
- An existing profiler or benchmark shows the code is a bottleneck (performance).
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

Always use the strongest available evidence. The audit's first move when a finding sits at "moderate" or "weak" should be to ask: would a diagnostic test push it to "strong" or "strongest"? If yes, write the test (see detection-strategies §7). The whole point of the diagnostic test phase is to upgrade evidence quality before issuing findings.

Fall back to weaker evidence only when stronger evidence is not obtainable, when the cost of writing the test would exceed the value of the finding, or when the finding's confidence already meets the bar without it.

### Justification Red Flags

These patterns indicate weak justification:

- "It would be cleaner" — clean is subjective. State the concrete improvement.
- "Best practices say..." — cite the specific practice and explain why it applies here.
- "This is a code smell" — name the concrete risk or cost.
- "Modern code would..." — the standard is whether the change is an improvement in this project, not whether it matches a hypothetical ideal.

## 5. Confidence Upgrade Pathway

Before issuing a finding at moderate or low confidence, ask:

1. "Would a diagnostic test upgrade this to high confidence?"
2. "Would additional research or code reading resolve the uncertainty?"

If the answer to either is yes, attempt the upgrade *before* issuing the finding, not after. Low and moderate confidence findings are not acceptable output unless you have already attempted the upgrade and failed — or the upgrade cost genuinely exceeds the finding's value and you have recorded that trade-off as a reasoned omission in the Obligation Evidence Map.

The failure mode this section exists to prevent: issuing a lukewarm finding ("this *might* be O(n^2); unclear if it matters") when a 20-line benchmark or a 5-minute follow-up read would have produced a confident finding or ruled it out. Confidence is not a dial the audit gets to set by fiat — it is earned by the evidence, and the audit's job when confidence is low is to try to raise it.

### Worked examples

**Example 1 — Algorithmic complexity case.** A reading pass surfaces a nested loop in a query handler. The outer loop iterates over request items; the inner loop iterates over a lookup array. At a glance this is O(n·m). The uncertainty: is the lookup array small enough in practice that the nested loop never becomes a bottleneck, or is it growing with tenant count?

Wrong: issue the finding at moderate confidence with "this *may* be a bottleneck depending on array size."

Right: before issuing, either (a) write a quick benchmark that runs the handler against realistic tenant-size distributions captured from the project's data, or (b) read the code that populates the lookup array to determine its growth curve. Either pushes the finding to high confidence. The finding is then issued as "confirmed O(n·m) with m growing linearly in tenant count, reaching ~4,000 at current scale; benchmark at `tests/query_handler_bench.rs` shows 180ms per request at 4k tenants" — or it is withdrawn.

**Example 2 — Dead-code-via-reflection case.** A module appears unused. Grep finds no direct callers. But the project uses a plugin loader that instantiates modules by name at runtime from a config file.

Wrong: issue a "Triage Needed" finding at low confidence saying "appears dead but the plugin system makes this unclear."

Right: before issuing, write a coverage probe — a test that exercises the plugin loader with the full set of plugin names from the project's config and asserts whether this module's entry point is ever called. If the probe shows zero invocations, the finding moves to high confidence as a Dead Code finding with the probe attached. If the probe shows the module is invoked by a plugin name, the finding is withdrawn. "Triage Needed" is a last-resort category when the upgrade was genuinely attempted and failed — not a comfortable default.

## 6. Behavioural Impact Assessment

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

## 7. Confidence Levels

When the evidence is not definitive, state your confidence level:

- **High confidence:** based on direct evidence. "This function has zero callers in the codebase."
- **Moderate confidence:** based on strong analysis. "This algorithm is O(n^2) and the dataset is typically 10,000 items, making this a meaningful bottleneck."
- **Low confidence:** based on inference. "This code appears unused, but it may be invoked via the plugin system. Flagged for triage."

Low-confidence findings should be categorised as "Triage Needed" rather than given definitive recommendations.

## 8. Research-Backed Findings

When a finding is supported by external research:

- **Cite the source:** what research, documentation, or authoritative reference supports this recommendation.
- **Explain applicability:** why the research applies to this specific implementation, not just to the general case.
- **Ground it:** show the connection between the research finding and the actual code in the project.
- **Acknowledge limits:** if the research was conducted on different conditions (different hardware, different data sizes, different language), note those differences.

A research finding that says "KD-trees are faster for nearest-neighbour search" is not sufficient. The finding must say "KD-trees are faster for nearest-neighbour search in 2D continuous space with ~1,000 points, which matches our spatial query in `src/environment/proximity.rs:89`. The current linear scan is O(n) per query with n=1,024; a KD-tree would give O(log n) queries after an O(n log n) build step. Since the point set changes infrequently, the build cost is amortised."
