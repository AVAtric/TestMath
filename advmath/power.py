"""Power Module - Iterative and Recursive Implementations"""

from typing import Union


def power_iterative(base: int, exponent: int) -> int:
    """
    Calculate base^exponent iteratively using the exponentiation by squaring method.

    Args:
        base: Base integer (can be any integer)
        exponent: Exponent integer (non-negative)

    Returns:
        The result of base^exponent

    Raises:
        ValueError: If exponent is negative

    Examples:
        >>> power_iterative(2, 3)
        8
        >>> power_iterative(3, 4)
        81
        >>> power_iterative(-2, 3)
        -8
    """
    if not isinstance(exponent, int):
        raise ValueError("Exponent must be an integer")

    if exponent < 0:
        raise ValueError("Exponent must be non-negative")

    result = 1
    current_base = base
    current_exp = exponent

    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exp //= 2

    return result


def power_recursive(base: int, exponent: int) -> int:
    """
    Calculate base^exponent recursively using the exponentiation by squaring method.

    Args:
        base: Base integer (can be any integer)
        exponent: Exponent integer (non-negative)

    Returns:
        The result of base^exponent

    Raises:
        ValueError: If exponent is negative

    Examples:
        >>> power_recursive(2, 3)
        8
        >>> power_recursive(3, 4)
        81
        >>> power_recursive(-2, 3)
        -8
    """
    if not isinstance(exponent, int):
        raise ValueError("Exponent must be an integer")

    if exponent < 0:
        raise ValueError("Exponent must be non-negative")

    if exponent == 0:
        return 1

    if exponent % 2 == 1:
        return base * power_recursive(base * base, (exponent - 1) // 2)
    else:
        return power_recursive(base * base, exponent // 2)


__all__ = ["power_iterative", "power_recursive"]