from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import LINK_LOGIN_TO_REGISTER,BLOCK_LOGIN_FORM, BUTTON_PERSONAL_ACCOUNT, BUTTON_REGISTER, INPUT_EMAIL, INPUT_NAME, INPUT_PASSWORD, LINK_REGISTER_TO_LOGIN, TEXT_REGISTRATION_ERROR
from data import REG_NAME, REG_EMAIL, REG_PASSWORD, INVALID_PASSWORD

def test_success_registration(driver):
    # Переходим в личный кабинет
    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
    # Ждём появления ссылки "Зарегистрироваться" и кликаем
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LINK_LOGIN_TO_REGISTER)).click()
    # Ждём поля Имя и вводим данные
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(INPUT_NAME)).send_keys(REG_NAME)
    driver.find_element(*INPUT_EMAIL).send_keys(REG_EMAIL)
    driver.find_element(*INPUT_PASSWORD).send_keys(REG_PASSWORD)
    driver.find_element(*BUTTON_REGISTER).click()
    # Ждём появления формы авторизации (значит регистрация прошла)
    auth_form = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BLOCK_LOGIN_FORM))
    assert auth_form.is_displayed()

def test_registration_with_invalid_password(driver):
    # Переходим в личный кабинет
    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
    # Ждём появления ссылки "Зарегистрироваться" и кликаем
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LINK_LOGIN_TO_REGISTER)).click()
    # Ждём поля Имя и вводим данные
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(INPUT_NAME)).send_keys(REG_NAME)
    driver.find_element(*INPUT_EMAIL).send_keys(REG_EMAIL)
    driver.find_element(*INPUT_PASSWORD).send_keys(INVALID_PASSWORD)
    driver.find_element(*BUTTON_REGISTER).click()
    # Ждём появления текста ошибки
    error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TEXT_REGISTRATION_ERROR))
    assert error_message.is_displayed()