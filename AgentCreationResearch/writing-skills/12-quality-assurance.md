# Quality Assurance Design

## The Role of Quality Checklists

Quality checklists at the end of a skill serve two distinct purposes:

1. **Verification:** The agent uses them to check its own output before presenting it.
2. **Recency anchoring:** Items at the end of the skill body receive strong attention due to the primacy-recency effect. The quality checklist is the last thing the agent reads in SKILL.md, making it the most salient set of requirements during output generation.

This dual role means the checklist is not just a final check — it actively shapes the agent's output priorities. Items in the checklist receive disproportionate attention. Use this strategically: the most important quality requirements belong in the checklist.

## Writing Verifiable Checklist Items

Every checklist item must be concrete and verifiable by the agent itself. The test: could the agent read this item and unambiguously answer "yes" or "no" about its own output?

| Weak (unverifiable) | Strong (verifiable) |
|---------------------|---------------------|
| Is the output good? | Every finding includes the full proof chain: current state, proposed change, justification, expected benefit. |
| Are the examples diverse enough? | Examples span at least 3 different project domains and include at least one rejected example demonstrating a decision boundary. |
| Is the format consistent? | Every output file uses the same heading hierarchy, finding template structure, and severity labelling scheme. |
| Did I check everything? | Every file in the repository's `src/` directory has been read and analysed. No directories were skipped. |
| Is the depth appropriate? | Every finding's justification references specific code (file path + function/line) rather than general assertions about what the code "probably" does. |

## Checklist Design Principles

- **Do not duplicate the instructions.** The checklist confirms that the instructions were followed; it does not restate them. If the checklist item is a direct copy of an instruction from earlier in SKILL.md, it wastes tokens and dilutes attention.

- **Keep the checklist proportionate.** A simple skill needs 5-8 items. A complex skill might need 12-15. Beyond 15, attention dilutes and the agent starts omitting items (IFScale saturation effect).

- **Order by importance.** The agent attends most to the first and last items in a list. Place the most critical quality requirements at the top and bottom of the checklist.

- **Make items independent.** Each item should be evaluable on its own, without reference to other items. Dependent items ("Did I do X? If yes, did I also do Y?") should be merged into one item.

## The Obligation Checklist vs Quality Rubric Distinction (2026-04-18 addition)

There are two distinct checklist patterns, and skills with reliability obligations need both — with the obligation checklist dominating.

**Quality rubric items** measure *how good* the output is. They are subjective, scaled, and evaluatable only by judgement. "Is the justification clear?" is a quality rubric item.

**Obligation checklist items** measure *whether* each required action happened. They are objective, binary, and evaluatable by evidence. "Did the agent call WebSearch and cite at least one source per system?" is an obligation checklist item.

RULERS research (arXiv 2601.08654) shows evidence-anchored scoring — where each rubric item has a required evidence slot — is measurably more stable against adversarial rubric perturbation than prompt-phrasing-based rubrics. Smaller models using evidence-anchored rubrics rival larger-model judges using subjective rubrics.

The research backing the obligation-checklist pattern:
- Sycophantic self-scoring (SycEval, 78.5% persistence) — subjective rubrics inflate.
- Iterative self-refinement (arXiv 2407.04549) — "now review" actively degrades.
- Self-Report Fine-Tuning (arXiv 2511.06626) — 770 samples moves hidden-objective F1 from 0.00 to 0.98. In-context analog: heavy example-based framing of honest admission.

**Rule:** A skill's completion checklist should be majority obligation-items, not majority quality-items. Obligations first, quality last.

## Component-Specific Evaluation Criteria

Different components of a skill require different evaluation approaches:

**Evaluating a description:**
- Does it activate for every reasonable phrasing of the skill's core use case?
- Does it NOT activate for adjacent skills' use cases?
- Is it dense with trigger terms? Count the unique trigger phrases — fewer than 5 is usually too sparse.
- Is it under 1024 characters?
- Is it written in third person?

**Evaluating a reference file:**
- Does it have a table of contents (if over 100 lines)?
- Does it cover one coherent topic?
- Does it explain *why* behind every major instruction?
- Does it include diverse examples (if applicable)?
- Does it avoid pointing to other reference files?
- Is the depth proportionate to the judgement involved, variation across projects, and cost of mistakes?
- Does it contain imperatives? If yes, consider promoting them to SKILL.md body (see F13).

**Evaluating a quality checklist:**
- Is every item verifiable by the agent (yes/no answer)?
- Are items independent of each other?
- Is the count proportionate (5-15 items)?
- Do the most critical items appear at the top and bottom?
- Does the checklist avoid duplicating instructions from the body?
- Is the balance of obligation-items to quality-items appropriate for the skill's reliability requirements?

**Evaluating a template:**
- Does every section have an intent description (not just a label)?
- Are worked examples varied in depth and complexity?
- Is the template framed as minimum structure, not maximum?

**Evaluating an example set:**
- Do examples span at least 2-3 domains?
- Is there at least one rejected example showing a decision boundary?
- Do examples vary in complexity and depth?
- Are examples framed as illustrations of principles, not templates to copy?
- Do all examples avoid anchoring on a single cardinality?
