#!/usr/bin/env python3
"""
Jenkins to GitHub Actions Converter
Converts Declarative Jenkinsfiles to GitHub Actions YAML workflows — fully offline.

Usage:
    python jenkins_to_gha.py Jenkinsfile
    python jenkins_to_gha.py Jenkinsfile -o .github/workflows/ci.yml
    python jenkins_to_gha.py Jenkinsfile --verbose

Supported mappings:
    agent any/none/label/docker  → runs-on / container
    environment {}               → env:
    stage('X') { steps {} }     → job with steps
    sh / bat / powershell        → run:
    checkout scm                 → actions/checkout@v4
    when { branch 'X' }         → if: github.ref == ...
    when { tag '...' }          → if: startsWith(github.ref, 'refs/tags/')
    post { always/success/failure } → if: always() / success() / failure()
    input {}                    → environment: (manual approval gate)
    withCredentials             → secrets reference comment
    junit                       → dorny/test-reporter@v1
    archiveArtifacts            → actions/upload-artifact@v4
    publishHTML                 → actions/upload-artifact@v4
    docker build/push           → run: docker ...
    kubectl                     → run: kubectl ...
    tools { nodejs/jdk/maven }  → setup-node / setup-java
    BUILD_NUMBER                → github.run_number
    BRANCH_NAME                 → github.ref_name
    GIT_COMMIT                  → github.sha
    $PASS / $TOKEN / $SECRET    → secrets.*
"""

import re
import sys
import argparse
from pathlib import Path


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def strip_line_comments(text):
    return re.sub(r"//[^\n]*", "", text)


def extract_brace_body(text, open_pos):
    depth = 0
    start = None
    for i in range(open_pos, len(text)):
        if text[i] == "{":
            depth += 1
            if start is None:
                start = i + 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start:i]
    return text[start:] if start else ""


def find_block(text, keyword):
    m = re.search(rf"\b{re.escape(keyword)}\s*\{{", text, re.DOTALL)
    return extract_brace_body(text, m.end() - 1) if m else None


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_agent(text):
    if re.search(r"\bagent\s+none\b", text):
        return None
    if re.search(r"\bagent\s+any\b", text):
        return "ubuntu-latest"
    agent_body = find_block(text, "agent")
    if agent_body:
        img = re.search(r"\bimage\s+['\"]([^'\"]+)['\"]", agent_body)
        if img:
            return f"docker:{img.group(1)}"
        label = re.search(r"\blabel\s+['\"]([^'\"]+)['\"]", agent_body)
        if label:
            return f"self-hosted  # label: {label.group(1)}"
    return "ubuntu-latest"


def parse_environment(text):
    env_body = find_block(text, "environment")
    if not env_body:
        return {}
    env = {}
    for line in env_body.splitlines():
        m = re.match(r"\s*(\w+)\s*=\s*['\"]?([^'\"]+?)['\"]?\s*$", line)
        if m:
            env[m.group(1)] = m.group(2).strip()
    return env


def parse_tools(text):
    tools_body = find_block(text, "tools")
    if not tools_body:
        return {}
    tools = {}
    for tool in ("jdk", "maven", "nodejs", "gradle", "python"):
        m = re.search(rf"\b{tool}\s+['\"]([^'\"]+)['\"]", tools_body, re.IGNORECASE)
        if m:
            tools[tool] = m.group(1)
    return tools


def parse_options(text):
    opts_body = find_block(text, "options")
    if not opts_body:
        return []
    opts = []
    if re.search(r"\bskipDefaultCheckout\b", opts_body):
        opts.append("skip_checkout")
    m = re.search(r"\btimeout\s*\(.*?time:\s*(\d+).*?unit:\s*['\"]?(\w+)['\"]?\s*\)", opts_body)
    if m:
        opts.append(f"timeout:{m.group(1)}:{m.group(2)}")
    return opts


def parse_when(text):
    when_body = find_block(text, "when")
    if not when_body:
        return None
    cond = {}
    m = re.search(r"\bbranch\s+['\"]([^'\"]+)['\"]", when_body)
    if m:
        cond["branch"] = m.group(1)
    m = re.search(r"\btag\s+(?:pattern:\s*)?['\"]([^'\"]+)['\"]", when_body)
    if m:
        cond["tag"] = m.group(1)
    m = re.search(r"\benvironment\s+name:\s*['\"]([^'\"]+)['\"],\s*value:\s*['\"]([^'\"]+)['\"]", when_body)
    if m:
        cond["env"] = (m.group(1), m.group(2))
    not_m = re.search(r"\bnot\s*\{", when_body)
    if not_m:
        inner = extract_brace_body(when_body, not_m.end() - 1)
        nb = re.search(r"\bbranch\s+['\"]([^'\"]+)['\"]", inner)
        if nb:
            cond["not_branch"] = nb.group(1)
    return cond if cond else None


def parse_post(text):
    post_body = find_block(text, "post")
    if not post_body:
        return {}
    result = {}
    for cond in ("always", "success", "failure", "unstable", "changed", "cleanup"):
        body = find_block(post_body, cond)
        if body:
            result[cond] = extract_step_list(body)
    return result


def parse_input_block(text):
    input_body = find_block(text, "input")
    if not input_body:
        return None
    m = re.search(r"\bmessage\s+['\"]([^'\"]+)['\"]", input_body)
    return {"message": m.group(1) if m else "Proceed?"}


def parse_stages(text):
    stages_body = find_block(text, "stages")
    if not stages_body:
        return []
    return _parse_stage_list(stages_body)


def _parse_stage_list(text):
    stages = []
    pattern = re.compile(r"\bstage\s*\(\s*['\"]([^'\"]+)['\"]\s*\)\s*\{", re.DOTALL)
    for m in pattern.finditer(text):
        name = m.group(1)
        body = extract_brace_body(text, m.end() - 1)
        stages.append({
            "name": name,
            "steps": _get_steps(body),
            "when": parse_when(body),
            "environment": parse_environment(body),
            "post": parse_post(body),
            "parallel": _get_parallel(body),
            "input": parse_input_block(body),
            "agent": _get_stage_agent(body),
        })
    return stages


def _get_stage_agent(text):
    m = re.search(r"\bagent\s+(\w+)\b", text)
    if m and m.group(1) not in ("any", "none"):
        return m.group(1)
    return None


def _get_parallel(text):
    parallel_body = find_block(text, "parallel")
    if not parallel_body:
        return []
    return _parse_stage_list(parallel_body)


def _get_steps(text):
    steps_body = find_block(text, "steps")
    return extract_step_list(steps_body) if steps_body else []


# ---------------------------------------------------------------------------
# Step extraction
# ---------------------------------------------------------------------------

CRED_HINTS = {"PASS", "PASSWORD", "TOKEN", "SECRET", "KEY", "CREDENTIAL", "CRED"}


def jenkins_var_to_gha(text):
    def replacer(m):
        var = m.group(1) or m.group(2) or ""
        if any(h in var.upper() for h in CRED_HINTS):
            return "${{{{ secrets.{} }}}}".format(var)
        mapping = {
            "BUILD_NUMBER": "${{ github.run_number }}",
            "BUILD_ID": "${{ github.run_number }}",
            "BRANCH_NAME": "${{ github.ref_name }}",
            "GIT_COMMIT": "${{ github.sha }}",
            "GIT_SHA": "${{ github.sha }}",
        }
        return mapping.get(var, "${{{{ env.{} }}}}".format(var))
    return re.sub(r"\$\{(\w+)\}|\$(\w+)", replacer, text)


def derive_name(cmd):
    cmd_clean = re.sub(r"\$\{\{[^}]*\}\}", "VAR", cmd)
    parts = cmd_clean.strip().split()
    if not parts:
        return "Run"
    first = parts[0].lstrip("./")
    second = parts[1] if len(parts) > 1 else ""
    for prefix in ("npm", "yarn", "npx", "mvn", "mvnw", "gradle", "gradlew",
                   "make", "pip", "pip3", "python", "python3", "go", "cargo", "dotnet"):
        if first == prefix:
            return f"{first} {second}".strip()
    if first in ("kubectl", "docker", "helm", "aws", "gcloud", "az"):
        return f"{first} " + " ".join(parts[1:3])
    if first == "echo":
        return "Print message"
    return first.capitalize()


def extract_step_list(text):
    """Return list of step dicts."""
    if not text:
        return []

    steps = []

    def run(cmd, shell="sh", name=None):
        cmd = jenkins_var_to_gha(cmd.strip())
        steps.append({"kind": "run", "cmd": cmd, "shell": shell,
                      "name": name or derive_name(cmd)})

    def action(uses, params=None, name=None):
        steps.append({"kind": "action", "uses": uses,
                      "with": params or {}, "name": name or uses.split("@")[0].split("/")[-1]})

    def comment(msg):
        steps.append({"kind": "comment", "text": msg})

    # Remove nested withCredentials / withEnv / sshagent blocks before scanning sh/run
    clean_text = text

    for wrapper in ("withCredentials", "withEnv", "sshagent"):
        for m in re.finditer(rf"\b{wrapper}\s*\(.*?\)\s*\{{", clean_text, re.DOTALL):
            inner = extract_brace_body(clean_text, m.end() - 1)
            if wrapper == "withCredentials":
                comment("Credentials: replace vars below with ${{ secrets.VAR_NAME }}")
            elif wrapper == "sshagent":
                comment("SSH agent — use webfactory/ssh-agent@v0 instead")
            steps.extend(extract_step_list(inner))
        # blank out these blocks so we don't double-parse them
        clean_text = re.sub(
            rf"\b{wrapper}\s*\(.*?\)\s*\{{.*?\}}",
            "",
            clean_text,
            flags=re.DOTALL,
        )

    # checkout scm
    if re.search(r"\bcheckout\s+scm\b", clean_text):
        steps.append({"kind": "checkout"})

    # sh / bat / powershell — triple-quoted
    for m in re.finditer(
        r"\b(sh|bat|powershell)\s+(?:script:\s*)?(?:'''(.*?)'''|\"\"\"(.*?)\"\"\")",
        clean_text, re.DOTALL
    ):
        shell = {"sh": "sh", "bat": "cmd", "powershell": "pwsh"}[m.group(1)]
        cmd = (m.group(2) or m.group(3) or "").strip()
        run(cmd, shell)

    # sh / bat / powershell — single-quoted inline
    for m in re.finditer(
        r"\b(sh|bat|powershell)\s+(?:script:\s*)?(?:'([^']*)'|\"([^\"]*)\")",
        clean_text
    ):
        shell = {"sh": "sh", "bat": "cmd", "powershell": "pwsh"}[m.group(1)]
        cmd = (m.group(2) or m.group(3) or "").strip()
        run(cmd, shell)

    # junit
    for m in re.finditer(r"\bjunit\s+(?:testResults:\s*)?['\"]([^'\"]+)['\"]", clean_text):
        action("dorny/test-reporter@v1", {
            "name": "Test results", "path": m.group(1), "reporter": "java-junit",
        }, name="Publish test results")

    # archiveArtifacts
    for m in re.finditer(r"\barchiveArtifacts\s+artifacts:\s*['\"]([^'\"]+)['\"]", clean_text):
        action("actions/upload-artifact@v4", {"name": "artifacts", "path": m.group(1)},
               name="Upload artifacts")

    # publishHTML
    m = re.search(r"\bpublishHTML\s*\(.*?reportDir:\s*['\"]([^'\"]+)['\"].*?\)",
                  clean_text, re.DOTALL)
    if m:
        action("actions/upload-artifact@v4", {"name": "html-report", "path": m.group(1)},
               name="Upload HTML report")

    # stash
    for m in re.finditer(r"\bstash\s+(?:name:\s*)?['\"]([^'\"]+)['\"]", clean_text):
        comment(f"stash '{m.group(1)}' — use upload-artifact + download-artifact across jobs")

    # slackSend
    m = re.search(r"\bslackSend\s+.*?message:\s*['\"]([^'\"]+)['\"]", clean_text, re.DOTALL)
    if m:
        action("slackapi/slack-github-action@v1.27.0", {
            "channel-id": "deployments",
            "slack-message": jenkins_var_to_gha(m.group(1)),
        }, name="Slack notification")

    # mail
    m = re.search(r"\bmail\s+to:\s*['\"]([^'\"]+)['\"].*?subject:\s*['\"]([^'\"]+)['\"]",
                  clean_text, re.DOTALL)
    if m:
        comment(f"mail to {m.group(1)} — add an email notification action here")

    return steps


# ---------------------------------------------------------------------------
# YAML generation
# ---------------------------------------------------------------------------

def when_to_if(when):
    parts = []
    if "branch" in when:
        parts.append(f"github.ref == 'refs/heads/{when['branch']}'")
    if "not_branch" in when:
        parts.append(f"github.ref != 'refs/heads/{when['not_branch']}'")
    if "tag" in when:
        parts.append("startsWith(github.ref, 'refs/tags/')")
    if "env" in when:
        k, v = when["env"]
        parts.append(f"env.{k} == '{v}'")
    return " && ".join(parts) if parts else "true"


def post_cond(cond):
    return {"always": "always()", "success": "success()", "failure": "failure()",
            "unstable": "failure()", "cleanup": "always()", "changed": "always()"}.get(cond, "always()")


def emit_steps(steps, pad="      "):
    lines = []
    for step in steps:
        k = step["kind"]
        if k == "checkout":
            lines.append(f"{pad}- uses: actions/checkout@v4")
        elif k == "run":
            cmd = step["cmd"]
            lines.append(f"{pad}- name: {step['name']}")
            if "\n" in cmd:
                lines.append(f"{pad}  run: |")
                for ln in cmd.splitlines():
                    lines.append(f"{pad}    {ln.rstrip()}")
            else:
                lines.append(f"{pad}  run: {cmd}")
            if step.get("shell") == "cmd":
                lines.append(f"{pad}  shell: cmd")
            elif step.get("shell") == "pwsh":
                lines.append(f"{pad}  shell: pwsh")
        elif k == "action":
            lines.append(f"{pad}- name: {step.get('name', step['uses'])}")
            lines.append(f"{pad}  uses: {step['uses']}")
            if step.get("with"):
                lines.append(f"{pad}  with:")
                for wk, wv in step["with"].items():
                    lines.append(f"{pad}    {wk}: {wv}")
        elif k == "comment":
            lines.append(f"{pad}# {step['text']}")
    return lines


def infer_branches(stages):
    branches = []
    for s in stages:
        w = s.get("when")
        if w and "branch" in w and w["branch"] not in branches:
            branches.append(w["branch"])
    return branches or ["main"]


def generate_yaml(parsed, verbose=False):
    stages = parsed["stages"]
    env = parsed["environment"]
    post = parsed["post"]
    tools = parsed["tools"]
    options = parsed["options"]
    agent = parsed["agent"]
    branches = infer_branches(stages)

    out = [
        "# Auto-generated by jenkins_to_gha.py",
        "# Review: runners, secrets, branch names, deployment targets.",
        "",
        "name: CI/CD",
        "",
        "on:",
        "  push:",
        "    branches:",
    ] + [f"      - {b}" for b in branches] + [
        "  pull_request:",
        "    branches:",
    ] + [f"      - {b}" for b in branches] + [
        "  workflow_dispatch:",
        "",
        "concurrency:",
        "  group: ${{ github.workflow }}-${{ github.ref }}",
        "  cancel-in-progress: true",
        "",
        "permissions:",
        "  contents: read",
        "  packages: write",
        "",
    ]

    if env:
        out.append("env:")
        for k, v in env.items():
            out.append(f"  {k}: {v}")
        out.append("")

    out.append("jobs:")

    skip_checkout = "skip_checkout" in options
    timeout_minutes = None
    for opt in options:
        if opt.startswith("timeout:"):
            _, t, unit = opt.split(":")
            timeout_minutes = int(t) if unit.upper().startswith("MIN") else int(t) * 60

    prev_id = None
    first_job = True

    for stage in stages:
        job_id = re.sub(r"[^a-zA-Z0-9_-]", "_", stage["name"].lower())
        job_id = re.sub(r"_+", "_", job_id).strip("_") or "job"

        out.append(f"  {job_id}:")
        out.append(f"    name: {stage['name']}")

        runner = stage.get("agent") or agent or "ubuntu-latest"
        if runner and runner.startswith("docker:"):
            out += ["    runs-on: ubuntu-latest", "    container:",
                    f"      image: {runner[7:]}"]
        else:
            out.append(f"    runs-on: {runner or 'ubuntu-latest'}")

        if prev_id:
            out.append(f"    needs: {prev_id}")
        if stage["when"]:
            out.append(f"    if: {when_to_if(stage['when'])}")
        if timeout_minutes:
            out.append(f"    timeout-minutes: {timeout_minutes}")
        if stage["input"]:
            out += ["    environment:",
                    f"      name: manual-approval  # gate: \"{stage['input']['message']}\""]
        if stage["environment"]:
            out.append("    env:")
            for k, v in stage["environment"].items():
                out.append(f"      {k}: {v}")

        out.append("    steps:")

        # Checkout on first job unless stage already has one or skip_checkout set
        if first_job and not skip_checkout:
            has_checkout = any(s["kind"] == "checkout" for s in stage["steps"])
            if not has_checkout:
                out.append("      - uses: actions/checkout@v4")

        # Tool setup on first job
        if first_job and tools:
            if "jdk" in tools:
                ver_m = re.search(r"\d+", tools["jdk"])
                out += ["      - uses: actions/setup-java@v4", "        with:",
                        f"          java-version: '{ver_m.group() if ver_m else 17}'",
                        "          distribution: temurin"]
            if "nodejs" in tools:
                ver_m = re.search(r"\d+", tools["nodejs"])
                out += ["      - uses: actions/setup-node@v4", "        with:",
                        f"          node-version: '{ver_m.group() if ver_m else 20}'"]
            if "python" in tools:
                ver_m = re.search(r"[\d.]+", tools["python"])
                out += ["      - uses: actions/setup-python@v5", "        with:",
                        f"          python-version: '{ver_m.group() if ver_m else 3.11}'"]
            if "maven" in tools:
                out += ["      - uses: actions/setup-java@v4", "        with:",
                        "          java-version: '17'", "          distribution: temurin"]

        # Parallel stages
        if stage["parallel"]:
            out.append("      # Parallel stages — consider a matrix strategy for true parallelism")
            for ps in stage["parallel"]:
                out.append(f"      # --- parallel: {ps['name']} ---")
                out.extend(emit_steps(ps["steps"]))
        else:
            out.extend(emit_steps(stage["steps"]))

        # Stage-level post
        for cond, psteps in stage["post"].items():
            gha_cond = post_cond(cond)
            for step in psteps:
                step_lines = emit_steps([step])
                if step_lines:
                    out.extend(step_lines)
                    for idx in range(len(out) - 1, -1, -1):
                        if re.match(r"\s+- (name|uses):", out[idx]):
                            out.insert(idx + 1, f"        if: {gha_cond}")
                            break

        out.append("")
        prev_id = job_id
        first_job = False

    # Global post → notify job
    if post:
        out += ["  notify:", "    name: Notifications", "    runs-on: ubuntu-latest",
                f"    needs: {prev_id}", "    if: always()", "    steps:"]
        for cond, psteps in post.items():
            gha_cond = post_cond(cond)
            for step in psteps:
                step_lines = emit_steps([step])
                if step_lines:
                    out.extend(step_lines)
                    for idx in range(len(out) - 1, -1, -1):
                        if re.match(r"\s+- (name|uses):", out[idx]):
                            out.insert(idx + 1, f"        if: {gha_cond}")
                            break
        out.append("")

    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_jenkinsfile(text):
    text = strip_line_comments(text)
    pipeline_m = re.search(r"\bpipeline\s*\{", text)
    if not pipeline_m:
        raise ValueError(
            "No 'pipeline { }' block found.\n"
            "This converter supports Declarative Pipelines only.\n"
            "Scripted pipelines (node { }) require manual conversion."
        )
    body = extract_brace_body(text, pipeline_m.end() - 1)
    return {
        "agent": parse_agent(body),
        "environment": parse_environment(body),
        "stages": parse_stages(body),
        "post": parse_post(body),
        "options": parse_options(body),
        "tools": parse_tools(body),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Convert a Declarative Jenkinsfile to GitHub Actions YAML (offline, stdlib only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("jenkinsfile", help="Path to Jenkinsfile")
    parser.add_argument("-o", "--output",
                        help="Output file path (default: stdout). E.g. .github/workflows/ci.yml")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Print stage summary to stderr")
    args = parser.parse_args()

    path = Path(args.jenkinsfile)
    if not path.exists():
        print(f"Error: '{path}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        parsed = parse_jenkinsfile(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        print(f"Parse error: {exc}", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print(f"Agent    : {parsed['agent']}", file=sys.stderr)
        print(f"Env vars : {list(parsed['environment'].keys())}", file=sys.stderr)
        print(f"Tools    : {parsed['tools']}", file=sys.stderr)
        print(f"Stages ({len(parsed['stages'])}):", file=sys.stderr)
        for s in parsed["stages"]:
            flags = []
            if s["when"]: flags.append(f"when={s['when']}")
            if s["parallel"]: flags.append(f"parallel({len(s['parallel'])})")
            if s["input"]: flags.append("input")
            suffix = f"  [{', '.join(flags)}]" if flags else ""
            print(f"  • {s['name']}{suffix}", file=sys.stderr)
        print(f"Post     : {list(parsed['post'].keys())}", file=sys.stderr)

    yaml_out = generate_yaml(parsed, verbose=args.verbose)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(yaml_out, encoding="utf-8")
        print(f"✓ Written to {out_path}")
    else:
        print(yaml_out)


if __name__ == "__main__":
    main()
