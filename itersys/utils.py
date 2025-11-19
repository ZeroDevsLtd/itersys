"""
Utility functions for nested data structures.
"""

from typing import Any, Union, List


def deep_get(d: dict, key_path: Union[str, List[str]], default: Any = None) -> Any:
    """
    Get a value from a nested dictionary using a dot-separated key path or list of keys.
    
    Args:
        d: The dictionary to search in
        key_path: Either a dot-separated string (e.g., "a.b.c") or a list of keys (e.g., ["a", "b", "c"])
        default: The default value to return if the path doesn't exist
        
    Returns:
        The value at the specified path, or the default value if not found
        
    Example:
        >>> d = {"a": {"b": {"c": 42}}}
        >>> deep_get(d, "a.b.c")
        42
        >>> deep_get(d, ["a", "b", "c"])
        42
        >>> deep_get(d, "a.b.d", default=0)
        0
    """
    if isinstance(key_path, str):
        keys = key_path.split('.')
    else:
        keys = key_path
    
    current = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def deep_set(d: dict, key_path: Union[str, List[str]], value: Any) -> None:
    """
    Set a value in a nested dictionary using a dot-separated key path or list of keys.
    Creates intermediate dictionaries as needed.
    
    Args:
        d: The dictionary to modify
        key_path: Either a dot-separated string (e.g., "a.b.c") or a list of keys (e.g., ["a", "b", "c"])
        value: The value to set
        
    Example:
        >>> d = {}
        >>> deep_set(d, "a.b.c", 42)
        >>> d
        {'a': {'b': {'c': 42}}}
        >>> deep_set(d, ["x", "y"], 10)
        >>> d
        {'a': {'b': {'c': 42}}, 'x': {'y': 10}}
    """
    if isinstance(key_path, str):
        keys = key_path.split('.')
    else:
        keys = key_path
    
    current = d
    for key in keys[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]
    
    current[keys[-1]] = value

