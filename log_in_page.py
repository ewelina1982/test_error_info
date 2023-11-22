from selenium.webdriver.common.by import By

from helpers.helpers import find_item_by_name
from pages.base_page import BasePage


from pages.regions.base_region import BaseRegion
from pages.regions.menu_region import MenuRegion


class LogInPage(BasePage):
    _entry_little = (By.CSS_SELECTOR, "h1[class='entry-title']")
    _username_input = (By.CSS_SELECTOR, "input[id='username']")
    _password_input = (By.CSS_SELECTOR, "input[id='password']")
    _button_log_in = (By.CSS_SELECTOR, "button[value='Zaloguj się']")
    _navigation = (By.CSS_SELECTOR, "nav[class='woocommerce-MyAccount-navigation']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._entry_little)

    def username_fill_field(self):
        self.wait.until(self.ec.visibility_of_element_located(self._username_input)).send_keys('cotaga1249@maillei.net')
        return self

    def password_fill_field(self):
        self.wait.until(self.ec.visibility_of_element_located(self._password_input)).send_keys('VRrMhK8MqFyd')
        return self

    def click_button_submit(self):
        return self.find_element(*self._button_log_in).click()

    def check_locator_exist(self):
        print('test')
        element_exist = bool(self.wait.until(self.ec.visibility_of_element_located(self._navigation)))
        assert element_exist == True




