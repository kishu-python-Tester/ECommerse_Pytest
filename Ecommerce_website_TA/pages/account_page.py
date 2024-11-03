from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.data_models import *
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class Account_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.account_button = (By.XPATH, "//button[@class='gh-ua gh-control']")
        self.search_cart = (By.ID, "gh-ac")
        self.search_button = (By.ID, "gh-btn")
        self.search_elements_options = "//div[@class='s-item__title']/span"
        self.first_item = (By.XPATH, "(//div[@class='s-item__title']/span)[2]")
        self.add_to_cart_options = [
            (By.XPATH, "//span[text()='View in cart']"),
            (By.XPATH, "//span[text()='Add to cart']")
        ]
        self.categories = (By.ID, 'gh-cat')
        self.categories_txt = (By.XPATH, "//span[@class='b-pageheader__text']")
        self.items_cart_page_billing = "//div[@class='cart-summary-line-item']/*/*[" \
                                       "@class='text-display-span']/span/span"

    def check_account_login(self, account_name):
        account_button = self.wait_method(20, self.account_button)
        account_text = account_button.text
        return account_name in account_text

    def search_elements(self, name_of_product):
        search_input = self.wait_method(20, self.search_cart)
        search_input.send_keys(name_of_product)
        search_input.send_keys(Keys.RETURN)

        search_results = self.driver.find_elements(By.XPATH, self.search_elements_options)
        return search_results

    def add_element_to_cart(self, name_of_product):
        self.search_elements(name_of_product)
        first_item_search = self.wait_method(20, self.first_item)
        first_item_search.click()
        self.switch_to_new_window()

        for add_to_cart_option in self.add_to_cart_options:
            try:
                add_to_cart_button = self.wait_method(30, add_to_cart_option)
                add_to_cart_button.click()
                break
            except Exception as e:
                print(f"Could not click add to cart button with XPath {add_to_cart_option}: {e}")

    def select_categories(self, category):
        select_element = self.wait_method(20, self.categories)
        select = Select(select_element)
        select.select_by_visible_text(category)
        search_button = self.wait_method(5, self.search_button)
        search_button.click()

    def check_search_category(self, text_category):
        search_elem_actual_text = self.wait_method(5, self.categories_txt)
        if text_category.lower() in search_elem_actual_text.text.lower():
            return True
        else:
            return False

    def return_billing_summary(self):
        billing_fields_list = []
        billing_results = self.driver.find_elements(By.XPATH, self.items_cart_page_billing)
        for billing_fields in billing_results:
            billing_fields_list.append(billing_fields.text)
        return return_cart_items(billing_fields_list)



