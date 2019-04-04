import pytest
from factorial import factorial

def test_0():
    assert factorial(0) == 1

def test_negative():
    assert factorial(-1) == 1

def test_5():
    assert factorial(5) == 120