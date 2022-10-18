import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




@pytest.fixture
def browser():
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()



def test_A11_registration_redirect_by_click(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    browser.get(url)

    element = browser.find_element('xpath','//*[@id="kc-register"]')
    element.click()

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div > div > form')

def test_A10_displaying_the_registr_form(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    browser.get(url)

    element = browser.find_element('xpath','//*[@id="kc-register"]')
    element.click()

    assert browser.find_element('xpath', '//*[@id="page-right"]/div[1]/div[1]/h1[1]')

def test_A13_registration_name_on_english(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'
    FIRSTName = 'ivan'

    browser.get(url)

    element = browser.find_element('xpath', '//*[@id="kc-register"]')
    element.click()

    input_field = browser.find_element(by=By.NAME, value='firstName')
    input_field.send_keys(FIRSTName)

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div > div > form > div > div > span')

def test_A37_registration_last_name_on_english(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    LASTName = 'ivanov'

    browser.get(url)

    element = browser.find_element('xpath', '//*[@id="kc-register"]')
    element.click()

    input_field = browser.find_element(by=By.NAME, value='lastName')
    input_field.send_keys(LASTName)

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div > div > form > div > div > span')

def test_A38_registration_unvalid_email(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'
    email = 'testqap78gmail.com'

    browser.get(url)

    element = browser.find_element('xpath','//*[@id="kc-register"]')
    element.click()

    btn_input = browser.find_element(by=By.ID, value='address')
    btn_input.send_keys(email)

    input = browser.find_element(by=By.ID, value='password')
    input.click()

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div > div > form > div:nth-of-type(3) > span')

def test_A17_registration_unvalid_password(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'
    email = 'testqap78gmail.com'
    password = 'asdfsd2sd'

    browser.get(url)

    element = browser.find_element('xpath','//*[@id="kc-register"]')
    element.click()

    input = browser.find_element(by=By.ID, value='password')
    input.send_keys(password)

    btn_input = browser.find_element(by=By.ID, value='address')
    btn_input.send_keys(email)

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')

def test_A19_registration_unmatched_passwords(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    FIRSTName = 'Иван'
    LASTName = 'Иванов'
    email = 'testQAP78@gmail.com'
    password = 'TestPassword22'
    password2 = 'TestPassword23'

    browser.get(url)

    element = browser.find_element('xpath','//*[@id="kc-register"]')
    element.click()

    btn_input = browser.find_element(by=By.NAME, value='firstName')
    btn_input.send_keys(FIRSTName)

    btn_input = browser.find_element(by=By.NAME, value='lastName')
    btn_input.send_keys(LASTName)

    btn_input = browser.find_element(by=By.ID, value='address')
    btn_input.send_keys(email)

    input = browser.find_element(by=By.ID, value='password')
    input.send_keys(password)

    input = browser.find_element(by=By.ID, value='password-confirm')
    input.send_keys(password2)

    element = browser.find_element(by=By.XPATH, value='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]')
    element.click()

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > span')

def test_A39_registration_matched_passwords(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    FIRSTName = 'Иван'
    LASTName = 'Иванов'
    email = 'testQAP79@gmail.com'
    password = 'TestPassword23'
    password2 = 'TestPassword23'

    browser.get(url)

    element = browser.find_element('xpath', '//*[@id="kc-register"]')
    element.click()

    btn_input = browser.find_element(by=By.NAME, value='firstName')
    btn_input.send_keys(FIRSTName)

    btn_input = browser.find_element(by=By.NAME, value='lastName')
    btn_input.send_keys(LASTName)

    btn_input = browser.find_element(by=By.ID, value='address')
    btn_input.send_keys(email)

    input = browser.find_element(by=By.ID, value='password')
    input.send_keys(password)

    input = browser.find_element(by=By.ID, value='password-confirm')
    input.send_keys(password2)

    element = browser.find_element(by=By.XPATH, value='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]')
    element.click()

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div > h1')

    assert browser.find_element(by=By.XPATH, value='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]')

def test_A16_registration_with_7_letters_password(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'
    email = 'testqap78gmail.com'
    password = 'asdfW2f'

    browser.get(url)

    element = browser.find_element('xpath','//*[@id="kc-register"]')
    element.click()

    input = browser.find_element(by=By.ID, value='password')
    input.send_keys(password)

    btn_input = browser.find_element(by=By.ID, value='address')
    btn_input.send_keys(email)

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')

def test_A14_registration_with_existing_email(browser):

    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    FIRSTName = 'Иван'
    LASTName = 'Иванов'
    email = 'testqap78@gmail.com'
    password = 'TestPassword23'
    password2 = 'TestPassword23'

    browser.get(url)

    element = browser.find_element('xpath', '//*[@id="kc-register"]')
    element.click()

    btn_input = browser.find_element(by=By.NAME, value='firstName')
    btn_input.send_keys(FIRSTName)

    btn_input = browser.find_element(by=By.NAME, value='lastName')
    btn_input.send_keys(LASTName)

    btn_input = browser.find_element(by=By.ID, value='address')
    btn_input.send_keys(email)

    input = browser.find_element(by=By.ID, value='password')
    input.send_keys(password)

    input = browser.find_element(by=By.ID, value='password-confirm')
    input.send_keys(password2)

    element = browser.find_element(by=By.XPATH, value='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]')
    element.click()

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div > div > form > div > div > div > h2')
