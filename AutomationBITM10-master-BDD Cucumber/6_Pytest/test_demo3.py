import pytest
import math


@pytest.mark.valid
def test_tc1_login():
    number1 = 20
    number2 = 10
    assert number1 * number2 == 200


@pytest.mark.valid
def test_tc2_login():
    number1 = 20
    number2 = 10
    assert number1 * number2 == 200


@pytest.mark.invalid
def test_tc3_login():
    number1 = 20
    number2 = 10
    assert number1 * number2 == 200


@pytest.mark.invalid
def test_tc4_login():
    number1 = 20
    number2 = 10
    assert number1 * number2 == 200
