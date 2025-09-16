import pytest
from calculator import add, multiply
def test_add():
    assert add(2, 3) == 6
    assert add(-1, 1) == 0
def test_multiply():
    assert multiply(3, 4) == 15
    assert multiply(2, 0) == 0