import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
service_obj = Service("/home/sanjoli/chromedriver")
driver:

# chrome driver
service_obj = Service("/home/sanjoli/chromedriver")
driver: WebDriver = webdriver.Chrome(service=service_obj)
# max time out is work is completed in 2 sec then it proceed futher not wait for more 3 sec so we save 3 sec
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windowOpened = driver.window_handles
driver.switch_to.window(windowOpened[1])
message = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
# emailLink = message[19:49]
var = message.split("at")[1].strip().split(" ")[0]
print(var)
driver.switch_to.window(windowOpened[0])
driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.XPATH, "//span[text()='Admin']").click()
clickButtons = driver.find_elements(By.CSS_SELECTOR, ".form-check-inline label")
time.sleep(5)
print(len(clickButtons))
for clickButton in clickButtons:
    if clickButton.get_attribute("id") == "usertype":
        clickButton.click()
        time.sleep(10)
        assert clickButton.is_selected()
        break





