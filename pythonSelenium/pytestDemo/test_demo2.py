# we can skip the test case  by using @pytest.mark.skip and run all the cases
# in terminal

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_assertion():
    msg = "statue"
    assert msg == "status", "test failed"


def test_creditCard(setup):
    a = 4
    b = 6
    assert a+2 == b, "test failed"

