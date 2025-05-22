
# Python Exceptions Summary

## 🚨 What Are Exceptions?
Exceptions are errors detected during execution. Python provides many built-in exceptions and allows custom ones.

---

## 🛠️ Handling Exceptions

### Basic Try-Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### Catching Multiple
```python
try:
    pass
except (TypeError, ValueError) as e:
    print(f"An error occurred: {e}")
```

### Else and Finally
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result is {result}")
finally:
    print("Execution completed.")
```

---

## 🧩 Custom Exceptions

### Define
```python
class CustomError(Exception):
    pass
```

### With Attributes
```python
class ValidationError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)
```

### Raise
```python
def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative", 1001)
```

### Handle
```python
try:
    validate_age(-5)
except ValidationError as e:
    print(f"Error: {e.message} (Code: {e.code})")
```

---

## 📚 Common Built-in Exceptions

- `ZeroDivisionError`
- `IndexError`
- `KeyError`
- `TypeError`
- `ValueError`
- `AttributeError`
- `ImportError`
- `FileNotFoundError`
- `OSError`
- `RuntimeError`

_For full list, see: https://docs.python.org/3/library/exceptions.html_

---

## 📺 Video Resource
[Custom Exceptions Tutorial](https://www.youtube.com/watch?v=CK0wc85inxk&utm_source=chatgpt.com)
