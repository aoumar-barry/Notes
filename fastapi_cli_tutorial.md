
# 🐍 FastAPI CLI Launcher Tutorial

This guide helps you set up a **command-line interface (CLI)** for your FastAPI project so you can run your app easily with one command.

---

## ✅ Goal

Create a CLI command like:
```bash
python run.py
```
or even:
```bash
fastapi-cli serve
```

---

## 🛠️ Option 1: Simple `run.py` File (Beginner Friendly)

### 🔹 Step 1: Create a `run.py` file in your project root

```python
# run.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
```

### ✅ Now run:
```bash
python run.py
```

---

## 🛠️ Option 2: Using Typer to Create a CLI Tool (Recommended for Advanced CLI)

### 🔹 Step 1: Install `typer`
```bash
pip install typer[all]
```

### 🔹 Step 2: Create a CLI app file (e.g., `cli.py`)

```python
# cli.py
import typer
import uvicorn

app_cli = typer.Typer()

@app_cli.command()
def serve(
    host: str = "127.0.0.1",
    port: int = 8000,
    reload: bool = True
):
    \"\"\"Serve the FastAPI app\"\"\"
    uvicorn.run("src.main:app", host=host, port=port, reload=reload)

if __name__ == "__main__":
    app_cli()
```

### ✅ Run the app:
```bash
python cli.py serve
```

With custom options:
```bash
python cli.py serve --host 0.0.0.0 --port 9000 --reload False
```

---

## 🛠️ Option 3: Install CLI as a Tool

To install your CLI globally, use `pyproject.toml` if you're using [Poetry](https://python-poetry.org/).

### Example `pyproject.toml`:

```toml
[tool.poetry.scripts]
fastapi-cli = "cli:app_cli"
```

Then install:
```bash
poetry install
```

Now you can run:
```bash
fastapi-cli serve
```

---

## 🧼 Bonus: Project Structure Example

```
project/
│
├── src/
│   └── main.py      # FastAPI app instance lives here (app = FastAPI())
├── cli.py           # Your Typer-based CLI entry point
├── run.py           # Quick launcher
└── pyproject.toml   # Optional for CLI installation
```

---

## ✅ Summary

| Option | Command                        | Best For               |
|--------|--------------------------------|------------------------|
| 1      | `python run.py`               | Quick local dev       |
| 2      | `python cli.py serve`         | CLI customization     |
| 3      | `fastapi-cli serve`           | Full CLI tooling      |
