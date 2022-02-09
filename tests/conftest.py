import pytest
import allure
from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.config.browser import BrowserConfig
from tests.config.browser import Grid


def pytest_addoption(parser):
    parser.addoption("--grid_port", action="store", default=Grid.GRID_PORT,
                     help="Port of remote connection")


@pytest.fixture(scope="session")
def create_browser(request):

    with allure.MASTER_HELPER.step("Creating a browser session from a config file"):
        browser = BrowserConfig.BROWSER
        Logger.info("Browser = " + browser)
        Browser.get_browser().set_up_driver(browser_key=browser, grid_port=request.config.getoption('--grid_port'))
        Browser.get_browser().maximize(browser_key=browser)

    yield

    with allure.MASTER_HELPER.step("Closing sessions of all browsers"):
        for browser_key in list(Browser.get_browser().get_driver_names()):
            Browser.get_browser().quit(browser_key=browser_key)
