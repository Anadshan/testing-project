import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# chrome driver
service_obj = Service("/home/sanjoli/chromedriver")
driver: WebDriver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
