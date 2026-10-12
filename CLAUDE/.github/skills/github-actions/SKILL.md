---
name: github-actions
description: Expert in GitHub Actions workflow design, optimization, and CI/CD pipeline management.
---

# GitHub Actions Skill

## Expertise

- Workflow design and optimization
- Action development and publishing
- Secret and security management
- Reusable workflow patterns
- Status checks and branch protection
- Matrix builds and parallelization
- Environment configuration
- Artifact management

## Best Practices

### Workflow Structure
- Use descriptive workflow names
- Organize jobs by responsibility
- Use concurrency groups for cancellation
- Pin action versions (avoid `@main`)
- Add helpful comments
- Document workflow purpose

### Performance
- Leverage matrix strategy for parallel builds
- Use conditional steps to skip unnecessary work
- Cache dependencies when possible
- Use self-hosted runners for long-running tasks
- Implement fail-fast logic

### Security
- Use secrets for sensitive data
- Never log sensitive information
- Review action dependencies
- Use least-privilege permissions
- Verify action sources

### Reusability
- Create reusable workflow files
- Use workflow_call for common patterns
- Parametrize with inputs/outputs
- Store in `.github/workflows/` directory
- Document all parameters

## Workflow Rules

### Concurrency Best Practice

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

Benefits:
- Cancel older runs on new push
- Save runner minutes
- Prevent duplicate deployments
- Faster feedback on latest commit

### Permissions Best Practice

```yaml
permissions:
  contents: read
  pull-requests: write
  # Add only what's needed
```

### Secrets Handling

- Store secrets in GitHub Secrets
- Use environment-specific secrets
- Never commit secrets to repository
- Rotate secrets regularly
- Audit secret usage

## Common Patterns

### Matrix Strategy

Used for testing multiple configurations:

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
```

### Conditional Execution

```yaml
if: github.event_name == 'pull_request'
```

### Output Sharing

```yaml
outputs:
  result: ${{ steps.build.outputs.result }}
```

## Troubleshooting

### Check
- Workflow syntax validation with `actionlint`
- Action version compatibility
- Secret availability in environment
- Permission sufficiency

### Debug
- Enable debug logging: `ACTIONS_STEP_DEBUG=true`
- Review workflow run logs
- Check artifact uploads
- Verify environment variables

## File Organization

```
.github/
├── workflows/
│   ├── ci.yml
│   ├── deploy.yml
│   └── scheduled-tasks.yml
├── actions/
│   ├── custom-action-1/
│   └── custom-action-2/
└── skills/
    └── github-actions/
        └── SKILL.md
```

## Critical Rules

- ✅ Always pin action versions
- ✅ Always review secrets access
- ✅ Always test workflows before merging
- ✅ Always document workflow purpose
- ✅ Always use concurrency groups
- ❌ Never log secrets
- ❌ Never use `@main` for production
- ❌ Never commit secrets
- ❌ Never bypass required checks
- ❌ Never disable branch protection
