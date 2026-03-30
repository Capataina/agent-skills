# Decomposition Rules

Choose the smallest durable output shape that can hold the research cleanly.

## Default: One Paper

Prefer one file when:

- there is one stable topic,
- the answer is coherent from start to finish,
- subtopics are supporting sections rather than separate reference objects,
- future growth is likely incremental rather than branching.

Examples:

- `context/references/event-sourcing.md`
- `context/references/logging-pipeline.md`
- `context/references/connection-pooling.md`

## Topic Folder

Prefer a folder when:

- the topic naturally splits into several stable subtopics,
- comparison papers need a shared home with cross-references,
- the area is likely to grow through repeated research sessions,
- one file would become hard to navigate or would mix multiple ownership scopes.

Examples:

```text
context/references/caching-strategies/
├── overview.md
├── application-layer-caching.md
└── redis-vs-memcached.md
```

```text
context/references/networking/
├── overview.md
├── rollback.md
└── client-prediction.md
```

## Update Existing Research

Prefer updating an existing artefact when:

- the new request clearly extends the same stable topic,
- the current artefact is thin but salvageable,
- the new material would otherwise produce overlap,
- the existing file is still the right canonical home.

## Merge Or Split

Merge when:

- two files explain the same stable topic,
- readers would struggle to know which one owns the answer,
- one file can reference the other only awkwardly because they overlap too much.

Split when:

- one file contains multiple stable topics with different growth paths,
- one section has become its own durable reference object,
- a comparison or subtopic now deserves independent updating.

## Avoid Arbitrary Fragmentation

Do not split output because:

- the skill "likes folders",
- the source material came from multiple tabs,
- it feels more impressive to generate more files.

Decomposition should serve clarity, stable ownership, and future upkeep.
