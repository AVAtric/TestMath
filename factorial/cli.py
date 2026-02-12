"""CLI for factorial calculator"""

import sys
from typing import Optional

import typer

from factorial.iterative import factorial_iterative
from factorial.recursive import factorial_recursive

app = typer.Typer()


def factorial(n: int, method: str = "iterative") -> int:
    """
    Calculate factorial with specified method.

    Args:
        n: The number to calculate factorial for
        method: The calculation method (iterative or recursive)

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative, not an integer, or method is invalid
    """
    if method not in ("iterative", "recursive"):
        raise ValueError("Method must be 'iterative' or 'recursive'")

    if method == "iterative":
        return factorial_iterative(n)
    else:
        return factorial_recursive(n)


@app.command()
def calc(n: int, method: Optional[str] = typer.Option(None, "--method", "-m", help="Calculation method (iterative|recursive)")):
    """
    Calculate the factorial of a number.

    Examples:
        factorial calc 5
        factorial calc 5 --method iterative
        factorial calc 5 -m recursive
    """
    try:
        result = factorial(n, method or "iterative")
        typer.echo(result)
        sys.exit(0)
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


@app.command()
def info():
    """Show information about the factorial calculator."""
    typer.echo("Factorial Calculator v0.1.0")
    typer.echo()
    typer.echo("Methods available: iterative, recursive")
    typer.echo("Run 'factorial calc <n> [--method iterative|recursive]' to calculate")


if __name__ == "__main__":
    app()