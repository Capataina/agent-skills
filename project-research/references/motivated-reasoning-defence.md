# Motivated Reasoning Defence

The most dangerous failure mode of this skill is not shallow research — it is well-written reasoning about why shallow research is sufficient. This file catalogues the specific reasoning signatures that mark that failure, and defines the adversarial-sweep move that defuses it.

## Why This Matters

Motivated reasoning in this skill is systematic, not random. It consistently points one direction: toward finishing sooner, with fewer external tool calls, and with the internal inspection work reframed as complete research. Because it is well-written and plausible, it passes casual self-review. The only reliable defence is to recognise the signatures and treat them as positive evidence that the floor has not been met.

## Signature Phrases To Watch For

If any of the following sentences (or close paraphrases) appear in your reasoning, pause. Do not continue until you have either performed additional external research or explicitly documented why the signature does not apply.

- "The initial search answered the question."
- "Additional sources would be redundant."
- "The repository context is sufficient grounding."
- "This is a simple topic; deep research would be over-engineering."
- "The authoritative source is already in my training data."
- "I already know the trade-offs here."
- "The answer is obvious once the project context is clear."
- "One strong source is enough for a topic this narrow."
- "The existing `context/` note already covers this."
- "Running more searches would just surface the same material."

Each of these is a rationalisation pattern, not a conclusion. They all serve the same function: they justify not calling `WebSearch` or `WebFetch` again.

## The Treatment Rule

Treat any sentence matching these signatures, whether written down or merely formed, as **direct evidence** that the tool-call floor has not been met. Not as a conclusion to evaluate — as a trigger to act.

Corrective actions, in order of preference:

1. Run a `WebSearch` with a query you have not yet used.
2. Run a `WebFetch` on a primary source (foundational paper, official documentation, strong reference implementation) that you have seen cited but not retrieved.
3. Identify one view that limits or disagrees with the emerging recommendation and search for it specifically.
4. Only after performing 1–3, reconsider whether the reasoning was actually correct.

## Adversarial Sweep Before Completion

Before declaring an artefact complete, perform an adversarial sweep.

Adopt a skeptical-reviewer persona:

> A reviewer who suspects I skipped the hard parts — what would they look for?

Write down, briefly, what that reviewer would flag. Typical things a reviewer catches:

- zero quoted passages from primary sources,
- no `WebFetch` calls against official documentation or foundational papers,
- every source cited agrees with the main recommendation,
- no "when this approach fails" material,
- alternatives section is absent or perfunctory,
- recommendations are not tied to specific code or `context/` references,
- depth words ("substantial", "broad", "deep") used without specific sources backing them.

Then **perform the actions that would satisfy the reviewer.** Do not merely acknowledge the gaps. The point of the sweep is to trigger the tool calls that remove them.

## Interaction With The Tool-Call Floor

The floor (3+ `WebSearch`, 3+ `WebFetch`, at least one contrasting source, at least one direct quote per major source-backed claim) is the floor precisely because motivated reasoning reliably attacks exhortation-style standards like "do enough research." Motivated reasoning cannot argue its way past a counted floor. If the floor is unmet, the work is incomplete, regardless of how the reasoning reads.
