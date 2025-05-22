
# 📄 Summary: File Paths and Context Managers in Python

## 🔹 File Paths

### ✅ Path Basics
- **Absolute Path**: Complete path from root (`C:\\Users\\...\\file.txt`)
- **Relative Path**: Relative to current working directory (`./data/file.txt`)
- **Best Practice**: Use the `pathlib` module (modern, object-oriented, cross-platform).

### 🧱 Example:
```python
from pathlib import Path
file_path = Path("data") / "sample.txt"
print(file_path.exists())  # Check if file exists
```

### 📁 `.parent` Attribute
- Returns the directory containing the file.
```python
Path("logs/logfile.txt").parent  # Returns: logs
```
- Used to create directories before writing:
```python
file_path.parent.mkdir(parents=True, exist_ok=True)
```

## 🔹 Context Managers (`with` statement)

### 📘 Why Use It?
- Automatically handles file closing.
- Cleaner and safer than manual `open()`/`close()`.

### ✅ Examples:
**Read a file:**
```python
with open("data/sample.txt", "r") as file:
    content = file.read()
```

**Write to a file:**
```python
with open("output.txt", "w") as file:
    file.write("Hello, Microsoft!")
```

## 🔹 File Operations with `Pathlib` Only

### 📖 Reading File:
```python
content = Path("data/sample.txt").read_text()
```

### ✍️ Writing File:
```python
Path("output.txt").write_text("Hello, Microsoft!")
```

### ⚠️ Use Cases:
- ✅ Use `.read_text()` when file is small and text-only.
- ❌ Avoid it for large or binary files — prefer context managers for those.
