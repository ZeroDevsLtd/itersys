"""Tests for iteration module."""

import pytest
from itersys.iteration import chunk, window, flatten, unique_by


def test_chunk():
    """Test chunk function."""
    assert list(chunk([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(chunk([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(chunk([1, 2, 3], 1)) == [[1], [2], [3]]
    assert list(chunk([1, 2, 3], 3)) == [[1, 2, 3]]
    assert list(chunk([], 2)) == []


def test_chunk_invalid_size():
    """Test chunk with invalid size."""
    with pytest.raises(ValueError):
        list(chunk([1, 2, 3], 0))
    with pytest.raises(ValueError):
        list(chunk([1, 2, 3], -1))


def test_window():
    """Test window function."""
    assert list(window([1, 2, 3, 4, 5], 3)) == [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    assert list(window([1, 2, 3], 2)) == [(1, 2), (2, 3)]
    assert list(window([1, 2], 2)) == [(1, 2)]
    assert list(window([1, 2], 3)) == []


def test_window_invalid_size():
    """Test window with invalid size."""
    with pytest.raises(ValueError):
        list(window([1, 2, 3], 0))


def test_flatten():
    """Test flatten function."""
    assert list(flatten([1, [2, 3], [4, [5]]])) == [1, 2, 3, 4, 5]
    assert list(flatten([1, 2, 3])) == [1, 2, 3]
    assert list(flatten([[1, 2], [3, 4]])) == [1, 2, 3, 4]
    assert list(flatten([])) == []
    assert list(flatten([[[1]]])) == [1]


def test_flatten_strings():
    """Test that strings are not flattened."""
    # Strings should not be flattened
    result = list(flatten(["abc", ["def"]]))
    assert result == ["abc", "def"]


def test_unique_by():
    """Test unique_by function."""
    assert list(unique_by([1, 2, 2, 3, 1])) == [1, 2, 3]
    assert list(unique_by([1, 2, 3])) == [1, 2, 3]
    assert list(unique_by([])) == []
    
    # Test with custom key function
    data = [{'a': 1}, {'a': 1}, {'a': 2}]
    result = list(unique_by(data, lambda x: x['a']))
    assert len(result) == 2
    assert result[0]['a'] == 1
    assert result[1]['a'] == 2

