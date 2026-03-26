# Formatting Patterns

Use the full expressive range of markdown and ASCII as analytical tools, not as decoration.

Agent creativity in choosing visual representations is encouraged. If you can see a way to make an insight clearer, more spatial, or more comparable through a diagram, table, or ASCII visualisation — use it.

The target style blends:

- the teaching clarity of educational archive material,
- the structural richness of implementation memory documents,
- the density and discipline of a technical synthesis paper.

## Good Uses Of Rich Formatting

### Comparison Tables

Use for:

- implementation choices,
- trade-offs,
- current state vs desired state,
- alternatives and selection criteria,
- maturity ladders.

### Matrices

Use when a plain table is not enough, for example:

- topic by subsystem impact,
- recommendation by cost/risk/benefit,
- repository feature by research support level.

### Trees

Use when explaining:

- proposed `context/references/` folder structure,
- decomposition of a topic area,
- related artefact ownership.

### Callouts Or Hero Blocks

Use sparingly for:

- the central judgement,
- the most important warning,
- the key framing sentence that the rest of the paper depends on.

### ASCII Diagrams and Data Visualisations

Use ASCII diagrams when an architecture or information flow is easier to understand visually.

Use ASCII data visualisations when comparing magnitudes, distributions, densities, or multi-dimensional properties.

Examples:

```text
External research
        |
        v
Project grounding -> Current-state model -> Recommendation
        |                                  |
        +---------- code verification -----+
```

```text
Algorithm comparison (sample efficiency):

A2C   ████████████░░░░░  62%
SAC   ██████████████████  91%
PPO   ████████████████░░  80%
TD3   ███████████████░░░  76%
      0%                 100%
```

The criterion is analytical value: does this representation make the finding more concrete, comparable, or spatially obvious? If yes, use it.

### Layered Presentation

It is often useful to present the same insight twice in different forms:

- a compact table for scanning,
- followed by short bullets that interpret the table.

This is supportive duplication inside one artefact and is allowed.

## Style Guidance

Write with:

- plain words when they are enough,
- exact terminology when it matters,
- short explanatory bridges around dense ideas,
- strong topic sentences,
- explicit contrast words such as `however`, `by contrast`, `in this repository`, `the main catch`, `the real constraint`.

Avoid:

- needlessly academic phrasing,
- paragraph walls where a table would be clearer,
- giant bullet dumps that never synthesise,
- charts or diagrams added only for visual variety.
