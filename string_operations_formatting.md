
# 🧵 Python String Operations and Formatting

## 🔤 Creating Strings
```python
s1 = 'Hello'
s2 = "World"
s3 = '''Multi-line
string'''
```

## 📏 Length of a String
```python
len("Python")  # 6
```

## 🔄 String Concatenation
```python
greeting = "Hello" + " " + "World"
```

## 🎯 String Repetition
```python
echo = "ha" * 3  # "hahaha"
```

## 🪟 Indexing and Slicing
```python
s = "Python"
first = s[0]      # 'P'
last = s[-1]      # 'n'
part = s[1:4]     # 'yth'
```

## 🧪 Membership Testing
```python
"Py" in "Python"      # True
"java" not in "Python"  # True
```

## 🔁 Iterating Through a String
```python
for char in "Hello":
    print(char)
```

## 🛠️ Common String Methods

| Method           | Example                          | Description                         |
|------------------|----------------------------------|-------------------------------------|
| `lower()`        | `"Python".lower()`               | Convert to lowercase                |
| `upper()`        | `"Python".upper()`               | Convert to uppercase                |
| `strip()`        | `"  hello  ".strip()`            | Remove leading/trailing spaces      |
| `replace()`      | `"hello".replace("l", "x")`      | Replace substrings                  |
| `split()`        | `"a,b,c".split(",")`             | Split into a list                   |
| `join()`         | `",".join(["a", "b", "c"])`      | Join list into string               |
| `find()`         | `"hello".find("e")`              | Find index of substring             |
| `startswith()`   | `"hello".startswith("he")`       | Check prefix                        |
| `endswith()`     | `"hello".endswith("lo")`         | Check suffix                        |
| `isalnum()`      | `"abc123".isalnum()`             | Alphanumeric check                  |
| `isdigit()`      | `"123".isdigit()`                | Digit check                         |

## ✨ String Formatting Methods

### 1. f-Strings (Python 3.6+)
```python
name = "Alice"
age = 30
f"Name: {name}, Age: {age}"
```

### 2. str.format() Method
```python
"Name: {}, Age: {}".format("Bob", 25)
"Name: {1}, Age: {0}".format(25, "Bob")
```

### 3. Percent (%) Formatting
```python
"Name: %s, Age: %d" % ("Charlie", 28)
```

## 🔢 Formatting Numbers
```python
f"{3.14159:.2f}"        # '3.14'
f"{1000:,}"             # '1,000'
f"{0.05:.1%}"           # '5.0%'
```
