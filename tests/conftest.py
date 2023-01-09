import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1280
    browser.config.window_height = 900
    yield
    browser.quit()
