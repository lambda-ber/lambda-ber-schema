---
description: Project management related tasks
argument-hint: "status" | [INSTRUCTIONS]
---

# Reporting on current status

- look at open issues and PRs in this repo, identify blockers
- auto-assign unassigned issues
- check on updates in gdrive

# Team

`gh api repos/lambda-ber/lambda-ber-schema/collaborators`

# Google drive

Gdive is mirrored locally in `assets/external` (this is in .gitignore, never check in)

To refresh:

`just -f sync.justfile sync-gdrive`

Relevant files:

* `Activity 2/` --> whole folder
* `Activity 1/MX_metadata_template.xlsx` --> current focus, see #47
* `Proposal Documents`

 # Local notes

Take any notes in ./PM_TODO.md at the top of this repo
