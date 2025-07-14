# UV from Zero to Hero — Summary

## 1. Install `uv`

```bash
# Linux/macOS (via install script)
curl -Ls https://astral.sh/uv/install.sh | bash

# or Homebrew
brew install astral-sh/uv/uv

# or Cargo
cargo install uv

# Verify
uv --version
```

---

## 2. Initialize Project & Virtual Environment

```bash
mkdir myapp
cd myapp

# Create and activate .venv
uv venv
# on Unix/macOS:
source .venv/bin/activate
# on Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

---

## 3. Project Structure & Code

```
myapp/
├── src/
│   └── myapp/
│       ├── __init__.py
│       └── core.py        # your module code
├── tests/                 # optional tests
│   └── test_core.py
├── README.md
└── pyproject.toml
```

### Example `core.py`

```python
# src/myapp/core.py
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"
```

---

## 4. Provided `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "myapp"
version = "0.1.0"
description = "A short description of your app"
readme = "README.md"
requires-python = ">=3.7"
authors = [{ name = "Your Name", email = "you@example.com" }]
license = { text = "MIT" }
keywords = ["example", "myapp"]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "fastapi>=0.116.1",
    "uvicorn>=0.35.0",
]

[project.urls]
"Homepage" = "https://example.com/myapp"
"Source"   = "https://github.com/you/myapp"

[tool.setuptools.packages.find]
where   = ["src"]
include = ["myapp*"]
```

---

## 5. Manage Dependencies with `uv`

```bash
# Install runtime deps (into .venv)
uv pip install fastapi uvicorn

# Install dev tools
uv pip install pytest build twine

# Freeze exact versions
uv pip freeze > requirements.txt

# Compile lock file (optional)
uv pip compile pyproject.toml -o requirements.lock.txt

# Sync your environment
uv pip sync requirements.lock.txt
```

---

## 6. Testing

```bash
pytest
```

---

## 7. Build Your Distribution

```bash
python -m build
```

---

## 8. Publish to PyPI

```bash
twine upload dist/*
# (Optional) Test on TestPyPI
twine upload --repository testpypi dist/*
```

---

## 9. Install & Verify

```bash
pip install dist/myapp-0.1.0-py3-none-any.whl
# or after publishing
pip install myapp
```

---

## 10. Quick Recap of `uv` Commands

| Task                                | Command                                          |
|-------------------------------------|--------------------------------------------------|
| Install `uv`                        | `brew install astral-sh/uv/uv` or install script |
| Create & activate virtualenv        | `uv venv` → `source .venv/bin/activate`          |
| Install packages                    | `uv pip install <pkg>`                           |
| Freeze dependencies                 | `uv pip freeze > requirements.txt`               |
| Compile lock file                   | `uv pip compile pyproject.toml -o requirements.lock.txt` |
| Sync environment                    | `uv pip sync requirements.lock.txt`              |
