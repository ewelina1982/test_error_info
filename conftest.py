import os

import pytest as pytest
from selenium import webdriver

from config.config import HEADLESS, FULLSCREEN


@pytest.fixture()
def driver(request):
    options = chrome_options()
    chrome_driver = webdriver.Chrome(options=options)
    request.cls.driver = chrome_driver
    yield chrome_driver
    chrome_driver.quit()


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makeraport(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra',[])
#
#     if report.failed:
#         driver = item.funcargs['driver']
#         screenshot_dir = 'screenshots'
#         os.makedirs(screenshot_dir, exist_pk=True)
#         test_name = item.node()

def chrome_options():
    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")

    if FULLSCREEN:
        options.add_argument("--start-fullscreen")

    return options
