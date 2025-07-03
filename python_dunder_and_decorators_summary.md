# Summary of Python Dunder Names and Decorators

This document provides an overview of special double-underscore (`__`) names in Python (dunder names) and a tutorial on decorators, with examples and key concepts.

---

## 1. Dunder (“__”) Names in Python

### 1.1 Name Mangling
- **Definition**: Identifiers in class definitions starting with two underscores (and not ending with two) are name-mangled.
- **Usage**: Prevents accidental access/subclass collisions.
- **Example**:
  ```python
  class C:
      def __init__(self):
          self.__secret = 42

  c = C()
  print(c._C__secret)  # → 42
  ```

### 1.2 Special Methods (Magic Methods)
Implement or hook into built-in operations. Define in classes; use via operators/functions.
| Operation          | Method          | Syntax Example     |
|--------------------|-----------------|--------------------|
| Initialization     | `__init__`      | `obj = MyClass()`  |
| Representation     | `__repr__`      | `repr(obj)`        |
| String Conversion  | `__str__`       | `str(obj)`         |
| Length             | `__len__`       | `len(obj)`         |
| Addition           | `__add__`       | `a + b`            |
| Iteration          | `__iter__`, `__next__` | `for x in obj:`  |
| Context Manager    | `__enter__`, `__exit__` | `with obj:`     |

### 1.3 Common Special Attributes
- `__name__`: Name of module, class, or function.
- `__doc__`: Docstring.
- `__file__`: Path for modules.
- `__class__`: Class of instance.
- `__dict__`: Attribute namespace.
- `__mro__`: Method Resolution Order (classes).
- `__bases__`: Base classes tuple.
- `__slots__`: Memory/attributes control.
- `__annotations__`: Type hints.
- `__all__`: Public names for `from module import *`.

### 1.4 Module-Level & Under-the-Hood Attributes
- **Module metadata**: `__package__`, `__loader__`, `__spec__`, `__cached__`.
- **Weak references**: `__weakref__`.
- **Subclass hooks**: `__init_subclass__`, `__subclasscheck__`, `__instancecheck__`.
- **Custom preparation**: `__prepare__` in metaclasses.

### 1.5 Best Practices
1. Don’t create your own `__foo__`.
2. Use name mangling sparingly.
3. Implement relevant magic methods to support Python idioms.
4. Document any non-obvious dunder methods in docstrings.

### 1.6 Quick Example
```python
class Vector:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __bool__(self):
        return bool(self.x or self.y)
```

---

## 2. Decorators in Python

### 2.1 What Is a Decorator?
A decorator is a callable that takes a function (or class) and returns a new one with modified behavior.

```python
decorated = decorator(original)
```

### 2.2 Functions Are First-Class
```python
def greet(name):
    return f"Hello, {name}"

say_hi = greet
print(say_hi("Alice"))
```

### 2.3 Simple Decorator
```python
def announce(func):
    def wrapper(*args, **kwargs):
        print("→ Calling", func.__name__)
        result = func(*args, **kwargs)
        print("← Done", func.__name__)
        return result
    return wrapper

@announce
def say(name):
    print("Hi,", name)
```

### 2.4 `@` Syntax
Syntactic sugar: `@announce` is equivalent to `say = announce(say)`.

### 2.5 Preserving Metadata with `functools.wraps`
```python
import functools

def announce(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("→ Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

### 2.6 Decorators with Arguments
```python
def prefixer(prefix):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix}→", func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@prefixer("LOG ")
def add(a, b):
    return a + b
```

### 2.7 Common Built-In Decorators
- `@staticmethod`, `@classmethod`
- `@property`
- `@functools.lru_cache(maxsize=…)`

### 2.8 Chaining Decorators
```python
@d1
@d2
def f(...):
    ...
# => f = d1(d2(f))
```

### 2.9 Decorating Classes
```python
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def get(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get

@singleton
class Database: ...
```

### 2.10 Practical Examples

#### 2.10.1 Timing Execution
```python
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper
```

#### 2.10.2 Access Control
```python
def requires_role(role):
    def dec(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kw):
            if user.role != role:
                raise PermissionError("Forbidden")
            return func(user, *args, **kw)
        return wrapper
    return dec
```

### 2.11 Best Practices
1. Always use `@functools.wraps`.
2. Keep signatures flexible (`*args, **kwargs`).
3. Avoid unintended side effects.
4. Document decorated behavior.

### 2.12 Further Reading
- [PEP 318 – Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
- Fluent Python, Chapter on Decorators
