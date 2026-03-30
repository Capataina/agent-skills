# Operating Modes

## Table of Contents

1. [Initialise](#1-initialise)
2. [Update](#2-update)
3. [Extend](#3-extend)
4. [Audit](#4-audit)
5. [Mode Selection Rule](#mode-selection-rule)

This skill supports four operating modes. Every invocation should classify itself into exactly one primary mode before making structural decisions.

## 1. Initialise

Use when `learning/` does not exist or is too incomplete to update safely.

Goals:

- create the top-level `learning/` structure,
- establish navigation files,
- create the first set of learning paths,
- create core concept, project, exercise, and materials files,
- avoid speculative depth that is not yet justified.

Initialisation should build a strong foundation without pretending the first pass is final.

## 2. Update

Use when `learning/` exists and the project has evolved.

Goals:

- revise existing files in place where possible,
- preserve learner progress in checklist files,
- update paths and exercise order to match the current learning system,
- add current concepts or systems,
- preserve older material only when it remains educationally valuable.

This is the default mode for a mature repository.

## 3. Extend

Use when the user wants learning coverage for a specific new area without reworking the whole learning system.

Examples:

- add Redis caching coverage to a project that already documents in-memory caching,
- add an advanced topics path,
- add project-specific system exercises,
- add comparison files for a newly adopted approach.

Extension should be local, low-churn, and aware of the existing structure.

## 4. Audit

Use when the user wants a diagnosis of the current learning system rather than immediate generation.

Goals:

- identify missing learning surfaces,
- identify bad folder depth, weak navigation, stale files, or missing practice,
- identify outdated paths or broken progress tracking,
- recommend targeted improvements.

Audit mode may lead to a later update, but the mode itself is diagnosis-first.

## Mode Selection Rule

Choose the smallest mode that solves the task.

Prefer:

- `extend` over `update` when the requested change is narrow,
- `update` over `initialise` when the existing structure is strong enough to expand responsibly,
- `audit` when the user wants assessment before edits.

Do not perform a folder-wide rewrite when a narrower mode would solve the task.
