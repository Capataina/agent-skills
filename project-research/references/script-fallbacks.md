# Script Fallbacks

The skill's scripts are mandatory parts of the workflow, not optional conveniences. When a script cannot run, the step itself does not become optional — only the automation does. This file defines what to do in each fallback case.

## Principle

Script failure is not a reason to skip a step. It is a reason to document the failure, perform the step manually, and surface the fact in the handoff so the reader knows what automated protection was bypassed.

The phrase "I could not run the script, so I skipped the check" is never an acceptable outcome. The acceptable outcome is: "The script failed with [specific error]; I performed [specific manual steps] that replicate its intent; here is what I found."

## Fallback For `init_research_artifact.py`

Expected role: scaffold the target file or folder inside `context/references/` with the required section headings.

If the script fails:

1. Record the exact command you ran and the error output. Include both in the response or artefact handoff.
2. Create the target directory manually — for a single-paper artefact, the `.md` file at the right path under `context/references/`; for a topic folder, the directory plus an `overview.md` inside it.
3. Copy the current required section headings into the new file manually. The required sections are the same as those the script would have produced — check SKILL.md and the current `FILE_TEMPLATE` / `OVERVIEW_TEMPLATE` to avoid drift.
4. Proceed with the research and writing as normal.
5. In the completion report, state explicitly that scaffolding was performed manually and list which scaffolding steps were replicated.

Do not silently skip scaffolding. Do not write the artefact without the required headings.

## Fallback For `validate_research_artifact.py`

Expected role: verify that the completed artefact contains the required headings, required research-signal columns, required obligation-audit block, and any other structural checks the hardened validator performs.

If the script fails:

1. Record the exact command and the error.
2. Walk the artefact manually, checking each required structural element. At minimum, verify:
   - the required section headings are present,
   - the Research Signal table is present with all required columns,
   - the External Research Trail section is present and populated with actual queries, URLs, and quoted passages,
   - the Pre-Completion Obligation Audit is present and every row has concrete evidence,
   - the "What I Did Not Do" block is present.
3. Write down, in the handoff, each check you performed manually and the result of each.
4. If any hard-failure-equivalent issue is found during manual walking, fix it before presenting the artefact — exactly as you would have if the script had flagged it.
5. In the completion report, state explicitly that validation was performed manually and list each check that was replicated.

## What Is Never Acceptable

- silently skipping either script,
- running neither script and not mentioning it,
- running a script, ignoring its hard failures, and presenting the artefact anyway,
- claiming "genuine fallback was needed" without specifying what went wrong and what manual work replaced it.

The scripts exist to catch the kinds of drift that are easy to miss under cognitive load. If they cannot run, that drift is now your personal responsibility to prevent. State that responsibility explicitly in the handoff.
