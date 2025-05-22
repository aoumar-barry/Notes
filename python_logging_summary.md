
# 🧾 Python Logging: Professional Summary

## 🔍 What is Logging?
Logging is the practice of recording messages that describe the runtime behavior of an application. It helps with debugging, auditing, monitoring, and understanding how software operates.

## ⚙️ Basic Logging Setup
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug message")
```

## 🔢 Logging Levels (Low to High)
| Level    | Description                         |
|----------|-------------------------------------|
| DEBUG    | Detailed info for diagnosing issues |
| INFO     | General operational messages        |
| WARNING  | Unexpected situations, not fatal    |
| ERROR    | Serious problems in the program     |
| CRITICAL | Severe errors causing shutdown      |

## 🪛 Creating and Using Loggers
```python
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
```
### Why `__name__`?
- Ties logger to the module name.
- Helps track which module emitted each log.

### Why `setLevel(logging.DEBUG)`?
- Sets the minimum level the logger will handle.
- Controls verbosity of logs.

## 🎯 Common Formatter Used
```python
'%(asctime)s - %(levelname)s - %(name)s - %(funcName)s:%(lineno)d - %(message)s'
```
### What It Includes:
- Timestamp, Log Level, Logger Name, Function Name, Line Number, Message

## 📂 Logging to Files and Console
```python
file_handler = logging.FileHandler("my_log.log")
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(console_handler)
```

## 🧰 Reusable Logger Class (With Rotation)
```python
from logging.handlers import TimedRotatingFileHandler

class Logger:
    def __init__(self, name: str, log_dir: str = "logs"):
        ...  # Refer to full code above

    def get_logger(self):
        return self.logger
```
### Features:
- Logs to both console and file
- Daily log rotation with backups
- Standard format for clarity

## ✅ Best Practices
- Use module-level loggers: `getLogger(__name__)`
- Avoid `print()` for anything beyond quick tests
- Never log sensitive data
- Use log rotation for maintainability
- Separate levels for console and file if needed

---

This setup reflects modern, professional, and industry-standard logging practices, ideal for production and scalable codebases.
