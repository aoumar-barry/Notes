# Uvicorn, ASGI, Gunicorn, Workers & TLS — Quick Reference

_Last updated: 2025-09-17 (Europe/Paris)_

## 1) What is **Uvicorn**?
Uvicorn is a **high‑performance ASGI web server** for Python used to run modern async frameworks like **FastAPI** and **Starlette**.

- Speaks **ASGI** (async successor to WSGI) → handles HTTP & WebSocket.
- Very fast via **uvloop** (event loop) & **httptools** (HTTP parser) when installed as extras.
- Great for local dev (`--reload`) and can be used in production (often behind a reverse proxy/LB).

**Common commands**
```bash
# Install
pip install "uvicorn[standard]"

# Run (module:app)
uvicorn myapp:app --reload                    # dev: auto-reload
uvicorn myapp:app --host 0.0.0.0 --port 8000  # bind and port
uvicorn myapp:app --workers 4                 # multiple processes
```

**With Gunicorn (prod pattern)**
```bash
pip install gunicorn "uvicorn[standard]"
gunicorn -w 4 -k uvicorn.workers.UvicornWorker myapp:app
```

---

## 2) What is **ASGI**?
**ASGI** = **Asynchronous Server Gateway Interface** — a **specification** for how async Python web servers and apps communicate (the async successor to WSGI).

- Supports **async I/O**, **WebSockets**, long‑lived connections, HTTP/2 (via implementations).
- Used by servers (**Uvicorn, Hypercorn, Daphne**) and frameworks (**FastAPI, Starlette, Django ASGI, Quart**, etc.).

**Minimal ASGI app**
```python
# app.py
async def app(scope, receive, send):
    assert scope["type"] == "http"
    await receive()  # wait for request event
    await send({"type": "http.response.start", "status": 200,
                "headers": [(b"content-type", b"text/plain")]})
    await send({"type": "http.response.body", "body": b"Hello, ASGI!"})
```
Run: `uvicorn app:app`

---

## 3) What is **Gunicorn**?
**Gunicorn** (Green Unicorn) is a **WSGI HTTP server** for Python (pre‑fork model: a master spawns multiple worker **processes**).

- Ideal for **WSGI apps** (Flask, Django‑WSGI).
- Can serve **ASGI apps** via **UvicornWorker**: `-k uvicorn.workers.UvicornWorker`.
- Typically placed **behind** a reverse proxy/load‑balancer.

**Examples**
```bash
# WSGI example (Flask)
gunicorn -w 4 -b 0.0.0.0:8000 myapp:wsgi_app

# ASGI example (FastAPI) via Uvicorn workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 myapp:app
```

---

## 4) Uvicorn `--workers` explained
`--workers N` starts **N separate processes** (each with its own event loop).

- **Not** a hard cap of N concurrent requests. Each worker can handle **many** in‑flight requests via `async`/`await` (I/O‑bound).
- Good defaults: start with **≈ CPU cores**; if I/O‑bound, try **cores × 2** and **load test**.
- **Gotchas:** no shared in‑memory state across workers (use Redis/DB), each worker has its own DB pool, more workers use more memory.

**Examples**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
```

---

## 5) Useful Uvicorn flags (cheat‑sheet)
- `--host 0.0.0.0` — listen on all interfaces (containers/VMs)
- `--port 8000` — set port
- `--workers 4` — number of **processes** (multi‑core parallelism)
- `--reload` — auto‑restart on code changes (dev only; forces 1 worker)
- `--reload-dir <path>` / `--reload-include` / `--reload-exclude` — control reload watch
- `--log-level info` — verbosity (`debug|info|warning|error|critical`)
- `--access-log` / `--no-access-log` — enable/disable access logs
- `--proxy-headers` — trust `X-Forwarded-*` (behind proxy/LB)
- `--forwarded-allow-ips '*'` — which proxy IPs to trust
- `--root-path /api` — mount when app is served under a path prefix
- `--env-file .env` — load environment variables
- `--app-dir app` — add base dir to `PYTHONPATH`
- `--factory` — treat `app` as a callable factory
- `--loop uvloop` / `--http httptools` / `--ws websockets` — choose implementations
- `--lifespan on|off|auto` — lifespan events handling
- `--timeout-keep-alive 5` — HTTP keep‑alive timeout
- `--limit-concurrency 1000` — max in‑flight connections per worker
- `--backlog 2048` — socket pending connections queue
- `--ssl-certfile` / `--ssl-keyfile` — serve HTTPS directly (see §6)
- `--server-header`/`--no-server-header`, `--date-header`/`--no-date-header` — toggle headers

**Examples**
```bash
# Dev
uvicorn app:app --reload --log-level debug

# Prod (container)
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4   --proxy-headers --forwarded-allow-ips '*'
```

---

## 6) Using TLS certs from a subfolder
```bash
# Relative subfolder
uvicorn app:app   --host 0.0.0.0 --port 8443   --ssl-certfile ./tls/fullchain.pem \   # certificate/full chain
  --ssl-keyfile  ./tls/privkey.pem       # private key
```

```bash
# Absolute paths
uvicorn app:app --host 0.0.0.0 --port 8443   --ssl-certfile /app/tls/server.crt   --ssl-keyfile  /app/tls/server.key
```

```bash
# With env vars
CERT=./certs/server.crt
KEY=./certs/server.key
uvicorn app:app --host 0.0.0.0 --port 8443   --ssl-certfile "$CERT" --ssl-keyfile "$KEY"
```

> **Note:** Restrict key permissions (e.g., `chmod 600 ./tls/privkey.pem`).

---

## 7) Corporate SSL issues: `--ssl-certfile` vs trust stores
- `--ssl-certfile` solely defines the **server certificate** your app presents for **incoming HTTPS**.  
- It **does not** modify or replace system/Python **CA trust stores** (e.g., `certifi`, `/etc/ssl/certs`). It won’t remove `cacert` or other certs.

**When the issue is outbound (your app calls external HTTPS under a corporate proxy/CA):**
- Add the **corporate root CA** to the trust store or point clients to it.

**Runtime (Python)**
```bash
export SSL_CERT_FILE=/etc/ssl/certs/corp-root-ca.pem
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/corp-root-ca.pem
```

**Per-request in code**
```python
import httpx
httpx.get("https://example.com", verify="/etc/ssl/certs/corp-root-ca.pem")
```

**System trust (Debian/Ubuntu & Alpine)**
```bash
# Copy your corporate CA
cp corp-root-ca.pem /usr/local/share/ca-certificates/corp-root-ca.crt
update-ca-certificates  # updates /etc/ssl/certs/ca-certificates.crt
```

**Tooling env vars**
```bash
# pip
export PIP_CERT=/etc/ssl/certs/corp-root-ca.pem
# git
export GIT_SSL_CAINFO=/etc/ssl/certs/corp-root-ca.pem
# Node (if relevant)
export NODE_EXTRA_CA_CERTS=/etc/ssl/certs/corp-root-ca.pem
```

**When to use `--ssl-certfile`**
- Only if your container **terminates TLS itself**. In many cloud setups (Azure Front Door/Ingress/Nginx), TLS is terminated before the app; then run Uvicorn on plain HTTP (no `--ssl-*`).

---

## 8) Key takeaways
- **Uvicorn**: fast ASGI server. **ASGI**: async contract between servers & apps.
- **Gunicorn**: robust pre‑fork server (WSGI); can run ASGI via **UvicornWorker**.
- `--workers` = number of processes; concurrency per worker comes from **async** code.
- `--ssl-certfile` presents a **server cert**; it **doesn’t change** CA trust stores.
- Corporate SSL/proxy issues for **outgoing** requests are fixed by **adding corporate CA** to trust stores or passing it via env vars/clients.

---

## 9) Quick production baseline (container)
```bash
uvicorn app:app   --host 0.0.0.0 --port 8000 --workers 4   --proxy-headers --forwarded-allow-ips '*'   --log-level info
# Put a reverse proxy / LB (Nginx, Azure Front Door, ACA Ingress) in front.
```
