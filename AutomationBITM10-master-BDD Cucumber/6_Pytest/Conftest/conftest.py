import pytest


@pytest.yield_fixture()
def setup():
    print("Browser Launch Successfully.")
    yield
    print("Browser Closed Successfully")


@pytest.yield_fixture(scope='module')
def oneTimeSetup():
    print("Running conftest oneTimeSetup start")
    yield
    print("Running conftest oneTimeSetup tearDown")
