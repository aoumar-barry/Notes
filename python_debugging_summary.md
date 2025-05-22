# 🐞 Python Debugging Summary Guide

## 🧠 Debugging Mindset
- Debugging is exploration — stay curious.
- Reproduce issues reliably.
- Narrow down issues through elimination.

---

## 🛠 Basic Debugging Tools

### Print Debugging
```python
print(f"Variable x is: {x}")
```

### `pdb` (Python Debugger)
```python
import pdb; pdb.set_trace()
```
Commands: `n`, `c`, `p var`, `q`

### Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug message")
```

---

## 🧪 IDE Debugging in VS Code
- Set breakpoints by clicking the margin.
- Use `F5` to start debugging — not `python main.py`
- Use toolbar or shortcuts:
  - Continue: `F5`
  - Step Over: `F10`
  - Step Into: `F11`
  - Step Out: `Shift+F11`

---

## 🚀 Debug FastAPI with Uvicorn
1. Create `.vscode/launch.json`:
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["main:app", "--reload"],
      "justMyCode": false
    }
  ]
}
```
2. Start debugging → Make an HTTP request → Breakpoint is triggered.

---

## ⚙️ Multiple Debug Configurations
Add multiple entries inside `launch.json > configurations`.

---

## ↩️ Can You Go Back a Line?
No. Python debugging is not reversible. Use restart (`Ctrl+Shift+F5`) and structure code into callable blocks.

---

## 🔄 Restart Debugging
- Use Restart button in the toolbar.
- Shortcut: `Ctrl+Shift+F5`

---

## 📚 Easier Error Reading
- Read stack trace from bottom to top.
- Focus on lines from your code.
- Click error lines in VS Code terminal.

### Optional Enhancer: `rich`
```bash
pip install rich
```
```python
from rich.traceback import install
install()
```

---

## 🎨 RichHandler for Logging
```python
from rich.logging import RichHandler
import logging

logging.basicConfig(
    level="DEBUG",
    format="%(message)s",
    handlers=[RichHandler()]
)
logger = logging.getLogger("rich")
```
