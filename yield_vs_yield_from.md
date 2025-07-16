# Difference Between `yield` and `yield from`

## Overview

- **`yield`** produces a single value from a generator.
- **`yield from`** delegates to another iterable or generator, automatically yielding all its values and forwarding sends/exceptions, and capturing return values.

## Basic `yield`

```python
def gen_simple(n):
    for i in range(n):
        yield i
```

Each call to `next()` on `gen_simple(3)` yields `0`, then `1`, then `2`.

## Manual delegation with `yield`

```python
def proxy_manual(iterable):
    # Manually loop through the iterable
    for item in iterable:
        yield item * 2
```

You must write an explicit loop to proxy values from another iterable.

## Using `yield from`

```python
def proxy_with_yield_from(iterable):
    # Automatically delegate to the iterable
    yield from iterable
```

This single line replaces the manual loop, forwarding all values directly.

## Capturing return values with `yield from`

```python
def child():
    yield 1
    return "done"

def parent():
    # `yield from` captures the return value of `child()`
    result = yield from child()
    print("child returned:", result)
```

Iterating over `parent()` yields `1` and then prints `"child returned: done"`.

## Comparison Table

| Aspect                 | `yield`                         | `yield from`                              |
|------------------------|---------------------------------|-------------------------------------------|
| Yields                 | One value per `yield`           | All values from the given iterable        |
| Delegation boilerplate | Manual loop                     | Built-in, no explicit loop               |
| `.send()` forwarding   | Not forwarded                   | Automatically forwarded                  |
| Capture return value   | Not possible                    | Captures return value of sub-generator   |

## Conclusion

- Use **`yield`** for simple generators that produce values directly.
- Use **`yield from`** when delegating to sub-generators or iterables, especially to benefit from automatic delegation of values, exceptions, and return values.
