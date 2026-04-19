import pytest
import string
import random
import requests
from selenium.webdriver import Firefox

@pytest.fixture(scope='function')
def driver():
    _driver = Firefox()
    yield _driver

    _driver.quit()

@pytest.fixture(scope='function')
def random_email():
    return ''.join(random.choice(string.ascii_letters) for _ in range(8)) + '@gmail.com'

@pytest.fixture(scope='function')
def shopping_cart():
    response = requests.post('https://api.practicesoftwaretesting.com/carts')
    assert response.status_code == 201

    return response.json()['id']