import pytest
import string
import random
import requests
from selenium.webdriver import Firefox
from playwright.sync_api import Page, sync_playwright

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = self.page.locator('[data-test="search-query"]')
        self.search_button = self.page.locator('[data-test="search-submit"]')
        self.product_cards = self.page.locator('.card')
        self.product_titles = self.page.locator('.card-title')
        self.product_prices = self.page.locator('[data-test="product-price"]')

    def goto(self):
        self.page.goto('https://practicesoftwaretesting.com/#/')
        self.page.wait_for_load_state('networkidle')

    def search_for_product(self, product_name: str):
        self.search_input.fill(product_name)
        self.search_button.click()
        self.page.wait_for_timeout(2000)

    def filter_by_category(self, category_name: str):
        self.page.get_by_label(category_name).check()
        self.page.wait_for_timeout(1500)

    def get_all_product_titles(self) -> list[str]:
        return self.product_titles.all_inner_texts()

    def get_all_product_prices(self) -> list[float]:
        price_texts = self.product_prices.all_inner_texts()
        return [float(price.replace('$', '').strip()) for price in price_texts if price.strip()]

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

@pytest.fixture(scope='function')
def home_page():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=True)
        context = browser.new_context()
        yield HomePage(context.new_page())