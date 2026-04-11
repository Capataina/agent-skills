# Visual Markdown Patterns

## Table of Contents

1. [Strong Patterns](#strong-patterns)
2. [Diagram Rule](#diagram-rule)
3. [Creative ASCII Visualisation](#creative-ascii-visualisation)
4. [Table Rule](#table-rule)
5. [Emphasis Rule](#emphasis-rule)
6. [Section Design Rule](#section-design-rule)
7. [Failure Modes](#failure-modes)

The universal output standard — rich formatting, depth as a virtue, full markdown range, agent creativity in choosing representations — is assumed. This file documents the specific visual patterns that teach well in `learning/` archive material and the discriminations that matter for educational writing.

Markdown in this context is a teaching tool, not a container for paragraphs. The patterns below describe how the standard formats earn their place in concept files, system deep-dives, exercise headers, and the rest of the archive.

## Strong Patterns

Use these freely where helpful:

- tables,
- comparison matrices,
- callout blocks,
- emphasis with bold and italics,
- numbered procedures,
- bulleted decompositions,
- ASCII diagrams,
- ASCII data visualisations (heat maps, bar charts, spatial layouts),
- dependency maps,
- tree views,
- side-by-side trade-off lists,
- checklists for route and exercise files,
- notation tables,
- symbol reference tables,
- flow charts,
- state transition diagrams,
- architecture overviews.

## Diagram Rule

If a concept has important structure, flow, hierarchy, or spatial meaning, consider a diagram.

Examples:

- runtime data flow,
- algorithm update flow,
- concept dependency map,
- subsystem relationship graph,
- path progression map,
- entity lifecycle,
- request processing pipeline.

ASCII diagrams are the default when portable markdown is the goal. Mermaid is acceptable when the archive is rendered in an environment that supports it.

## Creative ASCII Visualisation

ASCII can do more than flow diagrams. Use it to make abstract information concrete and spatial.

Examples of creative ASCII use:

**Heat map of event density across a grid:**
```text
      Col:  0    1    2    3    4
Row 0:    [ -- ][ -- ][ ## ][ ## ][ -- ]
Row 1:    [ -- ][ ## ][ ## ][ ## ][ ## ]
Row 2:    [ ## ][ ## ][ ++ ][ ## ][ -- ]
Row 3:    [ -- ][ -- ][ ## ][ -- ][ -- ]

Legend:  ++ = highest density   ## = medium   -- = low
```

**Comparison bar chart:**
```text
LRU       ████████████░░░░░  62%
LFU       ██████████████████  91%
TTL-only  ████████████████░░  80%
          0%                 100%
```

**Class anatomy:**
```text
┌─────────────────────────────────┐
│         ConnectionPool          │
├─────────────────────────────────┤
│  max_size: int                  │
│  pool: deque[Connection]        │
│  _lock: threading.Lock          │
├─────────────────────────────────┤
│  acquire() → Connection         │
│  release(conn) → None           │
│  __len__() → int                │
└─────────────────────────────────┘
```

If the information has a shape, a density, or a spatial relationship — draw it. A reader who can see the structure learns faster than a reader who has to construct it mentally from prose.

## Table Rule

Use tables when comparing:

- algorithms,
- statuses,
- alternatives,
- signals and ranges,
- components and responsibilities,
- current vs planned systems,
- terms and definitions,
- hyperparameter effects.

## Emphasis Rule

Use bold and italics intentionally:

- bold for major takeaways,
- italics for terminology emphasis or conceptual contrast,
- inline code for file names, symbols, paths, and literal identifiers.

Do not overdo formatting to the point that the page becomes noisy, but do not avoid formatting out of caution either.

## Section Design Rule

Long documents should be visually navigable.

Use:

- meaningful headings,
- subheadings,
- short framing paragraphs,
- lists after dense prose,
- recap sections after difficult parts.

## Failure Modes

Treat these as failures:

- major files that are giant undifferentiated text blocks,
- dense comparison topics with no tables,
- flow-heavy topics with no diagrams or structural aids,
- mathematically dense topics with no notation tables or worked formatting,
- spatial or data-heavy topics with no visual representation,
- a concept with clear structural anatomy described only in prose.
