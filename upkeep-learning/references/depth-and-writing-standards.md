# Depth And Writing Standards

## Table of Contents

1. [Core Rule](#core-rule)
2. [Narrative Standard](#narrative-standard)
3. [Pedagogical Completeness](#pedagogical-completeness)
4. [Long-Form Acceptance](#long-form-acceptance)
5. [Readability Standard](#readability-standard)
6. [Explanation Layers](#explanation-layers)
7. [Anti-Shallow Rules](#anti-shallow-rules)
8. [Repetition Rule](#repetition-rule)
9. [Tone Rule](#tone-rule)
10. [Cross-Linking Rule](#cross-linking-rule)
11. [Failure Modes](#failure-modes)

The universal output standard — depth as a virtue, comprehensive explanation, rich formatting — applies to everything in `learning/`. This file defines the additional writing bar specific to educational content: how teaching prose differs from reference prose, what counts as pedagogical completeness, and the failure modes that make educational material weak.

## Core Rule

Be verbose, explanatory, elaborate, descriptive, comprehensive, and exhaustive.

Do not self-limit.

Do not write as if concise prose is inherently better.

For this skill, shallow writing is a failure mode.

## Narrative Standard

Teach as a connected narrative, not as a topic inventory.

The difference matters. A topic inventory lists assertions:

- Raft uses a leader-based approach.
- Log replication ensures consistency.
- This applies to distributed databases.

A connected narrative explains the mechanism: what problem consensus solves, why a leader-based protocol simplifies ordering, how log replication guarantees that all nodes converge on the same state, what happens during leader failure and re-election, where Raft trades availability for consistency, how it compares to leaderless approaches like EPaxos, and where it appears in the project at hand. The inventory leaves the learner with a checklist of facts they cannot reason from. The narrative leaves the learner with a mental model they can use, extend, and question.

When writing about a concept, ask: could a motivated learner build a working understanding from this file alone, or are they left with a list of things they need to look up elsewhere? If the latter, the file is an inventory, not a teaching document. Expand it.

## Pedagogical Completeness

A major topic is not complete when it has been mentioned.

A major topic is complete only when it has been explained thoroughly enough that a motivated learner should not be left with obvious unresolved questions.

That usually requires:

- more than one angle of explanation,
- examples,
- edge cases,
- comparisons,
- cross-links,
- project grounding,
- explicit misconceptions and clarifications.

## Long-Form Acceptance

Long documents are expected.

Use as many lines as necessary to teach the topic properly.

It is normal for important files to be:

- several hundred lines,
- heavily structured,
- rich with examples,
- broken into many sections and subsections.

Do not apologise for length. Use it well.

## Readability Standard

The archive should be easy to follow despite its depth.

Use:

- clear sectioning,
- informative headings,
- lists where they improve scanability,
- tables where they clarify distinctions,
- emphasis where it helps the eye,
- examples after dense ideas,
- plain-English restatements of difficult material.

## Explanation Layers

For difficult topics, stack explanations in this order when useful:

1. why it matters,
2. intuition,
3. formal statement,
4. mechanism or derivation,
5. worked example,
6. project grounding,
7. misconceptions,
8. alternatives and trade-offs.

Do not jump straight to abstraction if the learner needs a bridge.

## Anti-Shallow Rules

Do not:

- reduce a major topic to a short prose summary,
- omit examples for difficult material,
- strip out detail because the page already "looks long enough",
- avoid repetition when a second framing would clarify a hard idea,
- replace explanation with vague labels like "standard approach" or "common technique".

## Repetition Rule

Useful repetition is allowed when it teaches from a different angle.

Bad repetition restates the same thing without adding value.

Good repetition:

- gives intuition after formalism,
- gives a worked example after a definition,
- compares two similar concepts side by side,
- revisits a concept later in a project-specific context.

## Tone Rule

Be intellectually ambitious but readable.

Use:

- precise terms,
- direct prose,
- patient explanation,
- explicit clarification.

Avoid:

- performative academic language,
- jargon stacking,
- sounding cryptic to imitate authority.

## Cross-Linking Rule

Deep archives need strong cross-links.

Whenever useful, point to:

- prerequisite files,
- next-step files,
- related paths,
- exercises,
- glossary entries,
- comparisons,
- system deep-dives.

## Failure Modes

Treat these as failures:

- a central concept file that reads like a brief overview,
- a system deep-dive with no mechanics,
- a mathematical topic with no worked example,
- a materials file that is only a link list,
- a path file with no real progression,
- an archive that is organised but intellectually thin.
