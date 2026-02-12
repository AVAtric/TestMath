"""Fibonacci Sequence Module - Iterative and Recursive Implementations"""

from functools import lru_cache
from typing import Union


def fibonacci_iterative(n: int) -> int:
    """
    Calculate nth Fibonacci number iteratively.

    Args:
        n: The position in the Fibonacci sequence (non-negative)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative or not an integer

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

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@lru_cache(maxsize=None)
def fibonacci_recursive(n: int) -> int:
    """
    Calculate nth Fibonacci number recursively with memoization.

    Args:
        n: The position in the Fibonacci sequence (non-negative)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative or not an integer

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

    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


__all__ = ["fibonacci_iterative", "fibonacci_recursive"]