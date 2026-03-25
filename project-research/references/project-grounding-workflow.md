# Project Grounding Workflow

The skill must understand how the topic relates to the repository before it writes conclusions. Follow this workflow.

## 1. Locate The Existing Memory Surface

Start in `context/`.

Look for:

- existing research in `context/references/`,
- architecture and systems files that mention the relevant subsystem,
- plans or decisions that already constrain the topic.

Answer these questions before expanding outward:

- what problem in this repository does the topic relate to,
- what parts of the system are likely involved,
- what prior conclusions already exist,
- what would be risky to assume without code verification.

## 2. Define The Repository-Specific Question

Rewrite the topic as a project question, not a generic topic heading.

Weak:

- `A2C`

Strong:

- `How far should A2C be taken as a trustworthy baseline for this repository`
- `What would a production-worthy retry strategy look like in this codebase`
- `Which storage model best fits the current event flow and consistency needs here`

This step is what keeps the research from wandering.

## 3. Inspect The Relevant Code Surface

Inspect the code paths that matter for the question.

Examples:

- current implementation of the algorithm or subsystem,
- interfaces the new design would need to fit,
- telemetry, evaluation, configuration, or persistence layers that change the recommendation,
- tests that reveal current expectations or missing safeguards.

The aim is not exhaustive coverage. The aim is enough verified context to speak accurately about the repository.

## 4. Establish The Project State

Before major synthesis, write down a working model of the current state:

- what exists,
- what is partial,
- what is missing,
- what appears fragile,
- which claims are verified versus inferred.

This model becomes the anchor for the rest of the research.

## 5. Expand Into External Research

Now widen scope outward. Gather the strongest sources that help answer the repository-specific question.

Look for:

- theory that explains why the approach works,
- implementation details that materially affect outcomes,
- real-world examples that match the repository's constraints,
- comparisons that sharpen the decision,
- common failure modes and evaluation traps.

## 6. Synthesize Back Into Repository Guidance

Bring the research back to the repository in concrete terms:

- what the topic means here,
- what the repository already does correctly,
- what gaps matter most,
- what not to overbuild,
- what to prioritise next,
- what should remain uncertain until validated experimentally.

## Grounding Checklist

Before writing the final artefact, confirm:

- the current repository state is described from `context/` plus code, not from the README alone,
- the external research actually answers the repository-specific question,
- the conclusions visibly depend on project reality,
- a reader can tell why the research belongs in this repository and not in any random project.
