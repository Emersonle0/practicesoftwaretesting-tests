from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, text_to_be_present_in_element


def test_pt_2_1(driver: Firefox):
    # arrange
    driver.get('https://practicesoftwaretesting.com/')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[contains(@class, \'container\') and @data-test]')))

    cards_container = driver.find_element(By.XPATH, '//div[contains(@class, \'container\') and @data-test]')
    card = cards_container.find_elements(By.CLASS_NAME, 'card')[0]
    card.click()

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'btn-add-to-cart')))

    # act
    driver.find_element(By.ID, 'btn-add-to-cart').click()

    # assert
    WebDriverWait(driver, 3.0).until(text_to_be_present_in_element((By.ID, 'lblCartCount'), '1'))

    driver.get('https://practicesoftwaretesting.com/checkout')

    # NOTE This serves as an assert as this span only exists when any product is present in the cart
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//span[@data-test=\'product-title\']')))

def test_pt_2_2(driver: Firefox):
    # arrange
    driver.get('https://practicesoftwaretesting.com/')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[contains(@class, \'container\') and @data-test]')))

    cards_container = driver.find_element(By.XPATH, '//div[contains(@class, \'container\') and @data-test]')
    card = cards_container.find_elements(By.CLASS_NAME, 'card')[0]
    card.click()

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'btn-add-to-cart')))

    driver.find_element(By.ID, 'btn-add-to-cart').click()

    WebDriverWait(driver, 3.0).until(text_to_be_present_in_element((By.ID, 'lblCartCount'), '1'))

    driver.get('https://practicesoftwaretesting.com/checkout')

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//span[@data-test=\'product-title\']/../..//a[contains(@class, \'btn\')]')))

    # act
    driver.find_element(By.XPATH, '//span[@data-test=\'product-title\']/../..//a[contains(@class, \'btn\')]').click()

    # assert
    WebDriverWait(driver, 3.0).until_not(visibility_of_element_located((By.XPATH, '//button[@data-test=\'proceed-1\']')))

def test_pt_2_3(driver: Firefox):
    # arrange
    driver.get('https://practicesoftwaretesting.com/')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[contains(@class, \'container\') and @data-test]')))

    cards_container = driver.find_element(By.XPATH, '//div[contains(@class, \'container\') and @data-test]')
    card = cards_container.find_elements(By.CLASS_NAME, 'card')[0]
    card.click()

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'quantity-input')))

    # act
    element = driver.find_element(By.ID, 'quantity-input')
    element.clear()
    element.send_keys('-')

    # assert
    assert element.get_attribute('value') == '1'