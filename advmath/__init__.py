"""Advanced Mathematics Package"""

__version__ = "0.2.0"

# Export factorial functions
from advmath.iterative import factorial_iterative
from advmath.recursive import factorial_recursive

# Export fibonacci function
from advmath.fibonacci import fibonacci_iterative

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
    "gcd_iterative",
    "gcd_recursive",
    "lcm_iterative",
    "lcm_recursive",
    "is_prime_iterative",
    "is_prime_recursive",
]