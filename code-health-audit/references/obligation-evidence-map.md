# Obligation Evidence Map

This reference defines the Obligation Evidence Map — a live artefact that records, as the audit runs, the evidence proving each non-negotiable obligation was met for each system audited.

## Table of Contents

1. What the Map Is
2. File Location
3. Required Rows
4. Required Columns
5. When to Update
6. Example Rows

## 1. What the Map Is

The Obligation Evidence Map is a live, running artefact produced *as the audit executes*, not a summary written at the end. Each row is appended the moment its corresponding system's Pass 2 work completes. Treating the map as an after-the-fact writeup defeats its purpose — the map exists to catch silent omission of WebSearch calls and diagnostic test writing before the final output is drafted, not to describe what happened after the fact.

The map is the ground truth for the "What I Did Not Do" section of the final output. Every obligation in the final report must be traceable to a row (or a reasoned omission) in this map.

## 2. File Location

```
context/plans/code-health-audit/obligation-evidence-map.md
```

Create the file at the start of the audit (during CHA-5's front-loaded WebSearch, if not earlier). If it does not yet exist when the front-loaded search runs, create it then and record the initial search.

## 3. Required Rows

One row per system audited in Pass 2. Additionally, a row for the front-loaded pre-Pass-1 WebSearch (see SKILL.md "Before Anything Else"). Systems consciously skipped with justification (e.g. single-line glue, type definitions) appear as reasoned-omission rows — not absent rows.

## 4. Required Columns

| Column | Contents |
|--------|----------|
| **System** | System or module name, matching the name used in `index.md` and Pass 1 prioritisation. |
| **Research obligation** | Exact WebSearch query text, at least one source URL, and the research-mode classification (mode 1 domain pattern lookup, mode 2 specific-technique evaluation, or mode 3 known-anti-pattern check — see `detection-strategies.md` §6 Variety Requirement). |
| **Diagnostic-test obligation** | Path(s) of any test file(s) the audit wrote for this system, a one-line assertion summary per test, and the run result (pass/fail/benchmark number). If no test was written, either the link to the finding body confirming a test was not needed, or an explicit reasoned omission (see "Defer or skip a test only when" in `detection-strategies.md` §7). |
| **Findings emitted** | Count of findings issued for this system, with links to each. |
| **Reasoned omissions** | Any obligation skipped for this system with the justification. Silence is not acceptable — if the research or diagnostic-test obligation was not fulfilled, the reason must be recorded in this column. |

## 5. When to Update

Each row gets written as the system's Pass 2 work completes. Never batched at the end of the audit. The map is a verification ledger, not a retrospective report.

If Pass 2 is interrupted (context limit, user pause), the map state reflects exactly where the audit stopped. Resuming the audit means continuing row-by-row from the next system, not starting the map over.

## 6. Example Rows

**Completed system with research + diagnostic test:**

| System | Research obligation | Diagnostic-test obligation | Findings emitted | Reasoned omissions |
|--------|--------------------|-----------------------------|------------------|--------------------|
| Proximity search (`src/environment/proximity.rs`) | Query: "KD-tree vs linear scan for 2D continuous nearest-neighbour with ~1k points"; Source: <https://example.com/kd-tree-analysis>; Mode: 2 (specific-technique evaluation) | `tests/proximity_benchmark.rs` — benchmarks linear scan vs KD-tree build+query on 1,024-point sample; result: KD-tree 4.2x faster for batched queries | 2 findings (see [training-pipeline.md#proximity-search](training-pipeline.md#proximity-search)) | None |

**Reasoned omission (genuinely trivial system):**

| System | Research obligation | Diagnostic-test obligation | Findings emitted | Reasoned omissions |
|--------|--------------------|-----------------------------|------------------|--------------------|
| `src/util/format_seconds.rs` | Not performed | Not written | 0 | Single-line glue function; research not applicable per `detection-strategies.md` §"When Research Is Not Required"; no uncertainty a test could resolve. |

**Partial row during an in-progress audit (research done, test still to write):**

| System | Research obligation | Diagnostic-test obligation | Findings emitted | Reasoned omissions |
|--------|--------------------|-----------------------------|------------------|--------------------|
| Replay buffer sampling (`src/brain/training.rs:142-189`) | Query: "top-k selection vs full sort for replay buffer sampling"; Source: <https://example.com/topk>; Mode: 2 | PENDING — equivalence test for partial sort vs full sort planned at `tests/replay_buffer_sampling.rs` | — | — |

A row left in "PENDING" state at the end of the audit is itself a finding-integrity failure. Either write the test before issuing the finding, or convert PENDING to a reasoned omission with justification.
