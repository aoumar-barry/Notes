
# 📘 Python Built-in Types – Methods Summary with Examples

This document summarizes the **most important methods and functions** for key Python built-in types with **examples** and **comments**.

---

## 🔢 int (Integer)

```python
abs(-5)            # Absolute value → 5
pow(2, 3)          # 2 raised to the power 3 → 8
int("42")          # Convert string to int → 42
(10).bit_length()  # Bits to represent 10 → 4
```

---

## ✅ bool (Boolean)

```python
bool(1)      # True because 1 is truthy
bool("")     # False because empty string is falsy

True and False  # → False
True or False   # → True
not True        # → False
```

---

## 🌡️ float (Floating Point)

```python
round(3.14159, 2)       # Round to 2 decimals → 3.14
float("3.14")           # Convert string to float → 3.14
(3.0).is_integer()      # True because 3.0 is a whole number
```

---

## 🧵 str (String)

```python
"hello".upper()         # Uppercase → "HELLO"
"HELLO".lower()         # Lowercase → "hello"
"  test  ".strip()      # Trim spaces → "test"
"abcabc".replace("a", "x")  # Replace → "xbcxbc"
"a,b,c".split(",")      # Split → ['a', 'b', 'c']
"-".join(["a", "b", "c"])  # Join → "a-b-c"
"hello".find("e")       # Index of 'e' → 1
"123".isdigit()         # Check digits → True
```

---

## 📦 list (List)

```python
numbers = [1, 2, 3]
numbers.append(4)       # Add element
numbers.extend([5, 6])  # Add multiple
numbers.insert(2, 99)   # Insert at index
numbers.remove(99)      # Remove by value
numbers.pop()           # Remove last
numbers.index(3)        # Index of value
numbers.count(2)        # Count of value
numbers.sort()          # Sort list
numbers.reverse()       # Reverse list
copy_list = numbers.copy()  # Shallow copy
numbers.clear()         # Remove all
```

---

## ⚙️ array.array (Typed Numeric Array)

```python
from array import array
a = array('i', [1, 2, 3])
a.append(4)             # Add one item
a.extend([5, 6])        # Add multiple
a.insert(0, 99)         # Insert at beginning
a.pop()                 # Remove last
a.remove(99)            # Remove by value
a.buffer_info()         # Memory info
a.tolist()              # Convert to list
```

---

## 📚 dict (Dictionary)

```python
person = {"name": "Alpha", "age": 25}
person.get("name")          # Safe access → "Alpha"
person.get("email", "N/A")  # Fallback → "N/A"
person["email"] = "a@b.com" # Add or update key

person.pop("email")         # Remove by key
person.popitem()            # Remove last item
person.clear()              # Remove all items

person.keys()               # Get keys
person.values()             # Get values
person.items()              # Get key-value pairs

person.update({"age": 26})  # Update from another dict
person.setdefault("lang", "Python")  # Add if not exist

# Dict comprehension
{x: x**2 for x in range(3)}  # → {0: 0, 1: 1, 2: 4}
```

---

## 🧱 object (Base Object Methods)

```python
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self): return f"User({self.name})"
    def __repr__(self): return f"User(name='{self.name}')"

u = User("Alpha")
str(u)                     # → "User(Alpha)"
repr(u)                    # → "User(name='Alpha')"
isinstance(u, User)        # → True
hasattr(u, "name")         # → True
getattr(u, "name")         # → "Alpha"
setattr(u, "name", "New")  # Set new value
```

---

This summary gives you practical, commonly used methods across Python core data types.
