
## Levenshtein Edit Distance

The `edit_distance.py` module provides `levenshtein_distance(s1: str, s2: str) -> int`,
which computes the minimum number of single-character edits (insertions, deletions,
substitutions) to transform one string into another using a dynamic programming approach
with O(min(m, n)) space.

Example:
```python
from edit_distance import levenshtein_distance

print(levenshtein_distance("kitten", "sitting"))  # 3
print(levenshtein_distance("flaw", "lawn"))       # 2
```
# Repository Overview

This repository contains:
- A palindrome utility with unit tests
- A Levenshtein edit distance utility with unit tests

## Structure
- `palindrome_check.py` — palindrome-related helpers
- `edit_distance.py` — Levenshtein edit distance implementation
- `tests/` — unit tests
  - `test_palindrome_check_new.py`
- `Dockerfile.test` — containerized test runner (Python 3.11)
- `requirements.txt` — Python dependencies for tests
- `repository_info.txt` — repository metadata/info

## Requirements
- Python 3.11+
- pip
- Optional: Docker (to run tests in a container)

## Running Tests

### Option A: Locally
1. (Recommended) Create and activate a virtual environment:
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
   python3 -m unittest discover -s tests
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
- Tests are discovered from the `tests/` directory using the standard `unittest` discovery pattern (`test_*.py`).
- When adding new tests, place them under `tests/` and name files `test_*.py`.
