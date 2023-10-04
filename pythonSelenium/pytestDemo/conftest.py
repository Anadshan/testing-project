# fixture are used to setuo and tear down method for test cases - conftest file
# to generalise fixture ans make it  available to all test cases
import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will execute first")
    yield
    print("i will execute in last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshetty@gamil.com"]


@pytest.fixture(params=[("chrome", "hiii", "testing"), ("Firefox", "rahul"), ("IE","shetty")])
def crossBrowser(request):
    return request.param


