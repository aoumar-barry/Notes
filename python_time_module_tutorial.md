# Python `time` Module Tutorial

A comprehensive guide to Python’s built-in `time` module with concise one-line descriptions for each function/method, examples, and best practices.

---

## 1. Overview

The `time` module provides tools for working with times and clocks: retrieving timestamps, pausing execution, converting between representations, formatting, parsing, and simple timezone data.

```python
import time
```

---

## 2. Getting the Current Time

### `time.time()`
Returns the current time in seconds since the Epoch (Jan 1, 1970 UTC).
```python
now = time.time()
print(now)  # e.g. 1687142123.456789
```

### `time.perf_counter()`
Provides the highest-resolution timer for measuring short durations.
```python
start = time.perf_counter()
# ... code ...
end = time.perf_counter()
print(f"Elapsed: {end - start:.6f}s")
```

### `time.monotonic()`
Returns a clock that cannot go backwards, suitable for reliable interval measurements.
```python
t1 = time.monotonic()
# ... code ...
t2 = time.monotonic()
print(f"Delta: {t2 - t1:.6f}s")
```

### `time.process_time()`
Measures CPU time consumed by the current process (excluding sleep).
```python
cpu_start = time.process_time()
# ... CPU work ...
cpu_end = time.process_time()
print(f"CPU time: {cpu_end - cpu_start:.6f}s")
```

### `time.thread_time()`
Reports CPU time of the current thread (Python 3.7+).
```python
thread_start = time.thread_time()
# ... thread work ...
thread_end = time.thread_time()
print(f"Thread CPU time: {thread_end - thread_start:.6f}s")
```

---

## 3. Pausing Execution

### `time.sleep(seconds)`
Suspends execution for the given number of seconds (can be fractional).
```python
print("Sleeping for 1.5 seconds...")
time.sleep(1.5)
print("Awake!")
```

---

## 4. Converting Between Timestamps and `struct_time`

Python represents broken-down times as `time.struct_time` tuples:  
`(year, month, day, hour, minute, second, weekday, yearday, isdst)`

### `time.gmtime([timestamp])`
Converts a timestamp to UTC `struct_time`; defaults to now.
```python
utc_struct = time.gmtime()
print(utc_struct)
```

### `time.localtime([timestamp])`
Converts a timestamp to local time `struct_time`; defaults to now.
```python
local_struct = time.localtime()
print(local_struct)
```

### `time.mktime(struct_time)`
Converts a local `struct_time` back to a POSIX timestamp.
```python
ts = time.mktime(local_struct)
print(ts)
```

---

## 5. Formatting and Parsing

### `time.strftime(format, [struct_time])`
Formats a `struct_time` (or current) to a string according to directives.
```python
fmt = "%Y-%m-%d %H:%M:%S"
s = time.strftime(fmt, local_struct)
print(s)  # e.g. "2025-07-03 16:45:00"
```

### `time.strptime(string, format)`
Parses a time string to a `struct_time` using matching directives.
```python
t = time.strptime("2025-07-03 16:45:00", "%Y-%m-%d %H:%M:%S")
print(t)
```

---

## 6. Convenient String Converters

### `time.ctime([timestamp])`
Returns a readable string for a timestamp (local time).
```python
print(time.ctime())  # e.g. "Thu Jul  3 16:45:00 2025"
```

### `time.asctime([struct_time])`
Formats a `struct_time` as a readable string.
```python
print(time.asctime(local_struct))
```

---

## 7. Timezone Helpers

### `time.timezone`
Offset of local (non-DST) timezone from UTC in seconds.
```python
print(time.timezone)
```

### `time.altzone`
Offset of local DST timezone from UTC in seconds.
```python
print(time.altzone)
```

### `time.daylight`
Nonzero if a DST timezone is defined.
```python
print(time.daylight)
```

### `time.tzname`
Tuple of names `(standard, DST)` for the local timezone.
```python
print(time.tzname)
```

---

## 8. Example: Simple Stopwatch Class

```python
import time

class Stopwatch:
    """A simple stopwatch using a high-resolution timer."""
    def __init__(self):
        self._start = None
        self._elapsed = 0.0

    def start(self):
        """Begin timing."""
        if self._start is not None:
            raise RuntimeError("Already running")
        self._start = time.perf_counter()

    def stop(self):
        """Stop timing and accumulate elapsed time."""
        if self._start is None:
            raise RuntimeError("Not running")
        self._elapsed += time.perf_counter() - self._start
        self._start = None

    def reset(self):
        """Reset elapsed time to zero."""
        self._start = None
        self._elapsed = 0.0

    @property
    def elapsed(self):
        """Get total elapsed time."""
        if self._start is not None:
            return self._elapsed + (time.perf_counter() - self._start)
        return self._elapsed

# Usage example
sw = Stopwatch()
sw.start()
time.sleep(0.3)
sw.stop()
print(f"Elapsed: {sw.elapsed:.4f}s")
```

---

## 9. Best Practices

- Use `time.perf_counter()` or `time.monotonic()` for measuring intervals.  
- Avoid `time.time()` for elapsed time logic since it can jump.  
- Remember that `sleep()` can overshoot due to OS scheduling.  
- For complex scheduling, consider `sched` or `threading.Timer`.

---

*End of tutorial.*
