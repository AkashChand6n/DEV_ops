# Claude Code Notes

A personal reference for Claude Code, Skills, Commands, and DevOps best practices.

---
# Claude Code File Structure
Repository Root
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

├── .claude/
│   ├── settings.json
│   └── agents/
│
├── frontend/
├── backend/
└── infrastructure/

---

# .claude/ Directory - Configuration Options

The `.claude/` directory contains configuration and settings for Claude Code integration.

## .claude/settings.json

The main configuration file for the project. Controls how Claude Code behaves within this repository.

### Configuration Structure

```json
{
  "project_name": "CLAUDE",
  "description": "Personal reference for Claude Code, Skills, Commands, and DevOps best practices.",
  "claude_instructions": "CLAUDE.md",
  "safety_rules": "KILL.md",
  "primary_technologies": [
    "GitHub Actions",
    "Terraform",
    "AWS",
    "Kubernetes",
    "OpenShift",
    "CI/CD"
  ],
  "available_skills": [
    ".github/skills/devops-engineer",
    ".github/skills/terraform-reviewer",
    ".github/skills/github-actions"
  ],
  "project_structure": {
    "frontend": "Frontend applications",
    "backend": "Backend services and APIs",
    "infrastructure": "Infrastructure as Code (Terraform, Kubernetes)"
  },
  "important_rules": [
    "Never push directly to main",
    "Always create PRs",
    "Run Terraform fmt and validate before commit",
    "Never modify production workflows without approval",
    "Do not store secrets in code",
    "Always verify deployment impact before merging"
  ]
}
```

### Configuration Options Explained

#### project_name
**Type:** String  
**Purpose:** Identifies the project in Claude Code  
**Example:** `"CLAUDE"`  
**When to change:** When renaming the project

---

#### description
**Type:** String  
**Purpose:** Short description of what the project is  
**Example:** `"Personal reference for Claude Code, Skills, Commands, and DevOps best practices."`  
**When to change:** When project scope changes

---

#### claude_instructions
**Type:** String (File path)  
**Purpose:** Points to the main instruction file Claude reads  
**Default:** `"CLAUDE.md"`  
**How Claude uses it:** Automatically reads this file for project context before responding  
**What it contains:**
- Coding standards
- Architecture decisions
- Branching strategy
- Deployment procedures
- Team conventions
- Security guidelines

**When to change:** Only if you rename CLAUDE.md

---

#### safety_rules
**Type:** String (File path)  
**Purpose:** Points to the safety/anti-pattern file  
**Default:** `"KILL.md"`  
**How Claude uses it:** References this file to avoid prohibited actions  
**What it contains:**
- Actions that must NEVER be performed
- Production safety boundaries
- Security restrictions
- Git/CI/CD safeguards

**When to change:** Only if you rename KILL.md

---

#### primary_technologies
**Type:** Array of Strings  
**Purpose:** Lists the main technologies used in this project  
**Example:**
```json
[
  "GitHub Actions",
  "Terraform",
  "AWS",
  "Kubernetes",
  "OpenShift",
  "CI/CD"
]
```
**How Claude uses it:** 
- Helps Claude understand the tech stack
- Influences which expertise Claude applies
- Used for context when making suggestions

**When to change:** When adding new major technologies to the project

---

#### available_skills
**Type:** Array of Strings (Directory paths)  
**Purpose:** Lists all available Claude expertise workflows  
**Example:**
```json
[
  ".github/skills/devops-engineer",
  ".github/skills/terraform-reviewer",
  ".github/skills/github-actions"
]
```
**How Claude uses it:** 
- Registers which skills/expertise are available
- Used when invoking specialized workflows
- Allows context switching between expertise domains

**Skills included:**
- **devops-engineer** - GitHub Actions, Terraform, Kubernetes, OpenShift expertise
- **terraform-reviewer** - Terraform code review and validation
- **github-actions** - GitHub Actions workflow design and optimization

**When to change:** When adding new skill directories

---

#### project_structure
**Type:** Object (Key-value pairs)  
**Purpose:** Describes the folder structure and what each folder contains  
**Example:**
```json
{
  "frontend": "Frontend applications",
  "backend": "Backend services and APIs",
  "infrastructure": "Infrastructure as Code (Terraform, Kubernetes)"
}
```
**How Claude uses it:**
- Understands where different parts of the project live
- Routes work to the correct folder
- Helps with file organization

**Keys to include:**
- Domain folders (frontend, backend, infrastructure)
- Any other major organizational areas

**When to change:** When folder structure changes

---

#### important_rules
**Type:** Array of Strings  
**Purpose:** Quick reference list of critical project rules  
**Example:**
```json
[
  "Never push directly to main",
  "Always create PRs",
  "Run Terraform fmt and validate before commit",
  "Never modify production workflows without approval",
  "Do not store secrets in code",
  "Always verify deployment impact before merging"
]
```
**How Claude uses it:**
- Used as a safety checklist
- Provides quick context about project standards
- Helps Claude understand boundaries

**Format:** Use imperative language ("Never...", "Always...")

**When to change:** When project rules change

---

## .claude/agents/

**Directory Purpose:** Location for custom Claude agent configurations (optional)

**Current Status:** Directory structure available for future agents

**Use Cases:**
- Custom specialized agents for this project
- Team-specific automation workflows
- Reusable agent definitions

**When to use:** When creating project-specific agents

---

# How to Modify .claude/settings.json

## Updating Technologies

When adding a new technology:

```json
"primary_technologies": [
  "GitHub Actions",
  "Terraform",
  "AWS",
  "Kubernetes",
  "OpenShift",
  "CI/CD",
  "Docker"  // ← ADD HERE
]
```

## Adding a New Skill

When you create a new skill:

1. Create skill directory: `.github/skills/my-skill/SKILL.md`
2. Update settings.json:
```json
"available_skills": [
  ".github/skills/devops-engineer",
  ".github/skills/terraform-reviewer",
  ".github/skills/github-actions",
  ".github/skills/my-skill"  // ← ADD HERE
]
```

## Adding a New Rule

When you add a project rule:

```json
"important_rules": [
  "Never push directly to main",
  "Always create PRs",
  "Never use production secrets in tests"  // ← ADD HERE
]
```

## Adding a New Domain Folder

When you create a new domain folder:

1. Create folder: `new-domain/`
2. Add README.md to the folder
3. Update settings.json:
```json
"project_structure": {
  "frontend": "Frontend applications",
  "backend": "Backend services and APIs",
  "infrastructure": "Infrastructure as Code",
  "new-domain": "Description of new domain"  // ← ADD HERE
}
```

---

# Configuration Best Practices

## ✅ DO

- ✅ Keep settings.json valid JSON
- ✅ Update technologies when adding major new tech
- ✅ Update rules when policy changes
- ✅ Keep descriptions short and clear
- ✅ Use relative paths for file references
- ✅ Use imperative language for rules

## ❌ DON'T

- ❌ Store secrets in settings.json
- ❌ Use absolute paths
- ❌ Add duplicate rules
- ❌ Change claude_instructions or safety_rules filenames without updating
- ❌ Leave unused skills in the list
- ❌ Use complex nested structures

---

# How Claude Uses .claude/settings.json

## When Claude Starts

```
1. Read .claude/settings.json
2. Load CLAUDE.md (from claude_instructions)
3. Load KILL.md (from safety_rules)
4. Register available_skills
5. Understand project_structure
6. Apply important_rules as safety checks
```

## During Conversation

```
User Request
    ↓
Read settings.json for context
    ↓
Load appropriate SKILL if relevant
    ↓
Check important_rules for constraints
    ↓
Check KILL.md for prohibited actions
    ↓
Apply project standards from CLAUDE.md
    ↓
Respond with project context applied
```

## When Making Decisions

Claude uses settings.json to:
- Understand technology choices
- Route work to correct folders
- Know which expertise is available
- Apply project-specific rules
- Avoid prohibited actions

---

# .claude/ Directory Contents Summary

| File/Folder | Purpose | Contains |
|-------------|---------|----------|
| settings.json | Project configuration | Metadata, tech stack, skills, rules |
| agents/ | Custom agents (optional) | Future agent definitions |

---

# How to Use .claude/settings.json

### For New Team Members
- Shows what technologies are used
- Lists what skills are available
- Explains project rules upfront

### For Maintaining Projects
- Update when technologies change
- Update when rules change
- Update when adding skills

### For Claude Code
- Provides context for all interactions
- Enforces project standards
- Routes to correct expertise

### For Automation
- Can be read by CI/CD pipelines
- Used by project tooling
- Helps with onboarding automation

---

# .claude/ vs Other Files

| File | Audience | Purpose |
|------|----------|---------|
| .claude/settings.json | Claude Code tool | Configuration & metadata |
| CLAUDE.md | Everyone | Project instructions & rules |
| KILL.md | Everyone | Anti-patterns & restrictions |
| README.md | Learners | Comprehensive guide |
| SKILL files | Claude expertise | Specialized workflows |

---

# Claude Code Slash Commands (/)

When you type "/" in Claude Code, you get access to special commands that help you work better.

Think of "/" like a menu of superpowers for Claude Code.

---

## What Does "/" Mean?

**"/" = Special Command**

When you type "/" and then a command name, Claude Code does something special based on that command.

**Example:**
```
/goal    → Tell Claude what you want to achieve
/help    → Get help about Claude Code
/rewind  → Go back to an earlier point in conversation
```

---

## All Available Slash Commands

### 1. /goal

**What it does:** Define what you want to accomplish before starting

**When to use:** At the beginning of any task

**Example:**
```
/goal
Deploy the new payment service to production
with automated rollback capability
```

**Why it's useful:**
- Claude understands success criteria upfront
- Prevents wasted work going wrong direction
- Makes solutions more targeted

**How Claude uses it:**
1. Reads your goal
2. Asks clarifying questions if needed
3. Plans steps to achieve it
4. Measures progress against goal
5. Stops when goal is reached

---

### 2. /triage

**What it does:** Investigate and diagnose problems before fixing them

**When to use:** When something is broken or not working

**Example:**
```
/triage
GitHub Actions deployment failing since yesterday
```

**Why it's useful:**
- Finds root cause instead of just fixing symptoms
- Prevents making things worse
- Saves time by fixing real problem

**How Claude uses it:**
1. Asks detailed questions
2. Examines logs and error messages
3. Reviews recent changes
4. Identifies root cause
5. Suggests fixes
6. Creates action plan

**Good use cases:**
- Build failures
- Deployment errors
- Application crashes
- Pipeline issues
- Configuration problems

---

### 3. /rewind

**What it does:** Go back to an earlier point in the conversation

**When to use:** When Claude is going in the wrong direction

**Example:**
```
/rewind
```

Then pick which checkpoint to go back to.

**Why it's useful:**
- Undo bad decisions without restarting
- Remove messy context
- Try a different approach
- Save time

**How it works:**
1. Shows you previous checkpoints
2. You select which one to return to
3. Conversation continues from that point
4. All work after that point is discarded

---

### 4. /plan

**What it does:** Create a detailed implementation plan before coding

**When to use:** Before starting complex work

**Example:**
```
/plan
Refactor the authentication system to use OAuth 2.0
```

**Why it's useful:**
- See the full approach before starting
- Catch issues early
- Agree on strategy
- Get buy-in from team

**How Claude uses it:**
1. Breaks down the work into steps
2. Identifies dependencies
3. Notes potential risks
4. Estimates effort
5. Suggests alternatives
6. Waits for your approval

**What you get:**
- Step-by-step breakdown
- Time estimates
- Risk assessment
- Resource requirements
- Alternative approaches

---

### 5. /help

**What it does:** Get help about Claude Code features

**When to use:** When you need to learn about a feature

**Example:**
```
/help
How do I use hooks?
```

**Why it's useful:**
- Learn features quickly
- Get examples
- Understand limitations
- Find alternatives

**Types of help available:**
- Command explanations
- Feature tutorials
- Best practices
- Troubleshooting
- Configuration help

---

### 6. /config

**What it does:** View and change Claude Code settings

**When to use:** When you want to customize behavior

**Example:**
```
/config
Show all settings
```

**Settings you can change:**
- Default model (fast vs standard)
- Permissions (what Claude can do)
- Hooks (automatic commands)
- Keybindings (keyboard shortcuts)
- Theme (light/dark mode)
- Editor behavior

---

### 7. /fast

**What it does:** Toggle between fast and standard mode

**When to use:** When you want faster responses

**Example:**
```
/fast
```

**Fast Mode:**
- ✅ Responds quicker
- ✅ Good for simple tasks
- ❌ Less detailed
- ❌ Less capable

**Standard Mode:**
- ✅ More thorough
- ✅ Better for complex work
- ❌ Takes longer
- ❌ More expensive

**When to use fast:**
- Simple code edits
- Quick questions
- Simple refactoring
- Basic debugging

**When to use standard:**
- Complex architecture changes
- Security-critical work
- Major refactoring
- Deep debugging

---

### 8. /skill

**What it does:** Invoke a specialized skill or expertise

**When to use:** When you need special knowledge

**Example:**
```
/skill devops-engineer
Deploy infrastructure changes
```

**Available skills in this project:**
- `devops-engineer` - GitHub Actions, Terraform, Kubernetes
- `terraform-reviewer` - Terraform code review
- `github-actions` - GitHub Actions workflows

**Why it's useful:**
- Switches Claude to expert mode
- Applies specialized workflows
- Better suggestions for domain
- Faster solutions

---

### 9. /loop

**What it does:** Run a command repeatedly on a schedule

**When to use:** For recurring tasks or monitoring

**Example:**
```
/loop 5m /check-deployment-status
```

**Formats:**
- `/loop 5m` = Every 5 minutes
- `/loop 1h` = Every 1 hour
- `/loop 30s` = Every 30 seconds

**Good use cases:**
- Monitoring deployments
- Watching for build completion
- Polling API status
- Repeating checks

**How it works:**
1. Runs initial command
2. Waits specified time
3. Runs command again
4. Repeats until you stop it

---

### 10. /clear

**What it does:** Clear the conversation history

**When to use:** When you want a fresh start

**Example:**
```
/clear
```

**Why you might use it:**
- Remove old context
- Start new unrelated task
- Clean up conversation
- Save token usage

**Warning:** This is permanent - can't undo

---

### 11. /memory

**What it does:** Save information for future conversations

**When to use:** When you learn something important

**Example:**
```
/memory
Save: This project uses OpenShift for container orchestration
```

**What gets saved:**
- User preferences
- Project details
- Workflow patterns
- Important decisions
- Team standards

**Why it's useful:**
- Next time you work on this, Claude remembers
- Doesn't have to re-explain everything
- Faster onboarding
- Consistent behavior

---

### 12. /agents

**What it does:** List available agents you can use

**When to use:** When you want specialized help

**Example:**
```
/agents
```

**What you see:**
- All available agents
- What each does
- How to invoke them

**Types of agents:**
- Code review agents
- Testing agents
- Deployment agents
- Security agents
- Custom agents

---

### 13. /fork

**What it does:** Create an independent branch of the conversation

**When to use:** When you want to try different approaches

**Example:**
```
/fork
Try approach B while keeping approach A
```

**Why it's useful:**
- Explore multiple options
- Compare approaches
- Avoid losing work
- Test ideas safely

**How it works:**
1. Saves current conversation state
2. Creates independent copy
3. You can work on both
4. Choose which version to keep

---

### 14. /workflows

**What it does:** View workflow progress

**When to use:** When running complex multi-step tasks

**Example:**
```
/workflows
```

**Shows:**
- Running workflows
- Progress percentage
- Current step
- Estimated time remaining
- Any issues

---

### 15. /skills-doctor

**What it does:** Diagnose skill configuration issues

**When to use:** When skills aren't working

**Example:**
```
/skills-doctor
```

**Checks:**
- Skill files exist
- Skill configuration correct
- Skills registered properly
- Permissions working
- File references valid

---

## Command Comparison Table

| Command | Purpose | Usage | Result |
|---------|---------|-------|--------|
| `/goal` | Define objective | Before starting work | Focused approach |
| `/triage` | Diagnose problems | When things break | Root cause identified |
| `/rewind` | Go back in time | Wrong direction | Start over from checkpoint |
| `/plan` | Create blueprint | Before complex work | Detailed implementation plan |
| `/help` | Get assistance | When confused | Learn features |
| `/config` | Change settings | Customize behavior | Updated configuration |
| `/fast` | Speed up responses | Want quick answers | Faster but less detailed |
| `/skill` | Use expertise | Need specialized help | Expert mode activated |
| `/loop` | Repeat command | Recurring tasks | Automatic repetition |
| `/clear` | Clean slate | Start fresh | Clear history |
| `/memory` | Save info | Remember things | Persistent memory |
| `/agents` | List helpers | Find tools | See available agents |
| `/fork` | Branch conversation | Try alternatives | Parallel exploration |
| `/workflows` | Check progress | Monitor tasks | See workflow status |
| `/skills-doctor` | Fix skills | Diagnose issues | Troubleshoot skills |

---

## How to Use Slash Commands

### Basic Usage

```
Type /command in the chat
↓
Claude Code recognizes it
↓
Special action happens
↓
Result displayed
```

### Example Workflow

```
User: /goal Deploy authentication service to production

Claude: I'll help you deploy. Let me understand the requirements...
       [asks questions]

User: [answers questions]

Claude: Here's the deployment plan:
       1. Run tests
       2. Build container
       3. Push to registry
       4. Update Kubernetes
       5. Verify health
       
       Ready to proceed?

User: Yes, proceed

Claude: [executes deployment]
       ✅ Deployment successful
```

---

## When to Use Which Command

### Starting New Work
```
→ /goal          (Define what you want)
→ /plan          (Plan the approach)
```

### Debugging Problems
```
→ /triage        (Find root cause)
```

### Adjusting Course
```
→ /rewind        (Go back)
```

### Customizing Behavior
```
→ /config        (Change settings)
→ /fast          (Speed up)
```

### Monitoring Tasks
```
→ /loop          (Repeat automatically)
→ /workflows     (Watch progress)
```

### Getting Help
```
→ /help          (Learn features)
→ /agents        (See available agents)
→ /memory        (Recall info)
```

### Troubleshooting
```
→ /skills-doctor (Diagnose issues)
```

---

## Command Workflow Examples

### Example 1: Fix a Deployment Issue

```
User: /triage
      Production API crashing after latest deploy

Claude: Let me investigate...
       [examines logs]
       Root cause: Database migration failed
       
       Solution:
       1. Rollback to previous version
       2. Fix migration script
       3. Test in staging
       4. Redeploy with fix

User: Do it!

Claude: ✅ Completed - Service is healthy
```

### Example 2: Complex Refactoring

```
User: /goal
      Migrate from REST API to GraphQL

Claude: I need to understand scope...
       [asks questions]

User: [answers]

Claude: /plan
       Step 1: Analyze current REST endpoints
       Step 2: Design GraphQL schema
       Step 3: Implement resolvers
       Step 4: Add tests
       Step 5: Update clients
       Step 6: Deprecate REST endpoints
       
       Estimated: 2 weeks
       Ready?

User: Yes

Claude: [proceeds with implementation]
```

### Example 3: Quick Task with Fast Mode

```
User: /fast
      Add a new function to sort the array

Claude: ✅ Fast mode enabled

Claude: ✅ Function added and tested
```

### Example 4: Exploring Options

```
User: /fork
      Try both implementation approaches

Claude: [creates two branches]
       Branch A: Using library X
       Branch B: Custom implementation
       
       Which do you prefer?

User: A is better

Claude: ✅ Keeping approach A
```

---

## Pro Tips for Slash Commands

### ✅ DO

- ✅ Use `/goal` at the start of complex work
- ✅ Use `/triage` for mysterious bugs
- ✅ Use `/plan` before major changes
- ✅ Use `/rewind` when stuck
- ✅ Use `/fast` for quick edits
- ✅ Use `/skill` for domain expertise
- ✅ Use `/memory` to save learnings
- ✅ Use `/loop` for monitoring tasks

### ❌ DON'T

- ❌ Skip `/goal` then complain about wrong direction
- ❌ Use `/fast` for critical security work
- ❌ Ignore `/plan` for complex changes
- ❌ Forget to set `/memory` for important decisions
- ❌ Use `/loop` without stopping when done
- ❌ Overuse `/clear` - conversation context is valuable

---

## Slash Commands vs Regular Chat

| Aspect | Regular Chat | Slash Command |
|--------|--------------|---------------|
| **Trigger** | Type normally | Type "/" first |
| **Purpose** | General questions | Special actions |
| **Processing** | Standard response | Command-specific workflow |
| **Result** | Answer provided | Action taken |
| **Context** | Uses full history | May reset or branch |

---

## Learning Path for Slash Commands

### Week 1 (Basics)
- [ ] Learn `/goal` - Define objectives
- [ ] Learn `/help` - Get assistance
- [ ] Learn `/config` - Customize behavior

### Week 2 (Debugging)
- [ ] Learn `/triage` - Diagnose issues
- [ ] Learn `/rewind` - Go back in time
- [ ] Learn `/plan` - Create plans

### Week 3 (Advanced)
- [ ] Learn `/skill` - Use expertise
- [ ] Learn `/loop` - Automate tasks
- [ ] Learn `/fork` - Explore options
- [ ] Learn `/memory` - Save information

### Ongoing
- [ ] Use `/fast` for quick work
- [ ] Use `/workflows` to monitor
- [ ] Use `/skills-doctor` when needed
- [ ] Use `/agents` to explore options

---

## Summary

**Slash commands (/) are special powers in Claude Code that help you:**

1. 🎯 **Define goals** - `/goal`
2. 🔍 **Debug issues** - `/triage`
3. ⏮️ **Go backwards** - `/rewind`
4. 📋 **Plan work** - `/plan`
5. ❓ **Get help** - `/help`
6. ⚙️ **Customize** - `/config`
7. ⚡ **Speed up** - `/fast`
8. 🎓 **Use expertise** - `/skill`
9. 🔄 **Repeat tasks** - `/loop`
10. 🧠 **Remember things** - `/memory`

**Next time you type "/", remember it's your command menu!**

---

# How Claude Uses These Files


                    User Request
                          │
                          ▼
                  ┌─────────────┐
                  │   /goal     │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ CLAUDE.md   │
                  │ Project     │
                  │ Knowledge   │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ SKILL.md    │
                  │ Expertise   │
                  │ Workflow    │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ /triage     │
                  │ Investigation│
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ Solution    │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ KILL.md     │
                  │ Safety      │
                  │ Check       │
                  └──────┬──────┘
                         │
                         ▼
                     Final Result

# DevOps Workflow Diagram

┌─────────────────────────┐
│        /goal            │
│ Define Success          │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│       /triage           │
│ Find Root Cause         │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│         Plan            │
│ Create Approach         │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│      Implement          │
│ Make Changes            │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│       Verify            │
│ Tests & Validation      │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│      KILL.md Check      │
│ Any Rule Violations?    │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│      Document           │
│ Explain Changes         │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│       Commit            │
└─────────────────────────┘


---

# CLAUDE.md

## What is CLAUDE.md?

`CLAUDE.md` is the primary instruction file for a repository.

Claude automatically reads this file and uses it as project context.

Think of it as a permanent prompt that explains:

- Project architecture
- Coding standards
- Branching strategy
- Deployment process
- Team conventions
- Testing requirements

---

## Example CLAUDE.md

```markdown
# Project Instructions

## Important Rules

- Never push directly to main
- Always create pull requests
- Run tests before commit
- Follow existing code patterns

## Repository Structure

- frontend/ -> React application
- backend/ -> APIs
- infra/ -> Terraform

## Development Workflow

1. Understand requirement
2. Create plan
3. Implement
4. Test
5. Document
6. Commit

## CI/CD

- GitHub Actions is the source of truth
- Production deployments require approval

## Security

- Never commit secrets
- Never store credentials in code
```

---

# SKILL.md

## What is SKILL.md?

A reusable capability that teaches Claude how to perform a specific workflow.

Examples:

- DevOps Engineer
- Terraform Reviewer
- GitHub Actions Expert
- Kubernetes Troubleshooter
- Security Auditor

---

## Example SKILL.md

```markdown
---
name: devops-engineer
description: Expert in GitHub Actions, AWS, Terraform, Kubernetes, and OpenShift.
---

# DevOps Engineer Skill

## Goal

Understand the desired outcome before making changes.

## Process

Goal -> Triage -> Plan -> Execute -> Verify -> Document

## GitHub Actions

- Use concurrency groups
- Use least privilege permissions
- Enable reusable workflows

## Terraform

- Run fmt
- Run validate
- Review plan before apply

## Kubernetes

- Verify namespace
- Check resource limits
- Prefer rolling deployments

## Output Format

1. Goal
2. Findings
3. Plan
4. Changes
5. Verification
6. Risks
7. Rollback
```

---

# KILL.md

## What is KILL.md?

Not an official Claude file.

Many teams use it as a "never do this" document.

It contains dangerous actions that should always be avoided.

---

## Example KILL.md

```markdown
# KILL.md

## Git

- Never force push main
- Never disable branch protection

## CI/CD

- Never bypass PR approvals
- Never disable security checks

## Terraform

- Never manually modify state files
- Never apply directly to production

## Kubernetes

- Never delete production namespaces
- Never remove resource limits

## Security

- Never commit secrets
- Never expose credentials in logs
```

---

# Claude Commands

---

## /goal

Define the desired outcome before solving a problem.

### Purpose

Helps Claude understand what success looks like.

### Template

```text
Goal:
- Desired result
- Success criteria
- Constraints
```

### Example

```text
/goal

Cancel all older GitHub Actions workflows and keep only the newest run for a branch.
```

### Success Criteria

```text
- Only one workflow run is active
- Older runs are cancelled automatically
- Deployment duplication is avoided
```

---

## /triage

Investigate and diagnose issues before making changes.

### Purpose

Find root cause before implementing a fix.

### Example

```text
/triage

GitHub Actions deployment failing after latest merge.
```

### Expected Output

```text
- Root cause
- Impact
- Recommended fix
- Risk assessment
```

### Good Use Cases

- Build failures
- Deployment failures
- Kubernetes issues
- Pipeline failures
- Terraform errors

---

## /rewind

Return to an earlier checkpoint in the conversation.

### Purpose

Used when Claude starts going in the wrong direction.

### Example

```text
/rewind
```

### Use Cases

- Wrong implementation path
- Overly complex solution
- New requirements discovered
- Incorrect assumptions made

---

# Recommended Workflow

For DevOps, Platform Engineering, and SRE work:

```text
/goal
    ↓
/triage
    ↓
Plan
    ↓
Implement
    ↓
Verify
    ↓
Document
    ↓
Commit
```

---

# GitHub Actions Best Practices

## Cancel Older Workflow Runs

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

Benefits:

- Lower runner costs
- Faster feedback
- Prevent duplicate deployments
- Avoid stale builds

---

# Terraform Best Practices

Before every PR:

```bash
terraform fmt
terraform validate
terraform plan
```

Rules:

- Never modify state manually
- Use remote state backend
- Review all plans
- Keep modules reusable

---

# Kubernetes/OpenShift Best Practices

Before deploy:

```bash
kubectl rollout status deployment/app
```

Rules:

- Use rolling updates
- Set resource requests
- Set resource limits
- Verify namespace
- Have rollback strategy

---

# Production Support Rules

## Always

- Verify impact before change
- Test in lower environments
- Keep rollback ready
- Communicate production risks

## Never

- Directly deploy to production
- Bypass approvals
- Disable security controls
- Commit secrets

---

# Personal DevOps Skill Summary

Primary Technologies:

- GitHub Actions
- GitHub Administration
- Terraform
- AWS
- Kubernetes
- OpenShift
- CI/CD
- Production Support

Primary Responsibilities:

- Manage production and non-production environments
- Build and maintain CI/CD pipelines
- Kubernetes/OpenShift cluster administration
- Production deployment support
- Migrate Jenkins pipelines to GitHub Actions
- Infrastructure automation using Terraform
- Troubleshoot production incidents
- Improve deployment reliability

---

# Quick Reference

```text
CLAUDE.md
=
Project instructions

SKILL.md
=
Reusable expertise and workflows

KILL.md
=
Actions that must never be performed

/goal
=
Define success

/triage
=
Find root cause

/rewind
=
Go back and restart from a good checkpoint
```

# Claude Code Hooks Guide

A simple guide to understanding Hooks, PreHooks, and PostHooks in Claude Code.

---

# What is a Hook?

A Hook is an automatic action that runs when a specific event happens.

Think of it like a trigger.

Real-life examples:

```text
Doorbell Pressed
      ↓
Bell Rings

Motion Detected
      ↓
Lights Turn On

Code Changed
      ↓
Hook Runs
```

In Claude Code, hooks allow you to automatically execute commands before or after Claude performs an action.

---

# Why Use Hooks?

Hooks help you:

- Enforce standards
- Run validations automatically
- Prevent mistakes
- Improve security
- Save manual effort

Examples:

✅ Run tests automatically

✅ Check code formatting

✅ Scan for secrets

✅ Validate Terraform

✅ Verify Kubernetes manifests

✅ Log activity

---

# Hook Workflow

```text
User Request
      │
      ▼
┌─────────────┐
│ PreHook     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Claude Work │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ PostHook    │
└──────┬──────┘
       │
       ▼
 Final Result
```

---

# What is a PreHook?

A PreHook runs BEFORE Claude performs an action.

Think:

```text
Before doing work
      ↓
Run checks
```

---

## Example

User asks Claude:

```text
Update Terraform files
```

PreHook runs:

```bash
terraform validate
```

If validation fails:

```text
❌ Stop operation
```

If validation succeeds:

```text
✅ Continue
```

---

# PreHook Diagram

```text
User Request
      │
      ▼
┌─────────────┐
│  PreHook    │
│ Validation  │
└──────┬──────┘
       │
       ▼
   Claude Acts
```

---

# Common PreHook Examples

## Git

```bash
git status
```

Verify repository state.

---

## Terraform

```bash
terraform validate
```

Verify Terraform configuration.

---

## Kubernetes

```bash
kubectl config current-context
```

Verify cluster context.

---

## Security

```bash
gitleaks detect
```

Check for secrets.

---

# What is a PostHook?

A PostHook runs AFTER Claude completes an action.

Think:

```text
Work Finished
      ↓
Run Verification
```

---

## Example

Claude updates code.

PostHook runs:

```bash
npm test
```

Result:

```text
✅ Tests passed
```

or

```text
❌ Tests failed
```

---

# PostHook Diagram

```text
Claude Work
      │
      ▼
┌─────────────┐
│ PostHook    │
│ Verification│
└──────┬──────┘
       │
       ▼
 Final Output
```

---

# Common PostHook Examples

## JavaScript

```bash
npm test
```

Run tests.

---

## Python

```bash
pytest
```

Run test suite.

---

## Terraform

```bash
terraform plan
```

Verify infrastructure changes.

---

## Kubernetes

```bash
kubectl rollout status deployment/app
```

Verify deployment.

---

# Hook Comparison

```text
PREHOOK
│
├─ Runs BEFORE Claude acts
├─ Prevents mistakes
├─ Validates inputs
└─ Security checks

POSTHOOK
│
├─ Runs AFTER Claude acts
├─ Verifies results
├─ Runs tests
└─ Confirms success
```

---

# Example DevOps Workflow

```text
User:
Update GitHub Actions workflow

          │
          ▼

PreHook
----------
yamllint
actionlint

          │
          ▼

Claude Updates Workflow

          │
          ▼

PostHook
----------
GitHub Actions Validation
Unit Tests
Security Scan

          │
          ▼

Completed
```

---

# GitHub Actions Example

## PreHook

```bash
actionlint
```

Checks workflow syntax before changes.

---

## PostHook

```bash
gh workflow view
```

Verify workflow configuration.

---

# Terraform Example

## PreHook

```bash
terraform fmt -check
terraform validate
```

---

## PostHook

```bash
terraform plan
```

Generate execution plan.

---

# Kubernetes Example

## PreHook

```bash
kubectl config current-context
```

Ensure correct cluster.

---

## PostHook

```bash
kubectl rollout status deployment/app
```

Verify deployment success.

---

# Production Safety Example

```text
Request:
Deploy to Production

        ▼

PreHook
--------
Check Approval
Check Change Ticket
Check Cluster

        ▼

Deployment

        ▼

PostHook
--------
Health Check
Smoke Test
Monitoring Check
```

---

# How to Create a Hook

## Step 1

Identify when it should run.

```text
Before action?
    → PreHook

After action?
    → PostHook
```

---

## Step 2

Create a command or script.

Example:

```bash
terraform validate
```

or

```bash
npm test
```

---

## Step 3

Configure Claude Code to execute it automatically.

---

# Simple Mental Model

```text
PreHook
=
"Before I do something,
check that it is safe."

Claude
=
"Do the work."

PostHook
=
"After I finish,
verify everything is okay."
```

---

# DevOps Examples

## PreHooks

```text
terraform validate

yamllint

actionlint

gitleaks

kubectl config current-context
```

## PostHooks

```text
terraform plan

npm test

pytest

kubectl rollout status

security scans
```

---

# Quick Cheat Sheet

```text
Hook
=
Automatic action triggered by an event

PreHook
=
Runs BEFORE Claude performs work

PostHook
=
Runs AFTER Claude performs work

Purpose
=
Automation + Validation + Safety

DevOps Pattern
=
PreHook
    ↓
Claude Change
    ↓
PostHook
```

---

# Easy Remember Rule

```text
HOOK
    ↓
Automatic Trigger

PREHOOK
    ↓
Check Before

POSTHOOK
    ↓
Check After
```

Think of it like driving:

```text
PreHook
=
Wear seatbelt

Drive
=
Journey

PostHook
=
Verify you reached destination safely
```