"""
itersys - A lightweight Python library for iterator and algorithm helpers.
"""

__version__ = "0.1.0"

from itersys.iteration import chunk, window, flatten, unique_by
from itersys.algorithms import binary_search, merge_sort, fibonacci, gcd
from itersys.combinatorics import powerset, cartesian_product
from itersys.utils import deep_get, deep_set

__all__ = [
    # Iteration
    "chunk",
    "window",
    "flatten",
    "unique_by",
    # Algorithms
    "binary_search",
    "merge_sort",
    "fibonacci",
    "gcd",
    # Combinatorics
    "powerset",
    "cartesian_product",
    # Utils
    "deep_get",
    "deep_set",
]

