"""CLI for Advanced Mathematics Package"""

import sys
from typing import Optional

import typer

from advmath.factorial import (
    factorial_iterative,
    factorial_recursive,
)
from advmath.fibonacci import (
    fibonacci_iterative,
    fibonacci_recursive,
)
from advmath.gcd import (
    gcd_iterative,
    gcd_recursive,
)
from advmath.lcm import (
    lcm_iterative,
    lcm_recursive,
)
from advmath.prime import (
    is_prime_iterative,
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
def fact(n: int, method: Optional[str] = typer.Option(None, "--method", "-m", help="Calculation method (iterative|recursive)"), verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output")):
    """
    Calculate factorial of a number.

    Examples:
        advmath fact 5
        advmath fact 5 --method iterative
        advmath fact 5 -m recursive
        advmath fact 5 --verbose
    """
    try:
        result = factorial(n, method or "iterative")
        if verbose:
            typer.echo(f"Factorial of {n} is {result}")
        else:
            typer.echo(result)
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
        advmath gcd-command 48 64
        advmath gcd-command 48 64 --method iterative
        advmath gcd-command 48 64 -m recursive
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
        advmath lcm-command 4 6
        advmath lcm-command 4 6 --method iterative
        advmath lcm-command 4 6 -m recursive
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
    typer.echo("  - Factorial: fact")
    typer.echo("  - GCD: gcd-command")
    typer.echo("  - LCM: lcm-command")
    typer.echo("  - Prime check: prime")
    typer.echo()
    typer.echo("Usage examples:")
    typer.echo("  advmath fact <n> [--method iterative|recursive] [--verbose]")
    typer.echo("  advmath gcd-command <a> <b> [--method iterative|recursive]")
    typer.echo("  advmath lcm-command <a> <b> [--method iterative|recursive]")
    typer.echo("  advmath prime <n> [--method iterative|recursive]")


if __name__ == "__main__":
    app()