import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute method in fixture demo method")

    def test_fixtureDemo1(self):
        print("i will execute method in fixture demo1 method")

    def test_fixtureDemo2(self):
        print("i will execute method in fixture demo2 method")

    def test_fixtureDemo3(self):
        print("i will execute method in fixture demo3 method")

