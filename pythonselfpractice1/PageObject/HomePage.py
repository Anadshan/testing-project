from selenium.webdriver.common.by import By


class HomePage:
    shop = (By.XPATH, "//a[contains(@href,'shop')]")

    def __init__(self,driver):
        self.driver = driver

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)  # * use to deserialize it and place this variable in tuple
