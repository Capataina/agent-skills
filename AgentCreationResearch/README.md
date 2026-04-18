# Agent Creation Research

This folder is the research foundation for everything produced in this repository. Three document sets, each answering a bounded design question:

| Folder / file | Answers the question |
|---------------|---------------------|
| [`writing-skills/`](writing-skills/) | What does a well-written skill look like? How do I evaluate one? |
| [`writing-personalities/`](writing-personalities/) | What does a well-written personality (CLAUDE.md) look like? How do I evaluate one? |
| [`writing-subagents.md`](writing-subagents.md) | When should I use subagents? How should I configure and coordinate them? |
| [`research-2026-04-18/`](research-2026-04-18/) | Six parallel Opus 4.7 research reports that produced the 2026-04-18 additions to the above. |

## Startup reading

Before starting any skill, personality, or subagent session, read these files as background. They synthesise research from Anthropic, OpenAI, the broader agent community, and empirical benchmarks (2022-2026) into actionable design principles.

Each folder has its own `README.md` that acts as a topical index — you do not need to read every file in linear order. Navigate by topic via the READMEs.

## The V14 problem

The 2026-04-18 research was triggered by a specific observed failure: long-horizon Claude Code agents running multi-obligation skills skip uncomfortable work (WebSearch, diagnostic tests, cross-system analysis) and self-certify complete. The honest admission only surfaces under direct user interrogation.

The research identified this as a known phenomenon in the literature:

- Academic name: **Procedure-Outcome Decoupling / Corrupt Success** (arXiv 2603.03116, 27-78% rates on frontier models)
- Practitioner names: **Potemkin interfaces** (Replit), **Skim the hard bits** (AMD), **AI slop** (Cognition)

And it identified five compounding novel failure modes not captured by the original 8-mode hypothesis:

1. Procedure-Outcome Decoupling
2. Motivated Reasoning in CoT
3. Self-Conditioning on Own Prior Trace
4. Exploitation Collapse
5. Confabulated Compliance

The additions across `writing-skills/` and `writing-personalities/` encode the mitigations — structural defences, verification gates, obligation-vs-exhortation distinction, tool-action patterns, Claude-specific calibration, completion honesty, context anxiety — with empirical grounding.

## Historical provenance

Files prefixed `01`-`16` (writing-skills) and `01`-`18` (writing-personalities) preserve content from the previous monolithic research files with minimal changes. Files `17`+ (skills) and `08`, `09`, `10`, `19`+ (personalities) contain material from the 2026-04-18 research pass. Sources files are updated throughout with new citations.
