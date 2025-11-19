"""
Iterator utilities for common operations.
"""

from typing import Iterable, Iterator, Callable, Any


def chunk(iterable: Iterable, size: int) -> Iterator[list]:
    """
    Split an iterable into chunks of the specified size.
    
    Args:
        iterable: The iterable to chunk
        size: The size of each chunk
        
    Yields:
        Lists of items from the iterable, each of length `size` (except possibly the last)
        
    Example:
        >>> list(chunk([1, 2, 3, 4, 5], 2))
        [[1, 2], [3, 4], [5]]
    """
    if size <= 0:
        raise ValueError("size must be positive")
    
    chunk_list = []
    for item in iterable:
        chunk_list.append(item)
        if len(chunk_list) == size:
            yield chunk_list
            chunk_list = []
    
    if chunk_list:
        yield chunk_list


def window(iterable: Iterable, size: int) -> Iterator[tuple]:
    """
    Create a sliding window over an iterable.
    
    Args:
        iterable: The iterable to create windows over
        size: The size of each window
        
    Yields:
        Tuples of consecutive items from the iterable
        
    Example:
        >>> list(window([1, 2, 3, 4, 5], 3))
        [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    """
    if size <= 0:
        raise ValueError("size must be positive")
    
    iterator = iter(iterable)
    window_list = []
    
    # Fill initial window
    for _ in range(size):
        try:
            window_list.append(next(iterator))
        except StopIteration:
            return
    
    yield tuple(window_list)
    
    # Slide the window
    for item in iterator:
        window_list.pop(0)
        window_list.append(item)
        yield tuple(window_list)


def flatten(nested_iterable: Iterable) -> Iterator[Any]:
    """
    Flatten a nested iterable structure.
    
    Args:
        nested_iterable: An iterable that may contain nested iterables
        
    Yields:
        Individual items from the nested structure
        
    Example:
        >>> list(flatten([1, [2, 3], [4, [5]]]))
        [1, 2, 3, 4, 5]
    """
    for item in nested_iterable:
        if isinstance(item, (list, tuple)) or hasattr(item, '__iter__') and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item


def unique_by(iterable: Iterable, key: Callable[[Any], Any] = lambda x: x) -> Iterator[Any]:
    """
    Return unique items from an iterable based on a key function.
    
    Args:
        iterable: The iterable to filter
        key: A function that returns the key to use for uniqueness comparison
        
    Yields:
        Unique items from the iterable (first occurrence of each unique key)
        
    Example:
        >>> list(unique_by([1, 2, 2, 3, 1], lambda x: x))
        [1, 2, 3]
        >>> list(unique_by([{'a': 1}, {'a': 1}, {'a': 2}], lambda x: x['a']))
        [{'a': 1}, {'a': 2}]
    """
    seen = set()
    for item in iterable:
        item_key = key(item)
        if item_key not in seen:
            seen.add(item_key)
            yield item

