import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# if we want to add more browser then:
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")  # for addoption
    if browser_name == "chrome":
        service_obj = Service("/home/sanjoli/")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("/home/sanjoli/geckodriver")
        driver = webdriver.Firefox(service=service_obj)
     elif browser_name == "IE":
        service_obj = Service("/home/sanjoli/msedgedriver/")
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver  # this is a class variable
    yield
    driver.close()

