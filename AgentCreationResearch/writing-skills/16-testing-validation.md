# Testing, Validation, and Post-Writing Verification

A skill cannot be fully evaluated by reading it — it must also be tested against realistic scenarios. This file describes how to validate that a skill works as intended, and the post-writing verification passes that catch issues invisible during writing.

## Mental Dry-Run

Read the skill as if you were the agent. Walk through a hypothetical task from trigger to output:

1. **Trigger test:** Given a realistic user request, would the description activate this skill? Try 3-5 different phrasings, including informal ones ("sweep for dead code," "clean up this repo," "find unused stuff").

2. **Loading test:** Once triggered, what files would you read? Follow the loading instructions literally. Would you know which reference files to read for this specific task? Are the conditional triggers clear?

3. **Execution test:** With SKILL.md and the relevant references loaded, would you know what to do at every decision point? Where would you get stuck? Where would you need to guess?

4. **Output test:** Would you know exactly what to produce? What format? What depth? Where to put it?

5. **Quality test:** After producing output, would you know how to evaluate it? Does the quality checklist cover the most important dimensions of output quality?

**Record every point of confusion.** Each one is a gap in the skill that needs to be filled.

## Edge Case Scenarios

Test the skill against situations that push its boundaries:

| Scenario | What It Tests |
|----------|--------------|
| **Minimal input** — a one-line user request with no details. | Does the skill guide the agent on what to ask for or infer? Or does it assume rich input? |
| **Unusual project type** — a project in an uncommon language or domain. | Do the examples and instructions generalise? Or do they assume a specific stack? |
| **Ambiguous trigger** — a user request that could activate this skill or an adjacent one. | Do the negative triggers correctly prevent false activation? |
| **Large scope** — a project with hundreds of files or thousands of lines. | Does the skill handle scale? Are there instructions for prioritisation and scoping? |
| **Small scope** — a project with 3 files and 100 lines of code. | Does the skill handle minimal projects without producing empty or padded output? |
| **Mid-conversation trigger** — the skill activates after the agent has already been working on something else. | Do the instructions make sense when the agent already has context? Or do they assume a fresh conversation? |

## First-Session Signals

When a skill is used for the first time in a real session, watch for these signals:

**Positive signals (skill is working):**
- The agent triggers correctly on the first user request.
- The agent loads the appropriate reference files without prompting.
- Output follows the quality checklist without reminders.
- Output depth is proportionate to the topic's complexity.
- The agent makes good judgement calls in open-field areas.

**Warning signals (skill needs adjustment):**
- The agent asks the user which mode to use (mode-question friction — see F7).
- The agent produces output anchored on a specific domain from the examples (domain bias — see F2).
- The agent follows some instructions but ignores others (over-constraining collapse — see F8).
- The agent produces mechanically uniform output regardless of input variation (template-as-output — see F6).
- The agent does not load conditional reference files when they are clearly relevant (under-loading — see F4).
- The agent self-certifies complete but skipped non-mechanical obligations (verification-gate absence — see F10).
- The agent skipped WebSearch or diagnostic test writing obligations (tool-action asymmetry — see F12).

## Regression Signals

After changing a skill, watch for these regression indicators:

- **Trigger regression:** A phrasing that previously activated the skill no longer does (or a phrasing that didn't now does incorrectly).
- **Quality regression:** Output quality decreased in an area that was previously strong. This often happens when adding instructions — the new instructions may conflict with or dilute existing ones.
- **Instruction count regression:** The total instruction count across the skill directory increased beyond the saturation threshold. Count instructions after every change.
- **Coherence regression:** The change introduced a terminology inconsistency or instruction contradiction. Search the directory for the changed terms.

## Evaluations-First (2026-04-18 addition)

Anthropic's canonical workflow for skill authoring puts evaluations before documentation:

1. **Run baseline without the skill.** Observe specific failure modes on realistic tasks.
2. **Document the failures.** What went wrong, under what conditions, with what input?
3. **Create 3+ test scenarios** that exercise the failure modes.
4. **Write minimal instructions** that address the specific failures observed.
5. **Iterate** — re-run, compare to baseline, refine.

This workflow is load-bearing. Skills written without first running the baseline tend to over-instruct on imagined failures and under-instruct on real ones. The order matters: observations first, instructions second.

## Post-Writing Verification Checks

After writing or editing any skill, run through these verification checks. No automated tools exist for multi-file prompt coherence checking — this is entirely manual work today (the research confirms this gap). These checks catch the kinds of issues that are invisible during writing but create real problems when agents use the skill.

### Bias and Diversity Check

- Read every example, template, and worked scenario across the entire skill directory. Are they drawn from at least 2-3 different domains? Would an agent working on any type of project (web service, game, CLI tool, data pipeline, mobile app, infrastructure) find the examples relatable and non-anchoring?
- Pay special attention to template files — these have the highest contamination risk because agents use them as direct structural patterns.
- Check that example titles, file names, variable names, and function names do not anchor on one domain. `select_experiences()` anchors on ML. `process_batch()` is generic.

### Coherence Check

- Read the SKILL.md and every reference file looking for instructions that contradict each other, even subtly. A "use judgement" instruction in one place and an "always do X" instruction in another is a contradiction.
- Verify that the quality checklist at the end of SKILL.md is consistent with the instructions in the body and reference files.
- Check that the description in the YAML frontmatter accurately reflects what the skill actually does.

### Terminology Check

- List the 5-10 most important concepts in the skill. Search the entire skill directory for each one. Is the same term used consistently?
- Check terminology against other skills in the ecosystem. A concept that appears in multiple skills should use the same term everywhere.

### Reference Integrity Check

- After any structural change (file rename, folder restructure, concept reorganisation), search the entire skill directory for the old names. Every stale reference must be updated.
- Verify that every file referenced in SKILL.md's reference loading instructions actually exists with that exact filename.
- Verify that reference files do not point to other reference files (one-level-deep rule).

### Framing Check

- Search for ALWAYS, NEVER, MUST, and MUST NOT in capitals. For each one, ask: does this need to be this emphatic, or would a principle with reasoning be better?
- Search for negative instructions ("do not," "never," "avoid"). For each one, ask: is there a positive framing that teaches the same lesson?
- Verify that every major instruction includes a *why* — not just what to do, but why it matters.
- Search for scenario-list patterns (instructions with comma-separated triggering scenarios). Evaluate each for the scenario-list anti-pattern.

### Autonomy Check

- Search for numeric constraints (word counts, file counts, section counts, character limits). For each one, ask: is this structural (context engineering) or arbitrary (restricting judgement)?
- Search for prohibitions on specific sections, files, or formats. Are there legitimate scenarios where the agent should be allowed to make a different choice?
- Read the skill from the perspective of a highly capable agent: does it feel like an empowering framework or a restrictive script?
- Count total instructions across the skill directory. If the count approaches or exceeds ~100, evaluate which instructions could be converted from constraints to principles.

### Verification-Gate Check (2026-04-18 addition)

- Is there a structural gate between "agent thinks it's done" and "declared done"? At minimum, evidence-anchored quality checklist items. At best, a Stop hook or PreToolUse hook that runtime-verifies the session transcript.
- Does the skill require a "What I did not do" declaration, or at least explicitly permit it?
- Are there any quality-rubric items phrased as subjective self-rating? Each is a candidate for rewriting as an obligation-item with an evidence slot.

### Exhortation-vs-Obligation Check (2026-04-18 addition)

- Search the skill for adverbs: *thoroughly, carefully, actively, honestly*. Each is a candidate for rewriting as a verifiable obligation.
- Search for modal exhortations: *always, never, must, should* without an evidence test. Each should either be a hard rule with structural justification, or rewritten as an obligation.
- Acid test: can a third party look at the agent's trace and say "yes, the agent did X" or "no, it didn't"? If not, the instruction is exhortation, not obligation.

### Cross-Skill Check (when the skill is part of an ecosystem)

- Verify that the skill does not reference other skills by name — only artefact patterns. (Exception: within coordinated skill families with shared components, see [14-cross-skill-coherence.md](14-cross-skill-coherence.md).)
- Verify that trigger descriptions do not overlap with other skills. Include negative triggers where needed.
- Check that the skill is fully self-contained — it should not depend on the reader knowing about other skills.
- Verify terminology consistency with the ecosystem.

### Scoring Check

- Score the skill against the rubric in [15-scoring-rubric.md](15-scoring-rubric.md). Any dimension scoring 1 should be addressed before the skill is deployed.
