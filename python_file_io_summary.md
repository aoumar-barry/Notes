
# 📘 Python File I/O Summary

This guide summarizes the essentials of reading and writing files in Python with examples.

---

## 📂 File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (text). File must exist. |
| `'w'` | Write (text). Truncates file or creates new. |
| `'x'` | Create file, fail if exists. |
| `'a'` | Append to file. |
| `'b'` | Binary mode (e.g. `'rb'`, `'wb'`). |
| `'t'` | Text mode (default). |
| `'+'` | Read and write. Combine like `'r+'`. |

---

## 🔤 Text vs Binary Mode

- **Text (`'r'`, `'w'`)**: Use for human-readable files (`.txt`, `.csv`).
- **Binary (`'rb'`, `'wb'`)**: Use for images, audio, PDFs, etc.

```python
# Read text
with open("example.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Read binary
with open("image.png", "rb") as f:
    data = f.read()
```

---

## 🔁 Looping Through Lines

```python
# Best practice
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Read all lines
with open("file.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# Manual loop
with open("file.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
```

---

## 🧪 Writing Files

```python
# Write text
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, file!")

# Append
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("\nNew line")
```

---

Keep this file for quick reference!
