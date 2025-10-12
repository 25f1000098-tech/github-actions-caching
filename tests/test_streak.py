import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_negative():
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_all_zeros():
    assert longest_positive_streak([0, 0, 0]) == 0

def test_mixed_positive_and_negative():
    assert longest_positive_streak([1, 2, -1, 3, 4, 5]) == 3

def test_with_zeros():
    assert longest_positive_streak([1, 2, 0, 3, 4]) == 2

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, 0, 1, 2]) == 3

def test_single_element_positive():
    assert longest_positive_streak([5]) == 1

def test_single_element_negative():
    assert longest_positive_streak([-5]) == 0

def test_single_element_zero():
    assert longest_positive_streak([0]) == 0

def test_example_from_brief():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_another_example():
    assert longest_positive_streak([-2, -3, 1, 5, 6, 7, 0, 4]) == 4