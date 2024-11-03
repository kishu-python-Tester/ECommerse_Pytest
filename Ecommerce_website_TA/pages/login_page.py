from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, 'userid')
        self.password_input = (By.ID, 'pass')
        self.login_button = (By.ID, "sgnBt")
        self.continue_button = (By.ID, "signin-continue-btn")
        self.pass_key = (By.ID,"passkeys-cancel-btn")
        self.invalid_login_message =(By.ID,"signin-error-msg")
        self.invalid_password_message =(By.ID,"errormsg")



    def wait_method(self, timeout, element_path):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(element_path))


    def enter_username(self,username):
        username_input = self.wait_method(20, self.username_input)
        username_input.send_keys(username)


    def click_continue_button(self):
        continue_button = self.wait_method(5, self.continue_button)
        continue_button.click()



    def login(self, username, password):
        self.enter_username(username)
        self.click_continue_button()
        password_input = self.wait_method(20, self.password_input)
        password_input.send_keys(password)
        login_button = self.wait_method(20, self.login_button)
        login_button.click()
        try:
             self.wait_method(20, self.pass_key).click()
        except:
            pass

    def account_invalid_login_message(self,user_name='',password=''):
        if user_name:
            invalid_login_actual = self.wait_method(20,self.invalid_login_message)

        elif password:
            invalid_login_actual = self.wait_method(20, self.invalid_password_message)

        return invalid_login_actual.text




