# Code Inspection Protocol

## Table of Contents

1. [Why This File Exists](#why-this-file-exists)
2. [When Code Inspection Is Required](#when-code-inspection-is-required)
3. [When Code Inspection Is Optional](#when-code-inspection-is-optional)
4. [What Code Inspection Means Here](#what-code-inspection-means-here)
5. [Depth: Spot-Check, Not Reverse-Engineer](#depth-spot-check-not-reverse-engineer)
6. [Verification Checklist Output](#verification-checklist-output)
7. [Failure Mode: The Unverified Claim](#failure-mode-the-unverified-claim)
8. [Integration With The Execution Workflow](#integration-with-the-execution-workflow)

## Why This File Exists

`upkeep-learning` is comfortable with reading and writing markdown. That comfort is an asymmetry. Glob, Grep, and opening code files in an unfamiliar repository carry lower pretraining support for this skill than editing prose, so the agent tends to route around them. The result is teaching content that asserts things about the code — "the retrieval system uses a dense HNSW index", "the auth flow issues a refresh token in this middleware" — without ever opening the code to check.

Archive material that cannot be traced back to something real in the repository is a hallucination risk. The teaching file may be internally coherent and still wrong about the project. This file defines the minimum investigation bar.

The rule: if a teaching file makes claims about implementation, those claims must be grounded in either `context/` (which is the maintained implementation memory) or in direct code inspection. When the claim is specific enough that `context/` alone cannot confirm it, inspect the code.

## When Code Inspection Is Required

Inspect the code when:

- verifying an implementation claim (the archive says X is implemented; confirm it is);
- understanding system architecture before teaching it (module layout, boundaries, entry points);
- confirming a feature is implemented rather than planned (the README and context both mention it, but neither makes the state unambiguous);
- identifying real file locations, so worked examples and cross-links point to paths that actually exist;
- grounding a worked example (the example should match the code's real shape, not a plausible-sounding substitute);
- resolving a conflict between `context/` and the `README`;
- teaching a project system file in `project/systems/` — these must be grounded in how the system is actually built;
- writing a project-specific exercise that reconstructs, debugs, or extends a real mechanism — the exercise must reflect the real shape of that mechanism.

## When Code Inspection Is Optional

Inspection is optional — not forbidden, just not required — when the topic is:

- foundational domain theory that exists independently of this project (the maths, the canonical algorithms, the standard patterns);
- hypothetical or illustrative exercises that are not reconstructing a real project mechanism;
- paths, navigation, study guides, and glossary entries that describe the archive itself;
- explicitly README-defined future direction that has no code yet (label it as planned and teach the theory; do not fabricate implementation detail).

## What Code Inspection Means Here

Code inspection in this skill is a spot-check, not an excavation. The expected pattern is:

1. **Locate** — use `Glob` or `Grep` to find the relevant files. Queries should target specific symbols, filenames, or domain terms, not broad topic sweeps.
2. **Sample** — read one to three files per component. Read only the sections needed to confirm or refute the claim.
3. **Verify** — confirm or refute the specific claim being made. Record the outcome in one sentence.
4. **Flag** — if the code is ambiguous or the inspection was shallow, flag uncertainty rather than hiding it.

This is verification, not reverse-engineering. You are not trying to re-derive the system; you are checking that what you already intend to teach matches what is actually there.

## Depth: Spot-Check, Not Reverse-Engineer

Budget roughly one to five minutes per claim. If a claim takes longer than that to verify, that is a signal:

- the claim is probably too specific for the archive to make confidently,
- the system may be poorly understood and deserves its own deep-dive instead of a passing assertion,
- or the archive should label the claim as uncertain rather than confident.

Do not let a single claim swallow the inspection budget. Spread checks across the system surfaces being taught.

## Verification Checklist Output

Every pass that includes implementation-facing teaching must emit a short inspection record inside the Completeness Audit. For each inspection, record:

- **files inspected** (paths, relative to repo root);
- **claims verified** (one sentence per claim: "confirmed", "refuted", or "ambiguous");
- **uncertainties flagged** (anything the inspection could not settle, and how the archive handles that uncertainty — e.g., labelled as planned, softened, or cross-referenced to `context/`).

A pass with zero code inspections while teaching implementation-facing content is structurally incomplete. Aim to verify at least five implementation claims across the pass; more when the pass touches `project/systems/`, `project/architecture/`, or project-specific exercises.

## Failure Mode: The Unverified Claim

The characteristic failure is not a hallucinated claim — it is an unverified claim that happens to be plausible. The file reads well, the section flows, the worked example looks right, and nobody opened the code. Months later, a learner discovers the example does not correspond to anything in the repository.

Prevent this by naming the claim before you write it ("this file will assert that the retrieval pipeline uses HNSW with cosine similarity") and deciding in advance where that claim will be grounded (context file? code file? README section?). If the grounding path does not exist, you have a research problem to solve before you write the teaching file, not after.

## Integration With The Execution Workflow

The `SKILL.md` Execution Workflow calls this protocol explicitly at the code-inspection step. The protocol also applies implicitly anywhere the archive teaches specific implementation behaviour — do not wait for the workflow step to prompt inspection if you are already writing a claim that needs grounding.

When in doubt, inspect. A teaching archive loses more from confidently wrong content than from verification overhead.
