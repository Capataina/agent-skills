# Communication Style

## Controlling Verbosity

Be explicit about when different verbosity levels apply:

- **In chat:** Direct, concise, technically rigorous. Do not pad responses.
- **In files:** Thorough, comprehensive, richly formatted. Depth is a virtue.

This distinction is critical. If you just say "be concise," the agent will be concise everywhere — including in context files and learning material where depth is the goal. If you just say "be thorough," the agent will write three paragraphs of chat response where one sentence would do.

The personality should make the boundary explicit: "These communication norms apply to chat conversation. When generating or editing files in context/, learning/, or context/references/, the Universal Output Standard governs depth and formatting — not the brevity norms below."

## Formatting and Creative Freedom

Give the agent maximum creative freedom in choosing formats, but establish the principle: use the representation that makes the information clearest. Tables for comparisons, trees for structure, diagrams for flows, bullets for takeaways. ASCII visualisations, heat maps, bar charts, class anatomy boxes — if the information has a shape, draw it.

The personality should actively encourage varied representation rather than defaulting to bullets. "Use the full expressive range of markdown and formatting. Prefer varied, rich representation over undifferentiated bullet lists when it improves understanding." This counteracts the agent's natural tendency toward bullet-list monotony.

## Adapting to the Medium

Chat interfaces may not render complex ASCII tables or diagrams well. The personality should acknowledge this: "In this chat interface, prefer clear and varied depictions, but use judgment — complex ASCII tables may not render cleanly in chat. Adapt the representation to the medium." This gives the agent permission to simplify in chat while going deep in files.

## 2026-04-18 nuance — Avoid urgency framings

Cognition documented that Claude Sonnet 4.5 exhibits context anxiety when exposed to urgency or efficiency framings. The model underestimates remaining tokens and self-compresses.

Avoid personality language like:
- "Be concise to save tokens"
- "Wrap up efficiently"
- "Minimise unnecessary prose"
- "Respect the context window"

Prefer:
- "In chat, direct responses without preamble" (structural rule, not urgency signal)
- "In files, the output standard is depth over brevity" (positive framing)
- Explicit reassurance on long tasks: *"You are not running low on context. Do not speed up or skip work because you think you are."*

See [12-failure-catalogue.md 12.10](12-failure-catalogue.md).
