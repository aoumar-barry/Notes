
# Python Package Management with pip

## 1. What is `pip`?
`pip` is the package installer for Python. It allows you to install and manage additional libraries and dependencies that are not part of the Python standard library.

## 2. Basic Commands
```bash
# Install a package
pip install package_name

# Install a specific version
pip install package_name==1.2.3

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show details of an installed package
pip show package_name

# Freeze installed packages
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

## 3. Virtual Environments
```bash
# Create a virtual environment
python -m venv env_name

# Activate it (Windows)
env_name\Scripts\activate

# Activate it (macOS/Linux)
source env_name/bin/activate

# Deactivate when done
deactivate
```

## 4. Using `requirements.txt`
Example content:
```
requests==2.28.1
numpy>=1.21,<1.25
```

## 5. Advanced Usage
```bash
# Editable installs for local development
pip install -e .

# Installing from GitHub
pip install git+https://github.com/username/repo.git

# Checking for outdated packages
pip list --outdated

# Installing extras
pip install flask[async]
```

## 6. Best Practices
- Always use virtual environments.
- Pin versions in `requirements.txt` for reproducibility.
- Avoid installing unnecessary packages globally.
- Regularly update your dependencies.
- Use `pip-tools` or `Poetry` for advanced dependency management.
