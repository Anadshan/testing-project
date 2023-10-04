import time
import pytest


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        # for css a[href*='shop']
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        driver.find_element(By.LINK_TEXT, "India").click()
        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "input[class*='btn-lg']").click()
        successText = driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you! " in successText


