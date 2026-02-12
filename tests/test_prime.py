"""
Tests for the Prime Number Checker module
"""

import pytest
from advmath.prime import is_prime_iterative, is_prime_recursive


class TestIsPrimeIterative:
    """Test cases for iterative prime checking implementation"""

    def test_small_primes(self):
        """Test small prime numbers"""
        assert is_prime_iterative(2) == True
        assert is_prime_iterative(3) == True
        assert is_prime_iterative(5) == True
        assert is_prime_iterative(7) == True
        assert is_prime_iterative(11) == True

    def test_small_composites(self):
        """Test small composite numbers"""
        assert is_prime_iterative(1) == False
        assert is_prime_iterative(4) == False
        assert is_prime_iterative(6) == False
        assert is_prime_iterative(8) == False
        assert is_prime_iterative(9) == False
        assert is_prime_iterative(10) == False

    def test_larger_primes(self):
        """Test larger prime numbers"""
        assert is_prime_iterative(13) == True
        assert is_prime_iterative(17) == True
        assert is_prime_iterative(19) == True
        assert is_prime_iterative(23) == True
        assert is_prime_iterative(29) == True

    def test_larger_composites(self):
        """Test larger composite numbers"""
        assert is_prime_iterative(25) == False
        assert is_prime_iterative(27) == False
        assert is_prime_iterative(33) == False
        assert is_prime_iterative(35) == False
        assert is_prime_iterative(39) == False

    def test_large_prime(self):
        """Test a larger prime number"""
        assert is_prime_iterative(101) == True
        assert is_prime_iterative(103) == True
        assert is_prime_iterative(997) == True

    def test_large_composite(self):
        """Test a larger composite number"""
        assert is_prime_iterative(100) == False
        assert is_prime_iterative(499) == True
        assert is_prime_iterative(500) == False
        assert is_prime_iterative(999) == False

    def test_negative_numbers(self):
        """Test that negative numbers raise ValueError"""
        with pytest.raises(ValueError):
            is_prime_iterative(-1)
        with pytest.raises(ValueError):
            is_prime_iterative(-5)
        with pytest.raises(ValueError):
            is_prime_iterative(-100)

    def test_non_integer_input(self):
        """Test that non-integer input raises TypeError"""
        with pytest.raises(TypeError):
            is_prime_iterative(1.5)
        with pytest.raises(TypeError):
            is_prime_iterative(5.5)
        with pytest.raises(TypeError):
            is_prime_iterative(2.0)

    def test_zero_and_one(self):
        """Test zero and one (neither prime nor composite)"""
        assert is_prime_iterative(0) == False
        assert is_prime_iterative(1) == False

    def test_even_numbers(self):
        """Test even numbers (except 2)"""
        assert is_prime_iterative(2) == True
        assert is_prime_iterative(4) == False
        assert is_prime_iterative(6) == False
        assert is_prime_iterative(8) == False
        assert is_prime_iterative(10) == False

    def test_famous_primes(self):
        """Test famous prime numbers"""
        assert is_prime_iterative(2) == True
        assert is_prime_iterative(3) == True
        assert is_prime_iterative(5) == True
        assert is_prime_iterative(7) == True
        assert is_prime_iterative(11) == True
        assert is_prime_iterative(13) == True
        assert is_prime_iterative(17) == True
        assert is_prime_iterative(19) == True
        assert is_prime_iterative(23) == True


class TestIsPrimeRecursive:
    """Test cases for recursive prime checking implementation"""

    def test_small_primes(self):
        """Test small prime numbers"""
        assert is_prime_recursive(2) == True
        assert is_prime_recursive(3) == True
        assert is_prime_recursive(5) == True
        assert is_prime_recursive(7) == True

    def test_small_composites(self):
        """Test small composite numbers"""
        assert is_prime_recursive(1) == False
        assert is_prime_recursive(4) == False
        assert is_prime_recursive(6) == False
        assert is_prime_recursive(8) == False

    def test_larger_primes(self):
        """Test larger prime numbers"""
        assert is_prime_recursive(13) == True
        assert is_prime_recursive(17) == True
        assert is_prime_recursive(19) == True

    def test_larger_composites(self):
        """Test larger composite numbers"""
        assert is_prime_recursive(25) == False
        assert is_prime_recursive(27) == False
        assert is_prime_recursive(33) == False

    def test_negative_numbers(self):
        """Test that negative numbers raise ValueError"""
        with pytest.raises(ValueError):
            is_prime_recursive(-1)
        with pytest.raises(ValueError):
            is_prime_recursive(-5)

    def test_non_integer_input(self):
        """Test that non-integer input raises TypeError"""
        with pytest.raises(TypeError):
            is_prime_recursive(1.5)
        with pytest.raises(TypeError):
            is_prime_recursive(5.5)

    def test_zero_and_one(self):
        """Test zero and one"""
        assert is_prime_recursive(0) == False
        assert is_prime_recursive(1) == False

    def test_famous_primes(self):
        """Test famous prime numbers"""
        assert is_prime_recursive(2) == True
        assert is_prime_recursive(3) == True
        assert is_prime_recursive(5) == True
        assert is_prime_recursive(7) == True
        assert is_prime_recursive(11) == True
        assert is_prime_recursive(13) == True
        assert is_prime_recursive(17) == True
        assert is_prime_recursive(19) == True


class TestIsPrimeConsistency:
    """Test that iterative and recursive implementations produce consistent results"""

    def test_consistency(self):
        """Test that both implementations give the same result"""
        test_cases = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            13,
            17,
            19,
            23,
            25,
            27,
            29,
            33,
            35,
            37,
            39,
            41,
            43,
            47,
            49,
            51,
            53,
            55,
            57,
            59,
            61,
            63,
            65,
            67,
            69,
            71,
            73,
            75,
            77,
            79,
            81,
            83,
            85,
            87,
            89,
            91,
            93,
            95,
            97,
            99,
        ]
        for number in test_cases:
            assert is_prime_iterative(number) == is_prime_recursive(number)

    def test_large_numbers(self):
        """Test that both implementations handle larger numbers consistently"""
        assert is_prime_iterative(101) == is_prime_recursive(101)
        assert is_prime_iterative(103) == is_prime_recursive(103)
        assert is_prime_iterative(997) == is_prime_recursive(997)
        assert is_prime_iterative(1001) == is_prime_iterative(1001)
        assert is_prime_iterative(1009) == is_prime_iterative(1009)