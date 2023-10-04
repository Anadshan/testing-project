import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstName"])
        homepage.getEmail().send_keys(getData["lastName"])
        homepage.getPassword().send_keys("123456")
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        # dropdown.select_by_value()
        homepage.submitForm().click()
        message = homepage.getSuccessMessage().text
        print(message)
        assert ("Success!" in message)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param

