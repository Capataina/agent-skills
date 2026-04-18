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

- `connection pooling`

Strong:

- `What connection pooling strategy best fits this repository's concurrency model`
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

## 4.25 Pattern-Breaking Checkpoint (for long runs)

If the session so far has exceeded roughly ten meaningful steps (each `Read`, `Grep`, `Bash`, or `WebSearch` counts), pause before continuing and write down, in the response, a short pattern-break block:

- list what you have done so far (one line per step, grouped by tool),
- name the next step explicitly — and if the next step is not external research with at least two distinct `WebSearch` queries, explain why in writing,
- commit in writing to the exact next action,
- execute it immediately.

The purpose of this checkpoint is to interrupt autopilot. Long internal-reading runs build momentum toward more internal reading. Naming the next step in writing breaks that momentum and forces the decision to be visible.

## 4.5 Motivated Reasoning Check

At the boundary between project grounding (steps 1–4) and external research (step 5), pause.

A common rationalisation appears at exactly this boundary: "I have read the project files; I can now synthesize a recommendation without external research because [simple problem / obvious answer / non-standard project / I already know this topic]." This is a failure mode, not a conclusion.

Your reasoning at this point is compromised for two reasons:

- you have momentum toward closure — the internal reading feels complete and moving to external search feels like regression,
- post-training bias against `WebSearch` and `WebFetch` makes skipping them feel natural (see `tool-asymmetry-and-investigation.md`).

External research is not optional. If you find yourself generating reasons why external research is not needed for this specific topic, **that is the signal you need it most**, not a valid exception.

**Pre-commitment:** You will call `WebSearch` or `WebFetch` at least twice with distinct queries before forming project-specific conclusions. This is not negotiable. The full floor from SKILL.md ("External Research Floor") still applies beyond this pre-commitment; the pre-commitment is only the minimum to cross the boundary.

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
