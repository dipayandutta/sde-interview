import pytest 
from main import get_even_numbers

def test_even_numbers():
    numbers = [1,2,3,4,5,6]
    result = get_even_numbers(numbers) 

    assert result == [2,4,6]