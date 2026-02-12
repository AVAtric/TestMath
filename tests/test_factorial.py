import pytest
from factorial.iterative import factorial_iterative
from factorial.recursive import factorial_recursive

def test_iterative_factorial():
    """Test iterative factorial implementation"""
    # Test basic cases
    assert factorial_iterative(0) == 1
    assert factorial_iterative(1) == 1
    assert factorial_iterative(5) == 120
    assert factorial_iterative(10) == 3628800
    
    # Test negative number handling
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        factorial_iterative(-1)
    
    # Test non-integer handling
    with pytest.raises(ValueError, match="Factorial is only defined for integers"):
        factorial_iterative(5.5)

def test_recursive_factorial():
    """Test recursive factorial implementation"""
    # Test basic cases
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3628800
    
    # Test negative number handling
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        factorial_recursive(-1)
    
    # Test non-integer handling
    with pytest.raises(ValueError, match="Factorial is only defined for integers"):
        factorial_recursive(5.5)

def test_both_implementations_equal():
    """Test that both implementations give the same results"""
    test_cases = [0, 1, 3, 5, 7, 10]
    
    for n in test_cases:
        assert factorial_iterative(n) == factorial_recursive(n)