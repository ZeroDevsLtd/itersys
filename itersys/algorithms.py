"""
Common algorithms for everyday use.
"""

from typing import List, Any, Optional


def binary_search(arr: List[Any], target: Any) -> Optional[int]:
    """
    Perform binary search on a sorted list.
    
    Args:
        arr: A sorted list to search in
        target: The value to search for
        
    Returns:
        The index of the target if found, None otherwise
        
    Example:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        None
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None


def merge_sort(arr: List[Any]) -> List[Any]:
    """
    Sort a list using merge sort algorithm.
    
    Args:
        arr: The list to sort
        
    Returns:
        A new sorted list
        
    Example:
        >>> merge_sort([5, 2, 9, 1])
        [1, 2, 5, 9]
    """
    if len(arr) <= 1:
        return arr[:]
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)


def _merge(left: List[Any], right: List[Any]) -> List[Any]:
    """Helper function to merge two sorted lists."""
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: The index of the Fibonacci number (0-indexed)
        
    Returns:
        The nth Fibonacci number
        
    Example:
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers using Euclidean algorithm.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        The greatest common divisor of a and b
        
    Example:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 13)
        1
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

