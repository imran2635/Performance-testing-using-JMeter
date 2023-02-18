import pytest
import math


@pytest.yield_fixture()
def setup():
    print("Browser Launch Successfully.")
    yield
    print("Browser Closed Successfully")


def test_tc1_login(setup):
    print("Login valid test passed")


def test_tc2_login(setup):
    print("Login Invalid test passed")
