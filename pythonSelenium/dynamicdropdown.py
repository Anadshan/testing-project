import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


# chrome driver
service_obj = Service("/home/sanjoli/chromedriver")
driver: WebDriver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
# if we have to fetch the dynamic text then driver.find_element(By.ID, "autosuggest").text will not work so we have
# to use :
# print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
# now we have to validate the value
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"






