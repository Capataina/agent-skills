# Glossary Standards

In a large learning archive, the glossary is infrastructure.

Treat `GLOSSARY.md` as one of the archive's most important files.

## Core Rule

The glossary should be comprehensive, precise, readable, and deeply cross-linked.

Do not write sparse dictionary fragments.

## Entry Structure

Strong entries usually include:

- term name,
- precise definition,
- plain-language explanation,
- concrete example,
- project-specific relevance when applicable,
- a `See:` line pointing to one or more deeper files.

## Scope Rule

Include:

- domain theory terms,
- project architecture terms,
- algorithmic terms,
- maths and statistics terms,
- implementation terms when they matter to understanding.

If a term appears repeatedly across the archive, it probably belongs in the glossary.

## Cross-Linking Rule

Glossary entries should point outward to deeper files.

Major files should also point back to the glossary when useful.

The glossary should become a stable lookup layer for the whole archive.

## Depth Rule

Important terms deserve substantial entries.

For central concepts, include:

- what the term means,
- why it matters,
- how it differs from nearby terms,
- where it appears in the project.

## Organisation Rule

Alphabetical ordering is usually best for a global glossary.

Use consistent formatting across entries.

## Failure Modes

Treat these as failures:

- too few entries,
- entries with no examples,
- entries that are too vague to be useful,
- no cross-links to deeper files,
- a glossary that ignores README-defined future/domain concepts because they are not yet implemented.
