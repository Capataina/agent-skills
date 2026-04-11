# Examples

This reference contains worked examples of good audit findings across different categories and stacks, plus a rejected finding that illustrates when a proposed change fails the inviolable rules.

The examples are deliberately drawn from different domains so the agent does not anchor on any single project type. Treat them as illustrations of the *shape* and *depth* a good finding should have, not as templates to copy. The principles transfer; the surface details should change with the project.

## Table of Contents

1. Example 1: Algorithm Optimisation (Backend Service, Partial Sort)
2. Example 2: Dead Code Removal (Web Application, Legacy Adapter)
3. Example 3: Pattern Extraction (Simulation, Geometric Sequence)
4. Example 4: Performance Improvement (Backend Service, Pre-allocation)
5. Example 5: Data Layout and Memory Access Patterns (Streaming Pipeline, Buffer Flattening)
6. Example 6: Rejected Finding — Algorithm Change That Alters Behaviour

---

## 1. Example 1: Algorithm Optimisation (Backend Service, Partial Sort)

> This example shows an algorithm-level finding with a clear complexity argument and a thorough impact assessment.

### Replace Full Sort With Partial Selection in Top-K Query
- [ ] Replace the full sort plus truncation in `select_top_results()` with a partial selection algorithm for O(n) average selection

**Category:** Algorithm Optimisation
**Severity:** High
**Effort:** Small
**Behavioural Impact:** None (verified — selection criteria and selected set are identical, internal ordering does not affect downstream consumers)

**Location:**
- `src/query/results.rs:142-167` — `select_top_results()`

**Current State:**
The `select_top_results` function selects the top-k results from a candidate list of approximately fifty thousand entries by relevance score. It currently:
1. Clones the score values into a new vector.
2. Sorts the entire vector with `.sort_by()` (O(n log n)).
3. Takes the first sixty-four entries.

The function is called once per incoming query, which the service handles at sustained rates of hundreds per second under load. The sort dominates the function's runtime according to the existing benchmarks in `benches/query.rs`.

**Proposed Change:**
Replace the full sort with the standard library's partial selection routine, which performs a linear-time partition that places the k-th element in its final sorted position and partitions the rest such that all earlier elements are less than or equal to it. Then take the first k elements and sort only those (O(k log k) for k=64 is negligible).

The function signature, input, output type, and selected set remain identical. The only change is the internal algorithm used to find the top-k elements.

**Justification:**
The current approach is O(n log n) where n is approximately fifty thousand, to select k=64 elements. The proposed approach is O(n) average for the selection plus O(k log k) for ordering the selected elements. The constant-factor improvement is roughly an order of magnitude in comparison count, and the standard library provides this routine specifically for this use case so no external dependency is needed.

**Expected Benefit:**
Approximately an order of magnitude fewer comparisons in the top-k selection hot path, which the existing benchmarks identify as a meaningful share of per-query latency. Reduces sustained CPU cost on the query handler proportionally.

**Impact Assessment:**
Zero functional change. The same sixty-four results are selected by the same relevance criteria. The internal ordering of the selected set may differ from the previous implementation, but the response builder processes them as a batch and applies its own ranking pass before returning to the client (verified: `format_response()` at `results.rs:180` re-sorts by relevance before serialisation). The unstable partitioning means equal-score elements may be selected differently than before, but since scores are floating-point values computed from weighted feature vectors, exact ties are vanishingly unlikely and would be broken arbitrarily even under the current implementation.

---

## 2. Example 2: Dead Code Removal (Web Application, Legacy Adapter)

> This example shows a straightforward dead code finding with clear proof of no callers.

### Remove Legacy Payment Processor Adapter
- [ ] Delete `src/payments/adapters/processor-v1.ts` and remove its export from `src/payments/adapters/index.ts`

**Category:** Dead Code Removal
**Severity:** High
**Effort:** Trivial
**Behavioural Impact:** None (verified — zero callers, zero imports)

**Location:**
- `src/payments/adapters/processor-v1.ts` — entire file (187 lines)
- `src/payments/adapters/index.ts:3` — re-export line

**Current State:**
The file `processor-v1.ts` implements an adapter for the v1 API of the project's external payment processor. The project migrated to v2 (implemented in `processor-v2.ts`, which is actively used). The v1 adapter:
- is exported from `adapters/index.ts` but never imported by any other file in the project,
- references API endpoints that the upstream provider deprecated last year,
- uses a `ProcessorV1Config` type that is defined inline and used nowhere else.

Verified by searching the entire codebase for:
- `processor-v1` — only appears in the file itself and the re-export line,
- `ProcessorV1Adapter` — only appears in the file itself and the re-export line,
- `ProcessorV1Config` — only appears in the file itself.

**Proposed Change:**
Delete `processor-v1.ts` entirely. Remove the re-export line from `adapters/index.ts`. No other files need to change.

**Justification:**
The file is dead code — it has no callers, references a deprecated upstream API, and was replaced by `processor-v2.ts`. Its continued presence:
- adds unmaintained code to the codebase,
- creates confusion about which adapter is active,
- may mislead a future engineer into thinking v1 is a viable fallback.

**Expected Benefit:**
Removes the dead file and its export. Eliminates confusion about active versus legacy adapters. Reduces the surface area of the payments module.

**Impact Assessment:**
Zero functional change by construction. The file has zero callers. Removing it cannot affect any code path. The re-export removal also has zero impact since the export is not consumed by any importer.

---

## 3. Example 3: Pattern Extraction (Simulation, Geometric Sequence)

> This example shows a pattern extraction with careful verification that the values match the formula.

### Replace Hardcoded Sensor Distances With Geometric Progression
- [ ] Replace the twelve-element `SENSOR_DISTANCES` array with a generated geometric sequence

**Category:** Pattern Extraction
**Severity:** Medium
**Effort:** Small
**Behavioural Impact:** None (verified — generated values exactly match hardcoded values)

**Location:**
- `src/sensors/lidar.py:23-36` — `SENSOR_DISTANCES` constant

**Current State:**
The file defines a hardcoded array of twelve sensor distances used for the lidar simulation. The values follow a geometric progression: each value is the previous value multiplied by a constant ratio, starting from a small base value.

Verification of the progression: every adjacent pair of values matches the multiplication exactly within floating-point precision, confirming the values are mechanically derived from a single base and ratio.

**Proposed Change:**
Replace the hardcoded array with a generated sequence using a list comprehension that produces values from the base and ratio. This produces values identical to the hardcoded array within floating-point representation, and the values are used as distance thresholds where such precision is irrelevant.

Alternatively, if the team prefers to keep the count and the progression ratio configurable, expose them as named constants and generate the array from the constants.

**Justification:**
The hardcoded array obscures the underlying pattern. A generated sequence:
- makes the geometric progression explicit and discoverable,
- makes changes to the sensor configuration straightforward (change the base, ratio, or count),
- eliminates the risk of transcription errors if the values ever need updating.

**Expected Benefit:**
Replaces twelve opaque hardcoded values with a formula that communicates the design intent. Enables future configuration changes without manual recalculation.

**Impact Assessment:**
Zero functional change (verified). The generated values match the hardcoded values within floating-point precision. The values are used as distance thresholds in ray casting where precision beyond the noise floor of the sensor is irrelevant. The order of values is preserved.

---

## 4. Example 4: Performance Improvement (Backend Service, Pre-allocation)

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
The `processBatch` function processes a batch of requests and collects results into a slice that starts with zero capacity. As results are appended, the runtime reallocates the backing array when capacity is exceeded — typically doubling each time. For a batch of one hundred requests this causes several intermediate allocations and copies.

This function is called for every incoming batch request. Batch sizes are typically fifty to two hundred items based on the request validation cap.

**Proposed Change:**
Pre-allocate the slice with the known capacity from the request count. The append loop is unchanged.

**Justification:**
The batch size is known before the loop begins. Pre-allocating avoids all intermediate reallocations and copies. The standard library provides the pre-allocation idiom directly so no helper or new dependency is needed.

**Expected Benefit:**
Eliminates unnecessary heap allocations and memory copies in the batch processing hot path. Reduces garbage collector pressure proportionally.

**Impact Assessment:**
Zero functional change by construction. The output slice contains the same elements in the same order. Only the internal allocation strategy differs. The function signature, return type, and observable behaviour are identical.

---

## 5. Example 5: Data Layout and Memory Access Patterns (Streaming Pipeline, Buffer Flattening)

> This example shows a data layout finding — the algorithm and the output are unchanged, but the underlying memory access pattern is reshaped for a substantial speedup. This is the kind of finding that surface-level analysis tends to miss and that careful reading of hot paths surfaces.

### Flatten Per-Frame Allocation Into Reused Contiguous Buffer
- [ ] Replace per-frame `Vec<u8>` allocation in `assemble_frame()` with a single owned `FrameBuffer` whose capacity is reused across frames

**Category:** Data Layout and Memory Access Patterns
**Severity:** High
**Effort:** Small
**Behavioural Impact:** None (verified — produces byte-identical output)

**Location:**
- `src/streaming/assembly.rs:88-130` — `assemble_frame()`
- `src/streaming/buffer.rs:14-22` — `FrameBuffer` struct (to be added)
- `src/streaming/pipeline.rs:45-78` — call sites that consume the assembled output

**Current State:**
The `assemble_frame()` function processes incoming streaming chunks and constructs a complete frame. For each frame it currently:
1. Allocates a fresh `Vec<u8>` for the assembled output.
2. Copies each chunk's payload through several intermediate vectors before reaching the assembly buffer.
3. Returns the vector by value to the downstream consumer.

The function runs at the project's target throughput rate, so the allocation pattern in steady state is: many fresh allocations per second on the assembly path, each requiring the allocator to walk free lists and potentially fault new pages, with the assembled vector dropped at the end of each frame and returning memory that the next frame immediately re-requests. The chunk payloads themselves are also copied through several intermediate vectors before reaching the assembly buffer.

Reading the hot path carefully reveals two compounding problems. First, the allocator is engaged on every frame even though the working set is bounded — the system asks for and releases the same amount of memory repeatedly. Second, the fresh allocations land on cold pages each time, so the cache and TLB never warm up across frames; the assembly loop spends a meaningful share of its time waiting for cache lines that the previous frame's loop had already pulled in but that have since been evicted because the allocation moved.

The benchmark fixtures in `benches/streaming.rs` show that under sustained load this pattern accounts for a substantial share of the assembly stage's runtime — far more than the actual byte-copying logic.

**Proposed Change:**
Add a single `FrameBuffer` instance owned by the assembly stage. On each frame:
1. Clear the buffer's logical length without freeing its capacity.
2. Reserve enough space upfront based on the known total chunk size for this frame.
3. Append chunk payloads directly into the buffer without intermediate vectors.
4. Hand the buffer's slice to the downstream consumer (which already takes a `&[u8]`).

The buffer keeps its capacity across frames, so after the warm-up period the allocator is no longer involved in normal operation. Only the case where a frame is unusually large requires growth, and the buffer's high-water-mark capacity reflects the recent maximum.

The function signature changes from `fn assemble_frame() -> Vec<u8>` to `fn assemble_frame(buf: &mut FrameBuffer)`, with the consumer reading from the buffer's slice. The downstream consumer already accepts a slice, so its observable behaviour does not change.

**Justification:**
The current allocation pattern fights the allocator on every frame for memory the system has just released. A single owned buffer eliminates the per-frame allocation cost entirely. Beyond raw allocation cost, the contiguous reuse improves cache locality — the buffer's pages stay hot in the CPU caches and TLB across frames, where fresh allocations land on cold pages. This is the same pattern used by every high-performance streaming pipeline (audio rings, video bitstream buffers, network packet pools), and it is well-documented in the engineering literature for low-latency data assembly.

The approach was researched in the context of similar streaming pipelines. The consistent finding across implementations is that reusing a single contiguous buffer for assembly delivers both an allocation-cost reduction (the dominant first-order effect) and a cache-locality reduction (the second-order effect that compounds when downstream stages also walk the buffer). For a system that runs at the project's target throughput, both effects matter.

Verified on the existing test suite: byte-for-byte output matches the previous implementation on every fixture. Verified on the assembly path's invariants: the consumer reads the slice synchronously inside `assemble_frame()`'s call site, so the buffer is never aliased across frames.

**Expected Benefit:**
Eliminates the per-frame allocation in the assembly hot path entirely after the warm-up period. The benchmarks in `benches/streaming.rs` indicate this is a substantial share of current runtime — exact speedup depends on the frame profile, but the order-of-magnitude reduction in allocator engagement should propagate to a meaningful end-to-end latency improvement on the streaming pipeline. Reduces allocator pressure across the rest of the process by removing one of the dominant short-lived allocators in the system.

**Impact Assessment:**
Zero functional change (verified). The output bytes are identical, the chunk processing order is identical, and the consumer's view of the data is identical. The buffer ownership change is internal to the assembly module — no caller observes a behavioural difference. Floating-point operations are not involved. Iteration order is preserved by construction.

The only edge case considered is concurrent access: the buffer is owned by a single assembly stage that runs sequentially on its own thread, and the consumer reads synchronously inside the same call. There is no aliasing risk. Verified by reading the call sites in `src/streaming/pipeline.rs:45-78`. If a future change made the consumer asynchronous, the ownership pattern would need revisiting — a brief comment in the buffer module should record this assumption so the constraint is not lost.

---

## 6. Example 6: Rejected Finding — Algorithm Change That Alters Behaviour

> This example shows a finding that was investigated, looked promising, but was ultimately rejected because it would change application behaviour. The lesson is about tracing the impact chain — not about avoiding data structure changes generally.

### REJECTED: Replace HashMap With BTreeMap for Deterministic Iteration

**Category:** Would have been Algorithm Optimisation
**Status:** Rejected — violates Zero Functional Change rule

**Location:**
- `src/scheduler/jobs.rs:45` — `JobRegistry` struct

**Investigation:**
The `JobRegistry` uses a `HashMap<JobId, Job>` to store scheduled jobs. During the dispatch loop (`dispatch_all()` at line 78), it iterates over all jobs:

```rust
for (id, job) in &self.jobs {
    job.run(ctx);
}
```

Initial assessment suggested replacing `HashMap` with `BTreeMap` because:
- BTreeMap iteration is ordered, which could improve cache locality for ordered access.
- The registry is iterated far more often than modified.
- BTreeMap has better cache performance than HashMap for ordered iteration of moderate-sized collections in some workloads.

**Why It Was Rejected:**

Investigation of the downstream effects revealed that job dispatch order matters. The `job.run(ctx)` call modifies shared scheduler state (queue ordering, retry timestamps, dependency tracking) that subsequent jobs observe. With HashMap, the iteration order is arbitrary but deterministic for a given run within a single Rust version. Changing to BTreeMap would change the iteration order to sorted-by-id, which would:

1. Change the order of state mutations across jobs, producing observably different schedule outputs.
2. Break replay-based testing — the test suite encodes the HashMap iteration order implicitly via golden-file comparisons.
3. Alter the dispatcher's empirical fairness properties, which the team has tuned around the current order.

Even though the cache-locality argument is real, the change is not free — it would alter the application's behaviour in ways that affect tests, scheduling output, and operational tuning. This belongs in a feature discussion, not in a code health audit.

**Lesson:**

The lesson is **not** "avoid data structure changes." Many data structure changes are perfectly safe and produce the kind of high-leverage wins that a code health audit should surface — see Example 5 for a layout change that delivers a substantial speedup without changing observable behaviour. The category is one of the highest-value sources of findings in the audit.

The lesson is "trace the full impact chain before claiming a change is free." A data structure change that looks internal can turn out to be load-bearing for ordering, replay, fairness, hashing, or some other property the rest of the system implicitly depends on. Always check the downstream consumers; if you can verify the change preserves every observable property the consumers depend on, the finding is still strong. If you cannot, the change either gets dropped or gets flagged as "not free — requires decision" so the implementing engineer can weigh the trade-off explicitly.

The discrimination is whether the impact chain has been fully traced and the change has been proven safe — not whether the category of change is "data structures."
