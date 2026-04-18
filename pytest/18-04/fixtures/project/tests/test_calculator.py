import pytest
from app.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5


def test_subtract(calc):
    assert calc.subtract(3, 2) == 1


def test_divide(calc):
    assert calc.divide(4, 2) == 2


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        assert calc.divide(4, 0)
