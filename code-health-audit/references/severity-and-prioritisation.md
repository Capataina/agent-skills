# Severity and Prioritisation

This reference defines how to rank, group, and order findings by impact and effort.

## Table of Contents

1. Severity Levels
2. Effort Estimates
3. Priority Matrix
4. Grouping Strategies
5. Cross-System Findings
6. Presentation Order

## 1. Severity Levels

Every finding must be assigned one severity level:

### Critical

The finding represents an active correctness or reliability risk. If not addressed, it may cause incorrect behaviour, data loss, or system failure.

Examples:
- Race conditions in production code paths.
- Silent error swallowing that hides failures.
- Resource leaks under load.

Critical findings are rare in a code health audit (which focuses on "free" improvements). When they appear, they belong in the "Known Issues and Active Risks" category.

### High

The finding represents a significant improvement opportunity with clear, concrete benefits. The change is straightforward and the impact is substantial.

Examples:
- A quadratic algorithm on a dataset of thousands of items.
- A large dead module causing navigation confusion.
- A hot-path function with unnecessary allocations in every call.

### Medium

The finding represents a meaningful but non-urgent improvement. The benefit is real but the current code is not causing active problems.

Examples:
- Inconsistent error handling across modules.
- Moderate modularisation opportunities in large files.
- Hardcoded configuration values that will eventually need tuning.

### Low

The finding represents a minor improvement. Fixing it would be nice but does not meaningfully change the project's health.

Examples:
- Unused imports.
- Minor naming inconsistencies.
- Small dead helper functions.

## 2. Effort Estimates

Every finding should include a rough effort indicator:

### Trivial

Less than 15 minutes. Delete a function, remove an import, rename a variable.

### Small

15 minutes to an hour. Extract a function, replace a hardcoded array with a formula, add a pre-allocation.

### Medium

One to several hours. Refactor a module, replace an algorithm, split a large file.

### Large

A day or more. Restructure a subsystem, introduce a new data structure across multiple callsites, reconcile inconsistent patterns project-wide.

Effort estimates are rough guides. Their purpose is to help the implementing engineer plan work, not to predict timelines precisely.

## 3. Priority Matrix

Priority combines severity and effort:

```
                    ┌────────────┬────────────┬────────────┬────────────┐
                    │  Trivial   │   Small    │   Medium   │   Large    │
    ┌───────────────┼────────────┼────────────┼────────────┼────────────┤
    │  Critical     │  Do first  │  Do first  │  Do first  │  Do first  │
    ├───────────────┼────────────┼────────────┼────────────┼────────────┤
    │  High         │  Do first  │  Do early  │  Do early  │  Plan it   │
    ├───────────────┼────────────┼────────────┼────────────┼────────────┤
    │  Medium       │  Do early  │  Do early  │  Plan it   │  Consider  │
    ├───────────────┼────────────┼────────────┼────────────┼────────────┤
    │  Low          │  Do early  │  Consider  │  Consider  │  Backlog   │
    └───────────────┴────────────┴────────────┴────────────┴────────────┘
```

- **Do first:** address before other audit items. These are high-value, often quick wins.
- **Do early:** address in the first pass of cleanup work.
- **Plan it:** worth doing but requires planning and may span multiple sessions.
- **Consider:** worth documenting but may not be worth the effort right now.
- **Backlog:** record for future reference but do not prioritise.

## 4. Grouping Strategies

Findings should be grouped to make the output navigable and to help the implementing engineer work efficiently.

### By System

Group findings by the subsystem they affect. This is the default when:
- findings are concentrated in a few systems,
- the implementing engineer is likely to work through one system at a time,
- the project has clear subsystem boundaries.

### By Category

Group findings by their analysis category. This works well when:
- findings are evenly distributed across systems,
- the implementing engineer wants to do all dead code removal at once, then all performance improvements, etc.,
- a single system has very few findings.

### Hybrid

Use one file per system, with findings organised by category within each file. This is often the best approach for large audits because it enables both navigation patterns.

### Choosing a Strategy

Let the data guide the grouping. If one system has 30 findings and three others have 2 each, a by-system approach with a combined "minor findings" file is better than 14 category files with 2 findings each.

The goal is that the implementing engineer can:
1. quickly understand the overall scope (from the index),
2. navigate to the findings relevant to their current focus,
3. work through findings in a logical order.

## 5. Cross-System Findings

Some findings span multiple systems:

- Inconsistent patterns that appear across the codebase.
- Dependencies that are unused project-wide.
- Configuration drift that affects multiple modules.

These should be:
- documented in a dedicated cross-cutting file (e.g., `cross-cutting.md` or `project-wide.md`),
- listed in the index with a note that they span systems,
- not duplicated into every affected system's file.

## 6. Presentation Order

Within each file, present findings in this order:

1. Critical findings first (if any).
2. High-severity, low-effort findings (quick wins).
3. High-severity, higher-effort findings.
4. Medium findings grouped logically.
5. Low findings at the end.

This ordering ensures the implementing engineer sees the most important and most actionable items first.
