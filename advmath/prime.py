"""Prime number detection – iterative and recursive.

This module provides two public functions:

- :func:`is_prime_iterative` – a straightforward loop based check.
- :func:`is_prime_recursive` – a tail‑recursive version that is
  memoised with :func:`functools.lru_cache`.

The helper functions are intentionally **not** exported; the public API is
kept small and consistent with the rest of the package.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Union


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

def _validate_int_and_nonnegative(n: int) -> None:
    """Validate that *n* is an integer and non‑negative.

    Raises
    ------
    TypeError
        If *n* is not an :class:`int`.
    ValueError
        If *n* is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Primality test requires an integer")
    if n < 0:
        raise ValueError("Must be a non‑negative integer")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def is_prime_iterative(n: int) -> bool:
    """Iteratively determine whether *n* is prime.

    Parameters
    ----------
    n : int
        Number to test.

    Returns
    -------
    bool
        ``True`` if *n* is prime, ``False`` otherwise.
    """
    _validate_int_and_nonnegative(n)

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
def _prime_recursive_helper(n: int, divisor: int = 3) -> bool:
    """Recursive helper for :func:`is_prime_recursive`.

    The function is memoised on *n* only – the ``divisor`` argument is an
    implementation detail.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return _prime_recursive_helper(n, divisor + 2)


def is_prime_recursive(n: int) -> bool:
    """Recursively determine whether *n* is prime.

    Parameters
    ----------
    n : int
        Number to test.

    Returns
    -------
    bool
        ``True`` if *n* is prime, ``False`` otherwise.
    """
    _validate_int_and_nonnegative(n)
    return _prime_recursive_helper(n)


__all__ = ["is_prime_iterative", "is_prime_recursive"]
