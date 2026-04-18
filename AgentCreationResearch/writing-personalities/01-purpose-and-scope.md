# Purpose and Scope

This folder is the quality evaluation bible for agent personality files. It serves three audiences:

- **Writers** creating a new personality from scratch — use the section writing patterns, failure catalogue, and scoring rubric to produce strong output on the first pass.
- **Reviewers** evaluating an existing personality — use the scoring rubric, hard rules, and post-writing verification to identify specific weaknesses.
- **Improvers** iterating on a personality that mostly works — use the failure pattern catalogue and testing methodology to find the gaps between current and ideal behaviour.

Every claim about what works and what fails is grounded in either published research or observed practice. The sources file catalogues all references.

## What a Personality File Is

A personality file is the highest-leverage configuration point in an agent system. It shapes every interaction — how the agent reasons, what it prioritises, how it communicates, when it acts autonomously, and when it defers. It is loaded at the start of every conversation and remains in context throughout.

A personality file is NOT:

- A tutorial for the agent on how software engineering works (the agent already knows).
- A comprehensive reference manual (that is what skills are for).
- A list of every rule the agent should follow (instruction-following degrades with instruction count).
- A repository documentation file (it documents the agent's behaviour, not the codebase).

A personality file IS:

- The agent's operating charter — who it is, how it works, what it prioritises.
- The coordinator layer that connects skills, sources, and workflows.
- The place where project-specific norms and conventions are established.
- The highest-signal, most-persistent context the agent receives.

## The Hierarchy

Most agent systems support multiple personality layers:

| Level | Claude Code Location | Purpose |
|-------|---------------------|---------|
| Global | `~/.claude/CLAUDE.md` | Personal preferences across all projects |
| Project | `CLAUDE.md` in repo root | Team conventions, committed to git |
| Local | `.claude/local.md` | Personal overrides, gitignored |
| Subdirectory | `subdir/CLAUDE.md` | Directory-specific context, loaded on demand |

Project-level is the primary target for team-shared personality files. Global is for personal style preferences. Subdirectory files enable progressive disclosure in monorepos.

## Provenance of this folder

This document set was restructured from a single 1159-line monolith on 2026-04-18, informed by six parallel Opus 4.7 research passes investigating why long-horizon agents skip hard work on multi-obligation skills. The research artefacts live in `AgentCreationResearch/research-2026-04-18/`.

Files `01`-`14` are migrated from the original monolith (content preserved). Files `15`+ are new, added from the 2026-04-18 research. The `README.md` is an index.
