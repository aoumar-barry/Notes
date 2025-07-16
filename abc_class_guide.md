# Abstract Base Classes (`ABC`) in Python

Abstract Base Classes (`ABC`) in Python provide a way to define interfaces with methods that must be implemented by concrete subclasses. They let you enforce a contract: any subclass of an `ABC` must override its abstract methods, or else you can’t instantiate it. Additionally, they support “virtual subclassing” via `register()`, so you can treat unrelated classes as implementing the same interface.

---

## 1. Brief Explanation (3 lines)
- An `ABC` is a class that can define abstract methods and properties.
- You cannot instantiate an `ABC` unless all its abstract methods are overridden.
- Use it to ensure that subclasses follow a specific API/contract.

## 2. Usage
```python
from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def do_something(self, data):
        """Process data in some way."""
        pass
```

## 3. Code Example
```python
from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def serialize(self, obj) -> str:
        """Convert object to string format."""
        pass

    @abstractmethod
    def deserialize(self, s: str):
        """Reconstruct object from string."""
        pass

class JsonSerializer(Serializer):
    def serialize(self, obj) -> str:
        import json
        return json.dumps(obj)

    def deserialize(self, s: str):
        import json
        return json.loads(s)

# Correct usage
js = JsonSerializer()
print(js.serialize({"a": 1}))  # '{"a": 1}'
```

## 4. Real‑World Scenario
Suppose you’re building a data pipeline library that supports multiple storage backends (JSON, YAML, XML). You can define a single `StorageBackend(ABC)` with `read()` and `write()` abstract methods, then create concrete backends (e.g. `JsonBackend`, `YamlBackend`) that must implement those methods—ensuring consistency across all backends.

## 5. Implementation Notes
- Use `@abstractmethod` for methods and `@property` + `@abstractmethod` for attributes.
- If a subclass fails to implement all abstract methods, attempting instantiation raises `TypeError`.
- Use `MyABC.register(SomeOtherClass)` for virtual subclassing when you want to treat an existing class as a subclass of your interface without inheritance.

## 6. Modern Modules & Alternatives
- **`typing.Protocol`** (Python 3.8+): defines structural subtyping (“duck typing”) without requiring explicit inheritance.
- **`zope.interface`**: a third‑party library offering more powerful interface declarations and component architecture.
- **`pydantic`** or **`attrs`**: for data validation models, often replace simple ABC classes for data-centric designs.

## 7. Further Mastery Recommendations
- **Deepen understanding**: Read [PEP 3119](https://peps.python.org/pep-3119/) on ABCs.
- **Practice**: Build a plugin system using `ABC` + `entry_points`.
- **Compare patterns**: Implement the same interface using both `ABC` and `Protocol` to see pros/cons.
- **Explore**: Look into `functools.singledispatchmethod` for method overloading complementing ABC designs.
