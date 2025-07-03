```python 
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-module-name"
version = "0.1.0"
description = "A greeting utility"
authors = [{name = "Your Name", email = "your@email.com"}]
readme = "README.md"
license = {text = "MIT"}
dependencies = []

[project.optional-dependencies]
dev = [
    "black",
    "pytest",
    "mypy"
]
docs = [
    "mkdocs",
    "mkdocs-material"
]
tool = [
    "some-tool-package",
    "another-tool-lib"
] 

[project.urls]
Homepage = "https://github.com/yourname/my_module"
```

```sh
    pip install build
    python -m build
    pip install twine
    twine upload dist/*
    pip install dist/my_module_name-0.1.0-py3-none-any.whl

    ## You can host it on github and install it 
    pip install git+https://github.com/yourname/my_module.git

```

    
