"""
Tests for the LCM (Least Common Multiple) calculator module
"""

import pytest
from advmath.lcm import lcm_iterative, lcm_recursive


class TestLCMIterative:
    """Test cases for iterative LCM implementation"""

    def test_basic_cases(self):
        """Test basic LCM calculations"""
        assert lcm_iterative(1, 1) == 1
        assert lcm_iterative(1, 5) == 5
        assert lcm_iterative(2, 3) == 6
        assert lcm_iterative(4, 6) == 12
        assert lcm_iterative(5, 10) == 10
        assert lcm_iterative(7, 13) == 91

    def test_multiples(self):
        """Test LCM with multiple numbers"""
        assert lcm_iterative(12, 18) == 36
        assert lcm_iterative(15, 25) == 75
        assert lcm_iterative(8, 12) == 24
        assert lcm_iterative(21, 14) == 42

    def test_coprime_numbers(self):
        """Test LCM with coprime numbers"""
        assert lcm_iterative(5, 7) == 35
        assert lcm_iterative(8, 9) == 72
        assert lcm_iterative(11, 13) == 143
        assert lcm_iterative(17, 19) == 323

    def test_zero_cases(self):
        """Test LCM with zero values"""
        assert lcm_iterative(0, 5) == 0
        assert lcm_iterative(5, 0) == 0
        assert lcm_iterative(0, 0) == 0

    def test_equal_numbers(self):
        """Test LCM with equal numbers"""
        assert lcm_iterative(5, 5) == 5
        assert lcm_iterative(10, 10) == 10
        assert lcm_iterative(25, 25) == 25

    def test_larger_numbers(self):
        """Test LCM with larger numbers"""
        assert lcm_iterative(100, 200) == 200
        assert lcm_iterative(144, 216) == 432
        assert lcm_iterative(500, 750) == 1500

    def test_gcd_relationship(self):
        """Test that LCM satisfies the relationship LCM(a,b) * GCD(a,b) = a * b"""
        from advmath.gcd import gcd_iterative, gcd_recursive as _gcd_iterative
        test_cases = [(4, 6), (15, 25), (8, 12), (7, 13), (21, 14)]
        for a, b in test_cases:
            expected_lcm = lcm_iterative(a, b)
            expected_gcd = _gcd_iterative(a, b)
            assert expected_lcm * expected_gcd == a * b

    def test_negative_numbers(self):
        """Test that negative numbers raise ValueError"""
        with pytest.raises(ValueError):
            lcm_iterative(-1, 5)
        with pytest.raises(ValueError):
            lcm_iterative(1, -5)
        with pytest.raises(ValueError):
            lcm_iterative(-1, -5)

    def test_non_integer_input(self):
        """Test that non-integer input raises TypeError"""
        with pytest.raises(TypeError):
            lcm_iterative(1.5, 5)
        with pytest.raises(TypeError):
            lcm_iterative(5, 2.5)


class TestLCMRecursive:
    """Test cases for recursive LCM implementation"""

    def test_basic_cases(self):
        """Test basic LCM calculations"""
        assert lcm_recursive(1, 1) == 1
        assert lcm_recursive(1, 5) == 5
        assert lcm_recursive(2, 3) == 6
        assert lcm_recursive(4, 6) == 12
        assert lcm_recursive(5, 10) == 10

    def test_multiples(self):
        """Test LCM with multiple numbers"""
        assert lcm_recursive(12, 18) == 36
        assert lcm_recursive(15, 25) == 75
        assert lcm_recursive(8, 12) == 24
        assert lcm_recursive(21, 14) == 42

    def test_coprime_numbers(self):
        """Test LCM with coprime numbers"""
        assert lcm_recursive(5, 7) == 35
        assert lcm_recursive(8, 9) == 72
        assert lcm_recursive(11, 13) == 143

    def test_zero_cases(self):
        """Test LCM with zero values"""
        assert lcm_recursive(0, 5) == 0
        assert lcm_recursive(5, 0) == 0
        assert lcm_recursive(0, 0) == 0

    def test_equal_numbers(self):
        """Test LCM with equal numbers"""
        assert lcm_recursive(5, 5) == 5
        assert lcm_recursive(10, 10) == 10

    def test_larger_numbers(self):
        """Test LCM with larger numbers"""
        assert lcm_recursive(100, 200) == 200
        assert lcm_recursive(144, 216) == 432

    def test_gcd_relationship(self):
        """Test that LCM satisfies the relationship LCM(a,b) * GCD(a,b) = a * b"""
        from advmath.gcd import gcd_recursive
        test_cases = [(4, 6), (15, 25), (8, 12), (7, 13)]
        for a, b in test_cases:
            expected_lcm = lcm_recursive(a, b)
            expected_gcd = gcd_recursive(a, b)
            assert expected_lcm * expected_gcd == a * b

    def test_negative_numbers(self):
        """Test that negative numbers raise ValueError"""
        with pytest.raises(ValueError):
            lcm_recursive(-1, 5)
        with pytest.raises(ValueError):
            lcm_recursive(1, -5)

    def test_non_integer_input(self):
        """Test that non-integer input raises TypeError"""
        with pytest.raises(TypeError):
            lcm_recursive(1.5, 5)


class TestLCMConsistency:
    """Test that iterative and recursive implementations produce consistent results"""

    def test_consistency(self):
        """Test that both implementations give the same result"""
        test_cases = [
            (1, 1),
            (1, 5),
            (2, 3),
            (4, 6),
            (5, 10),
            (12, 18),
            (15, 25),
            (8, 12),
            (7, 13),
            (21, 14),
            (0, 5),
            (5, 0),
            (0, 0),
            (100, 200),
        ]
        for a, b in test_cases:
            assert lcm_iterative(a, b) == lcm_recursive(a, b)