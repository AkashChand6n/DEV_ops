# Claude Code Quick Reference

Quick reference for Claude Code files and commands used in this project.

## Files Overview

| File | Purpose |
|------|---------|
| **CLAUDE.md** | Project instructions, coding standards, workflows |
| **KILL.md** | Safety rules - what MUST NEVER be done |
| **README.md** | Comprehensive guide and reference |
| **.claude/settings.json** | Claude Code configuration |
| **.github/skills/** | Reusable expertise workflows |

## Important Files in This Project

### CLAUDE.md
- Never push directly to main
- Always create PRs
- GitHub Actions is the primary CI/CD platform
- Run Terraform fmt and validate before commit
- Never modify production workflows without approval
- Use OpenShift/Kubernetes manifests already in the repository
- Do not store secrets in code
- Always verify deployment impact before merging

### KILL.md
- Never force push main
- Never disable branch protection
- Never skip Terraform validation
- Never deploy directly to production clusters
- Never commit credentials
- Never bypass required PR approvals

## Available Skills

Located in `.github/skills/`:

1. **devops-engineer** - GitHub Actions, Terraform, AWS, Kubernetes, OpenShift, CI/CD
2. **terraform-reviewer** - Terraform code review, validation, and best practices
3. **github-actions** - GitHub Actions workflow design and optimization

## Project Structure

```
CLAUDE/
├── frontend/          → Frontend applications
├── backend/           → Backend services and APIs
├── infrastructure/    → Infrastructure as Code
├── .github/skills/    → Custom Claude skills
├── .claude/           → Claude Code configuration
├── CLAUDE.md         → Project instructions
├── KILL.md           → Safety rules
└── README.md         → Full documentation
```

## Claude Commands

### /goal
Define the desired outcome before solving a problem.
```bash
/goal
Cancel all older GitHub Actions workflows and keep only the newest run.
```

### /triage
Investigate and diagnose issues before making changes.
```bash
/triage
GitHub Actions deployment failing after latest merge.
```

### /rewind
Return to an earlier checkpoint in the conversation.
```bash
/rewind
```

## Quick Checklist

Before committing:
- [ ] Check CLAUDE.md for project rules
- [ ] Run `terraform fmt` and `terraform validate`
- [ ] Run all tests
- [ ] Review git diff
- [ ] No secrets in code
- [ ] Check KILL.md - avoiding prohibited actions

Before deploying:
- [ ] Verify deployment impact
- [ ] Check required approvals
- [ ] Test in lower environments
- [ ] Have rollback plan ready

## Key Workflows

**DevOps Work:**
1. `/goal` - Define success
2. `/triage` - Find root cause
3. Plan → Implement → Verify
4. Check KILL.md for safety
5. Document → Commit

**Terraform Work:**
1. Write/update Terraform
2. `terraform fmt`
3. `terraform validate`
4. `terraform plan`
5. Create PR
6. Review changes
7. Merge and deploy via pipeline

## More Information

For complete details, see:
- `README.md` - Comprehensive guide with examples
- `.github/skills/devops-engineer/SKILL.md` - DevOps expertise
- `.github/skills/terraform-reviewer/SKILL.md` - Terraform review checklist
- `.github/skills/github-actions/SKILL.md` - GitHub Actions best practices