"""CLI for Advanced Mathematics Package.

The CLI has been refactored to centralise method validation, remove duplicate
error‑handling logic, and provide consistent error messages.  A simple
``_validate_method`` helper now raises a :class:`ValueError` with the
standardised message ``"Method must be 'iterative' or 'recursive'"``.  The
``handle_errors`` decorator continues to catch any exception and prints it to
stderr.
"""

from __future__ import annotations

import sys
from typing import Literal

import typer

# Import the math routines
from advmath.factorial import factorial_iterative, factorial_recursive
from advmath.fibonacci import fibonacci_iterative, fibonacci_recursive
from advmath.gcd import gcd_iterative, gcd_recursive
from advmath.lcm import lcm_iterative, lcm_recursive
from advmath.prime import is_prime_iterative, is_prime_recursive

app = typer.Typer()

# -------------------------------
# Utility helpers
# -------------------------------

CALC_METHOD = Literal["iterative", "recursive"]


def _validate_method(method: str) -> CALC_METHOD:
    """Validate the ``method`` option.

    Raises
    ------
    ValueError
        If *method* is not ``"iterative"`` or ``"recursive"``.
    """
    if method.lower() not in ("iterative", "recursive"):
        raise ValueError("Method must be 'iterative' or 'recursive'")
    return method.lower()  # type: ignore[return-value]


# -------------------------------
# Centralised error handling decorator
# -------------------------------

def handle_errors(func):
    """Decorator that catches all exceptions, prints an error message to
    stderr, and exits with status code 1.
    """

    def wrapper(*args, **kwargs):  # pragma: no cover – exercised via CLI tests
        try:
            return func(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001 – catching all for CLI
            typer.echo(f"Error: {exc}", err=True)
            sys.exit(1)

    return wrapper

# -------------------------------
# Helper wrappers
# -------------------------------

# Factorial

def _calculate_factorial(n: int, method: CALC_METHOD = "iterative") -> int:
    return factorial_iterative(n) if method == "iterative" else factorial_recursive(n)

# GCD

def _calculate_gcd(a: int, b: int, method: CALC_METHOD = "iterative") -> int:
    return gcd_iterative(a, b) if method == "iterative" else gcd_recursive(a, b)

# LCM

def _calculate_lcm(a: int, b: int, method: CALC_METHOD = "iterative") -> int:
    return lcm_iterative(a, b) if method == "iterative" else lcm_recursive(a, b)

# Prime

def _check_prime(n: int, method: CALC_METHOD = "iterative") -> bool:
    return is_prime_iterative(n) if method == "iterative" else is_prime_recursive(n)

# -------------------------------
# Commands
# -------------------------------

@app.command()
@handle_errors
def fact(
    n: int,
    method: str = typer.Option(
        "iterative",
        "--method",
        "-m",
        case_sensitive=False,
        help="Calculation method (iterative|recursive)",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show verbose output",
    ),
):
    """Calculate factorial of a number."""
    method = _validate_method(method)
    result = _calculate_factorial(n, method)
    if verbose:
        typer.echo(f"Factorial of {n} is {result}")
    else:
        typer.echo(result)


@app.command()
@handle_errors
def gcd(
    a: int,
    b: int,
    method: str = typer.Option(
        "iterative",
        "--method",
        "-m",
        case_sensitive=False,
        help="Calculation method (iterative|recursive)",
    ),
):
    """Calculate GCD of two numbers."""
    method = _validate_method(method)
    result = _calculate_gcd(a, b, method)
    typer.echo(f"GCD of {a} and {b} is {result}")


@app.command()
@handle_errors
def lcm(
    a: int,
    b: int,
    method: str = typer.Option(
        "iterative",
        "--method",
        "-m",
        case_sensitive=False,
        help="Calculation method (iterative|recursive)",
    ),
):
    """Calculate LCM of two numbers."""
    method = _validate_method(method)
    result = _calculate_lcm(a, b, method)
    typer.echo(f"LCM of {a} and {b} is {result}")


@app.command()
@handle_errors
def prime(
    n: int,
    method: str = typer.Option(
        "iterative",
        "--method",
        "-m",
        case_sensitive=False,
        help="Calculation method (iterative|recursive)",
    ),
):
    """Check if a number is prime."""
    method = _validate_method(method)
    result = _check_prime(n, method)
    typer.echo(f"{n} is {'prime' if result else 'not prime'}")


@app.command()
def info():
    """Show information about the Advanced Mathematics package."""
    typer.echo("Advanced Mathematics v0.2.0")
    typer.echo()
    typer.echo("Functions available:")
    typer.echo("  - Factorial: fact")
    typer.echo("  - GCD: gcd")
    typer.echo("  - LCM: lcm")
    typer.echo("  - Prime check: prime")
    typer.echo()
    typer.echo("Usage examples:")
    typer.echo("  advmath fact <n> [--method iterative|recursive] [--verbose]")
    typer.echo("  advmath gcd <a> <b> [--method iterative|recursive]")
    typer.echo("  advmath lcm <a> <b> [--method iterative|recursive]")
    typer.echo("  advmath prime <n> [--method iterative|recursive]")


if __name__ == "__main__":
    app()
