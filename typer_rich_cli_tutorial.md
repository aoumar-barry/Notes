
# ⚙️ Typer + Rich CLI App Tutorial

This tutorial teaches you how to build powerful CLI apps using [Typer](https://typer.tiangolo.com) and [Rich](https://rich.readthedocs.io).

---

## 🧱 1. Install the Tools

```bash
pip install typer[all] rich
```

---

## 🔹 2. Basic CLI with Typer

```python
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    app()
```

Run with:
```bash
python app.py hello Alice
```

---

## 🔹 3. Add Optional Flags and Default Values

```python
@app.command()
def greet(name: str, excited: bool = typer.Option(False, help="Add excitement")):
    msg = f"Hello, {name}"
    if excited:
        msg += "!!!"
    print(msg)
```

---

## 🔹 4. Use Prompts

```python
@app.command()
def signup():
    name = typer.prompt("What's your name?")
    age = typer.prompt("Your age?", type=int)
    print(f"Welcome {name}, age {age}")
```

---

## 🔹 5. Rich Console Output

```python
from rich.console import Console
console = Console()

@app.command()
def styled(name: str):
    console.print(f"[bold magenta]Hello {name}[/bold magenta]!")
```

---

## 🔹 6. Rich Panels and Emojis

```python
from rich.panel import Panel

@app.command()
def welcome():
    console.print(Panel("🎉 [green]Welcome to the CLI App![/green]"))
```

---

## 🔹 7. Command Groups (Subcommands)

```python
user = typer.Typer()
admin = typer.Typer()
app.add_typer(user, name="user")
app.add_typer(admin, name="admin")

@user.command()
def create(name: str):
    console.print(f"Created user: [cyan]{name}[/cyan]")

@admin.command()
def ban(name: str):
    console.print(f"🚫 Banned user: [red]{name}[/red]")
```

---

## 🔹 8. Progress Bars and Status (Rich)

```python
from time import sleep
from rich.progress import track

@app.command()
def download():
    for step in track(range(10), description="Downloading..."):
        sleep(0.3)
```

---

## 🔹 9. Validate Input with Enums

```python
from enum import Enum

class Role(str, Enum):
    admin = "admin"
    user = "user"

@app.command()
def set_role(role: Role):
    console.print(f"Role set to [blue]{role}[/blue]")
```

---

## 🔹 10. Exit Codes and Errors

```python
@app.command()
def risky_action(confirm: bool = False):
    if not confirm:
        console.print("[red]Use --confirm to proceed[/red]")
        raise typer.Exit(code=1)
    console.print("[green]Action completed[/green]")
```

---

## ✅ Conclusion

- Use **Typer** for structure and automatic CLI generation.
- Use **Rich** for beautiful terminal output.
- Build modular, modern CLI apps with zero boilerplate.

Happy CLI building! 🚀
