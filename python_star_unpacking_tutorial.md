
# 🧯 Python `*` and `**` Unpacking Explained

This guide explains the use of `*` (single asterisk) and `**` (double asterisk) in Python for unpacking and flexible function definitions.

---

## ✅ 1. Function Definitions

### 🔹 `*args`: Collects Extra Positional Arguments

```python
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")
```

### 🔹 `**kwargs`: Collects Extra Keyword Arguments

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Paris")
```

---

## ✅ 2. Function Calls

### 🔹 `*` to Unpack a List/Tuple

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))  # equivalent to add(1, 2, 3)
```

### 🔹 `**` to Unpack a Dictionary

```python
def greet(name, age):
    print(f"{name} is {age} years old.")

person = {"name": "Alice", "age": 30}
greet(**person)
```

---

## ✅ 3. Enforcing Keyword-only Arguments with `*`

```python
def send_email(to, *, subject, body):
    print(f"To: {to}, Subject: {subject}, Body: {body}")

send_email("alice@example.com", subject="Hello", body="Welcome!")
```

❌ This would raise an error:

```python
send_email("alice@example.com", "Hello", "Welcome")  # Error!
```

---

## ✅ 4. Unpacking in Variable Assignment

```python
first, *middle, last = [10, 20, 30, 40, 50]
print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

---

## ✅ 5. Unpacking in List Construction

```python
a = [1, 2, 3]
b = [4, 5]
merged = [*a, *b, 6]
print(merged)  # [1, 2, 3, 4, 5, 6]
```

---

## ✅ 6. Unpacking in Loops

```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

for num, letter in pairs:
    print(num, letter)
```

### 🔹 Partial Unpacking in Loop

```python
items = [(1, 2, 3), (4, 5, 6)]

for first, *rest in items:
    print(f"First: {first}, Rest: {rest}")
```

---

## ✅ 7. Unpacking in Expressions

```python
def values():
    return [1, 2, 3]

result = [0, *values(), 4]
print(result)  # [0, 1, 2, 3, 4]
```

---

## 📌 Summary Table

| Syntax          | Meaning                                    |
| --------------- | ------------------------------------------ |
| `*args`         | Collects extra positional arguments        |
| `**kwargs`      | Collects extra keyword arguments           |
| `*` (call)      | Unpacks list/tuple into separate arguments |
| `**` (call)     | Unpacks dict into named keyword arguments  |
| `*` (signature) | Forces keyword-only parameters             |

