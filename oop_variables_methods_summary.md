
# 🧠 Python OOP: Variables & Methods Quick Review

This is a concise guide on Python object-oriented programming focusing on variables and method types.

---

## 🔁 Class vs Instance Variables

### 🔹 Class Variable
- Declared directly inside the class.
- Shared by **all instances**.
- Can be accessed via class or instance.

```python
class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(Dog.species)    # Canine
print(dog1.species)   # Canine
```

### 🔹 Instance Variable
- Defined inside `__init__` or instance methods.
- **Unique** to each object.

---

## 🧱 Variable Shadowing

Instance variable can override a class variable **for that object only**:

```python
class Example:
    value = 10

    def __init__(self):
        self.value = 20

obj = Example()
print(obj.value)      # 20
print(Example.value)  # 10

del obj.value
print(obj.value)      # 10 (falls back to class-level)
```

---

## ⚙️ Method Types

### 🔸 Instance Method (`self`)
- Can access/modify instance & class data.
```python
class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")
```

### 🔸 Class Method (`@classmethod`)
- First parameter is `cls` (class).
- Can access/modify class-level data.
```python
class Tool:
    version = "1.0"

    @classmethod
    def info(cls):
        return f"Tool version: {cls.version}"
```

### 🔸 Static Method (`@staticmethod`)
- No access to instance or class.
- Utility functions tied to class.

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y
```

---

## ✨ Summary Table

| Feature           | Access Instance | Access Class | Purpose                         |
|------------------|------------------|--------------|---------------------------------|
| Instance Method   | ✅               | ✅           | Object behavior                 |
| Class Method      | ❌               | ✅           | Class-wide behavior             |
| Static Method     | ❌               | ❌           | General utility (self-contained)|
| Class Variable    | Shared by all    | ✅           | Global state for class          |
| Instance Variable | Unique per obj   | ✅           | Object-specific state           |

---

Use this for quick brushing up before coding or interviews!
