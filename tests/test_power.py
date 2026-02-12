import pytest
from advmath.power import power_iterative, power_recursive


def test_power_iterative_positive():
    """Test basic positive exponent cases"""
    assert power_iterative(2, 0) == 1
    assert power_iterative(2, 1) == 2
    assert power_iterative(2, 2) == 4
    assert power_iterative(2, 3) == 8
    assert power_iterative(2, 4) == 16
    assert power_iterative(3, 3) == 27
    assert power_iterative(5, 2) == 25


def test_power_iterative_negative():
    """Test negative base with positive exponent"""
    assert power_iterative(-2, 3) == -8
    assert power_iterative(-2, 2) == 4
    assert power_iterative(-3, 4) == 81
    assert power_iterative(-5, 1) == -5


def test_power_iterative_large():
    """Test larger exponent calculations"""
    assert power_iterative(2, 10) == 1024
    assert power_iterative(3, 5) == 243
    assert power_iterative(5, 4) == 625
    assert power_iterative(10, 3) == 1000


def test_power_iterative_edge_cases():
    """Test edge cases"""
    # Zero base
    assert power_iterative(0, 0) == 1  # 0^0 is typically defined as 1 in this context
    assert power_iterative(0, 5) == 0
    assert power_iterative(0, 10) == 0

    # Base of 1
    assert power_iterative(1, 100) == 1
    assert power_iterative(1, 0) == 1

    # Large exponents
    assert power_iterative(2, 31) == 2147483648


def test_power_iterative_negative_exponent():
    """Test negative exponent handling"""
    with pytest.raises(ValueError, match="Exponent must be non-negative"):
        power_iterative(2, -1)
    with pytest.raises(ValueError, match="Exponent must be non-negative"):
        power_iterative(5, -10)


def test_power_iterative_non_integer_exponent():
    """Test non-integer exponent handling"""
    with pytest.raises(ValueError, match="Exponent must be an integer"):
        power_iterative(2, 2.5)
    with pytest.raises(ValueError, match="Exponent must be an integer"):
        power_iterative(3, 1.5)
    with pytest.raises(ValueError, match="Exponent must be an integer"):
        power_iterative(4, 0.5)


def test_power_recursive_positive():
    """Test basic positive exponent cases with recursive implementation"""
    assert power_recursive(2, 0) == 1
    assert power_recursive(2, 1) == 2
    assert power_recursive(2, 2) == 4
    assert power_recursive(2, 3) == 8
    assert power_recursive(2, 4) == 16
    assert power_recursive(3, 3) == 27
    assert power_recursive(5, 2) == 25


def test_power_recursive_negative():
    """Test negative base with positive exponent with recursive implementation"""
    assert power_recursive(-2, 3) == -8
    assert power_recursive(-2, 2) == 4
    assert power_recursive(-3, 4) == 81
    assert power_recursive(-5, 1) == -5


def test_power_recursive_large():
    """Test larger exponent calculations with recursive implementation"""
    assert power_recursive(2, 10) == 1024
    assert power_recursive(3, 5) == 243
    assert power_recursive(5, 4) == 625
    assert power_recursive(10, 3) == 1000


def test_power_recursive_edge_cases():
    """Test edge cases with recursive implementation"""
    # Zero base
    assert power_recursive(0, 0) == 1
    assert power_recursive(0, 5) == 0
    assert power_recursive(0, 10) == 0

    # Base of 1
    assert power_recursive(1, 100) == 1
    assert power_recursive(1, 0) == 1

    # Large exponents
    assert power_recursive(2, 31) == 2147483648


def test_power_recursive_negative_exponent():
    """Test negative exponent handling with recursive implementation"""
    with pytest.raises(ValueError, match="Exponent must be non-negative"):
        power_recursive(2, -1)
    with pytest.raises(ValueError, match="Exponent must be non-negative"):
        power_recursive(5, -10)


def test_power_recursive_non_integer_exponent():
    """Test non-integer exponent handling with recursive implementation"""
    with pytest.raises(ValueError, match="Exponent must be an integer"):
        power_recursive(2, 2.5)
    with pytest.raises(ValueError, match="Exponent must be an integer"):
        power_recursive(3, 1.5)
    with pytest.raises(ValueError, match="Exponent must be an integer"):
        power_recursive(4, 0.5)


def test_both_power_implementations_equal():
    """Test that both implementations give the same results"""
    test_cases = [
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
        (3, 3),
        (5, 2),
        (2, 10),
        (3, 5),
        (5, 4),
        (10, 3),
        (-2, 3),
        (-2, 2),
        (-3, 4),
        (-5, 1),
        (0, 5),
        (0, 10),
        (1, 100),
        (1, 0),
        (2, 31),
    ]

    for base, exp in test_cases:
        assert power_iterative(base, exp) == power_recursive(base, exp)


def test_power_properties():
    """Test mathematical properties of power"""
    # Basic properties
    assert power_iterative(2, 3) ** 2 == power_iterative(4, 3)
    assert power_iterative(3, 2) == power_iterative(3, 1) * 3
    assert power_iterative(5, 0) == 1
    assert power_iterative(0, 5) == 0

    # Multiplication property
    assert power_iterative(2, 3) * power_iterative(3, 3) == power_iterative(6, 3)