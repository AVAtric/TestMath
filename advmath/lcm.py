"""Least Common Multiple (LCM) Module – iterative & recursive.

The original implementation duplicated validation logic in both the
iterative and recursive functions.  This refactor introduces a shared helper,
``_lcm_common``, that performs type checks and delegates the calculation to
the supplied GCD routine.  This removes duplication, makes the module easier
to test, and keeps the public API unchanged.
"""

from functools import lru_cache
from typing import Callable

from advmath.gcd import gcd_iterative, gcd_recursive


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _validate_ints(a: int, b: int) -> None:
    """Validate that *a* and *b* are non‑negative integers.

    Raises
    ------
    TypeError
        If either argument is not an :class:`int`.
    ValueError
        If either argument is negative.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("LCM requires integer inputs")
    if a < 0 or b < 0:
        raise ValueError("LCM is only defined for non-negative integers")


def _lcm_common(a: int, b: int, gcd_func: Callable[[int, int], int]) -> int:
    """Shared implementation used by :func:`lcm_iterative` and
    :func:`lcm_recursive`.

    Parameters
    ----------
    a, b : int
        Non‑negative integers.
    gcd_func : Callable[[int, int], int]
        Function to compute the GCD of *a* and *b*.
    """
    _validate_ints(a, b)
    if a == 0 or b == 0:
        return 0
    gcd_val = gcd_func(a, b)
    return (a * b) // gcd_val


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def lcm_iterative(a: int, b: int) -> int:
    """Iteratively compute the LCM using the Euclidean algorithm.

    Parameters
    ----------
    a, b : int
        Non‑negative integers.

    Returns
    -------
    int
        The least common multiple of *a* and *b*.
    """
    return _lcm_common(a, b, gcd_iterative)


@lru_cache(maxsize=None)
def lcm_recursive(a: int, b: int) -> int:
    """Recursively compute the LCM using the Euclidean algorithm.

    Parameters
    ----------
    a, b : int
        Non‑negative integers.

    Returns
    -------
    int
        The least common multiple of *a* and *b*.
    """
    return _lcm_common(a, b, gcd_recursive)


__all__ = ["lcm_iterative", "lcm_recursive"]
