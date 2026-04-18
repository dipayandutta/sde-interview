import pytest
from app.maths_utls import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 7) == 3


def test_multiply():
    assert multiply(10, 2) == 20


def test_divide():
    assert divide(4, 2) == 2


def test_divide_with_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
