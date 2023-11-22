from selenium.webdriver.common.by import By

from helpers.helpers import find_item_by_name
from pages.base_page import BasePage
from pages.regions.base_region import BaseRegion


class CartPage(BasePage):
    _cart_title = (By.XPATH, "//h1[contains(text(), 'Koszyk')]")
    _product_in_the_cart = (By.CSS_SELECTOR, "tr[class*='cart_item']")
    _delivery_fee = (By.CSS_SELECTOR, "td[data-title='Wysyłka'] span[class*='Price-amount']")
    _vat = (By.CSS_SELECTOR, "td[data-title='VAT'] span[class*='Price-amount']")
    _order_total_amount = (By.CSS_SELECTOR, "td[data-title='Łącznie'] span[class*='Price-amount']")
    _checkout_button = (By.XPATH, "//a[@class='checkout-button button alt wc-forward wp-element-button']")
    _list_products = (By.CSS_SELECTOR, "tr[class='woocommerce-cart-form__cart-item cart_item']")
    _remove_first_product = (By.XPATH, "(//a[@class='remove'])[1]")
    _info_about_remove = (By.CSS_SELECTOR, "div[class='woocommerce-message']")
    _button_go_to_pay = (By.CSS_SELECTOR, "a[class*='checkout-button']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._cart_title)

    @property
    def items_in_the_cart(self):
        return [CartItem(self, product) for product in self.find_elements(*self._product_in_the_cart)]

    @property
    def delivery_fee(self):
        fee = self.find_element(*self._delivery_fee).text
        return fee[1:]

    def check_length_list_products_in_basket(self):
        list_products = len(self.find_elements(*self._list_products))
        assert list_products == 2

    @property
    def vat(self):
        vat_fee = self.find_element(*self._vat).text
        return vat_fee[1:]

    @property
    def order_total_amount(self):
        total_amount = self.find_element(*self._order_total_amount).text
        return total_amount[1:]

    def assert_item_data(self, item_name, item_unit_price, quantity="1", total_price=None):
        if total_price is None:
            total_price = item_unit_price

        item = find_item_by_name(self.items_in_the_cart, item_name)

        assert item.item_unit_price == item_unit_price
        assert item.quantity == quantity
        assert item.item_total_price == total_price

    def click_checkout_button(self):
        self.find_element(*self._checkout_button).click()
        return self

    def remove_first_product(self):
        self.find_element(*self._remove_first_product).click()
        return self

    def check_info_about_remove_exist(self):
        info = bool(self.wait.until(self.ec.visibility_of_element_located(self._info_about_remove)))
        assert info == True

    def click_button_go_to_pay(self):
        button_pay = self.find_element(*self._button_go_to_pay)
        self.action.move_to_element(button_pay).perform()
        button_pay.click()
        return self


class CartItem(BaseRegion):
    _name = (By.CSS_SELECTOR, "td[class*='product-name']")
    _item_unit_price = (By.CSS_SELECTOR, "td[class*='product-price']")
    _quantity = (By.CSS_SELECTOR, "td[class*='product-quantity'] input[title='Ilość']")
    _item_total_price = (By.CSS_SELECTOR, "td[class*='product-subtotal']")

    @property
    def name(self):
        return self.find_element(*self._name).text

    @property
    def item_unit_price(self):
        price = self.find_element(*self._item_unit_price).text
        return price[1:]

    @property
    def quantity(self):
        item_quantity = self.find_element(*self._quantity)
        return item_quantity.get_attribute("value")

    @property
    def item_total_price(self):
        price = self.find_element(*self._item_total_price).text
        return price[1:]
