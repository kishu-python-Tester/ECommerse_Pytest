import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.data import get_credentials
import logging

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

@pytest.fixture(scope="session")
def logger():
    """Configure logging for the test session."""
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

@pytest.fixture(scope="session")
def logged_in_browser(request):
    headless = request.config.getoption("--headless")
    options = Options()
    if headless:
        options.add_argument("--headless")

    # Correcting the instantiation of the Chrome WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        login_page = LoginPage(driver)
        login_page.open('https://signin.ebay.com/signin/')
        username, password = get_credentials()
        login_page.login(username, password)
        yield driver
    finally:
        driver.quit()
