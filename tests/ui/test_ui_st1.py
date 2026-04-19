from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, text_to_be_present_in_element_value, new_window_is_opened

# NOTE In the newest version, register page automatically selects address data upon entering postal code. Tests were adjusted accordingly.
# NOTE To ensure that tests pass on each run, an automatically generated email is used instead of hardcoded one. This prevents `email already used` errors.
# NOTE In some tests, assertion is implicit, as stuff like WebDriverWait will throw an exception when test is malformed

def test_pt1_1(driver: Firefox, random_email: str):
    # arrange
    driver.get('https://practicesoftwaretesting.com/auth/register')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'first_name')))

    driver.find_element(By.ID, 'first_name').send_keys('foo')
    driver.find_element(By.ID, 'last_name').send_keys('bar')
    driver.find_element(By.ID, 'dob').send_keys('2000-01-01')
    driver.find_element(By.ID, 'country').send_keys('Poland')
    driver.find_element(By.ID, 'postal_code').send_keys('15-640')
    driver.find_element(By.ID, 'house_number').send_keys('17')

    # NOTE We wait after entering house number and postal code until page fills in rest of the address
    WebDriverWait(driver, 3.0).until(text_to_be_present_in_element_value((By.ID, 'street'), 'Staromiejska 17'))

    driver.find_element(By.ID, 'phone').send_keys('2137')
    driver.find_element(By.ID, 'email').send_keys(random_email)
    driver.find_element(By.ID, 'password').send_keys('Poziomka13.')

    # act
    driver.find_element(By.XPATH, '//button[@data-test=\'register-submit\']').click()

    # assert
    WebDriverWait(driver, 3.0).until(lambda _driver: _driver.current_url == 'https://practicesoftwaretesting.com/auth/login')

def test_pt1_2(driver: Firefox, random_email: str):
    # arrange
    driver.get('https://practicesoftwaretesting.com/auth/register')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'first_name')))

    driver.find_element(By.ID, 'first_name').send_keys('foo')
    driver.find_element(By.ID, 'last_name').send_keys('bar')
    driver.find_element(By.ID, 'dob').send_keys('2000-01-01')
    driver.find_element(By.ID, 'country').send_keys('Poland')
    driver.find_element(By.ID, 'postal_code').send_keys('15-640')
    driver.find_element(By.ID, 'house_number').send_keys('17')

    # NOTE We wait after entering house number and postal code until page fills in rest of the address
    WebDriverWait(driver, 3.0).until(text_to_be_present_in_element_value((By.ID, 'street'), 'Staromiejska 17'))

    driver.find_element(By.ID, 'phone').send_keys('2137')
    driver.find_element(By.ID, 'email').send_keys(random_email)
    driver.find_element(By.ID, 'password').send_keys('Poziomka13.')
    driver.find_element(By.XPATH, '//button[@data-test=\'register-submit\']').click()

    WebDriverWait(driver, 3.0).until(lambda _driver: _driver.current_url == 'https://practicesoftwaretesting.com/auth/login')

    driver.get('https://practicesoftwaretesting.com/auth/register')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'first_name')))

    driver.find_element(By.ID, 'first_name').send_keys('foo')
    driver.find_element(By.ID, 'last_name').send_keys('bar')
    driver.find_element(By.ID, 'dob').send_keys('2000-01-01')
    driver.find_element(By.ID, 'country').send_keys('Poland')
    driver.find_element(By.ID, 'postal_code').send_keys('15-640')
    driver.find_element(By.ID, 'house_number').send_keys('17')

    # NOTE We wait after entering house number and postal code until page fills in rest of the address
    WebDriverWait(driver, 3.0).until(text_to_be_present_in_element_value((By.ID, 'street'), 'Staromiejska 17'))

    driver.find_element(By.ID, 'phone').send_keys('2137')
    driver.find_element(By.ID, 'email').send_keys(random_email)
    driver.find_element(By.ID, 'password').send_keys('Poziomka13.')

    # act
    driver.find_element(By.XPATH, '//button[@data-test=\'register-submit\']').click()

    # assert
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[@data-test=\'register-error\']')))

def test_pt1_3(driver: Firefox):
    # arrange
    driver.get('https://practicesoftwaretesting.com/auth/login')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.CLASS_NAME, 'google-sign-in-button')))

    old_handles = driver.window_handles

    # act
    driver.find_element(By.CLASS_NAME, 'google-sign-in-button').click()

    # NOTE We aren't going to check if a real google sign-in works as it would require using already existing session on the user machine, or dedicated google account

    # assert
    WebDriverWait(driver, 3.0).until(new_window_is_opened(old_handles))