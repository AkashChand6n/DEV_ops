# Repository Structure & Organization

This document explains the repository structure, how files are organized, and what each file/folder does.

---

## 📁 Root Level Files

### CLAUDE.md
**Purpose:** Project instructions and rules  
**Audience:** Claude AI assistant  
**Content:**
- Important development rules
- CI/CD guidelines
- Production safety requirements
- Security policies

**When to update:** When project policies change

---

### KILL.md
**Purpose:** Anti-patterns and prohibited actions  
**Audience:** Developers and Claude AI  
**Content:**
- Actions that must NEVER be performed
- Security boundaries
- Production safety guardrails
- Git/CI/CD restrictions

**When to update:** When new safety requirements emerge

---

### README.md
**Purpose:** Comprehensive reference guide  
**Audience:** Team members and Claude AI  
**Content:**
- Claude Code concepts explanation
- File structure overview
- Command reference (/goal, /triage, /rewind)
- Best practices for DevOps work
- GitHub Actions and Terraform guides
- Hooks and automation examples

**When to update:** When documentation needs expansion

---

### claude-guide.md
**Purpose:** Quick reference guide  
**Audience:** Quick lookup during work  
**Content:**
- File overview table
- Project structure diagram
- Command quick reference
- Quick checklist
- Links to detailed docs

**When to update:** When quick reference needs updating

---

### STRUCTURE.md (This File)
**Purpose:** Explain repository organization  
**Audience:** New team members and maintainers  
**Content:**
- File and folder purposes
- Update guidelines
- When to use which file

---

## 📁 .claude/ Directory

Claude Code configuration and settings directory.

### .claude/settings.json
**Purpose:** Project configuration for Claude Code  
**Content:**
- Project metadata
- Available skills list
- Technology stack
- Important rules
- Project structure definition

**When to update:** When technologies or skills change

---

## 📁 .github/skills/ Directory

Reusable Claude AI expertise workflows.

### devops-engineer/SKILL.md
**Purpose:** DevOps expertise workflow  
**Content:**
- GitHub Actions best practices
- Terraform workflow
- Kubernetes/OpenShift management
- CI/CD patterns
- Production support rules

**When to use:** When working on DevOps tasks

---

### terraform-reviewer/SKILL.md
**Purpose:** Terraform code review expertise  
**Content:**
- Terraform validation checklist
- Security review items
- Best practices
- Common issues to check

**When to use:** When reviewing Terraform changes

---

### github-actions/SKILL.md
**Purpose:** GitHub Actions optimization  
**Content:**
- Workflow design patterns
- Performance optimization
- Security best practices
- Reusable workflow patterns
- Action version pinning rules

**When to use:** When creating/updating GitHub Actions workflows

---

## 📁 Domain Folders

### frontend/
**Purpose:** Frontend application code  
**Content:**
- Frontend source code
- Static assets
- UI tests
- Frontend documentation

**Standards:**
- Follow CLAUDE.md coding standards
- Run tests before PR
- Use TypeScript
- Ensure accessibility
- Security best practices

**Startup:** `npm install && npm start`

---

### backend/
**Purpose:** Backend services and APIs  
**Content:**
- API implementations
- Business logic
- Data models
- Database migrations
- Service tests

**Standards:**
- Follow CLAUDE.md coding standards
- API documentation required
- Test coverage mandatory
- Input validation required
- Error handling throughout

**Startup:** `npm install && npm run dev`

---

### infrastructure/
**Purpose:** Infrastructure as Code  
**Content:**
- Terraform configurations
- Kubernetes manifests
- AWS/Azure resources
- Infrastructure scripts
- Environment configurations

**Standards:**
- Run `terraform fmt` before commit
- Run `terraform validate` before commit
- Review `terraform plan` before merge
- Pin all versions
- Document resource purposes

**Terraform Workflow:**
```bash
terraform fmt
terraform validate
terraform plan
# Create PR with plan output
# After approval
terraform apply
```

---

## 📊 File Organization Decision Tree

### I need to document...

**Project rules/policies?**
→ Update CLAUDE.md or KILL.md

**How to use Claude Code?**
→ Update README.md

**Quick reference for work?**
→ Update claude-guide.md

**AI expertise workflow?**
→ Create/update in .github/skills/

**Application code?**
→ Put in frontend/, backend/, or infrastructure/

**Configuration for Claude?**
→ Update .claude/settings.json

---

## 🔄 Update Workflow

1. **Identify what changed:**
   - Project rules → Update CLAUDE.md
   - New safety concerns → Update KILL.md
   - Need documentation → Update README.md
   - Want quick reference → Update claude-guide.md

2. **Make the change:**
   - Edit relevant file(s)
   - Test the documentation (if applicable)
   - Verify no conflicts with other docs

3. **Create PR:**
   - Clear commit message
   - Reference the change reason
   - Link to related issues/discussions

4. **Request review:**
   - Team reviews documentation
   - Ensure clarity and accuracy

5. **Merge and communicate:**
   - Merge after approval
   - Share changes with team if significant

---

## 📝 Writing Guidelines

### For CLAUDE.md
- Keep rules simple and unambiguous
- Use imperative language: "Never...", "Always..."
- Focus on critical decisions
- Avoid excessive detail

### For KILL.md
- Clear, direct prohibitions
- Explain consequences if relevant
- Group related items
- Keep it scannable

### For README.md
- Comprehensive examples
- Explain the "why" behind practices
- Include diagrams and flowcharts
- Provide worked examples

### For claude-guide.md
- Quick lookup format
- Tables for comparison
- Short descriptions
- Links to detailed docs

### For Skill files
- Clear expertise definition
- Actionable workflow steps
- Practical examples
- Safety-first approach

---

## 🎯 Alignment Checklist

- [ ] CLAUDE.md rules match actual project standards
- [ ] KILL.md rules align with CLAUDE.md
- [ ] Skills in .github/skills/ match available expertise
- [ ] .claude/settings.json lists all skills
- [ ] Domain READMEs follow consistent format
- [ ] No duplicate information between files
- [ ] Quick links work correctly
- [ ] Examples are current and accurate
- [ ] Security guidelines are comprehensive
- [ ] File structure reflects in README diagrams

---

## 🚀 Quick Start for New Team Members

1. Read **CLAUDE.md** - Understand project rules
2. Read **KILL.md** - Know what to avoid
3. Read **claude-guide.md** - Get oriented quickly
4. Reference **README.md** - Deep dive when needed
5. Check domain folder README - Start coding

---

## 📞 Questions?

- For project rules → See CLAUDE.md
- For what NOT to do → See KILL.md
- For how-to guides → See README.md
- For quick answers → See claude-guide.md
- For domain-specific info → See domain folder README
