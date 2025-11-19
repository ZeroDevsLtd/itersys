# itersys

A lightweight Python library providing **one-line iterator and algorithm helpers**. Simplify your daily tasks with powerful utilities for chunking lists, flattening iterables, sliding windows, common algorithms, combinatorial operations, and nested dictionary utilities.

## Installation

```bash
pip install itersys
```

Or install from source:

```bash
git clone https://github.com/yourusername/itersys.git
cd itersys
pip install -e .
```

## Quick Start

```python
import itersys

# Chunk a list
print(list(itersys.chunk([1, 2, 3, 4, 5], 2)))  # [[1, 2], [3, 4], [5]]

# Flatten nested structures
print(list(itersys.flatten([1, [2, 3], [4, [5]]])))  # [1, 2, 3, 4, 5]

# Sort with merge sort
print(itersys.merge_sort([5, 2, 9, 1]))  # [1, 2, 5, 9]
```

## Features

### Iteration Utilities (`itersys.iteration`)

#### `chunk(iterable, size)`
Split an iterable into chunks of the specified size.

```python
from itersys.iteration import chunk

print(list(chunk([1, 2, 3, 4, 5], 2)))  # [[1, 2], [3, 4], [5]]
print(list(chunk("abcdef", 3)))  # [['a', 'b', 'c'], ['d', 'e', 'f']]
```

#### `window(iterable, size)`
Create a sliding window over an iterable.

```python
from itersys.iteration import window

print(list(window([1, 2, 3, 4, 5], 3)))  # [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

#### `flatten(nested_iterable)`
Flatten a nested iterable structure.

```python
from itersys.iteration import flatten

print(list(flatten([1, [2, 3], [4, [5]]])))  # [1, 2, 3, 4, 5]
print(list(flatten([[1, 2], [3, 4]])))  # [1, 2, 3, 4]
```

#### `unique_by(iterable, key=lambda x: x)`
Return unique items from an iterable based on a key function.

```python
from itersys.iteration import unique_by

print(list(unique_by([1, 2, 2, 3, 1])))  # [1, 2, 3]

# With custom key function
data = [{'a': 1}, {'a': 1}, {'a': 2}]
print(list(unique_by(data, lambda x: x['a'])))  # [{'a': 1}, {'a': 2}]
```

### Algorithms (`itersys.algorithms`)

#### `binary_search(arr, target)`
Perform binary search on a sorted list.

```python
from itersys.algorithms import binary_search

arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 3))  # 2
print(binary_search(arr, 6))  # None
```

#### `merge_sort(arr)`
Sort a list using merge sort algorithm.

```python
from itersys.algorithms import merge_sort

print(merge_sort([5, 2, 9, 1]))  # [1, 2, 5, 9]
print(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]))  # [1, 1, 2, 3, 4, 5, 6, 9]
```

#### `fibonacci(n)`
Calculate the nth Fibonacci number.

```python
from itersys.algorithms import fibonacci

print(fibonacci(5))  # 5
print(fibonacci(10))  # 55
```

#### `gcd(a, b)`
Calculate the greatest common divisor of two integers.

```python
from itersys.algorithms import gcd

print(gcd(48, 18))  # 6
print(gcd(17, 13))  # 1
```

### Combinatorics (`itersys.combinatorics`)

#### `powerset(iterable)`
Generate the powerset of an iterable (all possible subsets).

```python
from itersys.combinatorics import powerset

print(list(powerset([1, 2, 3])))
# [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
```

#### `cartesian_product(*iterables)`
Compute the Cartesian product of multiple iterables.

```python
from itersys.combinatorics import cartesian_product

print(list(cartesian_product([1, 2], [3, 4])))
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```

### Utilities (`itersys.utils`)

#### `deep_get(d, key_path, default=None)`
Get a value from a nested dictionary using a dot-separated key path or list of keys.

```python
from itersys.utils import deep_get

d = {"a": {"b": {"c": 42}}}
print(deep_get(d, "a.b.c"))  # 42
print(deep_get(d, ["a", "b", "c"]))  # 42
print(deep_get(d, "a.b.d", default=0))  # 0
```

#### `deep_set(d, key_path, value)`
Set a value in a nested dictionary using a dot-separated key path or list of keys.

```python
from itersys.utils import deep_set

d = {}
deep_set(d, "a.b.c", 42)
print(d)  # {'a': {'b': {'c': 42}}}

deep_set(d, ["x", "y"], 10)
print(d)  # {'a': {'b': {'c': 42}}, 'x': {'y': 10}}
```

## CLI Usage

The `itersys` package includes a command-line interface for quick operations:

### Chunk Command

```bash
itersys chunk --input '[1,2,3,4,5]' --size 2
# Output: [[1,2],[3,4],[5]]
```

### Flatten Command

```bash
itersys flatten --input '[1,[2,3],[4,[5]]]'
# Output: [1,2,3,4,5]
```

## Import Examples

You can import functions in multiple ways:

```python
# Import from main package
import itersys
print(list(itersys.chunk([1, 2, 3, 4], 2)))

# Import from specific modules
from itersys.iteration import chunk, flatten
from itersys.algorithms import merge_sort

# Import everything
from itersys import chunk, flatten, merge_sort, powerset
```

## Testing

Run tests with pytest:

```bash
pytest tests/
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

