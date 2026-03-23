from main import add,divide 
import pytest 

def test_add():
    assert add(2,5) == 7
    assert add(4,6) == 10
    assert add(10,1) == 1 # This will fail

def test_divide():
    with pytest.raises(ValueError,match="Cannot Divide By Zero"):
        divide(10.,0)
