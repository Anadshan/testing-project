import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver
service_obj = Service("/home/sanjoli/chromedriver")
driver: WebDriver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com/")
# driver.get("https://www.facebook.com/login/")
driver.get("https://rahulshettyacademy.com/angularpractice/")
# ID ,Xpath, CSSselector, Classname, name, linktext

driver.find_element(By.NAME, "name").send_keys("rohit")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath - //tagname[@attribute='value'] ->//input[@type='submit']
# CSSselector - tagname[attribute='value'] ->input[type='submit']
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
time.sleep(5)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success! " in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(10)

