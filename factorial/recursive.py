"""Recursive factorial implementation"""

from typing import Final, List

RECURSIVE_FACTORIAL: Final = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880,
    10: 3628800,
}


def factorial_recursive(n: int) -> int:
    """
    Calculate factorial recursively.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative or not an integer
    """
    if not isinstance(n, int):
        raise ValueError(f"Factorial is only defined for integers. Got {type(n).__name__}")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n in RECURSIVE_FACTORIAL:
        return RECURSIVE_FACTORIAL[n]

    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)