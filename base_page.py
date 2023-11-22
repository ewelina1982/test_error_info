from pypom import Page
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import config
from pages.regions.footer_region import FooterRegion
from pages.regions.menu_region import MenuRegion


class LogInRegion:
    pass


class BasePage(Page):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)
        self.base_url = config.BASE_URL
        self.wait = WebDriverWait(driver,config.MAX_WAIT)
        self.ec = ec
        self.action = ActionChains(driver)

    @property
    def menu(self):
        return MenuRegion(self)

    @property
    def footer(self):
        return FooterRegion(self)






