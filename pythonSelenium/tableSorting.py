import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
service_obj = Service("/home/sanjoli/chromedriver")
driver: WebDriver = webdriver.Chrome(service=service_obj)
# max time out is work is completed in 2 sec then it proceed futher not wait for more 3 sec so we save 3 sec
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserSortedVeggies = []
# click on the column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect all veggies name in browsersortedveggie list
VeggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for VeggieWebElement in VeggieWebElements:
    browserSortedVeggies.append(VeggieWebElement.text)
OriginalBrowerSortedVeggies = browserSortedVeggies.copy()
# to copy we can use slice() too but copy() is much faster

# sort this browserveggiesortedlist => new sort list
browserSortedVeggies.sort()
time.sleep(5)
assert browserSortedVeggies == OriginalBrowerSortedVeggies