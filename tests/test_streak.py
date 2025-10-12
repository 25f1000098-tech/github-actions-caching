import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks_longest_in_middle():
    """Test with multiple streaks to ensure the longest one is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Test with a mix of positive numbers, zeros, and negative numbers."""
    assert longest_positive_streak([1, 2, 0, 4, 5, -1, 6, 7, 8]) == 3

def test_all_positive_numbers():
    """Test with a list of all positive numbers."""
    assert longest_positive_streak([1, 1, 1, 1, 1]) == 5

def test_all_non_positive_numbers():
    """Test with a list of all non-positive numbers (zeros and negatives)."""
    assert longest_positive_streak([0, -1, -5, 0, -10]) == 0

def test_single_positive_number():
    """Test with a single positive number."""
    assert longest_positive_streak([10]) == 1

def test_single_zero():
    """Test with a single zero."""
    assert longest_positive_streak([0]) == 0

def test_single_negative_number():
    """Test with a single negative number."""
    assert longest_positive_streak([-10]) == 0

def test_streak_at_the_end():
    """Test where the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 0, 2, 3, 4]) == 3

def test_streak_at_the_beginning():
    """Test where the longest streak is at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 4, 0, 5]) == 4

def test_provided_example_1():
    """Test the first example from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_provided_example_2():
    """Test the second example from the problem description."""
    assert longest_positive_streak([]) == 0

def test_provided_example_3():
    """Test the third example from the problem description."""
    assert longest_positive_streak([1, 1, 1]) == 3