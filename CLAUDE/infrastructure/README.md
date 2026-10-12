# Infrastructure

Infrastructure as Code using Terraform, Kubernetes manifests, and AWS/Azure configurations.

## Structure

- `terraform/` - Terraform configuration files
  - `main.tf` - Main resources
  - `variables.tf` - Input variables
  - `outputs.tf` - Output values
  - `modules/` - Reusable modules
- `kubernetes/` - Kubernetes manifests
  - `deployments/` - Deployment manifests
  - `services/` - Service definitions
  - `configmaps/` - Configuration
- `scripts/` - Infrastructure scripts
- `docs/` - Infrastructure documentation

## Terraform Workflow

### Pre-Commit

```bash
terraform fmt
terraform validate
```

### Before Merge

```bash
terraform plan -out=tfplan
```

### Deployment

```bash
terraform apply tfplan
```

## Rules

- ✅ Always run `terraform fmt` before commit
- ✅ Always run `terraform validate` before commit
- ✅ Always review `terraform plan` before apply
- ✅ Always use remote state
- ✅ Pin all provider versions
- ❌ Never manually modify state files
- ❌ Never commit secrets
- ❌ Never deploy directly without PR approval

## Kubernetes

### Verify Before Apply

```bash
kubectl config current-context
kubectl get nodes
```

### Apply Manifests

```bash
kubectl apply -f kubernetes/
```

### Verify Deployment

```bash
kubectl rollout status deployment/app
```

## Security

- Never commit secrets
- Use AWS Secrets Manager / Azure Key Vault
- Implement RBAC
- Enable encryption
- Regular security audits
- Keep infrastructure patterns documented

## Disaster Recovery

- Maintain backup procedures
- Document recovery processes
- Test failover scenarios
- Keep state backups
- Document rollback procedures

## Change Management

1. Create feature branch
2. Update infrastructure code
3. Run validation checks
4. Create PR with plan output
5. Request review
6. Merge after approval
7. Deploy via pipeline
8. Monitor changes
