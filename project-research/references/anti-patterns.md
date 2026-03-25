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

## 3. Side-Quest Comprehensiveness

The paper wanders into adjacent topics that do not sharpen the repository decision.

Example:

- `A2C is interesting, SAC is interesting, PPO is interesting, RL is interesting`

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

## 8. Research That Cannot Compound

The artefact ignores existing references, creates overlap, and leaves no clear relationship to the rest of the research corpus.

Why this fails:

- `context/references/` should become smarter over time, not noisier.
