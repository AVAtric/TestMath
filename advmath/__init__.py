"""Advanced Mathematics Package"""

__version__ = "0.2.0"

# Export factorial functions
from advmath.factorial import factorial_iterative, factorial_recursive

# Export fibonacci functions
from advmath.fibonacci import fibonacci_iterative, fibonacci_recursive

# Export gcd functions
from advmath.gcd import gcd_iterative, gcd_recursive

# Export lcm functions
from advmath.lcm import lcm_iterative, lcm_recursive

# Export prime functions
from advmath.prime import is_prime_iterative, is_prime_recursive

__all__ = [
    "factorial_iterative",
    "factorial_recursive",
    "fibonacci_iterative",
    "fibonacci_recursive",
    "gcd_iterative",
    "gcd_recursive",
    "lcm_iterative",
    "lcm_recursive",
    "is_prime_iterative",
    "is_prime_recursive",
]