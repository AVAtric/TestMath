import pytest
from advmath.gcd import gcd_iterative, gcd_recursive

def test_gcd_iterative_basic():
    """Test basic GCD cases from lookup table"""
    assert gcd_iterative(1, 1) == 1
    assert gcd_iterative(2, 4) == 2
    assert gcd_iterative(3, 6) == 3
    assert gcd_iterative(5, 10) == 5
    assert gcd_iterative(8, 12) == 4
    assert gcd_iterative(7, 21) == 7
    assert gcd_iterative(9, 18) == 9
    assert gcd_iterative(4, 8) == 4
    assert gcd_iterative(6, 9) == 3
    assert gcd_iterative(15, 25) == 5
    assert gcd_iterative(14, 21) == 7
    assert gcd_iterative(8, 14) == 2
    assert gcd_iterative(10, 15) == 5

def test_gcd_iterative_larger():
    """Test larger GCD calculations"""
    assert gcd_iterative(48, 64) == 16
    assert gcd_iterative(100, 75) == 25
    assert gcd_iterative(101, 103) == 1
    assert gcd_iterative(56, 98) == 14
    assert gcd_iterative(17, 34) == 17
    assert gcd_iterative(30, 45) == 15

def test_gcd_iterative_edge_cases():
    """Test edge cases"""
    # One number is zero
    assert gcd_iterative(0, 5) == 5
    assert gcd_iterative(5, 0) == 5
    assert gcd_iterative(0, 0) == 0
    
    # Same number
    assert gcd_iterative(10, 10) == 10
    assert gcd_iterative(7, 7) == 7

def test_gcd_iterative_negative():
    """Test negative number handling"""
    with pytest.raises(ValueError, match="GCD is only defined for non-negative integers"):
        gcd_iterative(-1, 5)
    with pytest.raises(ValueError, match="GCD is only defined for non-negative integers"):
        gcd_iterative(5, -1)
    with pytest.raises(ValueError, match="GCD is only defined for non-negative integers"):
        gcd_iterative(-1, -1)

def test_gcd_iterative_non_integer():
    """Test non-integer handling"""
    with pytest.raises(ValueError, match="GCD is only defined for integers"):
        gcd_iterative(5.5, 10)
    with pytest.raises(ValueError, match="GCD is only defined for integers"):
        gcd_iterative(5, 10.5)
    with pytest.raises(ValueError, match="GCD is only defined for integers"):
        gcd_iterative(5.5, 10.5)

def test_gcd_recursive_basic():
    """Test basic GCD cases with recursive implementation"""
    assert gcd_recursive(1, 1) == 1
    assert gcd_recursive(2, 4) == 2
    assert gcd_recursive(3, 6) == 3
    assert gcd_recursive(5, 10) == 5
    assert gcd_recursive(8, 12) == 4
    assert gcd_recursive(7, 21) == 7
    assert gcd_recursive(9, 18) == 9
    assert gcd_recursive(4, 8) == 4
    assert gcd_recursive(6, 9) == 3
    assert gcd_recursive(15, 25) == 5
    assert gcd_recursive(14, 21) == 7
    assert gcd_recursive(8, 14) == 2
    assert gcd_recursive(10, 15) == 5

def test_gcd_recursive_larger():
    """Test larger GCD calculations with recursive implementation"""
    assert gcd_recursive(48, 64) == 16
    assert gcd_recursive(100, 75) == 25
    assert gcd_recursive(101, 103) == 1
    assert gcd_recursive(56, 98) == 14
    assert gcd_recursive(17, 34) == 17
    assert gcd_recursive(30, 45) == 15

def test_gcd_recursive_edge_cases():
    """Test edge cases with recursive implementation"""
    assert gcd_recursive(0, 5) == 5
    assert gcd_recursive(5, 0) == 5
    assert gcd_recursive(0, 0) == 0
    assert gcd_recursive(10, 10) == 10
    assert gcd_recursive(7, 7) == 7

def test_gcd_recursive_negative():
    """Test negative number handling with recursive implementation"""
    with pytest.raises(ValueError, match="GCD is only defined for non-negative integers"):
        gcd_recursive(-1, 5)
    with pytest.raises(ValueError, match="GCD is only defined for non-negative integers"):
        gcd_recursive(5, -1)
    with pytest.raises(ValueError, match="GCD is only defined for non-negative integers"):
        gcd_recursive(-1, -1)

def test_gcd_recursive_non_integer():
    """Test non-integer handling with recursive implementation"""
    with pytest.raises(ValueError, match="GCD is only defined for integers"):
        gcd_recursive(5.5, 10)
    with pytest.raises(ValueError, match="GCD is only defined for integers"):
        gcd_recursive(5, 10.5)
    with pytest.raises(ValueError, match="GCD is only defined for integers"):
        gcd_recursive(5.5, 10.5)

def test_both_gcd_implementations_equal():
    """Test that both implementations give the same results"""
    test_cases = [
        (1, 1), (2, 4), (3, 6), (5, 10), (8, 12),
        (7, 21), (9, 18), (4, 8), (6, 9), (15, 25),
        (14, 21), (8, 14), (10, 15), (48, 64),
        (100, 75), (101, 103), (56, 98), (17, 34),
        (30, 45), (0, 5), (5, 0), (0, 0),
        (10, 10), (7, 7)
    ]
    
    for a, b in test_cases:
        assert gcd_iterative(a, b) == gcd_recursive(a, b)

def test_gcd_properties():
    """Test mathematical properties of GCD"""
    # GCD should be non-negative
    assert gcd_iterative(10, 5) >= 0
    assert gcd_iterative(0, 0) == 0
    assert gcd_iterative(0, 5) == 5
    
    # GCD should divide both numbers
    gcd = gcd_iterative(12, 18)
    assert 12 % gcd == 0
    assert 18 % gcd == 0
    
    # GCD should be <= both numbers
    assert gcd_iterative(12, 18) <= 12
    assert gcd_iterative(12, 18) <= 18
    
    # GCD of coprime numbers should be 1
    assert gcd_iterative(7, 11) == 1
    assert gcd_iterative(17, 19) == 1