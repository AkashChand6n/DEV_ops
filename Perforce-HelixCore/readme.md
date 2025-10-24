# Git vs Perforce Helix Core - Command Reference Guide

A comprehensive comparison of commands between Git/GitHub and Perforce Helix Core version control systems.

---

## Getting Code

| Git | Perforce | Description |
|-----|----------|-------------|
| `git clone <url>` | `p4 client` + `p4 sync` | Get code from repository for first time |
| `git pull` | `p4 sync` | Update your local code with latest changes |
| `git fetch` | `p4 sync -n` | Preview what would be updated (without updating) |

---

## Making Changes

| Git | Perforce | Description |
|-----|----------|-------------|
| `git add <file>` | `p4 edit <file>` | Mark existing file for modification |
| `git add <newfile>` | `p4 add <file>` | Add new file to repository |
| `git rm <file>` | `p4 delete <file>` | Remove/delete a file |
| `git mv <old> <new>` | `p4 move <old> <new>` | Rename or move a file |
| `git status` | `p4 opened` | See what files you've changed |
| `git diff` | `p4 diff` | See changes in modified files |
| `git checkout -- <file>` | `p4 revert <file>` | Discard local changes to file |

---

## Saving Changes

| Git | Perforce | Description |
|-----|----------|-------------|
| `git commit -m "msg"` | `p4 change` | Prepare to save changes (create changelist) |
| `git push` | `p4 submit` | Send changes to central repository |
| `git commit -am "msg" && git push` | `p4 submit -d "msg"` | Commit all and push in one step |
| `git stash` | `p4 shelve` | Temporarily save work-in-progress |
| `git stash pop` | `p4 unshelve` | Restore shelved changes |
| `git stash list` | `p4 changes -s shelved -u <user>` | List your shelved changes |

---

## Branching & Merging

| Git | Perforce | Description |
|-----|----------|-------------|
| `git branch` | `p4 stream` or `p4 branch` | List/create branches |
| `git branch <name>` | `p4 stream -t development <name>` | Create new branch |
| `git checkout <branch>` | `p4 switch <stream>` | Switch to different branch |
| `git merge <branch>` | `p4 merge` | Merge changes from another branch |
| `git rebase <branch>` | `p4 copy` | Integrate changes (similar concept) |
| `git cherry-pick <commit>` | `p4 integrate -c <changelist>` | Apply specific change to current branch |

---

## History & Information

| Git | Perforce | Description |
|-----|----------|-------------|
| `git log` | `p4 changes` | View commit/changelist history |
| `git log <file>` | `p4 filelog <file>` | View history of specific file |
| `git blame <file>` | `p4 annotate <file>` | See who changed each line |
| `git show <commit>` | `p4 describe <changelist>` | View details of a specific change |
| `git log --oneline` | `p4 changes -m <n>` | View recent changes (limited to n) |
| `git log --author=<name>` | `p4 changes -u <user>` | View changes by specific user |

---

## Undoing Changes

| Git | Perforce | Description |
|-----|----------|-------------|
| `git checkout -- <file>` | `p4 revert <file>` | Discard local changes to file |
| `git reset HEAD <file>` | `p4 revert <file>` | Unstage file (undo add/edit) |
| `git reset --hard HEAD` | `p4 revert //...` | Discard all local changes |
| `git revert <commit>` | `p4 backout <changelist>` | Undo a submitted change |
| `git clean -fd` | `p4 clean` | Remove untracked files |

---

## Collaboration

| Git | Perforce | Description |
|-----|----------|-------------|
| `git remote -v` | `p4 info` | Show repository/server info |
| (no equivalent) | `p4 lock <file>` | Lock file to prevent others from submitting |
| (no equivalent) | `p4 unlock <file>` | Unlock a locked file |
| (no equivalent) | `p4 opened -a` | See what files others have checked out |
| `git pull --rebase` | `p4 sync` + `p4 resolve` | Update and resolve conflicts |
| (no equivalent) | `p4 reconcile` | Detect files changed without checkout |

---

## Configuration & Setup

| Git | Perforce | Description |
|-----|----------|-------------|
| `git config` | `p4 set` | Configure settings |
| `git config --global user.name` | `p4 set P4USER=<username>` | Set username |
| `git config --global user.email` | `p4 set P4MAIL=<email>` | Set email |
| `.gitignore` | `P4IGNORE` file + `p4 set P4IGNORE` | Ignore files from version control |
| `git remote add` | `p4 client` | Configure workspace/repository connection |
| `git init` | `p4 depot` (admin only) | Create new repository |

---

## Inspection & Debugging

| Git | Perforce | Description |
|-----|----------|-------------|
| `git diff HEAD` | `p4 diff -se` | Show modified files |
| `git diff --cached` | `p4 diff -sl` | Show files opened for edit |
| `git ls-files` | `p4 have` | List files in your workspace |
| `git reflog` | `p4 changes -m 100` | View recent activity |
| `git grep <pattern>` | `p4 grep <pattern>` | Search file contents |

---

## Key Philosophical Differences

### Workflow
- **Git**: Stage → Commit locally → Push to remote
- **Perforce**: Mark files (edit/add) → Submit directly to depot

### File Permissions
- **Git**: All files writable by default
- **Perforce**: Files read-only until explicitly checked out (`p4 edit`)

### Repository Structure
- **Git**: Distributed - full repository copy on every machine
- **Perforce**: Centralized - partial workspace possible, single source of truth

### Branching
- **Git**: Branch = lightweight pointer to commit
- **Perforce**: Branch = directory structure or stream with parent-child relationships

### File Locking
- **Git**: No native file locking (Git LFS only for large files)
- **Perforce**: Built-in file locking available for all files

### Merge Strategy
- **Git**: Merge happens locally, conflicts resolved before push
- **Perforce**: Changes submitted to server, conflicts resolved during sync

---

## Common Workflow Examples

### Starting Work on a Task

**Git:**
```bash
git checkout -b feature-branch
git add file.txt
git commit -m "Started feature"
git push origin feature-branch
```

**Perforce:**
```bash
p4 edit file.txt
# Make changes
p4 submit -d "Started feature"
```

### Getting Latest Changes and Resolving Conflicts

**Git:**
```bash
git pull
# Resolve conflicts if any
git add resolved-file.txt
git commit
git push
```

**Perforce:**
```bash
p4 sync
p4 resolve
p4 submit
```

### Saving Work in Progress

**Git:**
```bash
git stash save "WIP: feature half done"
# Switch to other work
git stash pop
```

**Perforce:**
```bash
p4 shelve -d "WIP: feature half done"
# Switch to other work
p4 unshelve -s <changelist#>
```

---

## Quick Reference: Most Common Commands

### Daily Git Commands
```bash
git status          # What's changed?
git add .           # Stage everything
git commit -m "msg" # Commit locally
git push            # Send to remote
git pull            # Get latest
```

### Daily Perforce Commands
```bash
p4 opened           # What's changed?
p4 edit file.txt    # Mark for editing
p4 submit           # Send to depot
p4 sync             # Get latest
p4 reconcile        # Find changed files
```

---

## Additional Notes

### Perforce Changelists
In Perforce, a **changelist** is similar to Git's staging area combined with a commit message. You can:
- Create numbered changelists to group related files
- Move files between changelists
- Submit changelists independently

### Perforce Streams
**Streams** in Perforce are like "branches with rules":
- Mainline stream = main branch
- Development stream = feature branch
- Release stream = release branch
- Task stream = short-lived personal branch

### File Types in Perforce
Perforce recognizes different file types that affect how files are stored and merged:
- Text files: Can be merged
- Binary files: Often set to exclusive checkout (`+l`)
- Compressed files: Stored differently for efficiency

---

## Resources

- **Git Documentation**: https://git-scm.com/doc
- **Perforce Documentation**: https://www.perforce.com/manuals/cmdref/
- **Git-P4 Bridge Tool**: https://git-scm.com/docs/git-p4