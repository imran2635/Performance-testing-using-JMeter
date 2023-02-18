import pytest
import math


def test_sqrt():
    number = 25
    assert math.sqrt(number) == 5


def test_add():
    number1 = 20
    number2 = 10
    assert number1 + number2 == 60
