# Operating Modes

Use one of these three modes. Do not improvise a fourth mode unless the repository has a truly unusual need.

## 1. Project-Grounded External Research

This is the default mode.

Use it when the user asks for research on a topic for the project, for example:

- `research event sourcing for this repo`
- `look into connection pooling for this codebase`
- `research best practices for implementing retry strategies here`

This mode means:

- external research meets the tool-call floor by default (at least 3 distinct `WebSearch` + 3 distinct `WebFetch` across ≥2 source classes, with quoted passages and at least one contrasting source — see Sufficiency Floors below),
- project grounding is mandatory,
- the deliverable is one or more durable reference artefacts in `context/references/`.

Choose this mode whenever the core question is:

> what does external research — across multiple primary sources, including at least one contrasting view — imply for this repository?

## 2. Project-Grounded Comparative Decision Research

Use this when the core question is comparative or selection-oriented.

Typical prompts:

- `Redis vs Postgres for this project`
- `SQLite vs sled for this repo`
- `which rendering architecture fits this engine`

This mode should not collapse into a generic side-by-side comparison. It should end with a repository-specific judgement that explains:

- which option fits better,
- under which assumptions,
- what the switching costs are,
- what would need to be true for the other option to win.

## 3. Update / Merge / Extend Existing Research

Use this when the repository already contains relevant research and the new request should refine the corpus instead of creating redundant artefacts.

Typical triggers:

- `update the caching research now that the code changed`
- `merge these two storage papers`
- `extend the storage research with RocksDB`
- `reorganise the networking references into a folder`

This mode should preserve stable topic ownership and avoid multiplying near-duplicate files.

### Guardrail against self-refinement inflation

Same-model refinement of one's own prior artefact has a documented failure mode (arXiv 2407.04549): within a single context, self-refinement inflates perceived quality while real quality drops. The artefact reads better after the pass but has not actually improved — the model is rewarding its own wording, not adding evidence.

To resist this, an Update pass is only valid if at least one of the following is true:

- new external sources not present in the prior artefact have been consulted and added to the External Research Trail,
- repository state has changed since the prior artefact (cite the specific commit, branch, or file diff that motivates the update),
- a specific factual error in the prior artefact has been identified and is being corrected (name the claim, the correction, and the source that grounds the correction).

An Update pass that merely reorganises, rewords, or re-weights existing content without new evidence is not a valid Update. Prefer "no change needed" over rewrite with the same inputs. Document the decision either way in the artefact's handoff.

## Scope Rules

Default scope rules:

- meet the tool-call floor on external research (3+ `WebSearch`, 3+ `WebFetch` across ≥2 source classes, with quoted passages and at least one contrasting source) rather than a single shallow lookup,
- prefer targeted code inspection over traversing the whole repository,
- prefer one coherent paper over many files,
- prefer a topic folder only when decomposition clearly improves durability and clarity,
- prefer updating existing research over creating overlap.

## Sufficiency Floors And Ceiling

Sufficiency is a two-layer idea in this skill: a **floor** below which research is incomplete regardless of how good the reasoning sounds, and a **ceiling** above which additional research stops sharpening the decision. Do not collapse these into one judgement. The floor is not negotiable; the ceiling is.

### Sufficiency floors (non-ratable)

Research is **not yet started** until all of the following are true. These are counted obligations, not qualitative assessments:

- at least 3 distinct `WebSearch` calls have been made against topic-specific queries (not paraphrases of each other),
- at least 3 distinct `WebFetch` calls have been made against primary sources identified by those searches, covering at least 2 source classes (for example: foundational paper + official documentation; benchmark + reference implementation),
- at least one direct quoted passage from a primary source is attached to each major source-backed claim in the artefact,
- at least one source that **limits, disagrees with, or complicates** the prevailing recommendation has been consulted and is represented in the artefact.

Research that only confirms is insufficient regardless of depth. A research pass that quotes six sources all agreeing has not yet touched the contrasting-source obligation.

### Sufficiency ceiling (qualitative, ratable)

Once the floors are met, research is **sufficient to stop** when:

- the major implementation directions are understood,
- the strongest relevant trade-offs are captured,
- the current repository state has been verified enough to support project-specific claims,
- the recommendation no longer depends on obvious unanswered questions that could have been resolved within the run.

The ceiling is a judgement call. The floor is not. Do not use the ceiling to argue past the floor. Specifically: the reasoning "my first search answered the question completely" is a motivated-reasoning signature, not a sufficiency argument — see `motivated-reasoning-defence.md`.

### Quota-thinking is still wrong, in the other direction

The floors above are not quotas to chase with thin coverage. Hitting 3 `WebSearch` calls with three near-identical queries does not satisfy the floor. The point of the count is to force a real breadth of evidence; padding it defeats the purpose just as badly as skipping it.
