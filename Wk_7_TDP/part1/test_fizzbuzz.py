import pytest
from .fizzbuzz import fizzbuzz


#Example Positive Test
def test_multipleOfThree_shouldReturnFizz():
    assert fizzbuzz(3) == 'Fizz'

def test_multipleOfFive_shouldReturnBuzz():
    assert fizzbuzz(5) == 'Buzz'

def test_multipleOfThreeAndFive_shouldReturnFizzBuzz():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_notMultipleOfThreeOrFive_shouldReturnNumber():
    assert fizzbuzz(2) == 2

def test_notMultipleOfThreeOrFive_shouldNotReturnFizz():
    assert fizzbuzz(11) != 'Fizz'

def test_notMultipleOfThreeOrFive_shouldNotReturnBuzz():
    assert fizzbuzz(13) != 'Buzz'

def test_notMultipleOfThreeOrFive_shouldNotReturnFizzBuzz():
    assert fizzbuzz(17) != 'FizzBuzz'

#Example Negative test throwing an Error
def test_array_shouldThrowTypeError():
    with pytest.raises(TypeError):
        fizzbuzz([1,2,3])

def test_string_shouldThrowTypeError():
    with pytest.raises(TypeError):
        fizzbuzz('alextest')