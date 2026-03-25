# Formatting Patterns

Use formatting as an analytical tool, not as decoration.

The target style blends:

- the teaching clarity of `upkeep-learning`,
- the structural richness of `upkeep-context`,
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

### ASCII Diagrams

Use when an architecture or information flow is easier to understand visually and a quick text diagram is sufficient.

Good example:

```text
External research
        |
        v
Project grounding -> Current-state model -> Recommendation
        |                                  |
        +---------- code verification -----+
```

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
