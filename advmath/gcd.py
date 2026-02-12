"""Greatest Common Divisor (GCD) Module - Iterative and Recursive Implementations"""

from functools import lru_cache
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

    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


@lru_cache(maxsize=None)
def gcd_recursive(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor (GCD) recursively with memoization.

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

    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


__all__ = ["gcd_iterative", "gcd_recursive"]