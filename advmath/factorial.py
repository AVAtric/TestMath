"""Factorial Module - Iterative and Recursive Implementations"""

from functools import lru_cache
from typing import Union


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial iteratively using multiplication.

    Args:
        n: The number to calculate factorial for (non-negative)

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative or not an integer

    Examples:
        >>> factorial_iterative(0)
        1
        >>> factorial_iterative(5)
        120
        >>> factorial_iterative(10)
        3628800
    """
    if not isinstance(n, int):
        raise ValueError("Factorial is only defined for integers")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@lru_cache(maxsize=None)
def factorial_recursive(n: int) -> int:
    """
    Calculate factorial recursively with memoization.

    Args:
        n: The number to calculate factorial for (non-negative)

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative or not an integer

    Examples:
        >>> factorial_recursive(0)
        1
        >>> factorial_recursive(5)
        120
        >>> factorial_recursive(10)
        3628800
    """
    if not isinstance(n, int):
        raise ValueError("Factorial is only defined for integers")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n < 2:
        return 1
    return n * factorial_recursive(n - 1)


__all__ = ["factorial_iterative", "factorial_recursive"]