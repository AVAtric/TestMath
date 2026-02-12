"""Least Common Multiple (LCM) Module - Iterative and Recursive Implementations"""

from functools import lru_cache

from advmath.gcd import gcd_iterative, gcd_recursive


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

    gcd_val = gcd_iterative(a, b)
    return (a * b) // gcd_val


@lru_cache(maxsize=None)
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

    gcd_val = gcd_recursive(a, b)
    return (a * b) // gcd_val


__all__ = ["lcm_iterative", "lcm_recursive"]