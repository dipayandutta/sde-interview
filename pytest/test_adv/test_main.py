from main import get_even_numbers, multiply, divide
import pytest 

def test_even_numbers():
    numbers = [1,2,3,4,5,6]
    result = get_even_numbers(numbers)

    assert result == [2,4,6]

def test_multiply():
    assert multiply(2,4) == 8 

def test_divide():
    assert divide(10,2) ==5 