# 📄 Python SSL Handling with certifi, Corporate CA, and Docker

## 🔹 1. What is `certifi`?

`certifi` is a Python package that provides Mozilla's list of trusted root certificates in a `cacert.pem` file.
Used by libraries like `requests`, `httpx`, and `urllib3` to validate SSL certificates.

### 🔧 Install and Use

```bash
pip install certifi
```

```python
import certifi
print(certifi.where())  # Show path to cacert.pem
```

---

## 🔹 2. What is `cacert.pem`?

`cacert.pem` is a PEM-encoded bundle of trusted root certificates used for SSL verification.

### 🔍 Sample Content

```
-----BEGIN CERTIFICATE-----
MIID...==
-----END CERTIFICATE-----
```

This is where trusted CAs are stored. It's used in verifying HTTPS connections.

---

## 🔹 3. Common SSL Error in Corporate Networks

```
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]
```

Occurs when your corporate proxy uses a custom CA that is not in `certifi` or the system trust store.

---

## 🔹 4. Solutions to SSL Errors

### ✅ A. Append CA to certifi

```bash
cat internal_ca.crt >> $(python -m certifi)
```

Or in Python:

```python
import certifi
with open(certifi.where(), "ab") as f:
    f.write(b"\n")
    f.write(open("internal_ca.crt", "rb").read())
```

### ✅ B. Use `verify` parameter

```python
requests.get("https://your-internal-url.com", verify="internal_ca.crt")
```

### ✅ C. Set Environment Variables

```bash
export REQUESTS_CA_BUNDLE=/path/to/internal_ca.crt
export SSL_CERT_FILE=/path/to/internal_ca.crt
```

### ❌ D. Disable SSL Verification (NOT recommended for production)

```python
requests.get("https://url", verify=False)
```

```python
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

---

## 🔹 5. Use in Docker

### 🐳 Dockerfile Example

```dockerfile
FROM python:3.11-slim
RUN apt-get update && apt-get install -y ca-certificates curl
COPY internal_ca.crt /usr/local/share/ca-certificates/internal_ca.crt
RUN update-ca-certificates
RUN pip install certifi
RUN cat /usr/local/share/ca-certificates/internal_ca.crt >> $(python -m certifi)
ENV SSL_CERT_FILE=$(python -m certifi)
ENV REQUESTS_CA_BUNDLE=$(python -m certifi)
```

### 🐳 docker-compose.yml

```yaml
services:
  app:
    build: .
    volumes:
      - ./internal_ca.crt:/usr/local/share/ca-certificates/internal_ca.crt
    environment:
      - SSL_CERT_FILE=/usr/local/share/ca-certificates/internal_ca.crt
      - REQUESTS_CA_BUNDLE=/usr/local/share/ca-certificates/internal_ca.crt
```

---

## 🔹 6. System-wide Certificate Locations

| OS      | Path                               |
| ------- | ---------------------------------- |
| Ubuntu  | /etc/ssl/certs/ca-certificates.crt |
| RedHat  | /etc/pki/tls/certs/ca-bundle.crt   |
| macOS   | System Keychain                    |
| Windows | Windows Cert Store                 |

---

## 🔹 7. Application-specific Certificate Paths

| App/Library | Default Certificate Location/Control  |
| ----------- | ------------------------------------- |
| `requests`  | `certifi.where()`                     |
| `curl`      | Varies (`curl --version`)             |
| `OpenSSL`   | ENV: `SSL_CERT_FILE`                  |
| `Java`      | `$JAVA_HOME/lib/security/cacerts`     |
| `Node.js`   | `NODE_EXTRA_CA_CERTS=/path/to/ca.pem` |
| `git`       | Configurable: `http.sslCAInfo`        |

---

## 🔹 8. Verify Inside Docker

```bash
docker exec -it <container> bash
python -c "import requests; print(requests.get('https://your-internal-url.com'))"
```

---

## ✅ Final Tips

- Always prefer proper CA installation over `verify=False`
- Use `certifi.where()` to locate the trusted CA bundle
- Corporate environments may require appending internal CA to both system store and certifi
- Environment variables help standardize CA location across libraries

---

Let me know if you want this exported as PDF or extended with Java/Node examples.
