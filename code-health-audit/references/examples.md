# Examples

This reference contains worked examples of good audit findings across different categories and stacks, plus a rejected finding that illustrates when a proposed change fails the inviolable rules.

## Table of Contents

1. Example 1: Algorithm Optimisation (Rust, ML Training)
2. Example 2: Dead Code Removal (TypeScript, Web Application)
3. Example 3: Pattern Extraction (Python, Simulation)
4. Example 4: Performance Improvement (Go, Backend Service)
5. Example 5: Rejected Finding — Algorithm Change That Alters Behaviour

---

## 1. Example 1: Algorithm Optimisation (Rust, ML Training)

> This example shows a research-backed finding with thorough justification and a clear impact assessment.

### Replace Linear Experience Selection with Partial Sort
- [ ] Replace full sort + truncate in `select_experiences()` with `select_nth_unstable_by()` for O(n) average selection

**Category:** Algorithm Optimisation
**Severity:** High
**Effort:** Small
**Behavioural Impact:** None (verified — selection criteria and selected set are identical)

**Location:**
- `src/brain/a2c/buffer.rs:142-167` — `select_experiences()`

**Current State:**
The `select_experiences` function selects the top-k experiences from a replay buffer of ~50,000 entries by priority score. It currently:
1. Clones the priority scores into a new vector.
2. Sorts the entire vector with `.sort_by()` (O(n log n)).
3. Takes the first 64 entries.

The function is called once per training step, which occurs ~200 times per episode. The sort dominates the function's runtime.

**Proposed Change:**
Replace the full sort with Rust's `select_nth_unstable_by()`, which performs a partial sort in O(n) average time. This selects the k-th element and partitions the array such that all elements before position k are less than or equal to it. Then take the first k elements and sort only those (O(k log k) for k=64 is negligible).

The function signature, input, output type, and selected set remain identical. The only change is the internal algorithm used to find the top-k elements.

**Justification:**
The current approach is O(n log n) where n=50,000 to select k=64 elements. The proposed approach is O(n) average for the selection plus O(k log k) for ordering the selected elements. For n=50,000 and k=64:
- Current: ~50,000 × 17 ≈ 850,000 comparisons
- Proposed: ~50,000 + 64 × 6 ≈ 50,384 comparisons

This is a ~17x reduction in comparisons. Rust's standard library provides `select_nth_unstable_by()` specifically for this use case, so no external dependency is needed.

**Expected Benefit:**
Approximately 17x fewer comparisons in the experience selection hot path, called ~200 times per episode. Reduces per-episode overhead by a meaningful constant factor with no change to the training algorithm.

**Impact Assessment:**
Zero functional change. The same 64 experiences are selected by the same priority criteria. The internal ordering of the selected set may differ from the previous implementation, but the training loop processes them as a batch where order does not matter (verified: `update_network()` at `buffer.rs:180` iterates the batch with `.iter()` and accumulates gradients without order dependence). The unstable partitioning means equal-priority elements may be selected differently than before, but since priorities are floating-point values computed from TD-error, exact ties are vanishingly unlikely.

---

## 2. Example 2: Dead Code Removal (TypeScript, Web Application)

> This example shows a straightforward dead code finding with clear proof of no callers.

### Remove Legacy Payment Processor Adapter
- [ ] Delete `src/payments/adapters/stripe-v1.ts` and remove its export from `src/payments/adapters/index.ts`

**Category:** Dead Code Removal
**Severity:** High
**Effort:** Trivial
**Behavioural Impact:** None (verified — zero callers, zero imports)

**Location:**
- `src/payments/adapters/stripe-v1.ts` — entire file (187 lines)
- `src/payments/adapters/index.ts:3` — re-export line

**Current State:**
The file `stripe-v1.ts` implements an adapter for Stripe's v1 API. The project migrated to Stripe v2 (implemented in `stripe-v2.ts`, which is actively used). The v1 adapter:
- is exported from `adapters/index.ts` but never imported by any other file in the project,
- references API endpoints that Stripe deprecated in 2024,
- uses a `StripeV1Config` type that is defined inline and used nowhere else.

Verified by searching the entire codebase for:
- `stripe-v1` — only appears in the file itself and the re-export line,
- `StripeV1Adapter` — only appears in the file itself and the re-export line,
- `StripeV1Config` — only appears in the file itself.

**Proposed Change:**
Delete `stripe-v1.ts` entirely. Remove the re-export line from `adapters/index.ts`. No other files need to change.

**Justification:**
The file is dead code — it has no callers, references a deprecated API, and was replaced by `stripe-v2.ts`. Its continued presence:
- adds 187 lines of unmaintained code to the codebase,
- creates confusion about which Stripe adapter is active,
- may mislead a future engineer into thinking v1 is a viable fallback.

**Expected Benefit:**
Removes 187 lines of dead code. Eliminates confusion about active vs. legacy payment adapters. Reduces the surface area of the payments module.

**Impact Assessment:**
Zero functional change by construction. The file has zero callers. Removing it cannot affect any code path. The re-export removal also has zero impact since the export is not consumed by any importer.

---

## 3. Example 3: Pattern Extraction (Python, Simulation)

> This example shows a pattern extraction with careful verification that the values match the formula.

### Replace Hardcoded Sensor Distances with Geometric Progression
- [ ] Replace the 12-element `SENSOR_DISTANCES` array with a generated geometric sequence

**Category:** Pattern Extraction
**Severity:** Medium
**Effort:** Small
**Behavioural Impact:** None (verified — generated values exactly match hardcoded values)

**Location:**
- `src/sensors/lidar.py:23-36` — `SENSOR_DISTANCES` constant

**Current State:**
The file defines a hardcoded array of 12 sensor distances used for the LiDAR simulation:

```python
SENSOR_DISTANCES = [2.0, 3.4, 5.78, 9.826, 16.7042, 28.39714, 48.275138, 82.067735, 139.515149, 237.175754, 403.198781, 685.437928]
```

These values are used in `cast_rays()` at line 52 to determine the distance thresholds for each LiDAR ring. The values follow a geometric progression with ratio 1.7: each value is the previous value multiplied by 1.7 (with the first value being 2.0).

Verification:
- 2.0 × 1.7 = 3.4 ✓
- 3.4 × 1.7 = 5.78 ✓
- 5.78 × 1.7 = 9.826 ✓
- 9.826 × 1.7 = 16.7042 ✓
- (all 12 values verified to match within floating-point precision)

**Proposed Change:**
Replace the hardcoded array with a generated sequence:

```python
SENSOR_DISTANCES = [2.0 * (1.7 ** i) for i in range(12)]
```

This produces values identical to the hardcoded array (verified: maximum difference is <1e-10 due to floating-point representation, and the values are used as distance thresholds where such precision is irrelevant).

Alternatively, if the team prefers to keep the number of sensors and the progression ratio configurable:

```python
SENSOR_BASE = 2.0
SENSOR_RATIO = 1.7
SENSOR_COUNT = 12
SENSOR_DISTANCES = [SENSOR_BASE * (SENSOR_RATIO ** i) for i in range(SENSOR_COUNT)]
```

**Justification:**
The hardcoded array obscures the underlying pattern. A generated sequence:
- makes the geometric progression explicit and discoverable,
- makes changes to the sensor configuration straightforward (change the base, ratio, or count),
- eliminates the risk of transcription errors if the values ever need updating.

**Expected Benefit:**
Replaces 12 opaque hardcoded values with a formula that communicates the design intent. Enables future configuration changes without manual recalculation.

**Impact Assessment:**
Zero functional change (verified). The generated values match the hardcoded values to within floating-point precision (<1e-10). The values are used as distance thresholds in ray casting where precision beyond ~0.001 is irrelevant. The order of values is preserved (ascending, same as the generated sequence).

---

## 4. Example 4: Performance Improvement (Go, Backend Service)

> This example shows a performance finding based on understanding the hot path.

### Pre-allocate Response Slice in Batch Handler
- [ ] Pre-allocate the `results` slice with `make([]Result, 0, len(requests))` instead of `var results []Result`

**Category:** Performance Improvement
**Severity:** Medium
**Effort:** Trivial
**Behavioural Impact:** None (verified — same output, different allocation pattern)

**Location:**
- `internal/handlers/batch.go:89` — `processBatch()`

**Current State:**
The `processBatch` function processes a batch of requests and collects results:

```go
var results []Result
for _, req := range requests {
    result := process(req)
    results = append(results, result)
}
```

The `results` slice starts with zero capacity. As results are appended, Go's runtime reallocates the backing array when capacity is exceeded — typically doubling each time. For a batch of 100 requests, this causes approximately 7 allocations and copies (1→2→4→8→16→32→64→128).

This function is called for every incoming batch request. Batch sizes are typically 50-200 items (based on the request validation at line 78 which caps batch size at 500).

**Proposed Change:**
Pre-allocate the slice with the known capacity:

```go
results := make([]Result, 0, len(requests))
for _, req := range requests {
    result := process(req)
    results = append(results, result)
}
```

**Justification:**
The batch size is known before the loop begins (`len(requests)`). Pre-allocating avoids all intermediate reallocations and copies. For a typical batch of 100 items, this eliminates ~7 allocations and ~200 element copies.

**Expected Benefit:**
Eliminates unnecessary heap allocations and memory copies in the batch processing hot path. For 100-item batches: from ~7 allocations to 1, and from ~200 element copies to 0. Reduces GC pressure proportionally.

**Impact Assessment:**
Zero functional change by construction. The output slice contains the same elements in the same order. Only the internal allocation strategy differs. The function signature, return type, and observable behaviour are identical.

---

## 5. Example 5: Rejected Finding — Algorithm Change That Alters Behaviour

> This example shows a finding that was investigated, appeared to be a good optimisation, but was ultimately rejected because it would change application behaviour.

### REJECTED: Replace HashMap with BTreeMap for Deterministic Agent Ordering

**Category:** Would have been Algorithm Optimisation
**Status:** Rejected — violates Zero Functional Change rule

**Location:**
- `src/environment/agents.rs:45` — `AgentRegistry` struct

**Investigation:**
The `AgentRegistry` uses a `HashMap<AgentId, Agent>` to store active agents. During the update loop (`update_all()` at line 78), it iterates over all agents:

```rust
for (id, agent) in &self.agents {
    agent.update(dt);
}
```

Initial assessment suggested replacing `HashMap` with `BTreeMap` because:
- BTreeMap iteration is ordered, which could improve cache locality.
- The registry is iterated far more often than modified (updates every frame, agents added/removed rarely).
- BTreeMap has better cache performance for ordered iteration of moderate-sized collections.

**Why It Was Rejected:**

Investigation of the downstream effects revealed that agent update order matters. The `agent.update(dt)` call modifies shared environment state (physics, collision detection) that subsequent agents observe. With HashMap, the iteration order is arbitrary but deterministic for a given Rust version and run. Changing to BTreeMap would change the iteration order to sorted-by-ID, which would:

1. Change the physics simulation results (agents collide in different order).
2. Break deterministic replay (saved replays encode the HashMap iteration order implicitly).
3. Alter training behaviour (the RL agent trains on trajectories that depend on update order).

Even though the performance benefit is real, the change is not "free" — it would alter the application's behaviour in ways that affect training reproducibility. This belongs in a feature discussion, not in a code health audit.

**Lesson:**
Always trace the full impact chain. An iteration order change in a data structure can cascade through physics, replay, and training systems. What looks like an internal implementation detail may be load-bearing for functional correctness.
