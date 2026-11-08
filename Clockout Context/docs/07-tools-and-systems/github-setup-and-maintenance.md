# Git setup and maintenance
The predecessor repository was set up on 2026-10-30. Routine updates to ClockoutHQ follow the authorization rules in AGENTS.md.

## Exact layout
The active Git root is `/Users/forex/ClockoutHQ`. This documentation root is `Clockout Context/docs/` inside it. Preserve the existing layout and single Git repository.

The active remote is `donovinsims/clockouthq`, branch `main`. Authenticated GitHub metadata reported PRIVATE on 2026-11-07 (W05). Keep local tool state and private records out of Git. Client production repositories are separate.

## Historical predecessor setup — 2026-10-30

These commands document the completed predecessor setup.
~~~sh
cd /Users/forex/Clockout-Context-Files-MASTER-2026-10-29
git init -b main
git add .gitignore README.md docs
git diff --cached --stat
git diff --cached
git commit -m "docs: establish Clockout source of truth"
gh repo create donovinsims/clockout-knowledge-base --private --source=. --remote=origin
gh repo view donovinsims/clockout-knowledge-base --json isPrivate,visibility,url
git push -u origin main
~~~
Visibility was confirmed **PRIVATE** through the GitHub API before the push, not merely from the creation command. This describes the October 30 creation only; it is not proof of current visibility. No repository is being created in this update. An existing repository is inspected before any decision, and a duplicate is never created. Source: [official CLI manual](https://cli.github.com/manual/gh_repo_create), W01.

## The five states of a change
Nothing here happens automatically. GitHub does not mirror your edits.

| State | What it means | How to see it |
|---|---|---|
| **Locally edited** | The file changed on this Mac. No version is recorded yet. | `git status`, `git diff` |
| **Staged** | The change is selected for the next commit. Still local. | `git diff --cached` |
| **Committed** | A snapshot with a message exists in this Mac's history. Still not uploaded. | `git log --oneline` |
| **Pushed** | The commit exists on the configured GitHub remote. | `git log origin/main --oneline` |
| **Synchronized** | Local `main` and `origin/main` point at the same commit and the tree is clean. | `git status`, `git fetch` then compare |

A file edit that has not been committed and pushed exists only on this Mac.

## Daily loop
Run from the active repository root.

~~~sh
cd /Users/forex/ClockoutHQ
git status                      # what changed, what is staged
git diff                        # read the actual change
~~~

Review the content, then record it deliberately:

~~~sh
git add "Clockout Context/docs/CURRENT_STATE.md" "Clockout Context/docs/CHANGELOG.md"   # only the files you reviewed
git diff --cached                                 # final check before recording
git commit -m "docs: reconcile verified sprint results"
git push
git status                                        # expect "up to date" and a clean tree
~~~

Prefer explicit `git add <path>` over `git add .` so an unexpected export, archive or private file is never swept in. Paths are listed relative to the repository root, so these documentation files take the `Clockout Context/docs/` prefix.

## Open, inspect, and pull
Open the repository folder itself in Codex/OpenCode/VS Code; the agent then sees `Clockout Context/docs/` within the consolidated workspace. Before resuming, check whether the remote moved:

~~~sh
git fetch origin
git status                    # reports ahead/behind
git pull --ff-only            # only when there are no local edits
~~~

`--ff-only` refuses to invent a merge. If it refuses, you have local work or divergent history: stop, read `git status`, and decide deliberately. Never pull blindly over uncommitted edits and never force-push to resolve a difference.

## Recovering an earlier version
A committed version is always recoverable, which is the main reason to commit.

~~~sh
git log --oneline -- "Clockout Context/docs/CURRENT_STATE.md"
git show "<commit>:Clockout Context/docs/CURRENT_STATE.md"
git restore --source=<commit> -- "Clockout Context/docs/CURRENT_STATE.md"
~~~

`git restore` overwrites the working copy of that one file. Commit the restore as a new change; do not rewrite published history to pretend the later version never existed. An uncommitted edit has no history and cannot be recovered by Git.

## When edits conflict
A conflict means the same lines changed in two places. Git marks the file; it does not choose.

1. Run `git status` to list the conflicted files.
2. Open each file and read both sides of the `<<<<<<<` / `=======` / `>>>>>>>` markers.
3. Resolve using business evidence, not convenience: read CURRENT_STATE, the canonical topic file and the source register.
4. Remove the markers, keep the correct text, then `git add` the resolved files and commit.
5. If the correct answer is genuinely unclear, stop and record the conflict in `09-execution-and-decisions/contradictions.md` instead of guessing.

Never resolve a conflict with `git checkout --ours/--theirs` on whole files, `git reset --hard`, or a force-push. Those discard someone's work, and the lost side may be the accurate one.

## Working safely across several AI agents
- One canonical copy, one repository. Do not clone a second copy inside the parent folder and do not let an agent re-initialize Git.
- Agents read in this order: AGENTS.md → CURRENT_STATE.md → CHECKPOINT.md (when resuming) → the canonical topic file → OPEN_DECISIONS.md → source extracts only when needed.
- `git status` before and after every agent session. If an agent reports work but the tree is clean, the work was not saved.
- One agent writes at a time. Two agents editing the same file produce conflicts that are cheap to avoid and expensive to reconcile.
- CHECKPOINT.md is the only handoff record. Do not create a second checkpoint, a second decision register or a competing "source of truth" folder.
- An agent's summary is not verification. Confirm the file changed and the claims are sourced before committing.

## After a major business decision
1. Record the decision, date, source and confidence in the canonical file.
2. Update CURRENT_STATE if priority or status changed.
3. Update OPEN_DECISIONS if an item was resolved, added or re-scoped.
4. Append CHANGELOG; preserve the superseded intent in history rather than overwriting it.
5. Update CHECKPOINT if the resume state changed.
6. Run the validator from `Clockout Context/docs/` and review the diff.
7. Regenerate SHA256SUMS after the content is final, rerun the validator, then commit and push under the applicable authorization.

~~~sh
cd docs
python3 10-reference-and-archive/validate_master.py
cd ..
git diff --check
git status
~~~

## Recovery and history rules
When a fast-forward or push fails, preserve local work, inspect the incoming history and reconcile the facts. Do not force-push, reset, clean or delete a branch to hide a conflict. Correct a business fact with a sourced edit, a dated history/changelog entry and a new reviewed commit; do not rewrite historical decisions.

`.gitignore` does not remove a file that is already tracked, and it is not a secret detector. If real exposure occurs, treat it as a credential incident: rotate the credential, then plan an authorized history remediation. Deleting the file in a new commit leaves it in history.

Never: force-push, rewrite published history, commit credentials, push sensitive material to a public remote, delete historical records, or overwrite a newer document with an older one.

## Backup and meaning
Keep the dated ZIP and an independent backup as appropriate. Review access periodically. Git history records edits; it does not prove cleared funds, site publication, profile verification or business outcomes. A remote is not automatic backup.

## Historical predecessor handoff — 2026-11-02

Initial setup is complete (OD14 closed). Authenticated GitHub metadata reported PUBLIC visibility for the predecessor, default branch main and ADMIN permission. The clean local checkout was fast-forwarded from 6d6836d to remote 0a3d45f, preserving the $500 offer changes. This update is prepared locally; Donovin paused the push and requested no visibility change. The commands in the maintenance loop are guidance, not authorization to override that pause. Recheck current remote state and applicable owner authorization before a future push. See [verification evidence](../10-reference-and-archive/CORE_WORKFLOW_VERIFICATION.md).
