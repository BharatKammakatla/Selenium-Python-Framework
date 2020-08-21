import pytest
import os
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="/Users/bharatkammakatla/TestAutomation/SeleniumPythonFramework/resources/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path="/Users/bharatkammakatla/TestAutomation/SeleniumPythonFramework/resources/geckodriver")
    elif browser_name == "ie":
        driver = webdriver.Ie(
            executable_path="/Users/bharatkammakatla/TestAutomation/SeleniumPythonFramework/resources/IEDriverServer.exe")

    driver.get("http://demoaut.katalon.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
