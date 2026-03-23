# Coverage And Organisation

This skill should maximise depth and coverage without falling into arbitrary, redundant, or repeated content.

## Coverage Rule

Never decide scope by hitting a numeric target.

Do not think:

- "I need 20 exercises."
- "I need 30 concept files."
- "I need 5 materials files."

Instead think:

- what must the learner understand?
- what must the learner practise?
- what must be explained from first principles?
- what project-specific systems deserve reconstruction or debugging exercises?
- what older approaches remain educationally valuable?

## Main Learning Surfaces

Check for coverage across these surfaces:

1. foundational prerequisites
2. core domain concepts
3. reusable domain patterns
4. project architecture and systems
5. important decisions and trade-offs
6. current vs superseded approaches where the contrast teaches something
7. project-specific practice tasks

Not every project needs equal depth in all seven surfaces, but the skill should examine all seven before deciding scope.

## Organisation Rule

Organisation is mandatory, but over-organisation is a failure mode.

Use this principle:

- stable top-level structure,
- conditional deeper nesting.

### Good organisation

- makes scanning easier,
- groups related files by topic,
- reduces the time needed to find the next useful file,
- matches the repository's real conceptual boundaries.

### Bad organisation

- creates deep folder chains with almost no files,
- mirrors temporary thinking instead of stable topics,
- exists only for symmetry,
- hides important files behind avoidable nesting.

## Conditional Folder Depth

Create deeper topic or type folders only when they improve navigation.

Prefer flatter layouts when:

- there are very few files,
- the topic boundaries are obvious without another layer,
- the extra folder would likely remain tiny.

Prefer deeper layouts when:

- sibling file counts are becoming hard to scan,
- there are clear topic clusters,
- exercises or materials naturally separate into distinct groups,
- the repository already uses a similar stable topic language in `context/`.

## Progression Rule

The learning system should support multiple study routes:

- bottom-up,
- top-down,
- implementation-first,
- interview-prep,
- subsystem-specific.

Do not force everything into one rigid linear curriculum.

`STUDY_GUIDE.md` and `paths/*.md` should provide structure without pretending learning must be sequential in only one way.

## Anti-Redundancy Rule

More depth is good. Repetition is not.

Before creating a new file, ask:

- does this file have a distinct teaching job?
- does it cover a separate topic boundary?
- does it add a different route through the same knowledge?
- does it enable practice that other files do not?

If not, strengthen an existing file instead of adding another.
