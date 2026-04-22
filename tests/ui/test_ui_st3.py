from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, text_to_be_present_in_element, visibility_of_all_elements_located
from selenium.webdriver.common.action_chains import ActionChains

def test_pt_3_1(driver: Firefox):
    driver.get('https://practicesoftwaretesting.com/')

    search_text = 'Saw'
    
    search_query_input: WebElement = WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'search-query')))
    search_query_input.send_keys(search_text)

    search_button: WebElement = WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//button[@data-test=\'search-submit\']')))
    search_button.click()

    search_term: WebElement = WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//span[@data-test=\'search-term\']')))
    assert search_term.text == search_text

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[@data-test=\'search_completed\']')))
    
    product_titles: list[WebElement] = WebDriverWait(driver, 3.0).until(visibility_of_all_elements_located((By.XPATH, '//*[@data-test=\'product-name\']')))
    assert all(search_text.lower() in x.text.lower() for x in product_titles)

def test_pt_3_2(driver: Firefox):
    driver.get('https://practicesoftwaretesting.com/')

    category_input: WebElement = WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//label[contains(text(), \'Power Tools\')]/input')))
    category_input.click()

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[@data-test=\'filter_completed\']')))
    
    product_titles: list[WebElement] = WebDriverWait(driver, 3.0).until(visibility_of_all_elements_located((By.XPATH, '//*[@data-test=\'product-name\']')))
    assert len(product_titles) > 0
    assert not any('pliers' in x.text.lower() for x in product_titles)    

def test_pt_3_3(driver: Firefox):
    driver.get('https://practicesoftwaretesting.com/')
    
    price_slider: WebElement = WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.CLASS_NAME, 'ngx-slider-pointer-max')))
    price_slider_bar: WebElement = WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//span[contains(@class, \'ngx-slider-full-bar\')]')))

    driver.execute_script('arguments[0].scrollIntoView();', price_slider)

    ActionChains(driver).drag_and_drop_by_offset(
        price_slider,
        -price_slider_bar.rect['width'] / 4,
        0).perform()
    
    driver.implicitly_wait(3.0)
    
    max_price_label: WebElement = WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//span[contains(@class, \'ngx-slider-model-high\')]')))
    max_price = int(max_price_label.text.strip())

    driver.implicitly_wait(3.0)
    
    product_prices: list[WebElement] = WebDriverWait(driver, 3.0).until(visibility_of_all_elements_located((By.XPATH, '//*[@data-test=\'product-price\']')))
    assert all(float(x.text[1:]) <= max_price for x in product_prices)