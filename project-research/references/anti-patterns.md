# Anti-Patterns

These are the failure modes this skill must actively resist.

## 1. Generic Topic Report

The paper explains the topic well enough for any reader but says very little about this repository.

Why this fails:

- the skill exists for project-grounded research,
- generic output does not justify a place in `context/references/`.

## 2. README-Led Fiction

The paper describes the project as if the README were implementation proof.

Why this fails:

- READMEs are often aspirational,
- the repository may already contain fixes, omissions, or changes that the README does not capture.

## 2b. Blog-Post-Led Fiction (external symmetry to §2)

The paper treats a single high-ranking blog post or tutorial as authoritative research, without checking foundational papers, official documentation, or reference implementations.

Why this fails:

- search ranking optimises for click-through, not source authority,
- plausible-sounding aggregators may replicate errors from older sources,
- a single secondary source cannot satisfy the skill's multi-source-class evidence standard.

Mitigation: the Evidence Standard requires at least 2 source classes; the contrasting-source obligation requires at least one source that limits or disagrees with the emerging recommendation. A single blog post satisfies neither. If the first useful hit is a blog post, use it as a pointer to the primary sources it cites, then `WebFetch` those.

## 3. Side-Quest Comprehensiveness

The paper wanders into adjacent topics that do not sharpen the repository decision.

Example:

- `Postgres is interesting, MongoDB is interesting, Redis is interesting, databases are interesting`

Why this fails:

- breadth without relevance creates noise instead of insight.

## 4. Decorative Research

The artefact has many headings, charts, and comparison tables but few concrete conclusions.

Why this fails:

- formatting is not analysis,
- the reader still cannot act on the result.

## 5. Recommendation Without Current-State Verification

The paper recommends improvements that are already implemented or critiques problems that do not exist.

Why this fails:

- it damages trust in the entire research artefact.

## 6. Blind Template Following

The paper includes every section pattern whether or not the topic needs it.

Why this fails:

- strong templates become weak when they are used mechanically.

## 7. Quota-Thinking

The paper acts as if depth can be guaranteed by raw counts.

Why this fails:

- arbitrary minima create predictable but thin output,
- the real standard is sufficiency of reasoning and relevance.

For the concrete sufficiency test, see operating-modes.md.

## 8. Research That Cannot Compound

The artefact ignores existing references, creates overlap, and leaves no clear relationship to the rest of the research corpus.

Why this fails:

- `context/references/` should become smarter over time, not noisier.

## 9. Research-by-Synthesis (Zero External Tools)

The paper reads thorough and cites project facts accurately, but the entire analysis derives from reading `context/` and code — zero `WebSearch`, zero `WebFetch`, zero external documentation lookups.

Why this fails:

- the skill exists to expand into external research, not to synthesize existing context into better prose,
- investigation without external tools is not research; it is reframing,
- the agent will consistently skip external research if not held to a mandatory floor — this is a documented tool-selection bias, not a judgement call.

Catch this by:

- requiring the agent to list every `WebSearch` and `WebFetch` call in the obligation-verification section of the artefact,
- failing any artefact with zero external tool calls,
- treating "I found everything I needed in `context/`" as a confession of incomplete work, not a success signal.

See `tool-asymmetry-and-investigation.md` for why this failure is systematic and `motivated-reasoning-defence.md` for the reasoning signatures that precede it.
