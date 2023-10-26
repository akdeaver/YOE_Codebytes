import pytest
from .calculator import add, operation

#Example Positive Test
def test_addoneplustwo_shouldReturnThree():
    assert add(1,2) == 3

def test_addthreenumbers_shouldReturnSixteen():
    assert add(3,5,8) == 16

def test_addfivenumbers_shouldeturnTwentysix():
    assert add(3,5,8,3,7) == 26

def test_error_ifnegativenumberpresent():
    with pytest.raises(TypeError):
        add(-1,2,3)

def test_subtracttwominusone_shouldReturnOne():
    assert operation("subtract",2,1) == 1

def test_multiplythreetimestwo_shoouldReturnSix():
    assert operation("multiply",3,3) == 9

def test_dividesixbytwo_shouldReturnThree():
    assert operation("divide",6,2) == 3

def test_string_shouldThrowTypeError():
    with pytest.raises(TypeError):
        operation("random",6,2)

def test_string_shouldThrowTypeError():
    with pytest.raises(TypeError):
        add('alextest')