"""Tests for combinatorics module."""

from itersys.combinatorics import powerset, cartesian_product


def test_powerset():
    """Test powerset function."""
    result = list(powerset([1, 2, 3]))
    expected = [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    assert len(result) == len(expected)
    assert set(result) == set(expected)
    
    # Test empty set
    result = list(powerset([]))
    assert result == [()]
    
    # Test single element
    result = list(powerset([1]))
    assert set(result) == {(), (1,)}


def test_cartesian_product():
    """Test cartesian_product function."""
    result = list(cartesian_product([1, 2], [3, 4]))
    expected = [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert result == expected
    
    result = list(cartesian_product([1], [2], [3]))
    assert result == [(1, 2, 3)]
    
    result = list(cartesian_product([1, 2], [3]))
    assert result == [(1, 3), (2, 3)]
    
    # Test empty iterable
    result = list(cartesian_product([], [1, 2]))
    assert result == []
    
    result = list(cartesian_product([1, 2], []))
    assert result == []

