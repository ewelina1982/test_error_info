import pytest
import time
from config.config import config
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.store_page import StorePage
from pages.log_in_page import LogInPage


@pytest.mark.usefixtures("driver")
class TestCheckError:
    def test_check_error(self):
        home_page = HomePage(self.driver).open()
        home_page.menu.open_my_account_page()
        #
        # store_page.footer.click_dismiss_button()
        log_in_page = LogInPage(self.driver).wait_for_page_to_load()
        log_in_page.username_fill_field().password_fill_field()
        log_in_page.click_button_submit()
        log_in_page.check_locator_exist()

        home_page.menu.open_store_page()

        store_page = StorePage(self.driver).wait_for_page_to_load()
        store_page.footer.click_dismiss_button()
        store_page.click_add_first_product().click_add_second_product()
        store_page.check_button_exist()
        store_page.click_basket()

        cart_page = CartPage(self.driver).wait_for_page_to_load()
        cart_page.check_length_list_products_in_basket()
        cart_page.remove_first_product()
        cart_page.check_info_about_remove_exist()
        cart_page.click_button_go_to_pay()

        order_page = OrderPage(self.driver).wait_for_page_to_load()
        order_page.clear_input_email()
        order_page.click_button_pay().check_info_exist()

