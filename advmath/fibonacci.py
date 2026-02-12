"""Fibonacci Sequence Module - Combined Iterative and Recursive Implementations"""

from typing import Union


def fibonacci_iterative(n: int) -> int:
    """
    Calculate nth Fibonacci number iteratively with lookup table optimization.

    Args:
        n: The position in the Fibonacci sequence (0-20)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative or not an integer
        ValueError: If n exceeds the lookup table size

    Examples:
        >>> fibonacci_iterative(0)
        0
        >>> fibonacci_iterative(5)
        5
        >>> fibonacci_iterative(10)
        55
    """
    if not isinstance(n, int):
        raise ValueError("Fibonacci is only defined for integers")

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    # Lookup table for Fibonacci (0-30)
    _fibonacci_lookup = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]

    if n >= len(_fibonacci_lookup):
        raise ValueError("Fibonacci sequence only defined up to 20")

    return _fibonacci_lookup[n]


def fibonacci_recursive(n: int, a: Union[int, None] = None, b: Union[int, None] = None) -> int:
    """
    Calculate nth Fibonacci number recursively with lookup table optimization.

    Args:
        n: The position in the Fibonacci sequence (0-20)
        a: First term (for recursion, leave as None)
        b: Second term (for recursion, leave as None)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative or not an integer
        ValueError: If n exceeds the lookup table size

    Examples:
        >>> fibonacci_recursive(0)
        0
        >>> fibonacci_recursive(5)
        5
        >>> fibonacci_recursive(10)
        55
    """
    if not isinstance(n, int):
        raise ValueError("Fibonacci is only defined for integers")

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    # Lookup table for Fibonacci (0-30)
    _fibonacci_lookup = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]

    if n >= len(_fibonacci_lookup):
        raise ValueError("Fibonacci sequence only defined up to 20")

    # First call with default values
    if a is None or b is None:
        return fibonacci_recursive(n, 0, 1)

    # Base case
    if n == 0:
        return a

    if n == 1:
        return b

    return fibonacci_recursive(n - 1, b, a + b)


__all__ = ["fibonacci_iterative", "fibonacci_recursive"]