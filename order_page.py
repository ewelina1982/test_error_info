import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    _order_title = (By.CSS_SELECTOR, "h1[class='entry-title']")
    _input_email = (By.CSS_SELECTOR, "input[id='billing_email']")
    _button_pay_all_shop = (By.XPATH, "//button[@id='place_order']")
    _info_error = (By.CSS_SELECTOR, "ul[class='woocommerce-error']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._order_title)

    def clear_input_email(self):
        self.find_element(*self._input_email).clear()
        return self

    def click_button_pay(self):
        # tutaj mam problem przycisk widoczny a raz działa raz nie
        button_pay_now = self.find_element(*self._button_pay_all_shop)
        self.action.move_to_element(button_pay_now).perform()
        button_pay_now.click()
        return self

    def check_info_exist(self):
        info = bool(self.wait.until(self.ec.visibility_of_element_located(self._info_error)))
        assert info == True
