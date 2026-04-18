# Example Design

## The Overfitting Risk

Examples are the single strongest influence on agent output — and the single biggest source of unintentional bias. They carry the risk of overfitting: the agent copies the surface pattern of the example rather than understanding the underlying principle. This is especially dangerous when:

- All examples look similar (the agent learns the superficial format, not the underlying reasoning).
- Examples are domain-specific (the agent applies the domain to unrelated projects).
- Examples are too detailed (the agent treats specifics as requirements).

## How Examples Actually Work in LLMs

The landmark paper "Rethinking the Role of Demonstrations" (Min et al., EMNLP 2022) demonstrated that what examples primarily teach is **format, distribution, and label space** — not content. Ground truth labels barely matter. What matters is the surface structure, vocabulary, and domain of the examples.

Research on **induction heads** (Olsson et al., 2022) presents evidence that attention mechanisms implement a pattern-completion circuit (`[A][B]...[A] -> [B]`) — the model copies previous patterns for next-token prediction rather than extracting underlying principles. While this mechanism is robustly demonstrated in small models, the evidence for large models is correlational rather than causal. The practical implication holds regardless: models replicate the surface patterns of their examples.

This means: the domain, structure, length, tone, and vocabulary of your examples will be replicated in the agent's output, regardless of whether those properties are relevant to the current task. Example design is not about showing correct answers — it is about shaping the distribution of outputs.

## Example Design Principles

1. **Use diverse examples.** Vary scenarios, input types, complexity levels, and domains. If the skill will be used across Rust, Python, TypeScript, and Go projects, include examples from multiple languages.

2. **Include rejected examples.** Show a finding that *looked* good but was rejected, and explain why. This teaches the agent the decision boundary, not just the positive space.

3. **Vary content, not just structure.** If every example has the same number of sections, the same tone, and the same depth, the agent will replicate that uniformity. Vary these dimensions to show the range of acceptable output.

4. **3-5 examples is optimal.** Research shows major gains after 2 examples, a plateau around 4-5, and diminishing returns beyond that. More examples burn tokens without improving output.

5. **Frame examples as illustrations, not templates.** "Here is an example of a good finding. Note how the justification connects the research to the specific code." This guides attention to the *principle* the example demonstrates, not the surface format.

6. **Keep examples generic or clearly hypothetical.** If an example references a specific technology, the agent may anchor on that technology when working on unrelated projects. Use examples that teach the format and reasoning without implying a specific domain.

## Worked Comparison: Weak vs. Strong Example Sets

**Weak example set (for a code health audit skill):**

Three examples, all from a machine learning project:
- "Unused TensorFlow import in training pipeline"
- "Hardcoded learning rate in model.py"
- "Dead replay buffer class in agent.py"

**What goes wrong:** The agent auditing a web application looks for ML-specific patterns. It anchors on "training pipeline," "model," and "agent" as concept categories. It may miss web-specific opportunities (unused middleware, hardcoded API endpoints, dead route handlers) because its example-shaped understanding does not include them.

**Strong example set (for a code health audit skill):**

Five examples spanning domains:
- "Unused database connection pool in a Go web service" (backend)
- "Hardcoded retry interval in a Python data pipeline" (data engineering)
- "Dead physics collision handler in a Rust game engine" (game dev)
- "Rejected finding: apparent dead code that is actually called via reflection" (boundary case)
- "Unreachable error branch in a TypeScript CLI tool" (CLI)

**What goes right:** The agent encounters any type of project and can generalise from the principles demonstrated across domains. The rejected example teaches the boundary between dead code and dynamically-invoked code, preventing false positives.
