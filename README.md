# Python Streak Counter

This project contains a Python script `streak.py` with a function `longest_positive_streak` that calculates the length of the longest run of consecutive positive integers in a list.

## Features

-   `longest_positive_streak(nums: list[int]) -> int`: A function to find the longest streak of positive numbers.
-   A comprehensive test suite using `pytest` in `tests/test_streak.py`.
-   A GitHub Actions workflow (`.github/workflows/pytest.yml`) that automatically runs tests on every push and pull request.

## Getting Started

To get started, you can clone the repository and install the dependencies:

```bash
pip install pytest
```

Then, you can run the tests:

```bash
python -m pytest
```