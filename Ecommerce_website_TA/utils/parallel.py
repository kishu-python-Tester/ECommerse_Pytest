import pytest
from selenium import webdriver

# Your parallel execution code here

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    yield driver
    driver.quit()