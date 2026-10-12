# Claude Code File Structure

## Repository Root

```
c:\Users\290397\Documents\GitHub\DEV_ops
│
├── README.md
│   └── Documentation and Notes
│
├── CLAUDE.md
│   └── Project Instructions
│       ├── Coding Standards
│       ├── Architecture
│       ├── CI/CD Rules
│       └── Team Conventions
│
├── KILL.md
│   └── Never Do These Things
│       ├── No Direct Prod Changes
│       ├── No Secrets in Code
│       ├── No Force Pushes
│       └── No Bypassing Reviews
│
├── .github/
│   └── skills/
│       ├── devops-engineer/
│       │   └── SKILL.md
│       ├── terraform-reviewer/
│       │   └── SKILL.md
│       └── github-actions/
│           └── SKILL.md
│
└── .claude/
    ├── settings.json
    └── agents/
        ├── frontend/
        ├── backend/
        └── infrastructure/
```

## Directory Descriptions

- **README.md** - Main project documentation and notes
- **CLAUDE.md** - Project instructions and conventions
- **KILL.md** - Guidelines on what NOT to do
- **.github/skills/** - Custom skills for Claude integration
  - **devops-engineer/** - DevOps-specific skill
  - **terraform-reviewer/** - Terraform review skill
  - **github-actions/** - GitHub Actions skill
- **.claude/agents/** - Claude agent configurations
  - **frontend/** - Frontend agent
  - **backend/** - Backend agent
  - **infrastructure/** - Infrastructure agent
