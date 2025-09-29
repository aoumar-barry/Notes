# FastAPI Exception Handling Guide

This document summarizes different ways to handle exceptions in **FastAPI**.

---

## 1. Registering Multiple Exception Handlers Separately

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Handle ValueError
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": "Invalid value", "message": str(exc)},
    )

# Handle KeyError
@app.exception_handler(KeyError)
async def key_error_handler(request: Request, exc: KeyError):
    return JSONResponse(
        status_code=404,
        content={"error": "Missing key", "message": str(exc)},
    )

@app.get("/test/{case}")
def test_exceptions(case: int):
    if case == 1:
        raise ValueError("Bad number!")
    elif case == 2:
        raise KeyError("Missing field!")
    else:
        return {"msg": "All good!"}
```

---

## 2. Handling Multiple Exceptions in One Handler

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler((ValueError, KeyError))
async def multiple_exceptions_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"error": type(exc).__name__, "message": str(exc)},
    )

@app.get("/test/{case}")
def test_exceptions(case: int):
    if case == 1:
        raise ValueError("Something wrong with the value")
    elif case == 2:
        raise KeyError("This key is missing")
    else:
        return {"msg": "No errors!"}
```

---

## 3. Catch-All Exception Handler

```python
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "message": str(exc)},
    )
```

---

## 4. Combining Specific Handlers with a Fallback

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": "ValueError", "message": str(exc)},
    )

@app.exception_handler(KeyError)
async def key_error_handler(request: Request, exc: KeyError):
    return JSONResponse(
        status_code=404,
        content={"error": "KeyError", "message": str(exc)},
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "UnexpectedError", "message": str(exc)},
    )

@app.get("/test/{case}")
def test_exceptions(case: int):
    if case == 1:
        raise ValueError("Bad number provided!")
    elif case == 2:
        raise KeyError("Missing required key!")
    elif case == 3:
        raise RuntimeError("Some unknown runtime failure!")
    else:
        return {"msg": "Everything is fine ✅"}
```

---

## 5. Organizing Handlers in a Separate File

### 📂 Project Structure

```
.
├── main.py
└── exceptions.py
```

### `exceptions.py`

```python
from fastapi import Request
from fastapi.responses import JSONResponse

async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": "ValueError", "message": str(exc)},
    )

async def key_error_handler(request: Request, exc: KeyError):
    return JSONResponse(
        status_code=404,
        content={"error": "KeyError", "message": str(exc)},
    )

async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "UnexpectedError", "message": str(exc)},
    )
```

### `main.py`

```python
from fastapi import FastAPI
from exceptions import (
    value_error_handler,
    key_error_handler,
    general_exception_handler,
)

app = FastAPI()

# Register handlers
app.add_exception_handler(ValueError, value_error_handler)
app.add_exception_handler(KeyError, key_error_handler)
app.add_exception_handler(Exception, general_exception_handler)

@app.get("/test/{case}")
def test_exceptions(case: int):
    if case == 1:
        raise ValueError("Bad number provided!")
    elif case == 2:
        raise KeyError("Missing required key!")
    elif case == 3:
        raise RuntimeError("Some unknown runtime failure!")
    else:
        return {"msg": "Everything is fine ✅"}
```

---

## 6. Registering All Exceptions at Once

### `exceptions.py`

```python
from fastapi import Request
from fastapi.responses import JSONResponse

async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": "ValueError", "message": str(exc)},
    )

async def key_error_handler(request: Request, exc: KeyError):
    return JSONResponse(
        status_code=404,
        content={"error": "KeyError", "message": str(exc)},
    )

async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "UnexpectedError", "message": str(exc)},
    )

EXCEPTION_HANDLERS = {
    ValueError: value_error_handler,
    KeyError: key_error_handler,
    Exception: general_exception_handler,
}
```

### `main.py`

```python
from fastapi import FastAPI
from exceptions import EXCEPTION_HANDLERS

app = FastAPI()

# Register all exception handlers in one loop
for exc_class, handler in EXCEPTION_HANDLERS.items():
    app.add_exception_handler(exc_class, handler)

@app.get("/test/{case}")
def test_exceptions(case: int):
    if case == 1:
        raise ValueError("Bad number provided!")
    elif case == 2:
        raise KeyError("Missing required key!")
    elif case == 3:
        raise RuntimeError("Unknown runtime error!")  # goes to catch-all
    else:
        return {"msg": "Everything is fine ✅"}
```

---

## ✅ Summary

- You can **register handlers separately** for each exception type.  
- You can **group multiple exceptions** in one handler.  
- You can create a **catch-all handler** for unexpected errors.  
- You can **combine specific handlers with a general fallback**.  
- You can **organize exception handlers in a separate file**.  
- You can **register all exception handlers in one loop** for cleaner code.

This way your FastAPI app stays organized and predictable when handling errors.
