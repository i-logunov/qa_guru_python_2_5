import pytest
from selene.support.shared import browser


@pytest.fixture()
def set_browser_size():
    browser.config.window_width = 800
    browser.config.window_height = 600
    browser.config.hold_browser_open = True
