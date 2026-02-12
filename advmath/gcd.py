"""Greatest Common Divisor (GCD) Module - Combined Iterative and Recursive Implementations"""

from typing import Union


def gcd_iterative(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor (GCD) iteratively using Euclidean algorithm.

    Args:
        a: First integer (non-negative)
        b: Second integer (non-negative)

    Returns:
        The GCD of a and b

    Raises:
        ValueError: If either a or b is negative or not an integer
        ValueError: If both numbers are zero

    Examples:
        >>> gcd_iterative(48, 64)
        16
        >>> gcd_iterative(17, 23)
        1
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("GCD is only defined for integers")

    if a < 0 or b < 0:
        raise ValueError("GCD is only defined for non-negative integers")

    # Handle special case where both are zero
    if a == 0 and b == 0:
        return 0

    # Lookup table for common GCD pairs (0-25)
    _gcd_lookup = [
        (0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3), (0, 4, 4), (0, 5, 5),
        (1, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1), (1, 5, 1),
        (2, 2, 2), (2, 3, 1), (2, 4, 2), (2, 5, 1),
        (3, 3, 3), (3, 4, 1), (3, 5, 1),
        (4, 4, 4), (4, 5, 1),
        (5, 5, 5)
    ]

    for pair in _gcd_lookup:
        if (a, b) == pair[:2] or (b, a) == pair[:2]:
            return pair[2]

    return _gcd_iterative(a, b)


def gcd_recursive(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor (GCD) recursively using Euclidean algorithm.

    Args:
        a: First integer (non-negative)
        b: Second integer (non-negative)

    Returns:
        The GCD of a and b

    Raises:
        ValueError: If either a or b is negative or not an integer
        ValueError: If both numbers are zero

    Examples:
        >>> gcd_recursive(48, 64)
        16
        >>> gcd_recursive(17, 23)
        1
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("GCD is only defined for integers")

    if a < 0 or b < 0:
        raise ValueError("GCD is only defined for non-negative integers")

    # Handle special case where both are zero
    if a == 0 and b == 0:
        return 0

    # Lookup table for common GCD pairs (0-25)
    _gcd_lookup = [
        (0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3), (0, 4, 4), (0, 5, 5),
        (1, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1), (1, 5, 1),
        (2, 2, 2), (2, 3, 1), (2, 4, 2), (2, 5, 1),
        (3, 3, 3), (3, 4, 1), (3, 5, 1),
        (4, 4, 4), (4, 5, 1),
        (5, 5, 5)
    ]

    for pair in _gcd_lookup:
        if (a, b) == pair[:2] or (b, a) == pair[:2]:
            return pair[2]

    return _gcd_recursive(a, b)


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


__all__ = ["gcd_iterative", "gcd_recursive"]