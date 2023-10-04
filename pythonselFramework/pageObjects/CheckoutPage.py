from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    finalCheckout = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOut(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def finalCheckOut(self):
        self.driver.find_element(*CheckoutPage.finalCheckout).click()
        confirmpage = ConfirmPage(self.driver)











