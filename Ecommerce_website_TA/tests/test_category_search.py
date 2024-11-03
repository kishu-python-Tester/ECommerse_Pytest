import pytest
from pages.account_page import Account_page
import allure

@allure.feature("Search item functionality")
@allure.story("Category search")
def test_category_search(logged_in_browser,logger):
    logger.info('Select the category and see category results displayed correctly or not')
    account_page = Account_page(logged_in_browser)
    account_page.open('https://www.ebay.com/')
    browser = account_page.driver
    browser.maximize_window()
    account_page.select_categories('Books')
    assert account_page.check_search_category('Books') == True
    logger.info('Assert with category results displayed correctly or not')

