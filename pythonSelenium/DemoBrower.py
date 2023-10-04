import service as service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver
# service_obj = Service("/home/sanjoli/")
# driver = webdriver.Chrome(service=service_obj)

service_obj = Service("/home/sanjoli/geckodriver")
driver = webdriver.Firefox(service=service_obj)

# service_obj = Service("/home/sanjoli/msedgedriver/")
# driver = webdriver.Edge(service=service_obj)



driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
driver.get("https://sanginijewellers.com/")
driver.maximize_window()
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
