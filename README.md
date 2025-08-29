# Repository Overview

This repository contains simple text utilities and accompanying unit tests.

## Structure
- `text_utils.py` — text utility functions
- `palindrome_check.py` — palindrome-related helpers
- `tests/` — unit tests
  - `test_edit_distance.py`
  - `test_palindrome_check_new.py`
  - `test_text_utils.py`
- `Dockerfile.test` — containerized test runner (Python 3.11)
- `requirements.txt` — Python dependencies for tests

## Requirements
- Python 3.11+
- pip
- Optional: Docker (to run tests in a container)

## Running Tests

### Option A: Locally
1. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the unit test suite (unittest):
   ```bash
   python -m unittest discover -s tests
   ```

### Option B: Docker
Build and run using the provided test Dockerfile:
```bash
docker build -f Dockerfile.test -t repo-tests .
docker run --rm repo-tests
```
The Docker image executes:
```bash
python3 -m unittest discover -s tests
```

## Notes
- Test discovery uses the standard `unittest` pattern in the `tests/` directory.
- If you are adding new tests, place them under `tests/` and ensure files are named `test_*.py`.
