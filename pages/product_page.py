from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_correct_product_in_success_message(self, product_name):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == success_message, f"Expected product name '{product_name}' but got '{success_message}'"

    def should_be_correct_price_in_basket(self, product_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Expected basket total '{product_price}' but got '{basket_total}'"
