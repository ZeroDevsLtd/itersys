"""Tests for algorithms module."""

import pytest
from itersys.algorithms import binary_search, merge_sort, fibonacci, gcd


def test_binary_search():
    """Test binary_search function."""
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 5) == 4
    assert binary_search(arr, 6) is None
    assert binary_search(arr, 0) is None
    
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(arr2, 7) == 6
    assert binary_search(arr2, 11) is None


def test_merge_sort():
    """Test merge_sort function."""
    assert merge_sort([5, 2, 9, 1]) == [1, 2, 5, 9]
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    assert merge_sort([1]) == [1]
    assert merge_sort([]) == []
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    # Test that original list is not modified
    original = [5, 2, 9, 1]
    sorted_list = merge_sort(original)
    assert original == [5, 2, 9, 1]
    assert sorted_list == [1, 2, 5, 9]


def test_fibonacci():
    """Test fibonacci function."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_fibonacci_invalid():
    """Test fibonacci with invalid input."""
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_gcd():
    """Test gcd function."""
    assert gcd(48, 18) == 6
    assert gcd(18, 48) == 6
    assert gcd(17, 13) == 1
    assert gcd(100, 25) == 25
    assert gcd(25, 100) == 25
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6

