from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "The basket is not empty"

    def should_be_basket_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "The basket is empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "The empty basket message is not present"

    def should__be_continue_shopping_link(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), "The continue shopping link is not present"


