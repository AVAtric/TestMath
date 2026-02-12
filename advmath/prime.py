"""Prime Number Checker Module - Iterative and Recursive Implementations"""

from functools import lru_cache
from typing import Union


def is_prime_iterative(n: int) -> bool:
    """
    Check if a number is prime using an iterative algorithm.

    Args:
        n: Integer to check for primality

    Returns:
        True if n is prime, False otherwise

    Raises:
        ValueError: If n is less than 0
        TypeError: If n is not an integer

    Examples:
        >>> is_prime_iterative(2)
        True
        >>> is_prime_iterative(5)
        True
        >>> is_prime_iterative(4)
        False
    """
    if not isinstance(n, int):
        raise TypeError("Primality test requires an integer")

    if n < 0:
        raise ValueError("Must be a non-negative integer")

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    limit = int(n ** 0.5) + 1
    for divisor in range(3, limit, 2):
        if n % divisor == 0:
            return False

    return True


@lru_cache(maxsize=None)
def is_prime_recursive(n: int, divisor: Union[int, None] = None) -> bool:
    """
    Check if a number is prime using a recursive algorithm with memoization.

    Args:
        n: Integer to check for primality
        divisor: Internal parameter for recursive calls (leave as None)

    Returns:
        True if n is prime, False otherwise

    Raises:
        ValueError: If n is less than 0
        TypeError: If n is not an integer

    Examples:
        >>> is_prime_recursive(2)
        True
        >>> is_prime_recursive(5)
        True
        >>> is_prime_recursive(4)
        False
    """
    if not isinstance(n, int):
        raise TypeError("Primality test requires an integer")

    if n < 0:
        raise ValueError("Must be a non-negative integer")

    # First call with default divisor
    if divisor is None:
        return is_prime_recursive(n, 3)

    # Base cases
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check if divisor exceeds sqrt(n)
    if divisor * divisor > n:
        return True

    # Recursive check
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 2)


__all__ = ["is_prime_iterative", "is_prime_recursive"]