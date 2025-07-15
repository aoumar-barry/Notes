# FastAPI Documentation Summary

This document provides a concise overview of how to document a FastAPI application, including examples.

---

## 1. Docstring Conventions

Choose a consistent style (Google or NumPy) and include:
- **Short summary** first line.
- **Args/Parameters** with types and descriptions.
- **Returns** section.
- **Raises/Exceptions** section.
- **Examples** or **Notes** where needed.

```python
def create(db: Session, user_in: UserCreate) -> User:
    """
    Create a new user record.

    Args:
        db (Session): SQLAlchemy database session.
        user_in (UserCreate): Payload with `email` and `password`.

    Returns:
        User: Created user instance.

    Raises:
        IntegrityError: If email already exists.
    """
    ...
```

---

## 2. Path Operation Documentation

Use FastAPI’s decorator parameters and docstrings:

```python
@router.post(
    "/users/",
    summary="Register a new user",
    response_description="Created user record",
)
def create_user(
    user_in: UserCreate = Body(..., description="Email & password"),
    db: Session = Depends(get_db),
):
    """Register a new user, hash password before saving."""
    ...
```

---

## 3. Pydantic Model Documentation

Annotate fields with `Field`:

```python
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50,
                      description="Name, 1–50 chars")
    price: float = Field(..., gt=0, description="Positive price")
    class Config:
        schema_extra = {"example": {"name": "Gadget", "price": 19.99}}
```

---

## 4. Custom OpenAPI Schema

Inject metadata, security schemes, logos:

```python
def custom_openapi():
    schema = get_openapi(title="API", version="1.0", routes=app.routes)
    schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http", "scheme": "bearer", "bearerFormat": "JWT"
        }
    }
    schema["info"]["x-logo"] = {"url": "https://example.com/logo.png"}
    return schema

app.openapi = custom_openapi
```

---

## 5. External Docs with Sphinx/MkDocs

- Set up `sphinx` with `autodoc`, `napoleon`, `sphinx_autodoc_typehints`.
- Use `automodule` and `toctree` in `.rst` files.
- Host on ReadTheDocs or GitHub Pages.

---

## 6. README & Changelog

- **README.md**: Quickstart, install, run server, example requests, doc links.
- **CHANGELOG.md**: Follow Keep a Changelog format; tag releases.

---

## 7. Versioning & Deprecations

- URL versioning: `/api/v1`, `/api/v2`.
- Mark endpoints `deprecated=True` with doc warnings.

```python
@router.get("/old", deprecated=True)
def old(): ...
```

---

## 8. Tutorials & Examples

Include inline snippets and external guides:

```python
# Example:
resp = client.get("/api/v1/items/1")
assert resp.status_code == 200
```

---

## 9. Automated Doc Checks

In CI, run:
- `pydocstyle` or `flake8-docstrings`.
- Sphinx build to catch broken links.

---

*End of summary.*
