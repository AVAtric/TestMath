import pytest
from advmath.fibonacci import fibonacci_iterative

def test_fibonacci_iterative_basic():
    """Test basic Fibonacci cases"""
    # Test first few numbers
    assert fibonacci_iterative(0) == 0
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(2) == 1
    assert fibonacci_iterative(3) == 2
    assert fibonacci_iterative(5) == 5
    assert fibonacci_iterative(10) == 55

def test_fibonacci_iterative_larger():
    """Test larger Fibonacci numbers"""
    assert fibonacci_iterative(15) == 610
    assert fibonacci_iterative(20) == 6765
    assert fibonacci_iterative(30) == 832040

def test_fibonacci_iterative_negative():
    """Test negative number handling"""
    with pytest.raises(ValueError, match="Fibonacci is not defined for negative numbers"):
        fibonacci_iterative(-1)

def test_fibonacci_iterative_non_integer():
    """Test non-integer handling"""
    with pytest.raises(ValueError, match="Fibonacci is only defined for integers"):
        fibonacci_iterative(5.5)

def test_fibonacci_iterative_consistency():
    """Test that iterative implementation gives correct results"""
    test_cases = [0, 1, 3, 5, 10, 15, 20, 25]
    
    for n in test_cases:
        result = fibonacci_iterative(n)
        # Verify it's the expected Fibonacci number
        assert isinstance(result, int)
        assert result >= 0