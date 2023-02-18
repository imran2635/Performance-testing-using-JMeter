import pytest
import math


@pytest.fixture
def input_values1():
    number1 = 20
    return number1


@pytest.mark.order(2)
def test_tc1_multiply(input_values1):
    number2 = 10
    assert input_values1 * number2 == 200


@pytest.mark.order(1)
def test_tc2_multiply(input_values1):
    number2 = 10
    assert input_values1 * number2 == 200


@pytest.mark.order(4)
def test_tc3_multiply(input_values1):
    number2 = 10
    assert input_values1 * number2 == 200


@pytest.mark.order(3)
def test_tc4_multiply(input_values1):
    number2 = 10
    assert input_values1 * number2 == 200
