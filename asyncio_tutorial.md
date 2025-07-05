
# 🌀 Python `asyncio` Module: Full Tutorial

## ✅ What is `asyncio`?

`asyncio` is a Python standard library for writing concurrent code using the async/await syntax. It enables asynchronous programming by allowing you to run multiple operations concurrently without using threads or processes.

It is ideal for:
- I/O-bound tasks (networking, file I/O, database access)
- High-level structured concurrency
- Event loops, tasks, coroutines

---

## 🧠 Core Concepts

| Concept     | Description |
|-------------|-------------|
| `coroutine` | A special function you define with `async def`, that can be paused/resumed with `await` |
| `await`     | Waits for a coroutine to finish and gives control back to the event loop |
| `event loop`| The engine that executes asynchronous tasks |
| `Task`      | A wrapper for a coroutine that lets it run concurrently |
| `gather()`  | Runs multiple coroutines concurrently and waits for all |
| `create_task()` | Schedules execution of a coroutine |

---

## 🛠️ Setup Example: Coroutine + Event Loop

```python
import asyncio

async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)
    print("...world!")

asyncio.run(say_hello())
```

---

## 🔄 Running Multiple Coroutines Concurrently

```python
async def task(name, delay):
    print(f"Starting {name}")
    await asyncio.sleep(delay)
    print(f"Finished {name} after {delay} seconds")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
    )

asyncio.run(main())
```

---

## 🚀 Creating Tasks with `create_task()`

```python
async def task(name, delay):
    print(f"Start {name}")
    await asyncio.sleep(delay)
    print(f"End {name}")

async def main():
    t1 = asyncio.create_task(task("task1", 2))
    t2 = asyncio.create_task(task("task2", 1))
    print("Waiting for tasks...")
    await t1
    await t2

asyncio.run(main())
```

---

## ⛓️ Sequential vs Concurrent Comparison

### 🔁 Sequential

```python
async def slow_task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} done")

async def main():
    await slow_task("Task1", 2)
    await slow_task("Task2", 2)

asyncio.run(main())
```

### ⚡ Concurrent

```python
async def slow_task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} done")

async def main():
    await asyncio.gather(
        slow_task("Task1", 2),
        slow_task("Task2", 2)
    )

asyncio.run(main())
```

---

## 🧲 `asyncio.sleep()` vs `time.sleep()`

- `time.sleep()` blocks the whole program.
- `asyncio.sleep()` yields control back to the event loop — non-blocking.

---

## 🔁 Example: Asynchronous Web Requests (Using `aiohttp`)

```bash
pip install aiohttp
```

```python
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: {response.status}")
            return await response.text()

async def main():
    urls = ["https://httpbin.org/get", "https://example.com"]
    await asyncio.gather(*(fetch(url) for url in urls))

asyncio.run(main())
```

---

## 💥 Exception Handling in Coroutines

```python
async def risky_task():
    raise ValueError("Something went wrong")

async def main():
    try:
        await risky_task()
    except Exception as e:
        print(f"Caught an error: {e}")

asyncio.run(main())
```

---

## ⛔ Common Pitfalls

| Problem                        | Fix |
|-------------------------------|-----|
| `RuntimeError: Event loop is closed` | Use `asyncio.run()` only once per program |
| `await` outside async function | Use `await` only inside `async def` |
| Blocking code (e.g. `time.sleep`) | Replace with `await asyncio.sleep()` |

---

## 📦 Useful asyncio APIs Summary

| Function / Class         | Description |
|--------------------------|-------------|
| `asyncio.run(coro)`      | Run a coroutine |
| `await asyncio.sleep()`  | Non-blocking delay |
| `asyncio.gather(*coros)` | Run multiple coroutines concurrently |
| `asyncio.create_task()`  | Schedule coroutine to run concurrently |
| `asyncio.get_event_loop()` | Get the current event loop |
| `asyncio.Queue()`        | Thread-safe producer/consumer queue |

---

## 🧪 Real-World Use Case: Asynchronous File Processing

```python
import asyncio

async def read_file(name):
    await asyncio.sleep(1)
    print(f"Reading {name}")
    return f"Content of {name}"

async def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    results = await asyncio.gather(*(read_file(f) for f in files))
    print(results)

asyncio.run(main())
```

---

## ⏲ When to Use `asyncio`

✅ Use `asyncio` when:
- Making many I/O calls (HTTP, database, disk)
- Building APIs with FastAPI or websockets

❌ Avoid it for:
- CPU-intensive operations (use multiprocessing/threading)
