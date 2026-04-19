import pytest
import string
import random
from selenium.webdriver import Firefox

@pytest.fixture(scope='function')
def driver():
    _driver = Firefox()
    yield _driver

    _driver.quit()

@pytest.fixture(scope='function')
def random_email():
    return ''.join(random.choice(string.ascii_letters) for _ in range(8)) + '@gmail.com'