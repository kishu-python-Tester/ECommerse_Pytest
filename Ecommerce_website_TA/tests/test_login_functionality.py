
from pages.account_page import Account_page
import allure
from utils.data import get_credentials
from pages.login_page import LoginPage
import pytest
from selenium import webdriver

'''
Verifying who ever the account holder logged 
'''

@allure.feature("Login  functionality")
@allure.story("Successful Login")
def test_valid_login(logged_in_browser,logger):
    logger.info('Logging with username and password from Config file')
    logger.info('Logging to ebay website')
    account_page = Account_page(logged_in_browser)
    assert account_page.check_account_login('Ravi') == True
    logger.info('Check with account holder name after sucessfull loging')


@allure.feature("Login functionality")
@allure.story("Wrong username Login unsuccessful")
def test_invalid_username(logger):
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open('https://signin.ebay.com/signin/')
    username, password = get_credentials()
    logger.info('Logging with wrong username ')
    login_page.enter_username(username + 'XXX')
    login_page.click_continue_button()
    assert "we couldn't find this ebay account." in (login_page.account_invalid_login_message(user_name=True)).lower()
    logger.info('Check with validation message proper or not ')
    driver.quit()

@allure.feature("Login functionality")
@allure.story("No username Login unsuccessful")
def test_no_username(logger):
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open('https://signin.ebay.com/signin/')
    login_page.click_continue_button()
    logger.info('With out enter username click the submit button')
    assert "not a match." in (login_page.account_invalid_login_message(user_name=True)).lower()
    logger.info('Check with validation message proper or not ')
    driver.quit()

