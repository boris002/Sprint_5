import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BLOCK_LOGIN_FORM, BLOCK_PERSONAL_ACCOUNT, BUTTON_LOGIN, BUTTON_PERSONAL_ACCOUNT, INPUT_LOGIN_EMAIL, INPUT_LOGIN_PASSWORD, LOGO_STELLAR, TEXT_CONSTRUCTOR_PAGE
from data import VALID_EMAIL, VALID_PASSWORD

class TestPersonalAccount:
 def test_open_personal_account(self,driver):
    # Открываем форму авторизации
    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
    # Вводим email и пароль
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(INPUT_LOGIN_EMAIL)).send_keys(VALID_EMAIL)
    driver.find_element(*INPUT_LOGIN_PASSWORD).send_keys(VALID_PASSWORD)
    driver.find_element(*BUTTON_LOGIN).click()
    # Ждём
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BUTTON_PERSONAL_ACCOUNT))
    # Переходим в личный кабинет
    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
    # Проверяем, что блок личного кабинета отображается
    personal_account_block = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BLOCK_PERSONAL_ACCOUNT))
    assert personal_account_block.is_displayed()

 def test_go_to_constructor_via_logo(self, driver):
    # Авторизация
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT)).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(INPUT_LOGIN_EMAIL)).send_keys(VALID_EMAIL)
    driver.find_element(*INPUT_LOGIN_PASSWORD).send_keys(VALID_PASSWORD)
    driver.find_element(*BUTTON_LOGIN).click()

    # Ждём появления кнопки "Личный кабинет" (логин прошёл)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BUTTON_PERSONAL_ACCOUNT))

    # Переходим в личный кабинет
    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BLOCK_PERSONAL_ACCOUNT))

    # Кликаем на логотип, чтобы вернуться в конструктор
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGO_STELLAR)).click()

    # Проверяем, что открылся конструктор
    constructor_page = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TEXT_CONSTRUCTOR_PAGE))
    assert constructor_page.is_displayed()