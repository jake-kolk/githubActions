import pytest
from mytest import add

def test_test(x1, x2):
    assert add(x1, x2) == x1 + x2
    assert add(x2,x1) == x2 + x1 
