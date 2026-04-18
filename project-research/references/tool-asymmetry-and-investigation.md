# Tool Asymmetry And Investigation

This skill exists on a tool-action boundary where the agent's pretraining strongly biases it away from the actions the skill most needs. Naming the bias is the first line of defence against it.

## The Asymmetry

For this skill, tools split into two groups:

**High-pretraining-support tools (comfortable, over-used):**

- `Read` — reading files in the repository,
- `Grep` / `Glob` — searching within the codebase,
- `Bash` — running local scripts and inspection commands.

These tools feel natural. Your pretraining corpus contains an enormous volume of sessions where reading and grepping code is the right answer. The model is calibrated to reach for them first.

**Low-pretraining-support tools (uncomfortable, under-used — and yet the investigative surface of this skill):**

- `WebSearch` — external search for topic-specific queries,
- `WebFetch` — retrieval of primary sources, papers, documentation, reference implementations.

These tools are less frequent in pretraining, less consistently rewarded in post-training, and feel further from the "read the code" default. The model is calibrated to avoid them when it can rationalise that enough information is already in context.

That calibration is wrong for this skill. This skill is not a code reader. It is an external-research engine that starts from repository reality. If you skip the external surface, you have not done the skill.

## The Pull And What To Do About It

You will feel pulled toward reasoning like:

- "I have read `context/` and the source; I have enough."
- "The question is simple and I already know the answer."
- "Additional sources would only confirm what I have."
- "The authoritative source is already in my training data."
- "External research here would be over-engineering."

**That pull is a pretraining artefact, not a judgement.** It arises from the same bias that under-rewards `WebSearch` and `WebFetch` in post-training — not from a genuine assessment that research is unnecessary.

**The rule:** The moment you notice yourself drafting reasoning about why you do not need more external sources, treat that reasoning as direct evidence that you should call `WebSearch` or `WebFetch` immediately. The reasoning is the symptom. The tool call is the treatment.

## Budget Inversion

Because the bias is systematic, budget inversion is the correction:

- When unsure whether to run another `WebSearch`, run it.
- When unsure whether to `WebFetch` a primary source you have only seen cited, fetch it.
- When unsure whether you have read enough of the codebase to speak about it, you have almost certainly already read enough — move to external research.

The failure mode is always the same direction: too much internal reading, too little external research. Correct toward the uncomfortable surface.

## Relationship To The Tool-Call Floor

SKILL.md specifies a tool-call floor — at least 3 distinct `WebSearch` calls and at least 3 distinct `WebFetch` calls against primary sources, with quoted passages. That floor exists because the pull described above is strong enough that exhortations like "do substantial research" do not survive it. Only a counted floor does.

If you find yourself computing whether you can finish below the floor, you are inside the failure pattern described on this page.
