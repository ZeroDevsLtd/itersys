"""
Combinatorial operations and utilities.
"""

from typing import Iterable, Iterator, Any
from itertools import product


def powerset(iterable: Iterable) -> Iterator[tuple]:
    """
    Generate the powerset of an iterable (all possible subsets).
    
    Args:
        iterable: The iterable to generate powerset for
        
    Yields:
        Tuples representing each subset
        
    Example:
        >>> list(powerset([1, 2, 3]))
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    items = list(iterable)
    n = len(items)
    
    for i in range(2 ** n):
        subset = tuple(items[j] for j in range(n) if (i >> j) & 1)
        yield subset


def cartesian_product(*iterables: Iterable) -> Iterator[tuple]:
    """
    Compute the Cartesian product of multiple iterables.
    
    Args:
        *iterables: Variable number of iterables
        
    Yields:
        Tuples representing each combination from the Cartesian product
        
    Example:
        >>> list(cartesian_product([1, 2], [3, 4]))
        [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    yield from product(*iterables)

