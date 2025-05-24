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

## Running Tests

```bash
# Run all tests
pytest

# Run tests matching a keyword
pytest -k even

# Run a specific test
pytest arrays_and_strings/test_clone_even_numbers.py
```

## Linting & Formatting

```bash
# Lint the codebase
flake8 .

# Format all files with black
black .
```

## Directory

1. [arrays_and_strings](./arrays_and_strings/)
