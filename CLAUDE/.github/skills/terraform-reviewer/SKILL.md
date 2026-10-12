---
name: terraform-reviewer
description: Expert in Terraform best practices, code review, validation, and infrastructure as code.
---

# Terraform Reviewer Skill

## Expertise

- Terraform validation and formatting
- Infrastructure code review
- State management
- Module design and reusability
- AWS/Azure/GCP resource management
- Remote state configuration
- Security best practices

## Review Checklist

### Format & Syntax
- [ ] Run `terraform fmt` 
- [ ] Run `terraform validate`
- [ ] Check for syntax errors

### Best Practices
- [ ] Verify variable naming conventions
- [ ] Check output definitions
- [ ] Validate remote state setup
- [ ] Review module structure

### Security
- [ ] No hardcoded secrets
- [ ] No exposed credentials
- [ ] Proper IAM permissions
- [ ] Resource encryption enabled

### Dependencies
- [ ] Verify provider versions pinned
- [ ] Check module dependencies
- [ ] Validate data source references

## Workflow

1. Review infrastructure requirements
2. Analyze Terraform code structure
3. Run validation and formatting checks
4. Identify security concerns
5. Suggest optimization improvements
6. Provide remediation steps

## Rules

### Terraform Rules

- Always run `terraform fmt` before commit
- Always run `terraform validate` before commit
- Never manually modify state files
- Always use remote state for shared infrastructure
- Pin provider versions in provider blocks
- Use modules for reusable infrastructure
- Document all variables and outputs

### Security Rules

- Never commit secrets or credentials
- Use Terraform Cloud/Enterprise for sensitive data
- Implement least privilege access
- Enable encryption for sensitive resources
- Use separate state files for different environments

### Deployment Rules

- Always run `terraform plan` before apply
- Review all resource changes carefully
- Test in non-production environments first
- Keep rollback procedures documented
- Verify no resources will be destroyed unexpectedly

## Common Issues to Check

- Unused variables or outputs
- Missing variable descriptions
- Hardcoded values instead of variables
- Missing tags on resources
- Incorrect resource naming
- Missing dependencies between resources
- Insecure default configurations
