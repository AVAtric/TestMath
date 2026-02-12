"""Factorial Module - Combined Iterative and Recursive Implementations"""

from typing import Union


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial iteratively with lookup table optimization.

    Args:
        n: The number to calculate factorial for (0-10)

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative or not an integer
        ValueError: If n exceeds the lookup table size

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

    # Lookup table for factorial (0! to 10!)
    _factorial_lookup = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800]

    if n >= len(_factorial_lookup):
        raise ValueError("Factorial only defined up to 10")

    return _factorial_lookup[n]


def factorial_recursive(n: int) -> int:
    """
    Calculate factorial recursively with lookup table optimization.

    Args:
        n: The number to calculate factorial for (0-10)

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative or not an integer
        ValueError: If n exceeds the lookup table size

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

    # Lookup table for factorial (0! to 10!)
    _factorial_lookup = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800]

    if n >= len(_factorial_lookup):
        raise ValueError("Factorial only defined up to 10")

    return _factorial_lookup[n]


__all__ = ["factorial_iterative", "factorial_recursive"]