# Python Project Setup with **uv** and VS Code

A clean, modern, repeatable setup for a Python project in VS Code using **uv** (fast package & env manager). This assumes Windows; macOS/Linux differences are noted.

---

## 1) Install prerequisites

1. **Python 3.11+** (recommended 3.12)
2. **uv**

```powershell
# Windows PowerShell
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
```
*(macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`)*

---

## 2) Create your project (src layout + managed venv)

```powershell
# Create folder & initialize
mkdir myapp && cd myapp
uv init --package  # pyproject.toml + src/ + tests/ scaffold

# Create a local .venv and pin Python
uv venv --seed
uv python pin 3.12

# Install deps from pyproject (none yet, but sets editable install)
uv sync
```

If you didn’t use `uv init`, use this **minimal pyproject**:

```toml
[project]
name = "myapp"
version = "0.1.0"
description = "Example app"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[project.scripts]
myapp = "myapp.__main__:main"   # uv run myapp

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

**Project tree (goal):**
```
myapp/
  .venv/                     # created by uv venv
  pyproject.toml
  uv.lock
  src/
    myapp/
      __init__.py
      __main__.py
      main.py
  tests/
    test_main.py
  .gitignore
  .vscode/
    settings.json
    launch.json
```

---

## 3) Add dev tools & first dependencies

```powershell
# Dev tools (formatter+lint+tests)
uv add --group dev ruff pytest

# Example runtime dep (pick what you need)
uv add rich
uv sync
```

---

## 4) Starter code

**`src/myapp/main.py`**
```python
from rich import print

def hello(name: str = "world") -> str:
    msg = f"Hello, {name}!"
    print(f"[bold green]{msg}")
    return msg
```

**`src/myapp/__main__.py`**
```python
from .main import hello

def main() -> None:
    hello()

if __name__ == "__main__":
    main()
```

**`tests/test_main.py`**
```python
from myapp.main import hello

def test_hello():
    assert hello("Alpha") == "Hello, Alpha!"
```

**Run it:**
```powershell
uv run myapp          # uses [project.scripts]
uv run pytest -q
```

---

## 5) VS Code setup

Install extensions: **Python** (Microsoft), **Pylance**, **Ruff**.

**`.vscode/settings.json`**
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
  "python.terminal.activateEnvironment": true,
  "python.analysis.typeCheckingMode": "basic",
  "editor.formatOnSave": true,
  "[python]": { "editor.defaultFormatter": "charliermarsh.ruff" },
  "ruff.organizeImports": true
}
```
*(macOS/Linux: set interpreter to `${workspaceFolder}/.venv/bin/python`)*

**`.vscode/launch.json`** (debug your package entry or a file)
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run myapp (module)",
      "type": "python",
      "request": "launch",
      "module": "myapp",
      "console": "integratedTerminal"
    },
    {
      "name": "Run main.py (file)",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/src/myapp/main.py",
      "console": "integratedTerminal"
    },
    {
      "name": "Pytests",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["-q"],
      "console": "integratedTerminal"
    }
  ]
}
```

---

## 6) Daily workflow with uv

- Add runtime deps: `uv add fastapi uvicorn` (example)  
- Add dev-only deps: `uv add --group dev ruff pytest`  
- Sync lockfile/env: `uv sync`  
- Run anything: `uv run python -m myapp` or `uv run pytest`  
- Pin Python: `uv python pin 3.12`  
- Upgrade deps (respecting constraints): `uv sync --upgrade`  
- Build sdist/wheel: `uv build`

---

## 7) Optional: FastAPI quick-start

```powershell
uv add fastapi uvicorn
```
**`src/myapp/api.py`**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```
**Run:**
```powershell
uv run uvicorn myapp.api:app --reload --host 0.0.0.0 --port 8000
```

---

## 8) Nice-to-haves

**`.gitignore`**
```
.venv/
__pycache__/
*.pyc
dist/
.build/
.pytest_cache/
# Decide with your team whether to commit the lockfile:
# uv.lock
```

**Ruff on save, tests on demand**
```powershell
uv run ruff check --fix
uv run ruff format
uv run pytest -q
```

---

### Notes
- Commit `uv.lock` for reproducible builds across machines (recommended for apps); for libraries, teams sometimes omit it.
- If VS Code doesn’t auto-pick the interpreter, run the **Python: Select Interpreter** command and choose the `.venv` one.
- On CI, you can use `uv sync --frozen` to enforce the lockfile.
