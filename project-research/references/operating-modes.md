# Operating Modes

Use one of these three modes. Do not improvise a fourth mode unless the repository has a truly unusual need.

## 1. Project-Grounded External Research

This is the default mode.

Use it when the user asks for research on a topic for the project, for example:

- `research event sourcing for this repo`
- `look into connection pooling for this codebase`
- `research best practices for implementing retry strategies here`

This mode means:

- external research is substantial by default,
- project grounding is mandatory,
- the deliverable is one or more durable reference artefacts in `context/references/`.

Choose this mode whenever the core question is:

> what does serious outside research imply for this repository?

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

## Scope Rules

Default scope rules:

- prefer wide external research over shallow lookup,
- prefer targeted code inspection over broad codebase traversal,
- prefer one coherent paper over many files,
- prefer a topic folder only when decomposition clearly improves durability and clarity,
- prefer updating existing research over creating overlap.

## Sufficiency Test

Do not use arbitrary counts such as "exactly three papers."

Instead, research is sufficient when:

- the major implementation directions are understood,
- the strongest relevant trade-offs are captured,
- the current repository state has been verified enough to support project-specific claims,
- the recommendation no longer depends on obvious unanswered questions that could have been resolved within the run.

Research is substantial when you have engaged with multiple distinct sources or perspectives, not just confirmed an initial impression. If your first search answered the question completely, verify that answer against at least one contrasting source before accepting it.
