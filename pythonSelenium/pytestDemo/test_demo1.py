# Pytest file name start with test_
# method name start with test_ or _test
# any code should be wrapped in method only
# method name should have some sense
# -k stand for method name execution , -s logs in output, -v stands for  info metadata
# you can run specific file with py.test <filename>
# you can mark tag(test) with @pytest.mark.smoke and run with -m
# to not skip the function but also don't want to disturb by the
# error part of function or method we can use @pytest.mark.xfail
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("hello")


@pytest.mark.xfail
def test_Program():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])
