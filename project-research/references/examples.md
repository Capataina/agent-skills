# Examples

## Table of Contents

1. [Example 1: Single-File Research Paper](#example-1-single-file-research-paper)
2. [Example 2: Comparative Decision Paper](#example-2-comparative-decision-paper)
3. [Example 3: Topic Folder](#example-3-topic-folder)
4. [Example 4: Strong Research Signal Pattern](#example-4-strong-research-signal-pattern)
5. [Example 5: Weak Vs Strong Conclusion](#example-5-weak-vs-strong-conclusion)

This file contains worked examples of how to shape research for a repository. Do not copy them mechanically. Use them to understand the level of synthesis and project grounding expected.

## Example 1: Single-File Research Paper

Topic:

- `event sourcing for this project`

Strong output shape:

- `context/references/event-sourcing.md`

Why one file works:

- one stable topic,
- one dominant question,
- comparisons and maturity analysis fit cleanly as sections.

Good section mix (see section-patterns.md for the full catalog):

- scope and purpose,
- current project relevance,
- what event sourcing actually is,
- research signal,
- what fits this project well,
- what fits this project badly,
- current state vs research-backed expectations,
- maturity ladder,
- gap analysis,
- recommended priority order,
- relationship to existing context.

## Example 2: Comparative Decision Paper

Topic:

- `Redis vs Memcached for this project`

Strong output shape:

- `context/references/redis-vs-memcached.md`

Key moves:

- do not describe both technologies in isolation for most of the paper,
- keep comparing them through the repository's constraints,
- end with a conditional decision rather than a vibes-based preference.

Useful sections:

- decision framing,
- repository constraints,
- comparison matrix,
- what each approach demands from the current codebase,
- transition costs,
- recommendation under current assumptions,
- what evidence could reverse the recommendation.

## Example 3: Topic Folder

Topic:

- `caching strategies for this repository`

Strong output shape:

```text
context/references/caching-strategies/
├── overview.md
├── application-layer-caching.md
└── redis-vs-memcached.md
```

Why a folder works:

- there is a stable research area,
- multiple papers share context,
- follow-up work is likely,
- one file would become crowded.

Folder roles:

- `overview.md`:
  the area map, relationships, and where each paper fits
- `application-layer-caching.md`:
  single-topic deep dive
- `redis-vs-memcached.md`:
  explicit decision surface

## Example 4: Strong Research Signal Pattern

Useful table shape:

| Topic | Source-backed signal | Current repository state | Project implication |
|---|---|---|---|
| Connection pooling | Critical for throughput under concurrent load | Single connection per request | Meaningful gap if latency persists |
| Query result caching | Often a strong default for read-heavy workloads | Already present via HTTP cache headers | Preserve; not a priority area |
| Schema migration tooling | Crucial for safe iterative schema evolution | Manual SQL scripts only | High leverage for deployment confidence |

Why this works:

- the section does not merely list lessons,
- it translates them into repository consequences.

## Example 5: Weak Vs Strong Conclusion

Weak:

> Redis is a good caching solution and has been used in many projects. Memcached is also strong and may be better in some situations.

Strong:

> In this repository, Redis still makes sense as the caching layer because the data shapes are varied (hashes, sorted sets, lists), the eviction policy needs fine-grained control, and the current question is "can we reduce P95 latency below 200ms?" The main catch is that the current usage pattern is not yet instrumented enough to make cache hit ratio data trustworthy. That means the first research-backed priority is not cache technology novelty but observability.

Why the strong version works:

- it answers the project question,
- it names the governing constraint,
- it turns research into a decision.
