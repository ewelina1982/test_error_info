from selenium.webdriver.common.by import By

from helpers.helpers import find_item_by_name
from pages.base_page import BasePage
from pages.regions.base_region import BaseRegion
from pages.regions.menu_region import MenuRegion


class StorePage(BasePage):
    # URL_TEMPLATE = "https://tapsshop.pl/?post_type=product"
    _products_list = (By.CSS_SELECTOR, "ul[class='products columns-4']")
    _product = (By.CSS_SELECTOR, "li[class*='product type-product']")
    _name1 = (By.CSS_SELECTOR, "h2[class*='woocommerce-loop-product']")
    _first_product = (By.XPATH, "(//li[contains(@class, 'product type-product')]//a/following-sibling::a)[1]")
    _second_product = (By.XPATH, "(//li[contains(@class, 'product type-product')]//a/following-sibling::a)[2]")
    _basket = (By.CSS_SELECTOR, "a[class='cart-contents']")
    _see_basket_button = (By.XPATH, "(//a[@title='Zobacz koszyk'])[2]")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._products_list)

    @property
    def items(self):
        test = self.find_elements(*self._product)
        # for i in test:
        #     print(i.text)

        # print(test)
        return [Item(self, product) for product in self.find_elements(*self._product)]

    def add_item_to_cart(self, item_name):
        find_item_by_name(self.items, item_name).click_add_to_card_button()
        menu = MenuRegion(self)
        self.wait.until(lambda page: menu.amount != "0,00", "Amount is equal to 0,00, after adding item to card")

    def click_add_first_product(self):
        self.find_element(*self._first_product).click()
        return self

    def check_button_exist(self):
        print('test')
        element_exist = bool(self.wait.until(self.ec.visibility_of_element_located(self._see_basket_button)))
        assert element_exist == True

    def click_add_second_product(self):
        self.find_element(*self._second_product).click()
        return self

    def click_basket(self):
        self.find_element(*self._basket).click()
        return self


class Item(BaseRegion):
    _name = (By.CSS_SELECTOR, "h2[class*='woocommerce-loop-product']")
    _add_to_card_button = (By.CSS_SELECTOR, "a[class*='add_to_cart_button']")

    @property
    def name(self):
        # print("test3" + self.find_element(*self._name).text)
        return self.find_element(*self._name).text

    def click_add_to_card_button(self):
        self.find_element(*self._add_to_card_button).click()
