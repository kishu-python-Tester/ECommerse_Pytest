import allure
from pages.account_page import Account_page

@allure.feature("Search item functionality")
@allure.story("Product search")
def test_product_search(logged_in_browser,logger):
    logger.info('Type one product in search bar')
    account_page = Account_page(logged_in_browser)
    account_page.open('https://www.ebay.com/')
    browser = account_page.driver
    browser.maximize_window()
    search_results = account_page.search_elements('PHONE')
    assert len(search_results) > 0, "No search results found"
    logger.info('Check with search results displayed or not')
    logger.info('Search for phone',search_results)


