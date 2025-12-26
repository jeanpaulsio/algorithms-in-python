# Algorithms in Python 🐍

A structured repository for practicing algorithms and data structures in Python

## Setup

```bash
# Clone and cd into repo
git clone https://github.com/jeanpaulsio/algorithms-in-python.git
cd algorithms-in-python

# Install Python version via asdf
asdf install

# Start virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Practice Mode

Hide solutions and practice implementing algorithms yourself:

```bash
# Enter practice mode (hides solutions, creates stubs)
make practice
# or: python scripts/practice_mode.py on

# Implement your solution, then run tests
pytest

# When done, restore solutions
make restore
# or: python scripts/practice_mode.py off
```

Practice mode will:
- Backup your current solutions
- Replace them with function stubs (signatures only)
- Hide private helper functions (they give hints away)
- Restore everything when you're done

## Running Tests

```bash
# Run all tests
pytest

# Run tests matching a keyword
pytest -k even

# Run a specific test
pytest tests/arrays_and_strings/test_clone_even_numbers.py
```

## Linting & Formatting

```bash
ruff check .
ruff format .
```

## Typechecking

```bash
pyright
```

## Directory

1. [arrays_and_strings](./src/algorithms/arrays_and_strings/)
