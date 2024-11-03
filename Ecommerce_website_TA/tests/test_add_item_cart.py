import pytest
from pages.account_page import Account_page
import allure

@allure.feature("Add item cart Functionality")
@allure.story("Successful item added cart")
def test_add_item_cart(logged_in_browser,logger):
    logger.info('Add the item in the cart and check wether it is adding correctly or not')
    account_page = Account_page(logged_in_browser)
    account_page.open('https://www.ebay.com/')
    browser = account_page.driver
    browser.maximize_window()
    logger.info('Search for the product and add to the cart')
    account_page.add_element_to_cart('Watch')
    assert "https://cart.payments.ebay.com/" in browser.current_url, \
        "URL doesn't match expected URL for cart page"
    logger.info('After adding to cart verify wether it is redirected to payment or not')

@allure.feature("Add item cart Functionality")
@allure.story("Successful add two items to cart")
def test_add_two_item_cart(logged_in_browser,logger):
    logger.info('Add more than one product and checking the qty of product')
    items_needed =['watch','purse']
    account_page = Account_page(logged_in_browser)
    for item in items_needed:
        account_page.open('https://www.ebay.com/')
        browser = account_page.driver
        browser.maximize_window()
        account_page.add_element_to_cart(item)
    cart_items = account_page.return_billing_summary()
    assert cart_items['items_count']>1
    logger.info('Assert the items count',cart_items)