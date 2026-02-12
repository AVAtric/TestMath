"""CLI for Advanced Mathematics Package"""

import sys
from typing import Optional

import typer

from advmath.iterative import (
    factorial_iterative,
    fibonacci_iterative,
    gcd_iterative,
    lcm_iterative,
    is_prime_iterative,
)
from advmath.recursive import (
    factorial_recursive,
    gcd_recursive,
    lcm_recursive,
    is_prime_recursive,
)

app = typer.Typer()


def factorial(n: int, method: str = "iterative") -> int:
    """Calculate factorial with specified method."""
    if method not in ("iterative", "recursive"):
        raise ValueError("Method must be 'iterative' or 'recursive'")

    if method == "iterative":
        return factorial_iterative(n)
    else:
        return factorial_recursive(n)


def gcd(a: int, b: int, method: str = "iterative") -> int:
    """Calculate GCD with specified method."""
    if method not in ("iterative", "recursive"):
        raise ValueError("Method must be 'iterative' or 'recursive'")

    if method == "iterative":
        return gcd_iterative(a, b)
    else:
        return gcd_recursive(a, b)


def lcm(a: int, b: int, method: str = "iterative") -> int:
    """Calculate LCM with specified method."""
    if method not in ("iterative", "recursive"):
        raise ValueError("Method must be 'iterative' or 'recursive'")

    if method == "iterative":
        return lcm_iterative(a, b)
    else:
        return lcm_recursive(a, b)


@app.command()
def calc(n: int, method: Optional[str] = typer.Option(None, "--method", "-m", help="Calculation method (iterative|recursive)")):
    """
    Calculate factorial of a number.

    Examples:
        advmath calc 5
        advmath calc 5 --method iterative
        advmath calc 5 -m recursive
    """
    try:
        result = factorial(n, method or "iterative")
        typer.echo(f"Factorial of {n} is {result}")
        sys.exit(0)
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


@app.command()
def gcd_command(a: int, b: int, method: Optional[str] = typer.Option(None, "--method", "-m", help="Calculation method (iterative|recursive)")):
    """
    Calculate GCD of two numbers.

    Examples:
        advmath gcd 48 64
        advmath gcd 48 64 --method iterative
        advmath gcd 48 64 -m recursive
    """
    try:
        result = gcd(a, b, method or "iterative")
        typer.echo(f"GCD of {a} and {b} is {result}")
        sys.exit(0)
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


@app.command()
def lcm_command(a: int, b: int, method: Optional[str] = typer.Option(None, "--method", "-m", help="Calculation method (iterative|recursive)")):
    """
    Calculate LCM of two numbers.

    Examples:
        advmath lcm 4 6
        advmath lcm 4 6 --method iterative
        advmath lcm 4 6 -m recursive
    """
    try:
        result = lcm(a, b, method or "iterative")
        typer.echo(f"LCM of {a} and {b} is {result}")
        sys.exit(0)
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


@app.command()
def prime(n: int, method: Optional[str] = typer.Option(None, "--method", "-m", help="Calculation method (iterative|recursive)")):
    """
    Check if a number is prime.

    Examples:
        advmath prime 17
        advmath prime 17 --method iterative
        advmath prime 17 -m recursive
    """
    try:
        if method not in ("iterative", "recursive"):
            method = "iterative"
        result = is_prime_iterative(n) if method == "iterative" else is_prime_recursive(n)
        typer.echo(f"{n} is {'prime' if result else 'not prime'}")
        sys.exit(0)
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


@app.command()
def info():
    """Show information about the Advanced Mathematics package."""
    typer.echo("Advanced Mathematics v0.2.0")
    typer.echo()
    typer.echo("Functions available:")
    typer.echo("  - Factorial: factorial")
    typer.echo("  - GCD: gcd")
    typer.echo("  - LCM: lcm")
    typer.echo("  - Prime check: prime")
    typer.echo()
    typer.echo("Usage examples:")
    typer.echo("  advmath calc <n> [--method iterative|recursive]")
    typer.echo("  advmath gcd <a> <b> [--method iterative|recursive]")
    typer.echo("  advmath lcm <a> <b> [--method iterative|recursive]")
    typer.echo("  advmath prime <n> [--method iterative|recursive]")


if __name__ == "__main__":
    app()