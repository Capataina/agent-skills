# Content Depth Standards

## Table of Contents

1. Goal
2. Comprehensive but Non-Redundant
3. Architecture Depth Expectations
4. System Document Depth Expectations
5. Evidence and Inference
6. Signs a Document Is Too Shallow
7. Signs a Document Is Overwritten

## 1. Goal

The goal is not longer files. The goal is files that contain enough grounded information to prevent immediate rediscovery from code.

## 2. Comprehensive but Non-Redundant

A strong context document should:

- cover the dimensions that matter for its role,
- be grounded in observed implementation reality,
- include enough detail to guide later work,
- avoid repeating the same fact in multiple documents as if each were canonical.

This means:

- more substance than a thin bullet summary,
- less sprawl than a prose dump that mirrors the code line by line.

## 3. Architecture Depth Expectations

`architecture.md` should usually cover:

- what the repository is and what it currently implements,
- a meaningful structure tree with important subdirectories and notable files,
- the major subsystem map,
- dependency direction between major layers,
- the main execution and data-flow pipelines,
- structural constraints or current-reality caveats that affect engineering work.

Depth should increase when:

- the repo has multiple layers or runtimes,
- there are important generated or non-source directories worth distinguishing,
- major behaviour depends on configuration or toolchain boundaries,
- different subsystems interact in non-obvious ways.

## 4. System Document Depth Expectations

A strong `systems/*.md` file should usually cover these dimensions when relevant to that subsystem:

- purpose,
- boundaries and ownership,
- current implemented behaviour,
- key interfaces or data flow,
- important artefacts or modules,
- active risks,
- partial work,
- missing or likely changes,
- durable lessons,
- obsolete assumptions.

Not every subsection needs the same density, but the document should not collapse into one-line bullets if the subsystem is materially important.

## 5. Evidence and Inference

Prefer statements grounded in direct evidence from:

- entrypoints,
- owning modules,
- configuration,
- tests,
- scripts,
- existing context that still matches the codebase.

When something is inferred:

- keep the wording cautious,
- avoid presenting the inference as verified implementation truth.

## 6. Signs a Document Is Too Shallow

Warning signs include:

- repository structure stops at superficial folder names,
- system docs name components but do not explain ownership or interfaces,
- risks and partial work are absent in a clearly evolving subsystem,
- a new reader would still need a first-pass rediscovery from code,
- every section is a flat list of short bullets with little differentiation.

## 7. Signs a Document Is Overwritten

Warning signs include:

- the document mirrors code almost line by line,
- structural sections are crowded with low-signal detail,
- multiple sections restate the same facts in slightly different wording,
- prose becomes slower to read than opening the actual source files.
