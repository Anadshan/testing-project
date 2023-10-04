from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
# for head and headless mode we ude Chromeoptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-error")


# chrome driver
service_obj = Service("/home/sanjoli/chromedriver")
driver: WebDriver = webdriver.Chrome(service=service_obj, options=chrome_options)
# max time out is work is completed in 2 sec then it proceed futher not wait for more 3 sec so we save 3 sec
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")

