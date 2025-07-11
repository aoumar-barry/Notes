# 🐍 Pythonic Getters and Setters in Python – Summary

## 📘 What are Getters and Setters?

In Python, **getters and setters** allow controlled access to a class’s private attributes.

### Why Use Them?
- Control attribute access
- Add validation logic
- Encapsulate internal state
- Provide a clean interface

---

## ✅ Pythonic Way: Using `@property`

Instead of defining `get_<attr>()` and `set_<attr>()` methods, Python recommends using `@property` decorators.

---

## 🔓 Basic Example

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, value):  # Setter
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value
```

**Usage:**

```python
p = Person("Alpha")
print(p.name)       # Getter call
p.name = "Barry"    # Setter call
```

---

## 🧪 Example with Validation

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
```

---

## 🔒 Read-Only Property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2
```

**Note:** Setting `c.area = 100` will raise an `AttributeError`.

---

## 🧠 Multiple Parameters in Setter (Workaround)

You can't directly pass multiple arguments to a setter. Use a tuple or dictionary:

### Tuple Example

```python
class Person:
    @property
    def fullname(self):
        return f"{self._first_name} {self._last_name}"

    @fullname.setter
    def fullname(self, name_tuple):
        first, last = name_tuple
        self._first_name = first
        self._last_name = last
```

### Dictionary Example

```python
class Person:
    @fullname.setter
    def fullname(self, name_dict):
        self._first_name = name_dict.get("first", "")
        self._last_name = name_dict.get("last", "")
```

---

## 🧰 Best Practices

| Guideline                  | Explanation                          |
|----------------------------|--------------------------------------|
| Use `@property`            | Cleaner and more Pythonic            |
| Validate in setters        | Prevent invalid state                |
| Use tuples/dicts for multi-arg setters | Python only allows one value  |
| Use read-only properties   | When no external mutation is needed  |

---

## 📌 Final Notes

- Python doesn't enforce private attributes, but we use `_attr` or `__attr` by convention.
- `@property` makes code look cleaner and more maintainable.
- Ideal for situations where you might later need validation or computed values.

---