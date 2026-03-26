# Markdown Presentation Patterns

## Table of Contents

1. Goal
2. Default Principle
3. When To Use Bullets
4. When To Use Tables
5. When To Use Trees
6. When To Use Diagrams
7. Supportive Multi-Format Presentation
8. Anti-Patterns

## 1. Goal

Use the full expressive range of markdown and ASCII to make repository memory as clear, scannable, and useful as possible for both humans and LLMs. Agent creativity in choosing representations is encouraged — if you can see a better way to show something visually, use it.

## 2. Default Principle

Choose the representation that makes the information clearest.

Do not force visuals for style alone. Do not force bullet lists when another format would communicate the same material better.

## 3. When To Use Bullets

Use bullets for:

- concise ownership lists,
- key takeaways,
- implementation facts that are easiest to scan sequentially,
- risks, caveats, and planned changes.

Bullets are the default, but they should not be the only format.

## 4. When To Use Tables

Use tables for:

- comparing multiple subsystems or components across the same dimensions,
- interface inventories,
- module-to-responsibility mappings,
- UI surfaces or feature inventories,
- configuration summaries.

Tables work best when each row shares the same fields.

## 5. When To Use Trees

Use fenced text trees for:

- repository structure,
- nested subsystem layouts,
- notable file and folder overviews.

Add one-line descriptions to important entries so the tree is informative rather than decorative.

## 6. When To Use Diagrams

Use a simple ASCII diagram or mermaid graph when:

- dependency relationships are hard to explain in bullets,
- execution flow spans several layers,
- ownership boundaries are easier to understand visually,
- state or data moves through multiple transformations.

Keep diagrams simple enough to read in plain text.

## 6b. Creative ASCII Visualisation

ASCII can go beyond flow diagrams. When information has spatial structure, density, or dimensional relationships, consider a more expressive ASCII representation.

Examples:

- module dependency heat maps showing coupling intensity,
- ASCII bar charts comparing subsystem sizes or call frequencies,
- class anatomy boxes showing fields and methods at a glance,
- timeline representations for pipeline stages.

The criterion is the same as any other format: does this make the information clearer? If yes, use it.

## 7. Supportive Multi-Format Presentation

It is often better to combine formats.

Good examples:

- a table that inventories eight modules, followed by bullets that call out the most important engineering implications,
- a repository tree followed by a short subsystem summary,
- a flow diagram followed by bullets describing the failure modes or constraints.

This is supportive duplication inside one canonical document.

## 8. Anti-Patterns

Avoid:

- decorative charts with no informational gain,
- tables used for content that reads better as bullets,
- diagrams that are more complex than the system they describe,
- repeating the same information verbatim across documents,
- replacing all prose with visuals and forcing the reader to reverse-engineer the meaning.
