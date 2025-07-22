# Git Hooks and Pre-Commit for Python Developers

This document summarizes our discussion on managing Git hooks and using the `pre-commit` framework to automate code formatting, linting, and custom workflows for Python projects.

---

## 1. Introduction to Git Hooks

- **What Are Git Hooks?**  
  Scripts that Git runs at key points (e.g., `pre-commit`, `commit-msg`, `pre-push`, `post-merge`).  
- **Client-Side vs. Server-Side**  
  - Client-side: run locally on actions like commit or push.  
  - Server-side: run on the server (e.g., enforcing policies on PRs).

---

## 2. Basic Manual Hook Example

- Created a `pre-commit` hook script in `.git/hooks/pre-commit`.  
- Example: run `black --check .` and reject unformatted commits.  
- Drawbacks: machine-specific, hard to share, not versioned.

---

## 3. Introducing Pre-Commit Framework

- Stores hook configs in `.pre-commit-config.yaml`.  
- Installs/manage hooks in `.git/hooks/`.  
- Supports community repos for formatters, linters, security checks, etc.

---

## 4. Installing and Configuring Pre-Commit

```bash
pip install pre-commit
```

Example `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]
  - repo: https://gitlab.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

Install hooks:

```bash
pre-commit install
pre-commit run --all-files
```

---

## 5. Common Formatting Hooks

- **Black:** auto-formats Python.  
- **isort:** sorts imports.  
- **Flake8:** linting and quality checks.

---

## 6. Writing Custom Hooks

- Create `.githooks/` directory.  
- Write scripts (e.g., check license header).  
- Reference via `repo: local` in `.pre-commit-config.yaml`.

---

## 7. Enforcing Hooks in CI

- Use GitHub Actions workflow to run `pre-commit run --all-files` on PRs and pushes.  
- Blocks merges when checks fail.

---

## 8. Best Practices

- Pin hook versions.  
- Commit `.pre-commit-config.yaml`.  
- Educate team to install hooks.  
- Use `pre-commit autoupdate`.  
- Cache hooks on CI.

---

## 9. Cool Python Hook Ideas

1. **Commit Message Conventions**  
2. **Auto-Bump Version from Git Tags**  
3. **Strip Debug Statements**  
4. **Convert Jupyter Notebooks to .py**  
5. **Update CHANGELOG.md**  
6. **Run Security Scans**  
7. **Notify Slack on Merge**  
8. **Auto-Run DB Migrations**  
9. **Pre-Populate Commit Templates**  
10. **Custom GitPython Scripts**

---

## 10. Implementing with Pre-Commit

- **Directory Layout:**

  ```
  .githooks/
  .pre-commit-config.yaml
  ```

- **Config Example:**

  ```yaml
  repos:
    - repo: local
      hooks:
        - id: enforce-commit-msg
          entry: python3 .githooks/commit_msg.py
          stages: [commit-msg]
        # ... other hooks ...
  ```

- **Installation:**

  ```bash
  pre-commit install --hook-type commit-msg
  pre-commit install
  ```

---

## 11. Community-Maintained Hooks

| Idea                                    | Hook                                   | Repo / ID                                       |
|-----------------------------------------|----------------------------------------|--------------------------------------------------|
| Commit message conventions              | gitlint                                | https://github.com/jorisroovers/gitlint, `gitlint` |
| Strip debug statements                  | flake8-print, flake8-debugger          | sobolevn/flake8-print, `/flake8-debugger`         |
| Security scans                          | detect-secrets, pre-commit-safety      | Yelp/detect-secrets, pyupio/pre-commit-safety     |
| Others (version bump, notebooks, etc.)  | _No official; use `local` scripts_     |                                                  |

For non-official hooks (bumping versions, notebooks, changelog, Slack, migrations, templates), keep small scripts in `.githooks/` and reference as `repo: local`.

---

*End of summary.*
