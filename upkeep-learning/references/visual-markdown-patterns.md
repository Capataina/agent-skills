# Visual Markdown Patterns

Use markdown as a teaching tool, not just a container for paragraphs.

Rich formatting is expected whenever it improves understanding. The goal is maximum clarity and insight — use the full expressive range of markdown and ASCII to achieve it. Agent creativity in choosing representations is encouraged: if you can see a better way to show something visually, use it.

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
- training loop stages.

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
A2C   ████████████░░░░░  62%
SAC   ██████████████████  91%
PPO   ████████████████░░  80%
      0%                 100%
```

**Class anatomy:**
```text
┌─────────────────────────────────┐
│           ReplayBuffer          │
├─────────────────────────────────┤
│  capacity: int                  │
│  buffer: deque[Transition]      │
│  _rng: np.RandomState           │
├─────────────────────────────────┤
│  push(transition) → None        │
│  sample(n) → List[Transition]   │
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
