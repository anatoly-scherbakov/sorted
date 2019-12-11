# Sorted containers

Contrary to its name, this package does not really help you to efficiently sort your data, - you may use built-in tools of Python, numpy or pandas for that purpose.

This tool, however, allows you to _declare_ that certain container is already sorted and, based on that information, perform certain operations on such containers more efficiently.

## Supported operations

* Merge two or more sorted iterators into one magnificent sorted iterator
* Subtract one sorted iterator from another, returning an iterator which yields all items that exist in the latter but not in the first
* Deduplicate a sorted iterator

## Examples

```python
from itertools import count, islice
from sorted import Sorted, merge

# Merge
print(list(Sorted([0, 2, 4]) + Sorted([1, 3, 5])))
# [0, 1, 2, 3, 4, 5]

# Subtract
natural_numbers = Sorted(count())
even_numbers = Sorted(filter(lambda i: i % 2 == 0, count()))
odd_numbers = natural_numbers - even_numbers
print(list(islice(odd_numbers, 5)))
# [1, 3, 5, 7, 9]

# Deduplicate
iterators = [
    Sorted((0, ) * 50),
    Sorted((5, ) * 50),
    Sorted(count(25))
]
list(islice(
    merge(*iterators).unique(),
    4
))
# [0, 5, 25, 26]
```

To perform these operations, `sorted` uses lazy iterative algorithms with linear complexity by time and constant complexity by RAM.
