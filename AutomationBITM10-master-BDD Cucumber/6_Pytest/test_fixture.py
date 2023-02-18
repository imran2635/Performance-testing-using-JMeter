import pytest
import math


@pytest.fixture
def input_values1():
    number1 = 20
    return number1


def test_tc1_multiply1(input_values1):
    number2 = 10
    assert input_values1 * number2 == 200


def test_tc2_multiply2(input_values1):
    number2 = 10
    assert input_values1 * number2 == 200

