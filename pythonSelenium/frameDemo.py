import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


# chrome driver
service_obj = Service("/home/sanjoli/chromedriver")
driver: WebDriver = webdriver.Chrome(service=service_obj)
# max time out is work is completed in 2 sec then it proceed futher not wait for more 3 sec so we save 3 sec
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("i am learning selenium")
time.sleep(3)
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)
