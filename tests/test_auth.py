import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



@pytest.fixture
def browser():
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

def test_A07_displaying_email_form_in_auth_form(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    browser.get(url)

    element = browser.find_element('xpath','//*[@id="t-btn-tab-mail"]')
    element.click()

    assert browser.find_element('xpath', '//*[@id="username"]')

def test_A06_displaying_number_form_in_auth_form(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    browser.get(url)

    element = browser.find_element('xpath','//*[@id="t-btn-tab-phone"]')
    element.click()

    assert browser.find_element('xpath', '//*[@id="username"]')

def test_A08_displaying_login_form_in_auth_form(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    browser.get(url)

    element = browser.find_element('xpath', '//*[@id="t-btn-tab-login"]')
    element.click()

    assert browser.find_element('xpath', '//*[@id="username"]')

def test_A09_displaying_personnel_account_form_in_auth_form(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    browser.get(url)

    element = browser.find_element('xpath', '//*[@id="t-btn-tab-ls"]')
    element.click()

    assert browser.find_element('xpath', '//*[@id="username"]')

def test_A01_displaying_the_auth_form(browser):
    url = 'https://b2c.passport.rt.ru/account_b2c/page'

    browser.get(url)

    assert browser.find_element(by=By.CSS_SELECTOR, value='section#page-right > div > div')

    assert browser.find_element('xpath', '//*[@id="page-right"]/div[1]/div[1]/h1[1]')

def test_A21_valid_authorization(browser):

    URL = 'https://b2c.passport.rt.ru/account_b2c/page'
    auth_login = 'testqap78@gmail.com'
    auth_password = 'QapTest45'

    browser.get(URL)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(auth_login + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(auth_password + Keys.RETURN)

def test_A25_unvalid_password_authorization(browser):

    URL = 'https://b2c.passport.rt.ru/account_b2c/page'
    auth_login = 'testqap78@gmail.com'
    auth_password = 'QapTes234'

    browser.get(URL)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(auth_login + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(auth_password + Keys.RETURN)

    assert browser.find_element('xpath', '//*[@id="page-right"]/div[1]/div[1]/p[1]')

def test_A30_unvalid_personal_account_auth(browser):

    URL = 'https://b2c.passport.rt.ru/account_b2c/page'
    auth_login = '12345678901234'  #лицевой счет
    auth_password = 'QapTest45'

    browser.get(URL)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(auth_login + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(auth_password + Keys.RETURN)

    assert browser.find_element('xpath', '//*[@id="page-right"]/div[1]/div[1]/p[1]')

def test_A31_unvalid_mobile_number_auth(browser):
    URL = 'https://b2c.passport.rt.ru/account_b2c/page'
    auth_login = '+79111110100'   #номер телефона
    auth_password = 'QapTest45'

    browser.get(URL)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(auth_login + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(auth_password + Keys.RETURN)

    assert browser.find_element('xpath', '//*[@id="page-right"]/div[1]/div[1]/p[1]')

def test_A29_unvalid_email_auth(browser):
    URL = 'https://b2c.passport.rt.ru/account_b2c/page'
    auth_login = 'testqap77@gmail.com'
    auth_password = 'QapTest45'

    browser.get(URL)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(auth_login + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(auth_password + Keys.RETURN)

    assert browser.find_element('xpath', '//*[@id="page-right"]/div[1]/div[1]/p[1]')

def test_A33_unvalid_email_password_auth(browser):
    URL = 'https://b2c.passport.rt.ru/account_b2c/page'
    auth_login = 'testqap7@gmail.com'
    auth_password = 'QapTest4'

    browser.get(URL)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(auth_login + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(auth_password + Keys.RETURN)

    assert browser.find_element('xpath', '//*[@id="page-right"]/div[1]/div[1]/p[1]')

def test_A34_unvalid_personal_account_password_auth(browser):
    URL = 'https://b2c.passport.rt.ru/account_b2c/page'
    auth_login = '12345678901234'
    auth_password = 'QapTest41'

    browser.get(URL)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(auth_login + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(auth_password + Keys.RETURN)

    assert browser.find_element('xpath', '//*[@id="page-right"]/div[1]/div[1]/p[1]')

def test_A35_phone_number_password_auth(browser):
    URL = 'https://b2c.passport.rt.ru/account_b2c/page'
    auth_login = '+79111111111'
    auth_password = 'QapTest41'

    browser.get(URL)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(auth_login + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(auth_password + Keys.RETURN)

    assert browser.find_element('xpath', '//*[@id="page-right"]/div[1]/div[1]/p[1]')
