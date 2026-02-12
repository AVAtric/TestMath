"""Least Common Multiple (LCM) Module - Combined Iterative and Recursive Implementations"""

from typing import Union


def lcm_iterative(a: int, b: int) -> int:
    """
    Calculate Least Common Multiple (LCM) iteratively using Euclidean algorithm.

    Args:
        a: First integer (non-negative)
        b: Second integer (non-negative)

    Returns:
        The LCM of a and b

    Raises:
        ValueError: If either a or b is negative or not an integer

    Examples:
        >>> lcm_iterative(4, 6)
        12
        >>> lcm_iterative(5, 7)
        35
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("LCM requires non-negative integer inputs")

    if a < 0 or b < 0:
        raise ValueError("LCM is only defined for non-negative integers")

    if a == 0 or b == 0:
        return 0

    gcd_val = _gcd_iterative(a, b)
    return (a * b) // gcd_val


def lcm_recursive(a: int, b: int) -> int:
    """
    Calculate Least Common Multiple (LCM) recursively using Euclidean algorithm.

    Args:
        a: First integer (non-negative)
        b: Second integer (non-negative)

    Returns:
        The LCM of a and b

    Raises:
        ValueError: If either a or b is negative or not an integer

    Examples:
        >>> lcm_recursive(4, 6)
        12
        >>> lcm_recursive(5, 7)
        35
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("LCM requires non-negative integer inputs")

    if a < 0 or b < 0:
        raise ValueError("LCM is only defined for non-negative integers")

    if a == 0 or b == 0:
        return 0

    gcd_val = _gcd_recursive(a, b)
    return (a * b) // gcd_val


def _gcd_iterative(a: int, b: int) -> int:
    """Helper function for iterative GCD calculation."""
    while b:
        a, b = b, a % b
    return abs(a)


def _gcd_recursive(a: int, b: int) -> int:
    """Helper function for recursive GCD calculation."""
    if b == 0:
        return abs(a)
    return _gcd_recursive(b, a % b)


__all__ = ["lcm_iterative", "lcm_recursive"]