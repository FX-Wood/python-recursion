import pytest
from fibonacci import fibonacci

def test_0():
    assert fibonacci(0) == 0

def test_negative():
    assert fibonacci(-1) == 0

def test_7():
    assert fibonacci(7) == 13