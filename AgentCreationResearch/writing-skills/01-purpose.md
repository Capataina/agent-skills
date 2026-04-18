# Purpose of This Document Set

This folder answers one question comprehensively: **what does a well-written skill look like at every level of detail?**

This is not a process document. It does not describe the steps for creating a skill (that lives in the project's CLAUDE.md). It describes what makes a skill well-written, how to evaluate one, what patterns to follow, what failures to avoid, and how to test quality.

## Use this reference to

- Identify whether a description will trigger correctly in edge cases
- Evaluate whether instructions are worded for generalisation or rote compliance
- Detect domain bias, terminology drift, instruction contradictions, and structural violations
- Score a skill across quality dimensions with concrete, observable criteria
- Design a test plan for validating a skill before deployment

## How this folder is organised

The folder is organised topically. Each file answers a bounded question. You do not need to read the whole folder for any single evaluation — navigate via the README to the topics relevant to your current task.

The folder is long by design. It is a reference.

## Provenance

This document set was restructured from a single 1251-line monolith on 2026-04-18, informed by six parallel Opus 4.7 research passes investigating why long-horizon agents skip hard work on multi-obligation skills. The research artefacts live in `AgentCreationResearch/research-2026-04-18/`.

Files prefixed `01`-`17` are migrated from the original monolith (content preserved verbatim). Files prefixed `18`+ are new, added from the 2026-04-18 research. The `README.md` is an index.
