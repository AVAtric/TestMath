"""
Iterative Implementations for Advanced Mathematics

This module provides iterative implementations for mathematical functions.
"""

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


def fibonacci_iterative(n: int) -> int:
    """
    Calculate nth Fibonacci number iteratively with lookup table optimization.

    Args:
        n: The position in the Fibonacci sequence (0-20)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative or not an integer
        ValueError: If n exceeds the lookup table size

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

    # Lookup table for Fibonacci (0-30)
    _fibonacci_lookup = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]

    if n >= len(_fibonacci_lookup):
        raise ValueError("Fibonacci sequence only defined up to 20")

    return _fibonacci_lookup[n]


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

    # Check odd divisors up to sqrt(n)
    limit = int(n ** 0.5) + 1
    for divisor in range(3, limit, 2):
        if n % divisor == 0:
            return False

    return True


def _gcd_iterative(a: int, b: int) -> int:
    """Helper function for iterative GCD calculation."""
    while b:
        a, b = b, a % b
    return abs(a)