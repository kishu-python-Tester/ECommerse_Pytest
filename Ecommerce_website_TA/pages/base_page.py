from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://example.com'


    def open(self, url):
        self.driver.get(url)

    def wait_method(self, timeout, element_path):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(element_path))

    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:

            raise Exception(f"Element {locator} not found within {timeout} seconds.")

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def switch_to_new_window(self):
        window_handles = self.driver.window_handles
        new_window_handle = window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
