# Formatting Patterns

## Table of Contents

1. [Good Uses Of Rich Formatting](#good-uses-of-rich-formatting)
2. [Style Guidance](#style-guidance)

The universal output standard — rich formatting, depth as a virtue, full markdown range, agent creativity in choosing representations — is assumed. This file documents the specific patterns that earn their place in research artefacts and the discriminations that matter for analytical writing.

In research artefacts, formatting is an analytical tool. The patterns below describe how the standard formats sharpen synthesis, comparison, and recommendation in `context/references/` papers.

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
Cache hit ratio by strategy:

LRU       ████████████░░░░░  62%
LFU       ██████████████████  91%
TTL-only  ████████████████░░  80%
Random    ███████████████░░░  76%
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
