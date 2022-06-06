import pytest

from framework.browser_factory import BrowserFactory


@pytest.fixture(scope='session')
def driver():
    yield BrowserFactory.get_driver()
