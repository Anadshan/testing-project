import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("gettimg all the card titles")
        # checkoutpage = CheckoutPage(self.driver)
        products = checkoutpage.getCardTitles()
        i=-1
        for product in products:
            i = i+1
            productText = product.text
            log.info(productText)
            if product == "Blackberry":
                product.Checkoutpage.getCardFooter()[i].click()
        checkoutpage.checkOut().click()
        confirmpage = checkoutpage.finalCheckOut()
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        # time.sleep(10)
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[class*='btn-lg']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from application is "+successText)
        assert "Success! Thank you.......! " in successText
