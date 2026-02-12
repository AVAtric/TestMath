# TestMath - Factorial Calculator

A small but complete factorial calculator package with both iterative and recursive implementations, plus a CLI interface.

## Features

- ✅ Iterative factorial implementation
- ✅ Recursive factorial implementation  
- ✅ Type hints throughout
- ✅ Comprehensive error handling (negative numbers, non-integers)
- ✅ CLI interface using Typer
- ✅ Fully tested with pytest
- ✅ Easy installation with pip

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

### CLI Usage

```bash
# Calculate factorial (defaults to iterative method)
factorial calc 5

# Specify calculation method
factorial calc 5 --method iterative
factorial calc 5 --method recursive

# Use short form
factorial calc 5 -m recursive

# Show information
factorial info
```

### Python API

```python
from factorial.iterative import factorial_iterative
from factorial.recursive import factorial_recursive

# Iterative
result = factorial_iterative(5)  # Returns 120

# Recursive
result = factorial_recursive(5)  # Returns 120

# Error handling
try:
    factorial_iterative(-5)
except ValueError as e:
    print(f"Error: {e}")  # Factorial is not defined for negative numbers

try:
    factorial_iterative(5.5)
except ValueError as e:
    print(f"Error: {e}")  # Factorial is only defined for integers
```

## Project Structure

```
TestMath/
├── factorial/
│   ├── __init__.py
│   ├── __main__.py
│   ├── iterative.py
│   ├── recursive.py
│   └── cli.py
├── tests/
│   └── test_factorial.py
├── pyproject.toml
└── README.md
```

## License

MIT License