# Testing, Validation, and Post-Writing Verification

## Mental Dry-Run

The most efficient pre-deployment test. Read the entire personality as if you are the agent. Start a hypothetical session and walk through the first few turns:

1. **Startup.** Do you know what to read? In what order? What to summarise? What to ask?
2. **First task.** A user says "Add a new API endpoint for user preferences." Do you know what to commit? When to parallelise? What to update afterward?
3. **Mid-session.** You are 30 turns in on a multi-phase plan. Do you know when to commit? Do you feel compelled to update documentation? Would you parallelise the next two independent steps?
4. **Edge case.** The user asks for something that partially overlaps with a skill. Do you know whether to handle it inline or invoke the skill? Do you know how to ask?

If any answer is unclear, the personality has a gap.

## Scenario Testing

Walk through specific scenarios designed to test known failure modes:

| Scenario | Tests | What to Watch For |
|----------|-------|-------------------|
| Multi-phase plan (5 phases, each producing files) | Version control, instruction persistence | Does the agent commit between phases? Or only at the end? |
| 14 independent files to create | Parallelisation | Does the agent create them in parallel? Or sequentially? |
| Broad refactoring across 8 files | Documentation upkeep | Does the agent update documentation afterward? Or skip because "refactoring" was not a listed trigger? |
| Binary decision (do X or do not do X) | Decision support, 3-option anchoring | Does the agent present 2 options? Or pad to 3? |
| User approves low-quality output | Instruction persistence, quality standards | Does the agent lower its standards in subsequent output? Or maintain personality-defined quality? |
| Trivial file edit | Autonomy, confirm-everything paralysis | Does the agent just do it? Or ask permission? |
| Accumulated drift over many small changes | Skill invocation threshold | Does the agent recommend a skill pass? Or keep making inline edits past the point of effectiveness? |
| Long-horizon task with non-mechanical obligation (research + test writing) | Tool-action asymmetry, sycophantic self-eval | Does the agent complete WebSearch and test-writing obligations, or satisfice and self-certify? |

## First-Session Signals

When deploying a personality for the first time, watch for these signals:

**Positive signals:**
- Agent follows the startup routine without prompting
- Agent commits at natural boundaries without being asked
- Agent parallelises when work is independent
- Agent captures notes without being asked
- Agent distinguishes inline edits from skill-worthy passes
- Agent asks permission only for the named hard constraints
- Agent produces the obligation audit before declaring done (if obligation-audit is in the operating loop)

**Negative signals:**
- Agent asks "Should I proceed?" after trivial actions
- Agent serialises independent work
- Agent does not commit until the user asks
- Agent does not update documentation after making changes
- Agent presents exactly 3 options for every decision
- Agent includes how-to detail that belongs in skills
- Agent declares complete while having skipped non-mechanical obligations (the V14 pattern)

## Regression Testing

After changing a personality, check:

1. **Did existing behaviours break?** Read the diff and identify any instruction that was removed or reworded. Verify the behaviour it produced is still produced by the new version.
2. **Did instruction count increase beyond budget?** Count the approximate instructions. If the personality grew substantially, verify nothing was added that belongs in a skill.
3. **Was a scenario-list anti-pattern introduced?** Search for new lists of specific situations where a behaviour should apply. Rewrite as principle + exception.
4. **Did emphasis inflate?** Count ALWAYS/NEVER/MUST/CRITICAL in caps. If the count increased, verify the new emphatic instructions are genuinely inviolable.
5. **Did the shared sections drift from other variants?** If multiple personality variants exist, verify the changed file is still aligned with the others on shared content.
6. **Did urgency framings creep in?** Search for efficiency language that triggers Sonnet 4.5 context anxiety.
7. **Did exhortations replace obligations?** Search for new adverbs and modal exhortations that should be verifiable obligations.

## Post-Writing Verification Checks

After writing or editing a personality file, verify these dimensions.

### Scope Check

- For each instruction, ask: "Does this belong in the personality (when/what) or in a skill (how)?" Move detailed procedural instructions to the relevant skill.
- Check that the personality does not duplicate instructions that already exist in skills. Duplication creates drift risk — when the skill is updated, the personality's copy becomes stale.

### Consistency Check

- Read the personality alongside every skill it references. Do they agree on terminology, folder structure, philosophical stance, and formatting expectations?
- Check that the skill ecosystem section accurately reflects what each skill actually does.

### Framing Check

- Search for negative prohibitions. Can they be reframed as positive instructions with reasoning?
- Search for rigid phrasing ("exactly this question," "always do X," "never do Y"). Is the rigidity justified, or would flexibility produce better results?
- Verify that every constraint includes reasoning — not just what the rule is, but why it exists.

### Scenario-List Check

- Search for instructions that list specific situations when a behaviour should apply. For each one, ask: "Would the agent apply this behaviour in a novel situation not on the list?" If no, rewrite as principle + exception.

### Persistence Check

- Are the most critical instructions placed early (primacy effect) and late (recency effect)?
- Are there instructions in the moderate-persistence zone (middle of the file) without structural reinforcement? If so, add reinforcement via the operating loop or note-taking.

### Emphasis Check

- Count ALWAYS/NEVER/MUST/CRITICAL in capitalised form. Is the count below 5? If not, identify which emphatic instructions are genuinely inviolable and normalise the rest.

### Budget Check

- Is the personality as short as it can be while retaining all genuinely personality-level instructions?
- Could any section be offloaded to a skill that loads on demand instead of every session?
- Does every line pass the test: "Would removing this cause the agent to make mistakes?"

### Multi-Variant Check (if applicable)

- Are shared sections aligned across all personality variants?
- Has the change been applied to all variants where it applies?
- Do the variants still differ only in the dimensions that justified the split?

### Exhortation-vs-Obligation Check (added 2026-04-18)

- Search the personality for adverbs: *thoroughly, carefully, actively, honestly, properly, diligently*. Each is a candidate for rewriting as a verifiable obligation.
- Search for modal exhortations: *always, never, must, should* without an evidence test. Each should either be a hard rule with structural justification, or rewritten.
- Acid test: can a third party look at the agent's trace and say "yes, the agent did X" or "no, it didn't"? If not, the instruction is exhortation.

### Urgency / Context-Anxiety Check (added 2026-04-18)

- Search for efficiency language: *"be concise", "wrap up", "quickly", "don't waste", "minimise tokens"*. Each triggers Sonnet 4.5 context anxiety. Remove or soften.
- Consider adding explicit reassurance on long tasks: *"You are not running low on context. Do not speed up or skip work because you think you are."*

### Structural-Defence Check (added 2026-04-18)

- Is there an operating loop? Does it include grounding + verification + upkeep?
- Is there a recitation / plan-file mechanism?
- Is there a pre-completion obligation audit (structural, not optional)?
- Is the tool-action asymmetry bias named explicitly?
- Are edge-placement rules stated and followed?

### Scoring Check

- Score the personality against the rubric in [19-scoring-rubric.md](19-scoring-rubric.md). Any dimension scoring Weak should be addressed before deployment.
