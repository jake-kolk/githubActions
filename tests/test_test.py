import pytest
from test import add

def test_test():
    assert add(1, 2) == 3
    assert add(2,1) == 3
